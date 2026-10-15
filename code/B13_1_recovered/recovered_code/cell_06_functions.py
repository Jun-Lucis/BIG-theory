# Computational functions copied verbatim; original notebook cell 6.

def logistic_kernel(delta_rad, kappa, c):
    z = kappa * (np.cos(2 * delta_rad) - c)
    z = np.clip(z, -60, 60)
    return 1.0 / (1.0 + np.exp(-z))

def fit_kernel_from_points(df, bin_width_deg=5.0):
    """
    Fit K_BIG(delta) = logistic[kappa*(cos(2delta)-c)]
    from rotated-basis selection points.
    """

    work = df.copy()
    work["delta"] = work["theta"] - work["alpha"]
    work["delta_deg"] = work["theta_deg"] - work["alpha_deg"]
    work["p_ref_delta"] = np.cos(work["delta"])**2
    work["delta_bin"] = (np.round(work["delta_deg"] / bin_width_deg) * bin_width_deg).astype(float)

    binned = (
        work
        .groupby("delta_bin", as_index=False)
        .agg(
            mean_p_plus=("p_plus", "mean"),
            std_p_plus=("p_plus", "std"),
            n=("p_plus", "count"),
            mean_ref=("p_ref_delta", "mean"),
        )
        .dropna(subset=["mean_p_plus"])
        .sort_values("delta_bin")
    )

    x_deg = binned["delta_bin"].to_numpy(dtype=float)
    y = binned["mean_p_plus"].to_numpy(dtype=float)
    x_rad = np.deg2rad(x_deg)

    y_cos2 = np.cos(x_rad)**2
    rmse_cos2_binned = float(np.sqrt(np.mean((y - y_cos2)**2)))

    if SCIPY_AVAILABLE:
        popt, _ = curve_fit(
            logistic_kernel,
            x_rad,
            y,
            p0=[3.0, 0.0],
            bounds=([0.01, -1.5], [50.0, 1.5]),
            maxfev=10000,
        )
    else:
        best = None
        for kappa in np.linspace(0.2, 25, 250):
            for c in np.linspace(-0.5, 0.5, 180):
                pred = logistic_kernel(x_rad, kappa, c)
                rmse = np.sqrt(np.mean((y - pred)**2))
                if best is None or rmse < best[0]:
                    best = (rmse, kappa, c)
        popt = np.array([best[1], best[2]])

    kappa, c = float(popt[0]), float(popt[1])
    y_fit = logistic_kernel(x_rad, kappa, c)
    rmse_kernel_binned = float(np.sqrt(np.mean((y - y_fit)**2)))

    raw_delta = work["delta"].to_numpy(dtype=float)
    raw_y = work["p_plus"].to_numpy(dtype=float)
    raw_rmse_cos2 = float(np.sqrt(np.mean((raw_y - np.cos(raw_delta)**2)**2)))
    raw_rmse_kernel = float(np.sqrt(np.mean((raw_y - logistic_kernel(raw_delta, kappa, c))**2)))

    return {
        "kappa": kappa,
        "c": c,
        "rmse_cos2_binned": rmse_cos2_binned,
        "rmse_kernel_binned": rmse_kernel_binned,
        "raw_rmse_cos2": raw_rmse_cos2,
        "raw_rmse_kernel": raw_rmse_kernel,
        "binned": binned,
        "work": work,
    }

