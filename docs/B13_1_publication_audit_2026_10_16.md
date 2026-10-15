# B13.1 version 1.1: methods and reproducibility clarification

Published version 1.1: https://zenodo.org/records/23400328. The single complete ZIP re-download matches the saved release byte for byte; CRC and all 155 internal SHA256 checksums pass. ZIP SHA-256: `7c7e6334db613400e77060762247d2b4be5a2a0e039439615c9f9492db28ead4`.

This edition preserves the original numerical outcomes, all 35 CSV files (5,532 rows), all 11 JSON summaries, and the eleven paper figures. It adds the recovered original notebook, unchanged computational function extracts, a portable adapter and audit receipts. No new stochastic trajectories were generated. Assessment: basically reproducible; independent full rerun audit not yet completed.

| Topic | Clarification |
|---|---|
| Rotation and the cos² reference | The full-plane energy, gradient, isotropic noise, radial norm guard and rotated absolute-component classifier are rotation-equivariant in distribution. A response depending only on θ−α can differ from cos²(θ−α). Residuals against cos² do not establish covariance failure. Finite Monte Carlo curves on different shifted grids are not identical arrays. |
| Bias fit | The additional bias is inside the logit: κ cos(2δ)−κc+bias. The separate c and bias are non-identifiable at fixed κ. Compare c_eff=c−bias/κ or the fitted curve. The original bias row is retained, including its omitted bias −0.0192310648. |
| Distinct calibrations | The pooled baseline fit is κ=3.7410978333, c=0.0033597885. Sequential/cloud tests use the scaling-grid fit κ=3.6912810588, c=−0.0142857410. |
| Centroid width | The actual notebook averages unnormalized final vectors. Their radial norms vary. R=exp(−w²/2) holds for the population directional resultant of a unit-radius Gaussian-angle cloud, not arbitrary raw-state centroid norms. The actual 13.7° value is an equivalent width under assumptions, not an independent angular-width measurement. |
| RMSE aggregation | Reset comparison uses 75 raw condition rows per mode, 225 overall. Convolution uses five angle-averaged probabilities per target and fits width to those same five points. Their RMSEs have different denominators. |
| Uncertainty | Condition standard deviations are not standard errors. No held-out validation or fitted-width confidence interval was established. The cloud fit is descriptive. |
| CSV roundtrip | Recomputing five-degree bins from reloaded raw angle columns moves ten half-bin ties among 625 rows through floating-point rounding. The resulting pooled κ is about 3.742041 rather than 3.741098. Use the stored bin assignments and collapse table for the stored-data fit. Probabilities and original outputs are unchanged. |

The deterministic archive audit passed 125 groups / 24,702 compared values. Provenance, fixed-point gradient/rotation identities and recovered stored-input analysis passed a further 75 groups / 8,852 values. These checks are not a full rerun of the stochastic experiment.

The recovered `Untitled67.ipynb` has SHA-256 `b55cedfcc7a6037a5c1e27aacc65e3aa06510af2c5b629d770bb2bf65427a170`. Thirty distinct computational names appear in 31 preserved definitions. Earlier duplicate cells, Drive setup, empty cells and pasted output are documented in `source_provenance.json`; the complete original notebook retains them. The adapter changes output paths, display setup and explicit execution control only. The original runtime lock was not recovered; the audit environment is recorded separately.

The original public archive is retained byte for byte, SHA-256 `2832b2246036ca43fa8615e1ce1914d06e1e8ad8c57043309e97677aae75cd4a`. All 82 recovered Drive result files match a published file byte for byte. All eleven original and clarified PDF figures match the original PNG RGB pixels.

Repository: https://github.com/Jun-Lucis/BIG-theory

Original Zenodo version: https://doi.org/10.5281/zenodo.21108338
