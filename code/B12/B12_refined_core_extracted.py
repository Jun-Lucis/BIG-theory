"""B12 refined core recovered by static extraction on 2026-10-15.
Pure function bodies copied from Untitled65.ipynb (Drive 1pvE787dKmTanQA6yi4PgST2_M16sxhza),
zero-based cells 0 and 16. Imports and version constants below are packaging additions.
No trajectory runs on import. Exact historical cells and provenance accompany this file.
The recovered code, parameters and data support reproduction in principle; the independent rerun audit is not yet complete.
"""
import math
import numpy as np
import pandas as pd
CODE_VERSION_B12D = "B12.1d_R_ignition_barrier_finite_noise_window_v1"
CODE_SHA16_B12D = "fae029d1ec8a101c"

def sigmoid(x):
    x = np.clip(x, -60, 60)
    return 1.0 / (1.0 + np.exp(-x))

def normalize(v, eps=1e-12):
    v = np.asarray(v, dtype=float)
    n = np.linalg.norm(v)
    if n < eps:
        return v * 0.0
    return v / n

def cosine(u, v, eps=1e-12):
    u = np.asarray(u, dtype=float)
    v = np.asarray(v, dtype=float)
    nu = np.linalg.norm(u)
    nv = np.linalg.norm(v)
    if nu < eps or nv < eps:
        return 0.0
    return float(np.dot(u, v) / (nu * nv))

def make_correlated_pair(N, rho, rng):
    """
    Parent hidden memories a,b in R^N with cosine approximately rho.
    """
    a = normalize(rng.normal(size=N))
    z = rng.normal(size=N)
    z = z - np.dot(z, a) * a
    z = normalize(z)
    b = rho * a + math.sqrt(max(0.0, 1.0 - rho**2)) * z
    return normalize(a), normalize(b)

def extended_templates(a, b):
    """
    h-space = R^{2N}.
    A memory occupies first sector.
    B memory occupies second sector.
    Inheritance occupies both sectors.
    """
    N = len(a)
    A = normalize(np.concatenate([a, np.zeros(N)]))
    B = normalize(np.concatenate([np.zeros(N), b]))
    I = normalize(np.concatenate([a, b]))
    return A, B, I

def sector_stats(h, a, b, eps=1e-12):
    N = len(a)
    hA = h[:N]
    hB = h[N:]

    nA = float(np.linalg.norm(hA))
    nB = float(np.linalg.norm(hB))
    balance = min(nA, nB) / (max(nA, nB) + eps)

    M_A = cosine(hA, a)
    M_B = cosine(hB, b)

    return hA, hB, nA, nB, balance, M_A, M_B

def post_energy_grad(h, templates, rho, amp_I_eff, p):
    """
    B11-like hidden-depth landscape:
      A assimilation well
      B assimilation well
      inheritance well, activated by R-lock
      folding conflict
      weak confinement

    amp_I_eff is dynamic:
      amp_I_eff = amp_I * G_lock
    """
    A, B, I, E = templates

    N2 = len(h)
    N = N2 // 2
    hA = h[:N]
    hB = h[N:]

    width = p["h_well_width"]
    width2 = width**2

    k_loss = p["h_k_loss"]
    k_quartic = p["h_k_quartic"]
    k_conflict = p["h_k_conflict"]

    amp_A = p["h_amp_A"]
    amp_B = p["h_amp_B"]
    amp_E = p["h_amp_E"]

    norm2 = float(np.dot(h, h))

    U = 0.5 * k_loss * norm2 + 0.25 * k_quartic * norm2**2
    grad = k_loss * h.copy() + k_quartic * norm2 * h

    # Folding conflict
    nA2 = float(np.dot(hA, hA))
    nB2 = float(np.dot(hB, hB))
    conflict_strength = k_conflict * max(0.0, 1.0 - rho)

    U_conflict = conflict_strength * nA2 * nB2
    U += U_conflict

    grad[:N] += 2.0 * conflict_strength * nB2 * hA
    grad[N:] += 2.0 * conflict_strength * nA2 * hB

    # Gaussian wells
    for amp, T in [
        (amp_A, A),
        (amp_B, B),
        (amp_I_eff, I),
        (amp_E, E),
    ]:
        if amp == 0:
            continue

        diff = h - T
        d2 = float(np.dot(diff, diff))
        e = math.exp(-d2 / (2.0 * width2))

        U += -amp * e
        grad += amp * e * diff / width2

    return U, grad, U_conflict

