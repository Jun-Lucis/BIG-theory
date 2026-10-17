def sig(df):
    return sorted([
        (
            str(r["ray_label"]),
            round(float(r["T"]), 12),
            round(float(r["epsilon_lo"]), 12),
            round(float(r["epsilon_hi"]), 12),
            round(float(r["F_lo"]), 12),
            round(float(r["F_hi"]), 12),
        )
        for _, r in df.iterrows()
    ])

def make_grid(N=48, L=8.0):
    dx = L / N
    x1 = (np.arange(N) - N//2) * dx
    X, Y, Z = np.meshgrid(x1, x1, x1, indexing="ij")

    k1 = 2.0*np.pi*np.fft.fftfreq(N, d=dx)
    KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing="ij")
    K2 = KX*KX + KY*KY + KZ*KZ
    Kmag = np.sqrt(K2)

    kmax_axis = float(np.max(np.abs(k1)))
    cutoff_axis = (2.0/3.0) * kmax_axis
    dealias = (np.abs(KX) <= cutoff_axis) & (np.abs(KY) <= cutoff_axis) & (np.abs(KZ) <= cutoff_axis)
    kcut_radial = float(np.max(Kmag[dealias]))

    return {
        "N": int(N),
        "L": float(L),
        "dx": float(dx),
        "X": X, "Y": Y, "Z": Z,
        "KX": KX, "KY": KY, "KZ": KZ,
        "K2": K2,
        "Kmag": Kmag,
        "kmax_axis": kmax_axis,
        "cutoff_axis": cutoff_axis,
        "kcut_radial": kcut_radial,
        "dealias": dealias,
        "dV": float(dx**3),
    }

def fftn3(f):
    return np.fft.fftn(f)

def ifftn3(fhat):
    return np.fft.ifftn(fhat).real

def apply_dealias_hat(fhat, grid):
    return fhat * grid["dealias"]

def spectral_derivative(f, K):
    return ifftn3(1j * K * fftn3(f))

def laplacian(f, grid):
    return ifftn3(-grid["K2"] * fftn3(f))

def curl_from_components(ax, ay, az, grid, dealias=False):
    KX, KY, KZ = grid["KX"], grid["KY"], grid["KZ"]
    axh, ayh, azh = fftn3(ax), fftn3(ay), fftn3(az)

    wxh = 1j * (KY*azh - KZ*ayh)
    wyh = 1j * (KZ*axh - KX*azh)
    wzh = 1j * (KX*ayh - KY*axh)

    if dealias:
        wxh = apply_dealias_hat(wxh, grid)
        wyh = apply_dealias_hat(wyh, grid)
        wzh = apply_dealias_hat(wzh, grid)

    return ifftn3(wxh), ifftn3(wyh), ifftn3(wzh)

def project_divergence_free_vector(vx, vy, vz, grid):
    KX, KY, KZ, K2 = grid["KX"], grid["KY"], grid["KZ"], grid["K2"]
    vxh, vyh, vzh = fftn3(vx), fftn3(vy), fftn3(vz)
    divh = KX*vxh + KY*vyh + KZ*vzh

    mask = K2 > 0
    vxh2 = vxh.copy()
    vyh2 = vyh.copy()
    vzh2 = vzh.copy()

    vxh2[mask] = vxh[mask] - KX[mask]*divh[mask]/K2[mask]
    vyh2[mask] = vyh[mask] - KY[mask]*divh[mask]/K2[mask]
    vzh2[mask] = vzh[mask] - KZ[mask]*divh[mask]/K2[mask]

    vxh2[~mask] = 0.0
    vyh2[~mask] = 0.0
    vzh2[~mask] = 0.0

    return ifftn3(vxh2), ifftn3(vyh2), ifftn3(vzh2)

def velocity_from_vorticity(wx, wy, wz, grid):
    KX, KY, KZ, K2 = grid["KX"], grid["KY"], grid["KZ"], grid["K2"]

    wx, wy, wz = project_divergence_free_vector(wx, wy, wz, grid)

    wxh, wyh, wzh = fftn3(wx), fftn3(wy), fftn3(wz)
    mask = K2 > 0

    uxhat = np.zeros_like(wxh, dtype=complex)
    uyhat = np.zeros_like(wyh, dtype=complex)
    uzhat = np.zeros_like(wzh, dtype=complex)

    uxhat[mask] = 1j * (KY[mask]*wzh[mask] - KZ[mask]*wyh[mask]) / K2[mask]
    uyhat[mask] = 1j * (KZ[mask]*wxh[mask] - KX[mask]*wzh[mask]) / K2[mask]
    uzhat[mask] = 1j * (KX[mask]*wyh[mask] - KY[mask]*wxh[mask]) / K2[mask]

    return ifftn3(uxhat), ifftn3(uyhat), ifftn3(uzhat)

def gradients_of_vector(vx, vy, vz, grid):
    KX, KY, KZ = grid["KX"], grid["KY"], grid["KZ"]
    grad = {}
    for name, f in [("x", vx), ("y", vy), ("z", vz)]:
        grad[(name, "x")] = spectral_derivative(f, KX)
        grad[(name, "y")] = spectral_derivative(f, KY)
        grad[(name, "z")] = spectral_derivative(f, KZ)
    return grad

