# Original notebook computational definitions, cell 2

def normalize_profile(m, ds, eps=1e-12):
    norm = np.sqrt(np.sum(m * m) * ds)
    if norm < eps:
        return m.copy()
    return m / norm

def make_memory_profile(
    s,
    centers,
    widths,
    amps,
):
    """
    Create boundary memory profile as sum of periodic Gaussian traces.
    """
    m = np.zeros_like(s)
    for c, w, a in zip(centers, widths, amps):
        m += a * periodic_gaussian(s, c, w)
    return np.maximum(m, 0.0)

def shift_profile_periodic(m, shift_steps):
    """
    Shift profile by integer steps on periodic grid.
    """
    return np.roll(m, shift_steps)

def fusion_compress_profiles(
    mA,
    mB,
    s,
    ds,
    alignment_shift_steps=0,
    compression_gamma=0.35,
    conflict_gamma=0.50,
    smoothing_steps=12,
    smoothing_D=0.015,
):
    """
    Reduced fusion-compression map.

    1. Align B to A by a shift.
    2. Combine traces.
    3. Penalize conflict/overlap saturation.
    4. Smooth as a compression-relaxation process.

    This is not biological membrane fusion.
    It is a toy model of memory compression under boundary fusion.
    """
    mB_aligned = shift_profile_periodic(mB, alignment_shift_steps)

    # normalized overlap / conflict
    overlap = circular_correlation(mA, mB_aligned, ds)

    raw_sum = mA + mB_aligned

    # conflict term: where both memories are strong, compression/saturation occurs
    conflict = mA * mB_aligned

    # compression map
    mC = raw_sum - conflict_gamma * conflict / (1.0 + conflict)
    mC = np.maximum(mC, 0.0)

    # global compression
    raw_norm = np.sqrt(np.sum(raw_sum * raw_sum) * ds)
    mC_norm = np.sqrt(np.sum(mC * mC) * ds)
    if mC_norm > 1e-12:
        target_norm = (1.0 - compression_gamma) * raw_norm + compression_gamma * max(
            np.sqrt(np.sum(mA * mA) * ds),
            np.sqrt(np.sum(mB_aligned * mB_aligned) * ds),
        )
        mC = mC * (target_norm / mC_norm)

    # smoothing relaxation on fused boundary
    for _ in range(smoothing_steps):
        mC = mC + smoothing_D * laplacian_periodic_1d(mC, ds)
        mC = np.maximum(mC, 0.0)

    # metrics
    corr_A = circular_correlation(mC, mA, ds)
    corr_B = circular_correlation(mC, mB_aligned, ds)
    corr_sum = circular_correlation(mC, raw_sum, ds)

    norm_A = float(np.sqrt(np.sum(mA * mA) * ds))
    norm_B = float(np.sqrt(np.sum(mB_aligned * mB_aligned) * ds))
    norm_raw = float(np.sqrt(np.sum(raw_sum * raw_sum) * ds))
    norm_C = float(np.sqrt(np.sum(mC * mC) * ds))

    loss_ratio = 1.0 - norm_C / norm_raw if norm_raw > 1e-12 else np.nan

    return {
        "mB_aligned": mB_aligned,
        "mC": mC,
        "raw_sum": raw_sum,
        "conflict": conflict,
        "overlap_AB": overlap,
        "corr_C_A": corr_A,
        "corr_C_B": corr_B,
        "corr_C_raw_sum": corr_sum,
        "norm_A": norm_A,
        "norm_B": norm_B,
        "norm_raw_sum": norm_raw,
        "norm_C": norm_C,
        "compression_loss_ratio": loss_ratio,
    }

