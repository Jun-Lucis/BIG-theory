def gaussian(center, width):
    return np.exp(-0.5 * ((x - center) / width) ** 2)

def laplacian_neumann(arr):
    lap = np.empty_like(arr)
    lap[1:-1] = (arr[2:] - 2.0 * arr[1:-1] + arr[:-2]) / (dx * dx)
    lap[0] = (arr[1] - arr[0]) / (dx * dx)
    lap[-1] = (arr[-2] - arr[-1]) / (dx * dx)
    return lap

def sample_field(arr, xpos):
    return float(np.interp(xpos, x, arr, left=0.0, right=0.0))

def weighted_sample(arr, center, width):
    w = gaussian(center, width)
    denom = float(np.sum(w) * dx)
    if denom <= 1e-15:
        return 0.0
    return float(np.sum(arr * w) * dx / denom)

def shift_field(arr, shift):
    # Positive shift moves a profile to the right.
    return np.interp(x - shift, x, arr, left=0.0, right=0.0)

def memory_moments(m, R):
    total = float(np.sum(m) * dx)
    peak = float(np.max(m)) if len(m) else 0.0
    idx = int(np.argmax(m)) if len(m) else 0
    x_peak = float(x[idx])
    if total > 1e-15:
        x_center = float(np.sum(x * m) * dx / total)
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

def simulate_write_phase(protocol, alpha, n_write_pulses, rest_delay, params=BASE, store_trace=False):
    R = float(params["R0"])
    R_initial = float(R)
    m = np.zeros_like(x)
    dt = float(params["dt"])

    lab_write_site = R_initial + params["y_anchor"]
    write_sites = []
    t_series, R_series = [], []
    local_m_series = []

    def do_step(source_center=None, active_write=False):
        nonlocal R, m

        old_R = R

        if active_write:
            # Feedback is disabled during write; boundary moves due to the external write stimulus only.
            dR = params["write_v"] * dt
            R += dR
        else:
            dR = 0.0

        if protocol == "advected_memory" and abs(dR) > 0.0:
            # Artificial control: attach existing memory to the moving boundary.
            m = shift_field(m, dR)

        source = 0.0
        if active_write and source_center is not None:
            source = gaussian(source_center, params["write_width"])

        m = m + dt * (
            -alpha * m
            + params["memory_diffusion"] * laplacian_neumann(m)
            + params["write_beta"] * source
        )
        m = np.maximum(m, 0.0)

        return old_R, R

    current_time = 0.0

    for pulse_idx in range(int(n_write_pulses)):
        nsteps_write = int(round(params["write_duration"] / dt))
        for _ in range(nsteps_write):
            if protocol == "boundary_anchored_write":
                write_center = R + params["y_anchor"]
            else:
                write_center = lab_write_site

            write_sites.append(write_center)
            do_step(source_center=write_center, active_write=True)

            if store_trace:
                t_series.append(current_time)
                R_series.append(R)
                local_m_series.append(weighted_sample(m, R + params["y_probe"], params["read_width"]))
            current_time += dt

        if pulse_idx < int(n_write_pulses) - 1:
            nsteps_gap = int(round(params["inter_write_gap"] / dt))
            for _ in range(nsteps_gap):
                do_step(source_center=None, active_write=False)
                if store_trace:
                    t_series.append(current_time)
                    R_series.append(R)
                    local_m_series.append(weighted_sample(m, R + params["y_probe"], params["read_width"]))
                current_time += dt

    nsteps_rest = int(round(rest_delay / dt))
    for _ in range(nsteps_rest):
        do_step(source_center=None, active_write=False)
        if store_trace:
            t_series.append(current_time)
            R_series.append(R)
            local_m_series.append(weighted_sample(m, R + params["y_probe"], params["read_width"]))
        current_time += dt

    R_read_start = float(R)
    x_read_probe = R_read_start + params["y_probe"]

    moments = memory_moments(m, R_read_start)
    moments.update({
        "R_initial": R_initial,
        "R_read_start": R_read_start,
        "boundary_advance_before_read": R_read_start - R_initial,
        "lab_write_site": lab_write_site,
        "last_write_site": float(write_sites[-1]) if write_sites else np.nan,
        "mean_write_site": float(np.mean(write_sites)) if write_sites else np.nan,
        "y_lab_write_from_R_read": lab_write_site - R_read_start,
        "y_last_write_from_R_read": (float(write_sites[-1]) - R_read_start) if write_sites else np.nan,
        "x_read_probe": x_read_probe,
        "y_read_probe_from_R": params["y_probe"],
        "m_local_read_start": weighted_sample(m, x_read_probe, params["read_width"]),
        "m_at_read_probe_point": sample_field(m, x_read_probe),
    })

    trace = None
    if store_trace:
        trace = {
            "t": np.array(t_series),
            "R": np.array(R_series),
            "m_local": np.array(local_m_series),
        }

    return R_read_start, m, moments, trace

