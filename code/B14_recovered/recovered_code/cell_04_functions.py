# Original notebook computational definitions, cell 4

def periodic_angle_distance(s, s0):
    return np.angle(np.exp(1j * (s - s0)))

def periodic_gaussian(s, s0, width):
    d = periodic_angle_distance(s, s0)
    return np.exp(-0.5 * (d / width) ** 2)

def L2_norm_profile(m, ds):
    return float(np.sqrt(np.sum(m * m) * ds))

def circular_correlation(a, b, ds):
    num = np.sum(a * b) * ds
    den = np.sqrt(np.sum(a * a) * ds) * np.sqrt(np.sum(b * b) * ds)
    if den < 1e-12:
        return np.nan
    return float(num / den)

def heat_smooth_periodic_fft(m, ds, smooth_tau=0.002):
    """
    Stable heat-kernel smoothing on periodic boundary.
    """
    m = np.asarray(m, dtype=float)
    N = len(m)
    freqs = np.fft.fftfreq(N, d=ds)
    k = 2 * np.pi * freqs
    mhat = np.fft.fft(m)
    multiplier = np.exp(-(k ** 2) * smooth_tau)
    return np.maximum(np.real(np.fft.ifft(mhat * multiplier)), 0.0)

def make_parent_memory_profile(s):
    """
    Parent memory with two localized traces.
    One strong trace and one weaker trace.
    """
    m = (
        1.00 * periodic_gaussian(s, np.deg2rad(60), 0.20)
        +
        0.70 * periodic_gaussian(s, np.deg2rad(230), 0.24)
    )
    return np.maximum(m, 0.0)

def smooth_partition_masks(s, cut_angle, sharpness=8.0):
    """
    Smooth division partition on a circular boundary.

    Daughter 1 receives the side around cut_angle.
    Daughter 2 receives the opposite side.

    mask1 + mask2 = 1.
    """
    x = np.cos(s - cut_angle)
    mask1 = 1.0 / (1.0 + np.exp(-sharpness * x))
    mask2 = 1.0 - mask1
    return mask1, mask2

