def make_basic_helpers(x, dx, D0, epsD, phi_c, gamma0, phi_thr):
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

def create_prehistory_state(
    alpha=0.015,
    N=384,
    L=8.0,
    dt=0.002,
    T_pre=10.0,
    t_probe_start=16.0,
    D0=0.12,
    epsD=0.010,
    phi_c=0.10,
    gamma0=0.0004,
    mu0=0.11,
    base_amp=0.20,
    base_width=0.65,
    stim_amp_1=0.040,
    stim_width=0.28,
    stim_offset=-0.05,
    phi_thr=0.030,
    phi_width=0.025,
    beta=3.0,
    Dm=0.006,
):
    x = np.linspace(-L, L, N)
    dx = float(x[1] - x[0])

    phi = np.zeros(N, dtype=float)
    m = np.zeros(N, dtype=float)

    base_source = base_amp * np.exp(-0.5 * (x / base_width) ** 2)

    lap, grad, div_flux, boundary_location = make_basic_helpers(
        x=x,
        dx=dx,
        D0=D0,
        epsD=epsD,
        phi_c=phi_c,
        gamma0=gamma0,
        phi_thr=phi_thr,
    )

    # Pre-equilibrate a base free boundary.
    steps_pre = int(T_pre / dt)

    for _ in range(steps_pre):
        phi = phi + dt * (div_flux(phi) - mu0 * phi + base_source)
        phi = np.clip(phi, 0.0, 2.0)

    R_initial = boundary_location(phi, side="right")
    L_initial = boundary_location(phi, side="left")

    # Nominal first memory-writing coordinate.
    x_memory = R_initial + stim_offset

    stim_profile_1 = np.exp(-0.5 * ((x - x_memory) / stim_width) ** 2)
    stim_profile_1 = stim_profile_1 / (np.max(stim_profile_1) + 1e-15)

    # Prehistory phase:
    # pulse 1 writes m; feedback remains OFF before pulse 2.
    steps_main = int(t_probe_start / dt)

    for n in range(steps_main):
        t = n * dt
        amp1 = stim_amp_1 if (2.0 <= t <= 5.0) else 0.0
        pulse_on = amp1 > 0.0

        dphi = grad(phi)
        grad_abs = np.abs(dphi)

        boundary_mask = np.exp(-0.5 * ((phi - phi_thr) / phi_width) ** 2)

        if np.max(grad_abs) > 1e-15:
            boundary_mask = boundary_mask * grad_abs / (np.max(grad_abs) + 1e-15)

        write = beta * boundary_mask * stim_profile_1 if pulse_on else 0.0

        m = m + dt * (-alpha * m + write + Dm * lap(m))
        m = np.clip(m, 0.0, 20.0)

        source = base_source + amp1 * stim_profile_1
        phi = phi + dt * (div_flux(phi) - mu0 * phi + source)
        phi = np.clip(phi, 0.0, 2.0)

    R_probe = boundary_location(phi, side="right")
    L_probe = boundary_location(phi, side="left")
    y = x - R_probe

    m_total = float(np.trapz(np.maximum(m, 0.0), x))
    if m_total > 1e-15:
        x_m_center = float(np.trapz(x * np.maximum(m, 0.0), x) / m_total)
        y_m_center = float(x_m_center - R_probe)
    else:
        x_m_center = np.nan
        y_m_center = np.nan

    m_peak_idx = int(np.argmax(m))
    x_m_peak = float(x[m_peak_idx])
    y_m_peak = float(y[m_peak_idx])

    state = {
        "x": x,
        "y": y,
        "dx": dx,
        "phi": phi.copy(),
        "m": m.copy(),
        "base_source": base_source,
        "stim_profile_1": stim_profile_1,
        "x_memory": float(x_memory),
        "R_initial": float(R_initial),
        "L_initial": float(L_initial),
        "R_probe": float(R_probe),
        "L_probe": float(L_probe),
        "x_m_peak": x_m_peak,
        "y_m_peak": y_m_peak,
        "x_m_center": x_m_center,
        "y_m_center": y_m_center,
        "m_peak": float(np.max(m)),
        "m_total": m_total,
        "params": {
            "alpha": alpha,
            "N": N,
            "L": L,
            "dt": dt,
            "T_pre": T_pre,
            "t_probe_start": t_probe_start,
            "D0": D0,
            "epsD": epsD,
            "phi_c": phi_c,
            "gamma0": gamma0,
            "mu0": mu0,
            "base_amp": base_amp,
            "base_width": base_width,
            "stim_amp_1": stim_amp_1,
            "stim_width": stim_width,
            "stim_offset": stim_offset,
            "phi_thr": phi_thr,
            "phi_width": phi_width,
            "beta": beta,
            "Dm": Dm,
        },
        "helpers": {
            "lap": lap,
            "grad": grad,
            "div_flux": div_flux,
            "boundary_location": boundary_location,
        },
    }

    return state

