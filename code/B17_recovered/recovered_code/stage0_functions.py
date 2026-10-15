def simulate_repeated_boundary_response(
    condition_name="memory_feedback",
    alpha=0.015,
    etaS=8.0,
    memory_write=True,
    feedback=True,
    N=384,
    L=8.0,
    dt=0.002,
    T_pre=10.0,
    T_main=42.0,
    D0=0.12,
    epsD=0.010,
    phi_c=0.10,
    gamma0=0.0004,
    mu0=0.11,
    base_amp=0.20,
    base_width=0.65,
    stim_width=0.28,
    stim_offset=-0.05,
    phi_thr=0.030,
    phi_width=0.025,
    beta=3.0,
    Dm=0.006,
    pulse_start=2.0,
    pulse_duration=2.0,
    pulse_gap=4.0,
    pulse_amps=None,
    adaptive_site_mode="initial_boundary",
    max_clip=2.0,
    record_every=25,
):
    if pulse_amps is None:
        # up-ramp then down-ramp. This is useful for hysteresis diagnostics.
        pulse_amps = [0.015, 0.025, 0.035, 0.045, 0.045, 0.035, 0.025, 0.015]

    pulse_amps = list(pulse_amps)
    n_pulses = len(pulse_amps)

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

    def div_flux(phi_local):
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

        idx = int(np.where(above)[0][0])
        if idx <= 0:
            return float(x[idx])
        x0, x1 = x[idx - 1], x[idx]
        y0, y1 = phi_local[idx - 1], phi_local[idx]
        if abs(y1 - y0) <= 1e-15:
            return float(x1)
        return float(x0 + (phi_thr - y0) * (x1 - x0) / (y1 - y0))

    # Pre-equilibrate the base free boundary.
    for _ in range(int(T_pre / dt)):
        phi = phi + dt * (div_flux(phi) - mu0 * phi + base_source)
        phi = np.clip(phi, 0.0, max_clip)

    R_initial = boundary_location(phi, side="right")
    x_stim = R_initial + stim_offset

    stim_profile = np.exp(-0.5 * ((x - x_stim) / stim_width) ** 2)
    stim_profile = stim_profile / (np.max(stim_profile) + 1e-15)

    def pulse_index_and_amp(t):
        for i, amp in enumerate(pulse_amps):
            s = pulse_start + i * (pulse_duration + pulse_gap)
            e = s + pulse_duration
            if s <= t <= e:
                return i, amp
        return None, 0.0

    rows = []

    for n in range(int(T_main / dt) + 1):
        t = n * dt
        pidx, amp = pulse_index_and_amp(t)
        pulse_on = pidx is not None

        if n % record_every == 0 or n == int(T_main / dt):
            R_right = boundary_location(phi, side="right")
            rows.append({
                "condition": condition_name,
                "t": float(t),
                "pulse_index": -1 if pidx is None else int(pidx),
                "pulse_amp": float(amp),
                "pulse_on": bool(pulse_on),
                "R_right": float(R_right),
                "R_left": float(boundary_location(phi, side="left")),
                "x_stim": float(x_stim),
                "y_stim_from_R": float(x_stim - R_right),
                "phi_at_stim": float(np.sum(phi * stim_profile) / (np.sum(stim_profile) + 1e-15)),
                "m_at_stim": float(np.sum(m * stim_profile) / (np.sum(stim_profile) + 1e-15)),
                "m_max": float(np.max(m)),
                "m_total": float(np.trapz(np.maximum(m, 0.0), x)),
                "alpha": float(alpha),
                "etaS": float(etaS),
                "memory_write": bool(memory_write),
                "feedback": bool(feedback),
            })

        dphi = grad(phi)
        grad_abs = np.abs(dphi)
        boundary_mask = np.exp(-0.5 * ((phi - phi_thr) / phi_width) ** 2)

        if np.max(grad_abs) > 1e-15:
            boundary_mask = boundary_mask * grad_abs / (np.max(grad_abs) + 1e-15)

        if pulse_on and memory_write:
            write = beta * boundary_mask * stim_profile
        else:
            write = 0.0

        m = m + dt * (-alpha * m + write + Dm * lap(m))
        m = np.clip(m, 0.0, 20.0)

        ext_source = amp * stim_profile

        if feedback:
            source_eff = base_source + ext_source * (1.0 + etaS * m)
        else:
            source_eff = base_source + ext_source

        phi = phi + dt * (div_flux(phi) - mu0 * phi + source_eff)
        phi = np.clip(phi, 0.0, max_clip)

    traj = pd.DataFrame(rows)

    pulse_rows = []
    for i, amp in enumerate(pulse_amps):
        s = pulse_start + i * (pulse_duration + pulse_gap)
        e = s + pulse_duration
        before = traj[(traj["t"] >= s - 0.4) & (traj["t"] < s)]
        during = traj[(traj["t"] >= s) & (traj["t"] <= e)]
        after = traj[(traj["t"] > e) & (traj["t"] <= e + 1.0)]

        if len(before) == 0 or len(during) == 0:
            continue

        phi_before = float(before["phi_at_stim"].mean())
        phi_peak = float(during["phi_at_stim"].max())
        R_before = float(before["R_right"].mean())
        R_peak = float(during["R_right"].max())
        m_before = float(before["m_at_stim"].mean())

        pulse_rows.append({
            "condition": condition_name,
            "pulse_index": int(i),
            "phase": "up" if i < len(pulse_amps)/2 else "down",
            "pulse_amp": float(amp),
            "pulse_start": float(s),
            "pulse_end": float(e),
            "phi_before": phi_before,
            "phi_peak": phi_peak,
            "phi_increment": float(phi_peak - phi_before),
            "R_before": R_before,
            "R_peak": R_peak,
            "R_increment": float(R_peak - R_before),
            "m_before": m_before,
            "m_after": float(after["m_at_stim"].mean()) if len(after) else np.nan,
            "effective_load_before": float(etaS * m_before if feedback else 0.0),
            "alpha": float(alpha),
            "etaS": float(etaS),
            "memory_write": bool(memory_write),
            "feedback": bool(feedback),
        })

    pulse_df = pd.DataFrame(pulse_rows)

    # Hysteresis metric:
    # Compare up and down responses at the same nominal amplitude.
    hyst_rows = []
    for amp in sorted(set(pulse_amps)):
        sub = pulse_df[pulse_df["pulse_amp"] == amp]
        up = sub[sub["phase"] == "up"]
        down = sub[sub["phase"] == "down"]
        if len(up) and len(down):
            hyst_rows.append({
                "condition": condition_name,
                "pulse_amp": float(amp),
                "up_phi_increment": float(up["phi_increment"].mean()),
                "down_phi_increment": float(down["phi_increment"].mean()),
                "hysteresis_phi_delta": float(down["phi_increment"].mean() - up["phi_increment"].mean()),
                "up_R_increment": float(up["R_increment"].mean()),
                "down_R_increment": float(down["R_increment"].mean()),
                "hysteresis_R_delta": float(down["R_increment"].mean() - up["R_increment"].mean()),
                "up_m_before": float(up["m_before"].mean()),
                "down_m_before": float(down["m_before"].mean()),
                "history_accumulation_delta": float(down["m_before"].mean() - up["m_before"].mean()),
            })

    hyst_df = pd.DataFrame(hyst_rows)

    summary = {
        "condition": condition_name,
        "alpha": float(alpha),
        "etaS": float(etaS),
        "memory_write": bool(memory_write),
        "feedback": bool(feedback),
        "R_initial": float(R_initial),
        "x_stim": float(x_stim),
        "final_R_right": float(traj.iloc[-1]["R_right"]),
        "final_m_at_stim": float(traj.iloc[-1]["m_at_stim"]),
        "final_phi_at_stim": float(traj.iloc[-1]["phi_at_stim"]),
        "mean_phi_increment": float(pulse_df["phi_increment"].mean()) if len(pulse_df) else np.nan,
        "last_over_first_phi_increment": float(
            pulse_df.iloc[-1]["phi_increment"] / (pulse_df.iloc[0]["phi_increment"] + 1e-15)
        ) if len(pulse_df) else np.nan,
        "max_hysteresis_phi_delta": float(np.max(np.abs(hyst_df["hysteresis_phi_delta"]))) if len(hyst_df) else 0.0,
        "mean_hysteresis_phi_delta": float(hyst_df["hysteresis_phi_delta"].mean()) if len(hyst_df) else 0.0,
    }

    return traj, pulse_df, hyst_df, summary
