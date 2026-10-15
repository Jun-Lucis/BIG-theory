# B3.1–B5 correction and publication register

**B5 follow-up — 15 October 2026 (JST): clarified dataset v1.1 published.** [DOI 10.5281/zenodo.23381643](https://doi.org/10.5281/zenodo.23381643) now serves the corrected documentation package. Its public ZIP matches the upload; the original CSV and representative PNG remain byte-identical. [Original v1 DOI 20575991](https://doi.org/10.5281/zenodo.20575991) remains archived. This supersedes the description-only state recorded in the initial audit below. See the [publication verification](B5_v1_1_publication_2026_10_15.json).

**Update — 15 October 2026 (JST): B3.1 file mismatch resolved.** The existing v2 record now serves the corrected seven-page manuscript under the same DOI. Its public download was checked byte for byte. The 14 October observations below are retained as the historical audit; see the [file-correction verification](B3_1_file_correction_2026_10_15.md) for the new filename and hash.

**Checked:** 14 October 2026 (UTC). Public Zenodo metadata and downloaded files were reconciled with the original and prepared correction files. This register distinguishes a corrected description from a corrected downloadable manuscript.

## Public record status at the 14 October audit

| Study | Current record | Original record | Verified state |
| --- | --- | --- | --- |
| B3.1 | [23342986](https://doi.org/10.5281/zenodo.23342986) | [20465842](https://doi.org/10.5281/zenodo.20465842) | Title/description corrected; downloadable PDF still identical to the original. Corrected PDF publication remains pending. |
| B4.1 | [23342902](https://doi.org/10.5281/zenodo.23342902) | [20541748](https://doi.org/10.5281/zenodo.20541748) | Corrected downloadable PDF matches the prepared correction. |
| B4.3 | [23342705](https://doi.org/10.5281/zenodo.23342705) | [20564435](https://doi.org/10.5281/zenodo.20564435) | Corrected downloadable PDF matches the prepared correction. |
| B5 | [20575991](https://doi.org/10.5281/zenodo.20575991) | Same record | Description clarified; original ZIP, CSV, figure, and archived README retained. No v1.1 package published. |

The B3.1, B4.1, and B4.3 current records share their respective original concept-record families. Links above identify specific record versions rather than an unspecified latest-version redirect.

## What the corrections mean

- **B3.1:** retain original figures and separate one-parameter position fits with intercepts. The proposed length scaling does not follow from the stated local balance, which cancels the length after substitution. The printed negative-sign source-free prototype also fails the proposed positive quadratic balance. The original executed B3.1 implementation remains unauthenticated; B4 evidence does not supply that missing provenance.
- **B4.1:** correct the printed negative quartic coefficient to the numerically supported regularized positive `+4 gamma` finite-volume prototype. Eight fields support that operator; four conditions have summary-level checks only. Selected finite-grid near-two signatures and loss of good-layer detection are retained, without establishing universality or an exact collapse threshold.
- **B4.3:** document the positive-flux prototype, source, regularization, boundary conditions, and stopping convention; repair figure assignments/cropping. The nine cases are six pilot fields plus three B4.1 reuses; the latter use 100 shells versus 120 for the pilot cases. The reference amplitude is conditional, and the historical classifications are retained.
- **B5:** scope the mobility scan to finite-time snapshots at `t = 0.24`, with all nine runs stopping at the step cap. Explain positive-contour finite-window fitting and selection sensitivity. The description no longer suggests an established critical mobility, exact support-edge exponent, or universality class. The original solver and fit source remain incompletely verified.

The B4 `+4 gamma` evidence must not be extrapolated to B3.1 or B5. B5 has separate negative-coefficient scalar-RHS consistency evidence, with the provenance limits described in its [paper entry](../papers/B5_mobility_dependent_boundary_exponents/README.md).

No archived numerical value, frozen gate, or formal PASS/FAIL/INCONCLUSIVE result is regraded by these documentation corrections. No new PDE trajectories were run for this update. Historical status snapshots and frozen protocols remain preserved.

## Downloaded-file verification at the 14 October audit

SHA-256 values are for complete files, not extracted text.

| File role | Bytes | SHA-256 | Result |
| --- | ---: | --- | --- |
| B3.1 PDF served by record 23342986 | 670724 | `9f7aa1403404b962a3206f1dbf5fd3484db21820c7db07bce078c90f942a11ec` | Matches original six-page PDF; does not match corrected preparation. |
| B3.1 prepared corrected PDF | 1506101 | `c47924f4b4e1735b9639a682cdd154b5480a52a316277b46b11b6ca01b546f68` | Seven-page preparation; publication not verified. |
| B4.1 PDF served by record 23342902 | 1200042 | `7f6aece001ead7e45ce800593c2ac4624ecce5d176c06999590bde8d79d52226` | Matches corrected preparation. |
| B4.3 PDF served by record 23342705 | 1781603 | `e80dff5b5797bad4ad37503c8157e4a98e5a1cafd7abe02e96261084de5a77c1` | Matches corrected preparation. |
| B5 original public ZIP | 97305 | `ea40eb63c56992f5e241ceb1895d95acddcdfba2c88deaef62594141500cc5ab` | Original archive retained; description-only clarification. |

The intended B3.1 corrected filename is `BIG_B3_1_DOI_Linked_Preparation_EN_20261013.pdf`. As checked, record 23342986 instead serves `BIG-B3.1 Boundary-Layer Scaling and Quadratic-Layer Interpretation in Degenerate Mixed-Gradient Dissipative Fields (2) (1).pdf`.

## Publication follow-up

The B3.1 pending action recorded in the 14 October audit was completed on 15 October 2026 (JST). Zenodo's published-file correction workflow replaced the mistaken attachment in the existing v2 record, retaining DOI 10.5281/zenodo.23342986 and the separately archived original v1. A public dated note documents the repair. The publication copy updates preparation-only identity text while preserving the corrected scientific pages and figures.

For the wider numbering/DOI check, see the [DOI inventory audit](doi_inventory_audit_2026_10_14.md).

## B5 v1.1 publication follow-up

Version 1.1 is a Dataset containing the unchanged numerical CSV/PNG, the matching archived parameter file, revised README, original README for comparison, change log and member checksums. The archive `BIG_B5_Clarified_Submission_Package_v1_1.zip` has 82,915 bytes and SHA-256 `3d0860d1d188495f04dbfba3e5e229c617ea3393abd9505df08a3dcbe92fd2b9`. The public download was verified at `2026-10-14T23:52:02.564644+00:00` (15 October in Japan). The new package does not contain authenticated original solver/fitting code and does not certify stationary convergence.

The wider [metadata register through B41](zenodo_metadata_maintenance_2026_10_15.md) separates this completed publication from proposed metadata edits that remain unapplied.
