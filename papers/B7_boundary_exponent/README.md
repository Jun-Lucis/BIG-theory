# BIG-B7: Free-Boundary Exponent Across a Runaway Transition

**Current publication — revised preprint v1.1 (31 October 2026):**
[10.5281/zenodo.23835715](https://doi.org/10.5281/zenodo.23835715)
([Zenodo record](https://zenodo.org/records/23835715), CC BY 4.0).
The release includes the revised English paper, Japanese reference translation,
and reproducibility supplement.

**Original historical release:**
[10.5281/zenodo.20603601](https://doi.org/10.5281/zenodo.20603601).
Its original nine finite-grid numerical outcomes, classifications, fitted
values and provenance remain archived and are **not** replaced by a claim
of continuum or physical instability.

**Detailed audit:** [B7 v1.1 source recovery, spatial-scheme sensitivity,
and conditional linearized operator result](../../docs/B7_v1_1_source_numerical_and_linearization_audit_2026_10_31.md).

BIG-B7 studies whether a **finite-window, positive-level-contour fitted**
boundary exponent changes across the **tested finite-grid numerical STOP
classification**. The original global-runaway interpretation is a
hypothesis rather than an established nonlinear continuum mechanism.

---

## Core question

The guiding question of B7 is:

> Does a global runaway transition destroy the local free-boundary structure, or can the local boundary profile remain regular while the global dynamics destabilize?

This question is important for BIG because boundary stability has both local and global aspects.

In the archived finite-grid solver, a fitted local boundary profile can
remain regular-looking while the numerical stopping classification changes.
This does not establish that an actual continuum configuration becomes globally unstable.

---

## Local boundary profile

A recurring BIG boundary motif is the local power-law form

$$
\phi(s) \sim A s^\nu,
$$

where:

* (s) is the distance from the boundary,
* (A) is a fitted amplitude,
* (\nu) is the boundary exponent.

In earlier compact-boundary studies, (\nu) often appears close to 2.

B7 asks whether this exponent changes near a runaway transition.

---

## Main result

The retained B7 observation is that the selected finite-grid fitted
local exponent remains approximately stable across the **numerical**
survival/STOP bracket near `gamma=0.8735 ± 0.0005`
(`N=160`, `dt=1e-6`, `T=0.3`). The selected mean fitted exponent
is approximately `nu=1.9085`. Both are finite-grid descriptors,
not universal critical parameters or asymptotic support-edge exponents.

Qualitatively:

```text
fitted positive-contour profile
    -> effective exponent stays near 1.91

numerical evolution (specified grid, stencil and STOP rule)
    -> some tested gamma values reach STOP before T=0.3
```

This observation shows that an apparently regular finite-window fitted
profile does not, by itself, prevent a **numerical** stopping event.
The underlying cause of the STOP cannot be identified as a global
physical or continuum instability on this basis alone.

The v1.1 audit identified **grid and spatial-stencil sensitivity**.
For the same elliptical input and `gamma=0.874`, the centered
scheme at N96 and N128 survives to `T=0.3`, whereas the original
N160 run stops near `t=0.299952`; a face-flux scheme on N96
instead stops near `t=0.254392`. A numerical STOP is not a
PDE blow-up.

---

## Interpretation

B7 separates two questions:

### Local question

```text
What is the boundary shape near the free boundary?
```

### Global question

```text
Does the entire configuration remain bounded, stable, or controlled over time?
```

B7 motivates keeping these two questions distinct, but the
continuum equation's behavior is **not established** by the archived
finite-grid solver.

A finite-grid computation may show:

```text
stable-looking fitted local contour
AND
numerical RHS-based STOP
```

This distinction becomes important for later BIG series.

---

## Relation to BIG

Within BIG, B7 plays the role of a bridge between early boundary-layer studies and later threshold studies.

The conceptual sequence is:

```text
B3--B4: compact-support-like boundary layers and quadratic landing
B7: local boundary exponent near runaway
B8: boundary anisotropy and finite-time separatrix thresholds
B9: fission-like metastability
B10: finite-noise capture
B11: hidden-depth inheritance
B12: unified boundary dynamics
```

B7 motivates a distinction between the observed finite-grid local fitted
profile and the globally defined *numerical* stopping condition.
Its formal negative-quartic-gradient continuum equation also has a
separate source-scoped linearized mathematical obstruction; see the audit.

---

## Why this matters

For BIG, this is important because the boundary is not just a visual edge.

The fitted exponent is comparatively stable in the archived
finite-grid protocol despite changes in the solver's STOP label.
This supports a **model-internal descriptive observation**, not
a universal statement about physically stable boundary layers.

This helps motivate later questions:

* Can boundary geometry shift finite-time thresholds?
* Can anisotropy control the onset of runaway?
* Can boundary cost stabilize or destabilize separation?
* Can boundary-mediated systems transition between separation, capture, and inheritance?

B7 does not answer all of these questions, but it helps define the local-versus-global distinction needed for them.

---

## Important limitations

BIG-B7 is a numerical boundary study in a reduced model.

It does not claim that:

* all physical free boundaries have exponent (\nu \approx 2);
* all runaway transitions preserve local boundary regularity;
* the measured exponent is universal;
* the model provides an asymptotic theorem;
* the result directly applies to physical, biological, or cosmological systems without further modeling.

The result should be read as **finite-grid numerical evidence** for
an approximately stable finite-window fitted exponent across a
numerical STOP bracket, not as evidence of a universal nonlinear
continuum runaway transition.

**Additional v1.1 limitations:** the originally executed centered
finite-difference solver uses clipping and numerical RHS/peak thresholds.
Nine archived fields pass independent arithmetic checks; only three
complete trajectories have been independently replayed at the original
grid. The formal *unprojected* equation has a negative principal
coefficient on part of the specified initial field, giving a
**conditional `L²` `C₀` semigroup-generation obstruction**
for a fixed-profile, variable-coefficient linearization under
explicit domain assumptions. This is **not** a nonlinear blow-up
or nonexistence theorem. Nonlinear continuum well-posedness, a
mesh-independent critical coefficient, and external physical
validation remain unresolved.

---

## Recommended wording

Preferred:

> BIG-B7 reports a finite-window fitted local contour exponent near
> a finite-grid, finite-time numerical STOP transition.

Preferred:

> A stable-looking fitted local contour can coexist with the
> numerical STOP classification in the specified solver; the
> continuum instability mechanism remains unresolved.

Preferred:

> B7 distinguishes local finite-window fitting from global numerical
> stopping, while keeping the underlying nonlinear continuum
> dynamics an open question.

Avoid unless carefully qualified:

> B7 proves universal boundary exponent stability.

> B7 solves runaway dynamics.

> B7 shows all free boundaries are quadratic.

---

## Zenodo record

**Current revised B7 preprint v1.1:**
[10.5281/zenodo.23835715](https://doi.org/10.5281/zenodo.23835715)
(English PDF, Japanese reference PDF, reproducibility ZIP).

**Original B7 archived report:**
[10.5281/zenodo.20603601](https://doi.org/10.5281/zenodo.20603601)
(retained as part of the record's version history).

Related B7/B8 summary notes may also be listed here as the repository is organized.

---

## Folder contents

Suggested future contents:

```text
papers/B7_boundary_exponent/
├── README.md
├── figures/
├── data_summaries/
├── scripts/
└── notes/
```

Large raw datasets should remain archived on Zenodo. This repository should contain lightweight summaries, representative figures, and reproducibility notes.