def strain_tensor_from_velocity(ux, uy, uz, grid):
    g = gradients_of_vector(ux, uy, uz, grid)
    Sxx = g[("x", "x")]
    Syy = g[("y", "y")]
    Szz = g[("z", "z")]
    Sxy = 0.5*(g[("x", "y")] + g[("y", "x")])
    Sxz = 0.5*(g[("x", "z")] + g[("z", "x")])
    Syz = 0.5*(g[("y", "z")] + g[("z", "y")])
    return Sxx, Syy, Szz, Sxy, Sxz, Syz

def omega_dot_S_omega(wx, wy, wz, S):
    Sxx, Syy, Szz, Sxy, Sxz, Syz = S
    return (
        Sxx*wx*wx + Syy*wy*wy + Szz*wz*wz
        + 2.0*Sxy*wx*wy + 2.0*Sxz*wx*wz + 2.0*Syz*wy*wz
    )

def divergence_of_vector(vx, vy, vz, grid):
    KX, KY, KZ = grid["KX"], grid["KY"], grid["KZ"]
    return spectral_derivative(vx, KX) + spectral_derivative(vy, KY) + spectral_derivative(vz, KZ)

def spectral_tail_diagnostics(wx, wy, wz, grid):
    wxh = fftn3(wx)
    wyh = fftn3(wy)
    wzh = fftn3(wz)

    spec = np.abs(wxh)**2 + np.abs(wyh)**2 + np.abs(wzh)**2
    total = float(np.sum(spec))
    if total <= 0:
        return {
            "outside_dealias_fraction": 0.0,
            "tail_fraction_70": 0.0,
            "tail_fraction_85": 0.0,
            "spectral_k95_over_kcut": 0.0,
        }

    Kmag = grid["Kmag"]
    dealias = grid["dealias"]
    kcut = max(grid["kcut_radial"], 1e-300)

    outside_fraction = float(np.sum(spec[~dealias]) / total)
    tail70 = float(np.sum(spec[(Kmag > 0.70*kcut) & dealias]) / total)
    tail85 = float(np.sum(spec[(Kmag > 0.85*kcut) & dealias]) / total)

    flat_k = Kmag.ravel()
    flat_s = spec.ravel()
    order = np.argsort(flat_k)
    cum = np.cumsum(flat_s[order])
    idx95 = int(np.searchsorted(cum, 0.95*total))
    idx95 = min(max(idx95, 0), len(order)-1)
    k95 = float(flat_k[order[idx95]])

    return {
        "outside_dealias_fraction": outside_fraction,
        "tail_fraction_70": tail70,
        "tail_fraction_85": tail85,
        "spectral_k95_over_kcut": float(k95 / kcut),
    }

def make_tilted_pair_vector_potential(
    X, Y, Z,
    R=0.55,
    sep_factor=0.95,
    pair_angle=np.pi/6,
    twist_factor=0.80,
    imbalance=0.80,
    axial_coupling=0.25,
    phase=np.pi/2,
    handedness=-1.0,
):
    eps = 1e-12
    sep = sep_factor * R
    ca, sa = np.cos(pair_angle), np.sin(pair_angle)

    x0 = sep * ca
    y0 = sep * sa
    x1 = -sep * ca
    y1 = -sep * sa

    G1 = np.exp(-((X-x0)**2 + (Y-y0)**2 + Z**2)/(2.0*R*R))
    G2 = np.exp(-((X-x1)**2 + (Y-y1)**2 + Z**2)/(2.0*R*R))

    k = twist_factor / max(R, eps)

    U = ca*X + sa*Y
    V = -sa*X + ca*Y

    ax = G1*np.cos(k*Z + phase) - imbalance*G2*np.sin(k*V - phase)
    ay = handedness*G1*np.sin(k*Z + phase) + imbalance*G2*np.cos(k*U + phase)
    az = axial_coupling*(G1-G2)*np.sin(k*(U+V) + 0.5*phase)

    return ax, ay, az

def make_base_vorticity_from_params(params, grid):
    X, Y, Z = grid["X"], grid["Y"], grid["Z"]

    ax, ay, az = make_tilted_pair_vector_potential(
        X, Y, Z,
        R=params["R"],
        sep_factor=params["sep_factor"],
        pair_angle=params["pair_angle"],
        twist_factor=params["twist_factor"],
        imbalance=params["imbalance"],
        axial_coupling=params["axial_coupling"],
        phase=params["phase"],
        handedness=params["handedness"],
    )

    wx, wy, wz = curl_from_components(ax, ay, az, grid, dealias=True)
    wx, wy, wz = project_divergence_free_vector(wx, wy, wz, grid)

    mag = np.sqrt(wx*wx + wy*wy + wz*wz)
    max_mag = float(np.max(mag))
    if max_mag <= 0:
        raise RuntimeError("zero vorticity field")
    return wx/max_mag, wy/max_mag, wz/max_mag

def kinetic_energy_from_vorticity(wx, wy, wz, grid):
    ux, uy, uz = velocity_from_vorticity(wx, wy, wz, grid)
    return 0.5 * float(np.sum((ux*ux + uy*uy + uz*uz)) * grid["dV"])

