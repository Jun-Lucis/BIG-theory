"""Original B13 computational functions, extracted from Untitled66.ipynb.
Function bodies are unchanged. Top-level experiment calls are excluded.
Use reproduce_b13.py for portable file output.
"""

import json
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Notebook cell 2, lines 6-21
def grad_binary(h, a=4.0, b=8.0, lambda_obs=0.0, F_align=1.0, H=(1.0, 1.0)):
    """
    Energy:
    E = a(r^2 - 1)^2 + b h_+^2 h_-^2
        - lambda_obs F_align (h_+ H_+ + h_- H_-)

    This is a spin-like binary observation toy model.
    It does not derive quantum measurement or the Born rule.
    """
    hp, hm = h
    Hp, Hm = H
    r2 = hp*hp + hm*hm

    d_hp = 4*a*(r2 - 1)*hp + 2*b*hp*(hm**2) - lambda_obs*F_align*Hp
    d_hm = 4*a*(r2 - 1)*hm + 2*b*hm*(hp**2) - lambda_obs*F_align*Hm
    return np.array([d_hp, d_hm], dtype=float)

# Notebook cell 2, lines 24-62
def simulate_binary_trial(
    h0,
    rng,
    a=4.0,
    b=8.0,
    lambda_obs=0.0,
    F_align=1.0,
    H=(1.0, 1.0),
    sigma=0.08,
    eta=0.01,
    steps=600,
    allow_negative=False,
):
    h = np.array(h0, dtype=float)

    H = np.array(H, dtype=float)
    norm = np.linalg.norm(H)
    if norm > 0:
        H = H / norm

    for _ in range(steps):
        g = grad_binary(h, a=a, b=b, lambda_obs=lambda_obs, F_align=F_align, H=H)
        h = h - eta * g + sigma * np.sqrt(eta) * rng.normal(size=2)

        if not allow_negative:
            h = np.maximum(h, 0.0)

        # soft numerical guard
        if np.linalg.norm(h) > 5:
            h = h / np.linalg.norm(h) * 5

    if abs(h[0]) > abs(h[1]):
        outcome = "+"
    elif abs(h[1]) > abs(h[0]):
        outcome = "-"
    else:
        outcome = "tie"

    return outcome, h

# Notebook cell 2, lines 65-210
def run_experiment_A(
    seed=123,
    a=4.0,
    b=8.0,
    lambda_obs=0.0,
    F_align=1.0,
    H=(1.0, 1.0),
    sigma=0.08,
    eta=0.01,
    steps=600,
    n_trials=300,
    n_theta=25,
    map_n=31,
    map_trials=40,
):
    rng = np.random.default_rng(seed)

    # ---- Born-like curve comparison ----
    rows = []
    thetas = np.linspace(0, np.pi/2, n_theta)

    for theta in thetas:
        h0 = np.array([np.cos(theta), np.sin(theta)])
        plus_count = 0
        minus_count = 0
        tie_count = 0

        for _ in range(n_trials):
            outcome, _ = simulate_binary_trial(
                h0, rng,
                a=a, b=b,
                lambda_obs=lambda_obs,
                F_align=F_align,
                H=H,
                sigma=sigma,
                eta=eta,
                steps=steps,
            )
            plus_count += (outcome == "+")
            minus_count += (outcome == "-")
            tie_count += (outcome == "tie")

        p_plus = plus_count / n_trials
        p_minus = minus_count / n_trials
        p_tie = tie_count / n_trials
        born_like = np.cos(theta)**2

        rows.append({
            "theta": theta,
            "h_plus_0": h0[0],
            "h_minus_0": h0[1],
            "p_plus": p_plus,
            "p_minus": p_minus,
            "p_tie": p_tie,
            "born_like_cos2": born_like,
            "abs_error": abs(p_plus - born_like),
        })

    df = pd.DataFrame(rows)
    rmse = float(np.sqrt(np.mean((df["p_plus"] - df["born_like_cos2"])**2)))

    save_csv(df, "A_binary_selection_curve.csv")

    plt.figure(figsize=(7, 4.5))
    plt.plot(df["theta"], df["p_plus"], marker="o", label="B13 toy model: estimated p(+)")
    plt.plot(df["theta"], df["born_like_cos2"], linestyle="--", label="Born-like comparison: cos^2(theta)")
    plt.xlabel("theta")
    plt.ylabel("selection probability")
    plt.title(f"Binary observation toy model vs Born-like curve\nRMSE = {rmse:.4f}")
    plt.legend()
    save_fig("A_binary_selection_vs_born_like.png")

    # ---- Basin map ----
    grid = np.linspace(0, 1, map_n)
    basin = np.zeros((map_n, map_n))

    for i, hp0 in enumerate(grid):
        for j, hm0 in enumerate(grid):
            plus_count = 0
            h0 = np.array([hp0, hm0])

            # avoid exactly zero vector
            if np.linalg.norm(h0) < 1e-12:
                h0 = np.array([1e-6, 1e-6])

            for _ in range(map_trials):
                outcome, _ = simulate_binary_trial(
                    h0, rng,
                    a=a, b=b,
                    lambda_obs=lambda_obs,
                    F_align=F_align,
                    H=H,
                    sigma=sigma,
                    eta=eta,
                    steps=steps,
                )
                plus_count += (outcome == "+")

            basin[j, i] = plus_count / map_trials

    basin_df = pd.DataFrame(basin, index=grid, columns=grid)
    basin_path = OUTDIR / "A_binary_basin_map_p_plus.csv"
    basin_df.to_csv(basin_path)
    backup_file(basin_path)

    plt.figure(figsize=(5.8, 5))
    plt.imshow(
        basin,
        origin="lower",
        extent=[0, 1, 0, 1],
        aspect="auto",
        vmin=0,
        vmax=1,
    )
    plt.colorbar(label="p(+)")
    plt.xlabel("h_plus(0)")
    plt.ylabel("h_minus(0)")
    plt.title("Binary basin map: probability of + outcome")
    save_fig("A_binary_basin_map.png")

    summary = {
        "experiment": "A_binary_observation_toy_model",
        "interpretation": "This tests Born-like selection. It does not derive the Born rule.",
        "rmse_vs_born_like_cos2": rmse,
        "parameters": {
            "a": a,
            "b": b,
            "lambda_obs": lambda_obs,
            "F_align": F_align,
            "H": list(H),
            "sigma": sigma,
            "eta": eta,
            "steps": steps,
            "n_trials": n_trials,
            "n_theta": n_theta,
            "map_n": map_n,
            "map_trials": map_trials,
            "seed": seed,
        }
    }
    save_json(summary, "A_experiment_summary.json")

    print("Experiment A complete.")
    print("RMSE vs Born-like cos^2:", rmse)

    return df, basin, summary

