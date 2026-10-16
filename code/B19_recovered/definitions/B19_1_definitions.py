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


def channel_ratio_energy_cap(R, s, nu=0.01, Emax=1.0, c_ell=0.5, R_floor=1e-6):
    """
    Maximum stretching/leakage ratio under finite core-energy cap.

    stretching/leakage ~ A*ell^2/nu.
    Under A <= sqrt(Emax) R^(-5/2):
        ratio_max ~ sqrt(Emax) c_ell^2 R^(2s-5/2) / nu.
    """
    R = np.maximum(np.asarray(R, dtype=float), R_floor)
    Amax = np.sqrt(Emax) * R ** (-2.5)
    ell = c_ell * R ** s
    ratio = Amax * ell * ell / max(nu, 1e-30)
    return ratio


def simulate_energy_constrained_core(params):
    T = float(params.get("T", 4.0))
    dt = float(params.get("dt", 1e-3))
    n = int(round(T / dt))

    nu = float(params.get("nu", 0.01))
    Emax = float(params.get("Emax", 1.0))
    s = float(params.get("s", 1.0))
    c_ell = float(params.get("c_ell", 0.5))
    ell_floor = float(params.get("ell_floor", 1e-5))
    R_floor = float(params.get("R_floor", 1e-5))

    cs = float(params.get("cs", 0.6))
    cd = float(params.get("cd", 1.0))
    cR = float(params.get("cR", 0.25))
    cnu = float(params.get("cnu", 0.01))
    beta = float(params.get("beta", 0.04))
    alpha = float(params.get("alpha", 0.10))
    m_gain = float(params.get("m_gain", 0.5))

    A = float(params.get("A0", 1.0))
    R = float(params.get("R0", 1.0))
    M = float(params.get("M0", 0.0))

    rows = []

    for i in range(n + 1):
        t = i * dt
        R_eff = max(R, R_floor)
        ell = max(ell_floor, c_ell * (R_eff ** s))
        Amax = np.sqrt(Emax) * (R_eff ** (-2.5))
        if A > Amax:
            A = Amax

        core_energy = A*A*(R_eff**5)
        enstrophy = A*A*(R_eff**3)
        interface_measure = R_eff**2
        boundary_exposure = A*A*interface_measure*ell

        rho = A*ell*ell / max(nu, 1e-30)
        readable_boost = 1.0 + m_gain * M / (1.0 + M)

        stretching = cs * A*A * readable_boost
        leakage = cd * nu * A / (ell*ell)

        # Smooth contraction only when rho > 1.
        H = max(0.0, (rho - 1.0) / (rho + 1.0))
        contraction = cR * R_eff * H
        diffusion_expansion = cnu * nu / ell

        dA = stretching - leakage
        dR = -contraction + diffusion_expansion
        dM = beta * boundary_exposure - alpha * M

        rows.append({
            "t": float(t),
            "A": float(A),
            "Amax_energy": float(Amax),
            "R": float(R_eff),
            "ell": float(ell),
            "M": float(M),
            "rho_stretch_leak": float(rho),
            "readable_boost": float(readable_boost),
            "stretching": float(stretching),
            "leakage": float(leakage),
            "stretch_minus_leakage": float(stretching - leakage),
            "core_energy": float(core_energy),
            "enstrophy": float(enstrophy),
            "boundary_exposure": float(boundary_exposure),
            "contraction": float(contraction),
            "diffusion_expansion": float(diffusion_expansion),
        })

        if i == n:
            break

        A = max(0.0, A + dt*dA)
        R = max(R_floor, R + dt*dR)
        M = max(0.0, M + dt*dM)

        # Explicit finite-energy projection.
        R_eff_next = max(R, R_floor)
        Amax_next = np.sqrt(Emax) * (R_eff_next ** (-2.5))
        A = min(A, Amax_next)

    df = pd.DataFrame(rows)

    info = {
        "T": T,
        "dt": dt,
        "nu": nu,
        "Emax": Emax,
        "s": s,
        "c_ell": c_ell,
        "cs": cs,
        "cd": cd,
        "cR": cR,
        "cnu": cnu,
        "beta": beta,
        "alpha": alpha,
        "m_gain": m_gain,
        "A0": float(params.get("A0", 1.0)),
        "R0": float(params.get("R0", 1.0)),
        "M0": float(params.get("M0", 0.0)),
        "A_final": float(df["A"].iloc[-1]),
        "R_final": float(df["R"].iloc[-1]),
        "M_final": float(df["M"].iloc[-1]),
        "min_R": float(df["R"].min()),
        "max_A": float(df["A"].max()),
        "max_rho": float(df["rho_stretch_leak"].max()),
        "median_rho": float(df["rho_stretch_leak"].median()),
        "fraction_rho_gt_1": float((df["rho_stretch_leak"] > 1.0).mean()),
        "max_core_energy": float(df["core_energy"].max()),
        "max_enstrophy": float(df["enstrophy"].max()),
        "energy_constraint_violation": float(max(0.0, df["core_energy"].max() - Emax)),
        "net_radius_shrinkage": float(df["R"].iloc[0] - df["R"].iloc[-1]),
        "channel_class": "open" if (df["rho_stretch_leak"] > 1.0).mean() > 0.8 else ("intermittent" if (df["rho_stretch_leak"] > 1.0).mean() > 0.2 else "closed"),
    }

    return df, info
