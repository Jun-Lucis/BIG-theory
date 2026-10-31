# BIG-B8: Boundary Anisotropy and Finite-Time Separatrix Thresholds

**Current B8 version: v0.3 — published 31 October 2026.**
[Version-specific DOI: 10.5281/zenodo.23832946](https://doi.org/10.5281/zenodo.23832946) · [Zenodo record](https://zenodo.org/records/23832946).
The v0.3 release includes an English revised preprint, a Japanese reference translation,
and a separate reproducibility supplement. Its additions audit the legacy numerical
claims and the formal unprojected negative-quartic-flux equation; they do **not**
replace the original finite-grid observations or establish a physical instability law.

**Previous documentation-corrected dataset v0.2 — 15 October 2026.**
[Version-specific DOI: 10.5281/zenodo.23385079](https://doi.org/10.5281/zenodo.23385079);
the [original archived record, DOI 20645317](https://doi.org/10.5281/zenodo.20645317)
remains part of the publication history.
The public ZIP was re-downloaded and verified byte-for-byte against the upload.
Nine model labels are corrected to exponential, 125 missing ratio identifiers
are restored, the N96 pooled history includes all 35 existing per-ratio rows,
and two figures are redrawn from archived values. Original thresholds,
coefficients, predictions, classifications, raw case exports and the separate
true log-log exponent 0.575225 are retained. The original solver and ray-fit
source remain unauthenticated. See the [correction and verification record](../../docs/B8_documentation_correction_2026_10_15.md).


## v0.3 source audit: numerical and mathematical scope

The original B8 scheme is a *finite-dimensional, box-projected explicit Euler*
algorithm, with centered spatial differences and numerical stopping criteria.
The archived ellipse-family amplitude thresholds and their N96-to-N120
aspect-ratio ordering are historical finite-grid results, not continuum or
asymptotic separatrices. The v0.3 audit establishes the following:

- **Limited original-scheme reproducibility:** four archived terminal fields
  match a source-aligned re-execution within a maximum all-cell difference
  of 9.36e-14. The complete original ray-fitting source and every historical
  trajectory were not independently authenticated or rerun.
- **Numerical scheme sensitivity:** at the circular initial condition
  (aspect ratio 1, amplitude 0.345), the original centered scheme at N96
  survives to T=0.4, whereas a separately implemented, smooth-test-consistent
  face-flux scheme crosses the same RHS stopping threshold near t=0.296.
  With the centered scheme, N144 and N160 cross near t=0.285417 and
  t=0.266403, respectively. Reduced-timestep controls gave nearly identical
  stop times at those fixed grids. A STOP is a numerical criterion, not proof
  of a continuous-PDE singularity.
- **Conditional mathematical obstruction:** in the positive interior,
  the formal unprojected flux is
  `J(phi) = phi*grad(phi) - gamma*|grad(phi)|^2*grad(phi)`
  for the audited m=1 settings. Its principal linearization may have negative
  eigenvalues. For the stated circular reference field, the *time-frozen,
  spatially variable-coefficient* linearized operator does not generate a
  standard L2 C0 semigroup for realizations containing compactly supported
  smooth interior perturbations. This is **not** a general nonlinear
  nonexistence or finite-time blow-up theorem.
- **Regularization remains a new assumption:** adding sufficient positive
  second-order diffusion or positive fourth-order smoothing changes the
  governing model; the latter lacks a general positivity principle.
  Neither intervention establishes stable compact-support evolution
  of the original B8 equation.
- **Evidence boundary:** finite-grid geometry-dependent classifications
  are preserved; a grid-independent continuum separatrix, original
  nonlinear well-posedness, BIG-specific added predictive value, and
  independently calibrated physical prediction are **not established**.

For the source-scoped theorem statements, numerical tables and provenance,
see the [v0.3 mathematical audit note](../../docs/B8_v0_3_source_and_mathematical_audit_2026_10_31.md)
and the [Zenodo v0.3 paper and supplement](https://doi.org/10.5281/zenodo.23832946).
The historical [v0.2 documentation correction](../../docs/B8_documentation_correction_2026_10_15.md)
and all prior formal outcomes are retained. Later BIG model families must be
evaluated under their own source equations and evidence gates; B42
`SCIENCE NONE` is unchanged.

---

This folder collects materials related to **BIG-B8**, a numerical study of how boundary anisotropy affects finite-time survival/runaway thresholds in reduced boundary-field models.

BIG-B8 studies whether boundary geometry is merely an initial visual feature, or whether it can actively shift the finite-time separatrix between survival-like and runaway-like outcomes.

---

## Core question

The guiding question of B8 is:

> Can boundary shape, especially anisotropy, control the finite-time threshold between survival and runaway?

This question follows from B7.

B7 suggests that local boundary structure may remain regular even when global runaway occurs.
B8 then asks whether the **shape of the boundary itself** can shift the onset of global runaway-like behavior.

---

## Finite-time separatrix

A **finite-time separatrix** is a threshold that separates different outcomes over a specified observation time.

In B8-type scans, the system is tested under different initial amplitudes, geometries, or anisotropies.
The numerical outcome is classified over a finite simulation window as, for example:

```text
survival-like
or
runaway-like
```

The critical amplitude or threshold is therefore a finite-time quantity.

It should not automatically be interpreted as an asymptotic stability boundary.

---

## Boundary anisotropy

Boundary anisotropy refers to directional imbalance in the boundary shape.

A simple example is an ellipse-like or deformed boundary with different characteristic lengths in different directions.

In reduced notation, anisotropy may be summarized by a ratio such as:

$$
\frac{b}{a}
$$

or another geometry-dependent shape descriptor.

The archived finite-grid B8 result is an aspect-ratio-dependent shift of a *numerically defined* finite-time threshold; no mesh-independent continuum threshold is established.

---

## Main result

The main B8 observation is:

> In the archived projected finite-difference solver, boundary anisotropy shifts the finite-time survival/stop threshold over the stated observation window.

Qualitatively:

```text
more isotropic boundary
    -> higher survival/runaway threshold

more anisotropic boundary
    -> lower finite-time runaway threshold
```

This means that boundary geometry is not only descriptive.
It can act as a stability-relevant variable.

---

## Interpretation

B8 turns the BIG statement “boundary matters” into a measurable numerical claim:

```text
boundary geometry
    -> changes finite-time threshold
    -> affects survival/runaway outcome
```

This is important because it connects local boundary structure to global fate.

B7 separates local boundary regularity from global instability.
B8 records geometry-dependent numerical stop thresholds, while the v0.3 audit independently identifies a negative-principal-coefficient obstruction for the formal unprojected continuum linearization.

---

## Relation to BIG

Within BIG, B8 plays the role of the **geometry-controlled threshold branch**.

The conceptual sequence is:

```text
B3--B4: compact-support-like boundary layers and quadratic landing
B7: local free-boundary exponent near runaway
B8: boundary anisotropy shifts finite-time thresholds
B9: boundary cost versus nonlocal repulsion gives fission-like metastability
B10: finite-noise capture
B11: hidden-depth inheritance
B12: unified boundary dynamics
```

B8 therefore connects early boundary-layer studies to later energy-landscape and event-threshold models.

---

## Why this matters

If boundary anisotropy affects the survival/runaway threshold, then stability is not determined only by bulk amplitude or total energy.

Boundary shape is a parameter of the measured finite-grid stopping classification. Its role in any well-posed continuum evolution remains open.

This motivates later BIG questions:

* Can boundary cost stabilize compactness?
* Can nonlocal repulsion overcome boundary cost?
* Can a boundary-supported system separate along a fission-like branch?
* Can noise later drive capture or locking?
* Can post-capture states preserve hidden-depth inheritance?

B8 does not answer these later questions; it records a geometry-dependent finite-time numerical classification under its specified solver.

---

## Important limitations

BIG-B8 is a numerical study in a reduced model.

The reported thresholds are finite-time thresholds.
They depend on:

* the chosen equations,
* initial geometry,
* parameter values,
* discretization,
* simulation time,
* and the event criterion used to classify runaway.

B8 does not claim that:

* the reported thresholds are universal constants;
* the finite-time separatrix is an asymptotic stability boundary;
* all anisotropic physical boundaries become unstable;
* the result directly applies to materials, fluids, biology, cosmology, or nuclear systems without further domain-specific modeling.

The result should be read as model-level numerical evidence that boundary anisotropy can affect finite-time stability thresholds.

---

## Recommended wording

Preferred:

> BIG-B8 studies how boundary anisotropy shifts finite-time survival/runaway thresholds in a reduced boundary-field model.

Preferred:

> B8 provides model-level numerical evidence for a geometry-dependent finite-time separatrix.

Preferred:

> Boundary anisotropy controls the position of the finite-time separatrix within the tested model.

Avoid unless carefully qualified:

> B8 proves a universal instability law.

> B8 gives an asymptotic stability theorem.

> B8 predicts real material failure thresholds.

> All anisotropic boundaries are unstable.

---

## Zenodo record

Current revised B8 preprint and reproducibility supplement (v0.3):

https://zenodo.org/records/23832946

Previous documentation-corrected dataset (v0.2):

https://zenodo.org/records/23385079

Original archived version:

https://zenodo.org/records/20645317

Related B7/B8 notes may also be listed here as the repository is organized.

---

## Folder contents

Suggested future contents:

```text
papers/B8_finite_time_separatrix/
├── README.md
├── figures/
├── data_summaries/
├── scripts/
└── notes/
```

Large raw datasets should remain archived on Zenodo. This repository should contain lightweight summaries, representative figures, and reproducibility notes.
