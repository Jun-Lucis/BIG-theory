# BIG-B41 — Prospective Trajectory-Space Response Geometry and Finite-Parameter Transfer

**Paper:** *Prospective Trajectory-Space Response Geometry and Second-Order Finite-Parameter Transfer: Failure Localization and a Fresh No-Fit Prediction Test in a Finite Vorticity-Response Model*  
**Author:** Jun Lucis (independent researcher)  
**Preprint v1.0 / manuscript date:** 2026-10-09  
**Zenodo DOI:** https://doi.org/10.5281/zenodo.23249677  
**Programme status:** B41 formally closed; original P1, P2, and P3 verdicts preserved.

## Scientific question and model

Can finite-window response trajectories at previously uncomputed parameter offsets be predicted from **local, pre-target trajectory geometry**, without fitting a new coefficient to target outcomes?

B41 returns to the finite Family-C operator-response setting developed from B20: a **three-dimensional periodic viscous vector-vorticity solver** with a six-horizon half-enstrophy response vector. Parameter secants along directions in a normalized four-dimensional Family-C subspace yield a local tangent vector `V_h` and local second-order acceleration vector `A_h`. These are numerical finite secants, not proved continuum derivatives. “Trajectory-space” means the six-horizon response vector across parameter values; it does not denote a physical-space moving interface or an externally observed trajectory.

This is a bounded **finite synthetic response-family** test. It is not a Navier–Stokes regularity result, a BIG-specific Taylor theorem, a universal law, or an external-system validation.

## Immutable prospective sequence

| Stage | Frozen formal verdict | Main evidence |
| --- | --- | --- |
| **P1** | `TRAJECTORY_RESPONSE_GEOMETRY_TRANSFER_PASS` | 32/32 targets favored tangent transfer; 97.7883% pooled weighted RMSE improvement over nearest-anchor baseline; gates A–F all PASS |
| **P2** | `DIMENSIONLESS_REMAINDER_TRANSFER_FAIL` | Fresh anchors/directions; 43/48 tangent advantages and 88.1862% pooled improvement, but scalar second-order predictor met the 20% mismatch criterion in only 19/24 sign-averaged cells; gates C and E FAIL |
| **P2 post-hoc** | Diagnostic only; **no regrading** | Five failing cells were localized to two nearly anti-aligned tangent/acceleration families |
| **P3** | `FULL_SECOND_ORDER_GEOMETRIC_REMAINDER_TRANSFER_PASS` | Separate fresh anchors I–L/directions u17–u24; 48/48 tangent advantages; 93.1041% pooled improvement; full second-order predictor 24/24 cells within 20%; gates A–E all PASS |

The parent **P2 FAIL is never converted to PASS** by either post-hoc diagnosis or P3's separately frozen prospective success.

## P1 — first-order trajectory transfer

The tangent predictor was frozen before any of the 32 target simulations. The nearest-anchor pooled weighted RMSE was `0.0042088806013`; the tangent-transfer RMSE was `0.00009308771363`, a **97.7883% reduction**. All 32 targets favored the tangent transfer. The sign-averaged scalar remainder-proxy ordering had Spearman `rho = 1.0`, with exact family-block permutation `p = 1/40320`. P1 established a strong local-to-finite-range prediction result **in its own frozen test family**, not a general transfer theorem.

## P2 — retained scalar-remainder failure

P2 tested a dimensionless scalar local-curvature proxy in new anchors E–H and directions u9–u16. In terms of a signed offset `dp` and local secants `V_h, A_h`, the frozen predictor was

```text
Q2_scalar(dp) = (|dp|/2) * ||A_h|| / ||V_h||
```

The scalar predictor discarded the orientation of `V_h` relative to `A_h`. Despite favorable aggregate first-order-transfer metrics (nearest `0.01463165737` versus tangent `0.00172855515`), the formal scalar quantitative-remainder test failed: only **19/24** sign-averaged cells met the frozen 20% mismatch criterion. Anchor E's median relative mismatch was **21.875%**, exceeding the 20% anchor gate. Gates **A, B, D PASS; C, E FAIL**.

A secondary 10% high-fidelity classification passed (**TP=11, TN=13, FP=FN=0**). That secondary success does **not** rescue the failed primary P2 verdict.

## Post-hoc failure localization (non-claim-bearing)