def run_kernel_sharpness_scaling(
    seed=777,
    b_values=(0.5, 1.0, 2.0, 4.0),
    sigma_values=(0.20, 0.25, 0.35, 0.45, 0.60),
    alphas=(0.0, np.pi/8, np.pi/4),
    n_theta=19,
    n_trials=120,
    steps=300,
    a=4.0,
    eta=0.01,
):
    rng_master = np.random.default_rng(seed)

    theta_grid = np.linspace(0, np.pi/2, n_theta)

    all_points = []
    all_binned = []
    summary_rows = []

    total = len(b_values) * len(sigma_values)
    count = 0

    for b in b_values:
        for sigma in sigma_values:
            count += 1
            print("=" * 70)
            print(f"[{count}/{total}] Running b={b}, sigma={sigma}")

            rows = []

            # condition-specific rng for reproducibility
            condition_seed = int(rng_master.integers(0, 2**31 - 1))
            rng = np.random.default_rng(condition_seed)

            for alpha in alphas:
                for theta in theta_grid:
                    p_plus = simulate_rotated_basis_trials(
                        theta=theta,
                        alpha=alpha,
                        rng=rng,
                        a=a,
                        b=b,
                        sigma=sigma,
                        eta=eta,
                        steps=steps,
                        n_trials=n_trials,
                    )

                    p_ref = np.cos(theta - alpha)**2

                    rows.append({
                        "b": b,
                        "sigma": sigma,
                        "alpha": alpha,
                        "alpha_deg": alpha * 180 / np.pi,
                        "theta": theta,
                        "theta_deg": theta * 180 / np.pi,
                        "p_plus": p_plus,
                        "p_ref_cos2_theta_minus_alpha": p_ref,
                        "condition_seed": condition_seed,
                    })

            df_condition = pd.DataFrame(rows)

            fit = fit_kernel_from_points(df_condition, bin_width_deg=5.0)

            summary_rows.append({
                "b": b,
                "sigma": sigma,
                "kappa": fit["kappa"],
                "c": fit["c"],
                "rmse_cos2_binned": fit["rmse_cos2_binned"],
                "rmse_kernel_binned": fit["rmse_kernel_binned"],
                "raw_rmse_cos2": fit["raw_rmse_cos2"],
                "raw_rmse_kernel": fit["raw_rmse_kernel"],
                "condition_seed": condition_seed,
            })

            df_condition2 = fit["work"].copy()
            all_points.append(df_condition2)

            binned2 = fit["binned"].copy()
            binned2["b"] = b
            binned2["sigma"] = sigma
            binned2["kappa"] = fit["kappa"]
            binned2["c"] = fit["c"]
            all_binned.append(binned2)

            print(
                f"kappa={fit['kappa']:.4f}, c={fit['c']:+.4f}, "
                f"RMSE cos2={fit['rmse_cos2_binned']:.4f}, "
                f"RMSE kernel={fit['rmse_kernel_binned']:.4f}"
            )

    points_df = pd.concat(all_points, ignore_index=True)
    binned_df = pd.concat(all_binned, ignore_index=True)
    summary_df = pd.DataFrame(summary_rows)

    save_csv_local(points_df, "B13_2_kernel_scaling_all_points.csv")
    save_csv_local(binned_df, "B13_2_kernel_scaling_binned_curves.csv")
    save_csv_local(summary_df, "B13_2_kernel_scaling_summary.csv")

    # Pivot tables
    pivot_kappa = summary_df.pivot(index="b", columns="sigma", values="kappa")
    pivot_kernel_rmse = summary_df.pivot(index="b", columns="sigma", values="rmse_kernel_binned")
    pivot_cos2_rmse = summary_df.pivot(index="b", columns="sigma", values="rmse_cos2_binned")

    save_csv_local(pivot_kappa.reset_index(), "B13_2_kernel_scaling_kappa_pivot.csv")
    save_csv_local(pivot_kernel_rmse.reset_index(), "B13_2_kernel_scaling_kernel_rmse_pivot.csv")
    save_csv_local(pivot_cos2_rmse.reset_index(), "B13_2_kernel_scaling_cos2_rmse_pivot.csv")

    # Figure 1: kappa vs sigma for each b
    plt.figure(figsize=(7.5, 5.0))
    for b, sub in summary_df.groupby("b"):
        sub = sub.sort_values("sigma")
        plt.plot(sub["sigma"], sub["kappa"], marker="o", label=f"b={b}")
    plt.xlabel("noise sigma")
    plt.ylabel("kernel sharpness kappa")
    plt.title("B13.2 kernel sharpness vs noise")
    plt.legend()
    save_fig_local("B13_2_kernel_sharpness_vs_sigma.png")

    # Figure 2: kappa heatmap
    plt.figure(figsize=(7.0, 5.0))
    im = plt.imshow(
        pivot_kappa.values,
        origin="lower",
        aspect="auto",
        extent=[
            min(sigma_values), max(sigma_values),
            min(b_values), max(b_values)
        ],
    )
    plt.colorbar(im, label="kappa")
    plt.xlabel("noise sigma")
    plt.ylabel("barrier b")
    plt.title("B13.2 kernel sharpness kappa(b, sigma)")
    save_fig_local("B13_2_kernel_sharpness_heatmap.png")

    # Figure 3: kernel RMSE vs cos2 RMSE
    plt.figure(figsize=(7.5, 5.0))
    plt.scatter(summary_df["rmse_cos2_binned"], summary_df["rmse_kernel_binned"])
    lim_max = max(summary_df["rmse_cos2_binned"].max(), summary_df["rmse_kernel_binned"].max()) * 1.05
    plt.plot([0, lim_max], [0, lim_max], linestyle="--", linewidth=1)
    plt.xlabel("RMSE vs cos²(delta)")
    plt.ylabel("RMSE vs logistic kernel")
    plt.title("Kernel fit improvement over cos² reference")
    save_fig_local("B13_2_kernel_fit_improvement.png")

    # Figure 4: c parameter
    plt.figure(figsize=(7.5, 5.0))
    for b, sub in summary_df.groupby("b"):
        sub = sub.sort_values("sigma")
        plt.plot(sub["sigma"], sub["c"], marker="o", label=f"b={b}")
    plt.axhline(0, linestyle="--", linewidth=1)
    plt.xlabel("noise sigma")
    plt.ylabel("threshold offset c")
    plt.title("B13.2 fitted basin-boundary offset c")
    plt.legend()
    save_fig_local("B13_2_kernel_threshold_offset_c.png")

    # Summary JSON
    summary = {
        "experiment": "B13_2_kernel_sharpness_scaling",
        "description": (
            "Scans barrier b and noise sigma to fit the empirical BIG selection kernel "
            "K(delta)=1/(1+exp[-kappa*(cos(2delta)-c)])."
        ),
        "parameters": {
            "seed": seed,
            "a": a,
            "b_values": list(map(float, b_values)),
            "sigma_values": list(map(float, sigma_values)),
            "alphas_deg": [float(x * 180 / np.pi) for x in alphas],
            "n_theta": n_theta,
            "n_trials": n_trials,
            "steps": steps,
            "eta": eta,
        },
        "key_ranges": {
            "kappa_min": float(summary_df["kappa"].min()),
            "kappa_max": float(summary_df["kappa"].max()),
            "rmse_kernel_binned_min": float(summary_df["rmse_kernel_binned"].min()),
            "rmse_kernel_binned_max": float(summary_df["rmse_kernel_binned"].max()),
            "rmse_cos2_binned_min": float(summary_df["rmse_cos2_binned"].min()),
            "rmse_cos2_binned_max": float(summary_df["rmse_cos2_binned"].max()),
        },
        "interpretation": (
            "If kappa decreases with sigma, the transition is noise-softened. "
            "If kappa increases with barrier b, the basin boundary becomes sharper. "
            "Kernel RMSE should remain lower than cos² RMSE if the logistic basin-boundary "
            "kernel is the better explanatory object."
        ),
    }

    save_json_local(summary, "B13_2_kernel_sharpness_scaling_summary.json")

    print("B13.2 kernel sharpness scaling complete.")
    print(json.dumps(summary, indent=2))

    display(summary_df)

    return points_df, binned_df, summary_df, summary
