# BIG-B9: Fission-like Metastability from Boundary Cost and Nonlocal Repulsion

This folder collects materials related to **BIG-B9**, a reduced boundary-energy model for fission-like metastability.

BIG-B9 studies how a simple competition between boundary cost and nonlocal repulsion can generate a metastable energy landscape with a compact branch, a finite pinch/scission barrier, and a separated branch.

---

## Core model

The minimal B9 energy is

$$
E(\Omega;\lambda)=\sigma P(\Omega)+\lambda C(\Omega),
$$

where:

* (P(\Omega)) is a perimeter-like boundary cost,
* (C(\Omega)) is a Coulomb-like nonlocal repulsion term,
* (\sigma) controls boundary cost,
* (\lambda) controls nonlocal repulsion strength.

The central idea is that boundary cost favors compactness, while nonlocal repulsion favors separation.

---

## Main structural result

The reduced B9 model produces a fission-like metastable landscape:

```text id="5lyru7"
compact state
    -> deformation / pinch barrier
    -> separated two-fragment branch
```

This resembles the classical macroscopic intuition in nuclear fission, where surface energy and Coulomb repulsion compete.

However, the correspondence is structural and qualitative, not quantitative.

---

## Structural comparison with empirical fission indicators

A follow-up empirical structural-comparison note compares B9 with macroscopic fission-related indicators.

Representative actinides include:

```text id="7o2hxr"
Th-232
U-236
U-238
Pu-240
Cm-244
Cf-252
```

The comparison uses coarse fissility-related indicators such as (Z^2/A) and a proxy quantity,

$$
x_{\mathrm{proxy}}=\frac{Z^2}{50A}.
$$

This proxy is used only for qualitative structural comparison. It is not intended as a calibrated liquid-drop fissility parameter.

---

## Interpretation

The B9 correspondence may be summarized as:

| Liquid-drop fission intuition | BIG-B9 reduced model                   |
| ----------------------------- | -------------------------------------- |
| surface energy                | boundary cost (\sigma P(\Omega))       |
| Coulomb repulsion             | nonlocal repulsion (\lambda C(\Omega)) |
| fissility                     | ratio-like control (\lambda/\sigma)    |
| fission barrier               | finite pinch barrier                   |
| separated fragments           | two-disk / separated branch            |

No quantitative mapping between (\lambda) and MeV is assumed.

---

## Important limitations

BIG-B9 is **not** a quantitative model of nuclear fission.

The current minimal B9 model does not explicitly resolve:

* shell corrections,
* pairing effects,
* quantum tunneling,
* excitation-energy dependence,
* fragment yields,
* cross-section normalization,
* or calibration to nuclear observables.

This limitation should not be interpreted as saying that such effects are fundamentally incompatible with BIG.

Possible future extensions may represent microscopic nuclear effects through:

* effective boundary corrections,
* state-dependent coefficients,
* hidden-depth mode contributions,
* barrier-crossing dynamics,
* or higher-level structures built on the B9 energy landscape.

Thus, B9 should be read as a macroscopic structural comparison and reduced mathematical model, not as a quantitative nuclear calculation.

---

## Relation to the BIG programme

Within BIG, B9 plays the role of the **separation / fission-like branch**.

It follows naturally from the boundary-centered question:

> What happens when maintaining a boundary is costly, but nonlocal repulsion favors separation?

This later connects to:

* **B10**, which studies finite-noise capture;
* **B11**, which studies post-capture hidden-depth inheritance;
* **B12**, which integrates approach, R-lock, and inheritance in one reduced model.

---

## Recommended wording

Preferred:

> BIG-B9 studies fission-like structural metastability from boundary cost and nonlocal repulsion.

Preferred:

> B9 provides a macroscopic structural comparison with empirical fission indicators.

Avoid unless carefully qualified:

> BIG-B9 explains nuclear fission.

> BIG-B9 predicts fission barriers.

> BIG-B9 is a nuclear fission model.

---

## Zenodo record

Primary BIG-B9 record:

https://doi.org/10.5281/zenodo.20799131

Additional B9-related records and empirical comparison notes may be listed here as they are finalized.

---

## Folder contents

Suggested future contents:

```text id="e0e045"
papers/B9_fission_like_metastability/
├── README.md
├── figures/
├── data_summaries/
├── scripts/
└── notes/
```

Large raw datasets should remain archived on Zenodo. This repository should contain lightweight summaries, representative figures, and reproducibility notes.