def scale_to_kinetic_energy(wx, wy, wz, grid, Emax=1.0, chi=1.0):
    E0 = kinetic_energy_from_vorticity(wx, wy, wz, grid)
    scale = chi * np.sqrt(Emax / max(E0, 1e-300))
    return scale*wx, scale*wy, scale*wz, float(scale), float(E0)

def make_gate_mask(omega_sq, gate_mode="top_k", top_k=32, theta_frac=0.70):
    flat = omega_sq.ravel()
    n_total = flat.size

    if gate_mode == "top_k":
        k = int(max(1, min(top_k, n_total)))
        kth = np.partition(flat, n_total-k)[n_total-k]
        mask = omega_sq >= kth
        gate_label = f"topk_{k}"
    elif gate_mode == "fixed_theta":
        threshold = theta_frac * float(np.max(omega_sq))
        mask = omega_sq >= threshold
        gate_label = f"theta_{theta_frac:g}"
    else:
        raise ValueError(f"Unknown gate_mode: {gate_mode}")

    return np.asarray(mask, dtype=bool), gate_label

def compute_balance_metrics(wx, wy, wz, grid, nu, gate_mode="top_k", top_k=32, theta_frac=0.70):
    dV = grid["dV"]

    ux, uy, uz = velocity_from_vorticity(wx, wy, wz, grid)
    S = strain_tensor_from_velocity(ux, uy, uz, grid)
    stretch_density = omega_dot_S_omega(wx, wy, wz, S)

    gw = gradients_of_vector(wx, wy, wz, grid)
    gradomega_sq = np.zeros_like(wx)
    for val in gw.values():
        gradomega_sq += val*val

    omega_sq = wx*wx + wy*wy + wz*wz
    u_sq = ux*ux + uy*uy + uz*uz

    mask, gate_label = make_gate_mask(omega_sq, gate_mode=gate_mode, top_k=top_k, theta_frac=theta_frac)

    stretch_total = float(np.sum(stretch_density) * dV)
    gradomega_total = float(np.sum(gradomega_sq) * dV)
    dissipation_total = float(nu * gradomega_total)
    balance_total = stretch_total - dissipation_total

    enstrophy_half = 0.5 * float(np.sum(omega_sq) * dV)
    kinetic_energy = 0.5 * float(np.sum(u_sq) * dV)

    stretch_gate = stretch_density[mask]
    grad_gate = gradomega_sq[mask]

    pos_gate = float(np.sum(np.maximum(stretch_gate, 0.0)) * dV)
    neg_gate = float(np.sum(np.maximum(-stretch_gate, 0.0)) * dV)
    signed_gate = pos_gate - neg_gate
    diss_gate = float(nu * np.sum(grad_gate) * dV)

    divw = divergence_of_vector(wx, wy, wz, grid)
    spectral = spectral_tail_diagnostics(wx, wy, wz, grid)

    return {
        "kinetic_energy": kinetic_energy,
        "enstrophy_half": enstrophy_half,
        "stretch_total": stretch_total,
        "gradomega_total": gradomega_total,
        "dissipation_total": dissipation_total,
        "balance_total": balance_total,
        "total_balance_open": bool(balance_total > 0),
        "gate_mode": gate_mode,
        "gate_label": gate_label,
        "gate_cell_count": int(np.sum(mask)),
        "gate_volume_fraction": float(np.mean(mask)),
        "positive_stretch_gate": pos_gate,
        "negative_stretch_gate": neg_gate,
        "signed_stretch_gate": signed_gate,
        "dissipation_gate": diss_gate,
        "theta_signed_gate": signed_gate / max(diss_gate, 1e-300),
        "gate_open": bool(signed_gate > diss_gate),
        "coherence_gate": signed_gate / max(pos_gate + neg_gate, 1e-300),
        "max_omega": float(np.max(np.sqrt(omega_sq))),
        "max_u": float(np.max(np.sqrt(u_sq))),
        "div_omega_l2": float(np.sqrt(np.sum(divw*divw) * dV)),
        **spectral,
    }

def vorticity_rhs(wx, wy, wz, grid, nu):
    ux, uy, uz = velocity_from_vorticity(wx, wy, wz, grid)

    cx = uy*wz - uz*wy
    cy = uz*wx - ux*wz
    cz = ux*wy - uy*wx

    ncx, ncy, ncz = curl_from_components(cx, cy, cz, grid, dealias=True)

    rhsx = ncx + nu * laplacian(wx, grid)
    rhsy = ncy + nu * laplacian(wy, grid)
    rhsz = ncz + nu * laplacian(wz, grid)

    return project_divergence_free_vector(rhsx, rhsy, rhsz, grid)

def rk4_step(wx, wy, wz, grid, nu, dt):
    k1 = vorticity_rhs(wx, wy, wz, grid, nu)
    k2 = vorticity_rhs(wx + 0.5*dt*k1[0], wy + 0.5*dt*k1[1], wz + 0.5*dt*k1[2], grid, nu)
    k3 = vorticity_rhs(wx + 0.5*dt*k2[0], wy + 0.5*dt*k2[1], wz + 0.5*dt*k2[2], grid, nu)
    k4 = vorticity_rhs(wx + dt*k3[0], wy + dt*k3[1], wz + dt*k3[2], grid, nu)

    wx_new = wx + (dt/6.0)*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0])
    wy_new = wy + (dt/6.0)*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1])
    wz_new = wz + (dt/6.0)*(k1[2] + 2*k2[2] + 2*k3[2] + k4[2])

    return project_divergence_free_vector(wx_new, wy_new, wz_new, grid)

