def make_grid(params):
    N = int(params["N"])
    L = float(params["L"])
    x = np.linspace(-L, L, N)
    dx = float(x[1] - x[0])
    return x, dx

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

def div_flux_phi(phi, dx, params):
    dphi_edge = (phi[1:] - phi[:-1]) / dx
    phi_edge = 0.5 * (phi[1:] + phi[:-1])

    mobility = params["D0"] * (
        phi_edge * phi_edge / (phi_edge * phi_edge + params["phi_c"] ** 2)
        + params["epsD"]
    )

    flux = mobility * dphi_edge + params["gamma"] * (dphi_edge ** 3)

    out = np.zeros_like(phi)
    out[1:-1] = (flux[1:] - flux[:-1]) / dx
    out[0] = flux[0] / dx
    out[-1] = -flux[-1] / dx
    return out

def boundary_location(x, phi, phi_thr, side="right"):
    above = phi > phi_thr
    if not np.any(above):
        return np.nan

    if side == "right":
        idx = int(np.where(above)[0][-1])
        if idx >= len(x) - 1:
            return float(x[idx])
        x0, x1 = x[idx], x[idx + 1]
        y0, y1 = phi[idx], phi[idx + 1]
        if abs(y1 - y0) < 1e-15:
            return float(x0)
        return float(x0 + (phi_thr - y0) * (x1 - x0) / (y1 - y0))

    idx = int(np.where(above)[0][0])
    if idx <= 0:
        return float(x[idx])
    x0, x1 = x[idx - 1], x[idx]
    y0, y1 = phi[idx - 1], phi[idx]
    if abs(y1 - y0) < 1e-15:
        return float(x1)
    return float(x0 + (phi_thr - y0) * (x1 - x0) / (y1 - y0))

def weighted_sample(x, arr, center, width):
    w = gaussian(x, center, width)
    dx = float(x[1] - x[0])
    denom = float(np.sum(w) * dx)
    if denom <= 1e-15:
        return 0.0
    return float(np.sum(arr * w) * dx / denom)

def shift_field(x, arr, shift):
    # Positive shift moves the field profile rightward.
    return np.interp(x - shift, x, arr, left=0.0, right=0.0)

def memory_moments(x, m, R):
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

def make_boundary_mask(x, phi, params):
    dphi = grad_centered(phi, float(x[1] - x[0]))
    grad_abs = np.abs(dphi)
    layer = np.exp(-0.5 * ((phi - params["phi_thr"]) / params["boundary_layer_width"]) ** 2)

    if np.max(grad_abs) > 1e-15:
        layer = layer * grad_abs / (np.max(grad_abs) + 1e-15)

    mx = np.max(layer)
    if mx > 1e-15:
        layer = layer / mx
    return layer

def phi_step(x, dx, phi, source, params):
    dt = params["dt"]
    rhs = div_flux_phi(phi, dx, params) - params["mu"] * phi + source
    phi_new = phi + dt * rhs
    return np.clip(phi_new, 0.0, params["phi_clip"])

def memory_step(x, dx, m, phi, write_profile, alpha, params, write_on=True):
    if write_on:
        boundary_mask = make_boundary_mask(x, phi, params)
        write = params["beta"] * boundary_mask * write_profile
    else:
        write = 0.0

    m_new = m + params["dt"] * (
        -alpha * m
        + params["Dm"] * lap_neumann(m, dx)
        + write
    )
    return np.clip(m_new, 0.0, 20.0)

def pre_equilibrate(params=DEFAULT):
    x, dx = make_grid(params)
    phi = np.zeros_like(x)
    m = np.zeros_like(x)
    base_source = params["base_amp"] * gaussian(x, 0.0, params["base_width"])

    nsteps = int(params["T_pre"] / params["dt"])
    for _ in range(nsteps):
        phi = phi_step(x, dx, phi, base_source, params)

    R0 = boundary_location(x, phi, params["phi_thr"], side="right")
    return x, dx, phi, m, base_source, R0

