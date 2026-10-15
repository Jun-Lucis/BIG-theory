def periodic_angle_distance(s, s0):
    return np.angle(np.exp(1j * (s - s0)))

def periodic_gaussian(s, s0, width):
    d = periodic_angle_distance(s, s0)
    return np.exp(-0.5 * (d / width) ** 2)

def L2_norm(x, ds):
    x = np.asarray(x, dtype=float)
    return float(np.sqrt(np.sum(x * x) * ds))

def heat_smooth_fft(H, s, tau=0.002):
    """
    Periodic heat smoothing.
    This is linear in H when tau is fixed.
    """
    H = np.asarray(H, dtype=float)
    ds = float(s[1] - s[0])
    N = len(s)

    freqs = np.fft.fftfreq(N, d=ds)
    k = 2.0 * np.pi * freqs

    return np.real(np.fft.ifft(np.fft.fft(H) * np.exp(-(k ** 2) * tau)))

def fixed_forgetting_map(H, s, decay=0.9, tau=0.002):
    """
    Linear map:
        H -> decay * heat_smooth(H)
    """
    return decay * heat_smooth_fft(H, s, tau=tau)

def writing_with_fixed_stimulus_map(H, s, stimulus, decay=0.9, beta=0.2, tau=0.002):
    """
    Affine map in H when stimulus is fixed:
        H -> decay*smooth(H) + beta*stimulus
    """
    return decay * heat_smooth_fft(H, s, tau=tau) + beta * stimulus

def division_fixed_partition_map(H, s, cut_angle=np.deg2rad(80.0), sharpness=8.0):
    """
    Linear map from one profile to two daughter profiles:
        H -> [mask1*H, mask2*H]
    """
    x = np.cos(s - cut_angle)
    mask1 = 1.0 / (1.0 + np.exp(-sharpness * x))
    mask2 = 1.0 - mask1
    return np.concatenate([mask1 * H, mask2 * H])

def division_leaky_fixed_partition_map(
    H,
    s,
    cut_angle=np.deg2rad(80.0),
    sharpness=8.0,
    efficiency=0.96,
    leakage=0.04,
):
    """
    Still linear if masks, efficiency, leakage are fixed and no clipping/noise is used.
    """
    x = np.cos(s - cut_angle)
    mask1 = 1.0 / (1.0 + np.exp(-sharpness * x))
    mask2 = 1.0 - mask1

    D1 = efficiency * mask1 * H + leakage * mask2 * H
    D2 = efficiency * mask2 * H + leakage * mask1 * H

    return np.concatenate([D1, D2])

def normalization_map(H, s):
    """
    Nonlinear due to normalization by integral.
    """
    Hpos = np.maximum(np.asarray(H, dtype=float), 0.0)
    ds = float(s[1] - s[0])

    total = float(np.sum(Hpos) * ds)

    if total <= 1e-15:
        return Hpos

    return Hpos / total

def fusion_addition_map(pair, s):
    """
    Linear in the joint pair:
        (A,B) -> A+B
    """
    A, B = pair
    return A + B

def fusion_compression_map(pair, s, compression_gamma=0.35, conflict_gamma=0.50):
    """
    Nonlinear fusion compression:
        (A,B) -> compressed(A+B)

    Local compression depends on overlap A*B.
    Global compression depends on normalized overlap <A,B>/(||A||||B||).
    """
    A, B = pair
    ds = float(s[1] - s[0])

    raw = A + B
    scale = max(float(np.max(raw)), 1e-12)

    conflict = (A * B) / (scale ** 2 + 1e-12)
    local_factor = np.exp(-conflict_gamma * conflict)

    C = raw * local_factor

    numerator = float(np.sum(A * B) * ds)
    denominator = L2_norm(A, ds) * L2_norm(B, ds)

    if denominator <= 1e-12:
        overlap = 0.0
    else:
        overlap = max(0.0, numerator / denominator)

    compression_factor = 1.0 - compression_gamma * overlap

    return C * compression_factor

def linearity_test_unary(name, f, x, y, grid_for_norm, lam=1.7):
    """
    Test:
        additivity:   f(x+y) ?= f(x)+f(y)
        homogeneity:  f(lam*x) ?= lam*f(x)
    """
    ds = float(grid_for_norm[1] - grid_for_norm[0])

    fx = f(x)
    fy = f(y)
    fxy = f(x + y)
    flx = f(lam * x)

    add_err = L2_norm(fxy - fx - fy, ds) / (L2_norm(fxy, ds) + 1e-12)
    hom_err = L2_norm(flx - lam * fx, ds) / (L2_norm(flx, ds) + 1e-12)

    return {
        "map_name": name,
        "map_kind": "unary",
        "additivity_error": float(add_err),
        "homogeneity_error": float(hom_err),
        "linearity_score": float(add_err + hom_err),
    }

def affine_test_unary(name, f, x, y, grid_for_norm, lam=1.7):
    """
    Some maps are affine:
        f(H) = L(H) + b

    For affine maps, the translated map g(H)=f(H)-f(0) should be linear.
    """
    zero = np.zeros_like(x)
    f0 = f(zero)

    def g(H):
        return f(H) - f0

    result = linearity_test_unary(name + "_after_subtracting_f0", g, x, y, grid_for_norm, lam=lam)

    return {
        "map_name": name,
        "map_kind": "unary_affine_test",
        "f0_norm": L2_norm(f0, float(grid_for_norm[1] - grid_for_norm[0])),
        "affine_additivity_error": result["additivity_error"],
        "affine_homogeneity_error": result["homogeneity_error"],
        "affinity_score": result["linearity_score"],
    }

def linearity_test_binary(name, g, A1, B1, A2, B2, s, lam=1.7):
    """
    Treat binary map as a map on joint pair:
        G(A,B)

    Test:
        G((A1,B1)+(A2,B2)) ?= G(A1,B1)+G(A2,B2)
        G(lam*(A1,B1)) ?= lam*G(A1,B1)
    """
    ds = float(s[1] - s[0])

    g1 = g((A1, B1))
    g2 = g((A2, B2))
    gsum = g((A1 + A2, B1 + B2))
    glam = g((lam * A1, lam * B1))

    add_err = L2_norm(gsum - g1 - g2, ds) / (L2_norm(gsum, ds) + 1e-12)
    hom_err = L2_norm(glam - lam * g1, ds) / (L2_norm(glam, ds) + 1e-12)

    return {
        "map_name": name,
        "map_kind": "binary",
        "additivity_error": float(add_err),
        "homogeneity_error": float(hom_err),
        "linearity_score": float(add_err + hom_err),
    }

def classify_from_scores(linearity_score, affinity_score=None):
    if linearity_score < 1e-10:
        return "linear"

    if affinity_score is not None and affinity_score < 1e-10:
        return "affine"

    if linearity_score < 1e-3:
        return "approximately linear"

    if affinity_score is not None and affinity_score < 1e-3:
        return "approximately affine"

    if linearity_score < 0.15:
        return "weakly nonlinear"

    return "nonlinear"
