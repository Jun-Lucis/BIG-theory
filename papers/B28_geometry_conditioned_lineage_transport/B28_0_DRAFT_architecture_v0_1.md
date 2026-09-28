# BIG-B28 — Geometry-Conditioned Response-Lineage Transport

**Status:** DRAFT / NOT FROZEN / NO CLAIM-BEARING COMPUTATION  
**Date:** 2026-09-29

## Motivation

B27 produced a clean two-part result:

- B27.1: retained readable history changed local response geometry at identical present phi;
- B27.2: the normalized history-induced response form did **not** remain invariant across the tested connected-to-disconnected topology reconfiguration under the frozen identity map.

Therefore a new B-series may ask a different question:

> If response lineage is not invariant, can its **transformation** across reconfiguration be predicted from geometry and reconfiguration structure without fitting the held-out post response?

This is a new hypothesis, not a rescue of B27.2.

## Provisional object

Retain the B27 history-induced response deformation

[
H_G = G_{m kept}-G_{m erased}.
]

Instead of testing

[
L_G^+approx L_G^-,
]

B28 would test a prospectively defined transport law

[
oxed{
L_G^+ approx mathcal T_Gamma[L_G^-]
}
]

where (Gamma) is a geometry/reconfiguration descriptor frozen independently of the held-out response.

The central restriction is:

[
mathcal T_Gamma
quad	ext{must not be fitted on the target }L_G^+.
]

## Why B28 is distinct from B27

B27 asked whether one normalized response-lineage form survives reconfiguration unchanged under a fixed geometry-only map.

B28 would instead ask whether reconfiguration itself supplies a measurable **transition rule**.

Thus the conceptual distinction is

[
	ext{invariance}
quad
eqquad
	ext{predictable transformation}.
]

## Candidate architecture A — component-resolved split transport

A topology split changes one connected body into two components. A single global five-mode probe basis may therefore be too coarse to represent the post-split response structure.

A new component-resolved representation could use

[
mathcal P^- simeq mathbb R^5
]

before the split and

[
mathcal P^+ simeq mathbb R^5oplusmathbb R^5
]

after the split.

A geometry-only split operator

[
S_Gamma:mathbb R^5ightarrowmathbb R^{10}
]

would be built from component centers, orientations, scales, and frozen weighting rules, not from response values.

The primary question would then be whether component-resolved history-induced response geometry is prospectively predicted by this split map.

## Candidate architecture B — local transport along the reconfiguration path

Instead of jumping directly from pre to post states, define a geometry parameter (s) along a frozen reconfiguration path and study

[
L_G(s).
]

On a connected branch, estimate a local transport generator

[
rac{dL_G}{ds}
=
mathcal A_Gamma(s)L_G
+
R(s),
]

using a training family only.

The resulting transport is then integrated prospectively toward a held-out branch or topology transition.

This would test whether the failure of B27.2 reflects a missing path-dependent connection rather than absence of any relation.

## Candidate architecture C — branch-transition chart

A topology transition may require different local response charts on the two sides:

[
L_G^- in mathcal C_-,
qquad
L_G^+ in mathcal C_+.
]

A finite transition rule

[
Psi_{Gamma}:mathcal C_-	omathcal C_+
]

could be trained on one reconfiguration family and frozen before testing a distinct held-out family.

This would align with the broader BIG result that local/branch structure can remain useful even when one global law fails.

## Required safeguards before freezing B28

Any B28 claim-bearing design should include:

- a fresh P0 firewall;
- training and held-out reconfiguration families separated before target evaluation;
- no reuse of B27 T1-T3 as held-out confirmation;
- no response-derived transform on a target;
- geometry-only or training-only construction of (mathcal T_Gamma);
- two-resolution and two-probe-scale validity gates;
- an explicit null-history/readability control;
- a terminal stop rule after held-out evaluation.

B27 data may motivate the architecture and provide scale intuition, but B27 failed targets must not be relabeled as B28 evidence.

## Current preference

The most natural next direction is **component-resolved split transport**, because topology change genuinely changes the component structure of the boundary. It addresses a structural limitation of using one global body-centered five-mode representation across a 1-to-2 split.

However, this file is deliberately **not frozen**. No B28 numerical experiment should be run until the representation, transport map, training family, held-out family, and verdict logic are separately reviewed and frozen.

## Claim boundary

B28, if pursued, would remain a finite reduced-model study of predictable response-structure transformation.

It would not establish personal identity, consciousness, subjective continuity, AI personhood, biological inheritance, or a universal law of individuality.
