# Original notebook computational definitions, cell 1

def periodic_angle_distance(s, s0):
    """
    Periodic signed distance on circle [0, 2pi).
    """
    return np.angle(np.exp(1j * (s - s0)))

def periodic_gaussian(s, s0, width):
    """
    Periodic Gaussian-like bump centered at s0.
    """
    d = periodic_angle_distance(s, s0)
    return np.exp(-0.5 * (d / width) ** 2)

def laplacian_periodic_1d(m, ds):
    """
    Periodic second derivative on a 1D circle.
    """
    return (np.roll(m, -1) - 2 * m + np.roll(m, 1)) / (ds ** 2)

def circular_correlation(a, b, ds):
    """
    Normalized inner product on circle.
    """
    num = np.sum(a * b) * ds
    den = np.sqrt(np.sum(a * a) * ds) * np.sqrt(np.sum(b * b) * ds)
    if den < 1e-12:
        return np.nan
    return float(num / den)

def memory_width(s, m):
    """
    Approximate circular width from first trigonometric moment.
    Smaller R means broader distribution.
    """
    weights = np.maximum(m, 0)
    total = np.sum(weights)
    if total < 1e-12:
        return np.nan, np.nan

    z = np.sum(weights * np.exp(1j * s)) / total
    R = np.abs(z)
    mean_angle = np.angle(z) % (2 * np.pi)

    # circular std approximation
    width = np.sqrt(max(0.0, -2.0 * np.log(max(R, 1e-12))))
    return float(mean_angle), float(width)

