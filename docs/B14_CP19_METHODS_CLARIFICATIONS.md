# B14 version 1.1: methods, provenance and interpretation

Assessment: basically reproducible; independent full stochastic rerun audit not yet completed. No new stochastic trajectories were generated and no formal scientific PASS/FAIL outcome was changed.

| Topic | Clarification |
|---|---|
| Table layout | The original Table 4 extended beyond the page and clipped its final column. Compact, wrapped headings restore all seven columns without changing the values. Table 2 is fitted within the text margins as well. |
| Fusion norm loss | The stable map explicitly rescales the fused output to `norm(raw_sum) * (1 - 0.35 * positive_overlap)`. Hence compression loss equals `0.35 * positive_overlap` by construction. The overlap-loss plot illustrates a prescribed operator property, rather than discovering an independent scaling law. |
| Shape diagnostics | Correlation and fidelity in the saved outputs are normalized uncentered inner products (cosine similarities), not centered Pearson correlations. They do not measure retained amplitude. |
| Division | Complementary logistic masks define assigned references. Independent map-level noise, nonnegative flooring and periodic heat smoothing follow efficiency/leakage mixing. Total retention combines daughter L2 norms in quadrature; it is not a conserved mass fraction. |
| Ensemble persistence | Without noise or an active floor, complementary partitioning implies `D1 + D2 = (efficiency + leakage) * T(parent)`. The mean descendant after generation g is `((efficiency + leakage)/2)^g * T^g(initial)`. The amplitude factor cancels in normalized similarity. Noisy policy differences should be assessed against this prescribed baseline. |
| Noise/grid | Writing uses per-grid independent Gaussian increments scaled by sqrt(dt), without spatial mesh normalization. Division adds Gaussian noise once per map. FFT smoothing is deterministic. No continuum-noise or mesh-convergence claim follows from this fixed N=256 experiment. |
| Archive representations | The old public package was reserialized and reduced: fields were omitted, and its profile matrix holds the 960 final-generation rows. The recovered original matrix holds all 1,905 profiles, including initial and intermediate generations. All 329,270 compared common numeric values in 14 public CSVs agree with the corresponding original outputs. Byte identity between these two representations is not claimed. |
| Recovered source | The original `Untitled68.ipynb` supplies 38 unchanged computational definitions / 31 distinct names and the original parameter calls. The unstable earlier B14.1 attempt is preserved as historical source; the opt-in stable-paper replay skips it and uses B14.1b. |
| Identity and uncertainty | A lineage row uses the composite identity scenario, seed, generation and cell_id. Cell IDs repeat across generations. Reported spread across conditions or seeds is not a standard error. |

The saved-result/source audit passed 165 groups / 36,176 values. It checks recovered function text, saved writing-field diagnostics and response integrals, the stable fusion operator on saved inputs, division identities, robustness aggregation and all 1,905 lineage-profile metrics and seed summaries. All 19 paper image panels match the original published-source PNG RGB pixels. The clarified paper has 13 pages, with no overfull LaTeX boxes or text outside the page.

Original notebook SHA-256: `773954ea7ca5bc6db5f8a1d44aa0ce8e170bb88cf6d9813a6bbeb08068e878d5`.

Original public ZIP SHA-256: `197d8d9b55653c3ae76e84625e72be1fa8eb21eb578f4b96d5a209b6ebb1d9af`.

The complete package preserves the old public ZIP, its source script and reduced data, the original standalone published PDF, all 70 recovered Drive result files, the original notebook and portable source, plus the clarified paper and audit tools. The original runtime lock was not recovered; audit-time versions are recorded separately.

Repository: https://github.com/Jun-Lucis/BIG-theory

Original Zenodo version: https://doi.org/10.5281/zenodo.21144373