# Notebook cell 4, lines 7-59
def run_binary_curve_only(
    seed=123,
    a=4.0,
    b=8.0,
    lambda_obs=0.0,
    F_align=1.0,
    H=(1.0, 1.0),
    sigma=0.08,
    eta=0.01,
    steps=400,
    n_trials=120,
    n_theta=17,
):
    rng = np.random.default_rng(seed)
    rows = []
    thetas = np.linspace(0, np.pi/2, n_theta)

    for theta in thetas:
        h0 = np.array([np.cos(theta), np.sin(theta)])
        plus_count = 0
        minus_count = 0
        tie_count = 0

        for _ in range(n_trials):
            outcome, _ = simulate_binary_trial(
                h0,
                rng,
                a=a,
                b=b,
                lambda_obs=lambda_obs,
                F_align=F_align,
                H=H,
                sigma=sigma,
                eta=eta,
                steps=steps,
            )
            plus_count += (outcome == "+")
            minus_count += (outcome == "-")
            tie_count += (outcome == "tie")

        p_plus = plus_count / n_trials
        born_like = np.cos(theta) ** 2

        rows.append({
            "theta": theta,
            "p_plus": p_plus,
            "born_like_cos2": born_like,
            "abs_error": abs(p_plus - born_like),
        })

    df = pd.DataFrame(rows)
    rmse = float(np.sqrt(np.mean((df["p_plus"] - df["born_like_cos2"]) ** 2)))
    return df, rmse