def choose_dt(wx, wy, wz, grid, nu, dt_cap=5.0e-5, cfl=0.10):
    ux, uy, uz = velocity_from_vorticity(wx, wy, wz, grid)
    max_u = float(np.max(np.sqrt(ux*ux + uy*uy + uz*uz)))
    dx = grid["dx"]
    dt_adv = cfl * dx / max(max_u, 1e-12)
    dt_diff = 0.08 * dx*dx / max(nu, 1e-12)
    return float(min(dt_cap, dt_adv, dt_diff))

def cumulative_trapezoid(y, x):
    y = np.asarray(y)
    x = np.asarray(x)
    out = np.zeros_like(y, dtype=float)
    if len(y) <= 1:
        return out
    increments = 0.5 * (y[1:] + y[:-1]) * np.diff(x)
    out[1:] = np.cumsum(increments)
    return out

def family_C_final_point(ray_label, epsilon):
    assert ray_label in ENDPOINTS_C
    e=float(epsilon); ep=ENDPOINTS_C[ray_label]
    p={}
    for k in PARAM_KEYS_C:
        p[k]=float(BASE_C[k] + e*(ep[k]-BASE_C[k]))
    p['handedness']=-1.0
    p['ray_label']=ray_label; p['epsilon']=e
    return p

def point_on_ray_B204_solver_ready(ray_label, epsilon):
    p=dict(family_C_final_point(ray_label, epsilon))
    p['nu']=NU; p['Emax']=EMAX
    return p

def run_one_case_B204_from_params(supplied_params, N=48, L=8.0, dt_cap=5e-5, keep_timeseries=False):
    params = dict(supplied_params)
    ray_label = str(params["ray_label"])
    epsilon = float(params["epsilon"])
    params["variant_id"] = f"{ray_label}_eps_{epsilon:.10f}_N{N}_dt{dt_cap:.2e}"

    grid = make_grid(N=int(N), L=float(L))
    nu = float(params["nu"])
    Emax = float(params["Emax"])

    wx0, wy0, wz0 = make_base_vorticity_from_params(params, grid)
    wx, wy, wz, scale, E_base = scale_to_kinetic_energy(wx0, wy0, wz0, grid, Emax=Emax, chi=1.0)

    initial = compute_balance_metrics(wx, wy, wz, grid, nu=nu, gate_mode=GATE_MODE, top_k=TOP_K, theta_frac=THETA_FRAC)
    Z0 = initial["enstrophy_half"]

    t, step, next_save_t = 0.0, 0, 0.0
    dt_used, ts_rows = [], []

    def record(diag, tnow, stepnow, dtlast):
        row = {
            "ray_label": ray_label, "epsilon": float(epsilon), "N": int(N), "L": float(L),
            "dt_cap": float(dt_cap), "step": int(stepnow), "t": float(tnow),
            "stretch_total": float(diag["stretch_total"]),
            "dissipation_total": float(diag["dissipation_total"]),
            "balance_total": float(diag["balance_total"]),
            "coherence_gate": float(diag["coherence_gate"]),
            "max_omega": float(diag["max_omega"]),
            "enstrophy_half": float(diag["enstrophy_half"]),
            "delta_enstrophy": float(diag["enstrophy_half"]-Z0),
            "tail_fraction_70": float(diag["tail_fraction_70"]),
            "tail_fraction_85": float(diag["tail_fraction_85"]),
            "outside_dealias_fraction": float(diag["outside_dealias_fraction"]),
            "div_omega_l2": float(diag["div_omega_l2"]),
            "theta_signed_gate": float(diag["theta_signed_gate"]),
            "gate_open": bool(diag["gate_open"]),
            "dt_last": dtlast,
        }
        ts_rows.append(row)

    record(initial, 0.0, 0, np.nan)
    next_save_t += SAVE_DT

    while t < T_FINAL - 1e-15:
        dt = choose_dt(wx, wy, wz, grid, nu=nu, dt_cap=dt_cap, cfl=CFL)
        if t + dt > T_FINAL:
            dt = T_FINAL - t
        wx, wy, wz = rk4_step(wx, wy, wz, grid, nu, dt)
        t += dt
        step += 1
        dt_used.append(float(dt))

        if t >= next_save_t - 1e-15:
            diag = compute_balance_metrics(wx, wy, wz, grid, nu=nu, gate_mode=GATE_MODE, top_k=TOP_K, theta_frac=THETA_FRAC)
            record(diag, t, step, float(dt))
            while next_save_t <= t + 1e-15:
                next_save_t += SAVE_DT

    final = compute_balance_metrics(wx, wy, wz, grid, nu=nu, gate_mode=GATE_MODE, top_k=TOP_K, theta_frac=THETA_FRAC)
    if len(ts_rows)==0 or abs(ts_rows[-1]["t"]-t) > 1e-12:
        record(final, t, step, float(dt_used[-1]))

    ts = pd.DataFrame(ts_rows).sort_values("t").drop_duplicates("t", keep="last")
    ts["integrated_balance_to_t"] = cumulative_trapezoid(ts["balance_total"].to_numpy(), ts["t"].to_numpy())
    ts["balance_integral_error_to_t"] = ts["delta_enstrophy"] - ts["integrated_balance_to_t"]

    dz = float(final["enstrophy_half"] - Z0)
    ib = float(ts["integrated_balance_to_t"].iloc[-1])

    summary = {
        "ray_label": ray_label, "epsilon": float(epsilon), "N": int(N), "L": float(L),
        "dt_cap": float(dt_cap), "T_final": float(t), "n_steps": int(step),
        "scale": float(scale), "E_base": float(E_base),
        "initial_enstrophy_half": float(Z0), "final_enstrophy_half": float(final["enstrophy_half"]),
        "final_delta_enstrophy": dz, "final_relative_growth": float(dz/max(abs(Z0),1e-300)),
        "initial_balance_total": float(initial["balance_total"]), "final_balance_total": float(final["balance_total"]),
        "integrated_balance_final": ib,
        "balance_integral_error_final": float(ts["balance_integral_error_to_t"].iloc[-1]),
        "growth_positive": bool(dz > 0), "integrated_balance_positive": bool(ib > 0),
        "integrated_sign_correct": bool((dz > 0) == (ib > 0)),
        "initial_theta_signed_gate": float(initial["theta_signed_gate"]),
        "final_theta_signed_gate": float(final["theta_signed_gate"]),
        "initial_gate_open": bool(initial["gate_open"]), "final_gate_open": bool(final["gate_open"]),
        "final_tail_fraction_70": float(final["tail_fraction_70"]),
        "final_tail_fraction_85": float(final["tail_fraction_85"]),
        "final_outside_dealias_fraction": float(final["outside_dealias_fraction"]),
        "final_div_omega_l2": float(final["div_omega_l2"]),
        "dt_min": float(np.min(dt_used)), "dt_max_used": float(np.max(dt_used)),
    }
    return (summary, ts) if keep_timeseries else summary

