# Computational functions copied verbatim; original notebook cell 5.

def logistic_kernel(delta_rad, kappa, c):
    """
    Noise-softened basin-selection kernel.
    Boundary is controlled by cos(2 delta).
    """
    z = kappa * (np.cos(2 * delta_rad) - c)
    z = np.clip(z, -60, 60)
    return 1.0 / (1.0 + np.exp(-z))

def logistic_kernel_bias(delta_rad, kappa, c, bias):
    """
    Same kernel with a probability bias term.
    """
    z = kappa * (np.cos(2 * delta_rad) - c) + bias
    z = np.clip(z, -60, 60)
    return 1.0 / (1.0 + np.exp(-z))

def cos2_ref(delta_rad):
    return np.cos(delta_rad)**2

def run_empirical_kernel_fit(collapse_points_df=None, collapse_binned_df=None):
    if collapse_points_df is None:
        try:
            collapse_points_df = collapse_points.copy()
        except NameError:
            raise RuntimeError("collapse_points not found. Run Cell 14 first.")

    if collapse_binned_df is None:
        try:
            collapse_binned_df = collapse_binned.copy()
        except NameError:
            raise RuntimeError("collapse_binned not found. Run Cell 14 first.")

    points = collapse_points_df.copy()
    binned = collapse_binned_df.copy().dropna(subset=["mean_p_plus"]).copy()

    # Use binned means for stable fitting
    x_deg = binned["delta_bin"].to_numpy(dtype=float)
    y = binned["mean_p_plus"].to_numpy(dtype=float)
    x_rad = np.deg2rad(x_deg)

    # Reference cos² metrics
    y_cos2 = cos2_ref(x_rad)
    rmse_cos2 = float(np.sqrt(np.mean((y - y_cos2)**2)))

    # Fit logistic kernel
    if SCIPY_AVAILABLE:
        popt1, pcov1 = curve_fit(
            logistic_kernel,
            x_rad,
            y,
            p0=[3.0, 0.0],
            bounds=([0.01, -1.5], [30.0, 1.5]),
            maxfev=10000,
        )
        popt2, pcov2 = curve_fit(
            logistic_kernel_bias,
            x_rad,
            y,
            p0=[3.0, 0.0, 0.0],
            bounds=([0.01, -1.5, -5.0], [30.0, 1.5, 5.0]),
            maxfev=10000,
        )
    else:
        # simple fallback grid search
        best1 = None
        for kappa in np.linspace(0.5, 15, 200):
            for c in np.linspace(-0.5, 0.5, 160):
                pred = logistic_kernel(x_rad, kappa, c)
                rmse = np.sqrt(np.mean((y - pred)**2))
                if best1 is None or rmse < best1[0]:
                    best1 = (rmse, kappa, c)
        popt1 = np.array([best1[1], best1[2]])

        best2 = None
        for kappa in np.linspace(0.5, 15, 160):
            for c in np.linspace(-0.5, 0.5, 100):
                for bias in np.linspace(-1.5, 1.5, 80):
                    pred = logistic_kernel_bias(x_rad, kappa, c, bias)
                    rmse = np.sqrt(np.mean((y - pred)**2))
                    if best2 is None or rmse < best2[0]:
                        best2 = (rmse, kappa, c, bias)
        popt2 = np.array([best2[1], best2[2], best2[3]])

    y_logistic = logistic_kernel(x_rad, *popt1)
    y_logistic_bias = logistic_kernel_bias(x_rad, *popt2)

    rmse_logistic = float(np.sqrt(np.mean((y - y_logistic)**2)))
    rmse_logistic_bias = float(np.sqrt(np.mean((y - y_logistic_bias)**2)))

    # Also evaluate against all raw points
    xp_rad = points["delta"].to_numpy(dtype=float)
    yp = points["p_plus"].to_numpy(dtype=float)

    raw_rmse_cos2 = float(np.sqrt(np.mean((yp - cos2_ref(xp_rad))**2)))
    raw_rmse_logistic = float(np.sqrt(np.mean((yp - logistic_kernel(xp_rad, *popt1))**2)))
    raw_rmse_logistic_bias = float(np.sqrt(np.mean((yp - logistic_kernel_bias(xp_rad, *popt2))**2)))

    # Save fitted curves
    dense_deg = np.linspace(x_deg.min(), x_deg.max(), 500)
    dense_rad = np.deg2rad(dense_deg)

    fit_df = pd.DataFrame({
        "delta_deg": dense_deg,
        "cos2_ref": cos2_ref(dense_rad),
        "logistic_kernel": logistic_kernel(dense_rad, *popt1),
        "logistic_kernel_bias": logistic_kernel_bias(dense_rad, *popt2),
    })

    metrics_df = pd.DataFrame([
        {
            "model": "cos2_ref",
            "binned_rmse": rmse_cos2,
            "raw_rmse": raw_rmse_cos2,
            "kappa": np.nan,
            "c": np.nan,
            "bias": np.nan,
        },
        {
            "model": "logistic_cos2delta",
            "binned_rmse": rmse_logistic,
            "raw_rmse": raw_rmse_logistic,
            "kappa": float(popt1[0]),
            "c": float(popt1[1]),
            "bias": np.nan,
        },
        {
            "model": "logistic_cos2delta_bias",
            "binned_rmse": rmse_logistic_bias,
            "raw_rmse": raw_rmse_logistic_bias,
            "kappa": float(popt2[0]),
            "c": float(popt2[1]),
            "bias": float(popt2[2]),
        },
    ])

    save_csv_local(fit_df, "A_rotated_basis_empirical_kernel_fit_curves.csv")
    save_csv_local(metrics_df, "A_rotated_basis_empirical_kernel_fit_metrics.csv")

    # Figure 1: fits
    plt.figure(figsize=(8, 5.5))
    plt.errorbar(
        binned["delta_bin"],
        binned["mean_p_plus"],
        yerr=binned["std_p_plus"],
        marker="o",
        capsize=3,
        linestyle="none",
        label="empirical K_BIG(delta), binned mean ± std",
    )
    plt.plot(dense_deg, fit_df["cos2_ref"], linestyle="--", linewidth=2, label=f"cos²(delta), RMSE={rmse_cos2:.4f}")
    plt.plot(dense_deg, fit_df["logistic_kernel"], linewidth=2, label=f"logistic cos(2δ), RMSE={rmse_logistic:.4f}")
    plt.plot(dense_deg, fit_df["logistic_kernel_bias"], linewidth=2, label=f"logistic+bias, RMSE={rmse_logistic_bias:.4f}")

    plt.xlabel("delta = theta - alpha [deg]")
    plt.ylabel("P(+)")
    plt.title("Empirical BIG selection kernel fit")
    plt.legend()
    save_fig_local("A_rotated_basis_empirical_kernel_fit.png")

    # Figure 2: residuals
    plt.figure(figsize=(8, 5.0))
    plt.plot(x_deg, y - y_cos2, marker="o", label="empirical - cos²")
    plt.plot(x_deg, y - y_logistic, marker="o", label="empirical - logistic")
    plt.plot(x_deg, y - y_logistic_bias, marker="o", label="empirical - logistic+bias")
    plt.axhline(0, linestyle="--", linewidth=1)
    plt.xlabel("delta bin [deg]")
    plt.ylabel("residual")
    plt.title("Kernel fit residual comparison")
    plt.legend()
    save_fig_local("A_rotated_basis_empirical_kernel_residuals.png")

    summary = {
        "experiment": "B13_1_empirical_selection_kernel_fit",
        "kernel_forms": {
            "cos2_ref": "K(delta)=cos^2(delta)",
            "logistic_cos2delta": "K(delta)=1/(1+exp[-kappa*(cos(2delta)-c)])",
            "logistic_cos2delta_bias": "K(delta)=1/(1+exp[-kappa*(cos(2delta)-c)-bias])"
        },
        "metrics": metrics_df.to_dict(orient="records"),
        "interpretation": (
            "If logistic kernels fit better than cos², the Born-like behavior should be "
            "interpreted as a noise-softened basin-selection kernel approximating a Born-like "
            "reference curve, not as a Born-rule derivation."
        ),
    }

    save_json_local(summary, "A_rotated_basis_empirical_kernel_fit_summary.json")

    print("Empirical kernel fit complete.")
    display(metrics_df)
    print(json.dumps(summary, indent=2))

    return fit_df, metrics_df, summary
