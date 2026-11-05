# BIG-OC3 C19–P92 — History-dependent response, transfer and identifiability

**Jun Lucis (2026).** *History-Dependent Response, Predictive Transfer, and Limits of Identifiability: Failure-Preserving Mathematical and Experimental Benchmarks from C19 to P92 Steel.*

- **Published:** 5 November 2026 · **Version:** 1.0 RevA · **Resource type:** standalone, unreviewed preprint · **License:** CC BY 4.0.
- **Version-specific DOI:** [10.5281/zenodo.23965486](https://doi.org/10.5281/zenodo.23965486).
- **Zenodo record:** [23965486](https://zenodo.org/records/23965486).
- **Record family:** independent **BIG-OC3 C19–P92** synthesis, not a B-series New version.
- **English main PDF** with a **Japanese reference PDF** and an independent protocol/code/audit ZIP. The P92 measurements were obtained from third-party published sources, not acquired in a new BIG laboratory experiment.

## Model-specific evidence and retained failures

The C19 model constructs a spatial internal history variable `h(x,t)` with formation/decay and a history-conditioned response under controlled synthetic conditions. A restricted internal causal contribution and prospective model-internal predictions were supported; however, the main external-readout test with finite noise and unknown gain **FAILed**. Internal history affecting a future response is **not the same** as a history being identifiable from finite/noisy readouts.

P92 steel evaluation used **630,582 recorded time-series rows across three distinct specimens** in RF (relaxation fatigue), SLR (zero-strain relaxation) and SLC (constant-stress creep). It compared **ordinary generalized Maxwell / viscoelastic constitutive models**, not an independently validated BIG-specific material law:

| Test | Retained result | Evidence boundary |
| --- | --- | --- |
| E9C | A conventional **two-branch Maxwell** model reached **NRMSE ≈ 0.02224** | Limited within-specimen RF held-out early cycles; not transfer to another specimen or protocol |
| E9D | **FAIL** | Fixed RF coefficients did **not** pass the joint SLR/SLC transfer gate |
| E9F | Conditional improvement with a slower component and specimen-specific calibration | Not shared-parameter cross-specimen validation |
| E9G | **Joint gate FAIL** | Shared-coefficient long-tail improvement **≈9.05% (SLR)** and **≈24.39% (SLC)**; both did not meet the specified 20% criterion |
| E9H–E9J | Conventional viscoelastic response can reproduce loops; slow reversible recovery and permanent deformation may be indistinguishable over a finite observation window | No independent proof that a loop measures permanent plastic strain |

The Bristol cantilever work in this synthesis is a **separate** ordinary-model comparator. No BIG-specific incremental predictive value above equally informed conventional models was established. The programme-wide B42 **SCIENCE NONE** verdict (independent R4 0/0/0), previous FAIL/OPEN/INCONCLUSIVE results, and experimental-eligibility limits remain unchanged.

This study's `h(x,t)` is **not** the `u(x,t)` of the independent [BIG-MATH-01 positive-flux PDE study](../BIG_MATH_01_positive_flux/README.md). Well-posedness of the latter neither verifies nor refutes the former's physical transfer/readout gates.

## Published files and verification boundary

The 5 November 2026 publication report records:

| Public file | Bytes | Author-supplied SHA-256 | Post-release readback |
| --- | ---: | --- | --- |
| `BIG_P92_EN_v1_0_RevA.pdf` | 614,687 | `3cc4b893bc6197bcbf11127b5d5a3fed33ac8d909e4bee6a979d3b6fb89323a7` | Reported SHA-256 PASS |
| `BIG_P92_JA_v1_0_RevA.pdf` | 880,364 | `f50f3d7096b71ff6953109d4343192b8eb5e1f16909c518f9beac14f9c779546` | Reported **size/MD5 match; post-download SHA-256 UNVERIFIED (timeout)** |
| `BIG_P92_Protocol_Code_Audit_Supplement_v1_0_RevA.zip` | 685,413 | `f99057bc61bc8142b01a0e1aae924d32b17b02be8b47394ff1a9554c9d6c1c2c` | Reported SHA-256 PASS |

The Japanese PDF's remaining raw-byte SHA-256 check is **an OPEN verification item, not evidence of a mismatch**. These statuses are drawn from the author's publication report; no new independent post-download verification was performed during this repository documentation update.

See the [publication map](../../docs/publication_map.md), [citation policy](../../docs/citation_policy.md), and [limitations](../../docs/limitations.md).
