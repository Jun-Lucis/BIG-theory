PROTOCOLS = [
    "front_anchored_write",
    "lab_fixed_write",
]

DEFAULT = {
    # grid
    "N": 384,
    "L": 12.0,

    # time step
    "dt": 0.004,

    # reaction-diffusion front
    "Du": 0.045,
    "r": 1.0,
    "a": 0.28,
    "u_thr": 0.5,
    "u_clip_low": 0.0,
    "u_clip_high": 1.2,

    # initial front
    "R0": -3.0,
    "front_width_init": 0.28,

    # trace dynamics
    "Dm": 0.004,
    "beta": 1.15,
    "front_mask_width": 0.10,
    "m_clip_high": 10.0,

    # read/write geometry
    "y_write": 0.0,
    "y_read": 0.0,
    "write_width": 0.35,
    "read_width_default": 0.35,

    # stimuli
    "write_amp": 0.12,
    "read_amp": 0.10,

    # timing
    "T_pre": 3.0,
    "write_duration": 1.3,
    "inter_write_gap": 0.8,
    "read_duration": 3.2,
    "record_every": 25,
}

def make_grid(params=DEFAULT):
    N = int(params["N"])
    L = float(params["L"])
    x = np.linspace(-L, L, N)
    dx = float(x[1] - x[0])
    return x, dx

def sigmoid_front(x, R0, width):
    return 1.0 / (1.0 + np.exp((x - R0) / width))

def gaussian(x, center, width):
    w = np.exp(-0.5 * ((x - center) / width) ** 2)
    mx = np.max(w)
    if mx > 0:
        w = w / mx
    return w

def lap_neumann(u, dx):
    out = np.zeros_like(u)
    out[1:-1] = (u[2:] - 2.0 * u[1:-1] + u[:-2]) / (dx * dx)
    out[0] = (u[1] - u[0]) / (dx * dx)
    out[-1] = (u[-2] - u[-1]) / (dx * dx)
    return out

def grad_centered(u, dx):
    out = np.zeros_like(u)
    out[1:-1] = (u[2:] - u[:-2]) / (2.0 * dx)
    out[0] = (u[1] - u[0]) / dx
    out[-1] = (u[-1] - u[-2]) / dx
    return out

def front_location(x, u, u_thr=0.5):
    above = u >= u_thr
    if not np.any(above):
        return np.nan
    idx = int(np.where(above)[0][-1])
    if idx >= len(x) - 1:
        return float(x[idx])

    x0, x1 = x[idx], x[idx + 1]
    y0, y1 = u[idx], u[idx + 1]
    if abs(y1 - y0) <= 1e-15:
        return float(x0)
    return float(x0 + (u_thr - y0) * (x1 - x0) / (y1 - y0))

def weighted_sample(x, arr, center, width):
    w = gaussian(x, center, width)
    dx = float(x[1] - x[0])
    denom = float(np.sum(w) * dx)
    if denom <= 1e-15:
        return 0.0
    return float(np.sum(arr * w) * dx / denom)

def weighted_sample_with_profile(x, arr, profile):
    dx = float(x[1] - x[0])
    denom = float(np.sum(profile) * dx)
    if denom <= 1e-15:
        return 0.0
    return float(np.sum(arr * profile) * dx / denom)

def trace_moments(x, m, R):
    dx = float(x[1] - x[0])
    mp = np.maximum(m, 0.0)
    total = float(np.sum(mp) * dx)
    peak = float(np.max(mp))
    idx = int(np.argmax(mp))
    x_peak = float(x[idx])

    if total > 1e-15:
        x_center = float(np.sum(x * mp) * dx / total)
    else:
        x_center = np.nan

    return {
        "m_total": total,
        "m_peak": peak,
        "x_m_peak": x_peak,
        "y_m_peak_from_R": x_peak - R,
        "x_m_center": x_center,
        "y_m_center_from_R": x_center - R if np.isfinite(x_center) else np.nan,
    }

def front_mask(x, u, params):
    dx = float(x[1] - x[0])
    gu = np.abs(grad_centered(u, dx))
    layer = np.exp(-0.5 * ((u - params["u_thr"]) / params["front_mask_width"]) ** 2)
    mask = gu * layer
    mx = np.max(mask)
    if mx > 1e-15:
        mask = mask / mx
    return mask

def reaction_term(u, params):
    return params["r"] * u * (1.0 - u) * (u - params["a"])

def active_gate(u):
    return np.maximum(u * (1.0 - u), 0.0)

