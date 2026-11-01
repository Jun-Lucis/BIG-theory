# BIG-B5: Mobility-Dependent Boundary Exponents

**Current published title (v1.2):** *BIG-B5: Mobility-Dependent Free-Boundary Exponents in a Mixed-Gradient Numerical Field — Revised Source-Linked Replication, Fit-Definition Sensitivity, and Conditional Linearized-PDE Limits*

**Current revised preprint v1.2:** [10.5281/zenodo.23850139](https://doi.org/10.5281/zenodo.23850139) · [Zenodo files](https://zenodo.org/records/23850139) · CC BY 4.0.

**Historical clarified dataset v1.1:** [10.5281/zenodo.23381643](https://doi.org/10.5281/zenodo.23381643)

**Original dataset v1.0:** [10.5281/zenodo.20575991](https://doi.org/10.5281/zenodo.20575991)

**Version-family DOI:** [10.5281/zenodo.20575990](https://doi.org/10.5281/zenodo.20575990)

**Full B5 v1.2 audit:** [source/trajectory replication, CP7 controls, conditional linearization proof, evidence limits](../../docs/B5_v1_2_source_replay_grid_and_fit_audit_2026_11_01.md).

### Current publication status — 1 November 2026

B5 **v1.2 is published as a Preprint** and as a **new version** of the original B5 record, not an independent record.
Zenodo lists exactly three files:

- `BIG_B5_Revised_Preprint_EN_v1_2.pdf` — English main preprint
- `BIG_B5_Japanese_Reference_v1_2.pdf` — Japanese reference translation
- `BIG_B5_v1_2_Reproducibility_Supplement.zip` — original B5 source/data provenance and CP6/CP7 audit results

The original nine `N=220, T=.24` finite-grid mobility cases and their historical results are **unchanged**. Recovered Colab source and output fields were matched; **9/9** full source-aligned numerical trajectory replays (with a disclosed FTZ/DAZ variant) and original contour-fitting computations reproduced the records. CP7 supplies **22** short numerical controls, and **54** fit-definition comparisons on the same archived final fields. A separate smooth positive profile shows that the *formal negative-quartic-flux equation* is **not forward parabolic for every positive smooth state**, with a **conditional frozen-profile linearized `L²` semigroup obstruction** under explicit operator domain assumptions. These findings **do not prove** nonlinear continuum blow-up or instability of the original elliptical initial-value problem. Exact universal boundary exponents and external physical prediction remain unestablished.

### Historical v1.1 publication status — 15 October 2026 (JST)



The clarified documentation package v1.1 is published as a **Dataset**. Its public ZIP was downloaded and verified byte for byte against the upload. The numerical CSV and representative PNG are byte-identical to the original v1 archive. The original June record is retained in the same concept family.

Version 1.1 adds the matching archived parameter file, a scope-corrected README, a change log, the original README for comparison, and per-file SHA-256 checksums. It is a documentation clarification of the existing finite-time results; no new PDE trajectories or authenticated original solver/fitting source are supplied.

See the [publication verification](../../docs/B5_v1_1_publication_2026_10_15.json), [B3.1–B5 correction register](../../docs/publication_corrections_B3_1_B5_2026_10_14.md), and [ordered metadata maintenance register](../../docs/zenodo_metadata_maintenance_2026_10_15.md).

### Historical v1.1 clarified dataset contents

`BIG_B5_Clarified_Submission_Package_v1_1.zip` contains:

- `data/B5_11_summary_all.csv`
- `figures/B5_11_mean_nu_vs_m.png`
- `parameters/B5_11_params.json`
- `README_BIG_B5.txt`
- `CHANGELOG_v1_1.txt`
- `previous_versions/README_BIG_B5_v1_original.txt`
- `FILE_CHECKSUMS_SHA256.txt`

The complete ZIP has 82,915 bytes and SHA-256 `3d0860d1d188495f04dbfba3e5e229c617ea3393abd9505df08a3dcbe92fd2b9`. Its public Zenodo MD5 is `40cabd832c66f8fd4f65eb8009d4f7d1`. Download verification completed at `2026-10-14T23:52:02.564644+00:00` (15 October in Japan).

The original v1 ZIP contains only the CSV, PNG and original README. Its stronger wording is retained as archival history; consult the v1.1 documentation for interpretation and limitations.

### Retained numerical observation

Nine mobilities, `m = 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.90, 1.00`, were evaluated at `N = 220`, `gamma = 0.10`. All nine runs reached `max_steps = 240000`, corresponding to `t = 0.24` with `dt = 1e-6`. Stationary convergence was not certified.

The exponents are effective finite-window fits associated with a positive contour at `10^-4` of each field maximum. The selected mean falls from `2.160614` at `m = 0.50` to approximately `1.80–1.82` at `m = 0.80–1.00`.

The retained fraction varies from approximately `68.88%` to `100%` across mobilities: 3004 of 3568 exported fits are retained overall. The broad decline also appears with all exported fits, but the crossing of two depends on selection: the selected mean crosses within `[0.55, 0.60]`, compared with `[0.60, 0.65]` for all fits.

### Historical v1.1 implementation evidence and limits (superseded by v1.2 source recovery)

A retrospective periodic central-difference reconstruction with the negative `-gamma` coefficient reproduces the saved scalar RHS RMS norms for all nine snapshots to numerical precision. A `+4 gamma` candidate differs by approximately `1.79–5.98%`. Scalar agreement does not authenticate the executed source, identify the full RHS vector, or verify the original fitting code. The B4 positive-flux correction must not be applied to B5 by analogy.

These are finite-time, finite-resolution observations. They do not establish an exact support-edge exponent, critical mobility, universality class, or continuum limit. At this v1.1 historical checkpoint, original solver and fitting-code verification was incomplete. The subsequently published v1.2 includes recovered source and source-aligned independent numerical replays, subject to the distinct limitations stated above.
