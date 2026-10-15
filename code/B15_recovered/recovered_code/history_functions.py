def periodic_angle_distance(s, s0):
    return np.angle(np.exp(1j * (s - s0)))

def periodic_gaussian(s, s0, width):
    d = periodic_angle_distance(s, s0)
    return np.exp(-0.5 * (d / width) ** 2)

def ket_from_boundary_coordinate(s):
    """
    Projective real 2D embedding from boundary coordinate s.

    |psi_s> = cos(s/2)|+> + sin(s/2)|->

    The half-angle makes s and s+2pi correspond to the same projector.
    """
    theta = 0.5 * s
    return np.array([np.cos(theta), np.sin(theta)], dtype=float)

def projector_from_s(s):
    v = ket_from_boundary_coordinate(s)
    return np.outer(v, v)

def density_from_boundary_history(s, H):
    """
    rho_hist = integral w(s) |psi_s><psi_s| ds

    where

        w(s) = max(H(s),0) / integral max(H(s),0) ds

    This is a density-like representation of boundary history.
    It is not assumed to be a quantum state derived from physics.
    """
    s = np.asarray(s, dtype=float)
    H = np.asarray(H, dtype=float)

    Hpos = np.maximum(H, 0.0)
    ds = float(s[1] - s[0])

    total = float(np.sum(Hpos) * ds)

    if total <= 1e-15:
        Hpos = np.ones_like(Hpos)
        total = float(np.sum(Hpos) * ds)

    w = Hpos / total

    rho = np.zeros((2, 2), dtype=float)

    for si, wi in zip(s, w):
        rho += wi * projector_from_s(si) * ds

    rho = 0.5 * (rho + rho.T)

    tr = np.trace(rho)
    if abs(tr) <= 1e-15:
        rho = np.eye(2) / 2.0
    else:
        rho = rho / tr

    return rho, w

def purity(rho):
    return float(np.trace(rho @ rho))

def eig_entropy(rho, eps=1e-12):
    vals = np.linalg.eigvalsh(rho)
    vals = np.maximum(vals, eps)
    vals = vals / np.sum(vals)
    return float(-np.sum(vals * np.log(vals)))

def response_curve_from_rho(rho, alpha_grid):
    vals = []

    for alpha in alpha_grid:
        v = np.array([np.cos(alpha), np.sin(alpha)], dtype=float)
        P = np.outer(v, v)
        vals.append(float(np.trace(rho @ P)))

    return np.array(vals)

def circular_mean_angle(s, H):
    Hpos = np.maximum(H, 0.0)
    if np.sum(Hpos) <= 1e-15:
        return np.nan

    z = np.sum(Hpos * np.exp(1j * s)) / np.sum(Hpos)
    angle = np.angle(z)

    if angle < 0:
        angle += 2 * np.pi

    return float(angle)

def circular_resultant_length(s, H):
    Hpos = np.maximum(H, 0.0)
    if np.sum(Hpos) <= 1e-15:
        return 0.0

    z = np.sum(Hpos * np.exp(1j * s)) / np.sum(Hpos)
    return float(np.abs(z))
