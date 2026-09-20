# BIG-B19 — Boundary-Core Channel Diagnostics


> 🇯🇵 **日本語要約**  
> B19では、合成した発散ゼロ3次元渦度場について、boundary-core量、Biot--Savart strain、符号付きstrain alignment、production/dissipation balanceを同時に調べます。単一のray-independentなスカラーしきい値への崩壊は得られず、代わりに方向依存の上流boundary-core channel群が、下流のproduction-versus-dissipation / total-balance構造へ接続するという整理が得られました。これは有限の合成場に対する診断結果であり、Navier--Stokes正則性問題の証明ではありません。

## Purpose

BIG-B19 studies synthetic divergence-free three-dimensional vorticity fields using boundary-core concentration, Biot--Savart strain, signed strain alignment, finite-window dynamics, and enstrophy-balance diagnostics.

The integrated result does not support a single ray-independent scalar threshold. Instead, the diagnostics identify direction-dependent upstream boundary-core channel families that feed a common downstream production-versus-dissipation / total-balance organization.

Later B19 work also shows that the finite-time response zero contour depends on the observation window, so it should not be treated as a fixed universal separator.

## Representative figure

![Boundary-core channel class retention](../../figures/B19/B19_16_class_retention_fraction.png)

*Local-neighborhood robustness diagnostic for the B19 boundary-core channel classes. Class retention is a finite synthetic-family result, not a universal Navier--Stokes classification.*

## Scope

B19 is a reduced numerical diagnostic on synthetic divergence-free vorticity fields. It does **not** prove Navier--Stokes blow-up or regularity.

## Publications

Integrated record: https://zenodo.org/records/22726848

Finite-time response follow-up: https://zenodo.org/records/22769513

Author: Jun Lucis
