# Original notebook computational definitions, cell 6

def normalized_trace_kernel(s, center_deg, width_rad):
    """
    Normalized periodic Gaussian trace kernel.
    """
    ds = s[1] - s[0]
    k = periodic_gaussian(s, np.deg2rad(center_deg), width_rad)
    denom = np.sum(k) * ds
    if denom > 1e-12:
        k = k / denom
    return k

def profile_trace_score(m, trace_kernel, ds):
    """
    Trace-specific memory score.
    """
    return float(np.sum(m * trace_kernel) * ds)

def cosine_corr_profile(a, b, ds):
    return circular_correlation(a, b, ds)

def normalized_entropy(values, eps=1e-12):
    """
    Normalized Shannon entropy of nonnegative lineage weights.
    0 = concentrated in one lineage
    1 = evenly distributed
    """
    v = np.maximum(np.asarray(values, dtype=float), 0.0)
    total = np.sum(v)
    n = len(v)

    if total < eps or n <= 1:
        return np.nan

    p = v / total
    H = -np.sum(p * np.log(p + eps))
    return float(H / np.log(n))

def concentration_index(values, eps=1e-12):
    """
    Max fraction of total trace carried by one lineage.
    """
    v = np.maximum(np.asarray(values, dtype=float), 0.0)
    total = np.sum(v)
    if total < eps:
        return np.nan
    return float(np.max(v) / total)

def pairwise_profile_correlation(profiles, ds, max_profiles=128, rng=None):
    """
    Mean pairwise cosine/circular profile correlation.
    If too many profiles, sample.
    """
    profiles = list(profiles)
    n = len(profiles)

    if n < 2:
        return np.nan

    if rng is None:
        rng = np.random.default_rng(0)

    if n > max_profiles:
        idx = rng.choice(n, size=max_profiles, replace=False)
        profiles = [profiles[i] for i in idx]
        n = len(profiles)

    corrs = []
    for i in range(n):
        for j in range(i + 1, n):
            c = circular_correlation(profiles[i], profiles[j], ds)
            if not np.isnan(c):
                corrs.append(c)

    if len(corrs) == 0:
        return np.nan

    return float(np.mean(corrs))

def choose_cut_angle(policy, generation, parent_index, rng, params=None):
    """
    Cut-angle policy for repeated division.

    Policies:
      random:
        uniform random cut

      fixed_separating:
        fixed cut near B14.2 best retention geometry

      fixed_mixing:
        fixed cut near B14.2 high mixing / worst fidelity geometry

      alternating:
        alternates between separating and mixing cuts

      jittered_separating:
        separating cut plus Gaussian angular jitter
    """
    if params is None:
        params = {}

    if policy == "random":
        return float(rng.uniform(0, 2 * np.pi))

    if policy == "fixed_separating":
        return float(np.deg2rad(params.get("cut_deg", 78.9)))

    if policy == "fixed_mixing":
        return float(np.deg2rad(params.get("cut_deg", 143.0)))

    if policy == "alternating":
        if generation % 2 == 0:
            return float(np.deg2rad(params.get("cut_deg_even", 78.9)))
        else:
            return float(np.deg2rad(params.get("cut_deg_odd", 143.0)))

    if policy == "jittered_separating":
        base = np.deg2rad(params.get("cut_deg", 78.9))
        jitter = np.deg2rad(params.get("jitter_deg", 15.0)) * rng.normal()
        return float((base + jitter) % (2 * np.pi))

    raise ValueError(f"Unknown cut policy: {policy}")

