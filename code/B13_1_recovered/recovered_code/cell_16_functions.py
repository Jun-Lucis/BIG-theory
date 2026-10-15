# Computational functions copied verbatim; original notebook cell 16.

def K_BIG_delta(delta_rad, kappa=3.691281058767646, c=-0.014285741026646481):
    """
    BIG logistic basin-boundary kernel:
        K(delta)=1/(1+exp[-kappa*(cos(2delta)-c)])
    """
    z = kappa * (np.cos(2.0 * delta_rad) - c)
    z = np.clip(z, -60, 60)
    return 1.0 / (1.0 + np.exp(-z))

def K_cloud_convolved(delta_rad, w_rad, kappa=3.691281058767646, c=-0.014285741026646481, n_gh=80):
    """
    Gaussian cloud convolution:
        K_cloud(delta; w) = E_{zeta ~ N(0,w^2)} K_BIG(delta + zeta)

    Uses Gauss-Hermite quadrature.
    For Z~N(0,1):
        E[f(wZ)] = 1/sqrt(pi) sum_i weight_i f(sqrt(2)*w*x_i)
    """
    delta_rad = np.asarray(delta_rad, dtype=float)

    if w_rad <= 1e-12:
        return K_BIG_delta(delta_rad, kappa=kappa, c=c)

    xs, ws = hermgauss(n_gh)

    # shape: [n_gh, len(delta)]
    shifted = delta_rad[None, :] + np.sqrt(2.0) * w_rad * xs[:, None]
    vals = K_BIG_delta(shifted, kappa=kappa, c=c)

    return np.sum(ws[:, None] * vals, axis=0) / np.sqrt(np.pi)

def rmse(a, b):
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    return float(np.sqrt(np.nanmean((a - b) ** 2)))

def estimate_width_from_centroid_norm(R):
    """
    For a small angular Gaussian cloud on unit circle:
        centroid norm R ≈ exp(-w^2 / 2)
    so:
        w ≈ sqrt(-2 log R)
    """
    R = float(np.clip(R, 1e-12, 1.0))
    return np.sqrt(-2.0 * np.log(R))

def get_b13_kernel_params(b=1.0, sigma=0.35):
    try:
        sub = B13_2_summary[
            (np.isclose(B13_2_summary["b"], b)) &
            (np.isclose(B13_2_summary["sigma"], sigma))
        ]
        if len(sub) > 0:
            return float(sub.iloc[0]["kappa"]), float(sub.iloc[0]["c"])
    except Exception:
        pass

    return 3.691281058767646, -0.014285741026646481

def get_target_curve(target="actual"):
    """
    target options:
      - "actual":
          B13_3b actual noisy post-selected state curve
      - "pointer_reset":
          B13_3b pointer reset curve
      - "centroid_reset":
          B13_3b centroid reset curve
      - "sequential_robust":
          B13_3 sequential robustness aggregate curve
      - "cloud_width_best_cos2":
          B13_3c artificial cloud curve at best cos2 width
    """

    if target in ["actual", "pointer_reset", "centroid_reset"]:
        try:
            sub = B13_3b_agg[B13_3b_agg["mode"] == target].copy()
        except NameError:
            raise RuntimeError("B13_3b_agg not found. Run Cell 20 first.")

        sub = sub.sort_values("delta_deg")
        return pd.DataFrame({
            "target": target,
            "delta_deg": sub["delta_deg"].to_numpy(dtype=float),
            "delta_rad": np.deg2rad(sub["delta_deg"].to_numpy(dtype=float)),
            "P_target": sub["mean_P"].to_numpy(dtype=float),
            "P_std": sub["std_P"].to_numpy(dtype=float),
        })

    if target == "sequential_robust":
        try:
            sub = B13_3_seq_robust_agg.copy()
        except NameError:
            raise RuntimeError("B13_3_seq_robust_agg not found. Run Cell 19 first.")

        sub = sub.sort_values("delta_deg")
        return pd.DataFrame({
            "target": target,
            "delta_deg": sub["delta_deg"].to_numpy(dtype=float),
            "delta_rad": np.deg2rad(sub["delta_deg"].to_numpy(dtype=float)),
            "P_target": sub["mean_P"].to_numpy(dtype=float),
            "P_std": sub["std_P"].to_numpy(dtype=float),
        })

    if target == "cloud_width_best_cos2":
        try:
            best_w = float(B13_3c_summary["best_width_for_cos2"]["width_deg"])
            sub = B13_3c_by_width_delta[np.isclose(B13_3c_by_width_delta["width_deg"], best_w)].copy()
        except NameError:
            raise RuntimeError("B13_3c_by_width_delta or B13_3c_summary not found. Run Cell 21 first.")

        sub = sub.sort_values("delta_deg")
        return pd.DataFrame({
            "target": target,
            "delta_deg": sub["delta_deg"].to_numpy(dtype=float),
            "delta_rad": np.deg2rad(sub["delta_deg"].to_numpy(dtype=float)),
            "P_target": sub["mean_P"].to_numpy(dtype=float),
            "P_std": sub["std_P"].to_numpy(dtype=float),
        })

    raise ValueError(f"Unknown target: {target}")