# Notebook cell 4, lines 62-174
def sweep_binary_parameters(
    seed=123,
    sigmas=(0.0, 0.02, 0.05, 0.08, 0.12, 0.18, 0.25, 0.35),
    bs=(0.5, 1.0, 2.0, 4.0, 8.0, 16.0),
    a=4.0,
    lambda_obs=0.0,
    F_align=1.0,
    H=(1.0, 1.0),
    eta=0.01,
    steps=400,
    n_trials=120,
    n_theta=17,
):
    summary_rows = []
    curves = {}

    for b in bs:
        for sigma in sigmas:
            df, rmse = run_binary_curve_only(
                seed=seed,
                a=a,
                b=b,
                lambda_obs=lambda_obs,
                F_align=F_align,
                H=H,
                sigma=sigma,
                eta=eta,
                steps=steps,
                n_trials=n_trials,
                n_theta=n_theta,
            )

            key = f"b={b}_sigma={sigma}"
            curves[key] = df.copy()

            summary_rows.append({
                "b": b,
                "sigma": sigma,
                "rmse_vs_born_like": rmse,
            })

            print(f"b={b:>5}, sigma={sigma:>5} -> RMSE={rmse:.4f}")

    summary_df = pd.DataFrame(summary_rows)
    save_csv(summary_df, "A_parameter_sweep_rmse.csv")

    # RMSE heatmap
    pivot = summary_df.pivot(index="b", columns="sigma", values="rmse_vs_born_like")

    plt.figure(figsize=(8, 5))
    plt.imshow(
        pivot.values,
        origin="lower",
        aspect="auto",
        extent=[
            min(sigmas), max(sigmas),
            min(bs), max(bs)
        ],
    )
    plt.colorbar(label="RMSE vs Born-like cos^2")
    plt.xlabel("noise sigma")
    plt.ylabel("barrier strength b")
    plt.title("Experiment A parameter sweep: RMSE vs Born-like curve")
    save_fig("A_parameter_sweep_rmse_heatmap.png")

    # best parameter
    best_row = summary_df.loc[summary_df["rmse_vs_born_like"].idxmin()]
    best_b = float(best_row["b"])
    best_sigma = float(best_row["sigma"])
    best_rmse = float(best_row["rmse_vs_born_like"])

    best_key = f"b={best_b}_sigma={best_sigma}"
    best_df = curves[best_key]

    save_csv(best_df, "A_best_curve_from_parameter_sweep.csv")

    plt.figure(figsize=(7, 4.5))
    plt.plot(best_df["theta"], best_df["p_plus"], marker="o", label="best B13 toy curve")
    plt.plot(best_df["theta"], best_df["born_like_cos2"], linestyle="--", label="Born-like cos^2(theta)")
    plt.xlabel("theta")
    plt.ylabel("selection probability")
    plt.title(f"Best curve in sweep: b={best_b}, sigma={best_sigma}, RMSE={best_rmse:.4f}")
    plt.legend()
    save_fig("A_best_curve_from_parameter_sweep.png")

    result = {
        "experiment": "A_parameter_sweep",
        "interpretation": (
            "This checks whether the binary basin model approaches a Born-like curve. "
            "It does not derive the Born rule."
        ),
        "best_b": best_b,
        "best_sigma": best_sigma,
        "best_rmse": best_rmse,
        "parameters": {
            "a": a,
            "lambda_obs": lambda_obs,
            "F_align": F_align,
            "H": list(H),
            "eta": eta,
            "steps": steps,
            "n_trials": n_trials,
            "n_theta": n_theta,
            "seed": seed,
        }
    }

    save_json(result, "A_parameter_sweep_summary.json")

    print("Parameter sweep complete.")
    print("Best:", result)

    return summary_df, curves, result

# Notebook cell 5, lines 7-125
def robust_check_best_binary(
    seeds=(101, 202, 303, 404, 505),
    b=1.0,
    sigma=0.35,
    a=4.0,
    lambda_obs=0.0,
    F_align=1.0,
    H=(1.0, 1.0),
    eta=0.01,
    steps=400,
    n_trials=300,
    n_theta=31,
):
    all_rows = []
    rmse_rows = []

    for seed in seeds:
        df, rmse = run_binary_curve_only(
            seed=seed,
            a=a,
            b=b,
            lambda_obs=lambda_obs,
            F_align=F_align,
            H=H,
            sigma=sigma,
            eta=eta,
            steps=steps,
            n_trials=n_trials,
            n_theta=n_theta,
        )

        df["seed"] = seed
        all_rows.append(df)

        rmse_rows.append({
            "seed": seed,
            "rmse_vs_born_like": rmse,
        })

        print(f"seed={seed} -> RMSE={rmse:.4f}")

    all_df = pd.concat(all_rows, ignore_index=True)
    rmse_df = pd.DataFrame(rmse_rows)

    grouped = all_df.groupby("theta").agg(
        p_plus_mean=("p_plus", "mean"),
        p_plus_std=("p_plus", "std"),
        born_like_cos2=("born_like_cos2", "mean"),
    ).reset_index()

    grouped["p_plus_sem"] = grouped["p_plus_std"] / np.sqrt(len(seeds))
    grouped["ci95_low"] = grouped["p_plus_mean"] - 1.96 * grouped["p_plus_sem"]
    grouped["ci95_high"] = grouped["p_plus_mean"] + 1.96 * grouped["p_plus_sem"]

    mean_rmse = float(rmse_df["rmse_vs_born_like"].mean())
    std_rmse = float(rmse_df["rmse_vs_born_like"].std())

    save_csv(all_df, "A_best_robust_all_seed_curves.csv")
    save_csv(grouped, "A_best_robust_mean_curve.csv")
    save_csv(rmse_df, "A_best_robust_rmse_by_seed.csv")

    plt.figure(figsize=(7, 4.5))
    plt.plot(
        grouped["theta"],
        grouped["p_plus_mean"],
        marker="o",
        label="B13 toy model mean p(+)"
    )
    plt.fill_between(
        grouped["theta"],
        grouped["ci95_low"],
        grouped["ci95_high"],
        alpha=0.25,
        label="approx. 95% CI over seeds"
    )
    plt.plot(
        grouped["theta"],
        grouped["born_like_cos2"],
        linestyle="--",
        label="Born-like cos^2(theta)"
    )
    plt.xlabel("theta")
    plt.ylabel("selection probability")
    plt.title(
        f"Robustness check: b={b}, sigma={sigma}\n"
        f"mean RMSE={mean_rmse:.4f}, std={std_rmse:.4f}"
    )
    plt.legend()
    save_fig("A_best_robust_mean_curve.png")

    summary = {
        "experiment": "A_best_parameter_robustness_check",
        "interpretation": (
            "Checks whether the best Born-like regime is robust across random seeds. "
            "This does not derive the Born rule."
        ),
        "b": b,
        "sigma": sigma,
        "mean_rmse": mean_rmse,
        "std_rmse": std_rmse,
        "seeds": list(seeds),
        "parameters": {
            "a": a,
            "lambda_obs": lambda_obs,
            "F_align": F_align,
            "H": list(H),
            "eta": eta,
            "steps": steps,
            "n_trials": n_trials,
            "n_theta": n_theta,
        }
    }

    save_json(summary, "A_best_robust_summary.json")

    print("Robustness check complete.")
    print(summary)

    return grouped, rmse_df, summary