def simulate_multigeneration_lineage(
    seed=1431,
    N=256,
    generations=6,
    cut_policy="random",
    cut_policy_params=None,

    partition_sharpness=8.0,
    inheritance_efficiency=0.96,
    leakage=0.04,
    noise_sigma=0.010,
    smooth_tau=0.002,
):
    """
    Simulate repeated boundary-memory division.

    Start from one parent memory profile.
    At each generation every cell divides into two daughters.
    Track memory norm, correlation to initial parent, trace-specific inheritance,
    lineage concentration, and lineage diversity.

    This is not a biological heredity model.
    It is a reduced repeated boundary-memory division map.
    """

    rng_master = np.random.default_rng(seed)

    s = np.linspace(0, 2 * np.pi, N, endpoint=False)
    ds = s[1] - s[0]

    # Initial parent memory
    m0 = make_parent_memory_profile(s)
    m0 = np.maximum(m0 + 0.010 * rng_master.normal(size=N), 0.0)

    trace1_kernel = normalized_trace_kernel(s, center_deg=60, width_rad=0.20)
    trace2_kernel = normalized_trace_kernel(s, center_deg=230, width_rad=0.24)

    initial_norm = L2_norm_profile(m0, ds)
    initial_trace1 = profile_trace_score(m0, trace1_kernel, ds)
    initial_trace2 = profile_trace_score(m0, trace2_kernel, ds)

    # Cell state list
    cells = [
        {
            "cell_id": "0",
            "parent_id": "",
            "generation": 0,
            "branch": "",
            "profile": m0,
        }
    ]

    cell_records = []
    profile_records = []
    event_records = []
    generation_profile_store = {}

    def record_cells(cells_now):
        for cell in cells_now:
            m = cell["profile"]
            gen = cell["generation"]

            norm = L2_norm_profile(m, ds)
            corr_initial = circular_correlation(m, m0, ds)
            trace1 = profile_trace_score(m, trace1_kernel, ds)
            trace2 = profile_trace_score(m, trace2_kernel, ds)

            trace_sum = trace1 + trace2
            if trace_sum > 1e-12:
                trace_balance = (trace1 - trace2) / trace_sum
                trace_dominance = abs(trace1 - trace2) / trace_sum
            else:
                trace_balance = np.nan
                trace_dominance = np.nan

            cell_records.append({
                "seed": seed,
                "cut_policy": cut_policy,
                "cell_id": cell["cell_id"],
                "parent_id": cell["parent_id"],
                "generation": gen,
                "branch": cell["branch"],

                "norm": norm,
                "norm_ratio_to_initial": norm / initial_norm if initial_norm > 1e-12 else np.nan,
                "corr_with_initial_parent": corr_initial,

                "trace1_score": trace1,
                "trace2_score": trace2,
                "trace1_ratio_to_initial": trace1 / initial_trace1 if initial_trace1 > 1e-12 else np.nan,
                "trace2_ratio_to_initial": trace2 / initial_trace2 if initial_trace2 > 1e-12 else np.nan,
                "trace_balance": trace_balance,
                "trace_dominance": trace_dominance,
            })

            profile_row = {
                "seed": seed,
                "cut_policy": cut_policy,
                "cell_id": cell["cell_id"],
                "parent_id": cell["parent_id"],
                "generation": gen,
                "branch": cell["branch"],
            }
            for i, val in enumerate(m):
                profile_row[f"m_{i}"] = float(val)
            profile_records.append(profile_row)

        key = gen
        generation_profile_store[key] = [c["profile"].copy() for c in cells_now]

    # Record generation 0
    record_cells(cells)

    # Repeated division
    for gen in range(1, generations + 1):
        new_cells = []

        for idx, parent in enumerate(cells):
            parent_profile = parent["profile"]
            cut_rng = np.random.default_rng(int(rng_master.integers(0, 2**31 - 1)))

            cut_angle = choose_cut_angle(
                policy=cut_policy,
                generation=gen,
                parent_index=idx,
                rng=cut_rng,
                params=cut_policy_params,
            )

            div_rng = np.random.default_rng(int(rng_master.integers(0, 2**31 - 1)))

            res = division_inherit_profiles(
                mP=parent_profile,
                s=s,
                ds=ds,
                cut_angle=cut_angle,
                partition_sharpness=partition_sharpness,
                inheritance_efficiency=inheritance_efficiency,
                leakage=leakage,
                noise_sigma=noise_sigma,
                smooth_tau=smooth_tau,
                rng=div_rng,
            )

            event_records.append({
                "seed": seed,
                "cut_policy": cut_policy,
                "generation": gen,
                "parent_cell_id": parent["cell_id"],
                "parent_branch": parent["branch"],
                "cut_angle_rad": cut_angle,
                "cut_angle_deg": cut_angle * 180 / np.pi,

                "mean_daughter_fidelity": res["mean_daughter_fidelity"],
                "mean_cross_contamination": res["mean_cross_contamination"],
                "total_retention": res["total_retention"],
                "inheritance_asymmetry": res["inheritance_asymmetry"],
                "reconstruction_corr": res["reconstruction_corr"],
                "reconstruction_norm_ratio": res["reconstruction_norm_ratio"],

                "norm_parent": L2_norm_profile(parent_profile, ds),
                "normD1": res["normD1"],
                "normD2": res["normD2"],
            })

            child1 = {
                "cell_id": parent["cell_id"] + "0",
                "parent_id": parent["cell_id"],
                "generation": gen,
                "branch": parent["branch"] + "0",
                "profile": res["D1"],
            }

            child2 = {
                "cell_id": parent["cell_id"] + "1",
                "parent_id": parent["cell_id"],
                "generation": gen,
                "branch": parent["branch"] + "1",
                "profile": res["D2"],
            }

            new_cells.extend([child1, child2])

        cells = new_cells
        record_cells(cells)

    cell_df = pd.DataFrame(cell_records)
    profile_df = pd.DataFrame(profile_records)
    event_df = pd.DataFrame(event_records)

    # Generation summary
    gen_rows = []

    for gen in range(generations + 1):
        sub = cell_df[cell_df["generation"] == gen]
        profiles = generation_profile_store[gen]

        trace1_vals = sub["trace1_score"].to_numpy(dtype=float)
        trace2_vals = sub["trace2_score"].to_numpy(dtype=float)

        pair_corr = pairwise_profile_correlation(
            profiles,
            ds=ds,
            max_profiles=128,
            rng=np.random.default_rng(seed + gen),
        )

        mean_profile = np.mean(np.array(profiles), axis=0)
        mean_profile_corr_initial = circular_correlation(mean_profile, m0, ds)

        gen_rows.append({
            "seed": seed,
            "cut_policy": cut_policy,
            "generation": gen,
            "n_cells": len(sub),

            "mean_norm": float(sub["norm"].mean()),
            "std_norm": float(sub["norm"].std()) if len(sub) > 1 else 0.0,
            "max_norm": float(sub["norm"].max()),
            "min_norm": float(sub["norm"].min()),

            "mean_norm_ratio_to_initial": float(sub["norm_ratio_to_initial"].mean()),
            "max_norm_ratio_to_initial": float(sub["norm_ratio_to_initial"].max()),

            "mean_corr_with_initial": float(sub["corr_with_initial_parent"].mean()),
            "max_corr_with_initial": float(sub["corr_with_initial_parent"].max()),
            "min_corr_with_initial": float(sub["corr_with_initial_parent"].min()),

            "mean_trace1_score": float(np.mean(trace1_vals)),
            "max_trace1_score": float(np.max(trace1_vals)),
            "sum_trace1_score": float(np.sum(trace1_vals)),
            "trace1_concentration": concentration_index(trace1_vals),
            "trace1_entropy": normalized_entropy(trace1_vals),

            "mean_trace2_score": float(np.mean(trace2_vals)),
            "max_trace2_score": float(np.max(trace2_vals)),
            "sum_trace2_score": float(np.sum(trace2_vals)),
            "trace2_concentration": concentration_index(trace2_vals),
            "trace2_entropy": normalized_entropy(trace2_vals),

            "mean_trace_dominance": float(sub["trace_dominance"].mean()),
            "max_trace_dominance": float(sub["trace_dominance"].max()),

            "mean_pairwise_profile_corr": pair_corr,
            "mean_profile_corr_with_initial": mean_profile_corr_initial,
        })

    gen_df = pd.DataFrame(gen_rows)

    return {
        "s": s,
        "ds": ds,
        "initial_profile": m0,
        "cell_df": cell_df,
        "profile_df": profile_df,
        "event_df": event_df,
        "gen_df": gen_df,
    }

