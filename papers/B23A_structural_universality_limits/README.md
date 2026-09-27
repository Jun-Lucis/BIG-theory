# BIG-B23A — Structural Universality and Its Limits in Boundary Information Geometry

*Prospective Tests of Smooth Transfer, Reconfiguration Reset, Local Response, and Rate Ordering*

## 日本語要約

> **位置づけ:** B23A は、B20–B23 で局所的に有効だった応答境界幾何が、別の再構成族・自由境界系・応答指標へどこまで移せるかを、事前固定した prospective test で検査した終端監査です。
>
> **結論:** 同じ数値量・同じ reset 則・同じ rate law が広く転送できるという **quantitative universality** は確立しませんでした。一方で、固定 branch 内の局所幾何、branch / reconfiguration を明示する piecewise representation、異なる系を共通形式で比較する **formal / structural universality** は残ります。
>
> **終端判断:** P6 まででこの探索枝を閉じ、P7 による事後的な救済探索は行いません。

## Purpose

B23A asks a narrower question than a universal boundary law:

> Which parts of the BIG response-geometry construction remain stable when the system, branch structure, topology, observable, and approach protocol are changed prospectively?

The study distinguishes three levels:

1. **structural universality** — recurring organization in terms of boundary, response, branch, reconfiguration, and history;
2. **formal universality** — a common mathematical language for response zero sets, local normals / curvature, and piecewise branch geometry;
3. **quantitative universality** — transfer of the same low-dimensional numerical predictor, reset amplitude, or rate law across systems.

The B23A terminal conclusion supports only the first two as working descriptions. The third is not established.

## Prospective evidence map

| Stage | Question | Retained verdict |
| --- | --- | --- |
| P1 | Does smooth local-normal transfer survive a new B9 reconfiguration family? | NOT_SUPPORTED_AT_NEW_B9_RECONFIGURATION_FAMILY |
| P2B | Does the connected/separated branch orientation recur in a third B9 family? | SUPPORTED_AT_THIRD_RECONFIGURATION_FAMILY |
| P3 | Does a piecewise/reset representation survive a 1D free-boundary merger? | SUPPORTED_PIECEWISE_GEOMETRY_RESET_AT_FREE_BOUNDARY_PDE |
| P4 | Does a non-topological outer-boundary reset survive in 2D? | INCONCLUSIVE_NUMERICAL_SENSITIVITY |
| P5 | Is reconfiguration preferentially localized on the interaction side? | INCONCLUSIVE_NUMERICAL_SENSITIVITY |
| P6 | Is the locality contrast monotonically ordered by approach rate? | NOT_SUPPORTED_RATE_ORDERED_LOCAL_RESPONSE_RECONFIGURATION |

## What P3 does and does not establish

P3 prospectively supported a reset contrast for the frozen threshold-support geometry vector. However, a post-hoc outer-boundary-only diagnostic gave a reset contrast consistent with zero. The retained interpretation is deliberately narrower:

**Supported:** piecewise / reset representation for the frozen topology-sensitive support geometry.

**Not established:** a universal non-topological outer-boundary reset law.

This distinction motivated P4 rather than being used to upgrade P3.

## P4–P6 terminal narrowing

P4 removed the directly topology-sensitive target but became resolution-sensitive, especially in its pointwise outer-gradient coordinate. P5 replaced that target with a finite-window local response susceptibility and again found no stable claim-bearing locality reset across resolution. P6 then prospectively tested the post-hoc P5 rate-ordering suggestion on nine new midpoint speeds at both N=256 and N=320.

For the P6 primary quantity

$$
L_{\mathrm{reset}}(v)=D_{\mathrm{inner}}(v)-D_{\mathrm{outer}}(v),
$$

the N=256 exact one-sided Spearman statistic was rho=0.2667, p=0.2467; the Theil–Sen 95% slope interval crossed zero. N=320 showed a stronger rank trend (rho=0.65, p=0.0333) but its Theil–Sen lower bound also remained below zero. All numerical integrity gates passed, so the frozen terminal verdict is a clean NOT_SUPPORTED, not a numerical inconclusive.

## Integrated interpretation

The combined B20–B23A record is most consistent with:

**fixed-branch local geometry can be useful + branch / reconfiguration identity must be represented explicitly + the concrete coefficients, normals, reset amplitudes, and rate laws can remain system- or regime-dependent.**

The strongest retained formulation is therefore:

> **a universal formalism for system-dependent boundary geometry**

This is not a statement that all systems possess the same boundary law.

## Claim boundary

B23A does **not** establish:

- a universal reset law;
- a universal response-normal field;
- a universal critical approach rate;
- cross-system quantitative universality;
- continuum convergence or a geometric theorem;
- a physical-space interface law for the synthetic vorticity response boundaries;
- a Navier–Stokes blow-up / regularity result;
- quantitative nuclear, biological, cognitive, AI, or cosmological predictions.

Negative and inconclusive prospective outcomes are retained as part of the result and are not reclassified.

## Relation to B24–B26

B23A is a **universality-audit branch** rooted in B20–B23 response geometry and B9/free-boundary reconfiguration tests. B24–B26 are a separate transfer programme concerning boundary-functionals and fixed-coefficient perimeter closure. Their positive, invalid, and negative verdicts remain unchanged.

Together, the two branches point in the same cautious direction: useful local or family-restricted reductions can exist without implying programme-wide quantitative universality.

## Publication

**Reserved Zenodo DOI:** https://doi.org/10.5281/zenodo.22994445

The English preprint is the authoritative version. A Japanese reference translation and reproducibility archive are included in the Zenodo publication package.

**Author:** Jun Lucis
