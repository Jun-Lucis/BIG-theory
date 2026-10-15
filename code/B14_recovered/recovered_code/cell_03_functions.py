# Original notebook computational definitions, cell 3

def heat_smooth_periodic_fft(m, ds, smooth_tau=0.003):
    """
    Stable heat-kernel smoothing on periodic 1D boundary.

    Solves approximately:
        ∂_τ m = ∂_s^2 m
    by Fourier multiplier:
        exp(-k^2 tau)

    This avoids explicit diffusion instability.
    """
    m = np.asarray(m, dtype=float)
    N = len(m)

    # angular wavenumbers for coordinate s in radians
    freqs = np.fft.fftfreq(N, d=ds)
    k = 2 * np.pi * freqs

    mhat = np.fft.fft(m)
    multiplier = np.exp(-(k ** 2) * smooth_tau)

    smoothed = np.real(np.fft.ifft(mhat * multiplier))
    return np.maximum(smoothed, 0.0)

def make_memory_profile(s, centers, widths, amps):
    """
    Boundary memory profile as sum of periodic Gaussian traces.
    """
    m = np.zeros_like(s)
    for c, w, a in zip(centers, widths, amps):
        m += a * periodic_gaussian(s, c, w)
    return np.maximum(m, 0.0)

def shift_profile_periodic(m, shift_steps):
    """
    Periodic integer shift.
    """
    return np.roll(m, shift_steps)

def L2_norm_profile(m, ds):
    return float(np.sqrt(np.sum(m * m) * ds))

def fusion_compress_profiles_stable(
    mA,
    mB,
    s,
    ds,
    alignment_shift_steps=0,
    compression_gamma=0.35,
    conflict_gamma=0.50,
    smooth_tau=0.003,
    eps=1e-12,
):
    """
    Stable reduced fusion-compression map.

    Steps:
      1. Align B to A.
      2. Form raw_sum = A + B.
      3. Apply local conflict saturation where A and B overlap.
      4. Apply global compression proportional to positive overlap.
      5. Smooth with stable FFT heat kernel.

    Interpretation:
      This is not biological membrane fusion.
      It is a reduced boundary-memory compression map.
    """

    mB_aligned = shift_profile_periodic(mB, alignment_shift_steps)

    overlap = circular_correlation(mA, mB_aligned, ds)
    if np.isnan(overlap):
        overlap = 0.0

    overlap_pos = max(0.0, float(overlap))

    raw_sum = mA + mB_aligned

    # Local conflict index, bounded and dimensionless.
    scale = max(float(np.max(raw_sum)), eps)
    conflict = (mA * mB_aligned) / (scale ** 2 + eps)

    # Local saturation: high conflict reduces local amplitude.
    local_factor = np.exp(-conflict_gamma * conflict)
    mC = raw_sum * local_factor

    # Stable smoothing.
    mC = heat_smooth_periodic_fft(mC, ds=ds, smooth_tau=smooth_tau)

    # Global compression: stronger overlap -> stronger compression.
    norm_raw = L2_norm_profile(raw_sum, ds)
    norm_C_pre = L2_norm_profile(mC, ds)

    compression_factor = 1.0 - compression_gamma * overlap_pos
    compression_factor = float(np.clip(compression_factor, 1.0 - compression_gamma, 1.0))

    target_norm = norm_raw * compression_factor

    if norm_C_pre > eps:
        mC = mC * (target_norm / norm_C_pre)

    mC = np.maximum(mC, 0.0)

    # Metrics
    norm_A = L2_norm_profile(mA, ds)
    norm_B = L2_norm_profile(mB_aligned, ds)
    norm_C = L2_norm_profile(mC, ds)

    corr_C_A = circular_correlation(mC, mA, ds)
    corr_C_B = circular_correlation(mC, mB_aligned, ds)
    corr_C_raw_sum = circular_correlation(mC, raw_sum, ds)

    compression_loss_ratio = 1.0 - norm_C / norm_raw if norm_raw > eps else np.nan

    # Memory preservation score: shape preservation and norm preservation together.
    preservation_score = corr_C_raw_sum * (1.0 - compression_loss_ratio)

    return {
        "mB_aligned": mB_aligned,
        "raw_sum": raw_sum,
        "conflict": conflict,
        "mC": mC,
        "overlap_AB": float(overlap),
        "overlap_pos": float(overlap_pos),
        "corr_C_A": corr_C_A,
        "corr_C_B": corr_C_B,
        "corr_C_raw_sum": corr_C_raw_sum,
        "norm_A": norm_A,
        "norm_B": norm_B,
        "norm_raw_sum": norm_raw,
        "norm_C": norm_C,
        "compression_factor": compression_factor,
        "compression_loss_ratio": compression_loss_ratio,
        "preservation_score": preservation_score,
    }

