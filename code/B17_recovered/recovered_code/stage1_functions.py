def make_pde_helpers(x, dx, D0, epsD, phi_c, gamma0, phi_thr):
    N = len(x)

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

    return lap, grad, div_flux, boundary_location

def simulate_write_phase(
    alpha=0.015,
    n_write_pulses=3,
    rest_delay=6.0,
    N=384,
    L=8.0,
    dt=0.002,
    T_pre=10.0,
    D0=0.12,
    epsD=0.010,
    phi_c=0.10,
    gamma0=0.0004,
    mu0=0.11,
    base_amp=0.20,
    base_width=0.65,
    write_amp=0.030,
    write_width=0.28,
    stim_offset=-0.05,
    phi_thr=0.030,
    phi_width=0.025,
    beta=3.0,
    Dm=0.006,
    pulse_duration=1.5,
    pulse_gap=3.0,
    max_clip=2.0,
    record_every=25,
):
    x = np.linspace(-L, L, N)
    dx = float(x[1] - x[0])

    phi = np.zeros(N, dtype=float)
    m = np.zeros(N, dtype=float)

    base_source = base_amp * np.exp(-0.5 * (x / base_width) ** 2)

    lap, grad, div_flux, boundary_location = make_pde_helpers(
        x=x,
        dx=dx,
        D0=D0,
        epsD=epsD,
        phi_c=phi_c,
        gamma0=gamma0,
        phi_thr=phi_thr,
    )

    # Pre-equilibrate the base free boundary.
    for _ in range(int(T_pre / dt)):
        phi = phi + dt * (div_flux(phi) - mu0 * phi + base_source)
        phi = np.clip(phi, 0.0, max_clip)

    R_initial = boundary_location(phi, side="right")
    x_write = R_initial + stim_offset

    write_profile = np.exp(-0.5 * ((x - x_write) / write_width) ** 2)
    write_profile = write_profile / (np.max(write_profile) + 1e-15)

    write_total_duration = n_write_pulses * pulse_duration + (n_write_pulses - 1) * pulse_gap
    T_write_end = write_total_duration
    T_total = T_write_end + rest_delay

    def write_pulse_on(t):
        for i in range(n_write_pulses):
            s = i * (pulse_duration + pulse_gap)
            e = s + pulse_duration
            if s <= t <= e:
                return i, True
        return -1, False

    rows = []
    n_steps = int(T_total / dt)

    for n in range(n_steps + 1):
        t = n * dt
        pulse_index, pulse_on = write_pulse_on(t)
        amp = write_amp if pulse_on else 0.0

        if n % record_every == 0 or n == n_steps:
            R_right = boundary_location(phi, side="right")
            rows.append({
                "t": float(t),
                "phase": "write" if t <= T_write_end else "rest",
                "pulse_index": int(pulse_index),
                "pulse_on": bool(pulse_on),
                "write_amp": float(amp),
                "R_right": float(R_right),
                "R_left": float(boundary_location(phi, side="left")),
                "x_write": float(x_write),
                "y_write_from_R": float(x_write - R_right),
                "phi_at_write": float(np.sum(phi * write_profile) / (np.sum(write_profile) + 1e-15)),
                "m_at_write": float(np.sum(m * write_profile) / (np.sum(write_profile) + 1e-15)),
                "m_max": float(np.max(m)),
                "m_total": float(np.trapz(np.maximum(m, 0.0), x)),
                "alpha": float(alpha),
                "n_write_pulses": int(n_write_pulses),
                "rest_delay": float(rest_delay),
            })

        dphi = grad(phi)
        grad_abs = np.abs(dphi)
        boundary_mask = np.exp(-0.5 * ((phi - phi_thr) / phi_width) ** 2)

        if np.max(grad_abs) > 1e-15:
            boundary_mask = boundary_mask * grad_abs / (np.max(grad_abs) + 1e-15)

        # Write phase:
        # The pulse can affect phi and write m, but feedback from m to source is OFF.
        write = beta * boundary_mask * write_profile if pulse_on else 0.0
        m = m + dt * (-alpha * m + write + Dm * lap(m))
        m = np.clip(m, 0.0, 20.0)

        source = base_source + amp * write_profile
        phi = phi + dt * (div_flux(phi) - mu0 * phi + source)
        phi = np.clip(phi, 0.0, max_clip)

    trajectory = pd.DataFrame(rows)

    R_read = boundary_location(phi, side="right")
    y = x - R_read

    m_total = float(np.trapz(np.maximum(m, 0.0), x))
    if m_total > 1e-15:
        x_m_center = float(np.trapz(x * np.maximum(m, 0.0), x) / m_total)
        y_m_center = float(x_m_center - R_read)
    else:
        x_m_center = np.nan
        y_m_center = np.nan

    m_peak_idx = int(np.argmax(m))
    x_m_peak = float(x[m_peak_idx])
    y_m_peak = float(y[m_peak_idx])

    state = {
        "x": x,
        "dx": dx,
        "phi": phi.copy(),
        "m": m.copy(),
        "base_source": base_source,
        "write_profile": write_profile,
        "x_write": float(x_write),
        "R_initial": float(R_initial),
        "R_read": float(R_read),
        "x_m_peak": float(x_m_peak),
        "y_m_peak": float(y_m_peak),
        "x_m_center": float(x_m_center),
        "y_m_center": float(y_m_center),
        "m_peak": float(np.max(m)),
        "m_total": float(m_total),
        "trajectory": trajectory,
        "params": {
            "alpha": alpha,
            "n_write_pulses": n_write_pulses,
            "rest_delay": rest_delay,
            "N": N,
            "L": L,
            "dt": dt,
            "T_pre": T_pre,
            "D0": D0,
            "epsD": epsD,
            "phi_c": phi_c,
            "gamma0": gamma0,
            "mu0": mu0,
            "base_amp": base_amp,
            "base_width": base_width,
            "write_amp": write_amp,
            "write_width": write_width,
            "stim_offset": stim_offset,
            "phi_thr": phi_thr,
            "phi_width": phi_width,
            "beta": beta,
            "Dm": Dm,
            "pulse_duration": pulse_duration,
            "pulse_gap": pulse_gap,
        },
        "helpers": {
            "lap": lap,
            "grad": grad,
            "div_flux": div_flux,
            "boundary_location": boundary_location,
        },
    }

    return state

