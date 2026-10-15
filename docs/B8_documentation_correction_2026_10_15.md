# B8 documentation and aggregation correction — 15 October 2026

Dataset v0.2 is published at [DOI 10.5281/zenodo.23385079](https://zenodo.org/records/23385079).
The [original DOI 10.5281/zenodo.20645317](https://doi.org/10.5281/zenodo.20645317) remains archived in the same version family.

The published ZIP was independently downloaded through Zenodo's public Download
control and matched the uploaded ZIP byte-for-byte. Its checksum and scope are
recorded in [the machine-readable verification](B8_v0_2_publication_2026_10_15.json).

## Corrections

| Audit item | Corrected representation | Preserved evidence |
| --- | --- | --- |
| B8-A01 | Nine comparison labels and 45 prediction labels now identify exponential models | All coefficients, predictions, residuals, LOO values and ranking |
| B8-A02 | 125 missing ratio identifiers restored by unique archived case matching; five-point figure repaired | Every other prediction cell and all originally nonempty identifiers |
| B8-A03 | N96 pooled history contains all 35 existing per-ratio rows instead of the earlier 14-row subset | Per-ratio source cells and original partial aggregate |

Two figures were redrawn from stored values, with no regression refit.
The separate genuine log-log relation
`A_c approximately 0.745980 * E24_c^0.575225` and its original figure remain unchanged.

The previous 14-row pooled file had reserialized 148 numeric text cells relative
to its per-ratio sources. The complete aggregate now copies source text directly.
The largest absolute difference is `5.684341886080802e-14`, in `elapsed_sec`.
These representation differences are listed in `POOLED_HISTORY_SERIALIZATION.json`;
the prior pooled file is retained byte-for-byte.

## Preservation and verification

Of the original 304 file members, 296 are byte-identical in the current release.
All eight replaced originals are retained under `previous_versions/v0_1`.
The release contains 318 files, a current manifest, source hashes, member
checksums, a change log and a stdlib-only verification script.
The saved ZIP was extracted into a separate directory and its packaged verifier
passed. The two changed figures were visually inspected.

- ZIP: `BIG_B8_Documentation_Corrected_Dataset_v0_2.zip`
- Bytes: **4,182,401**
- SHA-256: `e8461005e9eb46598be2e026f66da4cb20eb6eb81a09ad3370a2ea4bd99b5a89`
- MD5: `a2da2ce63fe51d9d2763e81270262eb3`

## Retained limits

This resolves the specified display, identification and pooled-history defects
in the new public representation. The original solver and ray-fitting code are
still unauthenticated, and the lightweight archive still excludes heavy final fields.
The 30-model comparison on five N96 cases remains exploratory. E24_c uses A_c
itself and is not a fully independent predictor. Initial analytic ellipse
curvature is distinct from evolved-boundary curvature.

The observations remain finite-time and finite-resolution. This release adds
no PDE trajectories, regression fits, continuum result, asymptotic-stability
claim or external physical validation. Formal research verdicts are unchanged.
The historical CP10 issues and original publication remain preserved; these
three public-documentation corrections do not close unrelated provenance issues.
