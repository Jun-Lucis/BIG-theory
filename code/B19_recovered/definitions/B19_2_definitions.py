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


def rho_max_energy_cap(R, s, nu=0.01, Emax=1.0, c_ell=0.5, chi=1.0):
    R = np.maximum(np.asarray(R, dtype=float), 1e-300)
    Amax = np.sqrt(Emax) * R**(-2.5)
    ell = c_ell * R**s
    return chi * Amax * ell**2 / max(nu, 1e-300)


def critical_radius(s, nu=0.01, Emax=1.0, c_ell=0.5, chi=1.0):
    C = chi * np.sqrt(Emax) * c_ell**2 / max(nu, 1e-300)
    a = 2.0*s - 2.5
    if abs(a) < 1e-12:
        return np.nan
    return C**(-1.0/a)


def prescribed_path(params):
    T = float(params.get("T", 1.0))
    n = int(params.get("n", 1200))
    R0 = float(params.get("R0", 1.0))
    Rend = float(params.get("Rend", 1e-5))
    q_path = float(params.get("q_path", 1.0))
    s = float(params.get("s", 1.0))
    nu = float(params.get("nu", 0.01))
    Emax = float(params.get("Emax", 1.0))
    c_ell = float(params.get("c_ell", 0.5))
    chi = float(params.get("chi", 1.0))

    t = np.linspace(0.0, T, n+1)
    tau = np.maximum(0.0, 1.0 - t/T)
    R = Rend + (R0 - Rend) * tau**q_path

    Amax = np.sqrt(Emax) * R**(-2.5)
    A = chi * Amax
    ell = c_ell * R**s
    rho = A * ell**2 / max(nu, 1e-300)

    core_energy = A*A*R**5
    enstrophy = A*A*R**3

    df = pd.DataFrame({
        "t": t,
        "R": R,
        "A": A,
        "ell": ell,
        "rho": rho,
        "core_energy": core_energy,
        "enstrophy": enstrophy,
    })

    open_mask = np.asarray(rho > 1.0, dtype=bool)
    open_start_value = bool(open_mask[0])
    open_end_value = bool(open_mask[-1])
    closed_after_open = bool(open_start_value and (not open_end_value))
    opened_after_closed = bool((not open_start_value) and open_end_value)
    min_rho = float(np.min(rho))
    max_rho = float(np.max(rho))

    info = {
        **params,
        "rho_start": float(rho[0]),
        "rho_end": float(rho[-1]),
        "rho_end_over_start": float(rho[-1] / rho[0]) if rho[0] != 0 else np.nan,
        "min_rho": min_rho,
        "max_rho": max_rho,
        "fraction_open": float(np.mean(open_mask)),
        "open_start": open_start_value,
        "open_end": open_end_value,
        "closed_after_open": closed_after_open,
        "opened_after_closed": opened_after_closed,
        "max_enstrophy": float(np.max(enstrophy)),
        "energy_max_observed": float(np.max(core_energy)),
    }
    return df, info