def run_B14_3_multigeneration_inheritance(
    seeds=(1431, 1432, 1433),
    generations=6,
    N=256,

    scenarios=None,

    partition_sharpness=8.0,
    inheritance_efficiency=0.96,
    leakage=0.04,
    noise_sigma=0.010,
    smooth_tau=0.002,
):
    """
    Run B14.3 across multiple cut-angle policies and seeds.
    """

    if scenarios is None:
        scenarios = [
            {
                "name": "fixed_separating",
                "policy": "fixed_separating",
                "params": {"cut_deg": 78.9},
            },
            {
                "name": "fixed_mixing",
                "policy": "fixed_mixing",
                "params": {"cut_deg": 143.0},
            },
            {
                "name": "alternating",
                "policy": "alternating",
                "params": {"cut_deg_even": 78.9, "cut_deg_odd": 143.0},
            },
            {
                "name": "random",
                "policy": "random",
                "params": {},
            },
            {
                "name": "jittered_separating",
                "policy": "jittered_separating",
                "params": {"cut_deg": 78.9, "jitter_deg": 15.0},
            },
        ]

    all_cell = []
    all_profile = []
    all_event = []
    all_gen = []

    first_result = None

    for scenario in scenarios:
        name = scenario["name"]
        policy = scenario["policy"]
        params = scenario.get("params", {})

        for seed in seeds:
            print("=" * 72)
            print(f"B14.3 scenario={name}, policy={policy}, seed={seed}")

            result = simulate_multigeneration_lineage(
                seed=seed,
                N=N,
                generations=generations,
                cut_policy=policy,
                cut_policy_params=params,

                partition_sharpness=partition_sharpness,
                inheritance_efficiency=inheritance_efficiency,
                leakage=leakage,
                noise_sigma=noise_sigma,
                smooth_tau=smooth_tau,
            )

            if first_result is None:
                first_result = result

            cell_df = result["cell_df"].copy()
            profile_df = result["profile_df"].copy()
            event_df = result["event_df"].copy()
            gen_df = result["gen_df"].copy()

            for df in [cell_df, profile_df, event_df, gen_df]:
                df["scenario"] = name

            all_cell.append(cell_df)
            all_profile.append(profile_df)
            all_event.append(event_df)
            all_gen.append(gen_df)

    cell_all = pd.concat(all_cell, ignore_index=True)
    profile_all = pd.concat(all_profile, ignore_index=True)
    event_all = pd.concat(all_event, ignore_index=True)
    gen_all = pd.concat(all_gen, ignore_index=True)

    # Aggregate over seeds
    gen_agg = (
        gen_all
        .groupby(["scenario", "generation"], as_index=False)
        .agg(
            n_cells=("n_cells", "mean"),

            mean_norm=("mean_norm", "mean"),
            std_mean_norm=("mean_norm", "std"),
            max_norm=("max_norm", "mean"),

            mean_corr_with_initial=("mean_corr_with_initial", "mean"),
            std_corr_with_initial=("mean_corr_with_initial", "std"),
            max_corr_with_initial=("max_corr_with_initial", "mean"),
            min_corr_with_initial=("min_corr_with_initial", "mean"),

            mean_profile_corr_with_initial=("mean_profile_corr_with_initial", "mean"),
            std_mean_profile_corr=("mean_profile_corr_with_initial", "std"),

            mean_trace1_score=("mean_trace1_score", "mean"),
            max_trace1_score=("max_trace1_score", "mean"),
            sum_trace1_score=("sum_trace1_score", "mean"),
            trace1_concentration=("trace1_concentration", "mean"),
            trace1_entropy=("trace1_entropy", "mean"),

            mean_trace2_score=("mean_trace2_score", "mean"),
            max_trace2_score=("max_trace2_score", "mean"),
            sum_trace2_score=("sum_trace2_score", "mean"),
            trace2_concentration=("trace2_concentration", "mean"),
            trace2_entropy=("trace2_entropy", "mean"),

            mean_trace_dominance=("mean_trace_dominance", "mean"),
            max_trace_dominance=("max_trace_dominance", "mean"),

            mean_pairwise_profile_corr=("mean_pairwise_profile_corr", "mean"),
            std_pairwise_profile_corr=("mean_pairwise_profile_corr", "std"),
        )
    )

    # Final-generation summary
    final_gen = generations
    final_summary = gen_agg[gen_agg["generation"] == final_gen].copy()

    # Save data
    save_csv_local(cell_all, "B14_3_multigeneration_cell_metrics.csv")
    save_csv_local(event_all, "B14_3_multigeneration_division_events.csv")
    save_csv_local(gen_all, "B14_3_multigeneration_generation_summary_by_seed.csv")
    save_csv_local(gen_agg, "B14_3_multigeneration_generation_summary_agg.csv")
    save_csv_local(final_summary, "B14_3_multigeneration_final_summary.csv")

    # Profile matrix can be large but useful for package reproducibility
    save_csv_local(profile_all, "B14_3_multigeneration_profiles_matrix.csv")

    # --------------------------------------------------------
    # Figures
    # --------------------------------------------------------

    # Figure 1: mean correlation to initial parent
    plt.figure(figsize=(8.5, 5.2))
    for scenario, sub in gen_agg.groupby("scenario"):
        sub = sub.sort_values("generation")
        plt.errorbar(
            sub["generation"],
            sub["mean_corr_with_initial"],
            yerr=sub["std_corr_with_initial"],
            marker="o",
            capsize=3,
            label=scenario,
        )
    plt.xlabel("generation")
    plt.ylabel("mean corr with initial parent")
    plt.title("B14.3 lineage memory correlation across generations")
    plt.legend(fontsize=8)
    save_fig_local("B14_3_lineage_corr_with_initial.png")

    # Figure 2: mean profile correlation to initial
    plt.figure(figsize=(8.5, 5.2))
    for scenario, sub in gen_agg.groupby("scenario"):
        sub = sub.sort_values("generation")
        plt.errorbar(
            sub["generation"],
            sub["mean_profile_corr_with_initial"],
            yerr=sub["std_mean_profile_corr"],
            marker="o",
            capsize=3,
            label=scenario,
        )
    plt.xlabel("generation")
    plt.ylabel("corr(mean profile, initial parent)")
    plt.title("B14.3 averaged lineage memory retains parent pattern")
    plt.legend(fontsize=8)
    save_fig_local("B14_3_mean_profile_corr_with_initial.png")

    # Figure 3: mean norm over generations
    plt.figure(figsize=(8.5, 5.2))
    for scenario, sub in gen_agg.groupby("scenario"):
        sub = sub.sort_values("generation")
        plt.errorbar(
            sub["generation"],
            sub["mean_norm"],
            yerr=sub["std_mean_norm"],
            marker="o",
            capsize=3,
            label=scenario,
        )
    plt.xlabel("generation")
    plt.ylabel("mean cell memory norm")
    plt.title("B14.3 memory norm across repeated division")
    plt.legend(fontsize=8)
    save_fig_local("B14_3_mean_memory_norm_across_generations.png")

    # Figure 4: trace entropy
    plt.figure(figsize=(8.5, 5.2))
    for scenario, sub in gen_agg.groupby("scenario"):
        sub = sub.sort_values("generation")
        plt.plot(
            sub["generation"],
            sub["trace1_entropy"],
            marker="o",
            label=f"{scenario}: trace1",
        )
        plt.plot(
            sub["generation"],
            sub["trace2_entropy"],
            marker="s",
            linestyle="--",
            label=f"{scenario}: trace2",
        )
    plt.xlabel("generation")
    plt.ylabel("normalized lineage entropy")
    plt.title("B14.3 trace distribution across lineages")
    plt.legend(fontsize=7, ncol=2)
    save_fig_local("B14_3_trace_entropy_across_generations.png")

    # Figure 5: trace concentration
    plt.figure(figsize=(8.5, 5.2))
    for scenario, sub in gen_agg.groupby("scenario"):
        sub = sub.sort_values("generation")
        plt.plot(
            sub["generation"],
            sub["trace1_concentration"],
            marker="o",
            label=f"{scenario}: trace1",
        )
        plt.plot(
            sub["generation"],
            sub["trace2_concentration"],
            marker="s",
            linestyle="--",
            label=f"{scenario}: trace2",
        )
    plt.xlabel("generation")
    plt.ylabel("max lineage fraction")
    plt.title("B14.3 trace concentration across lineages")
    plt.legend(fontsize=7, ncol=2)
    save_fig_local("B14_3_trace_concentration_across_generations.png")

    # Figure 6: pairwise diversity
    plt.figure(figsize=(8.5, 5.2))
    for scenario, sub in gen_agg.groupby("scenario"):
        sub = sub.sort_values("generation")
        plt.errorbar(
            sub["generation"],
            sub["mean_pairwise_profile_corr"],
            yerr=sub["std_pairwise_profile_corr"],
            marker="o",
            capsize=3,
            label=scenario,
        )
    plt.xlabel("generation")
    plt.ylabel("mean pairwise profile correlation")
    plt.title("B14.3 lineage diversity across generations")
    plt.legend(fontsize=8)
    save_fig_local("B14_3_pairwise_lineage_similarity.png")

    # Figure 7: final generation trace scatter
    final_cells = cell_all[cell_all["generation"] == final_gen].copy()

    plt.figure(figsize=(7.2, 6.2))
    for scenario, sub in final_cells.groupby("scenario"):
        plt.scatter(
            sub["trace1_score"],
            sub["trace2_score"],
            alpha=0.55,
            label=scenario,
        )
    plt.xlabel("trace1 score")
    plt.ylabel("trace2 score")
    plt.title("B14.3 final-generation trace inheritance")
    plt.legend(fontsize=8)
    save_fig_local("B14_3_final_generation_trace_scatter.png")

    # Figure 8: final-generation heatmap for one representative seed per scenario
    # Store separate images for readability.
    for scenario in final_cells["scenario"].unique():
        sub_profiles = profile_all[
            (profile_all["scenario"] == scenario)
            & (profile_all["generation"] == final_gen)
            & (profile_all["seed"] == seeds[0])
        ].copy()

        if len(sub_profiles) == 0:
            continue

        m_cols = [c for c in sub_profiles.columns if c.startswith("m_")]
        mat = sub_profiles[m_cols].to_numpy(dtype=float)

        # Sort by trace balance for visual clarity
        sub_cells = cell_all[
            (cell_all["scenario"] == scenario)
            & (cell_all["generation"] == final_gen)
            & (cell_all["seed"] == seeds[0])
        ].copy()

        order = np.argsort(sub_cells["trace_balance"].to_numpy(dtype=float))
        mat = mat[order]

        plt.figure(figsize=(9.0, 5.6))
        plt.imshow(
            mat,
            aspect="auto",
            origin="lower",
            extent=[0, 360, 0, mat.shape[0]],
        )
        plt.colorbar(label="boundary memory")
        plt.xlabel("boundary coordinate s [deg]")
        plt.ylabel("final-generation lineage index")
        plt.title(f"B14.3 final-generation memory profiles: {scenario}")
        save_fig_local(f"B14_3_final_profiles_heatmap_{scenario}.png")

    # --------------------------------------------------------
    # Summary JSON
    # --------------------------------------------------------

    key_results = {
        "final_generation": int(final_gen),
        "final_summary": final_summary.to_dict(orient="records"),
    }

    # Find best final mean corr and best mean profile corr
    if len(final_summary) > 0:
        best_mean_corr = final_summary.loc[final_summary["mean_corr_with_initial"].idxmax()].to_dict()
        best_mean_profile_corr = final_summary.loc[final_summary["mean_profile_corr_with_initial"].idxmax()].to_dict()
        highest_entropy_trace1 = final_summary.loc[final_summary["trace1_entropy"].idxmax()].to_dict()
        highest_entropy_trace2 = final_summary.loc[final_summary["trace2_entropy"].idxmax()].to_dict()
    else:
        best_mean_corr = {}
        best_mean_profile_corr = {}
        highest_entropy_trace1 = {}
        highest_entropy_trace2 = {}

    summary = {
        "experiment": "BIG_B14_3_multigeneration_boundary_memory_inheritance",
        "description": (
            "Repeated division maps for boundary-memory lineages. "
            "Tracks persistence, distribution, concentration, and mixing of boundary-localized traces "
            "across multiple generations."
        ),
        "parameters": {
            "seeds": list(seeds),
            "generations": generations,
            "N": N,
            "scenarios": scenarios,
            "partition_sharpness": partition_sharpness,
            "inheritance_efficiency": inheritance_efficiency,
            "leakage": leakage,
            "noise_sigma": noise_sigma,
            "smooth_tau": smooth_tau,
        },
        "key_results": {
            "best_final_mean_corr_with_initial": best_mean_corr,
            "best_final_mean_profile_corr_with_initial": best_mean_profile_corr,
            "highest_final_trace1_entropy": highest_entropy_trace1,
            "highest_final_trace2_entropy": highest_entropy_trace2,
            "final_generation_summary": final_summary.to_dict(orient="records"),
        },
        "interpretation": (
            "This is not a derivation of biological heredity. "
            "It is a reduced lineage-memory model showing how boundary-localized traces "
            "can decay, partition, concentrate, mix, or persist under repeated division maps."
        ),
    }

    save_json_local(summary, "B14_3_multigeneration_inheritance_summary.json")

    print("B14.3 multi-generation inheritance complete.")
    display(final_summary)
    print(json.dumps(summary, indent=2))

    return cell_all, profile_all, event_all, gen_all, gen_agg, final_summary, summary
