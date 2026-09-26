# BIG-B26: Prospective Topology-Realized Fixed-Sigma Transfer

**Author:** Jun Lucis  
**Status:** FROZEN BEFORE NEW B26 TRAJECTORIES  
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