def run_read_branch(
    state,
    branch_name="kept_feedback",
    erase_memory=False,
    feedback=True,
    read_amp=0.025,
    read_width=0.28,
    read_duration=2.0,
    read_follow=3.0,
    etaS=8.0,
    etaMu=0.0,
    write_during_read=False,
    beta=3.0,
    phi_thr=0.030,
    phi_width=0.025,
    Dm=0.006,
    alpha=None,
    dt=None,
    max_clip=2.0,
    record_every=25,
):
    x = state["x"]
    phi = state["phi"].copy()
    m = state["m"].copy()

    if erase_memory:
        m[:] = 0.0

    if alpha is None:
        alpha = state["params"]["alpha"]

    if dt is None:
        dt = state["params"]["dt"]

    mu0 = state["params"]["mu0"]
    base_source = state["base_source"]

    # Read at the same nominal write/probe site.
    x_read = state["x_write"]

    read_profile = np.exp(-0.5 * ((x - x_read) / read_width) ** 2)
    read_profile = read_profile / (np.max(read_profile) + 1e-15)

    lap = state["helpers"]["lap"]
    grad = state["helpers"]["grad"]
    div_flux = state["helpers"]["div_flux"]
    boundary_location = state["helpers"]["boundary_location"]

    probe_index = int(np.argmin(np.abs(x - x_read)))

    rows = []
    T_total = read_duration + read_follow
    n_steps = int(T_total / dt)

    for n in range(n_steps + 1):
        t = n * dt
        pulse_on = t <= read_duration
        amp = read_amp if pulse_on else 0.0

        if n % record_every == 0 or n == n_steps:
            R_now = boundary_location(phi, side="right")
            rows.append({
                "branch": branch_name,
                "t_read": float(t),
                "read_pulse_on": bool(pulse_on),
                "R_right": float(R_now),
                "R_left": float(boundary_location(phi, side="left")),
                "x_read": float(x_read),
                "y_read_from_R": float(x_read - R_now),
                "phi_at_read": float(np.sum(phi * read_profile) / (np.sum(read_profile) + 1e-15)),
                "phi_point_read": float(phi[probe_index]),
                "m_at_read": float(np.sum(m * read_profile) / (np.sum(read_profile) + 1e-15)),
                "m_max": float(np.max(m)),
                "m_total": float(np.trapz(np.maximum(m, 0.0), x)),
                "erase_memory": bool(erase_memory),
                "feedback": bool(feedback),
                "etaS": float(etaS),
            })

        dphi = grad(phi)
        grad_abs = np.abs(dphi)
        boundary_mask = np.exp(-0.5 * ((phi - phi_thr) / phi_width) ** 2)

        if np.max(grad_abs) > 1e-15:
            boundary_mask = boundary_mask * grad_abs / (np.max(grad_abs) + 1e-15)

        if pulse_on and write_during_read:
            write = beta * boundary_mask * read_profile
        else:
            write = 0.0

        m = m + dt * (-alpha * m + write + Dm * lap(m))
        m = np.clip(m, 0.0, 20.0)

        ext_source = amp * read_profile

        if feedback:
            source_eff = base_source + ext_source * (1.0 + etaS * m)
        else:
            source_eff = base_source + ext_source

        mu_eff = mu0 / (1.0 + etaMu * m)

        phi = phi + dt * (div_flux(phi) - mu_eff * phi + source_eff)
        phi = np.clip(phi, 0.0, max_clip)

    traj = pd.DataFrame(rows)

    before = traj[(traj["t_read"] >= 0.0) & (traj["t_read"] <= 0.2)]
    during = traj[(traj["t_read"] >= 0.0) & (traj["t_read"] <= read_duration)]

    phi_before = float(before["phi_at_read"].mean())
    phi_peak = float(during["phi_at_read"].max())
    R_before = float(before["R_right"].mean())
    R_peak = float(during["R_right"].max())

    metrics = {
        "branch": branch_name,
        "erase_memory": bool(erase_memory),
        "feedback": bool(feedback),
        "etaS": float(etaS),
        "read_amp": float(read_amp),
        "x_read": float(x_read),
        "R_read_branch": float(state["R_read"]),
        "y_read_branch": float(x_read - state["R_read"]),
        "retained_m_at_read_start": float(traj.iloc[0]["m_at_read"]),
        "effective_feedback_load_start": float(etaS * traj.iloc[0]["m_at_read"] if feedback else 0.0),
        "phi_before_read": phi_before,
        "phi_peak_read": phi_peak,
        "phi_increment_read": float(phi_peak - phi_before),
        "R_before_read": R_before,
        "R_peak_read": R_peak,
        "R_increment_read": float(R_peak - R_before),
        "final_phi_at_read": float(traj.iloc[-1]["phi_at_read"]),
        "final_m_at_read": float(traj.iloc[-1]["m_at_read"]),
    }

    return traj, metrics

def linear_fit(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    if len(x) < 2 or np.std(x) <= 1e-15:
        return np.nan, np.nan, np.nan, np.nan

    A = np.vstack([x, np.ones_like(x)]).T
    slope, intercept = np.linalg.lstsq(A, y, rcond=None)[0]
    yhat = slope * x + intercept
    ss_res = float(np.sum((y - yhat) ** 2))
    ss_tot = float(np.sum((y - np.mean(y)) ** 2))
    r2 = 1.0 - ss_res / (ss_tot + 1e-15)
    corr = float(np.corrcoef(x, y)[0, 1])

    return float(slope), float(intercept), float(r2), float(corr)
