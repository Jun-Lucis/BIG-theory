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
    """
    Periodic Biot--Savart reconstruction:
        u_hat = i (k x omega_hat) / |k|^2
    """
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


def strain_frobenius(S):
    Sxx, Syy, Szz, Sxy, Sxz, Syz = S
    return np.sqrt(Sxx*Sxx + Syy*Syy + Szz*Szz + 2*Sxy*Sxy + 2*Sxz*Sxz + 2*Syz*Syz)


def divergence_of_vector(vx, vy, vz, KX, KY, KZ):
    return spectral_derivative(vx, KX) + spectral_derivative(vy, KY) + spectral_derivative(vz, KZ)


def curl_of_velocity(ux, uy, uz, KX, KY, KZ):
    wx = spectral_derivative(uz, KY) - spectral_derivative(uy, KZ)
    wy = spectral_derivative(ux, KZ) - spectral_derivative(uz, KX)
    wz = spectral_derivative(uy, KX) - spectral_derivative(ux, KY)
    return wx, wy, wz


def make_vector_potential_family(family, R, X, Y, Z, L):
    r2 = X*X + Y*Y + Z*Z
    rho2 = X*X + Y*Y
    eps = 1e-12

    if family == "column_2d":
        # z-independent vector potential. This is a near-2D test case
        # where true vortex stretching should be weak.
        G = np.exp(-rho2/(2.0*R*R))
        ax = np.zeros_like(G)
        ay = np.zeros_like(G)
        az = G

    elif family == "localized_3d":
        G = np.exp(-r2/(2.0*R*R))
        k = 2.0 / max(R, eps)
        ax = 0.65 * G * np.sin(k*Z)
        ay = 0.45 * G * np.cos(k*X)
        az = 0.35 * G * np.sin(k*Y + 0.5*k*Z)

    elif family == "helical_3d":
        G = np.exp(-r2/(2.0*R*R))
        k = 1.5 / max(R, eps)
        ax = G * np.cos(k*Z)
        ay = G * np.sin(k*Z)
        az = 0.4 * G * np.cos(k*X - k*Y)

    else:
        raise ValueError(f"Unknown family: {family}")

    return ax, ay, az


def make_base_vorticity(family, R, grid):
    X, Y, Z, KX, KY, KZ, K2, dx = grid
    L = dx * X.shape[0]
    ax, ay, az = make_vector_potential_family(family, R, X, Y, Z, L)
    wx, wy, wz = curl_from_vector_potential(ax, ay, az, KX, KY, KZ)

    # Enforce divergence-free and remove mean.
    wx, wy, wz = project_divergence_free_vector(wx, wy, wz, KX, KY, KZ, K2)

    mag = np.sqrt(wx*wx + wy*wy + wz*wz)
    max_mag = float(np.max(mag))
    if max_mag <= 0:
        raise RuntimeError("zero vorticity field")

    # Normalize max |omega| to 1 for the base shape.
    wx, wy, wz = wx/max_mag, wy/max_mag, wz/max_mag
    return wx, wy, wz


def compute_base_metrics(wx, wy, wz, grid):
    X, Y, Z, KX, KY, KZ, K2, dx = grid
    dV = dx**3

    ux, uy, uz = velocity_from_vorticity(wx, wy, wz, KX, KY, KZ, K2)
    S = strain_tensor_from_velocity(ux, uy, uz, KX, KY, KZ)
    stretch_density = omega_dot_S_omega(wx, wy, wz, S)
    strain_mag = strain_frobenius(S)

    gw = gradients_of_vector(wx, wy, wz, KX, KY, KZ)
    gradomega_sq = np.zeros_like(wx)
    for val in gw.values():
        gradomega_sq += val*val

    omega_sq = wx*wx + wy*wy + wz*wz
    u_sq = ux*ux + uy*uy + uz*uz

    curl_u = curl_of_velocity(ux, uy, uz, KX, KY, KZ)
    curl_error_sq = (
        (curl_u[0]-wx)**2 + (curl_u[1]-wy)**2 + (curl_u[2]-wz)**2
    )
    div_u = divergence_of_vector(ux, uy, uz, KX, KY, KZ)
    div_w = divergence_of_vector(wx, wy, wz, KX, KY, KZ)

    # Weighted alignment proxy: compares positive stretching against |S||omega|^2.
    denom_align = float(np.sum(strain_mag * omega_sq) * dV)
    positive_stretch = float(np.sum(np.maximum(stretch_density, 0.0)) * dV)
    signed_stretch = float(np.sum(stretch_density) * dV)

    return {
        "kinetic_energy_base": float(0.5*np.sum(u_sq)*dV),
        "enstrophy_base": float(np.sum(omega_sq)*dV),
        "gradomega_integral_base": float(np.sum(gradomega_sq)*dV),
        "positive_stretch_base": positive_stretch,
        "signed_stretch_base": signed_stretch,
        "max_strain_base": float(np.max(strain_mag)),
        "weighted_alignment_base": float(positive_stretch / denom_align) if denom_align > 0 else np.nan,
        "curl_reconstruction_rel_error": float(np.sqrt(np.sum(curl_error_sq)*dV) / max(np.sqrt(np.sum(omega_sq)*dV), 1e-30)),
        "div_u_l2": float(np.sqrt(np.sum(div_u*div_u)*dV)),
        "div_omega_l2": float(np.sqrt(np.sum(div_w*div_w)*dV)),
    }
