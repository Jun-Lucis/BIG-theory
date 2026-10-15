def run_b16_memory_free_boundary(
    scenario_name="memory_feedback",
    N=384,
    L=8.0,
    dt=0.002,
    T_pre=10.0,
    T_main=26.0,
    D0=0.12,
    epsD=0.010,
    phi_c=0.10,
    gamma0=0.0004,
    mu0=0.11,
    base_amp=0.20,
    base_width=0.65,
    stim_amp_1=0.040,
    stim_amp_2=0.025,
    stim_width=0.28,
    stim_offset=-0.05,
    phi_thr=0.030,
    phi_width=0.025,
    alpha=0.015,
    beta=3.0,
    Dm=0.006,
    etaS=8.0,
    etaMu=0.50,
    memory_enabled=True,
    feedback_enabled=True,
    probe_side="right",
    record_every=25,
    store_profile_times=(0.0, 2.0, 5.0, 16.0, 19.0, 26.0),
    seed=1601,
):
    """
    Reduced 1D model for BIG-B16.

    The field phi forms a threshold-defined free boundary.
    Boundary history m is written near the active boundary during a pulse.
    If feedback_enabled=True, m changes later source susceptibility and decay.

    Returns:
        trajectory_df
        profile_df
        metrics
        params
    """

    rng = np.random.default_rng(seed)

    x = np.linspace(-L, L, N)
    dx = float(x[1] - x[0])

    phi = np.zeros(N, dtype=float)
    m = np.zeros(N, dtype=float)

    base_source = base_amp * np.exp(-0.5 * (x / base_width) ** 2)

    def lap(u):
        out = np.zeros_like(u)
        out[1:-1] = (u[2:] - 2.0 * u[1:-1] + u[:-2]) / (dx * dx)
        out[0] = (u[1] - u[0]) / (dx * dx)
        out[-1] = (u[-2] - u[-1]) / (dx * dx)
        return out

    def grad(u):
        out = np.zeros_like(u)
        out[1:-1] = (u[2:] - u[:-2]) / (2.0 * dx)
        out[0] = (u[1] - u[0]) / dx
        out[-1] = (u[-1] - u[-2]) / dx
        return out

    def div_flux(phi_local, m_local):
        dphi_edge = (phi_local[1:] - phi_local[:-1]) / dx
        phi_edge = 0.5 * (phi_local[1:] + phi_local[:-1])

        mobility = D0 * (
            phi_edge * phi_edge / (phi_edge * phi_edge + phi_c * phi_c)
            + epsD
        )

        flux = mobility * dphi_edge + gamma0 * (dphi_edge ** 3)

        out = np.zeros_like(phi_local)
        out[1:-1] = (flux[1:] - flux[:-1]) / dx
        out[0] = flux[0] / dx
        out[-1] = -flux[-1] / dx

        return out

    def boundary_location(phi_local, side="right"):
        above = phi_local > phi_thr

        if not np.any(above):
            return np.nan

        if side == "right":
            idx = int(np.where(above)[0][-1])

            if idx >= N - 1:
                return float(x[idx])

            x0, x1 = x[idx], x[idx + 1]
            y0, y1 = phi_local[idx], phi_local[idx + 1]

            if abs(y1 - y0) <= 1e-15:
                return float(x0)

            return float(x0 + (phi_thr - y0) * (x1 - x0) / (y1 - y0))

        else:
            idx = int(np.where(above)[0][0])

            if idx <= 0:
                return float(x[idx])

            x0, x1 = x[idx - 1], x[idx]
            y0, y1 = phi_local[idx - 1], phi_local[idx]

            if abs(y1 - y0) <= 1e-15:
                return float(x1)

            return float(x0 + (phi_thr - y0) * (x1 - x0) / (y1 - y0))

    def record_profile(profile_rows, t_abs, label, phi_local, m_local, stim_profile):
        for xi, phii, mi, si in zip(x, phi_local, m_local, stim_profile):
            profile_rows.append({
                "scenario": scenario_name,
                "t": float(t_abs),
                "label": label,
                "x": float(xi),
                "phi": float(phii),
                "m": float(mi),
                "stim_profile": float(si),
            })

    # --------------------------------------------------------
    # Pre-equilibrate a compact-like free boundary from base source
    # --------------------------------------------------------

    steps_pre = int(T_pre / dt)

    for _ in range(steps_pre):
        phi = phi + dt * (div_flux(phi, m) - mu0 * phi + base_source)
        phi = np.clip(phi, 0.0, 2.0)

    R0 = boundary_location(phi, side="right")
    L0 = boundary_location(phi, side="left")

    if probe_side == "right":
        x_stim = R0 + stim_offset
    else:
        x_stim = L0 - stim_offset

    stim_profile = np.exp(-0.5 * ((x - x_stim) / stim_width) ** 2)
    stim_profile = stim_profile / (np.max(stim_profile) + 1e-15)

    pulse1 = (2.0, 5.0)
    pulse2 = (16.0, 19.0)

    trajectory_rows = []
    profile_rows = []

    profile_time_targets = list(store_profile_times)
    profile_time_done = set()

    steps_main = int(T_main / dt)

    for n in range(steps_main + 1):
        t_main = n * dt
        t_abs = T_pre + t_main

        amp = 0.0
        if pulse1[0] <= t_main <= pulse1[1]:
            amp = stim_amp_1
        if pulse2[0] <= t_main <= pulse2[1]:
            amp = stim_amp_2

        pulse_on = amp > 0.0

        if n % record_every == 0 or n == steps_main:
            R = boundary_location(phi, side="right")
            Lb = boundary_location(phi, side="left")
            phi_at_stim = float(phi[int(np.argmin(np.abs(x - x_stim)))])
            m_at_stim = float(np.sum(m * stim_profile) / (np.sum(stim_profile) + 1e-15))

            trajectory_rows.append({
                "scenario": scenario_name,
                "t": float(t_abs),
                "t_main": float(t_main),
                "R_right": float(R),
                "R_left": float(Lb),
                "width": float(R - Lb) if np.isfinite(R) and np.isfinite(Lb) else np.nan,
                "phi_max": float(np.max(phi)),
                "phi_at_stim": phi_at_stim,
                "m_max": float(np.max(m)),
                "m_at_stim": m_at_stim,
                "pulse_on": bool(pulse_on),
                "x_stim": float(x_stim),
            })

        for target in profile_time_targets:
            if target not in profile_time_done and abs(t_main - target) <= 0.5 * dt:
                record_profile(
                    profile_rows,
                    t_abs,
                    f"tmain_{target:.1f}",
                    phi,
                    m,
                    stim_profile,
                )
                profile_time_done.add(target)

        dphi = grad(phi)
        grad_abs = np.abs(dphi)

        boundary_mask = np.exp(-0.5 * ((phi - phi_thr) / phi_width) ** 2)

        if np.max(grad_abs) > 1e-15:
            boundary_mask = boundary_mask * grad_abs / (np.max(grad_abs) + 1e-15)

        if pulse_on and memory_enabled:
            write = beta * boundary_mask * stim_profile
        else:
            write = 0.0

        m = m + dt * (-alpha * m + write + Dm * lap(m))
        m = np.clip(m, 0.0, 20.0)

        ext_source = amp * stim_profile

        if feedback_enabled:
            S_eff = base_source + ext_source * (1.0 + etaS * m)
            mu_eff = mu0 / (1.0 + etaMu * m)
        else:
            S_eff = base_source + ext_source
            mu_eff = mu0

        phi = phi + dt * (div_flux(phi, m) - mu_eff * phi + S_eff)
        phi = np.clip(phi, 0.0, 2.0)

        if not memory_enabled:
            m[:] = 0.0

    # Ensure final profile recorded
    record_profile(profile_rows, T_pre + T_main, "final", phi, m, stim_profile)

    trajectory_df = pd.DataFrame(trajectory_rows)
    profile_df = pd.DataFrame(profile_rows)

    def mean_window(a, b, col):
        sub = trajectory_df[
            (trajectory_df["t_main"] >= a)
            & (trajectory_df["t_main"] <= b)
        ]

        if len(sub) == 0:
            return np.nan

        return float(sub[col].mean())

    def max_window(a, b, col):
        sub = trajectory_df[
            (trajectory_df["t_main"] >= a)
            & (trajectory_df["t_main"] <= b)
        ]

        if len(sub) == 0:
            return np.nan

        return float(sub[col].max())

    R_before1 = mean_window(1.5, 2.0, "R_right")
    R_max1 = max_window(pulse1[0], pulse1[1], "R_right")
    R_before2 = mean_window(15.5, 16.0, "R_right")
    R_max2 = max_window(pulse2[0], pulse2[1], "R_right")
    R_after_relax = mean_window(23.0, 26.0, "R_right")

    phi_stim_before2 = mean_window(15.5, 16.0, "phi_at_stim")
    phi_stim_max2 = max_window(pulse2[0], pulse2[1], "phi_at_stim")

    metrics = {
        "scenario": scenario_name,
        "R0_pre": float(R0),
        "L0_pre": float(L0),
        "x_stim": float(x_stim),
        "R_before_pulse1": R_before1,
        "R_max_pulse1": R_max1,
        "R_expansion_pulse1": float(R_max1 - R_before1),
        "R_before_pulse2": R_before2,
        "R_max_pulse2": R_max2,
        "R_expansion_pulse2": float(R_max2 - R_before2),
        "R_after_final_relax": R_after_relax,
        "persistent_boundary_offset": float(R_before2 - R_before1),
        "m_at_stim_before_pulse2": mean_window(15.5, 16.0, "m_at_stim"),
        "m_max_before_pulse2": mean_window(15.5, 16.0, "m_max"),
        "phi_at_stim_before_pulse2": phi_stim_before2,
        "phi_at_stim_max_pulse2": phi_stim_max2,
        "phi_probe_increment_pulse2": float(phi_stim_max2 - phi_stim_before2),
        "final_m_at_stim": float(trajectory_df.iloc[-1]["m_at_stim"]),
    }

    params = {
        "scenario": scenario_name,
        "N": N,
        "L": L,
        "dt": dt,
        "T_pre": T_pre,
        "T_main": T_main,
        "D0": D0,
        "epsD": epsD,
        "phi_c": phi_c,
        "gamma0": gamma0,
        "mu0": mu0,
        "base_amp": base_amp,
        "base_width": base_width,
        "stim_amp_1": stim_amp_1,
        "stim_amp_2": stim_amp_2,
        "stim_width": stim_width,
        "stim_offset": stim_offset,
        "phi_thr": phi_thr,
        "phi_width": phi_width,
        "alpha": alpha,
        "beta": beta,
        "Dm": Dm,
        "etaS": etaS,
        "etaMu": etaMu,
        "memory_enabled": memory_enabled,
        "feedback_enabled": feedback_enabled,
        "probe_side": probe_side,
        "pulse1": pulse1,
        "pulse2": pulse2,
    }

    return trajectory_df, profile_df, metrics, params
