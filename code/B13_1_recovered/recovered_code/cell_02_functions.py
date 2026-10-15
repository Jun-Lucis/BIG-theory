# Computational functions copied verbatim; original notebook cell 2.

def basis_vectors(alpha):
    """
    Rotated observation basis:
    e_plus(alpha)  = (cos alpha, sin alpha)
    e_minus(alpha) = (-sin alpha, cos alpha)
    """
    e_plus = np.array([np.cos(alpha), np.sin(alpha)])
    e_minus = np.array([-np.sin(alpha), np.cos(alpha)])
    return e_plus, e_minus

def grad_rotated_batch(h, alpha, a=4.0, b=1.0):
    """
    Batch gradient of:
    E = a(y_plus^2 + y_minus^2 - 1)^2 + b y_plus^2 y_minus^2
    where y_plus  = h dot e_plus(alpha)
          y_minus = h dot e_minus(alpha)
    """
    e_plus, e_minus = basis_vectors(alpha)

    y_plus = h @ e_plus
    y_minus = h @ e_minus
    r2 = y_plus**2 + y_minus**2

    gy_plus = 4*a*(r2 - 1)*y_plus + 2*b*y_plus*(y_minus**2)
    gy_minus = 4*a*(r2 - 1)*y_minus + 2*b*y_minus*(y_plus**2)

    grad = gy_plus[:, None] * e_plus[None, :] + gy_minus[:, None] * e_minus[None, :]
    return grad

def simulate_rotated_basis_trials(
    theta,
    alpha,
    rng,
    a=4.0,
    b=1.0,
    sigma=0.35,
    eta=0.01,
    steps=350,
    n_trials=200,
    init_jitter=0.0,
):
    """
    Vectorized simulation for many noisy trials.
    Initial state is h0=(cos theta, sin theta).
    Outcome + is classified by |y_plus| >= |y_minus|.
    """
    h0 = np.array([np.cos(theta), np.sin(theta)])
    h = np.repeat(h0[None, :], n_trials, axis=0)

    if init_jitter > 0:
        h += init_jitter * rng.normal(size=h.shape)

    for _ in range(steps):
        g = grad_rotated_batch(h, alpha, a=a, b=b)
        h = h - eta * g + sigma * np.sqrt(eta) * rng.normal(size=h.shape)

        # numerical guard
        norm = np.linalg.norm(h, axis=1)
        mask = norm > 20
        if np.any(mask):
            h[mask] = h[mask] / norm[mask, None] * 20

    e_plus, e_minus = basis_vectors(alpha)
    y_plus = h @ e_plus
    y_minus = h @ e_minus

    outcome_plus = np.abs(y_plus) >= np.abs(y_minus)
    return float(np.mean(outcome_plus))

def run_rotated_basis_experiment(
    seed=123,
    alphas=(0.0, np.pi/12, np.pi/8, np.pi/6, np.pi/4),
    n_theta=25,
    n_trials=200,
    steps=350,
    a=4.0,
    b=1.0,
    sigma=0.35,
    eta=0.01,
):
    rng = np.random.default_rng(seed)

    theta_grid = np.linspace(0, np.pi/2, n_theta)
    rows = []

    for alpha in alphas:
        print(f"Running alpha={alpha:.4f} rad / {alpha*180/np.pi:.1f} deg")

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
                "alpha": alpha,
                "alpha_deg": alpha * 180 / np.pi,
                "theta": theta,
                "theta_deg": theta * 180 / np.pi,
                "p_plus": p_plus,
                "p_ref_cos2_theta_minus_alpha": p_ref,
                "error": p_plus - p_ref,
            })

    df = pd.DataFrame(rows)

    summary_rows = []
    for alpha, sub in df.groupby("alpha"):
        rmse = float(np.sqrt(np.mean(sub["error"]**2)))
        mean_shift = float(np.mean(sub["error"]))
        max_abs_error = float(np.max(np.abs(sub["error"])))

        summary_rows.append({
            "alpha": float(alpha),
            "alpha_deg": float(alpha * 180 / np.pi),
            "rmse_vs_basis_born_like": rmse,
            "mean_shift": mean_shift,
            "max_abs_error": max_abs_error,
        })

        print(
            f"alpha={alpha*180/np.pi:5.1f} deg "
            f"RMSE={rmse:.4f}, shift={mean_shift:+.4f}, max_err={max_abs_error:.4f}"
        )

    summary_df = pd.DataFrame(summary_rows)

    save_csv_local(df, "A_rotated_basis_selection_curves.csv")
    save_csv_local(summary_df, "A_rotated_basis_rmse_summary.csv")

    # Figure 1: RMSE vs alpha
    plt.figure(figsize=(7, 4.5))
    plt.plot(summary_df["alpha_deg"], summary_df["rmse_vs_basis_born_like"], marker="o")
    plt.xlabel("basis angle alpha [deg]")
    plt.ylabel("RMSE vs cos^2(theta-alpha)")
    plt.title("Rotated-basis Born-like reference comparison")
    save_fig_local("A_rotated_basis_rmse_vs_alpha.png")

    # Figure 2: overlay curves
    plt.figure(figsize=(8, 5.5))
    for alpha, sub in df.groupby("alpha"):
        sub = sub.sort_values("theta_deg")
        label = f"model alpha={alpha*180/np.pi:.1f} deg"
        ref_label = f"ref alpha={alpha*180/np.pi:.1f} deg"

        plt.plot(sub["theta_deg"], sub["p_plus"], marker="o", linewidth=1.5, label=label)
        plt.plot(sub["theta_deg"], sub["p_ref_cos2_theta_minus_alpha"], linestyle="--", linewidth=1.0, label=ref_label)

    plt.xlabel("initial angle theta [deg]")
    plt.ylabel("P(+)")
    plt.title("Rotated-basis selection curves")
    plt.legend(fontsize=8, ncol=2)
    save_fig_local("A_rotated_basis_curves_overlay.png")

    best = summary_df.loc[summary_df["rmse_vs_basis_born_like"].idxmin()].to_dict()
    worst = summary_df.loc[summary_df["rmse_vs_basis_born_like"].idxmax()].to_dict()

    summary = {
        "experiment": "B13_1_rotated_basis_binary_observation",
        "interpretation": (
            "Tests whether the finite-noise basin-selection regime follows a rotated "
            "basis-aware Born-like reference curve cos^2(theta-alpha). "
            "This is not a derivation of the Born rule."
        ),
        "parameters": {
            "seed": seed,
            "a": a,
            "b": b,
            "sigma": sigma,
            "eta": eta,
            "steps": steps,
            "n_trials": n_trials,
            "n_theta": n_theta,
            "alphas_deg": [float(x * 180 / np.pi) for x in alphas],
        },
        "best_case": best,
        "worst_case": worst,
    }

    save_json_local(summary, "A_rotated_basis_summary.json")

    print("Rotated-basis experiment complete.")
    print("Best case:", best)
    print("Worst case:", worst)

    return df, summary_df, summary