def rd_step(
    x,
    dx,
    u,
    m,
    params,
    read_profile=None,
    read_amp=0.0,
    kappa=0.0,
    inhibitor_on=False,
):
    if read_profile is None:
        read_profile = np.zeros_like(u)

    active = active_gate(u)
    drive = read_amp * read_profile * active

    if inhibitor_on:
        inhibition = kappa * m * active
    else:
        inhibition = 0.0

    du = (
        params["Du"] * lap_neumann(u, dx)
        + reaction_term(u, params)
        + drive
        - inhibition
    )

    u_new = u + params["dt"] * du
    u_new = np.clip(u_new, params["u_clip_low"], params["u_clip_high"])
    return u_new

def trace_step(
    x,
    dx,
    u,
    m,
    alpha,
    params,
    write_profile=None,
    write_on=False,
):
    if write_profile is None:
        write_profile = np.zeros_like(m)

    if write_on:
        write = params["beta"] * front_mask(x, u, params) * write_profile
    else:
        write = 0.0

    dm = (
        -alpha * m
        + params["Dm"] * lap_neumann(m, dx)
        + write
    )

    m_new = m + params["dt"] * dm
    m_new = np.clip(m_new, 0.0, params["m_clip_high"])
    return m_new

def compute_read_observables(x, u, m, R, read_width, kappa):
    xr = R
    W = gaussian(x, xr, read_width)
    A = active_gate(u)
    WA = W * A

    dx = float(x[1] - x[0])

    m_local = weighted_sample_with_profile(x, m, W)
    m_active = weighted_sample_with_profile(x, m, WA)

    raw_inhibitory_exposure = float(np.sum(kappa * m * WA) * dx)
    window_mass = float(np.sum(W) * dx)
    active_window_mass = float(np.sum(WA) * dx)

    return {
        "R": float(R),
        "x_read": float(xr),
        "m_local": float(m_local),
        "m_active": float(m_active),
        "raw_inhibitory_exposure": raw_inhibitory_exposure,
        "window_mass": window_mass,
        "active_window_mass": active_window_mass,
        "kappa_m_local": float(kappa * m_local),
        "kappa_m_active": float(kappa * m_active),
    }