# Notebook cell 6, lines 8-198
def sweep_observer_coupling(
    seed=123,
    lambdas=(0.0, 0.05, 0.1, 0.2, 0.4, 0.8),
    observer_axes=((1.0, 1.0), (1.0, 0.0), (0.0, 1.0), (0.8, 0.6)),
    a=4.0,
    b=1.0,
    sigma=0.35,
    F_align=1.0,
    eta=0.01,
    steps=400,
    n_trials=240,
    n_theta=25,
):
    rows = []
    curves = {}

    for H in observer_axes:
        H_arr = np.array(H, dtype=float)
        H_arr = H_arr / max(np.linalg.norm(H_arr), 1e-12)
        H_tuple = (float(H_arr[0]), float(H_arr[1]))
        H_label = f"H=({H_tuple[0]:.2f},{H_tuple[1]:.2f})"

        for lam in lambdas:
            df, rmse = run_binary_curve_only(
                seed=seed,
                a=a,
                b=b,
                lambda_obs=lam,
                F_align=F_align,
                H=H_tuple,
                sigma=sigma,
                eta=eta,
                steps=steps,
                n_trials=n_trials,
                n_theta=n_theta,
            )

            # bias metrics
            mean_shift = float(np.mean(df["p_plus"] - df["born_like_cos2"]))
            max_abs_error = float(np.max(np.abs(df["p_plus"] - df["born_like_cos2"])))

            key = f"{H_label}_lambda={lam}"
            curves[key] = df.copy()

            rows.append({
                "H_plus": H_tuple[0],
                "H_minus": H_tuple[1],
                "H_label": H_label,
                "lambda_obs": lam,
                "rmse_vs_born_like": rmse,
                "mean_shift_p_plus_minus_born": mean_shift,
                "max_abs_error": max_abs_error,
            })

            print(
                f"{H_label}, lambda={lam:>4} "
                f"-> RMSE={rmse:.4f}, shift={mean_shift:+.4f}"
            )

    summary_df = pd.DataFrame(rows)
    save_csv(summary_df, "A_observer_coupling_sweep_summary.csv")

    # Plot RMSE vs lambda for each observer axis
    plt.figure(figsize=(7.5, 4.8))
    for H_label, sub in summary_df.groupby("H_label"):
        sub = sub.sort_values("lambda_obs")
        plt.plot(
            sub["lambda_obs"],
            sub["rmse_vs_born_like"],
            marker="o",
            label=H_label
        )

    plt.xlabel("lambda_obs")
    plt.ylabel("RMSE vs Born-like cos^2")
    plt.title("Observer-coupling sweep: effect on Born-like regime")
    plt.legend()
    save_fig("A_observer_coupling_rmse_vs_lambda.png")

    # Plot mean shift vs lambda
    plt.figure(figsize=(7.5, 4.8))
    for H_label, sub in summary_df.groupby("H_label"):
        sub = sub.sort_values("lambda_obs")
        plt.plot(
            sub["lambda_obs"],
            sub["mean_shift_p_plus_minus_born"],
            marker="o",
            label=H_label
        )

    plt.axhline(0, linestyle="--")
    plt.xlabel("lambda_obs")
    plt.ylabel("mean shift: p(+) - Born-like")
    plt.title("Observer-coupling sweep: directional bias")
    plt.legend()
    save_fig("A_observer_coupling_mean_shift.png")

    # Best and worst cases
    best_row = summary_df.loc[summary_df["rmse_vs_born_like"].idxmin()]
    worst_row = summary_df.loc[summary_df["rmse_vs_born_like"].idxmax()]

    best_key = (
        f"H=({best_row['H_plus']:.2f},{best_row['H_minus']:.2f})"
        f"_lambda={best_row['lambda_obs']}"
    )
    worst_key = (
        f"H=({worst_row['H_plus']:.2f},{worst_row['H_minus']:.2f})"
        f"_lambda={worst_row['lambda_obs']}"
    )

    best_df = curves[best_key]
    worst_df = curves[worst_key]

    save_csv(best_df, "A_observer_coupling_best_curve.csv")
    save_csv(worst_df, "A_observer_coupling_worst_curve.csv")

    plt.figure(figsize=(7, 4.5))
    plt.plot(
        best_df["theta"],
        best_df["p_plus"],
        marker="o",
        label=f"best toy curve: {best_key}"
    )
    plt.plot(
        best_df["theta"],
        best_df["born_like_cos2"],
        linestyle="--",
        label="Born-like cos^2(theta)"
    )
    plt.xlabel("theta")
    plt.ylabel("selection probability")
    plt.title(
        "Best observer-coupling curve\n"
        f"RMSE={best_row['rmse_vs_born_like']:.4f}"
    )
    plt.legend()
    save_fig("A_observer_coupling_best_curve.png")

    plt.figure(figsize=(7, 4.5))
    plt.plot(
        worst_df["theta"],
        worst_df["p_plus"],
        marker="o",
        label=f"worst toy curve: {worst_key}"
    )
    plt.plot(
        worst_df["theta"],
        worst_df["born_like_cos2"],
        linestyle="--",
        label="Born-like cos^2(theta)"
    )
    plt.xlabel("theta")
    plt.ylabel("selection probability")
    plt.title(
        "Worst observer-coupling curve\n"
        f"RMSE={worst_row['rmse_vs_born_like']:.4f}"
    )
    plt.legend()
    save_fig("A_observer_coupling_worst_curve.png")

    result = {
        "experiment": "A_observer_coupling_sweep",
        "interpretation": (
            "Tests whether observer coupling preserves, biases, or destroys "
            "the finite-noise Born-like selection regime. "
            "This does not derive quantum measurement or the Born rule."
        ),
        "base_regime": {
            "a": a,
            "b": b,
            "sigma": sigma,
            "F_align": F_align,
            "eta": eta,
            "steps": steps,
            "n_trials": n_trials,
            "n_theta": n_theta,
            "seed": seed,
        },
        "best_case": best_row.to_dict(),
        "worst_case": worst_row.to_dict(),
    }

    save_json(result, "A_observer_coupling_sweep_result.json")

    print("Observer coupling sweep complete.")
    print("Best case:")
    print(best_row)
    print("Worst case:")
    print(worst_row)

    return summary_df, curves, result