def classify_h(h, a, b, templates, p):
    A, B, I, E = templates
    hA, hB, nA, nB, balance, M_A, M_B = sector_stats(h, a, b)

    sim_A = cosine(h, A)
    sim_B = cosine(h, B)
    sim_I = cosine(h, I)
    sim_E = cosine(h, E)
    norm_h = float(np.linalg.norm(h))

    if norm_h < p["h_annihilation_norm"]:
        outcome = "annihilation"

    elif sim_A > p["h_assim_sim_threshold"] and nB < p["h_sector_absent_threshold"]:
        outcome = "A_assimilation"

    elif sim_B > p["h_assim_sim_threshold"] and nA < p["h_sector_absent_threshold"]:
        outcome = "B_assimilation"

    elif (
        M_A > p["h_memory_threshold"]
        and M_B > p["h_memory_threshold"]
        and balance > p["h_balance_threshold"]
        and sim_I > p["h_inheritance_sim_threshold"]
    ):
        outcome = "inheritance"

    elif (
        norm_h >= p["h_annihilation_norm"]
        and max(sim_A, sim_B, sim_I) < p["h_emergent_max_parent_sim"]
        and sim_E > p["h_emergent_sim_threshold"]
    ):
        outcome = "emergent"

    else:
        outcome = "mixed"

    return {
        "h_outcome": outcome,
        "M_A": M_A,
        "M_B": M_B,
        "sim_A": sim_A,
        "sim_B": sim_B,
        "sim_I": sim_I,
        "sim_E": sim_E,
        "nA": nA,
        "nB": nB,
        "balance": balance,
        "norm_h": norm_h,
    }

def make_initial_h(init_mode, A, B, I, rng, p):
    N2 = len(I)
    init_norm = p["h_init_norm"]
    noise = p["h_init_noise"]

    if init_mode == "neutral_mix":
        ca = max(0.0, 1.0 + p["h_mix_spread"] * rng.normal())
        cb = max(0.0, 1.0 + p["h_mix_spread"] * rng.normal())
        h0 = ca * A + cb * B
        h = init_norm * normalize(h0) + noise * rng.normal(size=N2)

    elif init_mode == "A_seed":
        h = init_norm * A + noise * rng.normal(size=N2)

    elif init_mode == "B_seed":
        h = init_norm * B + noise * rng.normal(size=N2)

    elif init_mode == "random":
        h = init_norm * normalize(rng.normal(size=N2)) + noise * rng.normal(size=N2)

    else:
        raise ValueError(f"Unknown init_mode: {init_mode}")

    return h.astype(float)

