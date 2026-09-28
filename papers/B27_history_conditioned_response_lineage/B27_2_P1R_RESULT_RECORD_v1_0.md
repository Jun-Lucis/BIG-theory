# BIG-B27.2-P1R Result Record — Continuation-Prepared Connected Anchor

**Protocol:** BIG_B27_2_P1R_CONTINUATION_ANCHOR_v1_0  
**Status:** COMPLETED / VALID  
**Date:** 2026-09-29  
**Formal stage verdict:** `P1R_VALID_GATE_FROZEN`

## Topology gate

The continuation-prepared anchor satisfied the required connected topology at both claim resolutions:

| N | single baseline | before write | response anchor |
|---:|---:|---:|---:|
| 128 | 1 | 1 | 1 |
| 160 | 1 | 1 | 1 |

## Numerical stability

- cross-resolution lineage-form defect: 0.0017007830805675739
- cross-resolution G-kept defect: 0.002937767817392722
- cross-resolution G-erased defect: 0.0022224647719474833
- probe-scale lineage defects: about 1.17e-4 at both resolutions
- zero-feedback G defect: 0 at both resolutions

The training-anchor numerical floor is therefore

[
\epsilon_{\rm pre}=0.003.
]

The frozen B27.2 covariance gate is

[
\boxed{\epsilon_{\rm cov}=0.010}.
]

This is fixed before any B27.2 post-reconfiguration response has been evaluated.

## Frozen pre-lineage hash

Fine-resolution pre-lineage matrix (L_G^-), float64 C-order SHA-256:

`5e25d87279caa3b4f2a9b995375eb0db1bb68941e08d240c0a495cc7594a0eda`

The post-target notebook must reproduce this hash before evaluating any target.

## Evidence status

P1R is training/calibration-side evidence only. It freezes the pre-lineage object and numerical covariance tolerance. It is not itself a post-reconfiguration covariance result.
