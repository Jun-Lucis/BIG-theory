# Boundary Information Geometry (BIG)

**Boundary Information Geometry (BIG)** is an exploratory mathematical and numerical research programme by **Jun Lucis**, an independent researcher. It investigates explicitly specified boundaries and boundary-related observables in reduced models: localized field profiles, competing geometric costs, interactions, retained history, and finite-window response geometry.

These studies are **distinct model families, not one universal governing equation**. The published record contains both successful restricted numerical tests and retained **FAIL**, **INCONCLUSIVE**, and not-run outcomes. A BIG-specific physical law distinguished from equally informed conventional models has **not** been independently calibrated or experimentally established.

🇯🇵 [日本語での概要 / Japanese overview](docs/BIG_overview_ja.md)

## Start here — the programme-wide preprint

**Boundary Information Geometry: Distinct Model Families, Preserved Failures, and a Path toward Physical Measurement**  
*Jun Lucis · 2026 · Preprint v1.0 · CC BY 4.0*

- **[Zenodo record and three PDFs](https://zenodo.org/records/23486616)** — English main paper, Japanese reference translation, and English technical appendix.
- **[Version-specific DOI: 10.5281/zenodo.23486616](https://doi.org/10.5281/zenodo.23486616)**.
- [Technical overview](docs/technical_summary.md) · [Limitations and scope](docs/limitations.md) · [Full publication map](docs/publication_map.md).

The flagship is a synthesis and a source guide; it does not supersede the model-specific equations, frozen protocols, corrections, or citable original papers.

## New independent preprint — Fluid History (25 October 2026)

**Boundary History and Observability in Classical Fluid Dynamics: Prospective Numerical Tests, Classical Comparators, and Predictive Limits**  
*Jun Lucis · Zenodo Preprint v1.0*

- **[Version-specific DOI: 10.5281/zenodo.23635004](https://doi.org/10.5281/zenodo.23635004)** · [All-version DOI](https://doi.org/10.5281/zenodo.23635003).
- [Research scope, preserved FAIL/PASS results and reproduction guide](papers/Fluid_History_classical_NS/README.md) · [Publication map](docs/publication_map.md).

This post-B42 study uses **ordinary Navier–Stokes/Newtonian fluid equations** to examine whether partial pressure observations can read out preparation history and predict later response. The prospective R4.4/R4.5 numerical tests passed their frozen gates; a **conventional A-optimal six-sector layout outperformed** an earlier six-sector candidate under simulated independent noise. Initial failures, post-outcome analyses and independent-replay limits remain explicit. **No BIG-specific physical law or additional predictive value over equally informed classical methods was demonstrated.** The archive is public on Zenodo; access to the author's private Drive is not required.

## What the research has examined

| Model family | Examples of the question studied | Evidence boundary |
| --- | --- | --- |
| **Localized fields and geometry (B3–B9)** | Boundary-layer profiles, anisotropic finite-time behavior, perimeter versus nonlocal repulsion | Model-specific operators, source corrections and finite-resolution results; no calibrated nuclear or universal field law |
| **Interaction, selection and traces (B10–B18)** | First encounter versus sustained capture; designed retention, writing and reading of history | Constructed stochastic/PDE models; not biological heredity, quantum measurement or measured material memory |
| **Operator response and transfer (B19–B29)** | Finite-window response-zero sets, local geometry, branch transfer and reconfiguration | Parameter-space quantities; some forward tests pass, other transfers fail or are inconclusive |
| **Modal and relational response (B30–B41)** | Angular response, complex transfer, timing, measurement weighting and finite-parameter prediction | Restricted numerical families with separately preserved PASS/FAIL; no universal physical clock or wave |
| **Identifiability and physical eligibility (B42)** | What can independently measured structure predict, and what can distinguish a model from ordinary constitutive theories? | B42 overall formal science verdict **NONE**; the proposed CA16 material experiments have not been performed |

For the source-defined equations and results, begin with the [publication map](docs/publication_map.md), rather than interpreting this overview as a single model.

## Representative outcomes — successes and limits together

- **A local boundary layer is not automatically an exact free-support theorem.** B3–B5 include finite-grid near-quadratic profiles and source/implementation corrections; their equations and numerical provenance must be identified by version. [Corrections and scope](docs/publication_corrections_B3_1_B5_2026_10_14.md).
- **Shape-energy competition can create a separation-like barrier in a reduced model.** B9 balances perimeter and a specified nonlocal repulsive term. It is not a quantitative microscopic fission model. [B9 paper entry](papers/B9_fission_like_metastability/README.md).
- **Local response geometry can be predictive without transferring universally.** B20–B23 measure finite-window zero sets in a selected parameter subspace; the B23 aggregate verdict remains **INCONCLUSIVE**. [B23 entry](papers/B23_cross_branch_geometric_prediction/README.md).
- **Later fresh successes do not erase earlier failures.** A restricted perimeter transfer passed within a shape family but the B26 topology-straddling transfer failed; B41 P2 **FAIL** and P3 separate **PASS** are both retained. [B26 entry](papers/B26_topology_realized_fixed_sigma_transfer/README.md) · [B41 status](docs/research_status_update_B41.md).
- **External-data tests give mixed, bounded information.** B19E did not establish incremental predictive value over a strong external numerical-flow baseline; EV6 supported a frozen interpolation of previously collected experimental gravity-current trajectories, **not** a distinctive BIG material mechanism. [B19E](papers/B19E_external_flow_validation/README.md) · [EV6](papers/EV6_external_numerical_holdout/README.md).
- **Physical correspondence remains open.** The B42/CA16 assessment identifies calibration/identifiability limits, including a reciprocal completion equivalent to a conventional distributed-Maxwell model. Proposed microgel-interface measurement protocols are conditional and unperformed. [B42 preprint](https://doi.org/10.5281/zenodo.23432804) · [Flagship preprint](https://doi.org/10.5281/zenodo.23486616).

These examples are not a count or vote on the truth of BIG. Formal verdicts belong to their respective frozen protocol and evidence class.

## Explore the B-series and its records

- **B3–B26 (+B23A):** [Research status map](docs/research_status_map_B3_B26.md) · [日本語版](docs/research_status_map_B3_B26_ja.md).
- **B27–B36:** [Later-stage research status](docs/research_status_update_B27_B36.md) · [日本語版](docs/research_status_update_B27_B36_ja.md).
- **B37–B38:** [Timing and measurement duality status](docs/research_status_update_B37_B38.md).
- **B39:** [Relational clocks and metric drift](docs/research_status_update_B39.md).
- **B40:** [Clock-family transfer and reconstruction](docs/research_status_update_B40.md).
- **B41:** [Trajectory-space response geometry](docs/research_status_update_B41.md).
- **B42:** [Integrated mathematical/physical eligibility synthesis](https://doi.org/10.5281/zenodo.23432804).
- **All records and their DOI versions:** [Publication map](docs/publication_map.md). B6 mapping and a standalone B37 publication remain unresolved where so marked; no DOI is inferred.

The folders [`papers/`](papers/), [`code/`](code/) and [`figures/`](figures/) retain the existing source-specific organization. Full manuscripts, versioned data and supplemental reproducibility archives are primarily referenced through Zenodo.

## Reproducibility, corrections and citation

**Working audit position:** much of the preserved material is reproducible in principle; **independent full solver rerun auditing is not complete**. Archived-output checks, hash comparisons, frozen prospective experiments, and independent physical measurements are not interchangeable.

- [Limitations and outstanding issues](docs/limitations.md)
- [Original B3.1–B5 corrections](docs/publication_corrections_B3_1_B5_2026_10_14.md)
- [B19–B41 publication synchronization and audit scope](docs/publication_sync_B19_B41_2026_10_19_JA.md)
- [B22, B23 and B24–B25 Phase-I v1.1 changes](docs/publication_revisions_B22_B23_B24B25_2026_10_19_JA.md)
- [Citation policy](docs/citation_policy.md) · [Repository citation metadata](CITATION.cff)

**Citation guidance:** cite the [flagship v1.0](https://doi.org/10.5281/zenodo.23486616) when discussing this programme-wide synthesis; for any specific numerical quantity, field equation, correction or scientific verdict, cite its **version-specific original study**. For the repository as a living index, cite this GitHub repository. These are not interchangeable citations.

## Questions that may intersect with other research

Relevant questions also arise in nonlinear PDEs, geometric energy models, interface rheology, state-space observability, inverse problems and measurement science. For example, one may ask whether an independently imaged structure descriptor is sufficient to forecast a later mechanical response under controlled preparation histories, or whether an apparently new response law is equivalent to a standard internal-variable model.

The later papers discuss **conditional** ways to examine such questions. There is no ongoing BIG laboratory trial or expectation that a reader undertake one. Related work, critique, an ordinary-model explanation, or an independent negative result can stand on its own scientific merits.

## Author and related methodology

**Jun Lucis** — independent researcher.

The research-development methodology that emerged during parts of the programme is documented separately as **[Failure-Preserving AI-Assisted Research](https://github.com/Jun-Lucis/failure-preserving-research)**. Methodological documentation does not certify the mathematical or physical correctness of BIG.
