
"""B12.1d refined scan launcher (protocol stub).

This stub records the parameter grid and strict outcome definitions used for the
B12.1d-refined DOI package. It assumes the canonical B12.1d simulator function
`simulate_unified_one_B12_1d` is available from the research notebook.
"""
import numpy as np

D2_MID_BARRIER = {
    "variant_id": "d2_mid_barrier_refined",
    "variant_name": "refined middle ignition barrier",
    "A_R": 1.50,
    "H_R": 0.58,
    "A_att": 0.90,
    "A_hold": 1.35,
    "R_lock_threshold": 0.68,
    "G_lock_threshold": 0.25,
    "T_lock_hold": 3.0,
    "ell_lock_R": 0.24,
    "D_R_noise_decoh": 2.8,
    "min_lock_fraction_after_hit": 0.40,
    "min_final_lock_fraction": 0.35,
    "T_final_lock_hold": 5.0,
    "R_ignite": 0.18,
    "ell_ignite": 0.030,
    "R_baseline_gate": 0.000,
    "R_common_noise_weight": 0.55,
    "ignite_mode": "component",
}

SCAN_B12D_REF = {
    "rho": 0.90,
    "amp_I": 1.45,
    "sigma_R_list": [round(float(x), 3) for x in np.arange(0.000, 0.160 + 1e-12, 0.005)],
    "ntraj": 180,
}

# Main loop used in the notebook:
# for sigma_R in SCAN_B12D_REF["sigma_R_list"]:
#     for tr in range(SCAN_B12D_REF["ntraj"]):
#         seed = 12150000 + int(round(float(sigma_R) * 100000)) * 1000 + tr
#         out = simulate_unified_one_B12_1d(seed, rho=0.90, amp_I=1.45,
#                                          sigma_R=sigma_R,
#                                          p_config=p_d2_ref,
#                                          keep_trace=False)
