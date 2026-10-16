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
        try:
            if path.resolve() == dst.resolve():
                print("Already on Drive:", dst)
                return
        except Exception:
            pass
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

    kmax = np.max(np.abs(k1))
    cutoff = (2.0/3.0) * kmax
    dealias = (np.abs(KX) <= cutoff) & (np.abs(KY) <= cutoff) & (np.abs(KZ) <= cutoff)

    return {
        "N": int(N),
        "L": float(L),
        "dx": float(dx),
        "X": X, "Y": Y, "Z": Z,
        "KX": KX, "KY": KY, "KZ": KZ,
        "K2": K2,
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
        "coherence_gate": signed_gate / max(pos_gate + neg_gate, 1e-300),
        "max_omega": float(np.max(np.sqrt(omega_sq))),
        "max_u": float(np.max(np.sqrt(u_sq))),
        "div_omega_l2": float(np.sqrt(np.sum(divw*divw) * dV)),
    }


def vorticity_rhs(wx, wy, wz, grid, nu):
    ux, uy, uz = velocity_from_vorticity(wx, wy, wz, grid)

    # u x omega
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


def estimate_Ecrit_same_geometry(stretch_total, dissipation_total, Emax):
    if stretch_total <= 0 or dissipation_total <= 0:
        return np.inf
    return float(Emax * (dissipation_total / stretch_total)**2)
