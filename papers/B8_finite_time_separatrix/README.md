# BIG-B8: Boundary Anisotropy and Finite-Time Separatrix Thresholds

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

The B8 result is that such anisotropy can shift the finite-time threshold.

---

## Main result

The main B8 observation is:

> Boundary anisotropy can control the position of the finite-time separatrix.

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
B8 shows that geometry can influence when global instability appears.

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

Boundary shape itself becomes part of the stability structure.

This motivates later BIG questions:

* Can boundary cost stabilize compactness?
* Can nonlocal repulsion overcome boundary cost?
* Can a boundary-supported system separate along a fission-like branch?
* Can noise later drive capture or locking?
* Can post-capture states preserve hidden-depth inheritance?

B8 does not answer all of these questions, but it establishes that boundary geometry can shift finite-time dynamical outcomes.

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

Primary B8 record:

```text
https://zenodo.org/records/20645317
```

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
