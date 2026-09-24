# BIG-B23 — Cross-Branch Short-Horizon Geometric Prediction of Operator-Generated Response Boundaries

*Numerical Tests of Position, Normal, and Local Curvature*

## 日本語要約

> **問い:** B22で得た短時間の局所幾何予測は、同じFamily-C構成内の別の事前指定分枝へ移しても機能するか。
>
> **方法:** B20.5--B22と同じ正規化4次元部分空間を用い、3つのray方向に分布する4分枝で位置・法線の短時間予測を検査しました。さらに `r11_high` と `r12_low` をfull-geometry sentinelとして、次時刻のHessian、主曲率、主方向を検査しました。
>
> **結果:** 主評価の `hess_h2` では、評価可能な4記録のroot-midpoint誤差は **0.00033604--0.00135840**、法線角誤差は **0.02484--0.56706度**でした。後段の `r11_high` と `r12_low` ではHessian相対誤差が **0.62884%** と **0.36319%**、評価可能な主曲率の最大相対誤差が **0.98327%** と **2.42220%** でした。
>
> **重要な区別:** 当初のaggregate planは **INCONCLUSIVE** のままです。端付近の2対象では、予測中心の対称探索窓を許容domain内に置けなかったためです。修正版の `r12_low` と訂正再計算の `r09_high` は補足証拠として報告し、当初計画の成功へ遡及加算していません。
>
> **限界:** 有限の合成Family-C、有限差分、短い観測時間幅での結果です。普遍的境界運動則、連続体収束、full parameter spaceでの不変性、物理空間の界面法則、不変多様体、Navier--Stokesの爆発・正則性は主張しません。

## Purpose

B23 asks whether the B22 short-horizon local geometric construction transfers to other predeclared zero-set branches in the same exact normalized four-dimensional Family-C subspace.

The finite-window response remains

```math
F(T,P)=Z[U_T(P)]-Z[P], \qquad \mathcal B_T=\{P:F(T,P)=0\}.
```

The study separates two questions:

1. whether local position and normal predictions transfer across several branches; and
2. whether the later Hessian, principal-curvature, and principal-direction prediction also transfers to designated sentinel branches.

## Predeclared branch map

| Stage | Branch | T0 | T1 | Role |
| --- | --- | ---: | ---: | --- |
| E1 | `r11_high` | 0.0060 | 0.0065 | first-stage + sentinel |
| E2 | `r12_low` | 0.0100 | 0.0105 | first-stage + sentinel |
| E3 | `r09_high` | 0.0060 | 0.0065 | first-stage |
| E4 | `r11_low` | 0.0060 | 0.0065 | first-stage |

The two `r11` branches lie on the same ray and are not counted as two independent directions.

## First-stage results

At the primary `hess_h2` finite-difference scale:

| Record | Predicted position | Observed midpoint | Position error | Normal-angle error |
| --- | ---: | ---: | ---: | ---: |
| E1 | 1.81648548 | 1.81550892 | 0.00097656 | 0.07411° |
| E2R | 0.07485928 | 0.07519531 | 0.00033604 | 0.02484° |
| E3R2 | 1.92616308 | 1.92480469 | 0.00135840 | 0.56706° |
| E4 | 0.14980884 | 0.14883228 | 0.00097656 | 0.09421° |

E1 and E4 were executable under the original protocol. E2R is a boundary-safe supplementary validation frozen before the exact T1 PDE trajectories. E3R2 is a corrective replication after the earlier E3R implementation was found to dispatch the wrong ray.

## Later full-geometry sentinels

The later sequential tests use the observed intermediate state and freeze the next prediction before the corresponding new T2 trajectories.

| Metric | E5 `r11_high` | E6R `r12_low` |
| --- | ---: | ---: |
| next T | 0.0070 | 0.0110 |
| position error | 0.00097656 | 0.00195313 |
| normal-angle error | 0.06555° | 0.21349° |
| Hessian relative error | 0.62884% | 0.36319% |
| max assessable principal-curvature relative error | 0.98327% | 2.42220% |
| max principal-direction angle error | 0.10992° | 0.26110° |

All prescribed local geometric gates passed at both tested finite-difference scales.

## Protocol status

The original aggregate success condition is **not** promoted to PASS.

The original prediction-centered symmetric search window could not be placed fully inside the admissible family domain for E2 and E3. Those stages stopped before future outcome comparison. The later E2R/E3R2/E6R records therefore remain supplementary or corrective evidence rather than retroactive original-plan successes.

The original aggregate classification is retained as **INCONCLUSIVE**.

## Implementation correction

The first E3R repair run was invalidated after the scan-point inputs were checked and found to match the `r12` generator rather than the intended `r09` generator. The historical record is preserved as an implementation-invalid result, and E3R2 is reported as a corrective replication rather than as a new blinded prospective test.

## Claim boundary

B23 supports a limited numerical statement: short-horizon local geometric prediction transferred across the tested finite branches, including two later full-geometry sentinels.

It does **not** establish:

- a universal response-boundary motion law;
- continuum differentiability, Hessian existence, or curvature convergence;
- invariance in the full parameter space;
- a physical-space boundary normal or interface law;
- an invariant manifold or universal separatrix;
- Navier--Stokes blow-up, regularity, or singularity formation.

## Publication

**Reserved Zenodo DOI:** https://doi.org/10.5281/zenodo.22936794

The English preprint is the authoritative version. The Zenodo release also includes a Japanese reference translation and a compact reproducibility package.

**Author:** Jun Lucis
