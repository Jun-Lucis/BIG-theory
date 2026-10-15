# BIG-B13.1 — Rotated-Basis Observation and the Empirical BIG Selection Kernel


> 🇯🇵 **日本語要約**  
> B13.1では、B13の状態選択を回転した基底へ拡張し、入力状態と観測基底の相対角度に対する経験的な選択カーネルを調べます。これにより、単一の固定基底での選択から、基底の向きを変えた場合にも比較できる状態選択モデルへ進みました。Born-like則との比較は経験的参照であり、量子力学の測定則を導出したものではありません。

## Purpose

BIG-B13.1 extends the B13 observation-like reduced model to rotated bases and studies an empirical BIG selection kernel.

The emphasis is on basis-dependent state-selection diagnostics inside the reduced model, not on a derivation of quantum mechanics.

## Scope

The selection kernel is empirical and model-level. Similarity to Born-like angular structure is a comparison target, not a claim that the Born rule has been derived.

## Publication

Current version 1.1: https://doi.org/10.5281/zenodo.23400328  
Original v1: https://doi.org/10.5281/zenodo.21108338

Author: Jun Lucis

## CP18 audit and source recovery (16 October 2026)

**基本的に再現可能。独立した再実行監査は未了。**

Version 1.1 preserves all original numerical outcomes and the eleven paper figures. It clarifies rotation covariance, the redundant logit-bias parameter, distinct kernel calibrations, raw versus averaged RMSE, centroid-width assumptions and CSV half-bin rounding. The recovered original notebook and 30 distinct computational function names (31 unchanged definitions) are included in one complete Zenodo ZIP.

The audit passed 125 stored-data groups / 24,702 values and 75 provenance, symmetry and recovered deterministic-analysis groups / 8,852 values. No stochastic trajectories were generated. The public ZIP (19,146,726 bytes) is byte-identical to the saved release; CRC and all 155 internal SHA256 checksums pass. SHA-256: `7c7e6334db613400e77060762247d2b4be5a2a0e039439615c9f9492db28ead4`.

[Methods and audit](../../docs/B13_1_publication_audit_2026_10_16.md) · [Public verification](../../docs/B13_1_publication_verification_2026_10_16.json) · [Recovered source](../../code/B13_1_recovered/).