# Notebook cell 7, lines 6-28
def energy_self(h, alpha=1.0, well_strength=2.0, lambda_self=0.5,
                gamma=0.5, K_scale=0.0, A_diag=(1.0, 0.8)):
    """
    Reduced self-observation energy in 2D hidden-depth space.

    E = alpha/4 (||h||^2 - 1)^2
        + well_strength h1^2 h2^2
        - lambda_self/2 h^T A h
        + gamma/4 ||h||^4
        + K_scale/2 ||h||^2
    """
    h = np.array(h, dtype=float)
    h1, h2 = h
    r2 = h1*h1 + h2*h2
    A1, A2 = A_diag

    return (
        alpha/4 * (r2 - 1)**2
        + well_strength * h1*h1*h2*h2
        - lambda_self/2 * (A1*h1*h1 + A2*h2*h2)
        + gamma/4 * r2*r2
        + K_scale/2 * r2
    )

# Notebook cell 7, lines 31-46
def grad_self(h, alpha=1.0, well_strength=2.0, lambda_self=0.5,
              gamma=0.5, K_scale=0.0, A_diag=(1.0, 0.8)):
    h = np.array(h, dtype=float)
    h1, h2 = h
    r2 = h1*h1 + h2*h2
    A1, A2 = A_diag

    g = alpha * (r2 - 1) * h
    g += np.array([
        2 * well_strength * h1 * h2*h2,
        2 * well_strength * h2 * h1*h1
    ])
    g += -lambda_self * np.array([A1*h1, A2*h2])
    g += gamma * r2 * h
    g += K_scale * h
    return g