def affine_family_point(ray, eps):
    return (
        base_vec
        + float(eps) * V[ray]
    )

def b205_row_to_solver_params(row):

    params = {
        k: float(row[k])
        for k in PARAM_KEYS_205
    }

    # Solver-required inherited constants.
    params["nu"] = 0.003
    params["Emax"] = 30.0

    # Metadata labels only.
    params["ray_label"] = (
        f"B20_5_{row['anchor_id']}_"
        f"{row['h_label']}_"
        f"q{int(row['basis_direction'])}_"
        f"{'plus' if int(row['sign']) > 0 else 'minus'}"
    )

    # The inherited runner expects an epsilon metadata field.
    # B20.5 is not an epsilon-ray experiment, so this is
    # explicitly a metadata placeholder, not a Family-C epsilon.
    params["epsilon"] = 0.0

    # Family C handedness is frozen at -1.
    params["handedness"] = -1.0

    return params

def trajectory_id_205(row):

    return (
        f"A{row['anchor_id']}_"
        f"{row['h_label']}_"
        f"q{int(row['basis_direction'])}_"
        f"{'plus' if int(row['sign']) > 0 else 'minus'}"
    )

def cache_paths_205(tid):

    return {
        "summary":
            CACHE_DIR /
            f"{tid}_summary.csv",

        "timeseries":
            CACHE_DIR /
            f"{tid}_timeseries.csv",

        "metadata":
            CACHE_DIR /
            f"{tid}_metadata.json",
    }

def params_from_row_205(row):

    params = {
        k: float(row[k])
        for k in PARAM_KEYS_205
    }

    params["nu"] = .003
    params["Emax"] = 30.0
    params["handedness"] = -1.0

    # Metadata compatibility only.
    params["ray_label"] = (
        "B20_5_"
        + trajectory_id_205(row)
    )

    params["epsilon"] = 0.0

    return params

def response_at_T_205(ts, T):

    assert "t" in ts.columns
    assert "delta_enstrophy" in ts.columns

    tt = ts["t"].to_numpy(float)

    i = int(
        np.argmin(
            np.abs(tt - float(T))
        )
    )

    terr = abs(
        float(tt[i]) - float(T)
    )

    assert terr <= 1e-12, (
        f"Frozen horizon missing: "
        f"T={T}, nearest error={terr}"
    )

    F = float(
        ts.iloc[i]["delta_enstrophy"]
    )

    assert np.isfinite(F)

    return F, terr

