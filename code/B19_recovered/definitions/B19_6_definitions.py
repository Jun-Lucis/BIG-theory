# Extracted definitions only. Function bodies unchanged; no notebook top-level execution.

def to_jsonable(obj):
    if isinstance(obj, dict):
        return {str(k): to_jsonable(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [to_jsonable(v) for v in obj]
    if isinstance(obj, tuple):
        return [to_jsonable(v) for v in obj]
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    if isinstance(obj, np.integer):
        return int(obj)
    if isinstance(obj, np.floating):
        return float(obj)
    if isinstance(obj, np.bool_):
        return bool(obj)
    return obj


def backup_to_drive(path):
    path = Path(path)
    try:
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)
        dst = BACKUP_DIR / path.name
        if path.resolve() == dst.resolve():
            print("Already on Drive:", dst)
            return
        shutil.copy2(path, dst)
        print("Saved to Drive:", dst)
    except Exception as e:
        print("Drive backup failed:", e)


def save_csv(df, filename):
    path = OUTDIR / filename
    df.to_csv(path, index=False)
    print("Saved local:", path)
    backup_to_drive(path)
    return path


def save_json(obj, filename):
    path = OUTDIR / filename
    with open(path, "w", encoding="utf-8") as f:
        json.dump(to_jsonable(obj), f, indent=2, ensure_ascii=False)
    print("Saved local:", path)
    backup_to_drive(path)
    return path


def save_text(text, filename):
    path = OUTDIR / filename
    path.write_text(text, encoding="utf-8")
    print("Saved local:", path)
    backup_to_drive(path)
    return path


def save_figure(filename, dpi=180):
    path = OUTDIR / filename
    plt.tight_layout()
    plt.savefig(path, dpi=dpi)
    print("Saved local:", path)
    backup_to_drive(path)
    plt.show()
    plt.close()
    return path


def make_grid(N=48, L=8.0):
    dx = L / N
    x1 = (np.arange(N) - N//2) * dx
    X, Y, Z = np.meshgrid(x1, x1, x1, indexing="ij")

    k1 = 2.0*np.pi*np.fft.fftfreq(N, d=dx)
    KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing="ij")
    K2 = KX*KX + KY*KY + KZ*KZ
    return X, Y, Z, KX, KY, KZ, K2, dx


def fftn3(f):
    return np.fft.fftn(f)


def ifftn3(fhat):
    return np.fft.ifftn(fhat).real


def spectral_derivative(f, K):
    return ifftn3(1j * K * fftn3(f))


def curl_from_vector_potential(ax, ay, az, KX, KY, KZ):
    axh = fftn3(ax)
    ayh = fftn3(ay)
    azh = fftn3(az)
    wx = ifftn3(1j * (KY*azh - KZ*ayh))
    wy = ifftn3(1j * (KZ*axh - KX*azh))
    wz = ifftn3(1j * (KX*ayh - KY*axh))
    return wx, wy, wz


def project_divergence_free_vector(vx, vy, vz, KX, KY, KZ, K2):
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


def velocity_from_vorticity(wx, wy, wz, KX, KY, KZ, K2):
    wx, wy, wz = project_divergence_free_vector(wx, wy, wz, KX, KY, KZ, K2)
    wxh, wyh, wzh = fftn3(wx), fftn3(wy), fftn3(wz)
    mask = K2 > 0

    uxhat = np.zeros_like(wxh, dtype=complex)
    uyhat = np.zeros_like(wyh, dtype=complex)
    uzhat = np.zeros_like(wzh, dtype=complex)

    uxhat[mask] = 1j * (KY[mask]*wzh[mask] - KZ[mask]*wyh[mask]) / K2[mask]
    uyhat[mask] = 1j * (KZ[mask]*wxh[mask] - KX[mask]*wzh[mask]) / K2[mask]
    uzhat[mask] = 1j * (KX[mask]*wyh[mask] - KY[mask]*wxh[mask]) / K2[mask]

    return ifftn3(uxhat), ifftn3(uyhat), ifftn3(uzhat)


def gradients_of_vector(vx, vy, vz, KX, KY, KZ):
    grad = {}
    for name, f in [("x", vx), ("y", vy), ("z", vz)]:
        grad[(name, "x")] = spectral_derivative(f, KX)
        grad[(name, "y")] = spectral_derivative(f, KY)
        grad[(name, "z")] = spectral_derivative(f, KZ)
    return grad


def strain_tensor_from_velocity(ux, uy, uz, KX, KY, KZ):
    g = gradients_of_vector(ux, uy, uz, KX, KY, KZ)
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


def divergence_of_vector(vx, vy, vz, KX, KY, KZ):
    return spectral_derivative(vx, KX) + spectral_derivative(vy, KY) + spectral_derivative(vz, KZ)


def curl_of_velocity(ux, uy, uz, KX, KY, KZ):
    wx = spectral_derivative(uz, KY) - spectral_derivative(uy, KZ)
    wy = spectral_derivative(ux, KZ) - spectral_derivative(uz, KX)
    wz = spectral_derivative(uy, KX) - spectral_derivative(ux, KY)
    return wx, wy, wz


def make_tilted_pair_vector_potential(
    X, Y, Z,
    R=0.40,
    sep_factor=0.70,
    pair_angle=0.0,
    twist_factor=1.20,
    imbalance=0.60,
    axial_coupling=0.50,
    phase=0.0,
    handedness=1.0,
    perturb_amp=0.0,
    perturb_seed=0,
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

    if perturb_amp > 0:
        rng = np.random.default_rng(int(perturb_seed))
        modes = [(1, 2, 1), (2, 1, 3), (3, 2, 1), (2, 3, 2)]
        pert = np.zeros_like(X)
        for mx, my, mz in modes:
            ph = rng.uniform(0, 2*np.pi)
            pert += np.sin(mx*X + my*Y + mz*Z + ph)
        pert /= max(np.max(np.abs(pert)), 1e-12)
        envelope = np.exp(-(X*X + Y*Y + Z*Z)/(2.0*(1.5*R)**2))
        ax = ax + perturb_amp * envelope * pert
        ay = ay + perturb_amp * envelope * np.roll(pert, shift=1, axis=0)
        az = az + perturb_amp * envelope * np.roll(pert, shift=1, axis=1)

    return ax, ay, az


def make_base_vorticity_from_params(params, grid):
    X, Y, Z, KX, KY, KZ, K2, dx = grid

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
        perturb_amp=params.get("perturb_amp", 0.0),
        perturb_seed=params.get("perturb_seed", 0),
    )

    wx, wy, wz = curl_from_vector_potential(ax, ay, az, KX, KY, KZ)
    wx, wy, wz = project_divergence_free_vector(wx, wy, wz, KX, KY, KZ, K2)

    mag = np.sqrt(wx*wx + wy*wy + wz*wz)
    max_mag = float(np.max(mag))
    if max_mag <= 0:
        raise RuntimeError("zero vorticity field")
    return wx/max_mag, wy/max_mag, wz/max_mag


def make_gate_mask(omega_sq, gate_mode="fixed_theta", theta_frac=0.7, top_k=64, top_fraction=0.001):
    flat = omega_sq.ravel()
    n_total = flat.size

    if gate_mode == "fixed_theta":
        threshold = float(theta_frac) * float(np.max(flat))
        mask = omega_sq >= threshold
        label = f"theta_{theta_frac:g}"

    elif gate_mode == "top_k":
        k = int(max(1, min(top_k, n_total)))
        # threshold by kth largest value
        kth = np.partition(flat, n_total - k)[n_total - k]
        mask = omega_sq >= kth
        label = f"topk_{k}"

    elif gate_mode == "top_fraction":
        k = int(max(1, min(round(top_fraction * n_total), n_total)))
        kth = np.partition(flat, n_total - k)[n_total - k]
        mask = omega_sq >= kth
        label = f"topfrac_{top_fraction:g}"

    else:
        raise ValueError(f"Unknown gate_mode: {gate_mode}")

    mask = np.asarray(mask, dtype=bool)
    return mask, label


def compute_gate_metrics(wx, wy, wz, grid, gate_mode="fixed_theta", theta_frac=0.7, top_k=64, top_fraction=0.001):
    X, Y, Z, KX, KY, KZ, K2, dx = grid
    dV = dx**3
    N = int(X.shape[0])

    ux, uy, uz = velocity_from_vorticity(wx, wy, wz, KX, KY, KZ, K2)
    S = strain_tensor_from_velocity(ux, uy, uz, KX, KY, KZ)
    stretch_density = omega_dot_S_omega(wx, wy, wz, S)

    omega_sq = wx*wx + wy*wy + wz*wz
    mask, gate_label = make_gate_mask(
        omega_sq,
        gate_mode=gate_mode,
        theta_frac=theta_frac,
        top_k=top_k,
        top_fraction=top_fraction,
    )

    if not np.any(mask):
        return None

    gw = gradients_of_vector(wx, wy, wz, KX, KY, KZ)
    gradomega_sq = np.zeros_like(wx)
    for val in gw.values():
        gradomega_sq += val*val

    u_sq = ux*ux + uy*uy + uz*uz

    kinetic_energy = 0.5 * float(np.sum(u_sq) * dV)
    enstrophy_total = float(np.sum(omega_sq) * dV)
    enstrophy_gate = float(np.sum(omega_sq[mask]) * dV)
    gradomega_gate = float(np.sum(gradomega_sq[mask]) * dV)

    stretch_gate = stretch_density[mask]
    positive = float(np.sum(np.maximum(stretch_gate, 0.0)) * dV)
    negative = float(np.sum(np.maximum(-stretch_gate, 0.0)) * dV)
    signed = positive - negative

    abs_total = positive + negative + 1e-300
    coherence = signed / abs_total

    curl_u = curl_of_velocity(ux, uy, uz, KX, KY, KZ)
    curl_error_sq = (curl_u[0]-wx)**2 + (curl_u[1]-wy)**2 + (curl_u[2]-wz)**2
    div_u = divergence_of_vector(ux, uy, uz, KX, KY, KZ)
    div_w = divergence_of_vector(wx, wy, wz, KX, KY, KZ)

    gate_cell_count = int(np.sum(mask))

    return {
        "gate_mode": gate_mode,
        "gate_label": gate_label,
        "theta_frac": float(theta_frac),
        "top_k_requested": int(top_k),
        "top_fraction_requested": float(top_fraction),
        "gate_cell_count": gate_cell_count,
        "gate_volume_fraction": float(gate_cell_count / mask.size),
        "gate_volume": float(gate_cell_count * dV),
        "kinetic_energy_base": kinetic_energy,
        "enstrophy_total_base": enstrophy_total,
        "enstrophy_gate_base": enstrophy_gate,
        "gate_enstrophy_fraction": enstrophy_gate / max(enstrophy_total, 1e-300),
        "gradomega_gate_base": gradomega_gate,
        "positive_stretch_gate_base": positive,
        "negative_stretch_gate_base": negative,
        "signed_stretch_gate_base": signed,
        "coherence_signed_over_abs": coherence,
        "curl_reconstruction_rel_error": float(np.sqrt(np.sum(curl_error_sq)*dV) / max(np.sqrt(np.sum(omega_sq)*dV), 1e-300)),
        "div_u_l2": float(np.sqrt(np.sum(div_u*div_u)*dV)),
        "div_omega_l2": float(np.sqrt(np.sum(div_w*div_w)*dV)),
    }


def energy_scaled_channel_rows(base_metrics, params, nu_values, Emax_values, chi_values, min_gate_cells_values):
    rows = []
    for min_gate_cells in min_gate_cells_values:
        gate_size_pass = bool(base_metrics["gate_cell_count"] >= int(min_gate_cells))
        for nu in nu_values:
            for Emax in Emax_values:
                for chi in chi_values:
                    scale = chi * np.sqrt(Emax / max(base_metrics["kinetic_energy_base"], 1e-300))

                    positive = scale**3 * base_metrics["positive_stretch_gate_base"]
                    negative = scale**3 * base_metrics["negative_stretch_gate_base"]
                    signed = positive - negative
                    dissipation = nu * scale**2 * base_metrics["gradomega_gate_base"]

                    theta_positive = positive / max(dissipation, 1e-300)
                    theta_signed = signed / max(dissipation, 1e-300)

                    row = dict(params)
                    row.update(base_metrics)
                    row.update({
                        "min_gate_cells": int(min_gate_cells),
                        "gate_size_pass": gate_size_pass,
                        "nu": float(nu),
                        "Emax": float(Emax),
                        "chi": float(chi),
                        "scale": float(scale),
                        "energy_fraction": float(chi*chi),
                        "theta_positive": float(theta_positive),
                        "theta_signed": float(theta_signed),
                        "channel_positive_open": bool(theta_positive > 1.0),
                        "channel_signed_open": bool(theta_signed > 1.0),
                        "robust_signed_open": bool((theta_signed > 1.0) and gate_size_pass and (base_metrics["coherence_signed_over_abs"] > 0.0)),
                    })
                    rows.append(row)
    return rows


def load_candidates():
    candidate_paths = [
        Path("/content/drive/MyDrive/BIG_B19_colab_outputs/B19_5_run_001/coherent_channel_robustness/B19_5_top_coherent_candidates_rebuilt_for_cell6.csv"),
        Path("/content/drive/MyDrive/BIG_B19_colab_outputs/B19_5_run_001/coherent_channel_robustness/B19_5_top_coherent_candidates.csv"),
        Path("/content/B19_5_run_001_coherent_channel_robustness/B19_5_top_coherent_candidates_rebuilt_for_cell6.csv"),
        Path("/content/B19_5_run_001_coherent_channel_robustness/B19_5_top_coherent_candidates.csv"),
    ]

    for p in candidate_paths:
        if p.exists():
            print("Loaded candidates from:", p)
            return pd.read_csv(p)

    print("B19.5 candidate CSV not found. Using embedded candidates.")
    data = [
        {"R":0.30,"sep_factor":0.70,"pair_angle":1.0471975511965976,"twist_factor":1.2,"imbalance":0.8,"axial_coupling":0.75,"phase":0.0,"handedness":-1.0,"theta_frac":0.7},
        {"R":0.30,"sep_factor":0.95,"pair_angle":1.0471975511965976,"twist_factor":0.8,"imbalance":0.8,"axial_coupling":0.75,"phase":0.0,"handedness":-1.0,"theta_frac":0.7},
        {"R":0.30,"sep_factor":0.70,"pair_angle":0.0,"twist_factor":0.8,"imbalance":0.6,"axial_coupling":0.75,"phase":0.7853981633974483,"handedness":1.0,"theta_frac":0.7},
        {"R":0.30,"sep_factor":0.70,"pair_angle":0.5235987755982988,"twist_factor":1.2,"imbalance":0.8,"axial_coupling":0.75,"phase":0.7853981633974483,"handedness":-1.0,"theta_frac":0.7},
        {"R":0.30,"sep_factor":0.70,"pair_angle":0.0,"twist_factor":0.8,"imbalance":0.8,"axial_coupling":0.75,"phase":0.7853981633974483,"handedness":1.0,"theta_frac":0.7},
        {"R":0.30,"sep_factor":0.95,"pair_angle":1.0471975511965976,"twist_factor":0.8,"imbalance":0.6,"axial_coupling":0.75,"phase":0.0,"handedness":-1.0,"theta_frac":0.7},
        {"R":0.40,"sep_factor":0.95,"pair_angle":0.5235987755982988,"twist_factor":0.8,"imbalance":0.8,"axial_coupling":0.25,"phase":1.5707963267948966,"handedness":-1.0,"theta_frac":0.7},
        {"R":0.55,"sep_factor":0.95,"pair_angle":0.5235987755982988,"twist_factor":0.8,"imbalance":0.8,"axial_coupling":0.25,"phase":1.5707963267948966,"handedness":-1.0,"theta_frac":0.7},
    ]
    return pd.DataFrame(data)