def fit_cloud_width_to_target(
    target="actual",
    width_grid_deg=np.linspace(0, 30, 241),
    b=1.0,
    sigma=0.35,
    n_gh=100,
):
    kappa, c = get_b13_kernel_params(b=b, sigma=sigma)

    target_df = get_target_curve(target=target)

    delta_rad = target_df["delta_rad"].to_numpy(dtype=float)
    y = target_df["P_target"].to_numpy(dtype=float)

    rows = []

    for w_deg in width_grid_deg:
        w_rad = np.deg2rad(w_deg)

        pred = K_cloud_convolved(
            delta_rad,
            w_rad=w_rad,
            kappa=kappa,
            c=c,
            n_gh=n_gh,
        )

        rows.append({
            "target": target,
            "width_deg": float(w_deg),
            "width_rad": float(w_rad),
            "rmse_to_target": rmse(y, pred),
            "mean_shift": float(np.mean(pred - y)),
            "max_abs_error": float(np.max(np.abs(pred - y))),
        })

    fit_df = pd.DataFrame(rows)
    best = fit_df.loc[fit_df["rmse_to_target"].idxmin()].to_dict()

    # Compute predictions at best width
    best_w_rad = float(best["width_rad"])
    pred_best = K_cloud_convolved(delta_rad, best_w_rad, kappa=kappa, c=c, n_gh=n_gh)
    pred_zero = K_cloud_convolved(delta_rad, 0.0, kappa=kappa, c=c, n_gh=n_gh)
    cos2 = np.cos(delta_rad) ** 2

    curve_df = target_df.copy()
    curve_df["K_cloud_best"] = pred_best
    curve_df["K_BIG_w0"] = pred_zero
    curve_df["cos2_ref"] = cos2
    curve_df["error_best"] = curve_df["K_cloud_best"] - curve_df["P_target"]
    curve_df["error_w0"] = curve_df["K_BIG_w0"] - curve_df["P_target"]
    curve_df["error_cos2"] = curve_df["cos2_ref"] - curve_df["P_target"]

    metrics = {
        "target": target,
        "kappa": kappa,
        "c": c,
        "best_width_deg": float(best["width_deg"]),
        "best_width_rad": float(best["width_rad"]),
        "best_rmse_to_target": float(best["rmse_to_target"]),
        "rmse_K_BIG_w0_to_target": rmse(curve_df["P_target"], curve_df["K_BIG_w0"]),
        "rmse_cos2_to_target": rmse(curve_df["P_target"], curve_df["cos2_ref"]),
        "mean_shift_best": float(np.mean(curve_df["K_cloud_best"] - curve_df["P_target"])),
        "max_abs_error_best": float(np.max(np.abs(curve_df["K_cloud_best"] - curve_df["P_target"]))),
    }

    return fit_df, curve_df, metrics

