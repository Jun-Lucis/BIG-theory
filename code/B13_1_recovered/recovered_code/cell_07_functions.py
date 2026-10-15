# Computational functions copied verbatim; original notebook cell 7.

def fit_power_law_kappa(summary_df=None):
    """
    Fit:
        kappa = C * b^p * sigma^{-q}

    Equivalent log-linear form:
        log(kappa) = log C + p log b - q log sigma

    Also compares a simpler ratio model:
        kappa = C2 * (b / sigma^2)^r
    """

    if summary_df is None:
        try:
            summary_df = B13_2_summary.copy()
        except NameError:
            raise RuntimeError("B13_2_summary not found. Run Cell 16 first or pass summary_df.")

    df = summary_df.copy()

    # Remove invalid values if any
    df = df.replace([np.inf, -np.inf], np.nan).dropna(subset=["b", "sigma", "kappa"])
    df = df[(df["b"] > 0) & (df["sigma"] > 0) & (df["kappa"] > 0)].copy()

    # ----------------------------
    # Model 1: kappa = C b^p sigma^{-q}
    # ----------------------------
    y = np.log(df["kappa"].to_numpy(dtype=float))
    X = np.column_stack([
        np.ones(len(df)),
        np.log(df["b"].to_numpy(dtype=float)),
        -np.log(df["sigma"].to_numpy(dtype=float)),
    ])

    beta, residuals, rank, svals = np.linalg.lstsq(X, y, rcond=None)

    logC, p, q = beta
    C = float(np.exp(logC))
    p = float(p)
    q = float(q)

    df["kappa_pred_power"] = C * (df["b"] ** p) * (df["sigma"] ** (-q))
    df["log_kappa_pred_power"] = np.log(df["kappa_pred_power"])
    df["residual_log_power"] = np.log(df["kappa"]) - df["log_kappa_pred_power"]
    df["residual_power"] = df["kappa"] - df["kappa_pred_power"]

    ss_res = float(np.sum((np.log(df["kappa"]) - np.log(df["kappa_pred_power"]))**2))
    ss_tot = float(np.sum((np.log(df["kappa"]) - np.mean(np.log(df["kappa"])))**2))
    r2_log_power = 1.0 - ss_res / ss_tot

    rmse_log_power = float(np.sqrt(np.mean(df["residual_log_power"]**2)))
    rmse_kappa_power = float(np.sqrt(np.mean(df["residual_power"]**2)))

    # ----------------------------
    # Model 2: kappa = C2 * (b / sigma^2)^r
    # ----------------------------
    x_ratio = np.log(df["b"].to_numpy(dtype=float) / (df["sigma"].to_numpy(dtype=float)**2))
    X2 = np.column_stack([np.ones(len(df)), x_ratio])

    beta2, residuals2, rank2, svals2 = np.linalg.lstsq(X2, y, rcond=None)
    logC2, r = beta2
    C2 = float(np.exp(logC2))
    r = float(r)

    df["kappa_pred_ratio"] = C2 * ((df["b"] / (df["sigma"]**2)) ** r)
    df["log_kappa_pred_ratio"] = np.log(df["kappa_pred_ratio"])
    df["residual_log_ratio"] = np.log(df["kappa"]) - df["log_kappa_pred_ratio"]
    df["residual_ratio"] = df["kappa"] - df["kappa_pred_ratio"]

    ss_res2 = float(np.sum((np.log(df["kappa"]) - np.log(df["kappa_pred_ratio"]))**2))
    r2_log_ratio = 1.0 - ss_res2 / ss_tot

    rmse_log_ratio = float(np.sqrt(np.mean(df["residual_log_ratio"]**2)))
    rmse_kappa_ratio = float(np.sqrt(np.mean(df["residual_ratio"]**2)))

    # ----------------------------
    # Save fitted data
    # ----------------------------
    save_csv_local(df, "B13_2_kernel_scaling_law_fit_points.csv")

    metrics_df = pd.DataFrame([
        {
            "model": "power_law_C_b^p_sigma^-q",
            "C": C,
            "p": p,
            "q": q,
            "r": np.nan,
            "R2_log": r2_log_power,
            "RMSE_log": rmse_log_power,
            "RMSE_kappa": rmse_kappa_power,
        },
        {
            "model": "ratio_law_C_(b_sigma^-2)^r",
            "C": C2,
            "p": np.nan,
            "q": np.nan,
            "r": r,
            "R2_log": r2_log_ratio,
            "RMSE_log": rmse_log_ratio,
            "RMSE_kappa": rmse_kappa_ratio,
        },
    ])

    save_csv_local(metrics_df, "B13_2_kernel_scaling_law_fit_metrics.csv")

    # ----------------------------
    # Figure 1: observed vs predicted kappa
    # ----------------------------
    plt.figure(figsize=(6.5, 6.0))
    plt.scatter(df["kappa"], df["kappa_pred_power"], label="power law")
    plt.scatter(df["kappa"], df["kappa_pred_ratio"], marker="x", label="ratio law")

    lim_min = min(df["kappa"].min(), df["kappa_pred_power"].min(), df["kappa_pred_ratio"].min()) * 0.85
    lim_max = max(df["kappa"].max(), df["kappa_pred_power"].max(), df["kappa_pred_ratio"].max()) * 1.15

    plt.plot([lim_min, lim_max], [lim_min, lim_max], linestyle="--", linewidth=1)
    plt.xlabel("observed kappa")
    plt.ylabel("predicted kappa")
    plt.title("B13.2 scaling-law fit: observed vs predicted kappa")
    plt.legend()
    save_fig_local("B13_2_scaling_law_observed_vs_predicted.png")

    # ----------------------------
    # Figure 2: power-law residual heatmap
    # ----------------------------
    pivot_resid = df.pivot(index="b", columns="sigma", values="residual_log_power")

    plt.figure(figsize=(7.0, 5.0))
    im = plt.imshow(
        pivot_resid.values,
        origin="lower",
        aspect="auto",
        extent=[
            df["sigma"].min(), df["sigma"].max(),
            df["b"].min(), df["b"].max()
        ],
    )
    plt.colorbar(im, label="log residual: observed - predicted")
    plt.xlabel("noise sigma")
    plt.ylabel("barrier b")
    plt.title("B13.2 power-law residual heatmap")
    save_fig_local("B13_2_scaling_law_power_residual_heatmap.png")

    # ----------------------------
    # Figure 3: collapse plot for power-law scaling variable
    # ----------------------------
    df["scaling_variable_power"] = (df["b"] ** p) * (df["sigma"] ** (-q))

    plt.figure(figsize=(7.0, 5.0))
    plt.scatter(df["scaling_variable_power"], df["kappa"], label="observed")
    xs = np.linspace(df["scaling_variable_power"].min(), df["scaling_variable_power"].max(), 300)
    plt.plot(xs, C * xs, linestyle="--", label=f"fit: kappa = {C:.3g} X")
    plt.xlabel(r"scaling variable $X=b^p\sigma^{-q}$")
    plt.ylabel("kappa")
    plt.title("B13.2 kappa collapse under fitted scaling variable")
    plt.legend()
    save_fig_local("B13_2_scaling_law_power_collapse.png")

    # ----------------------------
    # Figure 4: ratio law collapse
    # ----------------------------
    df["scaling_variable_ratio"] = (df["b"] / (df["sigma"]**2)) ** r

    plt.figure(figsize=(7.0, 5.0))
    plt.scatter(df["scaling_variable_ratio"], df["kappa"], label="observed")
    xs = np.linspace(df["scaling_variable_ratio"].min(), df["scaling_variable_ratio"].max(), 300)
    plt.plot(xs, C2 * xs, linestyle="--", label=f"fit: kappa = {C2:.3g} X")
    plt.xlabel(r"scaling variable $X=(b/\sigma^2)^r$")
    plt.ylabel("kappa")
    plt.title("B13.2 kappa collapse under ratio-law variable")
    plt.legend()
    save_fig_local("B13_2_scaling_law_ratio_collapse.png")

    # ----------------------------
    # Figure 5: fitted law curves over sigma
    # ----------------------------
    plt.figure(figsize=(7.5, 5.2))
    for b, sub in df.groupby("b"):
        sub = sub.sort_values("sigma")
        plt.plot(sub["sigma"], sub["kappa"], marker="o", label=f"observed b={b}")

        sigma_grid = np.linspace(sub["sigma"].min(), sub["sigma"].max(), 200)
        pred_grid = C * (b ** p) * (sigma_grid ** (-q))
        plt.plot(sigma_grid, pred_grid, linestyle="--", linewidth=1.2)

    plt.xlabel("noise sigma")
    plt.ylabel("kappa")
    plt.title("B13.2 fitted power-law curves")
    plt.legend(fontsize=8)
    save_fig_local("B13_2_scaling_law_curves_vs_sigma.png")

    # ----------------------------
    # Summary JSON
    # ----------------------------
    summary = {
        "experiment": "B13_2_kernel_sharpness_scaling_law_fit",
        "model_1_power_law": {
            "form": "kappa = C * b^p * sigma^(-q)",
            "C": C,
            "p": p,
            "q": q,
            "R2_log": r2_log_power,
            "RMSE_log": rmse_log_power,
            "RMSE_kappa": rmse_kappa_power,
        },
        "model_2_ratio_law": {
            "form": "kappa = C2 * (b / sigma^2)^r",
            "C2": C2,
            "r": r,
            "R2_log": r2_log_ratio,
            "RMSE_log": rmse_log_ratio,
            "RMSE_kappa": rmse_kappa_ratio,
        },
        "interpretation": (
            "A good power-law fit supports the interpretation that the BIG selection-kernel "
            "sharpness is controlled by barrier hardening and noise softening. "
            "This is a scaling law for the empirical basin-boundary response, not a derivation "
            "of the Born rule."
        ),
    }

    save_json_local(summary, "B13_2_kernel_scaling_law_fit_summary.json")

    print("B13.2 scaling-law fit complete.")
    display(metrics_df)
    print(json.dumps(summary, indent=2))

    return df, metrics_df, summary