def simulate_boundary_memory_writing(
    seed=1401,
    N=256,
    T=8.0,
    dt=0.005,
    alpha=0.18,
    beta=1.00,
    D_sigma=0.020,
    noise_sigma=0.010,
    stimulus_center=np.pi / 3,
    stimulus_width=0.18,
    stimulus_amp=1.0,
    write_t0=0.5,
    write_t1=2.5,
    response_lambda=1.25,
    chi0=1.0,
    probe_width=0.18,
):
    """
    B14.0 minimal boundary memory model.

    Boundary memory:
        dm/dt = -alpha*m + beta*I(s,t) + D_sigma*d2m/ds2 + noise

    After writing/decay, response susceptibility is:
        chi(s) = chi0 + response_lambda * m(s)

    Probe response at center q:
        R(q) = ∫ probe_q(s) chi(s) ds

    This tests:
      1. memory writing
      2. decay/persistence
      3. spatial spreading
      4. history-dependent response amplification
    """

    rng = np.random.default_rng(seed)

    s = np.linspace(0, 2 * np.pi, N, endpoint=False)
    ds = s[1] - s[0]

    n_steps = int(T / dt)
    times = np.arange(n_steps + 1) * dt

    m = np.zeros(N)

    snapshots = []
    snapshot_times = []

    rows = []

    # store initial stimulus shape
    stimulus_shape = periodic_gaussian(s, stimulus_center, stimulus_width)
    stimulus_shape /= np.max(stimulus_shape)

    post_write_profile = None
    final_profile = None

    for step, t in enumerate(times):
        # stimulus schedule
        if write_t0 <= t <= write_t1:
            I = stimulus_amp * stimulus_shape
        else:
            I = np.zeros_like(s)

        # diagnostics before update
        L2 = float(np.sqrt(np.sum(m * m) * ds))
        L1 = float(np.sum(np.abs(m)) * ds)
        peak = float(np.max(m))
        minv = float(np.min(m))
        meanv = float(np.mean(m))

        corr_stim = circular_correlation(m, stimulus_shape, ds)
        mean_angle, circ_width = memory_width(s, m)

        rows.append({
            "t": t,
            "L2_memory": L2,
            "L1_memory": L1,
            "peak_memory": peak,
            "min_memory": minv,
            "mean_memory": meanv,
            "corr_with_initial_stimulus": corr_stim,
            "memory_mean_angle": mean_angle,
            "memory_circular_width_rad": circ_width,
            "stimulus_on": int(write_t0 <= t <= write_t1),
        })

        # snapshots
        if step % max(1, n_steps // 160) == 0 or step == n_steps:
            snapshots.append(m.copy())
            snapshot_times.append(t)

        # record post-write profile around write_t1
        if post_write_profile is None and t >= write_t1:
            post_write_profile = m.copy()

        if step == n_steps:
            final_profile = m.copy()
            break

        # update
        lap = laplacian_periodic_1d(m, ds)
        dm_det = -alpha * m + beta * I + D_sigma * lap
        dm_noise = noise_sigma * np.sqrt(dt) * rng.normal(size=N)

        m = m + dt * dm_det + dm_noise

        # mild floor to avoid noise-dominated negative memory for this first model
        # This keeps memory as an accumulated trace variable.
        m = np.maximum(m, 0.0)

    diagnostics_df = pd.DataFrame(rows)
    snapshots_arr = np.array(snapshots)
    snapshot_times = np.array(snapshot_times)

    # --------------------------------------------------------
    # Response map after decay
    # --------------------------------------------------------

    probe_centers = np.linspace(0, 2 * np.pi, 181, endpoint=False)
    response_rows = []

    chi_final = chi0 + response_lambda * final_profile
    chi_baseline = chi0 * np.ones_like(final_profile)

    for q in probe_centers:
        probe = periodic_gaussian(s, q, probe_width)
        probe /= np.sum(probe) * ds

        response_baseline = float(np.sum(probe * chi_baseline) * ds)
        response_memory = float(np.sum(probe * chi_final) * ds)
        response_gain = response_memory - response_baseline

        response_rows.append({
            "probe_center": q,
            "probe_center_deg": q * 180 / np.pi,
            "response_baseline": response_baseline,
            "response_with_memory": response_memory,
            "response_gain": response_gain,
        })

    response_df = pd.DataFrame(response_rows)

    # key locations
    trained_q = stimulus_center
    opposite_q = (stimulus_center + np.pi) % (2 * np.pi)

    def nearest_response(q):
        idx = np.argmin(np.abs(periodic_angle_distance(response_df["probe_center"].to_numpy(), q)))
        return response_df.iloc[idx].to_dict()

    trained_response = nearest_response(trained_q)
    opposite_response = nearest_response(opposite_q)

    # persistence metrics
    post_write_L2 = float(np.sqrt(np.sum(post_write_profile * post_write_profile) * ds))
    final_L2 = float(np.sqrt(np.sum(final_profile * final_profile) * ds))
    persistence_ratio = final_L2 / post_write_L2 if post_write_L2 > 1e-12 else np.nan

    final_corr = circular_correlation(final_profile, stimulus_shape, ds)
    final_angle, final_width = memory_width(s, final_profile)

    summary = {
        "experiment": "BIG_B14_0_boundary_memory_writing_decay_response",
        "model": "dm/dt = -alpha*m + beta*I + D_sigma*d2m/ds2 + noise",
        "parameters": {
            "seed": seed,
            "N": N,
            "T": T,
            "dt": dt,
            "alpha": alpha,
            "beta": beta,
            "D_sigma": D_sigma,
            "noise_sigma": noise_sigma,
            "stimulus_center_rad": float(stimulus_center),
            "stimulus_center_deg": float(stimulus_center * 180 / np.pi),
            "stimulus_width_rad": stimulus_width,
            "stimulus_amp": stimulus_amp,
            "write_t0": write_t0,
            "write_t1": write_t1,
            "response_lambda": response_lambda,
            "chi0": chi0,
            "probe_width": probe_width,
        },
        "results": {
            "post_write_L2_memory": post_write_L2,
            "final_L2_memory": final_L2,
            "persistence_ratio_final_over_post_write": persistence_ratio,
            "final_corr_with_initial_stimulus": final_corr,
            "final_memory_mean_angle_rad": final_angle,
            "final_memory_mean_angle_deg": None if np.isnan(final_angle) else float(final_angle * 180 / np.pi),
            "final_memory_width_rad": final_width,
            "final_memory_width_deg": None if np.isnan(final_width) else float(final_width * 180 / np.pi),
            "trained_response_gain": trained_response["response_gain"],
            "opposite_response_gain": opposite_response["response_gain"],
            "response_gain_contrast_trained_minus_opposite": trained_response["response_gain"] - opposite_response["response_gain"],
        },
        "interpretation": (
            "A localized boundary stimulus writes a boundary memory trace. "
            "The trace decays and spreads but can persist after stimulus removal. "
            "A later probe response is amplified near the trained boundary location, "
            "indicating history-dependent boundary response."
        ),
    }

    # --------------------------------------------------------
    # Save data
    # --------------------------------------------------------

    save_csv_local(diagnostics_df, "B14_0_memory_diagnostics_timeseries.csv")
    save_csv_local(response_df, "B14_0_history_dependent_response_map.csv")

    profile_df = pd.DataFrame({
        "s": s,
        "s_deg": s * 180 / np.pi,
        "stimulus_shape": stimulus_shape,
        "post_write_memory": post_write_profile,
        "final_memory": final_profile,
        "chi_final": chi_final,
    })
    save_csv_local(profile_df, "B14_0_memory_profiles.csv")

    snapshot_df = pd.DataFrame(snapshots_arr)
    snapshot_df.insert(0, "t", snapshot_times)
    save_csv_local(snapshot_df, "B14_0_memory_snapshots_matrix.csv")

    save_json_local(summary, "B14_0_boundary_memory_summary.json")

    # --------------------------------------------------------
    # Figures
    # --------------------------------------------------------

    # Figure 1: heatmap of memory over time
    plt.figure(figsize=(9.0, 5.0))
    plt.imshow(
        snapshots_arr,
        aspect="auto",
        origin="lower",
        extent=[0, 360, snapshot_times[0], snapshot_times[-1]],
    )
    plt.colorbar(label="boundary memory m(s,t)")
    plt.xlabel("boundary coordinate s [deg]")
    plt.ylabel("time")
    plt.title("B14.0 boundary memory writing and decay")
    save_fig_local("B14_0_memory_heatmap.png")

    # Figure 2: memory norm and peak
    plt.figure(figsize=(8.0, 5.0))
    plt.plot(diagnostics_df["t"], diagnostics_df["L2_memory"], label="L2 memory")
    plt.plot(diagnostics_df["t"], diagnostics_df["peak_memory"], label="peak memory")
    plt.axvspan(write_t0, write_t1, alpha=0.15, label="writing interval")
    plt.xlabel("time")
    plt.ylabel("memory magnitude")
    plt.title("B14.0 memory magnitude over time")
    plt.legend()
    save_fig_local("B14_0_memory_norm_peak.png")

    # Figure 3: profiles
    plt.figure(figsize=(8.5, 5.0))
    plt.plot(s * 180 / np.pi, stimulus_shape, linestyle="--", label="initial stimulus shape")
    plt.plot(s * 180 / np.pi, post_write_profile, label="post-write memory")
    plt.plot(s * 180 / np.pi, final_profile, label="final memory")
    plt.xlabel("boundary coordinate s [deg]")
    plt.ylabel("profile value")
    plt.title("B14.0 boundary memory profiles")
    plt.legend()
    save_fig_local("B14_0_memory_profiles.png")

    # Figure 4: correlation with initial stimulus
    plt.figure(figsize=(8.0, 5.0))
    plt.plot(diagnostics_df["t"], diagnostics_df["corr_with_initial_stimulus"])
    plt.axvspan(write_t0, write_t1, alpha=0.15)
    plt.xlabel("time")
    plt.ylabel("correlation with initial stimulus")
    plt.title("B14.0 memory identity persistence")
    save_fig_local("B14_0_memory_correlation.png")

    # Figure 5: response map
    plt.figure(figsize=(8.5, 5.0))
    plt.plot(response_df["probe_center_deg"], response_df["response_with_memory"], label="response with memory")
    plt.plot(response_df["probe_center_deg"], response_df["response_baseline"], linestyle="--", label="baseline response")
    plt.plot(response_df["probe_center_deg"], response_df["response_gain"], label="response gain")
    plt.axvline(stimulus_center * 180 / np.pi, linestyle=":", label="trained location")
    plt.axvline(opposite_q * 180 / np.pi, linestyle=":", label="opposite location")
    plt.xlabel("probe center [deg]")
    plt.ylabel("response")
    plt.title("B14.0 history-dependent boundary response")
    plt.legend()
    save_fig_local("B14_0_history_dependent_response.png")

    # Figure 6: final chi field
    plt.figure(figsize=(8.5, 5.0))
    plt.plot(s * 180 / np.pi, chi_final, label="chi(s)=chi0+lambda_m*m(s)")
    plt.axvline(stimulus_center * 180 / np.pi, linestyle=":", label="trained location")
    plt.xlabel("boundary coordinate s [deg]")
    plt.ylabel("susceptibility chi")
    plt.title("B14.0 memory-modulated boundary susceptibility")
    plt.legend()
    save_fig_local("B14_0_memory_modulated_susceptibility.png")

    print("B14.0 complete.")
    print(json.dumps(summary, indent=2))

    return diagnostics_df, response_df, profile_df, snapshot_df, summary
