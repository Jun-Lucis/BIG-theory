# Original notebook computational definitions, cell 5

def run_single_division_scan_for_condition(
    seed,
    N=256,
    cut_angles_deg=np.linspace(0, 360, 37, endpoint=False),
    partition_sharpness=8.0,
    inheritance_efficiency=0.96,
    leakage=0.04,
    noise_sigma=0.010,
    smooth_tau=0.002,
):
    """
    Run B14.2 division scan for one parameter condition.
    Assumes division_inherit_profiles and make_parent_memory_profile
    are already defined from Cell 3.
    """

    rng_master = np.random.default_rng(seed)

    s = np.linspace(0, 2 * np.pi, N, endpoint=False)
    ds = s[1] - s[0]

    mP = make_parent_memory_profile(s)
    mP = np.maximum(mP + 0.010 * rng_master.normal(size=N), 0.0)

    rows = []

    for cut_deg in cut_angles_deg:
        cut_angle = np.deg2rad(cut_deg)
        rng = np.random.default_rng(int(rng_master.integers(0, 2**31 - 1)))

        res = division_inherit_profiles(
            mP=mP,
            s=s,
            ds=ds,
            cut_angle=cut_angle,
            partition_sharpness=partition_sharpness,
            inheritance_efficiency=inheritance_efficiency,
            leakage=leakage,
            noise_sigma=noise_sigma,
            smooth_tau=smooth_tau,
            rng=rng,
        )

        rows.append({
            "seed": seed,
            "cut_angle_deg": float(cut_deg),
            "partition_sharpness": float(partition_sharpness),
            "inheritance_efficiency": float(inheritance_efficiency),
            "leakage": float(leakage),
            "noise_sigma": float(noise_sigma),
            "smooth_tau": float(smooth_tau),

            "mean_daughter_fidelity": res["mean_daughter_fidelity"],
            "fidelity_D1_ref1": res["fidelity_D1_ref1"],
            "fidelity_D2_ref2": res["fidelity_D2_ref2"],

            "mean_cross_contamination": res["mean_cross_contamination"],
            "cross_D1_ref2": res["cross_D1_ref2"],
            "cross_D2_ref1": res["cross_D2_ref1"],

            "total_retention": res["total_retention"],
            "inheritance_asymmetry": res["inheritance_asymmetry"],
            "reconstruction_corr": res["reconstruction_corr"],
            "reconstruction_norm_ratio": res["reconstruction_norm_ratio"],

            "normD1": res["normD1"],
            "normD2": res["normD2"],

            "trace1_D1": res["trace1_D1"],
            "trace1_D2": res["trace1_D2"],
            "trace2_D1": res["trace2_D1"],
            "trace2_D2": res["trace2_D2"],
        })

    return pd.DataFrame(rows)

def summarize_division_robustness(df, group_cols):
    """
    Aggregate scan results by condition.
    """

    agg = (
        df
        .groupby(group_cols, as_index=False)
        .agg(
            mean_fidelity=("mean_daughter_fidelity", "mean"),
            std_fidelity=("mean_daughter_fidelity", "std"),
            min_fidelity=("mean_daughter_fidelity", "min"),

            mean_cross_contamination=("mean_cross_contamination", "mean"),
            std_cross_contamination=("mean_cross_contamination", "std"),
            max_cross_contamination=("mean_cross_contamination", "max"),

            mean_total_retention=("total_retention", "mean"),
            std_total_retention=("total_retention", "std"),
            min_total_retention=("total_retention", "min"),

            mean_asymmetry=("inheritance_asymmetry", "mean"),
            std_asymmetry=("inheritance_asymmetry", "std"),
            max_asymmetry=("inheritance_asymmetry", "max"),

            mean_reconstruction_corr=("reconstruction_corr", "mean"),
            std_reconstruction_corr=("reconstruction_corr", "std"),
            min_reconstruction_corr=("reconstruction_corr", "min"),
        )
    )

    return agg

