# Extracted definitions only. Function bodies unchanged; no notebook top-level execution.

def to_jsonable(obj):
    if isinstance(obj, dict): return {str(k): to_jsonable(v) for k,v in obj.items()}
    if isinstance(obj, list): return [to_jsonable(v) for v in obj]
    if isinstance(obj, tuple): return [to_jsonable(v) for v in obj]
    if isinstance(obj, np.ndarray): return obj.tolist()
    if isinstance(obj, np.integer): return int(obj)
    if isinstance(obj, np.floating): return float(obj)
    if isinstance(obj, np.bool_): return bool(obj)
    return obj


def backup_to_drive(path):
    path = Path(path)
    try:
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)
        dst = BACKUP_DIR / path.name
        shutil.copy2(path, dst)
        print('Saved to Drive:', dst)
    except Exception as e:
        print('Drive backup failed:', e)


def save_csv(df, filename):
    path = OUTDIR / filename
    df.to_csv(path, index=False)
    print('Saved local:', path)
    backup_to_drive(path)
    return path


def save_json(obj, filename):
    path = OUTDIR / filename
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(to_jsonable(obj), f, indent=2, ensure_ascii=False)
    print('Saved local:', path)
    backup_to_drive(path)
    return path


def save_figure(filename, dpi=180):
    path = OUTDIR / filename
    plt.tight_layout()
    plt.savefig(path, dpi=dpi)
    print('Saved local:', path)
    backup_to_drive(path)
    plt.show()
    plt.close()
    return path


def classify_scaling(p, q, s):
    finite_core_energy = (2.0*p <= 5.0*q)
    enstrophy_blowup = (2.0*p > 3.0*q)
    stretching_dominates_leakage = (p > 2.0*q*s)
    return {
        'finite_core_energy': bool(finite_core_energy),
        'enstrophy_blowup': bool(enstrophy_blowup),
        'stretching_dominates_leakage': bool(stretching_dominates_leakage),
        'compatible_window': bool(finite_core_energy and enstrophy_blowup and stretching_dominates_leakage),
        'exponent_core_energy': float(-2.0*p + 5.0*q),
        'exponent_enstrophy': float(-2.0*p + 3.0*q),
        'stretch_minus_leakage_dominance': float((2.0*p) - (p + 2.0*q*s)),
    }


def simulate_core_ode(params):
    T=float(params.get('T',3.0)); dt=float(params.get('dt',1e-3)); n=int(round(T/dt))
    nu=float(params.get('nu',0.01)); cs=float(params.get('cs',1.0)); cd=float(params.get('cd',1.0))
    cc=float(params.get('cc',0.35)); cnu=float(params.get('cnu',0.02))
    beta=float(params.get('beta',0.16)); alpha=float(params.get('alpha',0.10)); m_gain=float(params.get('m_gain',0.8))
    ell_coeff=float(params.get('ell_coeff',0.45)); ell_floor=float(params.get('ell_floor',1e-3)); R_floor=float(params.get('R_floor',1e-3))
    s=float(params.get('s',1.0)); A=float(params.get('A0',1.0)); R=float(params.get('R0',1.0)); M=float(params.get('M0',0.0))
    rows=[]; blowup_flag=False
    for i in range(n+1):
        t=i*dt; R_safe=max(R,R_floor); ell=max(ell_floor, ell_coeff*(R_safe**s))
        core_volume=R_safe**3; interface_measure=R_safe**2
        enstrophy_core=A*A*core_volume; kinetic_core=A*A*(R_safe**5)
        boundary_exposure=A*A*interface_measure*ell
        readable_boost=1.0+m_gain*M/(1.0+M)
        stretching=cs*A*A*readable_boost
        leakage=cd*nu*A/(ell*ell)
        dA=stretching-leakage
        contraction=cc*R_safe*(readable_boost-1.0)/readable_boost
        diffusion_expansion=cnu*nu/max(ell,ell_floor)
        dR=-contraction+diffusion_expansion
        dM=beta*boundary_exposure-alpha*M
        rows.append({'t':t,'A':A,'R':R,'ell':ell,'M':M,'readable_boost':readable_boost,'stretching':stretching,'leakage':leakage,'stretch_minus_leakage':stretching-leakage,'enstrophy_core':enstrophy_core,'kinetic_core':kinetic_core,'boundary_exposure':boundary_exposure})
        if i==n: break
        A=max(A+dt*dA,0.0); R=max(R+dt*dR,R_floor); M=max(M+dt*dM,0.0)
        if A>params.get('A_blowup_threshold',1e4):
            blowup_flag=True; break
    df=pd.DataFrame(rows)
    return df, {'blowup_flag':bool(blowup_flag),'t_end':float(df['t'].iloc[-1]),'A_final':float(df['A'].iloc[-1]),'R_final':float(df['R'].iloc[-1]),'M_final':float(df['M'].iloc[-1]),'max_A':float(df['A'].max()),'max_enstrophy_core':float(df['enstrophy_core'].max()),'max_kinetic_core':float(df['kinetic_core'].max()),'min_R':float(df['R'].min()),'final_stretch_minus_leakage':float(df['stretch_minus_leakage'].iloc[-1])}