def division_inherit_profiles(
    mP,
    s,
    ds,
    cut_angle,
    partition_sharpness=8.0,
    inheritance_efficiency=0.96,
    leakage=0.04,
    noise_sigma=0.010,
    smooth_tau=0.002,
    rng=None,
):
    """
    Reduced division inheritance map.

    Parent memory:
        mP(s)

    Partition:
        mask1(s), mask2(s)

    Ideal inherited references:
        ref1 = mask1 * mP
        ref2 = mask2 * mP

    Daughter memories:
        D1 = efficiency*ref1 + leakage*ref2 + noise
        D2 = efficiency*ref2 + leakage*ref1 + noise

    Then stable smoothing.

    Interpretation:
        This is not biological cell division.
        It is a reduced boundary-memory inheritance map.
    """

    if rng is None:
        rng = np.random.default_rng()

    mask1, mask2 = smooth_partition_masks(
        s=s,
        cut_angle=cut_angle,
        sharpness=partition_sharpness,
    )

    ref1 = mask1 * mP
    ref2 = mask2 * mP

    D1 = inheritance_efficiency * ref1 + leakage * ref2
    D2 = inheritance_efficiency * ref2 + leakage * ref1

    D1 = np.maximum(D1 + noise_sigma * rng.normal(size=len(s)), 0.0)
    D2 = np.maximum(D2 + noise_sigma * rng.normal(size=len(s)), 0.0)

    D1 = heat_smooth_periodic_fft(D1, ds=ds, smooth_tau=smooth_tau)
    D2 = heat_smooth_periodic_fft(D2, ds=ds, smooth_tau=smooth_tau)

    # Norms
    normP = L2_norm_profile(mP, ds)
    norm_ref1 = L2_norm_profile(ref1, ds)
    norm_ref2 = L2_norm_profile(ref2, ds)
    normD1 = L2_norm_profile(D1, ds)
    normD2 = L2_norm_profile(D2, ds)

    # Fidelity with assigned parent regions
    fid1 = circular_correlation(D1, ref1, ds)
    fid2 = circular_correlation(D2, ref2, ds)

    # Cross-contamination with opposite regions
    cross12 = circular_correlation(D1, ref2, ds)
    cross21 = circular_correlation(D2, ref1, ds)

    # Total memory retention.
    # Use L2-combined daughter norm relative to parent norm.
    total_retention = np.sqrt(normD1**2 + normD2**2) / normP if normP > 1e-12 else np.nan

    # Partition balance and asymmetry
    inherited_sum = normD1 + normD2
    asymmetry = abs(normD1 - normD2) / inherited_sum if inherited_sum > 1e-12 else np.nan

    # Reconstruction from daughters
    reconstructed = D1 + D2
    reconstruction_corr = circular_correlation(reconstructed, mP, ds)
    reconstruction_norm_ratio = L2_norm_profile(reconstructed, ds) / normP if normP > 1e-12 else np.nan

    # Trace-specific inheritance:
    # evaluate response at original memory centers.
    trace1 = periodic_gaussian(s, np.deg2rad(60), 0.20)
    trace2 = periodic_gaussian(s, np.deg2rad(230), 0.24)

    trace1_D1 = float(np.sum(D1 * trace1) * ds)
    trace1_D2 = float(np.sum(D2 * trace1) * ds)
    trace2_D1 = float(np.sum(D1 * trace2) * ds)
    trace2_D2 = float(np.sum(D2 * trace2) * ds)

    return {
        "mask1": mask1,
        "mask2": mask2,
        "ref1": ref1,
        "ref2": ref2,
        "D1": D1,
        "D2": D2,
        "reconstructed": reconstructed,

        "normP": normP,
        "norm_ref1": norm_ref1,
        "norm_ref2": norm_ref2,
        "normD1": normD1,
        "normD2": normD2,

        "fidelity_D1_ref1": fid1,
        "fidelity_D2_ref2": fid2,
        "mean_daughter_fidelity": float(np.nanmean([fid1, fid2])),
        "cross_D1_ref2": cross12,
        "cross_D2_ref1": cross21,
        "mean_cross_contamination": float(np.nanmean([cross12, cross21])),

        "total_retention": float(total_retention),
        "inheritance_asymmetry": float(asymmetry),
        "reconstruction_corr": reconstruction_corr,
        "reconstruction_norm_ratio": float(reconstruction_norm_ratio),

        "trace1_D1": trace1_D1,
        "trace1_D2": trace1_D2,
        "trace2_D1": trace2_D1,
        "trace2_D2": trace2_D2,
    }

