# BIG-B26: Prospective Topology-Realized Fixed-Sigma Transfer

**Author:** Jun Lucis  
**Status:** CLOSED — terminal B26.2 test completed  
**Date frozen:** 2026-09-26  
**Protocol ID:** `BIG_B26_TWO_CENTER_TOPOLOGY_REALIZED_FIXED_SIGMA_TRANSFER_v1_0`  
**Canonical semantic configuration SHA-256:** `e40b26c7dae79a31da8f02071d1d29ff39a5fa197d623d17ce29b8953ebb34e2`

## Purpose

B25.2 attempted to transfer the fixed B25.1e perimeter coefficient to a two-center family, but the frozen experiment did not validly realize its required topology span. B26 repairs only the prospective test geometry; it does not change the B25.1e coefficient or retroactively alter the B25.2 verdict.

The B26 question is:

> Does the fixed B25.1e perimeter coefficient transfer to a two-center geometry family that actually spans connected and disconnected representative contours within the same low-level claim band?

## Retrospective basis

B26R uses only archived B25.2 profiles. At fine resolution, the central saddle relative level decreased with dimensionless center separation (delta=d/R). A descriptive retrospective fit estimated that the saddle crosses:

- the claim-band upper edge near (deltaapprox4.293);
- the representative level near (deltaapprox5.283);
- the claim-band lower edge near (deltaapprox6.115).

These retrospective values motivate the frozen B26 range but do not count as B26 evidence.

## Frozen cases

[
deltain{4.4,5.4,6.2},qquad Nin{384,448}.
]

Total: six new trajectories.

## Fixed coefficient and predictor

The B25.1e coefficient is immutable:

[
sigma_{m cal}=9.434181431178162	imes10^{-8}.
]

The primary held-out predictor is

[
J_{m pred}=sigma_{m cal}P_{m total,rep}.
]

Only target representative perimeter may enter the primary predictor. Target peak amplitude, full (P(r)), target outcome, and coefficient refitting are forbidden.

## Fine-resolution topology gate

At (N=448):

- (delta=4.4) must have exactly one primary representative contour;
- (delta=6.2) must have at least two;
- (delta=5.4) is recorded but not individually gated.

If all numerical cases are valid but the topology gate is not realized, the formal result is `TOPOLOGY_SPAN_NOT_REALIZED`.

## Validity and verdicts

Every case must satisfy the frozen numerical validity gates, including predicted claim-band thickness of at least three grid cells.

Possible formal verdicts:

```text
IMPLEMENTATION_INVALID
TOPOLOGY_SPAN_NOT_REALIZED
AB_TWO_CENTER_FIXED_COEFFICIENT_TRANSFER_PASS
AB_TWO_CENTER_FIXED_COEFFICIENT_TRANSFER_PARTIAL
AB_TWO_CENTER_FIXED_COEFFICIENT_TRANSFER_FAIL
```

No B26 outcome may modify (sigma_{m cal}), the held-out cases, or the frozen gates.

## Claim boundary

A PASS or FAIL applies only to this frozen canonical two-center family and finite resolutions. B26 does not establish a universal source/topology theorem, continuum convergence, the B9 nonlocal term, the complete B9 energy, or external physical validity.

**Related B25 Phase-II DOI:** https://doi.org/10.5281/zenodo.22967474


---

## Result

B26 completed all six frozen trajectories and all six passed the numerical validity gates.

At the fine resolution (N=448), however, all three tested separations had two primary representative contours:

```text
delta=4.4 -> 2
delta=5.4 -> 2
delta=6.2 -> 2
```

The predeclared topology gate therefore was not realized.

**Formal verdict:** `TOPOLOGY_SPAN_NOT_REALIZED`.

The descriptive fixed-coefficient errors are retained but are not promoted to a formal transfer PASS/PARTIAL/FAIL because the topology-span prerequisite failed.

At the common (N=384) resolution, archived B25.2 gives one primary representative contour at (delta=3.2), while B26 gives two at (delta=4.4). This establishes the finite-resolution bracket

[
3.2<delta_*<4.4
]

for the representative-level topology transition and motivates a separate topology-only B26.1 refinement stage.


---

## B26.1 result — topology-only bracket refinement

B26.1 was frozen as a topology-only locator after B26 ended with `TOPOLOGY_SPAN_NOT_REALIZED`.

At N=384, four new adaptive bisection trajectories were run without calculating fixed-sigma action error:

```text
delta = 3.8000 -> 1 primary representative contour
delta = 4.1000 -> 1
delta = 4.2500 -> 2
delta = 4.1750 -> 1
```

All four trajectories passed the frozen numerical validity gates.

**Formal verdict:** `TOPOLOGY_BRACKET_REFINED`

The resulting finite-resolution bracket is

[
4.175 < delta_* < 4.250,
]

with final width 0.075.

No fixed-sigma action-error quantity was used to select the bisection branch.

## B26.2 — frozen terminal B26 transfer test

B26.2 is frozen before any new B26.2 trajectories.

New held-out separations:

[
deltain{3.95, 4.2125, 4.35},
]

with resolutions

[
Nin{384, 448}.
]

All three delta values are new: none was simulated in B25.2, B26, or B26.1.

The immutable coefficient remains

[
sigma_{m cal}=9.434181431178162	imes10^{-8}.
]

The primary predictor remains

[
J_{m pred}=sigma_{m cal}P_{m total,rep,target}.
]

At N=448 the frozen topology gate requires delta=3.95 to have one primary representative contour and delta=4.35 to have at least two.

Possible formal outcomes are:

```text
IMPLEMENTATION_INVALID
TOPOLOGY_SPAN_NOT_REALIZED
AB_TOPOLOGY_STRADDLING_FIXED_COEFFICIENT_TRANSFER_PASS
AB_TOPOLOGY_STRADDLING_FIXED_COEFFICIENT_TRANSFER_PARTIAL
AB_TOPOLOGY_STRADDLING_FIXED_COEFFICIENT_TRANSFER_FAIL
```

B26 closes after B26.2 regardless of outcome, provided the protocol is executable. No further delta tuning is permitted within B26.

**B26.2 canonical semantic SHA-256:**  
`21617eac41537c9d5baa0aa9c149c35d8fb6929a7b657ae26bd5e1f0bb510c9c`


---

## B26.2 terminal result

B26.2 completed all six frozen held-out trajectories. All six passed the numerical validity gates, and the frozen fine-resolution topology gate was realized:

    N=448
    delta=3.95   -> 1 primary representative contour
    delta=4.2125 -> 1
    delta=4.35   -> 2

The immutable B25.1e coefficient therefore received a valid topology-straddling transfer test.

The primary fixed-coefficient errors were:

    median relative error = 42.91%
    maximum relative error = 44.79%

The frozen resolution-pair |Delta q| values were 0.0271, 0.0212, and 0.0142; all remained within the predeclared stability gate.

**Formal verdict:** AB_TOPOLOGY_STRADDLING_FIXED_COEFFICIENT_TRANSFER_FAIL.

The result resolves a finite-resolution geometry-transfer boundary of the fixed-coefficient perimeter closure. It does not establish that topology change itself is the unique cause of failure, because substantial error is already present on the connected side.

The terminal B26 stop rule is triggered. No further delta tuning is permitted within B26.

**B26 Zenodo DOI:** https://doi.org/10.5281/zenodo.22972985

**Authoritative publication title:**  
*Resolving the Geometry-Transfer Boundary of a Fixed-Coefficient Perimeter Closure: Topology Localization and Prospective Two-Center Tests in Boundary Information Geometry*
