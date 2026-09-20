# BIG-B19 — Boundary-Core Channel Diagnostics


> 🇯🇵 **日本語要約**  
> B19では、合成した発散ゼロ3次元渦度場について、boundary-core量、Biot--Savart strain、符号付きstrain alignment、production/dissipation balanceを同時に調べます。単一のray-independentなスカラーしきい値への崩壊は得られず、代わりに方向依存の上流boundary-core channel群が、下流のproduction-versus-dissipation / total-balance構造へ接続するという整理が得られました。これは有限の合成場に対する診断結果であり、Navier--Stokes正則性問題の証明ではありません。

## Purpose

BIG-B19 studies synthetic divergence-free three-dimensional vorticity fields using boundary-core concentration, Biot--Savart strain, signed strain alignment, finite-window dynamics, and enstrophy-balance diagnostics.

The integrated B19 study combines a reduced shrinking-core scaling model with synthetic divergence-free vorticity fields, periodic Biot--Savart strain readout, signed strain--vorticity alignment, high-vorticity gates, short-time viscous evolution, numerical robustness controls, local perturbations, and directional continuation.

Under the stated stretching-versus-leakage assumptions, the reduced scaling model identifies an energy-compatible concentration window with a critical thickness exponent $s^*=5/4$. In the dynamical experiments, local positive stretching and coherent signed gate-local openness are insufficient by themselves for positive finite-window enstrophy growth. Growth and decay are instead organized by the evolving competition between stretching production and viscous dissipation, including delayed activation.

Local-neighborhood tests show heterogeneous robustness across boundary-core channel classes. Controlled continuation around a fragile late-delayed channel resolves three directional local growth--decay boundaries. Reduction tests using 21 single observables and eight predeclared two-coordinate portraits do not yield a robust ray-independent upstream reduction. Mechanism comparison instead supports a channel-family interpretation: distinct direction-dependent upstream boundary-core pathways can feed into a common downstream finite-window production-versus-dissipation organization.

The principal integrated result is therefore not a universal boundary threshold, but a reproducible boundary-core channel-family structure within the tested numerical construction.

The B19 follow-up studies the finite-window response surface
`F_ray(T,epsilon)=Delta Z(T,epsilon;ray)` and treats the growth/decay boundary as its derived zero set.

The original `T=0.010` brackets do not persist as fixed sign-separating boundaries when the observation horizon is extended. In the sampled continuation family, `p01` and `p02` show outward-moving detected zero contours while retaining a decreasing transverse epsilon-response. The `p03` direction behaves differently: its detected zero contour moves rapidly outward and leaves the sampled epsilon-domain, after which the response changes from globally decreasing to mixed and then globally increasing. Deterministic epsilon- and time-thinning controls preserve this p03 orientation-reversal ordering in all tested variants, while p01/p02 remain non-reversing.

A predeclared cone-inspired coordinate motivated by the 2026 OpenAI forced Navier--Stokes construction does not collapse the three B19 directions. This comparison is structural only.

## Representative figure

![Boundary-core channel class retention](../../figures/B19/B19_16_class_retention_fraction.png)

*Local-neighborhood robustness diagnostic for the B19 boundary-core channel classes. Class retention is a finite synthetic-family result, not a universal Navier--Stokes classification.*

## Scope

B19 is limited to the stated reduced model and constructed synthetic divergence-free vorticity families. It does **not** establish finite-time Navier--Stokes blow-up, a singularity criterion, a regularity criterion, a global invariant separatrix, a universal invariant manifold, a universal separatrix, or reproduction/validation of the OpenAI theorem.

## Publications

Integrated record: https://zenodo.org/records/22726848

Finite-time response follow-up: https://zenodo.org/records/22769513

Author: Jun Lucis
