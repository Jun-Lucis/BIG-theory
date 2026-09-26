# BIG-B26.1: Prospective Topology-Bracket Refinement

**Author:** Jun Lucis  
**Status:** FROZEN BEFORE NEW B26.1 TRAJECTORIES  
**Date frozen:** 2026-09-26  
**Protocol ID:** `BIG_B26_1_TOPOLOGY_BRACKET_REFINEMENT_v1_0`  
**Canonical semantic configuration SHA-256:** `5377a3b614c9e9426b5a60997cdd9f4288d7c5abef2c9660908dba8629b92cf1`

## Purpose

B26 did not realize its intended topology span because all tested B26 separations were already on the two-contour side. At the same (N=384) resolution, however:

```text
archived B25.2: delta=3.2 -> 1 primary representative contour
B26:            delta=4.4 -> 2 primary representative contours
```

Therefore the representative-level topology transition is bracketed by

[
3.2<delta_*<4.4.
]

B26.1 refines only this topology bracket.

## Evidence firewall

B26.1 is a topology-only locator. It must not calculate or inspect:

- (J_{m obs});
- fixed-(sigma P) ratios or relative errors;
- coefficient fits;
- any branch-selection quantity other than representative-level primary contour count.

This preserves the subsequent fixed-(sigma) transfer test as a new held-out stage.

## Frozen algorithm

Resolution:

[
N=384.
]

Initial archived bracket:

[
[delta_L,delta_U]=[3.2,4.4].
]

Run exactly four adaptive bisection trajectories. At each midpoint:

- count = 1 -> replace the lower bound;
- count >= 2 -> replace the upper bound.

The resulting bracket must have width at most

[
(4.4-3.2)/2^4=0.075.
]

No extra point may be added after observing the four outcomes.

## Formal verdicts

```text
TOPOLOGY_BRACKET_REFINED
IMPLEMENTATION_INVALID
ARCHIVED_BRACKET_NOT_VALID
```

## Next-stage rule

Only after B26.1 closes may a non-overlapping B26.2 fixed-coefficient transfer protocol be frozen from the refined topology bracket.

**Related B25 Phase-II DOI:** https://doi.org/10.5281/zenodo.22967474
