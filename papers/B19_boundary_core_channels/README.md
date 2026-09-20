# BIG-B19 — Boundary-Core Channel Diagnostics


> 🇯🇵 **日本語要約**  
> B19では、合成した発散ゼロ3次元渦度場について、boundary-core量、Biot--Savart strain、符号付きstrain alignment、production/dissipation balanceを同時に調べます。単一のray-independentなスカラーしきい値への崩壊は得られず、代わりに方向依存の上流boundary-core channel群が、下流のproduction-versus-dissipation / total-balance構造へ接続するという整理が得られました。これは有限の合成場に対する診断結果であり、Navier--Stokes正則性問題の証明ではありません。

## Purpose

BIG-B19 studies synthetic divergence-free three-dimensional vorticity fields using boundary-core concentration, Biot--Savart strain, signed strain alignment, finite-window dynamics, and enstrophy-balance diagnostics.

The integrated result does not support a single ray-independent scalar threshold. Instead, the diagnostics identify direction-dependent upstream boundary-core channel families that feed a common downstream production-versus-dissipation / total-balance organization.

The B19 follow-up studies the finite-window response surface
`F_ray(T,epsilon)=Delta Z(T,epsilon;ray)` and treats the growth/decay boundary as its derived zero set.

The original `T=0.010` brackets do not persist as fixed sign-separating boundaries when the observation horizon is extended. In the sampled continuation family, `p01` and `p02` show outward-moving detected zero contours while retaining a decreasing transverse epsilon-response. The `p03` direction behaves differently: its detected zero contour moves rapidly outward and leaves the sampled epsilon-domain, after which the response changes from globally decreasing to mixed and then globally increasing. Deterministic epsilon- and time-thinning controls preserve this p03 orientation-reversal ordering in all tested variants, while p01/p02 remain non-reversing.

A predeclared cone-inspired coordinate motivated by the 2026 OpenAI forced Navier--Stokes construction does not collapse the three B19 directions. This comparison is structural only.

## Representative figure

![Boundary-core channel class retention](../../figures/B19/B19_16_class_retention_fraction.png)

*Local-neighborhood robustness diagnostic for the B19 boundary-core channel classes. Class retention is a finite synthetic-family result, not a universal Navier--Stokes classification.*

## Scope

B19 is a reduced numerical diagnostic on finite synthetic divergence-free vorticity fields. It does **not** establish Navier--Stokes finite-time blow-up, a regularity or singularity criterion, a universal invariant manifold, a universal separatrix, or reproduction/validation of the OpenAI theorem.

## Publications

Integrated record: https://zenodo.org/records/22726848

Finite-time response follow-up: https://zenodo.org/records/22769513

Author: Jun Lucis