def run_B14_1_fusion_compression(
    seed=1411,
    N=256,
    compression_gamma=0.35,
    conflict_gamma=0.50,
    smoothing_steps=12,
    smoothing_D=0.015,
):
    """
    B14.1 tests whether boundary memories can be fused and compressed.
    We scan alignment shifts between two memory profiles.
    """

    rng = np.random.default_rng(seed)

    s = np.linspace(0, 2 * np.pi, N, endpoint=False)
    ds = s[1] - s[0]

    # Two memory-bearing boundaries
    mA = make_memory_profile(
        s,
        centers=[np.deg2rad(60)],
        widths=[0.20],
        amps=[1.0],
    )

    mB = make_memory_profile(
        s,
        centers=[np.deg2rad(210)],
        widths=[0.22],
        amps=[0.85],
    )

    # mild noise in memory
    mA = np.maximum(mA + 0.015 * rng.normal(size=N), 0.0)
    mB = np.maximum(mB + 0.015 * rng.normal(size=N), 0.0)

    # Scan alignment shifts
    shift_deg_values = np.linspace(-180, 180, 49)
    rows = []
    profile_records = {}

    for shift_deg in shift_deg_values:
        shift_steps = int(np.round((shift_deg / 360.0) * N))

        res = fusion_compress_profiles(
            mA=mA,
            mB=mB,
            s=s,
            ds=ds,
            alignment_shift_steps=shift_steps,
            compression_gamma=compression_gamma,
            conflict_gamma=conflict_gamma,
            smoothing_steps=smoothing_steps,
            smoothing_D=smoothing_D,
        )

        rows.append({
            "shift_deg": float(shift_deg),
            "shift_steps": int(shift_steps),
            "overlap_AB": res["overlap_AB"],
            "corr_C_A": res["corr_C_A"],
            "corr_C_B": res["corr_C_B"],
            "corr_C_raw_sum": res["corr_C_raw_sum"],
            "norm_A": res["norm_A"],
            "norm_B": res["norm_B"],
            "norm_raw_sum": res["norm_raw_sum"],
            "norm_C": res["norm_C"],
            "compression_loss_ratio": res["compression_loss_ratio"],
        })

        # Save representative cases
        if shift_deg in [-180, -90, 0, 90, 180]:
            profile_records[shift_deg] = res

    summary_df = pd.DataFrame(rows)

    best_preservation = summary_df.loc[summary_df["corr_C_raw_sum"].idxmax()].to_dict()
    worst_loss = summary_df.loc[summary_df["compression_loss_ratio"].idxmax()].to_dict()
    max_overlap = summary_df.loc[summary_df["overlap_AB"].idxmax()].to_dict()

    # representative profiles: choose best and high-overlap cases
    best_shift_deg = best_preservation["shift_deg"]
    high_overlap_shift_deg = max_overlap["shift_deg"]

    def compute_at_shift(shift_deg):
        shift_steps = int(np.round((shift_deg / 360.0) * N))
        return fusion_compress_profiles(
            mA=mA,
            mB=mB,
            s=s,
            ds=ds,
            alignment_shift_steps=shift_steps,
            compression_gamma=compression_gamma,
            conflict_gamma=conflict_gamma,
            smoothing_steps=smoothing_steps,
            smoothing_D=smoothing_D,
        )

    best_res = compute_at_shift(best_shift_deg)
    overlap_res = compute_at_shift(high_overlap_shift_deg)

    profile_df = pd.DataFrame({
        "s": s,
        "s_deg": s * 180 / np.pi,
        "mA": mA,
        "mB_original": mB,
        "best_mB_aligned": best_res["mB_aligned"],
        "best_raw_sum": best_res["raw_sum"],
        "best_fused_memory": best_res["mC"],
        "overlap_mB_aligned": overlap_res["mB_aligned"],
        "overlap_raw_sum": overlap_res["raw_sum"],
        "overlap_fused_memory": overlap_res["mC"],
        "overlap_conflict": overlap_res["conflict"],
    })

    # Save
    save_csv_local(summary_df, "B14_1_fusion_compression_scan.csv")
    save_csv_local(profile_df, "B14_1_fusion_compression_profiles.csv")

    summary = {
        "experiment": "BIG_B14_1_boundary_memory_fusion_compression",
        "model": "M_C = C_fuse(M_A, M_B, alignment, conflict, compression)",
        "parameters": {
            "seed": seed,
            "N": N,
            "compression_gamma": compression_gamma,
            "conflict_gamma": conflict_gamma,
            "smoothing_steps": smoothing_steps,
            "smoothing_D": smoothing_D,
            "shift_scan_deg_min": float(np.min(shift_deg_values)),
            "shift_scan_deg_max": float(np.max(shift_deg_values)),
            "shift_scan_count": int(len(shift_deg_values)),
        },
        "results": {
            "best_preservation": best_preservation,
            "worst_loss": worst_loss,
            "max_overlap": max_overlap,
        },
        "interpretation": (
            "Fusion compression is alignment-dependent. "
            "When boundary memories overlap strongly, conflict and compression can reduce memory norm. "
            "When aligned without severe conflict, the fused memory preserves the combined trace more faithfully."
        ),
    }

    save_json_local(summary, "B14_1_fusion_compression_summary.json")

    # Figures

    # Figure 1: scan metrics
    plt.figure(figsize=(8.5, 5.2))
    plt.plot(summary_df["shift_deg"], summary_df["overlap_AB"], marker="o", label="A-B overlap")
    plt.plot(summary_df["shift_deg"], summary_df["corr_C_raw_sum"], marker="s", label="corr(fused, raw sum)")
    plt.plot(summary_df["shift_deg"], summary_df["compression_loss_ratio"], marker="^", label="compression loss ratio")
    plt.xlabel("alignment shift of B [deg]")
    plt.ylabel("metric")
    plt.title("B14.1 fusion compression depends on alignment")
    plt.legend()
    save_fig_local("B14_1_fusion_compression_alignment_scan.png")

    # Figure 2: best preservation profiles
    plt.figure(figsize=(8.8, 5.2))
    plt.plot(profile_df["s_deg"], profile_df["mA"], label="mA")
    plt.plot(profile_df["s_deg"], profile_df["best_mB_aligned"], label=f"mB aligned, best shift={best_shift_deg:.1f}°")
    plt.plot(profile_df["s_deg"], profile_df["best_raw_sum"], linestyle="--", label="raw sum")
    plt.plot(profile_df["s_deg"], profile_df["best_fused_memory"], linewidth=2, label="fused compressed memory")
    plt.xlabel("boundary coordinate s [deg]")
    plt.ylabel("memory")
    plt.title("B14.1 best-preservation fusion profile")
    plt.legend()
    save_fig_local("B14_1_fusion_best_preservation_profiles.png")

    # Figure 3: high-overlap / conflict profile
    plt.figure(figsize=(8.8, 5.2))
    plt.plot(profile_df["s_deg"], profile_df["mA"], label="mA")
    plt.plot(profile_df["s_deg"], profile_df["overlap_mB_aligned"], label=f"mB aligned, max overlap shift={high_overlap_shift_deg:.1f}°")
    plt.plot(profile_df["s_deg"], profile_df["overlap_raw_sum"], linestyle="--", label="raw sum")
    plt.plot(profile_df["s_deg"], profile_df["overlap_fused_memory"], linewidth=2, label="fused compressed memory")
    plt.plot(profile_df["s_deg"], profile_df["overlap_conflict"], linestyle=":", label="conflict term")
    plt.xlabel("boundary coordinate s [deg]")
    plt.ylabel("memory")
    plt.title("B14.1 high-overlap fusion conflict")
    plt.legend()
    save_fig_local("B14_1_fusion_high_overlap_conflict_profiles.png")

    # Figure 4: norm comparison
    plt.figure(figsize=(8.0, 5.0))
    plt.plot(summary_df["shift_deg"], summary_df["norm_raw_sum"], label="raw-sum norm")
    plt.plot(summary_df["shift_deg"], summary_df["norm_C"], label="fused memory norm")
    plt.xlabel("alignment shift of B [deg]")
    plt.ylabel("L2 norm")
    plt.title("B14.1 memory norm before and after fusion compression")
    plt.legend()
    save_fig_local("B14_1_fusion_norm_comparison.png")

    print("B14.1 fusion compression complete.")
    print(json.dumps(summary, indent=2))

    return summary_df, profile_df, summary