# Notebook cell 7, lines 49-68
def hessian_self(h, alpha=1.0, well_strength=2.0, lambda_self=0.5,
                 gamma=0.5, K_scale=0.0, A_diag=(1.0, 0.8)):
    h = np.array(h, dtype=float)
    h1, h2 = h
    r2 = h1*h1 + h2*h2
    A1, A2 = A_diag
    I = np.eye(2)
    outer = np.outer(h, h)

    H = alpha * ((r2 - 1) * I + 2 * outer)

    H += np.array([
        [2 * well_strength * h2*h2, 4 * well_strength * h1*h2],
        [4 * well_strength * h1*h2, 2 * well_strength * h1*h1]
    ])

    H += -lambda_self * np.diag([A1, A2])
    H += gamma * (r2 * I + 2 * outer)
    H += K_scale * I
    return H

# Notebook cell 7, lines 71-89
def minimize_self_from_initial(
    h0,
    eta_min=0.01,
    steps=3000,
    **params
):
    h = np.array(h0, dtype=float)

    for _ in range(steps):
        g = grad_self(h, **params)
        h = h - eta_min * g

        if np.linalg.norm(h) > 20:
            h = h / np.linalg.norm(h) * 20

        if np.linalg.norm(g) < 1e-8:
            break

    return h

# Notebook cell 7, lines 92-100
def unique_points(points, tol=1e-2):
    unique = []
    for p in points:
        if not unique:
            unique.append(p)
        else:
            if min(np.linalg.norm(p - q) for q in unique) > tol:
                unique.append(p)
    return unique

# Notebook cell 7, lines 103-129
def find_self_fixed_points(
    seed=123,
    n_initial=80,
    initial_radius=2.0,
    eta_min=0.01,
    steps=3000,
    **params
):
    rng = np.random.default_rng(seed)
    points = []

    # include structured initial points
    structured = [
        [1, 0], [-1, 0], [0, 1], [0, -1],
        [1, 1], [-1, 1], [1, -1], [-1, -1],
        [0.1, 0.1], [-0.1, 0.1]
    ]

    for h0 in structured:
        points.append(minimize_self_from_initial(h0, eta_min=eta_min, steps=steps, **params))

    for _ in range(n_initial):
        h0 = rng.normal(size=2)
        h0 = initial_radius * h0 / max(np.linalg.norm(h0), 1e-12)
        points.append(minimize_self_from_initial(h0, eta_min=eta_min, steps=steps, **params))

    return unique_points(points, tol=1e-2)

# Notebook cell 7, lines 132-161
def classify_self_model(fixed_points, eta_update=0.05, rigid_threshold=20.0, sensitive_threshold=0.05, **params):
    if len(fixed_points) == 0:
        return "no_fixed_point", 0

    all_eigs = []
    for p in fixed_points:
        H = hessian_self(p, **params)
        eigs = np.linalg.eigvalsh(H)
        all_eigs.extend(list(eigs))

    all_eigs = np.array(all_eigs)
    min_eig = float(np.min(all_eigs))
    max_eig = float(np.max(all_eigs))

    if min_eig < -1e-6:
        return "unstable", 1

    if eta_update * max_eig >= 2:
        return "numerically_unstable", 2

    if len(fixed_points) >= 2:
        return "multistable", 3

    if max_eig > rigid_threshold:
        return "overly_rigid", 4

    if min_eig < sensitive_threshold:
        return "noise_sensitive", 5

    return "stable", 6

