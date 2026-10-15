# B13 archive audit — 15 October 2026

**Current Zenodo record:** https://doi.org/10.5281/zenodo.21072783  
**Correction status:** Version 1.1 manuscript and single-archive package prepared; Zenodo publication pending.

The original public manuscript contains reconstructed illustrations rather than the archived Colab figure files. In particular, Figures 1 and 2 differ from the saved numerical basin map and baseline selection curve. This is a substantive figure-provenance correction. The underlying saved numerical values agree with the manuscript's principal reported results.

The prepared correction restores all twelve panels: eleven use original Colab PNGs and Figure 3 is redrawn directly from the unchanged 48-condition table with the tested coordinates labeled explicitly. It also repairs two gradient symbols and printed contents-page numbers, and clarifies Appendix A provenance and the four locally stable points found by the search. The original PDF and all 37 original result-package files are retained.

## Verified scope

- 86 groups / 4508 comparison values passed in the stored-data and static-source audit.
- The 1140 selection/summary/map rows, the 31×31 basin map, the high-noise 4×4 transition matrix and the principal 24-field summary are consistent.
- All 128 transition counts agree with the recovered original notebook's saved output logs.
- The recovered original notebook supplies eighteen unchanged computational function bodies. A portable output adapter is prepared.
- The corrected 17-page PDF passed all-page rendering and restored-image checks. Text outside the declared correction regions is preserved.
- No stochastic trajectory, PDE integration or fixed-point minimization was rerun; scientific outcomes are unchanged.

**Reproduction is supported in principle; independent rerun auditing is not yet complete.**  
**基本的に再現可能。独立した再実行監査は未了。**

## Interpretation clarified

The executed binary scheme uses sigma sqrt(eta) noise, nonnegative projection, a norm guard and terminal-state classification. Its gate is fixed and the observer axis is not jointly evolved. Common-seed zero-coupling repetitions are paired comparisons, not independent replications.

The main self-observation energy has four stable minima, four off-axis saddles and an unstable origin. The four reported points are the locally stable minima found by the search. The 625-row classification map is consistent with the found point set and classifier priority; an unstable label does not imply that no stable minimum exists.

The reported noise stay probability is terminal-label retention, allowing exit and return. The Born-like reference comparisons remain finite-model diagnostics, without a derivation of quantum measurement or consciousness; separately testable future extensions remain open.

## Publication bookkeeping

The current public Zenodo record already includes https://github.com/Jun-Lucis/BIG-theory as a related URL. The prepared correction has not yet been published on Zenodo and must not be cited as a published new DOI. Public re-download verification will follow publication.

[Machine-readable status](B13_archive_audit_status_2026_10_15.json).  
[Paper entry](../papers/B13_boundary_folding_observation/README.md).
