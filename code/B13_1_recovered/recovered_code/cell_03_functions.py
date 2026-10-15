# Computational functions copied verbatim; original notebook cell 3.

def run_rotated_basis_robustness(
    seeds=(101, 202, 303, 404, 505),
    alphas=(0.0, np.pi/12, np.pi/8, np.pi/6, np.pi/4),
    n_theta=25,
    n_trials=300,
    steps=400,
    a=4.0,
    b=1.0,
    sigma=0.35,
    eta=0.01,
):
    all_summary = []
    all_curves = []

    for seed in seeds:
        print("=" * 60)
        print("Seed:", seed)

        df_seed, summary_seed, result_seed = run_rotated_basis_experiment(
            seed=seed,
            alphas=alphas,
            n_theta=n_theta,
            n_trials=n_trials,
            steps=steps,
            a=a,
            b=b,
            sigma=sigma,
            eta=eta,
        )

        df_seed = df_seed.copy()
        summary_seed = summary_seed.copy()

        df_seed["seed"] = seed
        summary_seed["seed"] = seed

        all_curves.append(df_seed)
        all_summary.append(summary_seed)

    curves_df = pd.concat(all_curves, ignore_index=True)
    summary_df = pd.concat(all_summary, ignore_index=True)

    agg = (
        summary_df
        .groupby(["alpha", "alpha_deg"], as_index=False)
        .agg(
            mean_rmse=("rmse_vs_basis_born_like", "mean"),
            std_rmse=("rmse_vs_basis_born_like", "std"),
            min_rmse=("rmse_vs_basis_born_like", "min"),
            max_rmse=("rmse_vs_basis_born_like", "max"),
            mean_shift=("mean_shift", "mean"),
            std_shift=("mean_shift", "std"),
            mean_max_abs_error=("max_abs_error", "mean"),
        )
    )

    save_csv_local(curves_df, "A_rotated_basis_robust_curves_all_seeds.csv")
    save_csv_local(summary_df, "A_rotated_basis_robust_summary_by_seed.csv")
    save_csv_local(agg, "A_rotated_basis_robust_summary_agg.csv")

    # Figure 1: robust RMSE vs alpha
    plt.figure(figsize=(7, 4.5))
    plt.errorbar(
        agg["alpha_deg"],
        agg["mean_rmse"],
        yerr=agg["std_rmse"],
        marker="o",
        capsize=4,
    )
    plt.xlabel("basis angle alpha [deg]")
    plt.ylabel("RMSE vs cos^2(theta-alpha)")
    plt.title("Rotated-basis robustness across seeds")
    save_fig_local("A_rotated_basis_robust_rmse_vs_alpha.png")

    # Figure 2: mean shift vs alpha
    plt.figure(figsize=(7, 4.5))
    plt.errorbar(
        agg["alpha_deg"],
        agg["mean_shift"],
        yerr=agg["std_shift"],
        marker="o",
        capsize=4,
    )
    plt.axhline(0, linestyle="--", linewidth=1)
    plt.xlabel("basis angle alpha [deg]")
    plt.ylabel("mean shift")
    plt.title("Rotated-basis mean shift across seeds")
    save_fig_local("A_rotated_basis_robust_shift_vs_alpha.png")

    # Figure 3: averaged curves with bands
    curve_agg = (
        curves_df
        .groupby(["alpha", "alpha_deg", "theta", "theta_deg"], as_index=False)
        .agg(
            mean_p_plus=("p_plus", "mean"),
            std_p_plus=("p_plus", "std"),
            p_ref=("p_ref_cos2_theta_minus_alpha", "mean"),
        )
    )

    plt.figure(figsize=(8.5, 5.8))
    for alpha, sub in curve_agg.groupby("alpha"):
        sub = sub.sort_values("theta_deg")
        label = f"model alpha={alpha*180/np.pi:.1f} deg"
        ref_label = f"ref alpha={alpha*180/np.pi:.1f} deg"

        plt.plot(sub["theta_deg"], sub["mean_p_plus"], marker="o", linewidth=1.4, label=label)
        plt.fill_between(
            sub["theta_deg"],
            sub["mean_p_plus"] - sub["std_p_plus"],
            sub["mean_p_plus"] + sub["std_p_plus"],
            alpha=0.12,
        )
        plt.plot(sub["theta_deg"], sub["p_ref"], linestyle="--", linewidth=0.9, label=ref_label)

    plt.xlabel("initial angle theta [deg]")
    plt.ylabel("P(+)")
    plt.title("Rotated-basis averaged selection curves across seeds")
    plt.legend(fontsize=7, ncol=2)
    save_fig_local("A_rotated_basis_robust_curves_overlay.png")

    best = agg.loc[agg["mean_rmse"].idxmin()].to_dict()
    worst = agg.loc[agg["mean_rmse"].idxmax()].to_dict()

    robust_summary = {
        "experiment": "B13_1_rotated_basis_robustness",
        "parameters": {
            "seeds": list(seeds),
            "a": a,
            "b": b,
            "sigma": sigma,
            "eta": eta,
            "steps": steps,
            "n_trials": n_trials,
            "n_theta": n_theta,
            "alphas_deg": [float(x * 180 / np.pi) for x in alphas],
        },
        "best_alpha_by_mean_rmse": best,
        "worst_alpha_by_mean_rmse": worst,
        "interpretation": (
            "Robustness check for basis-aware finite-noise basin selection. "
            "The result should be interpreted as Born-like reference comparison, "
            "not as a derivation of the Born rule."
        ),
    }

    save_json_local(robust_summary, "A_rotated_basis_robust_summary.json")

    print("Robustness check complete.")
    print("Aggregate summary:")
    display(agg)

    print("Best alpha by mean RMSE:", best)
    print("Worst alpha by mean RMSE:", worst)

    return curves_df, summary_df, agg, robust_summary
