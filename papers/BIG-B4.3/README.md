# BIG-B4.3

## Finite-Width Quadratic-Layer Signatures under Joint Dissipation and Quartic-Flux Variation

B4.3 reports selected finite-width approximately quadratic layers on a `3 × 3` grid: `mu ∈ {0.3, 0.7, 1.0}` and `gamma ∈ {0.5, 1.0, 2.0}`. Effective mean exponents remain near two under the historical shell-selection and good-layer/near-two fallback rules; shell span and relative amplitude error vary with the parameters.

### Publication status — checked 14 October 2026 (UTC)

- **Corrected report:** [10.5281/zenodo.23342705](https://doi.org/10.5281/zenodo.23342705). The downloadable PDF matches the prepared corrected report byte for byte.
- **Original report:** [10.5281/zenodo.20564435](https://doi.org/10.5281/zenodo.20564435).
- [Correction register and file verification](../../docs/publication_corrections_B3_1_B5_2026_10_14.md).

### Equation and data-lineage clarification

The original manuscript printed `-gamma div(|grad(phi)|² grad(phi))`. The numerically supported finite-volume implementation instead has a positive `+4 gamma` quartic-gradient face flux, `epsilon = 1e-12`, a Gaussian source, and zero outer-face flux.

Six recovered pilot fields give stationary residuals near `1e-8` with the positive-flux operator; the printed negative coefficient in the same stencil gives approximately `0.0021–0.0103`. Three additional `gamma = 1` fields were recovered as **reuse from B4.1** and checked. The nine summary conditions therefore represent six pilot cases plus three reused cases. The reused column uses 100 shells, compared with 120 for the pilot cases.

This extends the six-field scope of the [12 October audit](../../docs/B4_3_printed_equation_vs_numerical_solver_audit_2026_10.md). Complete original run-to-source authentication remains unresolved, and this operator evidence is not assigned to B3.1 or B5.

### What the correction changes

- Corrects the equation/implementation description and documents regularization, source, boundary conditions, and stopping convention.
- Corrects Figure 5–7 assignments and the clipped axis in Figure 1 of the report.
- Distinguishes six pilot cases from three B4.1 reuses and their different shell counts.
- Presents `A_ref = sqrt(mu/(96 gamma))` as a conditional local approximation.

The original numerical table, selection thresholds, fallback rule, and Stable/Recovered, Compressed, and Residual labels are preserved. These are historical diagnostic classifications, not a dynamical-stability theorem. No new PDE trajectories or retrospective reclassification were performed.

### Limits

The results do not establish exact compact support, dynamical stability, geometric universality, a continuum limit, or a joint `gamma/mu` scaling law.

Related reports: [B3.1](../BIG-B3.1/README.md), [B4.1](../BIG-B4.1/README.md), and [B5](../B5_mobility_dependent_boundary_exponents/README.md).

### Archived representative figure

![B4.3 State Map](../../figures/B4_3/B4_3_state_map.png)

The image retains the historical finite-grid classification labels; the interpretation limits above apply.