def run_shifted_probe(
    state,
    alpha=0.015,
    etaS=10.0,
    shift=0.0,
    erase_memory=False,
    branch_name="kept",
    dt=0.002,
    t_probe_start=16.0,
    t_probe_end=22.0,
    stim_amp_2=0.025,
    stim_width_2=0.28,
    phi_thr=0.030,
    Dm=0.006,
    etaMu=0.0,
    write_second_pulse=False,
    beta=3.0,
    phi_width=0.025,
    record_every=25,
):
    x = state["x"]
    phi = state["phi"].copy()
    m = state["m"].copy()

    if erase_memory:
        m[:] = 0.0

    base_source = state["base_source"]
    R_probe_branch = state["R_probe"]
    x_memory = state["x_memory"]
    x_probe = x_memory + shift
    y_probe = x_probe - R_probe_branch

    stim_profile_2 = np.exp(-0.5 * ((x - x_probe) / stim_width_2) ** 2)
    stim_profile_2 = stim_profile_2 / (np.max(stim_profile_2) + 1e-15)

    lap = state["helpers"]["lap"]
    grad = state["helpers"]["grad"]
    div_flux = state["helpers"]["div_flux"]
    boundary_location = state["helpers"]["boundary_location"]

    mu0 = state["params"]["mu0"]
    probe_index = int(np.argmin(np.abs(x - x_probe)))

    rows = []
    steps = int((t_probe_end - t_probe_start) / dt)

    for n in range(steps + 1):
        t_rel = n * dt
        t = t_probe_start + t_rel

        amp2 = stim_amp_2 if (t_probe_start <= t <= 19.0) else 0.0
        pulse_on = amp2 > 0.0

        R_now = boundary_location(phi, side="right")
        y_probe_now = x_probe - R_now

        if n % record_every == 0 or n == steps:
            rows.append({
                "branch": branch_name,
                "alpha": float(alpha),
                "etaS": float(etaS),
                "shift": float(shift),
                "erase_memory": bool(erase_memory),
                "t": float(t),
                "t_rel": float(t_rel),
                "R_right": float(R_now),
                "R_left": float(boundary_location(phi, side="left")),
                "x_memory": float(x_memory),
                "x_probe": float(x_probe),
                "y_probe_branch": float(y_probe),
                "y_probe_now": float(y_probe_now),
                "phi_at_probe": float(phi[probe_index]),
                "m_at_probe": float(np.sum(m * stim_profile_2) / (np.sum(stim_profile_2) + 1e-15)),
                "m_at_memory_site": float(np.sum(m * state["stim_profile_1"]) / (np.sum(state["stim_profile_1"]) + 1e-15)),
                "m_max": float(np.max(m)),
                "pulse_on": bool(pulse_on),
            })

        dphi = grad(phi)
        grad_abs = np.abs(dphi)
        boundary_mask = np.exp(-0.5 * ((phi - phi_thr) / phi_width) ** 2)

        if np.max(grad_abs) > 1e-15:
            boundary_mask = boundary_mask * grad_abs / (np.max(grad_abs) + 1e-15)

        if pulse_on and write_second_pulse:
            write = beta * boundary_mask * stim_profile_2
        else:
            write = 0.0

        m = m + dt * (-alpha * m + write + Dm * lap(m))
        m = np.clip(m, 0.0, 20.0)

        ext_source = amp2 * stim_profile_2
        source_eff = base_source + ext_source * (1.0 + etaS * m)
        mu_eff = mu0 / (1.0 + etaMu * m)

        phi = phi + dt * (div_flux(phi) - mu_eff * phi + source_eff)
        phi = np.clip(phi, 0.0, 2.0)

    traj = pd.DataFrame(rows)

    def mean_window(a, b, col):
        sub = traj[(traj["t"] >= a) & (traj["t"] <= b)]
        if len(sub) == 0:
            return np.nan
        return float(sub[col].mean())

    def max_window(a, b, col):
        sub = traj[(traj["t"] >= a) & (traj["t"] <= b)]
        if len(sub) == 0:
            return np.nan
        return float(sub[col].max())

    metrics = {
        "branch": branch_name,
        "alpha": float(alpha),
        "etaS": float(etaS),
        "shift": float(shift),
        "erase_memory": bool(erase_memory),
        "x_memory": float(x_memory),
        "x_probe": float(x_probe),
        "R_probe_branch": float(R_probe_branch),
        "y_memory_branch": float(x_memory - R_probe_branch),
        "y_probe_branch": float(y_probe),
        "x_m_peak": float(state["x_m_peak"]),
        "y_m_peak": float(state["y_m_peak"]),
        "x_m_center": float(state["x_m_center"]),
        "y_m_center": float(state["y_m_center"]),
        "retained_m_at_probe": float(traj.iloc[0]["m_at_probe"]),
        "retained_m_at_memory_site": float(traj.iloc[0]["m_at_memory_site"]),
        "effective_feedback_load": float(etaS * traj.iloc[0]["m_at_probe"]),
        "phi_before_probe": mean_window(16.0, 16.2, "phi_at_probe"),
        "phi_max_probe": max_window(16.0, 19.0, "phi_at_probe"),
        "phi_increment_probe": float(
            max_window(16.0, 19.0, "phi_at_probe")
            - mean_window(16.0, 16.2, "phi_at_probe")
        ),
        "R_before_probe": mean_window(16.0, 16.2, "R_right"),
        "R_max_probe": max_window(16.0, 19.0, "R_right"),
        "R_increment_probe": float(
            max_window(16.0, 19.0, "R_right")
            - mean_window(16.0, 16.2, "R_right")
        ),
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