def simulate_unified_one_B12_1d(seed, rho, amp_I, sigma_R, p_config, keep_trace=False):
    """
    B12.1d trajectory with R ignition barrier.

    Main modification:
      R growth is gated by an ignition threshold.

      dR ~ A_R * F_prox * S(R - R_ignite) * (1 - R)
           - H_R R
           - noise_decoh

    This prevents deterministic low-noise lock unless R crosses the ignition
    threshold through stochastic fluctuation.
    """
    rng = np.random.default_rng(seed)

    N = int(p_config["N"])

    # Parent memories
    a, b = make_correlated_pair(N, rho, rng)
    A, B, I = extended_templates(a, b)

    E = rng.normal(size=2 * N)
    for T in [A, B, I]:
        E = E - np.dot(E, T) * T
    E = E / (np.linalg.norm(E) + 1e-12)

    templates = (A, B, I, E)

    # Initial state
    d = float(p_config["d0"])
    R = np.clip(
        p_config["R_init"] + p_config["R_init_noise"] * rng.normal(size=N),
        0.0,
        1.0,
    )
    h = make_initial_h(p_config["h_init_mode"], A, B, I, rng, p_config)

    dt = float(p_config["dt"])
    steps = int(float(p_config["T"]) / dt)

    # Event trackers
    hit = False
    hit_time = np.nan

    first_lock_event = False
    first_lock_time = np.nan

    max_consecutive_lock_steps = 0
    current_consecutive_lock_steps = 0

    post_hit_steps = 0
    post_hit_lock_steps = 0

    final_window_steps = int(float(p_config.get("T_final_lock_hold", 5.0)) / dt)
    final_lock_buffer = []

    inherited_during_lock = False
    inheritance_time = np.nan

    max_R_score = 0.0
    max_R_component = 0.0
    min_d = d
    max_G_lock = 0.0
    max_ignite_gate_mean = 0.0

    U_h0, _, Uconf0 = post_energy_grad(
        h, templates, rho=rho, amp_I_eff=0.0, p=p_config
    )

    trace = []

    for step in range(steps):
        t = step * dt

        # ----------------------------------------------------
        # Boundary proximity
        # ----------------------------------------------------
        F_prox = sigmoid((p_config["d_int"] - d) / p_config["ell_d"])

        if t < p_config["t_pass"]:
            v_protocol = -p_config["v_in"]
        else:
            v_protocol = p_config["v_out"]

        # ----------------------------------------------------
        # Resonance gates
        # ----------------------------------------------------
        R_score = float(np.mean(R))
        max_R_score = max(max_R_score, R_score)
        max_R_component = max(max_R_component, float(np.max(R)))

        G_R_open = sigmoid((R_score - p_config["R_gate"]) / p_config["ell_R_gate"])

        G_lock_R = math.exp(
            -((R_score - p_config["R_star"]) ** 2)
            / (p_config["ell_lock_R"] ** 2)
        )
        G_lock_d = sigmoid((p_config["d_lock"] - d) / p_config["ell_lock_d"])
        G_lock = float(G_lock_R * G_lock_d)
        max_G_lock = max(max_G_lock, G_lock)

        # ----------------------------------------------------
        # R ignition barrier
        # ----------------------------------------------------
        R_ignite = float(p_config["R_ignite"])
        ell_ignite = float(p_config["ell_ignite"])

        if p_config.get("ignite_mode", "component") == "score":
            ignite_gate_scalar = sigmoid((R_score - R_ignite) / ell_ignite)
            ignite_gate = ignite_gate_scalar * np.ones_like(R)
        else:
            ignite_gate = sigmoid((R - R_ignite) / ell_ignite)

        ignite_gate_mean = float(np.mean(ignite_gate))
        max_ignite_gate_mean = max(max_ignite_gate_mean, ignite_gate_mean)

        # optional weak baseline activation; usually very small
        baseline_gate = float(p_config.get("R_baseline_gate", 0.0))
        effective_gate = baseline_gate + (1.0 - baseline_gate) * ignite_gate

        # noise-induced decoherence
        D_decoh = float(p_config.get("D_R_noise_decoh", 0.0))
        noise_decoh = D_decoh * (sigma_R ** 2) * R

        dR_drift = (
            p_config["A_R"] * F_prox * effective_gate * (1.0 - R)
            - p_config["H_R"] * R
            - p_config["B_R_cross"] * (np.sum(R) - R) * R / max(1, N - 1)
            - noise_decoh
        )

        # partly common noise helps coordinated ignition
        common_weight = float(p_config.get("R_common_noise_weight", 0.0))
        common_noise = rng.normal()
        indep_noise = rng.normal(size=N)
        noise_vec = (
            common_weight * common_noise
            + math.sqrt(max(0.0, 1.0 - common_weight**2)) * indep_noise
        )

        R += dR_drift * dt + sigma_R * math.sqrt(dt) * noise_vec
        R = np.clip(R, 0.0, p_config.get("R_clip", 1.35))

        # ----------------------------------------------------
        # Distance dynamics
        # ----------------------------------------------------
        capture_pull = -p_config["A_att"] * G_R_open * F_prox * (d - p_config["d_fuse"])
        hold_pull = -p_config["A_hold"] * G_lock * (d - p_config["d_fuse"])
        repulsion = p_config["K_rep"] / ((d + p_config["eps_d"]) ** 2)

        dd = v_protocol + capture_pull + hold_pull + repulsion

        d += dd * dt + p_config["sigma_d"] * math.sqrt(dt) * rng.normal()
        d = float(np.clip(d, p_config["d_floor"], p_config["d_escape_hard"]))

        min_d = min(min_d, d)

        # ----------------------------------------------------
        # Hit
        # ----------------------------------------------------
        if (not hit) and d < p_config["d_hit"]:
            hit = True
            hit_time = t

        # ----------------------------------------------------
        # Strict lock step
        # ----------------------------------------------------
        is_lock_step = (
            d < p_config["d_lock"]
            and R_score > p_config["R_lock_threshold"]
            and G_lock > p_config["G_lock_threshold"]
        )

        if hit:
            post_hit_steps += 1
            if is_lock_step:
                post_hit_lock_steps += 1

        if is_lock_step:
            current_consecutive_lock_steps += 1
        else:
            current_consecutive_lock_steps = 0

        max_consecutive_lock_steps = max(
            max_consecutive_lock_steps,
            current_consecutive_lock_steps,
        )

        if (
            not first_lock_event
            and current_consecutive_lock_steps * dt >= p_config["T_lock_hold"]
        ):
            first_lock_event = True
            first_lock_time = t

        final_lock_buffer.append(1 if is_lock_step else 0)
        if len(final_lock_buffer) > final_window_steps:
            final_lock_buffer.pop(0)

        # ----------------------------------------------------
        # Hidden-depth h dynamics
        # ----------------------------------------------------
        M_h = p_config["M_h0"] + p_config["M_h1"] * G_lock
        amp_I_eff = amp_I * G_lock

        U_h, grad_h, Uconf = post_energy_grad(
            h,
            templates,
            rho=rho,
            amp_I_eff=amp_I_eff,
            p=p_config,
        )

        h += (
            -M_h * grad_h * dt
            + p_config["sigma_h"] * math.sqrt(dt) * rng.normal(size=2 * N)
        )

        norm_h = np.linalg.norm(h)
        if norm_h > p_config["h_clip"]:
            h = h / norm_h * p_config["h_clip"]

        h_class = classify_h(h, a, b, templates, p_config)

        if first_lock_event and (not inherited_during_lock) and h_class["h_outcome"] == "inheritance":
            inherited_during_lock = True
            inheritance_time = t

        if keep_trace and step % p_config["trace_stride"] == 0:
            trace.append({
                "t": t,
                "d": float(d),
                "R_score": float(np.mean(R)),
                "R_max": float(np.max(R)),
                "G_lock": float(G_lock),
                "F_prox": float(F_prox),
                "ignite_gate_mean": float(ignite_gate_mean),
                "is_lock_step": int(is_lock_step),
                "h_outcome": h_class["h_outcome"],
                "sim_I": h_class["sim_I"],
                "balance": h_class["balance"],
                "amp_I_eff": float(amp_I_eff),
                "U_h": float(U_h),
                "Uconf": float(Uconf),
            })

    # --------------------------------------------------------
    # Final strict lock decision
    # --------------------------------------------------------
    if post_hit_steps > 0:
        lock_fraction_after_hit = post_hit_lock_steps / post_hit_steps
    else:
        lock_fraction_after_hit = 0.0

    final_lock_fraction = (
        np.mean(final_lock_buffer)
        if len(final_lock_buffer) > 0
        else 0.0
    )

    strict_lock = (
        first_lock_event
        and lock_fraction_after_hit >= p_config.get("min_lock_fraction_after_hit", 0.40)
        and final_lock_fraction >= p_config.get("min_final_lock_fraction", 0.35)
    )

    lock_time = first_lock_time if strict_lock else np.nan

    U_h_final, _, Uconf_final = post_energy_grad(
        h,
        templates,
        rho=rho,
        amp_I_eff=amp_I * max_G_lock,
        p=p_config,
    )

    final_h = classify_h(h, a, b, templates, p_config)

    escaped = d > p_config["d_escape"]
    full_success = bool(strict_lock and final_h["h_outcome"] == "inheritance")

    result = {
        "seed": int(seed),
        "rho": float(rho),
        "amp_I": float(amp_I),
        "sigma_R": float(sigma_R),

        "hit": int(hit),
        "first_lock_event": int(first_lock_event),
        "lock": int(strict_lock),
        "escaped": int(escaped),
        "full_success": int(full_success),
        "inherited_during_lock": int(inherited_during_lock),

        "hit_time": hit_time,
        "first_lock_time": first_lock_time,
        "lock_time": lock_time,
        "inheritance_time": inheritance_time,

        "lock_fraction_after_hit": float(lock_fraction_after_hit),
        "final_lock_fraction": float(final_lock_fraction),
        "max_consecutive_lock_time": float(max_consecutive_lock_steps * dt),

        "final_d": float(d),
        "min_d": float(min_d),
        "max_R_score": float(max_R_score),
        "max_R_component": float(max_R_component),
        "max_G_lock": float(max_G_lock),
        "max_ignite_gate_mean": float(max_ignite_gate_mean),

        "h_outcome": final_h["h_outcome"],
        "M_A": final_h["M_A"],
        "M_B": final_h["M_B"],
        "sim_A": final_h["sim_A"],
        "sim_B": final_h["sim_B"],
        "sim_I": final_h["sim_I"],
        "balance": final_h["balance"],
        "norm_h": final_h["norm_h"],

        "U_h0": float(U_h0),
        "U_h_final": float(U_h_final),
        "h_release_drop": float(U_h0 - U_h_final),

        "Uconf0": float(Uconf0),
        "Uconf_final": float(Uconf_final),
        "conflict_drop": float(Uconf0 - Uconf_final),

        "CODE_VERSION": CODE_VERSION_B12D,
        "CODE_SHA16": CODE_SHA16_B12D,
    }

    if keep_trace:
        return result, pd.DataFrame(trace)

    return result
