# Computational functions copied verbatim; original notebook cell 9.

def K_logistic_delta(delta_rad, kappa=3.691281, c=-0.014286):
    """
    Logistic BIG selection kernel from B13.2.
    Default uses b=1.0, sigma=0.35 quick-scan fit.
    """
    z = kappa * (np.cos(2 * delta_rad) - c)
    z = np.clip(z, -60, 60)
    return 1.0 / (1.0 + np.exp(-z))

def run_sequential_observation_robustness(
    seeds=(111, 222, 333, 444, 555),
    alpha1_values=(0.0, np.pi/12, np.pi/6),
    delta_values=(0.0, np.pi/12, np.pi/8, np.pi/6, np.pi/4),
    n_trials_stage1=400,
    n_trials_stage2_per_parent=1,
    steps1=350,
    steps2=350,
    a=4.0,
    b=1.0,
    sigma=0.35,
    eta=0.01,
    logistic_kappa=None,
    logistic_c=None,
):
    """
    Robust sequential observation test.

    For each alpha1:
      initial state is prepared at theta=alpha1,
      so it begins aligned with + basis of alpha1.

    Then:
      stage1 relaxes under basis alpha1;
      + outcomes are post-selected;
      stage2 relaxes under alpha2=alpha1+delta;
      estimate P(+_alpha2 | +_alpha1).

    Compares with:
      cos²(delta)
      logistic BIG kernel K(delta)
    """

    # Try to get B13.2 fitted kappa,c for b=1.0, sigma=0.35 if available
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

    rows = []

    for seed in seeds:
        rng_master = np.random.default_rng(seed)

        for alpha1 in alpha1_values:
            # Prepare initial state aligned with + alpha1
            initial_theta = alpha1
            h0 = np.array([np.cos(initial_theta), np.sin(initial_theta)])

            # Independent RNG per seed/alpha1
            condition_seed = int(rng_master.integers(0, 2**31 - 1))
            rng = np.random.default_rng(condition_seed)

            # Stage 1
            h1_all, outcome1_plus = simulate_relax_to_basis_state(
                h0=h0,
                alpha=alpha1,
                rng=rng,
                a=a,
                b=b,
                sigma=sigma,
                eta=eta,
                steps=steps1,
                n_trials=n_trials_stage1,
            )

            h1_plus = h1_all[outcome1_plus]
            n_plus1 = len(h1_plus)
            stage1_p_plus = n_plus1 / n_trials_stage1

            print(
                f"seed={seed}, alpha1={alpha1*180/np.pi:5.1f} deg, "
                f"P(+1)={stage1_p_plus:.3f}, n_plus={n_plus1}"
            )

            for delta in delta_values:
                alpha2 = alpha1 + delta

                if n_plus1 == 0:
                    p_plus2 = np.nan
                    n_total2 = 0
                    n_plus2 = 0
                else:
                    h0_stage2 = np.repeat(h1_plus, n_trials_stage2_per_parent, axis=0)
                    n_total2 = len(h0_stage2)
                    h = h0_stage2.copy()

                    for _ in range(steps2):
                        g = grad_rotated_batch(h, alpha2, a=a, b=b)
                        h = h - eta * g + sigma * np.sqrt(eta) * rng.normal(size=h.shape)

                        norm = np.linalg.norm(h, axis=1)
                        mask = norm > 20
                        if np.any(mask):
                            h[mask] = h[mask] / norm[mask, None] * 20

                    e_plus2, e_minus2 = basis_vectors(alpha2)
                    y_plus2 = h @ e_plus2
                    y_minus2 = h @ e_minus2
                    outcome2_plus = np.abs(y_plus2) >= np.abs(y_minus2)

                    n_plus2 = int(np.sum(outcome2_plus))
                    p_plus2 = float(np.mean(outcome2_plus))

                ref_cos2 = float(np.cos(delta)**2)
                ref_logistic = float(K_logistic_delta(delta, kappa=logistic_kappa, c=logistic_c))

                rows.append({
                    "seed": seed,
                    "condition_seed": condition_seed,
                    "alpha1": alpha1,
                    "alpha1_deg": alpha1 * 180 / np.pi,
                    "alpha2": alpha2,
                    "alpha2_deg": alpha2 * 180 / np.pi,
                    "delta": delta,
                    "delta_deg": delta * 180 / np.pi,
                    "stage1_P_plus": stage1_p_plus,
                    "stage1_n_plus": n_plus1,
                    "stage2_n_total": n_total2,
                    "stage2_n_plus": n_plus2,
                    "P_plus2_given_plus1": p_plus2,
                    "ref_cos2_delta": ref_cos2,
                    "ref_logistic_delta": ref_logistic,
                    "error_cos2": p_plus2 - ref_cos2 if not np.isnan(p_plus2) else np.nan,
                    "error_logistic": p_plus2 - ref_logistic if not np.isnan(p_plus2) else np.nan,
                })

    df = pd.DataFrame(rows)

    # Aggregates
    agg = (
        df
        .groupby("delta_deg", as_index=False)
        .agg(
            mean_P=("P_plus2_given_plus1", "mean"),
            std_P=("P_plus2_given_plus1", "std"),
            mean_cos2=("ref_cos2_delta", "mean"),
            mean_logistic=("ref_logistic_delta", "mean"),
            mean_error_cos2=("error_cos2", "mean"),
            std_error_cos2=("error_cos2", "std"),
            mean_error_logistic=("error_logistic", "mean"),
            std_error_logistic=("error_logistic", "std"),
            n=("P_plus2_given_plus1", "count"),
        )
    )

    by_alpha1 = (
        df
        .groupby("alpha1_deg", as_index=False)
        .agg(
            rmse_cos2=("error_cos2", lambda x: float(np.sqrt(np.nanmean(np.asarray(x)**2)))),
            rmse_logistic=("error_logistic", lambda x: float(np.sqrt(np.nanmean(np.asarray(x)**2)))),
            mean_shift_cos2=("error_cos2", "mean"),
            mean_shift_logistic=("error_logistic", "mean"),
            mean_stage1_P_plus=("stage1_P_plus", "mean"),
        )
    )

    global_rmse_cos2 = float(np.sqrt(np.nanmean(df["error_cos2"]**2)))
    global_rmse_logistic = float(np.sqrt(np.nanmean(df["error_logistic"]**2)))
    global_shift_cos2 = float(np.nanmean(df["error_cos2"]))
    global_shift_logistic = float(np.nanmean(df["error_logistic"]))
    max_abs_error_cos2 = float(np.nanmax(np.abs(df["error_cos2"])))
    max_abs_error_logistic = float(np.nanmax(np.abs(df["error_logistic"])))

    save_csv_local(df, "B13_3_sequential_robust_all_points.csv")
    save_csv_local(agg, "B13_3_sequential_robust_by_delta.csv")
    save_csv_local(by_alpha1, "B13_3_sequential_robust_by_alpha1.csv")

    # Figure 1: averaged conditional curve
    plt.figure(figsize=(7.5, 5.2))
    plt.errorbar(
        agg["delta_deg"],
        agg["mean_P"],
        yerr=agg["std_P"],
        marker="o",
        capsize=3,
        label="sequential model mean ± std",
    )
    plt.plot(agg["delta_deg"], agg["mean_cos2"], linestyle="--", label="cos²(delta)")
    plt.plot(agg["delta_deg"], agg["mean_logistic"], linestyle=":", linewidth=2, label="B13.2 logistic kernel")
    plt.xlabel("basis difference delta = alpha2 - alpha1 [deg]")
    plt.ylabel("P(+ alpha2 | + alpha1)")
    plt.title("B13.3 sequential observation robustness")
    plt.legend()
    save_fig_local("B13_3_sequential_robust_curve.png")

    # Figure 2: residuals
    plt.figure(figsize=(7.5, 5.0))
    plt.errorbar(
        agg["delta_deg"],
        agg["mean_error_cos2"],
        yerr=agg["std_error_cos2"],
        marker="o",
        capsize=3,
        label="model - cos²",
    )
    plt.errorbar(
        agg["delta_deg"],
        agg["mean_error_logistic"],
        yerr=agg["std_error_logistic"],
        marker="s",
        capsize=3,
        label="model - logistic",
    )
    plt.axhline(0, linestyle="--", linewidth=1)
    plt.xlabel("basis difference delta [deg]")
    plt.ylabel("residual")
    plt.title("B13.3 sequential residual comparison")
    plt.legend()
    save_fig_local("B13_3_sequential_robust_residuals.png")

    # Figure 3: RMSE by alpha1
    plt.figure(figsize=(7.0, 4.8))
    plt.plot(by_alpha1["alpha1_deg"], by_alpha1["rmse_cos2"], marker="o", label="RMSE vs cos²")
    plt.plot(by_alpha1["alpha1_deg"], by_alpha1["rmse_logistic"], marker="s", label="RMSE vs logistic")
    plt.xlabel("first basis alpha1 [deg]")
    plt.ylabel("RMSE")
    plt.title("B13.3 RMSE by first basis")
    plt.legend()
    save_fig_local("B13_3_sequential_robust_rmse_by_alpha1.png")

    summary = {
        "experiment": "B13_3_sequential_observation_robustness",
        "parameters": {
            "seeds": list(seeds),
            "alpha1_values_deg": [float(x * 180 / np.pi) for x in alpha1_values],
            "delta_values_deg": [float(x * 180 / np.pi) for x in delta_values],
            "a": a,
            "b": b,
            "sigma": sigma,
            "eta": eta,
            "steps1": steps1,
            "steps2": steps2,
            "n_trials_stage1": n_trials_stage1,
            "n_trials_stage2_per_parent": n_trials_stage2_per_parent,
            "logistic_kappa": float(logistic_kappa),
            "logistic_c": float(logistic_c),
        },
        "metrics": {
            "global_rmse_cos2": global_rmse_cos2,
            "global_rmse_logistic": global_rmse_logistic,
            "global_shift_cos2": global_shift_cos2,
            "global_shift_logistic": global_shift_logistic,
            "max_abs_error_cos2": max_abs_error_cos2,
            "max_abs_error_logistic": max_abs_error_logistic,
        },
        "interpretation": (
            "Robust sequential post-selected observation test. "
            "If cos² RMSE is lower than logistic RMSE, the post-selected sequential response "
            "is closer to the basis-difference reference than to the single-shot BIG kernel. "
            "This remains a reduced measurement-like toy result, not a derivation of quantum measurement."
        ),
    }

    save_json_local(summary, "B13_3_sequential_robust_summary.json")

    print("Sequential robustness complete.")
    display(agg)
    display(by_alpha1)
    print(json.dumps(summary, indent=2))

    return df, agg, by_alpha1, summary