# Notebook cell 7, lines 164-310
def run_experiment_B(
    seed=123,
    alpha=1.0,
    well_strength=2.0,
    lambda_self=0.5,
    gamma=0.5,
    K_scale=0.0,
    A_diag=(1.0, 0.8),
    eta_update=0.05,
    n_initial=80,
):
    params = {
        "alpha": alpha,
        "well_strength": well_strength,
        "lambda_self": lambda_self,
        "gamma": gamma,
        "K_scale": K_scale,
        "A_diag": A_diag,
    }

    fixed = find_self_fixed_points(seed=seed, n_initial=n_initial, **params)

    fixed_rows = []
    for k, p in enumerate(fixed):
        Hmat = hessian_self(p, **params)
        eigs = np.linalg.eigvalsh(Hmat)
        fixed_rows.append({
            "index": k,
            "h1": float(p[0]),
            "h2": float(p[1]),
            "energy": float(energy_self(p, **params)),
            "eig_min": float(np.min(eigs)),
            "eig_max": float(np.max(eigs)),
            "eigs": [float(x) for x in eigs],
        })

    label, code = classify_self_model(fixed, eta_update=eta_update, **params)

    summary = {
        "experiment": "B_self_observation_Hessian_stability",
        "interpretation": "This classifies reduced self-model stability. It does not explain consciousness.",
        "classification": label,
        "classification_code": code,
        "n_fixed_points": len(fixed),
        "fixed_points": fixed_rows,
        "parameters": {
            "alpha": alpha,
            "well_strength": well_strength,
            "lambda_self": lambda_self,
            "gamma": gamma,
            "K_scale": K_scale,
            "A_diag": list(A_diag),
            "eta_update": eta_update,
            "n_initial": n_initial,
            "seed": seed,
        }
    }

    save_json(summary, "B_self_observation_single_summary.json")

    # ---- landscape plot ----
    xs = np.linspace(-2, 2, 180)
    ys = np.linspace(-2, 2, 180)
    Z = np.zeros((len(ys), len(xs)))

    for iy, y in enumerate(ys):
        for ix, x in enumerate(xs):
            Z[iy, ix] = energy_self([x, y], **params)

    plt.figure(figsize=(6, 5.5))
    plt.contourf(xs, ys, Z, levels=50)
    plt.colorbar(label="E_self")
    if fixed:
        fp = np.array(fixed)
        plt.scatter(fp[:, 0], fp[:, 1], marker="x", s=80, label="fixed points")
        plt.legend()
    plt.xlabel("h1")
    plt.ylabel("h2")
    plt.title(f"Self-observation landscape\nclassification: {label}")
    save_fig("B_self_observation_landscape_fixed_points.png")

    # ---- stability map over lambda_self and eta ----
    lambda_grid = np.linspace(0.0, 2.0, 25)
    eta_grid = np.linspace(0.005, 0.25, 25)

    code_map = np.zeros((len(eta_grid), len(lambda_grid)))

    rows = []
    for i, eta_val in enumerate(eta_grid):
        for j, lam in enumerate(lambda_grid):
            p2 = dict(params)
            p2["lambda_self"] = float(lam)

            fps = find_self_fixed_points(
                seed=seed,
                n_initial=40,
                eta_min=0.01,
                steps=2000,
                **p2
            )
            lab, c = classify_self_model(fps, eta_update=float(eta_val), **p2)
            code_map[i, j] = c
            rows.append({
                "eta": float(eta_val),
                "lambda_self": float(lam),
                "classification": lab,
                "code": int(c),
                "n_fixed_points": len(fps),
            })

    map_df = pd.DataFrame(rows)
    save_csv(map_df, "B_self_stability_code_map.csv")

    plt.figure(figsize=(7, 5))
    plt.imshow(
        code_map,
        origin="lower",
        extent=[lambda_grid[0], lambda_grid[-1], eta_grid[0], eta_grid[-1]],
        aspect="auto",
        vmin=0,
        vmax=6,
    )
    plt.colorbar(label="classification code")
    plt.xlabel("lambda_self")
    plt.ylabel("eta")
    plt.title("Self-observation stability map\n0 no fixed, 1 unstable, 2 num unstable, 3 multistable, 4 rigid, 5 sensitive, 6 stable")
    save_fig("B_self_observation_stability_map.png")

    save_json({
        "single_summary_file": "B_self_observation_single_summary.json",
        "stability_map_file": "B_self_stability_code_map.csv",
        "classification_codes": {
            "0": "no_fixed_point",
            "1": "unstable",
            "2": "numerically_unstable",
            "3": "multistable",
            "4": "overly_rigid",
            "5": "noise_sensitive",
            "6": "stable",
        }
    }, "B_experiment_summary.json")

    print("Experiment B complete.")
    print("Classification:", label)
    print("Fixed points:", len(fixed))

    return summary, map_df

# Notebook cell 10, lines 6-15
def classify_basin_2d(h):
    """
    Classify final hidden-depth state into four self-model basins.
    """
    h1, h2 = h

    if abs(h1) >= abs(h2):
        return "x+" if h1 >= 0 else "x-"
    else:
        return "y+" if h2 >= 0 else "y-"

# Notebook cell 10, lines 18-36
def simulate_self_noisy(
    h0,
    rng,
    sigma=0.05,
    eta=0.01,
    steps=2000,
    **params
):
    h = np.array(h0, dtype=float)

    for _ in range(steps):
        g = grad_self(h, **params)
        h = h - eta * g + sigma * np.sqrt(eta) * rng.normal(size=2)

        # numerical guard
        if np.linalg.norm(h) > 20:
            h = h / np.linalg.norm(h) * 20

    return h, classify_basin_2d(h)

