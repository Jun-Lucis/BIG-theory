# BIG-B38 — Relational Timing and Weighted Measurement Duality

**Published preprint:** *Relational Timing and Weighted Measurement Duality in a Finite Nonlinear Boundary Field Model*  
**Subtitle:** *From Directed Source–Receiver Rephasing to Operator-Compatible Readout*  
**Author:** Jun Lucis  
**Zenodo DOI:** https://doi.org/10.5281/zenodo.23104248

The English preprint is the authoritative manuscript. A Japanese reference translation is deposited in the same Zenodo record.

---

## Why B38 matters

B38 marks a methodological shift from asking only for an absolute timing quantity to asking which timing structures remain stable under changes of geometry, source/receiver orientation, discretization, and readout convention.

The central retained result is not that the tested model has a fundamental one-way law. Instead, the measured timing asymmetry is strongly **relational**: it depends on the joint structure of the evolving operator, source, receiver, and readout.

The sequence begins with a prospective relative-lag result and ends with a prospective measurement-duality intervention.

---

## Retained claim-bearing sequence

| Stage | Retained verdict | Main role |
| --- | --- | --- |
| B38.1 | `RELATIVE_BOUNDARY_LAG_GEOMETRY_PASS` | Relative boundary lag is coherent across fresh geometry, phase, resolution, and amplitude checks. |
| B38.2-P1 | `DIRECTED_SOURCE_RECEIVER_SWAP_ASYMMETRY_PASS` | Source/receiver swap produces reproducible directed response asymmetry in the tested finite model. |
| B38.3-P1 | `D_WEIGHTED_NEAR_SYMMETRY_WITH_DIAGONAL_CYCLE_OBSTRUCTION_PASS` | The exact semi-discrete tangent operator is strongly closer to symmetry in the D-weighted metric than in the standard metric. |
| B38.3-P2-P1 | `COMPATIBLE_GAMMA_RESIDUAL_CYCLE_WITH_DISCRETIZATION_DOMINANCE_PASS` | A compatible gamma=0 control closes to roundoff; the directional cubic term leaves a smaller finite-grid residual cycle. |
| B38.4-P1 | `TIME_DEPENDENT_TANGENT_RESPONSE_BRIDGE_PASS` | Frozen tangent predictions prospectively reproduce fresh nonlinear directed-response traces and swap metrics. |
| B38.5-P1 | `D_COMPATIBLE_GAMMA0_REPHASING_RETENTION_PASS` | Most swap rephasing remains under the time-dependent D-compatible gamma=0 tangent control; gamma timing contribution is subdominant. |
| B38.6-P1 | `D_WEIGHTED_DUAL_READOUT_SUPPRESSION_PASS` | The large standard-readout rephasing is strongly suppressed by D-weighted dual receiver conventions. |

---

## Core quantitative landmarks

### Relative lag

B38.1 found an approximately linear intrinsic-arc relative-lag relation in fresh finite-model cases:

- minimum primary pair (R^2): **0.98491**
- minimum shifted correlation: **0.99626**
- cross-geometry phase-mean slope span: **0.9876%**
- representative N128/N160 symmetric relative slope difference: **0.0256%**

This is a relational timing result, not a propagation-speed or wave-law result.

### Directed swap response

B38.2-P1 found fresh source/receiver swap defects of approximately **0.0678–0.0748**, with best-shift magnitudes of approximately **0.230–0.300**. After temporal rephasing, the minimum shifted correlation was **0.9999788**.

### Operator-to-response bridge

B38.4-P1 prospectively froze tangent predictions before any fresh nonlinear response trajectory was run. On the fresh N160 cases:

- maximum directed trace defect: **0.0007851**
- minimum directed trace correlation: **0.99999923**
- maximum swap-defect absolute error: **7.14e-05**
- maximum best-shift absolute error: **0.0025**

Thus the time-dependent tangent operator predicts the tested small-amplitude nonlinear directed-response structure to high accuracy.

### Gamma intervention

B38.5-P1 found:

- minimum observed absolute best shift: **0.245**
- minimum C0/observed absolute-shift ratio: **0.93**
- maximum O1–O2 best-shift difference after removing gamma in the original tangent: **0**
- maximum compatible (C_gamma-C_0) timing increment as a fraction of O1: **0.9259%**

The directional cubic tangent is therefore not supported as the dominant source of the large observed rephasing in these fresh finite-model cases.

### Weighted measurement duality

B38.6-P1 froze the protocol before any fresh B38.6-P1 trajectory. All formal components passed.

For the fresh cases:

- minimum standard-readout absolute best shift: **0.235**
- maximum frozen-D dual / standard shift ratio: **0.14737**
- maximum instantaneous-D dual / standard shift ratio: **0.17021**
- mean frozen-D dual / standard shift ratio: **0.09299**
- mean instantaneous-D dual / standard shift ratio: **0.15537**

The frozen-C0 weighted-dual reciprocity sentinel closed to roundoff:

- maximum direct swap defect: **3.14e-16**
- maximum absolute best shift: **4.44e-16**

The result is therefore a strong finite-model demonstration that a large timing asymmetry seen under one readout convention can be substantially reduced when the receiver is chosen according to the operator-compatible D-weighted dual structure.

---

## Mathematical relation

For the compatible gamma=0 tangent control,

[
J_{C0}(t)u = Delta_h!left(D(phi_{m ref}(t))uight)-mu u.
]

At a frozen state, with (W=operatorname{diag}D), the compatible discrete operator satisfies the weighted symmetry relation

[
WJ = J^T W
]

at the finite-matrix level under the matched boundary implementation.

The weighted-dual receiver is therefore chosen as

[
c_i = W b_i.
]

B38.6 tests what happens when this operator-compatible dual relation is applied to the measured response.

---

## Interpretation

The retained B38 result can be stated narrowly:

> In the tested fresh finite semi-discrete model, directed source/receiver timing rephasing is prospectively reproducible and predictable from the time-dependent tangent operator, but its magnitude is strongly readout-dependent. D-weighted dual receiver conventions suppress most of the large rephasing measured under the standard matched readout.

The remaining evolving weighted-dual residual is deliberately left unresolved.

It may reflect, among other possibilities:

- evolving metric effects,
- nonautonomous time ordering,
- finite-window extraction,
- discretization,
- support/readout construction,
- or another finite-model contribution.

B38 does **not** establish fundamental non-reciprocity, time-reversal violation, an observer-limited law, continuum persistence, wave propagation, propagation speed, Lorentz structure, electromagnetism, quantum structure, or a universal law.

---

## Forward question

B38 still uses an externally supplied evolution parameter (t). The next theoretical question is therefore distinct from the B38 claim:

> Can an internal timing structure be reconstructed from boundary-to-boundary relations and their histories, rather than treating external (t) as the only primitive temporal variable?

This is a motivation for future work, not a conclusion of B38.

---

## Citation

```text
Lucis, J. Relational Timing and Weighted Measurement Duality in a Finite
Nonlinear Boundary Field Model: From Directed Source–Receiver Rephasing
to Operator-Compatible Readout. Boundary Information Geometry (BIG-B38),
2026. DOI: 10.5281/zenodo.23104248.
```

Zenodo: https://doi.org/10.5281/zenodo.23104248
