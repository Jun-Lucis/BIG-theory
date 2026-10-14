# BIG-B5: Mobility-Dependent Boundary Exponents

**Published title:** *BIG-B5: Numerical Observation of Mobility-Dependent Free-Boundary Exponents in Degenerate Mixed-Gradient Dissipative Fields*

**DOI:** [10.5281/zenodo.20575991](https://doi.org/10.5281/zenodo.20575991)

### Publication status — checked 14 October 2026 (UTC)

The existing Zenodo description has been clarified. The original ZIP, numerical summary, and representative figure remain unchanged. This is a **description-only clarification under the same DOI**; no corrected v1.1 package or standalone revised B5 paper has been published in this record.

See the [B3.1–B5 correction register](../../docs/publication_corrections_B3_1_B5_2026_10_14.md) and [DOI inventory](../../docs/doi_inventory_audit_2026_10_14.md).

### What the archive contains

`BIG_B5_Zenodo_Submission_Package.zip` contains:

- `data/B5_11_summary_all.csv`
- `figures/B5_11_mean_nu_vs_m.png`
- `README_BIG_B5.txt`

The archived README retains its original stronger wording. Consult the clarified description and the limits documented here when interpreting it. The public CSV and PNG match the corresponding original B5.11 exports byte for byte.

### Retained numerical observation

Nine mobilities, `m = 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.90, 1.00`, were evaluated at `N = 220`, `gamma = 0.10`. All nine runs reached `max_steps = 240000`, corresponding to `t = 0.24` with `dt = 1e-6`. Stationary convergence was not certified.

The exponents are effective finite-window fits associated with a positive contour at `10^-4` of each field maximum. The selected mean falls from `2.160614` at `m = 0.50` to approximately `1.80–1.82` at `m = 0.80–1.00`.

The retained fraction varies from approximately `68.88%` to `100%` across mobilities: 3004 of 3568 exported fits are retained overall. The broad decline also appears with all exported fits, but the crossing of two depends on selection: the selected mean crosses within `[0.55, 0.60]`, compared with `[0.60, 0.65]` for all fits.

### Implementation evidence and limits

A retrospective periodic central-difference reconstruction with the negative `-gamma` coefficient reproduces the saved scalar RHS RMS norms for all nine snapshots to numerical precision. A `+4 gamma` candidate differs by approximately `1.79–5.98%`. Scalar agreement does not authenticate the executed source, identify the full RHS vector, or verify the original fitting code. The B4 positive-flux correction must not be applied to B5 by analogy.

These are finite-time, finite-resolution observations. They do not establish an exact support-edge exponent, critical mobility, universality class, or continuum limit. Verification of the original solver and fitting code remains incomplete.
