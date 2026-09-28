# BIG-B27.2 Frozen Prospective Topology-Reconfiguration Covariance Test

**Status:** FROZEN BEFORE FIRST POST-RECONFIGURATION RESPONSE TRAJECTORY  
**Protocol ID:** BIG_B27_2_TOPOLOGY_RECONFIGURATION_COVARIANCE_v1_0  
**Freeze date:** 2026-09-29

## 1. Question

Does the history-induced local response-lineage form remain quantitatively related after a controlled connected-to-disconnected geometry reconfiguration?

The primary pre-reconfiguration object is

[
H_G^- = G^-_{\rm kept}-G^-_{\rm erased},
qquad
L_G^- = rac{H_G^-}{|H_G^-|_F}.
]

The P1R continuation anchor was valid at both resolutions and froze

[
\epsilon_{\rm cov}=0.010.
]

The fine-resolution pre-lineage matrix is identified by SHA-256:

`5e25d87279caa3b4f2a9b995375eb0db1bb68941e08d240c0a495cc7594a0eda`.

No post-reconfiguration response has been evaluated when this protocol is frozen.

## 2. Reconfiguration class

B27.2 v1.0 tests **topology reconfiguration without imposed rigid rotation**. Therefore the geometry-only probe-space map is

[
A=I_5.
]

The primary prospective prediction is consequently

[
\boxed{L_G^+ \approx L_G^-}.
]

This stage does not test nontrivial rotational covariance. Such a test must be reserved for a later held-out stage.

## 3. Frozen pre-anchor preparation

At each resolution:

1. start from (phi=0,m=0);
2. evolve the single-center compact source for (T=20);
3. switch with (eta_S=0) and no history writing to the normalized equal two-center source
   [
   delta_-=4.75,quad 	heta=0^circ
   ]
   for (T=20);
4. require one primary threshold component;
5. write history on the body-frame ray
   [
   psi_{\rm write}=55^circ
   ]
   using the frozen B27.1/P1R write protocol;
6. rest for (T=1);
7. require one primary threshold component.

The notebook must reproduce the P1R N=160 (L_G^-) SHA-256 before proceeding to any post target.

## 4. Frozen post targets

Each target starts independently from the same pre-anchor state. During reconfiguration:

- history writing is disabled;
- read feedback is disabled: (eta_S=0);
- retained (m) may only decay/diffuse through the inherited history equation;
- (phi) therefore reconfigures independently of readable history.

The three frozen post targets are:

| target | (delta_+) | source orientation | reconfiguration time |
|---|---:|---:|---:|
| T1 | 5.40 | 0° | 20 |
| T2 | 5.70 | 0° | 20 |
| T3 | 6.00 | 0° | 20 |

These (delta_+) values were not used in P0, failed P1, or P1R.

Each target must realize exactly two primary (phi>0.03) components at both (N=128) and (N=160).

No target may be replaced or extended after execution begins.

## 5. Post response measurement

At each post anchor, branch from the exact same (phi^+) into

[
X^+_{\rm kept}=(phi^+,m^+),
qquad
X^+_{\rm erased}=(phi^+,0),
]

and the (eta_S=0) null-readability control.

Use unchanged:

- (N=128,160);
- (dt=0.003,0.0025);
- (T_{\rm read}=0.25);
- (h=0.001) primary and (0.002) secondary;
- five probe modes ((l0,l1_x,l1_y,l2_c,l2_s));
- (Z=(A/A_0,c_x/R_0,c_y/R_0,q_1,q_2)).

Define

[
H_G^+ = G^+_{\rm kept}-G^+_{\rm erased},
qquad
L_G^+ = rac{H_G^+}{|H_G^+|_F}.
]

## 6. Primary covariance defect

Because (A=I_5),

[
\epsilon_L
=
rac{|L_G^+-L_G^-|_F}
{|L_G^+|_F+|L_G^-|_F}.
]

The per-target primary defect is

[
\epsilon_{\rm target}
=
max(
\epsilon_L^{128},
\epsilon_L^{160}
).
]

Frozen per-target classifications:

- PASS: (epsilon_{\rm target}le 0.010)
- PARTIAL: (0.010<epsilon_{\rm target}le 0.030)
- FAIL: (epsilon_{\rm target}>0.030)

The PARTIAL band is fixed prospectively at three times the covariance gate.

## 7. Mandatory validity gates

Every target must satisfy all of the following at both resolutions:

1. solver completion with finite values;
2. post topology = exactly two primary components;
3. maximum boundary-edge (phi < 0.003);
4. retained-history maximum (>10^{-4});
5. post history effect remains resolved:
   [
   Delta_G^+>0.009;
   ]
6. probe-scale (G) defects (le0.001);
7. zero-feedback (G) defect (le0.003);
8. branchwise cross-resolution (G) defects (le0.01);
9. post (L_G^+) cross-resolution defect (le0.01).

If any target fails a mandatory scientific validity gate, the aggregate B27.2 verdict is `INCONCLUSIVE`. A software/protocol execution defect yields `IMPLEMENTATION_INVALID`. No invalid target is replaced.

## 8. Frozen aggregate verdict

If all three targets are valid:

- at least 2/3 target PASS -> `RECONFIGURATION_COVARIANCE_PASS`
- otherwise at least 2/3 target PASS-or-PARTIAL -> `RECONFIGURATION_COVARIANCE_PARTIAL`
- otherwise -> `RECONFIGURATION_COVARIANCE_FAIL`

The verdict is terminal for B27.2 v1.0.

## 9. Secondary diagnostics

Record without affecting the primary verdict:

- (|H_G^+|_F/|H_G^-|_F);
- absolute response-gain changes;
- quadrupole and area changes;
- retained-history mass after reconfiguration;
- topology midpoint/bridge diagnostics.

## 10. Claim boundary

A PASS would support only the finite-model statement that a normalized **history-induced local response structure** remains quantitatively related across the tested connected-to-disconnected reconfigurations.

It would not establish identity, consciousness, subjective continuity, biological inheritance, AI personhood, or a universal law of individuality.

A FAIL would reject this particular frozen covariance construction for the tested family; it would not erase B27.1.

## 11. Anti-rescue

After the first post target starts:

- no target replacement;
- no domain extension;
- no change of (delta_+), relaxation time, history protocol, response basis, readout, or covariance gate;
- no response-derived transform;
- no switch from (L_G) to absolute (G);
- no target-specific rescaling;
- no retrospective reclassification of P0/P1/P1R as post evidence.