def run_pde_case(
    protocol="lab_fixed_write",
    alpha=0.015,
    etaS=8.0,
    n_write_pulses=3,
    rest_delay=1.0,
    params=DEFAULT,
    store_trace=False,
):
    x, dx, phi0, m0, base_source, R_initial = pre_equilibrate(params)

    phi = np.array(phi0, copy=True)
    m = np.array(m0, copy=True)

    lab_write_site = R_initial + params["y_anchor"]
    write_sites = []

    trace_rows = []

    def record(phase, t_local, pulse_idx=-1):
        R = boundary_location(x, phi, params["phi_thr"], side="right")
        x_probe = R + params["y_probe"]
        row = {
            "phase": phase,
            "t": float(t_local),
            "pulse_index": int(pulse_idx),
            "R": float(R),
            "x_probe": float(x_probe),
            "phi_probe": weighted_sample(x, phi, x_probe, params["read_width"]),
            "m_probe": weighted_sample(x, m, x_probe, params["read_width"]),
            "m_total": memory_moments(x, m, R)["m_total"],
            "m_peak": memory_moments(x, m, R)["m_peak"],
        }
        trace_rows.append(row)

    t = 0.0
    if store_trace:
        record("write_start", t, -1)

    # ----------------------
    # Write phase
    # feedback is disabled during writing.
    # ----------------------
    for pidx in range(int(n_write_pulses)):
        nsteps_write = int(round(params["write_duration"] / params["dt"]))

        for step in range(nsteps_write):
            R_before = boundary_location(x, phi, params["phi_thr"], side="right")

            if protocol == "boundary_anchored_write":
                write_center = R_before + params["y_anchor"]
            else:
                write_center = lab_write_site

            write_profile = gaussian(x, write_center, params["write_width"])
            ext_source = params["write_amp"] * write_profile
            source = base_source + ext_source

            phi = phi_step(x, dx, phi, source, params)

            R_after = boundary_location(x, phi, params["phi_thr"], side="right")
            if protocol == "advected_memory" and np.isfinite(R_before) and np.isfinite(R_after):
                dR = R_after - R_before
                if abs(dR) > 0:
                    m = shift_field(x, m, dR)

            m = memory_step(x, dx, m, phi, write_profile, alpha, params, write_on=True)

            write_sites.append(float(write_center))
            t += params["dt"]

            if store_trace and (step % params["record_every"] == 0):
                record("write", t, pidx)

        # inter-write rest
        if pidx < int(n_write_pulses) - 1:
            nsteps_gap = int(round(params["inter_write_gap"] / params["dt"]))
            for step in range(nsteps_gap):
                R_before = boundary_location(x, phi, params["phi_thr"], side="right")

                phi = phi_step(x, dx, phi, base_source, params)

                R_after = boundary_location(x, phi, params["phi_thr"], side="right")
                if protocol == "advected_memory" and np.isfinite(R_before) and np.isfinite(R_after):
                    dR = R_after - R_before
                    if abs(dR) > 0:
                        m = shift_field(x, m, dR)

                m = memory_step(
                    x, dx, m, phi,
                    write_profile=np.zeros_like(x),
                    alpha=alpha,
                    params=params,
                    write_on=False,
                )
                t += params["dt"]

                if store_trace and (step % params["record_every"] == 0):
                    record("inter_write_rest", t, pidx)

    # post-write rest
    nsteps_rest = int(round(rest_delay / params["dt"]))
    for step in range(nsteps_rest):
        R_before = boundary_location(x, phi, params["phi_thr"], side="right")

        phi = phi_step(x, dx, phi, base_source, params)

        R_after = boundary_location(x, phi, params["phi_thr"], side="right")
        if protocol == "advected_memory" and np.isfinite(R_before) and np.isfinite(R_after):
            dR = R_after - R_before
            if abs(dR) > 0:
                m = shift_field(x, m, dR)

        m = memory_step(
            x, dx, m, phi,
            write_profile=np.zeros_like(x),
            alpha=alpha,
            params=params,
            write_on=False,
        )
        t += params["dt"]

        if store_trace and (step % params["record_every"] == 0):
            record("post_write_rest", t, -1)

    R_read_start = boundary_location(x, phi, params["phi_thr"], side="right")
    x_read_probe_start = R_read_start + params["y_probe"]

    phi_read_start = np.array(phi, copy=True)
    m_read_start = np.array(m, copy=True)

    write_moments = memory_moments(x, m_read_start, R_read_start)

    # ----------------------
    # Read branches:
    # kept history and erased history.
    # no new memory is written during read.
    # ----------------------
    def read_branch(erase=False, branch_name="kept"):
        phib = np.array(phi_read_start, copy=True)
        mb = np.array(m_read_start, copy=True)
        if erase:
            mb[:] = 0.0

        branch_rows = []

        def record_branch(t_read):
            Rb = boundary_location(x, phib, params["phi_thr"], side="right")
            xp = Rb + params["y_probe"]
            branch_rows.append({
                "branch": branch_name,
                "t_read": float(t_read),
                "R": float(Rb),
                "x_probe": float(xp),
                "phi_probe": weighted_sample(x, phib, xp, params["read_width"]),
                "m_probe": weighted_sample(x, mb, xp, params["read_width"]),
            })

        nsteps_read = int(round(params["read_duration"] / params["dt"]))
        if store_trace:
            record_branch(0.0)

        for step in range(nsteps_read):
            Rb = boundary_location(x, phib, params["phi_thr"], side="right")
            x_probe = Rb + params["y_probe"]

            read_profile = gaussian(x, x_probe, params["read_width"])
            m_local = weighted_sample(x, mb, x_probe, params["read_width"])

            ext_source = params["read_amp"] * read_profile * (1.0 + etaS * m_local)
            source = base_source + ext_source

            phib = phi_step(x, dx, phib, source, params)

            # Read phase: no new memory writing. Memory can forget and diffuse.
            mb = memory_step(
                x, dx, mb, phib,
                write_profile=np.zeros_like(x),
                alpha=alpha,
                params=params,
                write_on=False,
            )

            if store_trace and (step % params["record_every"] == 0):
                record_branch((step + 1) * params["dt"])

        R_end = boundary_location(x, phib, params["phi_thr"], side="right")
        x_probe_end = R_end + params["y_probe"]

        out = {
            "R_end": float(R_end),
            "phi_probe_end": weighted_sample(x, phib, x_probe_end, params["read_width"]),
            "m_probe_end": weighted_sample(x, mb, x_probe_end, params["read_width"]),
            "phi_final": phib,
            "m_final": mb,
            "trace": pd.DataFrame(branch_rows),
        }
        return out

    kept = read_branch(erase=False, branch_name="kept")
    erased = read_branch(erase=True, branch_name="erased")

    metrics = {
        "protocol": protocol,
        "alpha": float(alpha),
        "etaS": float(etaS),
        "n_write_pulses": int(n_write_pulses),
        "rest_delay": float(rest_delay),
        "R_initial": float(R_initial),
        "R_read_start": float(R_read_start),
        "boundary_advance_before_read": float(R_read_start - R_initial),
        "lab_write_site": float(lab_write_site),
        "last_write_site": float(write_sites[-1]) if write_sites else np.nan,
        "mean_write_site": float(np.mean(write_sites)) if write_sites else np.nan,
        "y_lab_write_from_R_read": float(lab_write_site - R_read_start),
        "y_last_write_from_R_read": float((write_sites[-1] - R_read_start) if write_sites else np.nan),
        "x_read_probe_start": float(x_read_probe_start),
        "y_read_probe_from_R": float(params["y_probe"]),
        "m_local_read_start": weighted_sample(x, m_read_start, x_read_probe_start, params["read_width"]),
        "m_at_read_probe_point": float(np.interp(x_read_probe_start, x, m_read_start, left=0.0, right=0.0)),
        "effective_local_load_start": float(etaS * weighted_sample(x, m_read_start, x_read_probe_start, params["read_width"])),
        "effective_global_load_start": float(etaS * write_moments["m_total"]),
        **write_moments,
        "phi_kept_end": kept["phi_probe_end"],
        "phi_erased_end": erased["phi_probe_end"],
        "adaptive_phi_delta": float(kept["phi_probe_end"] - erased["phi_probe_end"]),
        "R_kept_end": kept["R_end"],
        "R_erased_end": erased["R_end"],
        "adaptive_R_delta": float(kept["R_end"] - erased["R_end"]),
    }

    traces = None
    if store_trace:
        traces = {
            "write_trace": pd.DataFrame(trace_rows),
            "kept_read_trace": kept["trace"],
            "erased_read_trace": erased["trace"],
            "x": x,
            "phi_read_start": phi_read_start,
            "m_read_start": m_read_start,
            "kept_phi_final": kept["phi_final"],
            "erased_phi_final": erased["phi_final"],
            "kept_m_final": kept["m_final"],
            "erased_m_final": erased["m_final"],
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
