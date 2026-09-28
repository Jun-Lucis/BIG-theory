# BIG-B27 — History-Conditioned Boundary Response and Reconfiguration Covariance

> 🇯🇵 **日本語概要**  
> B27では、「個」を不変な状態や形として置くのではなく、境界を介して外部変化を受け取り、履歴によって形成され、branch/topologyの再構成を越えて継承されうる **response lineage** として数理的に検査します。哲学的な個体同一性そのものは判定せず、有限の縮約モデルで測定可能な応答作用素とその共変的対応だけを前向きに検査します。

## Central question

Can a history-conditioned boundary response structure remain measurably related across reconfiguration even when the state, geometry, and absolute response change?

The primary objects are the local response operator

\[
K=D_a\mathcal R_T|_{a=0},
\]

and the normalized response pullback form

\[
G=\frac{K^T W_ZK}{\operatorname{tr}(K^T W_ZK)}.
\]

Across a frozen geometry-induced frame map \(A\), B27 tests

\[
G^+\stackrel{?}{\approx}A^T G^-A.
\]

## Stages

- **B27-P0:** calibration only; no claim-bearing evidence.
- **B27.1:** same-current-geometry retained-versus-erased history intervention.
- **B27.2:** response covariance across controlled reconfiguration.
- **B27.3:** unchanged prospective transfer to a new held-out reconfiguration family.

## Frozen architecture

- [B27.0 frozen programme architecture](B27_0_FROZEN_programme_architecture_v1_0.md)
- [B27.0 machine-readable protocol](B27_0_FROZEN_protocol_v1_0.json)

## Claim boundary

B27 does not test consciousness, subjective continuity, AI personhood, personal identity, or a universal law of individuality. The philosophical motivation is kept separate from the finite numerical claims.

## Programme relation

B27 begins after formal closure of B19-B26. It does not reopen or upgrade any archived verdict.


## B27-P0 calibration

- [P0 calibration record](B27_P0_CALIBRATION_RECORD_v1_0.md)
- Colab notebook: `BIG_B27_P0_Calibration_v1_0.ipynb` (conversation artifact)

P0 is non-claim-bearing. It selected the converged primary readout and numerical floors only.

## B27.1 frozen test

- [B27.1 final frozen predeclaration](B27_1_FROZEN_predeclaration_v1_1.md)
- [B27.1 final machine-readable protocol](B27_1_FROZEN_protocol_v1_1.json)
- [B27.1 result record](B27_1_RESULT_RECORD_v1_0.md)

**Formal B27.1 verdict:** `HISTORY_RESPONSE_GEOMETRY_PASS` (4/4 held-out angles passed the frozen structural gate at both resolutions; all numerical validity gates passed).


## B27.2-P1 frozen training anchor

B27.2 does not compare absolute response geometry directly. It isolates the history-induced response deformation

[
H_G = G_{\rm kept}-G_{\rm erased},
qquad
L_G = H_G/\|H_G\|_F.
]

The P1 stage measures only the connected pre-reconfiguration anchor and freezes the numerical covariance floor before any post-reconfiguration target is evaluated.

- [B27.2-P1 frozen training-anchor protocol](B27_2_P1_FROZEN_training_anchor_v1_0.md)
- [B27.2-P1 machine-readable protocol](B27_2_P1_FROZEN_protocol_v1_0.json)

No disconnected B27.2 post-target response had been evaluated when these files were frozen.


## B27.2 status

- [B27.2-P1 frozen training anchor](B27_2_P1_FROZEN_training_anchor_v1_0.md)
- [B27.2-P1 result record](B27_2_P1_RESULT_RECORD_v1_0.md)
- [B27.2-P1R frozen continuation anchor](B27_2_P1R_FROZEN_training_anchor_v1_0.md)
- [B27.2-P1R machine-readable protocol](B27_2_P1R_FROZEN_protocol_v1_0.json)

B27.2-P1 completed with `P1_ANCHOR_TOPOLOGY_GATE_FAIL`: direct initialization at delta=4.90 produced two threshold components at both claim resolutions, so its provisional covariance gate is not adopted. No post-reconfiguration target was run. P1R prospectively switches to a continuation-prepared connected anchor before any target evaluation.


## B27.2 topology-reconfiguration covariance

- [B27.2-P1 failed-anchor result](B27_2_P1_RESULT_RECORD_v1_0.md)
- [B27.2-P1R continuation-anchor predeclaration](B27_2_P1R_FROZEN_training_anchor_v1_0.md)
- [B27.2-P1R machine protocol](B27_2_P1R_FROZEN_protocol_v1_0.json)
- [B27.2-P1R valid-anchor result](B27_2_P1R_RESULT_RECORD_v1_0.md)
- [B27.2 frozen prospective predeclaration](B27_2_FROZEN_predeclaration_v1_0.md)
- [B27.2 frozen machine protocol](B27_2_FROZEN_protocol_v1_0.json)

P1R reproduced a connected pre-anchor at both claim resolutions and froze the B27.2 covariance gate at **0.010** before any post-reconfiguration response.

B27.2 then completed all three frozen connected-to-disconnected targets. All three were numerically valid, but their frozen lineage defects were 0.1118248844, 0.1276381141, and 0.1450767448, all above the PASS threshold 0.010 and PARTIAL ceiling 0.030.

**Formal B27.2 verdict:** `RECONFIGURATION_COVARIANCE_FAIL`.

- [B27.2 terminal result record](B27_2_RESULT_RECORD_v1_0.md)
- [B27.2 secondary trend audit](B27_2_SECONDARY_TREND_AUDIT_v1_0.md)
- [B27 programme closeout](B27_CLOSEOUT_v1_0.md)
- [B28 non-frozen architecture draft](../B28_geometry_conditioned_lineage_transport/B28_0_DRAFT_architecture_v0_1.md)

Per the frozen stop rule, B27.3 is not run. B27 is closed: retained history prospectively changes local response geometry, but that normalized history-induced response geometry does not remain invariant across the tested topology reconfiguration. Any new transport/covariance mapping hypothesis belongs to B28 or later.