def run_B14_1_fusion_compression_stable(
    seed=1411,
    N=256,
    compression_gamma=0.35,
    conflict_gamma=0.50,
    smooth_tau=0.003,
):
    """
    B14.1 stable fusion compression scan.
    """

    rng = np.random.default_rng(seed)

    s = np.linspace(0, 2 * np.pi, N, endpoint=False)
    ds = s[1] - s[0]

    # Boundary memory A
    mA = make_memory_profile(
        s,
        centers=[np.deg2rad(60)],
        widths=[0.20],
        amps=[1.00],
    )

    # Boundary memory B
    mB = make_memory_profile(
        s,
        centers=[np.deg2rad(210)],
        widths=[0.22],
        amps=[0.85],
    )

    # Mild nonnegative memory noise
    mA = np.maximum(mA + 0.015 * rng.normal(size=N), 0.0)
    mB = np.maximum(mB + 0.015 * rng.normal(size=N), 0.0)

    shift_deg_values = np.linspace(-180, 180, 49)

    rows = []

    for shift_deg in shift_deg_values:
        shift_steps = int(np.round((shift_deg / 360.0) * N))

        res = fusion_compress_profiles_stable(
            mA=mA,
            mB=mB,
            s=s,
            ds=ds,
            alignment_shift_steps=shift_steps,
            compression_gamma=compression_gamma,
            conflict_gamma=conflict_gamma,
            smooth_tau=smooth_tau,
        )

        rows.append({
            "shift_deg": float(shift_deg),
            "shift_steps": int(shift_steps),
            "overlap_AB": res["overlap_AB"],
            "overlap_pos": res["overlap_pos"],
            "corr_C_A": res["corr_C_A"],
            "corr_C_B": res["corr_C_B"],
            "corr_C_raw_sum": res["corr_C_raw_sum"],
            "norm_A": res["norm_A"],
            "norm_B": res["norm_B"],
            "norm_raw_sum": res["norm_raw_sum"],
            "norm_C": res["norm_C"],
            "compression_factor": res["compression_factor"],
            "compression_loss_ratio": res["compression_loss_ratio"],
            "preservation_score": res["preservation_score"],
        })

    summary_df = pd.DataFrame(rows)

    best_preservation = summary_df.loc[summary_df["preservation_score"].idxmax()].to_dict()
    best_shape_preservation = summary_df.loc[summary_df["corr_C_raw_sum"].idxmax()].to_dict()
    worst_loss = summary_df.loc[summary_df["compression_loss_ratio"].idxmax()].to_dict()
    max_overlap = summary_df.loc[summary_df["overlap_AB"].idxmax()].to_dict()
    min_overlap = summary_df.loc[summary_df["overlap_AB"].idxmin()].to_dict()

    def compute_at_shift(shift_deg):
        shift_steps = int(np.round((shift_deg / 360.0) * N))
        return fusion_compress_profiles_stable(
            mA=mA,
            mB=mB,
            s=s,
            ds=ds,
            alignment_shift_steps=shift_steps,
            compression_gamma=compression_gamma,
            conflict_gamma=conflict_gamma,
            smooth_tau=smooth_tau,
        )

    best_res = compute_at_shift(best_preservation["shift_deg"])
    max_overlap_res = compute_at_shift(max_overlap["shift_deg"])
    min_overlap_res = compute_at_shift(min_overlap["shift_deg"])

    profile_df = pd.DataFrame({
        "s": s,
        "s_deg": s * 180 / np.pi,
        "mA": mA,
        "mB_original": mB,

        "best_mB_aligned": best_res["mB_aligned"],
        "best_raw_sum": best_res["raw_sum"],
        "best_conflict": best_res["conflict"],
        "best_fused_memory": best_res["mC"],

        "max_overlap_mB_aligned": max_overlap_res["mB_aligned"],
        "max_overlap_raw_sum": max_overlap_res["raw_sum"],
        "max_overlap_conflict": max_overlap_res["conflict"],
        "max_overlap_fused_memory": max_overlap_res["mC"],

        "min_overlap_mB_aligned": min_overlap_res["mB_aligned"],
        "min_overlap_raw_sum": min_overlap_res["raw_sum"],
        "min_overlap_conflict": min_overlap_res["conflict"],
        "min_overlap_fused_memory": min_overlap_res["mC"],
    })

    save_csv_local(summary_df, "B14_1b_fusion_compression_stable_scan.csv")
    save_csv_local(profile_df, "B14_1b_fusion_compression_stable_profiles.csv")

    summary = {
        "experiment": "BIG_B14_1b_boundary_memory_fusion_compression_stable",
        "model": "stable M_C = C_fuse(M_A, M_B, alignment, conflict, compression)",
        "parameters": {
            "seed": seed,
            "N": N,
            "compression_gamma": compression_gamma,
            "conflict_gamma": conflict_gamma,
            "smooth_tau": smooth_tau,
            "shift_scan_deg_min": float(np.min(shift_deg_values)),
            "shift_scan_deg_max": float(np.max(shift_deg_values)),
            "shift_scan_count": int(len(shift_deg_values)),
        },
        "results": {
            "best_preservation": best_preservation,
            "best_shape_preservation": best_shape_preservation,
            "worst_loss": worst_loss,
            "max_overlap": max_overlap,
            "min_overlap": min_overlap,
        },
        "interpretation": (
            "Stable fusion-compression test. Boundary memory fusion is alignment-dependent. "
            "High overlap increases compression loss, while low-conflict alignment better preserves "
            "the combined memory trace."
        ),
    }

    save_json_local(summary, "B14_1b_fusion_compression_stable_summary.json")

    # --------------------------------------------------------
    # Figures
    # --------------------------------------------------------

    plt.figure(figsize=(8.5, 5.2))
    plt.plot(summary_df["shift_deg"], summary_df["overlap_AB"], marker="o", label="A-B overlap")
    plt.plot(summary_df["shift_deg"], summary_df["corr_C_raw_sum"], marker="s", label="corr(fused, raw sum)")
    plt.plot(summary_df["shift_deg"], summary_df["compression_loss_ratio"], marker="^", label="compression loss")
    plt.plot(summary_df["shift_deg"], summary_df["preservation_score"], marker="x", label="preservation score")
    plt.xlabel("alignment shift of B [deg]")
    plt.ylabel("metric")
    plt.title("B14.1b stable fusion compression depends on alignment")
    plt.legend()
    save_fig_local("B14_1b_fusion_compression_stable_alignment_scan.png")

    plt.figure(figsize=(8.8, 5.2))
    plt.plot(profile_df["s_deg"], profile_df["mA"], label="mA")
    plt.plot(profile_df["s_deg"], profile_df["best_mB_aligned"], label=f"mB aligned, best shift={best_preservation['shift_deg']:.1f}°")
    plt.plot(profile_df["s_deg"], profile_df["best_raw_sum"], linestyle="--", label="raw sum")
    plt.plot(profile_df["s_deg"], profile_df["best_fused_memory"], linewidth=2, label="fused compressed memory")
    plt.xlabel("boundary coordinate s [deg]")
    plt.ylabel("memory")
    plt.title("B14.1b best-preservation fusion profile")
    plt.legend()
    save_fig_local("B14_1b_fusion_best_preservation_profiles.png")

    plt.figure(figsize=(8.8, 5.2))
    plt.plot(profile_df["s_deg"], profile_df["mA"], label="mA")
    plt.plot(profile_df["s_deg"], profile_df["max_overlap_mB_aligned"], label=f"mB aligned, max overlap shift={max_overlap['shift_deg']:.1f}°")
    plt.plot(profile_df["s_deg"], profile_df["max_overlap_raw_sum"], linestyle="--", label="raw sum")
    plt.plot(profile_df["s_deg"], profile_df["max_overlap_fused_memory"], linewidth=2, label="fused compressed memory")
    plt.plot(profile_df["s_deg"], profile_df["max_overlap_conflict"], linestyle=":", label="conflict")
    plt.xlabel("boundary coordinate s [deg]")
    plt.ylabel("memory")
    plt.title("B14.1b high-overlap fusion conflict")
    plt.legend()
    save_fig_local("B14_1b_fusion_high_overlap_conflict_profiles.png")

    plt.figure(figsize=(8.8, 5.2))
    plt.plot(profile_df["s_deg"], profile_df["mA"], label="mA")
    plt.plot(profile_df["s_deg"], profile_df["min_overlap_mB_aligned"], label=f"mB aligned, min overlap shift={min_overlap['shift_deg']:.1f}°")
    plt.plot(profile_df["s_deg"], profile_df["min_overlap_raw_sum"], linestyle="--", label="raw sum")
    plt.plot(profile_df["s_deg"], profile_df["min_overlap_fused_memory"], linewidth=2, label="fused compressed memory")
    plt.xlabel("boundary coordinate s [deg]")
    plt.ylabel("memory")
    plt.title("B14.1b low-overlap fusion profile")
    plt.legend()
    save_fig_local("B14_1b_fusion_low_overlap_profiles.png")

    plt.figure(figsize=(8.0, 5.0))
    plt.plot(summary_df["shift_deg"], summary_df["norm_raw_sum"], label="raw-sum norm")
    plt.plot(summary_df["shift_deg"], summary_df["norm_C"], label="fused memory norm")
    plt.xlabel("alignment shift of B [deg]")
    plt.ylabel("L2 norm")
    plt.title("B14.1b memory norm before and after stable fusion compression")
    plt.legend()
    save_fig_local("B14_1b_fusion_norm_comparison.png")

    plt.figure(figsize=(7.0, 5.2))
    plt.scatter(summary_df["overlap_AB"], summary_df["compression_loss_ratio"])
    plt.xlabel("A-B overlap")
    plt.ylabel("compression loss ratio")
    plt.title("B14.1b overlap vs compression loss")
    save_fig_local("B14_1b_overlap_vs_compression_loss.png")

    print("B14.1b stable fusion compression complete.")
    print(json.dumps(summary, indent=2))

    return summary_df, profile_df, summary
