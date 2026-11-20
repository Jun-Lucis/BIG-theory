# BIG-MATH-02 R8 — Waiting-time boundary slopes (2026-11-20)

**Jun Lucis.** *Waiting-Time Boundary Slopes for a Mixed Degenerate Diffusion: Vanishing Tangents, Averaged Regularization, and an Open Classical Trace Problem.* **Preprint v0.4.2**, published 20 November 2026. Open Access, **CC BY 4.0**, **not externally peer reviewed**.

- **Version-specific DOI:** [10.5281/zenodo.24387025](https://doi.org/10.5281/zenodo.24387025)
- **Zenodo record and public files:** [zenodo.org/records/24387025](https://zenodo.org/records/24387025)
- **Status:** independent **AI-assisted**, source-scoped final mathematical audit of the frozen v0.4 manuscript: `MANUSCRIPT_FINAL_AUDIT_PASS_WITH_SCOPE`. The subsequent v0.4.1/v0.4.2 changes were editorial/display-only and **do not constitute a new independent mathematical audit**. There has been no external human specialist peer review.

## Published files and reported post-deposit verification

The author's publication Work reports that it downloaded all three published files and verified their **SHA-256** against the frozen Drive release originals. This GitHub index records that report; it is **not a separate GitHub-side re-download/recalculation**.

| Public filename | Bytes | SHA-256 (reported readback match) |
| --- | ---: | --- |
| `R8_integrated_paper_v0_4_2.pdf` | 457,990 | `81e5c4dacfb7ac93bbf9719e4ff244bd78e6ff5ec6b7f9ca1b0fcd4771522770` |
| `R8_technical_proof_appendix_v0_4_2.pdf` | 373,362 | `58f112b7ccbc43fd01d1e446f55a7d8fdedd6f0e5d2b89f2ce65e9a273f3149c` |
| `BIG_MATH_02_R8_v0_4_2_PUBLICATION_READY.zip` | 4,933,818 | `8e119e89d3472e958bbe12e06285bbde5bc5981f6474ec8d355cd6a31d99b31a` |

The main manuscript is **20 pages** and the companion technical proof appendix is **9 pages**. The ZIP contains TeX sources, provenance/QA material, and 14 frozen primary proof/audit documents. It also preserves a historical v0.4.1 archive; old `HOLD_NOT_APPROVED` labels therein are historical, **not** the status of the published v0.4.2 record.

## Mathematical scope

The studied original **one-dimensional**, source-free, mixed degenerate diffusion is

```text
u_t = partial_x( u^2 u_x + 4 gamma (u_x)^3 ),   gamma > 0.
```

Within the **specified restricted nonnegative weak-solution/approximation class**, the manuscript assembles:

- **U01 / Definition 3.1:** strictly positive periodic classical approximants, restricted class nonemptiness, and the stated strong `L^4` gradient convergence;
- **U03:** vanishing *quadratic* blow-up tangent for specified superflat initial data, with a weak zero initial trace and finite-strip comparison; **not** a classical pressure-slope tip trace;
- **U07:** **time-integrated** naturally weighted curvature dissipation; **not** an unproved distance-weighted tip bound;
- **U08:** regularity strictly in the positive interior and a conditional connected high-gradient interval width result; **not** regularity up to the vacuum boundary.

Certain further propositions remain explicitly **conditional** on additional hypotheses. The argument imports specified source-scoped CP10AK/R7 results and external parabolic PDE theorems; the 29-page main-plus-appendix pair is **not** a from-scratch proof of every upstream theorem.

### Open questions and scope guards

- Classical vacuum-tip pressure-gradient trace: `INCONCLUSIVE`.
- Genuine positive-time PDE nonconvergence counterexample: `COUNTEREXAMPLE_NOT_FOUND`.
- Mathematical novelty: `NOT_ESTABLISHED`; priority: `PRIORITY_UNRESOLVED`.
- Human specialist mathematical peer review: `NOT_DONE`.
- No independently established BIG-specific new physical law or experimental validation; the programme-wide B42 verdict **SCIENCE NONE** (independent R4 0/0/0) remains unchanged.

This **R8 evolution preprint is a new standalone Zenodo record**, not a new version of the separate **BIG-MATH-02 static-observation paper**, nor of BIG-MATH-01 or any B-series record.

## Citation

> Lucis, J. (2026). *Waiting-Time Boundary Slopes for a Mixed Degenerate Diffusion: Vanishing Tangents, Averaged Regularization, and an Open Classical Trace Problem* (Preprint v0.4.2). Zenodo. https://doi.org/10.5281/zenodo.24387025

See the [publication map](../../docs/publication_map.md) and [citation policy](../../docs/citation_policy.md) for the distinct model families and version-specific citation rules.