def run_b18_1_case(
    protocol="front_anchored_write",
    alpha=0.03,
    kappa=6.0,
    n_write_pulses=1,
    rest_delay=3.0,
    read_width=None,
    params=DEFAULT,
    store_trace=False,
):
    if read_width is None:
        read_width = params["read_width_default"]

    x, dx = make_grid(params)
    u = sigmoid_front(x, params["R0"], params["front_width_init"])
    m = np.zeros_like(x)

    # Pre-evolve.
    for _ in range(int(round(params["T_pre"] / params["dt"]))):
        u = rd_step(x, dx, u, m, params, read_amp=0.0, kappa=0.0, inhibitor_on=False)
        m = trace_step(x, dx, u, m, alpha, params, write_on=False)

    R_initial = front_location(x, u, params["u_thr"])
    lab_write_site = R_initial + params["y_write"]
    write_sites = []

    write_trace_rows = []
    t = 0.0

    def record_write(phase, pulse_index=-1):
        R_now = front_location(x, u, params["u_thr"])
        moment = trace_moments(x, m, R_now)
        obs = compute_read_observables(x, u, m, R_now, read_width, kappa)
        write_trace_rows.append({
            "phase": phase,
            "t": float(t),
            "pulse_index": int(pulse_index),
            **moment,
            **obs,
        })

    if store_trace:
        record_write("write_start")

    # Write phase: no inhibitory feedback.
    for pidx in range(int(n_write_pulses)):
        for step in range(int(round(params["write_duration"] / params["dt"]))):
            R_now = front_location(x, u, params["u_thr"])

            if protocol == "front_anchored_write":
                x_write = R_now + params["y_write"]
            elif protocol == "lab_fixed_write":
                x_write = lab_write_site
            else:
                raise ValueError(f"Unknown protocol: {protocol}")

            write_profile = gaussian(x, x_write, params["write_width"])

            u = rd_step(
                x, dx, u, m, params,
                read_profile=write_profile,
                read_amp=params["write_amp"],
                kappa=0.0,
                inhibitor_on=False,
            )

            m = trace_step(
                x, dx, u, m, alpha, params,
                write_profile=write_profile,
                write_on=True,
            )

            write_sites.append(float(x_write))
            t += params["dt"]

            if store_trace and step % params["record_every"] == 0:
                record_write("write", pidx)

        if pidx < int(n_write_pulses) - 1:
            for step in range(int(round(params["inter_write_gap"] / params["dt"]))):
                u = rd_step(x, dx, u, m, params, read_amp=0.0, kappa=0.0, inhibitor_on=False)
                m = trace_step(x, dx, u, m, alpha, params, write_on=False)
                t += params["dt"]

                if store_trace and step % params["record_every"] == 0:
                    record_write("inter_write_gap", pidx)

    # Rest before read.
    for step in range(int(round(rest_delay / params["dt"]))):
        u = rd_step(x, dx, u, m, params, read_amp=0.0, kappa=0.0, inhibitor_on=False)
        m = trace_step(x, dx, u, m, alpha, params, write_on=False)
        t += params["dt"]

        if store_trace and step % params["record_every"] == 0:
            record_write("rest_before_read")

    R_read_start = front_location(x, u, params["u_thr"])
    x_read_start = R_read_start + params["y_read"]

    u_read_start = np.array(u, copy=True)
    m_read_start = np.array(m, copy=True)

    moment_start = trace_moments(x, m_read_start, R_read_start)
    read_start_obs = compute_read_observables(x, u_read_start, m_read_start, R_read_start, read_width, kappa)

    def read_branch(erase=False, branch_name="kept"):
        ub = np.array(u_read_start, copy=True)
        mb = np.array(m_read_start, copy=True)

        if erase:
            mb[:] = 0.0

        branch_rows = []

        # Path-integrated diagnostics.
        L_path_local = 0.0
        L_path_active = 0.0
        L_path_raw_exposure = 0.0
        L_path_window_mass = 0.0
        L_path_active_window_mass = 0.0

        for step in range(int(round(params["read_duration"] / params["dt"]))):
            Rb = front_location(x, ub, params["u_thr"])
            xr = Rb + params["y_read"]
            read_profile = gaussian(x, xr, read_width)

            obs = compute_read_observables(x, ub, mb, Rb, read_width, kappa)

            dt = params["dt"]
            L_path_local += obs["kappa_m_local"] * dt
            L_path_active += obs["kappa_m_active"] * dt
            L_path_raw_exposure += obs["raw_inhibitory_exposure"] * dt
            L_path_window_mass += obs["window_mass"] * dt
            L_path_active_window_mass += obs["active_window_mass"] * dt

            if store_trace and step % params["record_every"] == 0:
                branch_rows.append({
                    "branch": branch_name,
                    "t_read": float(step * dt),
                    "R": float(Rb),
                    "u_at_read": weighted_sample(x, ub, xr, read_width),
                    "m_total": trace_moments(x, mb, Rb)["m_total"],
                    **obs,
                    "L_path_local_cum": float(L_path_local),
                    "L_path_active_cum": float(L_path_active),
                    "L_path_raw_exposure_cum": float(L_path_raw_exposure),
                })

            ub = rd_step(
                x, dx, ub, mb, params,
                read_profile=read_profile,
                read_amp=params["read_amp"],
                kappa=kappa,
                inhibitor_on=True,
            )

            # No new writing during read.
            mb = trace_step(x, dx, ub, mb, alpha, params, write_on=False)

        Rend = front_location(x, ub, params["u_thr"])
        xrend = Rend + params["y_read"]

        return {
            "R_end": float(Rend),
            "u_read_end": weighted_sample(x, ub, xrend, read_width),
            "m_local_end": weighted_sample(x, mb, xrend, read_width),
            "L_path_local": float(L_path_local),
            "L_path_active": float(L_path_active),
            "L_path_raw_exposure": float(L_path_raw_exposure),
            "L_path_window_mass": float(L_path_window_mass),
            "L_path_active_window_mass": float(L_path_active_window_mass),
            "u_final": ub,
            "m_final": mb,
            "trace": pd.DataFrame(branch_rows),
        }

    kept = read_branch(erase=False, branch_name="kept")
    erased = read_branch(erase=True, branch_name="erased")

    metrics = {
        "protocol": protocol,
        "alpha": float(alpha),
        "kappa": float(kappa),
        "n_write_pulses": int(n_write_pulses),
        "rest_delay": float(rest_delay),
        "read_width": float(read_width),
        "R_initial": float(R_initial),
        "R_read_start": float(R_read_start),
        "boundary_advance_before_read": float(R_read_start - R_initial),
        "lab_write_site": float(lab_write_site),
        "last_write_site": float(write_sites[-1]) if write_sites else np.nan,
        "mean_write_site": float(np.mean(write_sites)) if write_sites else np.nan,
        "y_lab_write_from_R_read": float(lab_write_site - R_read_start),
        "y_last_write_from_R_read": float((write_sites[-1] - R_read_start) if write_sites else np.nan),
        "x_read_start": float(x_read_start),

        # read-start metrics
        "m_local_read_start": float(read_start_obs["m_local"]),
        "m_active_read_start": float(read_start_obs["m_active"]),
        "effective_local_load_start": float(read_start_obs["kappa_m_local"]),
        "effective_active_load_start": float(read_start_obs["kappa_m_active"]),
        "raw_inhibitory_exposure_start": float(read_start_obs["raw_inhibitory_exposure"]),
        "effective_global_trace_load_start": float(kappa * moment_start["m_total"]),
        **moment_start,

        # Path-integrated metrics
        "L_path_local_kept": kept["L_path_local"],
        "L_path_active_kept": kept["L_path_active"],
        "L_path_raw_exposure_kept": kept["L_path_raw_exposure"],
        "L_path_window_mass_kept": kept["L_path_window_mass"],
        "L_path_active_window_mass_kept": kept["L_path_active_window_mass"],

        # erased should be near zero for path-load variables because m is erased
        "L_path_local_erased": erased["L_path_local"],
        "L_path_active_erased": erased["L_path_active"],
        "L_path_raw_exposure_erased": erased["L_path_raw_exposure"],

        # branch endpoints
        "R_kept_end": kept["R_end"],
        "R_erased_end": erased["R_end"],
        "u_kept_end": kept["u_read_end"],
        "u_erased_end": erased["u_read_end"],

        # Inhibitory readout convention:
        # positive means retained trace suppressed the front/read response.
        "suppression_R_delta": float(erased["R_end"] - kept["R_end"]),
        "suppression_u_delta": float(erased["u_read_end"] - kept["u_read_end"]),

        # B17-style sign for comparison
        "adaptive_R_delta_kept_minus_erased": float(kept["R_end"] - erased["R_end"]),
        "adaptive_u_delta_kept_minus_erased": float(kept["u_read_end"] - erased["u_read_end"]),
    }

    traces = None
    if store_trace:
        traces = {
            "write_trace": pd.DataFrame(write_trace_rows),
            "kept_read_trace": kept["trace"],
            "erased_read_trace": erased["trace"],
            "x": x,
            "u_read_start": u_read_start,
            "m_read_start": m_read_start,
            "u_kept_final": kept["u_final"],
            "u_erased_final": erased["u_final"],
            "m_kept_final": kept["m_final"],
            "m_erased_final": erased["m_final"],
        }

    return metrics, traces

