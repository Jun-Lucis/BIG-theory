# BIG-B4.1

## Selected Quadratic-Layer Signatures and Loss of Good-Layer Detection in Mixed-Gradient Fields

B4.1 reports a twelve-condition dissipation scan at `gamma = 1`. Under the historical diagnostic rules, selected approximately quadratic signatures remain detectable while the span of the detected good region decreases across the higher-`mu` part of the scan.

### Publication status — checked 14 October 2026 (UTC)

- **Corrected report:** [10.5281/zenodo.23342902](https://doi.org/10.5281/zenodo.23342902). The downloadable PDF matches the prepared corrected report byte for byte.
- **Original report:** [10.5281/zenodo.20541748](https://doi.org/10.5281/zenodo.20541748).
- [Correction register and file verification](../../docs/publication_corrections_B3_1_B5_2026_10_14.md).

### Equation and implementation clarification

The original manuscript printed a negative quartic-flux coefficient, `-gamma`. Eight recovered original fields strongly support a regularized positive `+4 gamma` finite-volume operator through stationary-residual checks with the recovered B4.3 pilot spatial operator. Authentication of the original executed B4.1 notebook and ray-fit code remains unresolved.

Eight conditions were checked with fields and shell summaries; `mu = 0.1, 0.2, 0.4, 0.8` remain checked against restored summaries only. The table retains all 34 numerical cells and the two missing good-region widths.

### Retained observations and limits

- No good region is detected at `mu = 1.0, 1.1` under the historical criteria, although near-two traces remain.
- The near-two and good diagnostics use different exponent windows and are not a simply nested pair.
- Loss of good-layer detection is conditional on the finite grid, selection criteria, and measurement procedure; it does not establish a continuum collapse threshold or dynamical instability.
- The original four figures, thresholds, state labels, and numerical values are retained. The correction ran no new PDE trajectories and did not reclassify the archived cases.

These are selected finite-grid observations. Exact compact support and a universality class are not established.

Related reports: [B3.1](../BIG-B3.1/README.md), [B4.3](../BIG-B4.3/README.md), and [B5](../B5_mobility_dependent_boundary_exponents/README.md).
