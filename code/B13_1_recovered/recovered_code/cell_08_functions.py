# Computational functions copied verbatim; original notebook cell 8.

def simulate_relax_to_basis_state(
    h0,
    alpha,
    rng,
    a=4.0,
    b=1.0,
    sigma=0.35,
    eta=0.01,
    steps=350,
    n_trials=200,
):
    """
    Evolve many trials from the same initial h0 under rotated-basis landscape.
    Returns final h and outcome signs in basis alpha.
    """
    h = np.repeat(np.array(h0, dtype=float)[None, :], n_trials, axis=0)

    for _ in range(steps):
        g = grad_rotated_batch(h, alpha, a=a, b=b)
        h = h - eta * g + sigma * np.sqrt(eta) * rng.normal(size=h.shape)

        norm = np.linalg.norm(h, axis=1)
        mask = norm > 20
        if np.any(mask):
            h[mask] = h[mask] / norm[mask, None] * 20

    e_plus, e_minus = basis_vectors(alpha)
    y_plus = h @ e_plus
    y_minus = h @ e_minus

    outcome_plus = np.abs(y_plus) >= np.abs(y_minus)

    # signed representative state in the selected basin:
    # use actual final h, not forced projection
    return h, outcome_plus

def run_sequential_observation_experiment(
    seed=909,
    alpha1=0.0,
    alpha2_values=(0.0, np.pi/12, np.pi/8, np.pi/6, np.pi/4),
    initial_theta=0.0,
    n_trials_stage1=300,
    n_trials_stage2_per_parent=1,
    steps1=350,
    steps2=350,
    a=4.0,
    b=1.0,
    sigma=0.35,
    eta=0.01,
):
    """
    Sequential observation:
      1. Start from h0=(cos initial_theta, sin initial_theta).
      2. Measure/relax in basis alpha1.
      3. Keep only + outcomes from stage 1.
      4. Use those final states as initial states for stage 2 in basis alpha2.
      5. Estimate P(+_alpha2 | +_alpha1).

    For alpha1=0 and initial_theta=0, stage1 should mostly produce +_alpha1.
    Reference: cos^2(alpha2-alpha1).
    """
    rng = np.random.default_rng(seed)

    h0 = np.array([np.cos(initial_theta), np.sin(initial_theta)])

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

    print(f"Stage 1: alpha1={alpha1*180/np.pi:.1f} deg, P(+1)={n_plus1/n_trials_stage1:.3f}, n_plus={n_plus1}")

    rows = []

    for alpha2 in alpha2_values:
        if n_plus1 == 0:
            p_plus2 = np.nan
            n_total2 = 0
            n_plus2 = 0
        else:
            # Repeat each parent if desired
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

        delta = alpha2 - alpha1
        p_ref = np.cos(delta)**2

        rows.append({
            "seed": seed,
            "alpha1": alpha1,
            "alpha1_deg": alpha1 * 180 / np.pi,
            "alpha2": alpha2,
            "alpha2_deg": alpha2 * 180 / np.pi,
            "delta": delta,
            "delta_deg": delta * 180 / np.pi,
            "initial_theta": initial_theta,
            "initial_theta_deg": initial_theta * 180 / np.pi,
            "stage1_P_plus": n_plus1 / n_trials_stage1,
            "stage1_n_plus": n_plus1,
            "stage2_n_total": n_total2,
            "stage2_n_plus": n_plus2,
            "P_plus2_given_plus1": p_plus2,
            "ref_cos2_delta": p_ref,
            "error": p_plus2 - p_ref if not np.isnan(p_plus2) else np.nan,
        })

        print(
            f"alpha2={alpha2*180/np.pi:5.1f} deg, "
            f"P(+2|+1)={p_plus2:.4f}, ref={p_ref:.4f}, "
            f"err={p_plus2-p_ref:+.4f}"
        )

    df = pd.DataFrame(rows)

    rmse = float(np.sqrt(np.nanmean(df["error"]**2)))
    mean_shift = float(np.nanmean(df["error"]))
    max_abs_error = float(np.nanmax(np.abs(df["error"])))

    save_csv_local(df, "B13_3_sequential_observation_results.csv")

    # Figure
    plt.figure(figsize=(7.5, 5.0))
    plt.plot(df["delta_deg"], df["P_plus2_given_plus1"], marker="o", label="sequential model")
    plt.plot(df["delta_deg"], df["ref_cos2_delta"], linestyle="--", label="cos²(alpha2-alpha1)")
    plt.xlabel("basis difference delta = alpha2 - alpha1 [deg]")
    plt.ylabel("P(+ alpha2 | + alpha1)")
    plt.title("B13.3 sequential rotated-basis observation")
    plt.legend()
    save_fig_local("B13_3_sequential_observation_curve.png")

    summary = {
        "experiment": "B13_3_sequential_rotated_basis_observation",
        "parameters": {
            "seed": seed,
            "alpha1_deg": float(alpha1 * 180 / np.pi),
            "alpha2_values_deg": [float(x * 180 / np.pi) for x in alpha2_values],
            "initial_theta_deg": float(initial_theta * 180 / np.pi),
            "a": a,
            "b": b,
            "sigma": sigma,
            "eta": eta,
            "steps1": steps1,
            "steps2": steps2,
            "n_trials_stage1": n_trials_stage1,
            "n_trials_stage2_per_parent": n_trials_stage2_per_parent,
        },
        "metrics": {
            "rmse_vs_cos2_delta": rmse,
            "mean_shift": mean_shift,
            "max_abs_error": max_abs_error,
            "stage1_P_plus": float(n_plus1 / n_trials_stage1),
        },
        "interpretation": (
            "Sequential toy test for measurement-like update. "
            "This compares conditional basin selection with cos² basis-difference reference. "
            "It is not a quantum measurement derivation."
        ),
    }

    save_json_local(summary, "B13_3_sequential_observation_summary.json")

    print("Sequential observation experiment complete.")
    print(json.dumps(summary, indent=2))

    return df, summary
