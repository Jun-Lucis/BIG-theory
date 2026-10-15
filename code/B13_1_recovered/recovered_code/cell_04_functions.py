# Computational functions copied verbatim; original notebook cell 4.

def run_rotated_basis_curve_collapse(curves_df=None):
    """
    Uses curves_rot_robust if available.
    Computes collapse diagnostics in delta = theta - alpha coordinates.
    """
    if curves_df is None:
        try:
            curves_df = curves_rot_robust.copy()
        except NameError:
            raise RuntimeError("curves_rot_robust not found. Run Cell 13 first or pass curves_df.")

    df = curves_df.copy()

    # delta coordinate
    df["delta"] = df["theta"] - df["alpha"]
    df["delta_deg"] = df["theta_deg"] - df["alpha_deg"]
    df["p_ref_delta"] = np.cos(df["delta"])**2
    df["error_delta"] = df["p_plus"] - df["p_ref_delta"]

    # Global RMSE in shifted coordinate
    global_rmse = float(np.sqrt(np.mean(df["error_delta"]**2)))
    global_shift = float(np.mean(df["error_delta"]))
    global_max_abs_error = float(np.max(np.abs(df["error_delta"])))

    # Bin delta to evaluate collapse thickness
    bin_width = 5.0
    df["delta_bin"] = (np.round(df["delta_deg"] / bin_width) * bin_width).astype(float)

    collapse = (
        df
        .groupby("delta_bin", as_index=False)
        .agg(
            mean_p_plus=("p_plus", "mean"),
            std_p_plus=("p_plus", "std"),
            n=("p_plus", "count"),
            mean_ref=("p_ref_delta", "mean"),
            mean_error=("error_delta", "mean"),
            std_error=("error_delta", "std"),
        )
        .sort_values("delta_bin")
    )

    # Alpha-level shifted RMSE
    by_alpha = (
        df
        .groupby(["alpha", "alpha_deg"], as_index=False)
        .agg(
            rmse_delta=("error_delta", lambda x: float(np.sqrt(np.mean(np.asarray(x)**2)))),
            mean_shift_delta=("error_delta", "mean"),
            max_abs_error_delta=("error_delta", lambda x: float(np.max(np.abs(np.asarray(x))))),
        )
    )

    save_csv_local(df, "A_rotated_basis_collapse_all_points.csv")
    save_csv_local(collapse, "A_rotated_basis_collapse_by_delta_bin.csv")
    save_csv_local(by_alpha, "A_rotated_basis_collapse_by_alpha.csv")

    # Figure 1: all shifted curves
    plt.figure(figsize=(8, 5.5))
    for (seed, alpha), sub in df.groupby(["seed", "alpha"]):
        sub = sub.sort_values("delta_deg")
        plt.plot(
            sub["delta_deg"],
            sub["p_plus"],
            alpha=0.25,
            linewidth=1,
        )

    delta_grid = np.linspace(df["delta_deg"].min(), df["delta_deg"].max(), 300)
    plt.plot(delta_grid, np.cos(np.deg2rad(delta_grid))**2, linewidth=2.5, label="cos²(delta)")
    plt.xlabel("delta = theta - alpha [deg]")
    plt.ylabel("P(+)")
    plt.title("Rotated-basis shifted-coordinate curve collapse")
    plt.legend()
    save_fig_local("A_rotated_basis_curve_collapse_all_curves.png")

    # Figure 2: binned mean with spread
    plt.figure(figsize=(8, 5.5))
    valid = collapse.dropna(subset=["std_p_plus"])
    plt.errorbar(
        valid["delta_bin"],
        valid["mean_p_plus"],
        yerr=valid["std_p_plus"],
        marker="o",
        capsize=3,
        label="model mean ± std across alpha/seeds",
    )
    delta_grid = np.linspace(valid["delta_bin"].min(), valid["delta_bin"].max(), 300)
    plt.plot(delta_grid, np.cos(np.deg2rad(delta_grid))**2, linestyle="--", linewidth=2, label="cos²(delta)")
    plt.xlabel("delta bin = theta - alpha [deg]")
    plt.ylabel("P(+)")
    plt.title("Binned curve-collapse diagnostic")
    plt.legend()
    save_fig_local("A_rotated_basis_curve_collapse_binned.png")

    # Figure 3: collapse error by delta
    plt.figure(figsize=(8, 4.8))
    plt.errorbar(
        valid["delta_bin"],
        valid["mean_error"],
        yerr=valid["std_error"],
        marker="o",
        capsize=3,
    )
    plt.axhline(0, linestyle="--", linewidth=1)
    plt.xlabel("delta bin = theta - alpha [deg]")
    plt.ylabel("model - cos²(delta)")
    plt.title("Systematic collapse error by shifted coordinate")
    save_fig_local("A_rotated_basis_curve_collapse_error.png")

    summary = {
        "experiment": "B13_1_rotated_basis_curve_collapse",
        "global_rmse_vs_cos2_delta": global_rmse,
        "global_mean_shift": global_shift,
        "global_max_abs_error": global_max_abs_error,
        "bin_width_deg": bin_width,
        "interpretation": (
            "Tests whether rotated-basis selection curves collapse when plotted against "
            "delta=theta-alpha. Good collapse supports partial basis-awareness. "
            "Systematic residuals indicate deviations from exact basis covariance."
        )
    }

    save_json_local(summary, "A_rotated_basis_curve_collapse_summary.json")

    print("Curve-collapse diagnostic complete.")
    print(json.dumps(summary, indent=2))
    print("By alpha:")
    display(by_alpha)

    return df, collapse, by_alpha, summary
