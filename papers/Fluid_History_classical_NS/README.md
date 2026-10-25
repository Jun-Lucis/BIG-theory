# BIG Fluid History — Boundary History and Observability in Classical Fluid Dynamics

**Published record:** *Boundary History and Observability in Classical Fluid Dynamics: Prospective Numerical Tests, Classical Comparators, and Predictive Limits*  
**Author:** Jun Lucis (independent researcher)  
**Publication:** Zenodo Preprint v1.0, 25 October 2026  
**Version-specific DOI:** [10.5281/zenodo.23635004](https://doi.org/10.5281/zenodo.23635004)  
**All-version (concept) DOI:** [10.5281/zenodo.23635003](https://doi.org/10.5281/zenodo.23635003)  
**Record and supplementary archives:** https://zenodo.org/records/23635004

This is a **separate, post-B42 study**, not a renumbered B-series paper or a replacement for the B42 and programme-wide preprints. It operationalizes boundary-history, partial-observation and future-response questions within **ordinary incompressible Newtonian Navier–Stokes models**, without introducing an additional BIG constitutive term.

## Main findings and evidence limits

| Stage | Supported finding / archived status | Important qualification |
| --- | --- | --- |
| R0, parallel channel | Analytic counterexamples for selected partial observations; eight frozen preparations retained different pressure/shear responses after returning to the same flow rate | Ordinary Newtonian fluid state is sufficient; no independent BIG memory variable; equally informed BIG-style and standard minimum-norm readouts coincided |
| R0-2D CP0/CP1 | Periodic solver tests against analytic/manufactured solutions (27 settings) and nonlinear evolution (6 settings) | Internal solver verification, not physical validation |
| CP2 confined-cylinder benchmark | Poiseuille 3/3 PASS; cylinder v0.1 **FAIL**; separately frozen supplemental v0.2 16/16 PASS | DFG Re=20 reference is numerical, not an experiment; initial FAIL remains |
| CP3-T | Initial transient and preparation-history numerical failures retained; separately documented additional checks passed | Additional validation does not retroactively change an initial result |
| R3 and readout diagnostics | A restricted three-parameter inlet-history family showed numerical rank 2 for the first pressure harmonic and rank 3 for the full 16-sector pressure readout | Finite-dimensional local sensitivity, not full continuum-state observability; earlier near-null predictions were exploratory |
| R4.4 fresh numerical holdout | `R4_4_HOLDOUT_PASS`. Predicted future drag difference −0.003722830610; new computation −0.003974638900, 6.7639% discrepancy. Earlier OPT6/UNIFORM6 history-estimation RMSE ratio 0.861492 with simulated independent noise | Predeclared model-internal test; algebraic independent replay, not independent PDE integration |
| R4.5 new classical comparator | `R4_5_NUMERICAL_COMPARATOR_SUPPORTIVE`. Under simulated independent noise OPT6/UNIFORM6=0.846611; conventional A-opt6/OPT6=0.846165, implying about 15.38% lower RMSE for A-opt6 | Under strong hypothetical error correlation the rankings changed; ideal-covariance GLS analysis was **post-outcome**, not another formal holdout |
| Separate external PIV reanalysis | In the tested regime, long-history features reduced training error but worsened held-out prediction error | Different experimental Reynolds number and measurement protocol; **not** a direct validation of Re=20 three-pulse cylinder pressure/drag predictions |

**Scientific boundary:** `BIG-specific added predictive value = NOT DEMONSTRATED`. No new physical law, BIG-specific stress/force term, universal sensor-placement advantage, independent Re=20 laboratory replication, or independent full PDE re-execution is established by this record. Results are tied to their respective predeclared, exploratory or retrospective evidence classes.

## Public record and reproducibility

The Zenodo record contains the authoritative English main paper (`MAIN_EN_v1_0.pdf`), a **Japanese reference summary** (`REFERENCE_JA_v1_0.pdf`, not a word-for-word translation), an English technical appendix (`APPENDIX_EN_v1_0.pdf`), archived numerical materials, and release aids (`README_v1_0.md`, `REPRODUCTION.md`, `PUBLIC_SOURCE_MAP_v1_0.csv`, `SHA256SUMS_v1_0.txt`, `verify_release.py`, license and third-party notices).

Numerical archive files on Zenodo include:

- `BIG_Fluid_History_Public_Research_Core_v1_0.zip`
- `BIG_Fluid_History_R0_Originals_v1_0.zip`
- `BIG_Fluid_History_CP0_CP2_Originals_v1_0.zip`
- `BIG_Fluid_History_CP3_Originals_v1_0.zip`

These archives support source-level inspection and specified reproduction paths. They should **not** be described as independent third-party reruns of every study stage. Zenodo—not a privately shared Google Drive—is the public evidence source.

**Rights:** The record's CC BY 4.0 manuscript/data scope does not replace licenses attached to third-party software. In particular, embedded scikit-fem retains its BSD 3-Clause license and notices; consult `LICENSES.md` and `THIRD_PARTY_NOTICES.txt` in the published record. External PIV source measurements are cited at [10.5281/zenodo.20765567](https://doi.org/10.5281/zenodo.20765567) and are not redistributed here.

## How to cite

For the study's numerical values, formal verdicts and limitation statements, cite the **version-specific** Zenodo preprint:

> Lucis, J. (2026). *Boundary History and Observability in Classical Fluid Dynamics: Prospective Numerical Tests, Classical Comparators, and Predictive Limits*. Preprint, v1.0. Zenodo. https://doi.org/10.5281/zenodo.23635004

For the overall BIG programme, use the separate [flagship preprint](https://doi.org/10.5281/zenodo.23486616). The Fluid History study does not revise B42's overall formal science verdict **NONE** or the status of proposed, unperformed physical experiments.

See also: [Publication map](../../docs/publication_map.md) · [Citation policy](../../docs/citation_policy.md) · [Limitations](../../docs/limitations.md).