# Notebook cell 10, lines 39-187
def run_self_noise_switching(
    seed=123,
    sigmas=(0.0, 0.02, 0.05, 0.08, 0.12, 0.18, 0.25, 0.35),
    n_trials=300,
    eta=0.01,
    steps=2500,
    alpha=1.0,
    well_strength=2.0,
    lambda_self=0.5,
    gamma=0.5,
    K_scale=0.0,
    A_diag=(1.0, 0.8),
):
    rng = np.random.default_rng(seed)

    params = {
        "alpha": alpha,
        "well_strength": well_strength,
        "lambda_self": lambda_self,
        "gamma": gamma,
        "K_scale": K_scale,
        "A_diag": A_diag,
    }

    initial_basins = {
        "x+": np.array([1.0, 0.0]),
        "x-": np.array([-1.0, 0.0]),
        "y+": np.array([0.0, 0.9660917865]),
        "y-": np.array([0.0, -0.9660917865]),
    }

    rows = []

    for sigma in sigmas:
        for init_label, h0 in initial_basins.items():
            counts = {"x+": 0, "x-": 0, "y+": 0, "y-": 0}

            for _ in range(n_trials):
                # small perturbation around the fixed point
                h_init = h0 + 0.02 * rng.normal(size=2)

                hT, final_label = simulate_self_noisy(
                    h_init,
                    rng,
                    sigma=sigma,
                    eta=eta,
                    steps=steps,
                    **params
                )
                counts[final_label] += 1

            for final_label, count in counts.items():
                rows.append({
                    "sigma": sigma,
                    "initial_basin": init_label,
                    "final_basin": final_label,
                    "count": count,
                    "probability": count / n_trials,
                })

            stay_prob = counts[init_label] / n_trials
            print(
                f"sigma={sigma:>5}, init={init_label} "
                f"-> stay_prob={stay_prob:.3f}, counts={counts}"
            )

    df = pd.DataFrame(rows)
    save_csv(df, "B_noise_switching_transition_table.csv")

    # Plot stay probability vs sigma
    stay_rows = []
    for sigma in sigmas:
        for init_label in initial_basins.keys():
            sub = df[
                (df["sigma"] == sigma)
                & (df["initial_basin"] == init_label)
                & (df["final_basin"] == init_label)
            ]
            stay_rows.append({
                "sigma": sigma,
                "initial_basin": init_label,
                "stay_probability": float(sub["probability"].iloc[0]),
            })

    stay_df = pd.DataFrame(stay_rows)
    save_csv(stay_df, "B_noise_switching_stay_probability.csv")

    plt.figure(figsize=(7, 4.8))
    for init_label, sub in stay_df.groupby("initial_basin"):
        sub = sub.sort_values("sigma")
        plt.plot(
            sub["sigma"],
            sub["stay_probability"],
            marker="o",
            label=init_label
        )

    plt.xlabel("noise sigma")
    plt.ylabel("stay probability")
    plt.title("Self-observation basin stability under noise")
    plt.legend()
    save_fig("B_noise_switching_stay_probability.png")

    # Transition heatmap for highest sigma
    max_sigma = max(sigmas)
    sub = df[df["sigma"] == max_sigma]
    basin_order = ["x+", "x-", "y+", "y-"]

    mat = np.zeros((4, 4))
    for i, init_label in enumerate(basin_order):
        for j, final_label in enumerate(basin_order):
            val = sub[
                (sub["initial_basin"] == init_label)
                & (sub["final_basin"] == final_label)
            ]["probability"].iloc[0]
            mat[i, j] = val

    transition_df = pd.DataFrame(mat, index=basin_order, columns=basin_order)
    path = OUTDIR / "B_noise_switching_transition_matrix_max_sigma.csv"
    transition_df.to_csv(path)
    backup_file(path)

    plt.figure(figsize=(5.8, 5))
    plt.imshow(mat, vmin=0, vmax=1)
    plt.colorbar(label="transition probability")
    plt.xticks(range(4), basin_order)
    plt.yticks(range(4), basin_order)
    plt.xlabel("final basin")
    plt.ylabel("initial basin")
    plt.title(f"Transition matrix at sigma={max_sigma}")
    save_fig("B_noise_switching_transition_matrix_max_sigma.png")

    summary = {
        "experiment": "B_noise_induced_basin_switching",
        "interpretation": (
            "Tests whether locally stable self-model basins remain stable under noise. "
            "This does not model consciousness; it tests multistable hidden-depth dynamics."
        ),
        "sigmas": list(sigmas),
        "n_trials": n_trials,
        "eta": eta,
        "steps": steps,
        "parameters": params,
    }

    save_json(summary, "B_noise_switching_summary.json")

    print("Noise switching experiment complete.")
    return df, stay_df, summary
