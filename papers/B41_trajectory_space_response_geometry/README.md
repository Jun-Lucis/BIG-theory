# BIG-B41 — Prospective Trajectory-Space Response Geometry

**Full preprint title:** *Prospective Trajectory-Space Response Geometry and Second-Order Finite-Parameter Transfer: Failure Localization and a Fresh No-Fit Prediction Test in a Finite Vorticity-Response Model*  
**Author:** Jun Lucis (independent researcher)  
**DOI:** https://doi.org/10.5281/zenodo.23249677  
**Publication:** Zenodo preprint, 2026-10-09, v1.0  
**Licence of Zenodo record:** CC BY 4.0

The **English manuscript** is the primary paper; the Japanese manuscript is a reference translation of the same study, not a separate independent verification. Zenodo hosts the paper and reproducibility materials.

## Read the paper / download the archive

- **Zenodo record and DOI:** https://zenodo.org/records/23249677
- **Citation DOI:** https://doi.org/10.5281/zenodo.23249677
- **Full research status (English):** [B41 status](../../docs/research_status_update_B41.md)
- **研究状況 (日本語):** [B41 研究状況](../../docs/research_status_update_B41_ja.md)
- **Research-methodology counterpart:** [B41 failure-preserving case study](https://github.com/Jun-Lucis/failure-preserving-research/blob/main/case_studies/BIG/B41_P2_failure_to_P3_fresh_test.md)

## Paper in brief

The question is whether **local parameter-response geometry** measured before seeing held-out targets can predict finite-offset errors in the six-horizon response trajectory of a finite three-dimensional periodic vector-vorticity model.

```text
P1: frozen first-order tangent transfer
    TRAJECTORY_RESPONSE_GEOMETRY_TRANSFER_PASS
    32/32 targets favor tangent; pooled improvement 97.7883%

P2: fresh scalar dimensionless-remainder test
    DIMENSIONLESS_REMAINDER_TRANSFER_FAIL
    19/24 cells meet the 20% mismatch limit; gates C/E FAIL

P2 post-hoc localization (not an independent success)
    five failing cells confined to two anti-aligned V_h/A_h families
    original P2 FAIL is preserved

P3: new fresh no-fit signed second-order predictor
    FULL_SECOND_ORDER_GEOMETRIC_REMAINDER_TRANSFER_PASS
    48/48 target tangent advantage; pooled improvement 93.1041%
    24/24 cells within 20%; rho 0.997391; gates A-E PASS
```

The **strongest supported result** is fresh, no-fit prospective quantitative transfer of the sign-sensitive second-order response-geometry predictor within the specified finite synthetic family.

**Not supported:** universal full-versus-scalar superiority. The non-gating scalar predictor also performs strongly on the fresh P3 set (24/24 cells; median mismatch 0.6755%, compared with 0.6792% for the full version). No continuum theorem, Navier–Stokes regularity result, external-system law, or universal BIG mechanism is claimed.

## Reproducibility / provenance

The deposited publication package includes the primary and Japanese-reference PDFs, manuscript/figure sources, P1–P3 local and target-stage frozen archives, pre-outcome hashes, the saved numerical evaluator notebook, and integrity manifests.

**Recorded P3 target-stage ZIP SHA-256:**

```text
dd2e3ef9fafa24c3eb5553f43fb4a0b99523472e63d8d69f2cfab41daee909e6
```

P1, P2, and P3 each have a **formal evaluator run count of one** in the archived logs. Subsequent plots and text do not constitute a new formal evaluation.

## Citation

```text
Lucis, Jun (2026). Prospective Trajectory-Space Response Geometry and
Second-Order Finite-Parameter Transfer: Failure Localization and a Fresh
No-Fit Prediction Test in a Finite Vorticity-Response Model.
BIG-B41, preprint v1.0. Zenodo. DOI: 10.5281/zenodo.23249677.
```

This page is a navigation and bounded-outcome summary. The Zenodo preprint is the canonical citable record.