def validate_cache_205(row):

    tid = trajectory_id_205(row)
    p = cache_paths_205(tid)

    if not all(
        p[k].exists()
        for k in [
            "summary",
            "timeseries",
            "metadata",
        ]
    ):
        return False, "missing"

    try:

        s = pd.read_csv(
            p["summary"]
        )

        ts = pd.read_csv(
            p["timeseries"]
        )

        with open(
            p["metadata"],
            "r",
            encoding="utf-8"
        ) as f:
            meta = json.load(f)

        if len(s) != 1:
            return False, "summary_rows"

        sr = s.iloc[0]

        if (
            str(meta["trajectory_id"])
            != tid
        ):
            return False, "trajectory_id"

        if (
            str(meta["anchor_id"])
            != str(row["anchor_id"])
        ):
            return False, "anchor_id"

        if not np.isclose(
            float(meta["T_observe"]),
            float(row["T"]),
            rtol=0,
            atol=1e-15
        ):
            return False, "T_observe"

        if (
            str(meta["h_label"])
            != str(row["h_label"])
        ):
            return False, "h_label"

        if not np.isclose(
            float(meta["h"]),
            float(row["h"]),
            rtol=0,
            atol=1e-15
        ):
            return False, "h"

        if (
            int(meta["basis_direction"])
            != int(row["basis_direction"])
        ):
            return False, "basis_direction"

        if (
            int(meta["sign"])
            != int(row["sign"])
        ):
            return False, "sign"

        # Exact geometry check.
        for k in PARAM_KEYS_205:

            if not np.isclose(
                float(meta["parameters"][k]),
                float(row[k]),
                rtol=0,
                atol=1e-14
            ):
                return False, f"geometry_{k}"

        required_ts = [
            "t",
            "delta_enstrophy",
            "enstrophy_half",
            "balance_total",
            "div_omega_l2",
        ]

        for c in required_ts:

            if c not in ts.columns:
                return False, f"missing_{c}"

            if not np.isfinite(
                ts[c].to_numpy(float)
            ).all():
                return False, f"nonfinite_{c}"

        tt = ts["t"].to_numpy(float)

        if len(tt) < 2:
            return False, "too_few_times"

        if not np.all(
            np.diff(tt) > 0
        ):
            return False, "time_order"

        if not np.isclose(
            tt[0],
            0.0,
            rtol=0,
            atol=1e-12
        ):
            return False, "t0"

        if not np.isclose(
            tt[-1],
            .020,
            rtol=0,
            atol=1e-12
        ):
            return False, "tfinal"

        F, terr = response_at_T_205(
            ts,
            float(row["T"])
        )

        if not np.isclose(
            F,
            float(meta["F_observe"]),
            rtol=0,
            atol=1e-12
        ):
            return False, "F_observe"

        return True, "valid"

    except Exception as e:

        return (
            False,
            "validation_exception:"
            + type(e).__name__
            + ":"
            + str(e)
        )

def acquire_trajectory_205(row):

    tid = trajectory_id_205(row)

    ok, reason = validate_cache_205(
        row
    )

    if ok:

        print(
            f"CACHE VALID: {tid}"
        )

        return

    print(
        f"\nPDE RUN: {tid}"
    )

    params = params_from_row_205(
        row
    )

    # Final geometry check immediately before PDE.
    for k in PARAM_KEYS_205:

        assert np.isclose(
            float(params[k]),
            float(row[k]),
            rtol=0,
            atol=1e-14
        )

    assert params["nu"] == .003
    assert params["Emax"] == 30.0
    assert params["handedness"] == -1.0

    tic = time.time()

    summary, ts = (
        run_one_case_B204_from_params(
            params,
            N=48,
            L=8.0,
            dt_cap=5e-5,
            keep_timeseries=True
        )
    )

    elapsed = (
        time.time() - tic
    )

    Fobs, terr = response_at_T_205(
        ts,
        float(row["T"])
    )

    p = cache_paths_205(
        tid
    )

    pd.DataFrame(
        [summary]
    ).to_csv(
        p["summary"],
        index=False
    )

    ts.to_csv(
        p["timeseries"],
        index=False
    )

    metadata = {
        "experiment":
            "BIG B20.5",

        "stage":
            "Stage A gradient reconstruction",

        "trajectory_id":
            tid,

        "anchor_id":
            str(row["anchor_id"]),

        "anchor_ray":
            str(row["anchor_ray"]),

        "T_observe":
            float(row["T"]),

        "epsilon_star_metadata":
            float(row["epsilon_star"]),

        "h_label":
            str(row["h_label"]),

        "h":
            float(row["h"]),

        "basis_direction":
            int(row["basis_direction"]),

        "sign":
            int(row["sign"]),

        "parameters": {
            k: float(row[k])
            for k in PARAM_KEYS_205
        },

        "nu":
            .003,

        "Emax":
            30.0,

        "handedness":
            -1.0,

        "N":
            48,

        "L":
            8.0,

        "dt_cap":
            5e-5,

        "T_final":
            .020,

        "F_observe":
            float(Fobs),

        "horizon_time_error":
            float(terr),

        "elapsed_seconds":
            float(elapsed),

        "scientific_freeze_modified":
            False,

        "b20_4_archive_modified":
            False,

        "holdout_trajectory":
            False,
    }

    with open(
        p["metadata"],
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            metadata,
            f,
            indent=2,
            sort_keys=True
        )

    ok2, reason2 = validate_cache_205(
        row
    )

    assert ok2, (
        f"Checkpoint invalid "
        f"for {tid}: {reason2}"
    )

    print(
        "COMPLETE / CHECKPOINT VALID: "
        f"{elapsed/60:.2f} min "
        f"/ F(T)={Fobs:+.9e}"
    )

def trajectory_id_205(row):
    return (
        f"A{row['anchor_id']}_"
        f"{row['h_label']}_"
        f"q{int(row['basis_direction'])}_"
        f"{'plus' if int(row['sign']) > 0 else 'minus'}"
    )