def run_B14_2b_division_robustness(
    seeds=(1421, 1422, 1423),
    N=256,
    cut_angles_deg=np.linspace(0, 360, 37, endpoint=False),

    base_partition_sharpness=8.0,
    base_inheritance_efficiency=0.96,
    base_leakage=0.04,
    base_noise_sigma=0.010,
    base_smooth_tau=0.002,

    noise_values=(0.0, 0.005, 0.010, 0.020, 0.040, 0.080),
    leakage_values=(0.0, 0.02, 0.04, 0.08, 0.12, 0.20),
    sharpness_values=(3.0, 5.0, 8.0, 12.0, 20.0),
):
    """
    Robustness scans:
      A. noise_sigma scan
      B. leakage scan
      C. partition_sharpness scan

    Each scan changes one parameter while holding the others fixed.
    """

    all_rows = []

    # --------------------------------------------------------
    # A. Noise scan
    # --------------------------------------------------------
    for noise in noise_values:
        print("=" * 70)
        print(f"Noise scan: noise_sigma={noise}")

        for seed in seeds:
            df = run_single_division_scan_for_condition(
                seed=seed,
                N=N,
                cut_angles_deg=cut_angles_deg,
                partition_sharpness=base_partition_sharpness,
                inheritance_efficiency=base_inheritance_efficiency,
                leakage=base_leakage,
                noise_sigma=noise,
                smooth_tau=base_smooth_tau,
            )
            df["scan_type"] = "noise"
            df["scan_value"] = float(noise)
            all_rows.append(df)

    # --------------------------------------------------------
    # B. Leakage scan
    # --------------------------------------------------------
    for leakage in leakage_values:
        print("=" * 70)
        print(f"Leakage scan: leakage={leakage}")

        for seed in seeds:
            df = run_single_division_scan_for_condition(
                seed=seed,
                N=N,
                cut_angles_deg=cut_angles_deg,
                partition_sharpness=base_partition_sharpness,
                inheritance_efficiency=base_inheritance_efficiency,
                leakage=leakage,
                noise_sigma=base_noise_sigma,
                smooth_tau=base_smooth_tau,
            )
            df["scan_type"] = "leakage"
            df["scan_value"] = float(leakage)
            all_rows.append(df)

    # --------------------------------------------------------
    # C. Partition sharpness scan
    # --------------------------------------------------------
    for sharpness in sharpness_values:
        print("=" * 70)
        print(f"Sharpness scan: partition_sharpness={sharpness}")

        for seed in seeds:
            df = run_single_division_scan_for_condition(
                seed=seed,
                N=N,
                cut_angles_deg=cut_angles_deg,
                partition_sharpness=sharpness,
                inheritance_efficiency=base_inheritance_efficiency,
                leakage=base_leakage,
                noise_sigma=base_noise_sigma,
                smooth_tau=base_smooth_tau,
            )
            df["scan_type"] = "sharpness"
            df["scan_value"] = float(sharpness)
            all_rows.append(df)

    all_df = pd.concat(all_rows, ignore_index=True)

    # Aggregate by scan type and scan value
    agg = summarize_division_robustness(
        all_df,
        group_cols=["scan_type", "scan_value"]
    )

    # Additional by seed aggregation
    by_seed = summarize_division_robustness(
        all_df,
        group_cols=["scan_type", "scan_value", "seed"]
    )

    # Save
    save_csv_local(all_df, "B14_2b_division_robustness_all_points.csv")
    save_csv_local(agg, "B14_2b_division_robustness_summary.csv")
    save_csv_local(by_seed, "B14_2b_division_robustness_by_seed.csv")

    # --------------------------------------------------------
    # Figures
    # --------------------------------------------------------

    def plot_scan_metric(scan_type, metric, ylabel, filename, title):
        sub = agg[agg["scan_type"] == scan_type].sort_values("scan_value")

        std_col = None
        if metric == "mean_fidelity":
            std_col = "std_fidelity"
        elif metric == "mean_cross_contamination":
            std_col = "std_cross_contamination"
        elif metric == "mean_total_retention":
            std_col = "std_total_retention"
        elif metric == "mean_asymmetry":
            std_col = "std_asymmetry"
        elif metric == "mean_reconstruction_corr":
            std_col = "std_reconstruction_corr"

        plt.figure(figsize=(7.5, 5.0))
        if std_col is not None:
            plt.errorbar(
                sub["scan_value"],
                sub[metric],
                yerr=sub[std_col],
                marker="o",
                capsize=3,
            )
        else:
            plt.plot(sub["scan_value"], sub[metric], marker="o")

        plt.xlabel(scan_type)
        plt.ylabel(ylabel)
        plt.title(title)
        save_fig_local(filename)

    # Noise figures
    plot_scan_metric(
        "noise",
        "mean_fidelity",
        "mean daughter fidelity",
        "B14_2b_noise_vs_fidelity.png",
        "B14.2b noise robustness: fidelity"
    )

    plot_scan_metric(
        "noise",
        "mean_cross_contamination",
        "mean cross-contamination",
        "B14_2b_noise_vs_cross_contamination.png",
        "B14.2b noise robustness: cross-contamination"
    )

    plot_scan_metric(
        "noise",
        "mean_total_retention",
        "mean total retention",
        "B14_2b_noise_vs_retention.png",
        "B14.2b noise robustness: retention"
    )

    # Leakage figures
    plot_scan_metric(
        "leakage",
        "mean_cross_contamination",
        "mean cross-contamination",
        "B14_2b_leakage_vs_cross_contamination.png",
        "B14.2b leakage controls cross-contamination"
    )

    plot_scan_metric(
        "leakage",
        "mean_fidelity",
        "mean daughter fidelity",
        "B14_2b_leakage_vs_fidelity.png",
        "B14.2b leakage robustness: fidelity"
    )

    plot_scan_metric(
        "leakage",
        "mean_asymmetry",
        "mean inheritance asymmetry",
        "B14_2b_leakage_vs_asymmetry.png",
        "B14.2b leakage robustness: asymmetry"
    )

    # Sharpness figures
    plot_scan_metric(
        "sharpness",
        "mean_cross_contamination",
        "mean cross-contamination",
        "B14_2b_sharpness_vs_cross_contamination.png",
        "B14.2b partition sharpness controls mixing"
    )

    plot_scan_metric(
        "sharpness",
        "mean_total_retention",
        "mean total retention",
        "B14_2b_sharpness_vs_retention.png",
        "B14.2b partition sharpness robustness: retention"
    )

    plot_scan_metric(
        "sharpness",
        "mean_asymmetry",
        "mean inheritance asymmetry",
        "B14_2b_sharpness_vs_asymmetry.png",
        "B14.2b partition sharpness robustness: asymmetry"
    )

    # Combined compact figure
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

    for ax, scan_type, xlab in zip(
        axes,
        ["noise", "leakage", "sharpness"],
        ["noise sigma", "leakage", "partition sharpness"]
    ):
        sub = agg[agg["scan_type"] == scan_type].sort_values("scan_value")

        ax.plot(sub["scan_value"], sub["mean_fidelity"], marker="o", label="fidelity")
        ax.plot(sub["scan_value"], sub["mean_cross_contamination"], marker="s", label="cross contamination")
        ax.plot(sub["scan_value"], sub["mean_total_retention"], marker="^", label="retention")
        ax.plot(sub["scan_value"], sub["mean_asymmetry"], marker="x", label="asymmetry")

        ax.set_xlabel(xlab)
        ax.set_title(f"{scan_type} scan")
        ax.grid(True, alpha=0.25)

    axes[0].set_ylabel("metric")
    axes[-1].legend(fontsize=8)
    plt.suptitle("B14.2b division inheritance robustness summary")
    save_fig_local("B14_2b_division_robustness_combined_summary.png")

    # --------------------------------------------------------
    # Key results
    # --------------------------------------------------------

    def row_at(scan_type, scan_value):
        sub = agg[(agg["scan_type"] == scan_type) & np.isclose(agg["scan_value"], scan_value)]
        if len(sub) == 0:
            return None
        return sub.iloc[0].to_dict()

    key_results = {
        "baseline_noise": row_at("noise", base_noise_sigma),
        "highest_noise": row_at("noise", max(noise_values)),
        "baseline_leakage": row_at("leakage", base_leakage),
        "highest_leakage": row_at("leakage", max(leakage_values)),
        "lowest_sharpness": row_at("sharpness", min(sharpness_values)),
        "baseline_sharpness": row_at("sharpness", base_partition_sharpness),
        "highest_sharpness": row_at("sharpness", max(sharpness_values)),
    }

    summary = {
        "experiment": "BIG_B14_2b_division_inheritance_robustness",
        "description": (
            "Robustness scan for boundary memory division inheritance under noise, "
            "leakage, and partition sharpness variation."
        ),
        "parameters": {
            "seeds": list(seeds),
            "N": N,
            "cut_angle_count": int(len(cut_angles_deg)),
            "base_partition_sharpness": base_partition_sharpness,
            "base_inheritance_efficiency": base_inheritance_efficiency,
            "base_leakage": base_leakage,
            "base_noise_sigma": base_noise_sigma,
            "base_smooth_tau": base_smooth_tau,
            "noise_values": list(map(float, noise_values)),
            "leakage_values": list(map(float, leakage_values)),
            "sharpness_values": list(map(float, sharpness_values)),
        },
        "key_results": key_results,
        "interpretation": (
            "If leakage increases cross-contamination, partition sharpness reduces mixing, "
            "and noise lowers fidelity or retention, then B14.2 division inheritance is robustly "
            "controlled by explicit inheritance parameters rather than by a single division example."
        ),
    }

    save_json_local(summary, "B14_2b_division_robustness_summary.json")

    print("B14.2b division inheritance robustness complete.")
    display(agg)
    print(json.dumps(summary, indent=2))

    return all_df, agg, by_seed, summary
