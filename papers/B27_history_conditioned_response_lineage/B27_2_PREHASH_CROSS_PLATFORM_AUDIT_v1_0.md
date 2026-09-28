# BIG-B27.2 Cross-Platform Pre-Lineage Reproducibility Audit

**Date:** 2026-09-29  
**Status:** PRE-TARGET IMPLEMENTATION AUDIT  
**Post-reconfiguration response trajectories evaluated:** 0

## Observation

The frozen B27.2 v1.0 notebook was executed independently outside Colab before any post target.

The reconstructed N=160 pre-lineage matrix was numerically equivalent to the frozen P1R matrix but not bitwise identical:

- frozen SHA-256: `5e25d87279caa3b4f2a9b995375eb0db1bb68941e08d240c0a495cc7594a0eda`
- independent-environment SHA-256: `b2152d2f09d22f6656fc6581ea1d33745fe6b89dd5f1abb907651d63f74f4455`
- normalized matrix defect: (2.0217767569\times10^{-12})
- maximum absolute entry difference: (1.9464430068\times10^{-12})

The v1.0 exact-hash gate therefore stopped the run before any post-reconfiguration target was evaluated.

## Interpretation

The discrepancy is a cross-platform floating-point reproducibility effect, not a scientifically resolved difference in the pre-lineage state. The observed matrix mismatch is many orders of magnitude below the frozen numerical floor (0.003) and the covariance gate (0.010).

## Protocol consequence

B27.2 v1.1 supersedes only the bitwise pre-lineage verification rule. It retains the frozen hash for provenance and accepts cross-platform reconstruction only when either:

1. the SHA-256 matches exactly, or
2. both the normalized pre-lineage defect and the maximum absolute matrix-entry difference are (le10^{-10}).

No target, response definition, topology gate, covariance threshold, PARTIAL threshold, or verdict rule is changed.

This audit and v1.1 amendment are frozen before the first post-reconfiguration response trajectory.