def simulate_read_branch(R_start, m_start, etaS, params=BASE, erase=False, store_trace=False):
    R = float(R_start)
    m = np.array(m_start, copy=True)
    if erase:
        m[:] = 0.0

    dt = float(params["dt"])
    nsteps = int(round(params["read_duration"] / dt))
    phi = float(params["phi0"])

    t_series = []
    phi_series = []
    R_series = []
    mlocal_series = []

    for k in range(nsteps + 1):
        time = k * dt
        x_probe = R + params["y_probe"]
        m_local = weighted_sample(m, x_probe, params["read_width"])

        if store_trace:
            t_series.append(time)
            phi_series.append(phi)
            R_series.append(R)
            mlocal_series.append(m_local)

        if k == nsteps:
            break

        feedback = etaS * m_local
        response_factor = 1.0 + feedback

        # Read phase: no new history is written. Memory only decays/diffuses.
        phi = phi + dt * (
            params["phi_drive"] * response_factor
            - params["phi_decay"] * (phi - params["phi0"])
        )

        R = R + dt * params["read_v"] * response_factor

        m = m + dt * (
            -0.50 * params.get("read_memory_decay_factor", 1.0) * m * 0.0
            + params["memory_diffusion"] * laplacian_neumann(m)
        )
        m = np.maximum(m, 0.0)

    out = {
        "R_end": float(R),
        "phi_end": float(phi),
        "m_local_read_end": float(mlocal_series[-1]) if store_trace else weighted_sample(m, R + params["y_probe"], params["read_width"]),
    }

    trace = None
    if store_trace:
        trace = {
            "t": np.array(t_series),
            "phi": np.array(phi_series),
            "R": np.array(R_series),
            "m_local": np.array(mlocal_series),
        }

    return out, trace

def run_case(protocol, alpha, etaS, n_write_pulses, rest_delay, params=BASE, store_trace=False):
    R_read_start, m_read_start, write_metrics, write_trace = simulate_write_phase(
        protocol=protocol,
        alpha=alpha,
        n_write_pulses=n_write_pulses,
        rest_delay=rest_delay,
        params=params,
        store_trace=store_trace,
    )

    kept, kept_trace = simulate_read_branch(
        R_read_start,
        m_read_start,
        etaS=etaS,
        params=params,
        erase=False,
        store_trace=store_trace,
    )

    erased, erased_trace = simulate_read_branch(
        R_read_start,
        m_read_start,
        etaS=etaS,
        params=params,
        erase=True,
        store_trace=store_trace,
    )

    metrics = dict(write_metrics)
    metrics.update({
        "protocol": protocol,
        "alpha": float(alpha),
        "etaS": float(etaS),
        "n_write_pulses": int(n_write_pulses),
        "rest_delay": float(rest_delay),
        "effective_local_load_start": float(etaS * write_metrics["m_local_read_start"]),
        "effective_global_load_start": float(etaS * write_metrics["m_total"]),
        "phi_kept_end": kept["phi_end"],
        "phi_erased_end": erased["phi_end"],
        "adaptive_phi_delta": kept["phi_end"] - erased["phi_end"],
        "R_kept_end": kept["R_end"],
        "R_erased_end": erased["R_end"],
        "adaptive_R_delta": kept["R_end"] - erased["R_end"],
    })

    traces = None
    if store_trace:
        traces = {
            "write": write_trace,
            "kept_read": kept_trace,
            "erased_read": erased_trace,
            "m_read_start": m_read_start,
            "R_read_start": R_read_start,
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
    corr = float(np.corrcoef(xv, yv)[0, 1])

    return {
        "slope": float(slope),
        "intercept": float(intercept),
        "r2": float(r2),
        "corr": corr,
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
