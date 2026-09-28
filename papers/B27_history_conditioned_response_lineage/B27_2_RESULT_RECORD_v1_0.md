# BIG-B27.2 Result Record — Topology-Reconfiguration Covariance

**Protocol:** BIG_B27_2_TOPOLOGY_RECONFIGURATION_COVARIANCE_v1_0  
**Status:** COMPLETED  
**Date:** 2026-09-29  
**Formal verdict:** `RECONFIGURATION_COVARIANCE_FAIL`

## Frozen test

B27.2 v1.0 prospectively tested whether the normalized history-induced response-lineage form

[
H_G=G_{m kept}-G_{m erased},
qquad
L_G=H_G/|H_G|_F
]

remained approximately unchanged across connected-to-disconnected topology reconfiguration.

The frozen geometry-only covariance map was

[
A=I_5,
]

so the primary prediction was

[
L_G^+approx L_G^-.
]

The covariance PASS threshold was fixed before any post-reconfiguration response:

[
epsilon_{m cov}le 0.010,
]

with PARTIAL defined prospectively by

[
0.010<epsilon_{m target}le0.030.
]

## Target outcomes

All three frozen targets satisfied the mandatory numerical/scientific validity gates.

| target | delta+ | epsilon_target | classification |
|---|---:|---:|---|
| T1 | 5.40 | 0.1118248844 | FAIL |
| T2 | 5.70 | 0.1276381141 | FAIL |
| T3 | 6.00 | 0.1450767448 | FAIL |

Thus every target exceeded even the frozen PARTIAL ceiling by a wide margin.

## Validity notes

For all three targets:

- post topology was exactly two primary components at both N=128 and N=160;
- the zero-feedback response defect was 0;
- probe-scale G defects remained below 0.001;
- cross-resolution G and L defects remained below 0.01;
- retained-history response remained resolved above the frozen Delta_G=0.009 gate;
- domain-edge field values were negligible.

Therefore the result is not classified as INCONCLUSIVE and is not an implementation failure.

## Secondary pattern

The history-induced response amplitude remained nonzero but weakened after reconfiguration. The post/pre (|H_G|_F) amplitude ratios were approximately:

- T1: 0.370;
- T2: 0.364;
- T3: 0.351.

At the same time, the normalized lineage-form defect increased monotonically with separation:

[
0.1118 ightarrow 0.1276 ightarrow 0.1451.
]

This secondary trend does not alter the frozen verdict.

## Frozen verdict

Because all three targets were valid and all three were FAIL,

[
oxed{	exttt{RECONFIGURATION_COVARIANCE_FAIL}}.
]

## Interpretation

B27.2 rejects the specific frozen hypothesis that the normalized history-induced response form is approximately invariant under the tested topology reconfiguration with the identity geometry map.

The negative result is structurally informative:

- B27.1 showed that retained history changes local response geometry at identical present phi;
- B27.2 shows that this history-conditioned response geometry is not carried through the tested topology change as one unchanged normalized lineage form.

Thus, in this finite model, **history dependence survives while simple response-lineage invariance does not**.

This does not erase B27.1 and does not imply that every possible reconfiguration relation fails. Any new transport/covariance map is a new hypothesis and must be tested under a new numbered programme rather than tuned inside B27.2.

## Stop rule

Per the B27 architecture, no response-derived map is fitted to rescue the failed family. B27.3 is not run under the failed B27.2 covariance construction.

A new mapping hypothesis, if pursued, belongs to a new B-series.