def simple_linear_fit(xv, yv):
    xv = np.asarray(xv, dtype=float)
    yv = np.asarray(yv, dtype=float)
    mask = np.isfinite(xv) & np.isfinite(yv)
    xv = xv[mask]
    yv = yv[mask]

    if len(xv) < 2 or np.std(xv) <= 1e-15:
        return {
            "slope": np.nan,
            "intercept": np.nan,
            "r2": np.nan,
            "corr": np.nan,
            "n": int(len(xv)),
        }

    A = np.vstack([xv, np.ones_like(xv)]).T
    slope, intercept = np.linalg.lstsq(A, yv, rcond=None)[0]
    yhat = slope * xv + intercept

    ss_res = float(np.sum((yv - yhat) ** 2))
    ss_tot = float(np.sum((yv - np.mean(yv)) ** 2))
    r2 = 1.0 - ss_res / (ss_tot + 1e-15)

    return {
        "slope": float(slope),
        "intercept": float(intercept),
        "r2": float(r2),
        "corr": float(np.corrcoef(xv, yv)[0, 1]),
        "n": int(len(xv)),
    }

def zscore(s):
    s = pd.Series(s).astype(float)
    sd = float(s.std(ddof=0))
    if sd <= 1e-15:
        return s * 0.0
    return (s - float(s.mean())) / sd

def multi_linear_fit(data, feature_cols, target_col):
    X = data[feature_cols].to_numpy(dtype=float)
    y = data[target_col].to_numpy(dtype=float)

    mask = np.isfinite(y)
    for j in range(X.shape[1]):
        mask &= np.isfinite(X[:, j])

    X = X[mask]
    y = y[mask]

    if len(y) < X.shape[1] + 1:
        out = {"r2": np.nan, "n": int(len(y)), "intercept": np.nan}
        for c in feature_cols:
            out[f"coef_{c}"] = np.nan
        return out

    X_aug = np.column_stack([X, np.ones(len(X))])
    coef = np.linalg.lstsq(X_aug, y, rcond=None)[0]
    yhat = X_aug @ coef

    ss_res = float(np.sum((y - yhat) ** 2))
    ss_tot = float(np.sum((y - np.mean(y)) ** 2))
    r2 = 1.0 - ss_res / (ss_tot + 1e-15)

    out = {
        "r2": float(r2),
        "n": int(len(y)),
        "intercept": float(coef[-1]),
    }
    for c, v in zip(feature_cols, coef[:-1]):
        out[f"coef_{c}"] = float(v)
    return out
