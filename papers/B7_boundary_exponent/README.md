# BIG-B7: Free-Boundary Exponent Across a Runaway Transition

This folder collects materials related to **BIG-B7**, a numerical study of local free-boundary structure near a global runaway transition.

BIG-B7 studies whether the local boundary exponent changes when the global system approaches runaway-like behavior.

---

## Core question

The guiding question of B7 is:

> Does a global runaway transition destroy the local free-boundary structure, or can the local boundary profile remain regular while the global dynamics destabilize?

This question is important for BIG because boundary stability has both local and global aspects.

A boundary can remain locally well-formed even when the entire configuration becomes globally unstable.

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

The main B7 observation is that the local boundary exponent remains approximately stable across the tested transition regime.

Qualitatively:

```text
local boundary profile
    -> remains close to quadratic landing

global dynamics
    -> may approach runaway-like behavior
```

This suggests that runaway-like behavior does not necessarily begin as a local boundary-profile breakdown.

Instead, it may arise from global accumulation, global instability, or long-range dynamical effects while the immediate boundary layer remains locally regular.

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

B7 suggests that these two questions should not be automatically identified.

A system may show:

```text
local boundary regularity
AND
global runaway tendency
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

B7 supports the idea that local boundary structure can remain meaningful even when global behavior changes sharply.

---

## Why this matters

For BIG, this is important because the boundary is not just a visual edge.

If the boundary exponent remains stable near a runaway transition, then the boundary layer may carry robust local information even when the total configuration is dynamically unstable.

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

The result should be read as model-level numerical evidence for the persistence of local boundary structure across a tested runaway transition.

---

## Recommended wording

Preferred:

> BIG-B7 studies the persistence of the local free-boundary exponent near a global runaway transition.

Preferred:

> B7 suggests that local boundary regularity can coexist with global instability in a reduced boundary model.

Preferred:

> B7 separates local boundary-profile behavior from global runaway dynamics.

Avoid unless carefully qualified:

> B7 proves universal boundary exponent stability.

> B7 solves runaway dynamics.

> B7 shows all free boundaries are quadratic.

---

## Zenodo record

Primary B7 record:

```text
DOI to be listed
```

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