All five scalar-prediction cells exceeding 20% mismatch belonged to `E_u10` (three magnitudes) and `H_u16` (two magnitudes). These were the only two strongly anti-aligned local families:

- `E_u10`: `cos(V_h,A_h) ≈ -0.998970`
- `H_u16`: `cos(V_h,A_h) ≈ -0.985142`

The missing sign-sensitive geometry suggested a new, no-fit predictor using the same pre-target `V_h` and `A_h`:

```text
Q2_full(dp) =
    [0.5 * dp^2 * ||A_h||]
    /
    [||dp * V_h + 0.5 * dp^2 * A_h|| + eps]
```

Applying this formula to *already-opened* P2 outcomes was **post-hoc** and cannot turn P2 into a prospective success. Instead, the formula motivated a new P3 pre-outcome freeze.

## P3 — fresh prospective full-second-order test

P3 independently froze the new primary predictor before producing any of the **48 fresh target** responses. At freeze, **8/8** local geometric families had passed and **0/48** fresh target PDE integrations had been completed. The evaluator's implementation interpretation was independently frozen before target exposure; the evaluator ran **once**.

The signed target offsets were `dp = ±8h, ±16h, ±24h`. The predeclared assessment used **24 sign-averaged family-by-magnitude cells**.

| P3 quantitative outcome | Frozen result |
| --- | ---: |
| Target cases improving on nearest baseline | 48/48 |
| Pooled weighted RMSE: nearest | 0.01638094006 |
| Pooled weighted RMSE: tangent | 0.00112961088 |
| Pooled improvement | **93.1041%** |
| Spearman rho(`Q2_full`, observed sign-averaged error) | 0.9973913043 |
| Median relative mismatch of `Q2_full` | **0.6792%** |
| Cells within frozen 20% mismatch tolerance | **24/24** |
| Spearman rho for each magnitude (8h, 16h, 24h) | 1.0 each |
| Primary formal gates A–E | **all PASS** |
| Secondary 10% fidelity-classification boundary | TP=18, TN=6, FP=0, FN=0 |

Fresh strongly anti-aligned families included `J_u20` (`cos(V_h,A_h) ≈ -0.972471`) and `K_u22` (`≈ -0.996708`); both were part of the prospectively frozen P3 target set.

**Essential comparator limitation:** On the same fresh P3 sample, the non-gating scalar `Q2_scalar` diagnostic also achieved 24/24 cells within 20%, rho `0.9973913043`, and median mismatch **0.6755%** (versus **0.6792%** for `Q2_full`). P3 therefore does **not** demonstrate that direction information is always necessary or that `Q2_full` is generically superior to scalar `Q2_scalar`.

## Claim boundary

The strongest defensible conclusion is:

> A full, sign-sensitive second-order local trajectory-space geometry predictor achieved **no-fit, response-blind prospective quantitative transfer** across a separately frozen, finite synthetic response family with fresh parameter anchors and directions, including nearly anti-aligned tangent/acceleration stress cases.

**Not established:** generic superiority over scalar predictors; an invariant second-order law; arbitrary reparameterization covariance; a continuum theorem; a physical-space interface law; Navier–Stokes regularity or blow-up results; external physical validation; or a universal coefficient/law spanning BIG systems.

## Reproducibility and related repositories

- **Zenodo paper and archive:** https://doi.org/10.5281/zenodo.23249677
- **B41 paper navigation:** [papers/B41_trajectory_space_response_geometry](../papers/B41_trajectory_space_response_geometry/README.md)
- **Methodology case study:** [Failure-preserving B41 case](https://github.com/Jun-Lucis/failure-preserving-research/blob/main/case_studies/BIG/B41_P2_failure_to_P3_fresh_test.md)
- **B41 programme closeout:** `BIG_B41_Program_Closeout_v1_0` in the research archive.

The deposited reproducibility package includes P1–P3 local and target-stage archives, frozen predictions, SHA-256 manifests, and a saved evaluator notebook. The P3 target-stage archive's reported SHA-256 is:

```text
dd2e3ef9fafa24c3eb5553f43fb4a0b99523472e63d8d69f2cfab41daee909e6
```

The metadata and historical B41 results must remain distinct from later experiments or interpretations. Zenodo is the canonical preprint/archive record; GitHub is the navigational research index.
