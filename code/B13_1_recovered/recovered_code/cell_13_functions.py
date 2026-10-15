# Computational functions copied verbatim; original notebook cell 13.

def make_angular_cloud(alpha_center, width_rad, n_samples, rng, radial_jitter=0.0):
    """
    Create a cloud of hidden-depth states around e_plus(alpha_center).

    angle = alpha_center + zeta, zeta ~ N(0, width_rad^2)
    h = r * (cos angle, sin angle)

    width_rad:
        angular spread of the post-selected cloud.
    radial_jitter:
        optional radial spread around unit norm.
    """
    angles = alpha_center + width_rad * rng.normal(size=n_samples)

    if radial_jitter > 0:
        radii = 1.0 + radial_jitter * rng.normal(size=n_samples)
        radii = np.clip(radii, 0.1, 3.0)
    else:
        radii = np.ones(n_samples)

    h = np.column_stack([
        radii * np.cos(angles),
        radii * np.sin(angles),
    ])

    return h, angles

def run_cloud_width_controlled_sequential_response(
    seed=1212,
    alpha1_values=(0.0, np.pi/12, np.pi/6),
    delta_values=(0.0, np.pi/12, np.pi/8, np.pi/6, np.pi/4),
    width_deg_values=(0.0, 2.5, 5.0, 7.5, 10.0, 12.5, 15.0, 20.0, 25.0, 30.0),
    n_cloud=600,
    steps2=350,
    a=4.0,
    b=1.0,
    sigma=0.35,
    eta=0.01,
    radial_jitter=0.0,
    logistic_kappa=None,
    logistic_c=None,
):
    """
    Artificial cloud-width test.

    For each alpha1 and cloud width w:
      1. Construct an artificial post-selected cloud around e_plus(alpha1).
      2. For each delta, evolve the cloud under basis alpha2=alpha1+delta.
      3. Estimate P(+_alpha2 | cloud around +_alpha1).
      4. Compare with cos²(delta) and B13.2 logistic kernel.

    This tests whether finite angular spread of the post-selected cloud can
    transform a logistic basin-boundary response into a cos²-like conditional response.
    """

    # Use B13.2 fitted kernel if available
    if logistic_kappa is None or logistic_c is None:
        try:
            sub = B13_2_summary[
                (np.isclose(B13_2_summary["b"], b)) &
                (np.isclose(B13_2_summary["sigma"], sigma))
            ]
            if len(sub) > 0:
                logistic_kappa = float(sub.iloc[0]["kappa"])
                logistic_c = float(sub.iloc[0]["c"])
            else:
                logistic_kappa = 3.691281
                logistic_c = -0.014286
        except Exception:
            logistic_kappa = 3.691281
            logistic_c = -0.014286

    print(f"Using logistic kernel kappa={logistic_kappa:.4f}, c={logistic_c:+.4f}")

    rng_master = np.random.default_rng(seed)

    rows = []
    cloud_diag_rows = []

    for width_deg in width_deg_values:
        width_rad = np.deg2rad(width_deg)

        for alpha1 in alpha1_values:
            # Make one cloud for this alpha1/width condition
            cloud_seed = int(rng_master.integers(0, 2**31 - 1))
            rng_cloud = np.random.default_rng(cloud_seed)

            h_cloud, angles = make_angular_cloud(
                alpha_center=alpha1,
                width_rad=width_rad,
                n_samples=n_cloud,
                rng=rng_cloud,
                radial_jitter=radial_jitter,
            )

            e_plus1, _ = basis_vectors(alpha1)
            centroid = np.mean(h_cloud, axis=0)
            centroid_norm = float(np.linalg.norm(centroid))
            mean_abs_alignment = float(np.mean(np.abs(h_cloud @ e_plus1)))
            std_abs_alignment = float(np.std(np.abs(h_cloud @ e_plus1)))
            angle_std_deg = float(np.std((angles - alpha1) * 180 / np.pi))

            cloud_diag_rows.append({
                "width_deg": width_deg,
                "width_rad": width_rad,
                "alpha1": alpha1,
                "alpha1_deg": alpha1 * 180 / np.pi,
                "cloud_seed": cloud_seed,
                "n_cloud": n_cloud,
                "centroid_x": centroid[0],
                "centroid_y": centroid[1],
                "centroid_norm": centroid_norm,
                "mean_abs_alignment": mean_abs_alignment,
                "std_abs_alignment": std_abs_alignment,
                "angle_std_deg": angle_std_deg,
            })

            print(
                f"width={width_deg:5.1f} deg, alpha1={alpha1*180/np.pi:5.1f} deg, "
                f"centroid_norm={centroid_norm:.4f}, angle_std={angle_std_deg:.2f}"
            )

            for delta in delta_values:
                alpha2 = alpha1 + delta

                # independent RNG for each evolution
                evolve_seed = int(rng_master.integers(0, 2**31 - 1))
                rng_evolve = np.random.default_rng(evolve_seed)

                h2, outcome2_plus = evolve_stage2_batch(
                    h0_batch=h_cloud,
                    alpha2=alpha2,
                    rng=rng_evolve,
                    a=a,
                    b=b,
                    sigma=sigma,
                    eta=eta,
                    steps=steps2,
                )

                p_plus = float(np.mean(outcome2_plus))
                ref_cos2 = float(np.cos(delta)**2)
                ref_logistic = float(K_logistic_delta(delta, kappa=logistic_kappa, c=logistic_c))

                rows.append({
                    "seed": seed,
                    "cloud_seed": cloud_seed,
                    "evolve_seed": evolve_seed,
                    "width_deg": width_deg,
                    "width_rad": width_rad,
                    "alpha1": alpha1,
                    "alpha1_deg": alpha1 * 180 / np.pi,
                    "alpha2": alpha2,
                    "alpha2_deg": alpha2 * 180 / np.pi,
                    "delta": delta,
                    "delta_deg": delta * 180 / np.pi,
                    "n_cloud": n_cloud,
                    "P_plus2": p_plus,
                    "ref_cos2_delta": ref_cos2,
                    "ref_logistic_delta": ref_logistic,
                    "error_cos2": p_plus - ref_cos2,
                    "error_logistic": p_plus - ref_logistic,
                    "centroid_norm": centroid_norm,
                    "angle_std_deg": angle_std_deg,
                })

    df = pd.DataFrame(rows)
    cloud_diag = pd.DataFrame(cloud_diag_rows)

    # Aggregate by cloud width
    by_width = (
        df
        .groupby("width_deg", as_index=False)
        .agg(
            rmse_cos2=("error_cos2", lambda x: float(np.sqrt(np.nanmean(np.asarray(x)**2)))),
            rmse_logistic=("error_logistic", lambda x: float(np.sqrt(np.nanmean(np.asarray(x)**2)))),
            mean_shift_cos2=("error_cos2", "mean"),
            mean_shift_logistic=("error_logistic", "mean"),
            max_abs_error_cos2=("error_cos2", lambda x: float(np.nanmax(np.abs(np.asarray(x))))),
            max_abs_error_logistic=("error_logistic", lambda x: float(np.nanmax(np.abs(np.asarray(x))))),
            mean_centroid_norm=("centroid_norm", "mean"),
            mean_angle_std_deg=("angle_std_deg", "mean"),
        )
    )

    # Aggregate by width and delta
    by_width_delta = (
        df
        .groupby(["width_deg", "delta_deg"], as_index=False)
        .agg(
            mean_P=("P_plus2", "mean"),
            std_P=("P_plus2", "std"),
            mean_cos2=("ref_cos2_delta", "mean"),
            mean_logistic=("ref_logistic_delta", "mean"),
            mean_error_cos2=("error_cos2", "mean"),
            mean_error_logistic=("error_logistic", "mean"),
            n=("P_plus2", "count"),
        )
    )

    # Best widths
    best_cos2 = by_width.loc[by_width["rmse_cos2"].idxmin()].to_dict()
    best_logistic = by_width.loc[by_width["rmse_logistic"].idxmin()].to_dict()

    save_csv_local(df, "B13_3c_cloud_width_all_points.csv")
    save_csv_local(cloud_diag, "B13_3c_cloud_width_cloud_diagnostics.csv")
    save_csv_local(by_width, "B13_3c_cloud_width_summary_by_width.csv")
    save_csv_local(by_width_delta, "B13_3c_cloud_width_summary_by_width_delta.csv")

    # Figure 1: RMSE vs width
    plt.figure(figsize=(7.5, 5.0))
    plt.plot(by_width["width_deg"], by_width["rmse_cos2"], marker="o", label="RMSE vs cos²")
    plt.plot(by_width["width_deg"], by_width["rmse_logistic"], marker="s", label="RMSE vs logistic")
    plt.xlabel("artificial cloud angular width w [deg]")
    plt.ylabel("RMSE")
    plt.title("B13.3c cloud-width control: RMSE vs width")
    plt.legend()
    save_fig_local("B13_3c_cloud_width_rmse_vs_width.png")

    # Figure 2: shifts vs width
    plt.figure(figsize=(7.5, 5.0))
    plt.plot(by_width["width_deg"], by_width["mean_shift_cos2"], marker="o", label="shift vs cos²")
    plt.plot(by_width["width_deg"], by_width["mean_shift_logistic"], marker="s", label="shift vs logistic")
    plt.axhline(0, linestyle="--", linewidth=1)
    plt.xlabel("artificial cloud angular width w [deg]")
    plt.ylabel("mean shift")
    plt.title("B13.3c cloud-width control: mean shift")
    plt.legend()
    save_fig_local("B13_3c_cloud_width_shift_vs_width.png")

    # Figure 3: curves for selected widths
    selected_widths = sorted(set([
        min(width_deg_values),
        best_cos2["width_deg"],
        best_logistic["width_deg"],
        max(width_deg_values),
    ]))

    plt.figure(figsize=(8.0, 5.5))
    for width in selected_widths:
        sub = by_width_delta[np.isclose(by_width_delta["width_deg"], width)].sort_values("delta_deg")
        plt.errorbar(
            sub["delta_deg"],
            sub["mean_P"],
            yerr=sub["std_P"],
            marker="o",
            capsize=3,
            label=f"w={width:.1f} deg",
        )

    ref = by_width_delta.groupby("delta_deg", as_index=False).agg(
        cos2=("mean_cos2", "mean"),
        logistic=("mean_logistic", "mean"),
    ).sort_values("delta_deg")

    plt.plot(ref["delta_deg"], ref["cos2"], linestyle="--", linewidth=2, label="cos²(delta)")
    plt.plot(ref["delta_deg"], ref["logistic"], linestyle=":", linewidth=2.2, label="B13.2 logistic")
    plt.xlabel("basis difference delta [deg]")
    plt.ylabel("P(+ alpha2 | cloud around + alpha1)")
    plt.title("B13.3c selected cloud-width response curves")
    plt.legend()
    save_fig_local("B13_3c_cloud_width_selected_curves.png")

    # Figure 4: centroid norm vs width
    plt.figure(figsize=(7.5, 5.0))
    cloud_mean = cloud_diag.groupby("width_deg", as_index=False).agg(
        mean_centroid_norm=("centroid_norm", "mean"),
        std_centroid_norm=("centroid_norm", "std"),
        mean_angle_std_deg=("angle_std_deg", "mean"),
    )
    plt.errorbar(
        cloud_mean["width_deg"],
        cloud_mean["mean_centroid_norm"],
        yerr=cloud_mean["std_centroid_norm"],
        marker="o",
        capsize=3,
    )
    plt.xlabel("artificial cloud angular width w [deg]")
    plt.ylabel("centroid norm")
    plt.title("B13.3c artificial cloud coherence")
    save_fig_local("B13_3c_cloud_width_centroid_norm.png")

    summary = {
        "experiment": "B13_3c_cloud_width_controlled_sequential_response",
        "parameters": {
            "seed": seed,
            "alpha1_values_deg": [float(x * 180 / np.pi) for x in alpha1_values],
            "delta_values_deg": [float(x * 180 / np.pi) for x in delta_values],
            "width_deg_values": list(map(float, width_deg_values)),
            "n_cloud": n_cloud,
            "steps2": steps2,
            "a": a,
            "b": b,
            "sigma": sigma,
            "eta": eta,
            "radial_jitter": radial_jitter,
            "logistic_kappa": float(logistic_kappa),
            "logistic_c": float(logistic_c),
        },
        "best_width_for_cos2": best_cos2,
        "best_width_for_logistic": best_logistic,
        "interpretation": (
            "Tests whether finite angular width of a post-selected basin cloud can transform "
            "the BIG logistic basin-boundary response into a cos²-like sequential response. "
            "A finite nonzero best width for cos² would support the cloud-averaging hypothesis."
        ),
    }

    save_json_local(summary, "B13_3c_cloud_width_summary.json")

    print("B13.3c cloud-width controlled sequential response complete.")
    print("Best width for cos²:")
    print(best_cos2)
    print("Best width for logistic:")
    print(best_logistic)
    display(by_width)
    print(json.dumps(summary, indent=2))

    return df, cloud_diag, by_width, by_width_delta, summary