def center_paths(anchor):

    stem = f"B20_5_center_{anchor}"

    return {
        "summary":
            CENTER_CACHE /
            f"{stem}_summary.csv",

        "timeseries":
            CENTER_CACHE /
            f"{stem}_timeseries.csv",

        "metadata":
            CENTER_CACHE /
            f"{stem}_metadata.json",
    }

def validate_center_checkpoint(anchor):

    paths = center_paths(anchor)

    if not all(
        p.exists()
        for p in paths.values()
    ):
        return None

    try:
        summary = pd.read_csv(
            paths["summary"]
        )

        ts = pd.read_csv(
            paths["timeseries"]
        )

        with open(
            paths["metadata"],
            "r",
            encoding="utf-8"
        ) as f:
            meta = json.load(f)

        assert len(summary) == 1

        assert (
            str(meta["anchor_id"])
            == anchor
        )

        assert np.isclose(
            float(meta["T_observe"]),
            CENTER_T_205[anchor],
            rtol=0,
            atol=1e-15
        )

        # Frozen geometry
        p = center_params205[anchor]

        for k in PARAM_KEYS_205:

            assert np.isclose(
                float(meta["parameters"][k]),
                float(p[k]),
                rtol=0,
                atol=1e-14
            )

        assert np.isclose(
            float(meta["parameters"]["nu"]),
            .003
        )

        assert np.isclose(
            float(meta["parameters"]["Emax"]),
            30.0
        )

        assert np.isclose(
            float(meta["parameters"]["handedness"]),
            -1.0
        )

        required_cols = [
            "t",
            "delta_enstrophy",
            "enstrophy_half",
            "balance_total",
            "div_omega_l2",
        ]

        for c in required_cols:
            assert c in ts.columns

            assert np.isfinite(
                ts[c].to_numpy(float)
            ).all()

        tt = ts["t"].to_numpy(float)

        assert len(tt) >= 2
        assert np.all(
            np.diff(tt) > 0
        )

        assert np.isclose(
            tt[0],
            0.0,
            atol=1e-12
        )

        assert np.isclose(
            tt[-1],
            .020,
            atol=1e-12
        )

        Tc = CENTER_T_205[anchor]

        ii = int(
            np.argmin(
                np.abs(tt - Tc)
            )
        )

        terr = abs(
            float(tt[ii]) - Tc
        )

        assert terr <= 1e-12

        Fc = float(
            ts.iloc[ii][
                "delta_enstrophy"
            ]
        )

        assert np.isclose(
            Fc,
            float(meta["Fc"]),
            rtol=0,
            atol=1e-12
        )

        return {
            "anchor_id": anchor,
            "T_observe": Tc,
            "Fc": Fc,
            "horizon_time_error": terr,
            "final_delta_enstrophy":
                float(
                    summary.iloc[0][
                        "final_delta_enstrophy"
                    ]
                ),
            "final_div_omega_l2":
                float(
                    summary.iloc[0][
                        "final_div_omega_l2"
                    ]
                ),
            "status":
                "valid_checkpoint",
        }

    except Exception:
        return None

def first_existing(df, candidates):
    for c in candidates:
        if c in df.columns:
            return c
    return None

def holdout_paths(case_id):

    return {
        "summary":
            CACHE_DIR /
            f"{case_id}_summary.csv",

        "timeseries":
            CACHE_DIR /
            f"{case_id}_timeseries.csv",

        "metadata":
            CACHE_DIR /
            f"{case_id}_metadata.json",
    }

def validate_holdout_checkpoint(case_id):

    paths = holdout_paths(case_id)

    if not all(
        p.exists()
        for p in paths.values()
    ):
        return None

    try:

        s = pd.read_csv(
            paths["summary"]
        )

        ts = pd.read_csv(
            paths["timeseries"]
        )

        with open(
            paths["metadata"],
            "r",
            encoding="utf-8"
        ) as f:

            meta = json.load(f)

        assert len(s) == 1

        assert (
            str(meta["case_id"])
            == case_id
        )

        specrow = (
            holdout_parameter_table205[
                holdout_parameter_table205[
                    "case_id"
                ] == case_id
            ]
        )

        assert len(specrow) == 1
        specrow = specrow.iloc[0]

        assert (
            str(meta["anchor_id"])
            == str(
                specrow["anchor_id"]
            )
        )

        assert (
            str(meta["holdout_id"])
            == str(
                specrow["holdout_id"]
            )
        )

        assert (
            str(meta["sign_label"])
            == str(
                specrow["sign_label"]
            )
        )

        for k in PARAM_KEYS_205:

            assert np.isclose(
                float(
                    meta[
                        "parameters"
                    ][k]
                ),
                float(specrow[k]),
                rtol=0,
                atol=1e-14
            )

        tt = ts["t"].to_numpy(float)

        assert len(tt) >= 2

        assert np.all(
            np.diff(tt) > 0
        )

        assert np.isclose(
            tt[0],
            0.0,
            atol=1e-12
        )

        assert np.isclose(
            tt[-1],
            .020,
            atol=1e-12
        )

        Tc = float(
            specrow["T_observe"]
        )

        ii = int(
            np.argmin(
                np.abs(tt - Tc)
            )
        )

        terr = abs(
            float(tt[ii]) - Tc
        )

        assert terr <= 1e-12

        F_obs = float(
            ts.iloc[ii][
                "delta_enstrophy"
            ]
        )

        assert np.isfinite(F_obs)

        # Numerical validity diagnostics.
        required = [
            "enstrophy_half",
            "delta_enstrophy",
            "balance_total",
            "div_omega_l2",
        ]

        for c in required:

            assert c in ts.columns

            assert np.isfinite(
                ts[c].to_numpy(float)
            ).all()

        return {
            "case_id":
                case_id,

            "anchor_id":
                str(specrow["anchor_id"]),

            "T_observe":
                Tc,

            "holdout_id":
                str(specrow["holdout_id"]),

            "h":
                float(specrow["h"]),

            "sign_label":
                str(specrow["sign_label"]),

            "signed_step":
                float(
                    specrow[
                        "signed_step"
                    ]
                ),

            "F_pred":
                float(specrow["F_pred"]),

            "D_pred":
                float(specrow["D_pred"]),

            "F_obs":
                F_obs,

            "horizon_time_error":
                terr,

            "final_delta_enstrophy":
                float(
                    s.iloc[0][
                        "final_delta_enstrophy"
                    ]
                ),

            "final_div_omega_l2":
                float(
                    s.iloc[0][
                        "final_div_omega_l2"
                    ]
                ),

            "status":
                "valid_checkpoint",
        }

    except Exception:

        return None

