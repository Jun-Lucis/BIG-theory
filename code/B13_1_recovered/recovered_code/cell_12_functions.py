# Computational functions copied verbatim; original notebook cell 12.

def normalize_vector(v, eps=1e-12):
    v = np.asarray(v, dtype=float)
    n = np.linalg.norm(v)
    if n < eps:
        return v
    return v / n

def evolve_stage2_batch(
    h0_batch,
    alpha2,
    rng,
    a=4.0,
    b=1.0,
    sigma=0.35,
    eta=0.01,
    steps=350,
):
    """
    Evolve a batch under the rotated-basis landscape alpha2.
    Classify + by |y_plus| >= |y_minus|.
    """
    h = np.array(h0_batch, dtype=float).copy()

    for _ in range(steps):
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
    return h, outcome2_plus

def run_sequential_reset_comparison(
    seeds=(111, 222, 333, 444, 555),
    alpha1_values=(0.0, np.pi/12, np.pi/6),
    delta_values=(0.0, np.pi/12, np.pi/8, np.pi/6, np.pi/4),
    n_trials_stage1=500,
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
    Compares three stage-2 initializations after + post-selection in stage 1:

    1. actual:
       use the actual noisy final states h1_plus.

    2. pointer_reset:
       replace every post-selected state by ideal e_plus(alpha1).

    3. centroid_reset:
       replace every post-selected state by the normalized centroid of h1_plus.

    Reference curves:
       cos²(delta)
       B13.2 logistic kernel
    """

    # Get B13.2 logistic kernel parameters if available
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
    cloud_rows = []

    for seed in seeds:
        rng_master = np.random.default_rng(seed)

        for alpha1 in alpha1_values:
            # Prepare initial state aligned with + alpha1
            e_plus1, e_minus1 = basis_vectors(alpha1)
            h0 = e_plus1.copy()

            condition_seed = int(rng_master.integers(0, 2**31 - 1))
            rng_stage1 = np.random.default_rng(condition_seed)

            # Stage 1 actual relaxation
            h1_all, outcome1_plus = simulate_relax_to_basis_state(
                h0=h0,
                alpha=alpha1,
                rng=rng_stage1,
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

            if n_plus1 == 0:
                print(f"seed={seed}, alpha1={alpha1*180/np.pi:.1f}: no + outcomes")
                continue

            # Cloud diagnostics
            centroid = np.mean(h1_plus, axis=0)
            centroid_norm = np.linalg.norm(centroid)
            centroid_unit = normalize_vector(centroid)

            # Alignment of cloud with ideal pointer
            align = h1_plus @ e_plus1
            abs_align = np.abs(align)

            cloud_rows.append({
                "seed": seed,
                "condition_seed": condition_seed,
                "alpha1": alpha1,
                "alpha1_deg": alpha1 * 180 / np.pi,
                "stage1_P_plus": stage1_p_plus,
                "stage1_n_plus": n_plus1,
                "centroid_x": centroid[0],
                "centroid_y": centroid[1],
                "centroid_norm": centroid_norm,
                "centroid_angle_deg": np.arctan2(centroid_unit[1], centroid_unit[0]) * 180 / np.pi,
                "mean_abs_alignment_with_eplus1": float(np.mean(abs_align)),
                "std_abs_alignment_with_eplus1": float(np.std(abs_align)),
            })

            print(
                f"seed={seed}, alpha1={alpha1*180/np.pi:5.1f} deg, "
                f"P(+1)={stage1_p_plus:.3f}, n_plus={n_plus1}, "
                f"centroid_norm={centroid_norm:.3f}"
            )

            for delta in delta_values:
                alpha2 = alpha1 + delta

                # Reference values
                ref_cos2 = float(np.cos(delta)**2)
                ref_logistic = float(K_logistic_delta(delta, kappa=logistic_kappa, c=logistic_c))

                # Three reset modes
                init_batches = {
                    "actual": h1_plus,
                    "pointer_reset": np.repeat(e_plus1[None, :], n_plus1, axis=0),
                    "centroid_reset": np.repeat(centroid_unit[None, :], n_plus1, axis=0),
                }

                for mode, h0_stage2 in init_batches.items():
                    # Independent but reproducible stage2 RNG for each mode/delta
                    mode_seed = int(rng_master.integers(0, 2**31 - 1))
                    rng_stage2 = np.random.default_rng(mode_seed)

                    h2, outcome2_plus = evolve_stage2_batch(
                        h0_batch=h0_stage2,
                        alpha2=alpha2,
                        rng=rng_stage2,
                        a=a,
                        b=b,
                        sigma=sigma,
                        eta=eta,
                        steps=steps2,
                    )

                    p_plus2 = float(np.mean(outcome2_plus))
                    n_plus2 = int(np.sum(outcome2_plus))

                    rows.append({
                        "seed": seed,
                        "condition_seed": condition_seed,
                        "mode_seed": mode_seed,
                        "mode": mode,
                        "alpha1": alpha1,
                        "alpha1_deg": alpha1 * 180 / np.pi,
                        "alpha2": alpha2,
                        "alpha2_deg": alpha2 * 180 / np.pi,
                        "delta": delta,
                        "delta_deg": delta * 180 / np.pi,
                        "stage1_P_plus": stage1_p_plus,
                        "stage1_n_plus": n_plus1,
                        "stage2_n_total": len(h0_stage2),
                        "stage2_n_plus": n_plus2,
                        "P_plus2_given_plus1": p_plus2,
                        "ref_cos2_delta": ref_cos2,
                        "ref_logistic_delta": ref_logistic,
                        "error_cos2": p_plus2 - ref_cos2,
                        "error_logistic": p_plus2 - ref_logistic,
                        "centroid_norm": centroid_norm,
                    })

    df = pd.DataFrame(rows)
    cloud_df = pd.DataFrame(cloud_rows)

    # Aggregates
    agg = (
        df
        .groupby(["mode", "delta_deg"], as_index=False)
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

    by_mode = (
        df
        .groupby("mode", as_index=False)
        .agg(
            rmse_cos2=("error_cos2", lambda x: float(np.sqrt(np.nanmean(np.asarray(x)**2)))),
            rmse_logistic=("error_logistic", lambda x: float(np.sqrt(np.nanmean(np.asarray(x)**2)))),
            mean_shift_cos2=("error_cos2", "mean"),
            mean_shift_logistic=("error_logistic", "mean"),
            max_abs_error_cos2=("error_cos2", lambda x: float(np.nanmax(np.abs(np.asarray(x))))),
            max_abs_error_logistic=("error_logistic", lambda x: float(np.nanmax(np.abs(np.asarray(x))))),
            mean_stage1_P_plus=("stage1_P_plus", "mean"),
            mean_centroid_norm=("centroid_norm", "mean"),
        )
    )

    by_mode_alpha1 = (
        df
        .groupby(["mode", "alpha1_deg"], as_index=False)
        .agg(
            rmse_cos2=("error_cos2", lambda x: float(np.sqrt(np.nanmean(np.asarray(x)**2)))),
            rmse_logistic=("error_logistic", lambda x: float(np.sqrt(np.nanmean(np.asarray(x)**2)))),
            mean_shift_cos2=("error_cos2", "mean"),
            mean_shift_logistic=("error_logistic", "mean"),
        )
    )

    save_csv_local(df, "B13_3b_sequential_reset_comparison_all_points.csv")
    save_csv_local(cloud_df, "B13_3b_stage1_cloud_diagnostics.csv")
    save_csv_local(agg, "B13_3b_sequential_reset_comparison_by_delta.csv")
    save_csv_local(by_mode, "B13_3b_sequential_reset_comparison_by_mode.csv")
    save_csv_local(by_mode_alpha1, "B13_3b_sequential_reset_comparison_by_mode_alpha1.csv")

    # Figure 1: curves by mode
    plt.figure(figsize=(8.0, 5.4))
    for mode, sub in agg.groupby("mode"):
        sub = sub.sort_values("delta_deg")
        plt.errorbar(
            sub["delta_deg"],
            sub["mean_P"],
            yerr=sub["std_P"],
            marker="o",
            capsize=3,
            label=mode,
        )

    ref_sub = agg.groupby("delta_deg", as_index=False).agg(
        cos2=("mean_cos2", "mean"),
        logistic=("mean_logistic", "mean"),
    ).sort_values("delta_deg")

    plt.plot(ref_sub["delta_deg"], ref_sub["cos2"], linestyle="--", linewidth=1.8, label="cos²(delta)")
    plt.plot(ref_sub["delta_deg"], ref_sub["logistic"], linestyle=":", linewidth=2.2, label="B13.2 logistic kernel")
    plt.xlabel("basis difference delta [deg]")
    plt.ylabel("P(+ alpha2 | + alpha1)")
    plt.title("B13.3b sequential reset comparison")
    plt.legend()
    save_fig_local("B13_3b_sequential_reset_comparison_curves.png")

    # Figure 2: RMSE by mode
    plt.figure(figsize=(7.2, 4.8))
    x = np.arange(len(by_mode))
    width = 0.35
    plt.bar(x - width/2, by_mode["rmse_cos2"], width, label="RMSE vs cos²")
    plt.bar(x + width/2, by_mode["rmse_logistic"], width, label="RMSE vs logistic")
    plt.xticks(x, by_mode["mode"], rotation=15)
    plt.ylabel("RMSE")
    plt.title("B13.3b RMSE by reset mode")
    plt.legend()
    save_fig_local("B13_3b_sequential_reset_comparison_rmse_by_mode.png")

    # Figure 3: residuals vs cos²
    plt.figure(figsize=(8.0, 5.2))
    for mode, sub in agg.groupby("mode"):
        sub = sub.sort_values("delta_deg")
        plt.errorbar(
            sub["delta_deg"],
            sub["mean_error_cos2"],
            yerr=sub["std_error_cos2"],
            marker="o",
            capsize=3,
            label=f"{mode} - cos²",
        )
    plt.axhline(0, linestyle="--", linewidth=1)
    plt.xlabel("basis difference delta [deg]")
    plt.ylabel("residual vs cos²")
    plt.title("B13.3b residuals against cos² reference")
    plt.legend()
    save_fig_local("B13_3b_sequential_reset_comparison_residuals_cos2.png")

    # Figure 4: stage1 cloud centroid norms
    plt.figure(figsize=(7.0, 4.8))
    if len(cloud_df) > 0:
        for alpha1_deg, sub in cloud_df.groupby("alpha1_deg"):
            plt.scatter(
                sub["alpha1_deg"],
                sub["centroid_norm"],
                label=f"alpha1={alpha1_deg:.1f} deg",
            )
        cloud_mean = cloud_df.groupby("alpha1_deg", as_index=False).agg(
            mean_centroid_norm=("centroid_norm", "mean"),
            std_centroid_norm=("centroid_norm", "std"),
        )
        plt.errorbar(
            cloud_mean["alpha1_deg"],
            cloud_mean["mean_centroid_norm"],
            yerr=cloud_mean["std_centroid_norm"],
            marker="o",
            capsize=3,
            linewidth=2,
            label="mean ± std",
        )
    plt.xlabel("first basis alpha1 [deg]")
    plt.ylabel("stage1 + cloud centroid norm")
    plt.title("B13.3b post-selected cloud coherence")
    plt.legend()
    save_fig_local("B13_3b_stage1_cloud_centroid_norm.png")

    summary = {
        "experiment": "B13_3b_actual_vs_pointer_vs_centroid_reset",
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
            "logistic_kappa": float(logistic_kappa),
            "logistic_c": float(logistic_c),
        },
        "mode_metrics": by_mode.to_dict(orient="records"),
        "interpretation": (
            "Compares actual noisy post-selected states with ideal pointer reset and centroid reset. "
            "If pointer_reset improves same-basis repeatability and changes the reference fit, "
            "the departure from ideal projection can be attributed to finite-noise basin-localized cloud effects."
        ),
    }

    save_json_local(summary, "B13_3b_sequential_reset_comparison_summary.json")

    print("B13.3b reset comparison complete.")
    print("By mode:")
    display(by_mode)
    print("Cloud diagnostics:")
    display(cloud_df.head())
    print(json.dumps(summary, indent=2))

    return df, cloud_df, agg, by_mode, by_mode_alpha1, summary