def run_B14_2_division_inheritance(
    seed=1421,
    N=256,
    cut_angles_deg=np.linspace(0, 360, 73, endpoint=False),
    partition_sharpness=8.0,
    inheritance_efficiency=0.96,
    leakage=0.04,
    noise_sigma=0.010,
    smooth_tau=0.002,
):
    """
    B14.2:
    Scan division geometry and measure how parent boundary memory is inherited
    by two daughters.
    """

    rng_master = np.random.default_rng(seed)

    s = np.linspace(0, 2 * np.pi, N, endpoint=False)
    ds = s[1] - s[0]

    mP = make_parent_memory_profile(s)
    mP = np.maximum(mP + 0.010 * rng_master.normal(size=N), 0.0)

    rows = []

    results_by_angle = {}

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
            "cut_angle_deg": float(cut_deg),
            "cut_angle_rad": float(cut_angle),

            "normP": res["normP"],
            "normD1": res["normD1"],
            "normD2": res["normD2"],
            "norm_ref1": res["norm_ref1"],
            "norm_ref2": res["norm_ref2"],

            "fidelity_D1_ref1": res["fidelity_D1_ref1"],
            "fidelity_D2_ref2": res["fidelity_D2_ref2"],
            "mean_daughter_fidelity": res["mean_daughter_fidelity"],

            "cross_D1_ref2": res["cross_D1_ref2"],
            "cross_D2_ref1": res["cross_D2_ref1"],
            "mean_cross_contamination": res["mean_cross_contamination"],

            "total_retention": res["total_retention"],
            "inheritance_asymmetry": res["inheritance_asymmetry"],
            "reconstruction_corr": res["reconstruction_corr"],
            "reconstruction_norm_ratio": res["reconstruction_norm_ratio"],

            "trace1_D1": res["trace1_D1"],
            "trace1_D2": res["trace1_D2"],
            "trace2_D1": res["trace2_D1"],
            "trace2_D2": res["trace2_D2"],
        })

        results_by_angle[float(cut_deg)] = res

    scan_df = pd.DataFrame(rows)

    best_fidelity = scan_df.loc[scan_df["mean_daughter_fidelity"].idxmax()].to_dict()
    worst_fidelity = scan_df.loc[scan_df["mean_daughter_fidelity"].idxmin()].to_dict()
    best_retention = scan_df.loc[scan_df["total_retention"].idxmax()].to_dict()
    worst_asymmetry = scan_df.loc[scan_df["inheritance_asymmetry"].idxmax()].to_dict()
    best_reconstruction = scan_df.loc[scan_df["reconstruction_corr"].idxmax()].to_dict()

    # Representative angles
    representative_angles = {
        "best_fidelity": best_fidelity["cut_angle_deg"],
        "worst_fidelity": worst_fidelity["cut_angle_deg"],
        "worst_asymmetry": worst_asymmetry["cut_angle_deg"],
        "best_reconstruction": best_reconstruction["cut_angle_deg"],
    }

    profile_cols = {
        "s": s,
        "s_deg": s * 180 / np.pi,
        "parent_memory": mP,
    }

    for label, angle_deg in representative_angles.items():
        # nearest available angle
        angle_key = min(results_by_angle.keys(), key=lambda x: abs(x - angle_deg))
        res = results_by_angle[angle_key]

        profile_cols[f"{label}_mask1"] = res["mask1"]
        profile_cols[f"{label}_mask2"] = res["mask2"]
        profile_cols[f"{label}_ref1"] = res["ref1"]
        profile_cols[f"{label}_ref2"] = res["ref2"]
        profile_cols[f"{label}_D1"] = res["D1"]
        profile_cols[f"{label}_D2"] = res["D2"]
        profile_cols[f"{label}_reconstructed"] = res["reconstructed"]

    profiles_df = pd.DataFrame(profile_cols)

    # Save data
    save_csv_local(scan_df, "B14_2_division_inheritance_scan.csv")
    save_csv_local(profiles_df, "B14_2_division_inheritance_profiles.csv")

    summary = {
        "experiment": "BIG_B14_2_boundary_memory_division_inheritance",
        "model": "M_P -> (M_D1, M_D2) by smooth partition geometry, leakage, noise, and smoothing",
        "parameters": {
            "seed": seed,
            "N": N,
            "partition_sharpness": partition_sharpness,
            "inheritance_efficiency": inheritance_efficiency,
            "leakage": leakage,
            "noise_sigma": noise_sigma,
            "smooth_tau": smooth_tau,
            "cut_angle_count": int(len(cut_angles_deg)),
        },
        "results": {
            "best_fidelity": best_fidelity,
            "worst_fidelity": worst_fidelity,
            "best_retention": best_retention,
            "worst_asymmetry": worst_asymmetry,
            "best_reconstruction": best_reconstruction,
        },
        "interpretation": (
            "Boundary memory division is geometry-dependent. "
            "Parent memory is not copied uniformly; it is partitioned into daughter memories. "
            "Inheritance fidelity, asymmetry, cross-contamination, and total retention depend on the division axis."
        ),
    }

    save_json_local(summary, "B14_2_division_inheritance_summary.json")

    # --------------------------------------------------------
    # Figures
    # --------------------------------------------------------

    # Figure 1: fidelity and retention vs cut angle
    plt.figure(figsize=(9.0, 5.2))
    plt.plot(scan_df["cut_angle_deg"], scan_df["mean_daughter_fidelity"], marker="o", label="mean daughter fidelity")
    plt.plot(scan_df["cut_angle_deg"], scan_df["total_retention"], marker="s", label="total retention")
    plt.plot(scan_df["cut_angle_deg"], scan_df["reconstruction_corr"], marker="^", label="reconstruction corr")
    plt.xlabel("division axis / cut angle [deg]")
    plt.ylabel("metric")
    plt.title("B14.2 division inheritance depends on partition geometry")
    plt.legend()
    save_fig_local("B14_2_division_inheritance_geometry_scan.png")

    # Figure 2: asymmetry and cross-contamination
    plt.figure(figsize=(9.0, 5.2))
    plt.plot(scan_df["cut_angle_deg"], scan_df["inheritance_asymmetry"], marker="o", label="inheritance asymmetry")
    plt.plot(scan_df["cut_angle_deg"], scan_df["mean_cross_contamination"], marker="s", label="mean cross-contamination")
    plt.xlabel("division axis / cut angle [deg]")
    plt.ylabel("metric")
    plt.title("B14.2 asymmetry and cross-contamination")
    plt.legend()
    save_fig_local("B14_2_division_asymmetry_cross_contamination.png")

    # Figure 3: trace-specific inheritance
    plt.figure(figsize=(9.0, 5.2))
    plt.plot(scan_df["cut_angle_deg"], scan_df["trace1_D1"], label="trace 1 inherited by D1")
    plt.plot(scan_df["cut_angle_deg"], scan_df["trace1_D2"], label="trace 1 inherited by D2")
    plt.plot(scan_df["cut_angle_deg"], scan_df["trace2_D1"], label="trace 2 inherited by D1")
    plt.plot(scan_df["cut_angle_deg"], scan_df["trace2_D2"], label="trace 2 inherited by D2")
    plt.xlabel("division axis / cut angle [deg]")
    plt.ylabel("trace inheritance")
    plt.title("B14.2 trace-specific daughter inheritance")
    plt.legend()
    save_fig_local("B14_2_trace_specific_inheritance.png")

    # Figure 4: best fidelity profiles
    angle_key = min(results_by_angle.keys(), key=lambda x: abs(x - best_fidelity["cut_angle_deg"]))
    res = results_by_angle[angle_key]

    plt.figure(figsize=(9.0, 5.4))
    plt.plot(s * 180 / np.pi, mP, label="parent memory", linewidth=2)
    plt.plot(s * 180 / np.pi, res["ref1"], linestyle="--", label="reference D1 partition")
    plt.plot(s * 180 / np.pi, res["ref2"], linestyle="--", label="reference D2 partition")
    plt.plot(s * 180 / np.pi, res["D1"], label="daughter D1 memory")
    plt.plot(s * 180 / np.pi, res["D2"], label="daughter D2 memory")
    plt.xlabel("boundary coordinate s [deg]")
    plt.ylabel("memory")
    plt.title(f"B14.2 best-fidelity division profile, cut={angle_key:.1f}°")
    plt.legend()
    save_fig_local("B14_2_best_fidelity_division_profile.png")

    # Figure 5: worst asymmetry profiles
    angle_key = min(results_by_angle.keys(), key=lambda x: abs(x - worst_asymmetry["cut_angle_deg"]))
    res = results_by_angle[angle_key]

    plt.figure(figsize=(9.0, 5.4))
    plt.plot(s * 180 / np.pi, mP, label="parent memory", linewidth=2)
    plt.plot(s * 180 / np.pi, res["D1"], label="daughter D1 memory")
    plt.plot(s * 180 / np.pi, res["D2"], label="daughter D2 memory")
    plt.plot(s * 180 / np.pi, res["mask1"], linestyle=":", label="mask1")
    plt.plot(s * 180 / np.pi, res["mask2"], linestyle=":", label="mask2")
    plt.xlabel("boundary coordinate s [deg]")
    plt.ylabel("memory / mask")
    plt.title(f"B14.2 high-asymmetry division profile, cut={angle_key:.1f}°")
    plt.legend()
    save_fig_local("B14_2_high_asymmetry_division_profile.png")

    # Figure 6: reconstruction
    angle_key = min(results_by_angle.keys(), key=lambda x: abs(x - best_reconstruction["cut_angle_deg"]))
    res = results_by_angle[angle_key]

    plt.figure(figsize=(9.0, 5.4))
    plt.plot(s * 180 / np.pi, mP, label="parent memory", linewidth=2)
    plt.plot(s * 180 / np.pi, res["reconstructed"], linestyle="--", label="D1 + D2 reconstructed")
    plt.plot(s * 180 / np.pi, res["D1"], label="D1")
    plt.plot(s * 180 / np.pi, res["D2"], label="D2")
    plt.xlabel("boundary coordinate s [deg]")
    plt.ylabel("memory")
    plt.title(f"B14.2 daughter reconstruction, cut={angle_key:.1f}°")
    plt.legend()
    save_fig_local("B14_2_daughter_reconstruction_profile.png")

    print("B14.2 division inheritance complete.")
    print(json.dumps(summary, indent=2))

    return scan_df, profiles_df, summary