def holdout_paths(case_id):

    return {
        "summary":
            CACHE_DIR /
            f"{case_id}_summary.csv",

        "timeseries":
            CACHE_DIR /
            f"{case_id}_timeseries.csv",

        "metadata":
            CACHE_DIR /
            f"{case_id}_metadata.json",
    }

def validate_holdout_checkpoint(case_id):

    paths = holdout_paths(case_id)

    if not all(
        p.exists()
        for p in paths.values()
    ):
        return None

    try:

        s = pd.read_csv(
            paths["summary"]
        )

        ts = pd.read_csv(
            paths["timeseries"]
        )

        with open(
            paths["metadata"],
            "r",
            encoding="utf-8"
        ) as f:

            meta = json.load(f)

        assert len(s) == 1

        assert (
            str(meta["case_id"])
            == case_id
        )

        specrow = (
            holdout_parameter_table205[
                holdout_parameter_table205[
                    "case_id"
                ] == case_id
            ]
        )

        assert len(specrow) == 1
        specrow = specrow.iloc[0]

        assert (
            str(meta["anchor_id"])
            == str(specrow["anchor_id"])
        )

        assert (
            str(meta["holdout_id"])
            == str(specrow["holdout_id"])
        )

        assert (
            str(meta["sign_label"])
            == str(specrow["sign_label"])
        )

        for k in PARAM_KEYS_205:

            assert np.isclose(
                float(
                    meta[
                        "parameters"
                    ][k]
                ),
                float(specrow[k]),
                rtol=0,
                atol=1e-14
            )

        tt = ts["t"].to_numpy(float)

        assert len(tt) >= 2

        assert np.all(
            np.diff(tt) > 0
        )

        assert np.isclose(
            tt[0],
            0.0,
            atol=1e-12
        )

        assert np.isclose(
            tt[-1],
            .020,
            atol=1e-12
        )

        Tc = float(
            specrow["T_observe"]
        )

        ii = int(
            np.argmin(
                np.abs(tt - Tc)
            )
        )

        terr = abs(
            float(tt[ii]) - Tc
        )

        assert terr <= 1e-12

        F_obs = float(
            ts.iloc[ii][
                "delta_enstrophy"
            ]
        )

        assert np.isfinite(F_obs)

        required = [
            "enstrophy_half",
            "delta_enstrophy",
            "balance_total",
            "div_omega_l2",
        ]

        for c in required:

            assert c in ts.columns

            assert np.isfinite(
                ts[c].to_numpy(float)
            ).all()

        return {
            "case_id":
                case_id,

            "anchor_id":
                str(specrow["anchor_id"]),

            "T_observe":
                Tc,

            "holdout_id":
                str(specrow["holdout_id"]),

            "h":
                float(specrow["h"]),

            "sign_label":
                str(specrow["sign_label"]),

            "signed_step":
                float(specrow["signed_step"]),

            "F_pred":
                float(specrow["F_pred"]),

            "D_pred":
                float(specrow["D_pred"]),

            "F_obs":
                F_obs,

            "horizon_time_error":
                terr,

            "final_delta_enstrophy":
                float(
                    s.iloc[0][
                        "final_delta_enstrophy"
                    ]
                ),

            "final_div_omega_l2":
                float(
                    s.iloc[0][
                        "final_div_omega_l2"
                    ]
                ),

            "status":
                "valid_checkpoint",
        }

    except Exception:

        return None

def sha256_file(path, chunk_size=1024 * 1024):

    h = hashlib.sha256()

    with open(path, "rb") as f:

        while True:

            chunk = f.read(chunk_size)

            if not chunk:
                break

            h.update(chunk)

    return h.hexdigest()