def run_gaussian_cloud_convolution_analysis(
    targets=("actual", "pointer_reset", "centroid_reset", "sequential_robust", "cloud_width_best_cos2"),
    width_grid_deg=np.linspace(0, 30, 241),
    b=1.0,
    sigma=0.35,
    n_gh=100,
):
    all_fit = []
    all_curves = []
    metrics_rows = []

    for target in targets:
        print("=" * 70)
        print("Fitting target:", target)

        try:
            fit_df, curve_df, metrics = fit_cloud_width_to_target(
                target=target,
                width_grid_deg=width_grid_deg,
                b=b,
                sigma=sigma,
                n_gh=n_gh,
            )
        except RuntimeError as e:
            print("Skipped:", target, "|", e)
            continue

        all_fit.append(fit_df)
        all_curves.append(curve_df)
        metrics_rows.append(metrics)

        print(json.dumps(metrics, indent=2))

    fit_all = pd.concat(all_fit, ignore_index=True)
    curves_all = pd.concat(all_curves, ignore_index=True)
    metrics_df = pd.DataFrame(metrics_rows)

    # Estimate actual cloud width from B13.3b centroid norm if available
    centroid_width_estimates = []
    try:
        cloud_mean_R = float(B13_3b_cloud["centroid_norm"].mean())
        w_from_R_rad = estimate_width_from_centroid_norm(cloud_mean_R)
        w_from_R_deg = float(np.rad2deg(w_from_R_rad))

        centroid_width_estimates.append({
            "source": "B13_3b_actual_post_selected_cloud_mean_centroid_norm",
            "mean_centroid_norm": cloud_mean_R,
            "estimated_width_deg_from_R": w_from_R_deg,
        })
    except Exception:
        pass

    try:
        actual_best_R = float(B13_3c_summary["best_width_for_cos2"]["mean_centroid_norm"])
        w_from_best_R_rad = estimate_width_from_centroid_norm(actual_best_R)
        w_from_best_R_deg = float(np.rad2deg(w_from_best_R_rad))

        centroid_width_estimates.append({
            "source": "B13_3c_best_cos2_cloud_centroid_norm",
            "mean_centroid_norm": actual_best_R,
            "estimated_width_deg_from_R": w_from_best_R_deg,
        })
    except Exception:
        pass

    centroid_width_df = pd.DataFrame(centroid_width_estimates)

    # Save data
    save_csv_local(fit_all, "B13_3d_gaussian_cloud_convolution_width_fit_all.csv")
    save_csv_local(curves_all, "B13_3d_gaussian_cloud_convolution_curves_all.csv")
    save_csv_local(metrics_df, "B13_3d_gaussian_cloud_convolution_metrics.csv")

    if len(centroid_width_df) > 0:
        save_csv_local(centroid_width_df, "B13_3d_centroid_norm_width_estimates.csv")

    # --------------------------------------------------------
    # Figure 1: RMSE vs fitted width for all targets
    # --------------------------------------------------------
    plt.figure(figsize=(8.0, 5.2))
    for target, sub in fit_all.groupby("target"):
        sub = sub.sort_values("width_deg")
        plt.plot(sub["width_deg"], sub["rmse_to_target"], label=target)

    # markers for centroid-derived widths
    if len(centroid_width_df) > 0:
        for _, row in centroid_width_df.iterrows():
            plt.axvline(
                row["estimated_width_deg_from_R"],
                linestyle="--",
                linewidth=1,
                alpha=0.7,
                label=f"R-est {row['estimated_width_deg_from_R']:.1f}°"
            )

    plt.xlabel("Gaussian cloud width w [deg]")
    plt.ylabel("RMSE to target curve")
    plt.title("B13.3d Gaussian cloud convolution: width fit")
    plt.legend(fontsize=8)
    save_fig_local("B13_3d_gaussian_cloud_convolution_rmse_vs_width.png")

    # --------------------------------------------------------
    # Figure 2: best convolved curve vs actual target
    # --------------------------------------------------------
    preferred_targets = [t for t in ["actual", "sequential_robust", "cloud_width_best_cos2"] if t in curves_all["target"].unique()]

    for target in preferred_targets:
        sub = curves_all[curves_all["target"] == target].sort_values("delta_deg")
        metric = metrics_df[metrics_df["target"] == target].iloc[0].to_dict()

        plt.figure(figsize=(7.8, 5.2))
        plt.errorbar(
            sub["delta_deg"],
            sub["P_target"],
            yerr=sub["P_std"],
            marker="o",
            capsize=3,
            label=f"target: {target}",
        )
        plt.plot(sub["delta_deg"], sub["K_cloud_best"], marker="s", label=f"K_cloud best w={metric['best_width_deg']:.2f}°")
        plt.plot(sub["delta_deg"], sub["K_BIG_w0"], linestyle=":", linewidth=2, label="K_BIG w=0")
        plt.plot(sub["delta_deg"], sub["cos2_ref"], linestyle="--", linewidth=2, label="cos²(delta)")

        plt.xlabel("basis difference delta [deg]")
        plt.ylabel("P(+)")
        plt.title(f"B13.3d convolution fit to {target}")
        plt.legend()
        save_fig_local(f"B13_3d_convolution_fit_curve_{target}.png")

    # --------------------------------------------------------
    # Figure 3: residuals for actual target if available
    # --------------------------------------------------------
    if "actual" in curves_all["target"].unique():
        sub = curves_all[curves_all["target"] == "actual"].sort_values("delta_deg")

        plt.figure(figsize=(7.8, 5.0))
        plt.plot(sub["delta_deg"], sub["error_best"], marker="o", label="K_cloud best - target")
        plt.plot(sub["delta_deg"], sub["error_w0"], marker="s", label="K_BIG w=0 - target")
        plt.plot(sub["delta_deg"], sub["error_cos2"], marker="^", label="cos² - target")
        plt.axhline(0, linestyle="--", linewidth=1)

        plt.xlabel("basis difference delta [deg]")
        plt.ylabel("residual")
        plt.title("B13.3d residuals against actual sequential target")
        plt.legend()
        save_fig_local("B13_3d_convolution_fit_residuals_actual.png")

    summary = {
        "experiment": "B13_3d_gaussian_cloud_convolution_model",
        "kernel": "K_cloud(delta;w)=E_zeta[K_BIG(delta+zeta)], zeta~N(0,w^2)",
        "parameters": {
            "b": b,
            "sigma": sigma,
            "n_gh": n_gh,
            "width_grid_deg_min": float(np.min(width_grid_deg)),
            "width_grid_deg_max": float(np.max(width_grid_deg)),
            "width_grid_count": int(len(width_grid_deg)),
        },
        "target_metrics": metrics_df.to_dict(orient="records"),
        "centroid_width_estimates": centroid_width_df.to_dict(orient="records") if len(centroid_width_df) > 0 else [],
        "interpretation": (
            "Fits a Gaussian angular cloud convolution of the BIG logistic basin kernel "
            "to sequential observation curves. Agreement between fitted width and measured "
            "post-selected cloud width supports the cloud-averaging mechanism for cos²-like response."
        ),
    }

    save_json_local(summary, "B13_3d_gaussian_cloud_convolution_summary.json")

    print("=" * 70)
    print("B13.3d Gaussian cloud convolution analysis complete.")
    display(metrics_df)
    if len(centroid_width_df) > 0:
        display(centroid_width_df)
    print(json.dumps(summary, indent=2))

    return fit_all, curves_all, metrics_df, centroid_width_df, summary
