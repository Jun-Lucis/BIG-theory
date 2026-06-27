# BIG-B10: Finite-Noise Capture and Stochastic-Resonance-Like Boundary Locking

This folder collects materials related to **BIG-B10**, a reduced dynamic boundary model for finite-noise sustained capture.

BIG-B10 studies whether two boundary-supported systems can enter a sustained coupled state under noise. The central observation is that noise can be both constructive and destructive: too little noise may fail to activate the capture channel, intermediate noise can enable sustained capture, and excessive noise can destroy sustained locking.

---

## Core question

The guiding question of B10 is:

> Can boundary-supported systems achieve sustained capture only within a finite-noise window?

This question follows naturally from the BIG programme.

If B9 studies separation and fission-like branching, then B10 studies the opposite direction:

```text
separated boundary-supported systems
    -> approach
    -> internal activation
    -> sustained capture
```

---

## First hit is not sustained capture

A central distinction in B10 is:

```text
first hit != sustained capture
```

A trajectory may reach contact or near-contact once, but that does not mean it has entered a stable coupled state.

B10 therefore distinguishes:

* **first hit**: the system reaches a proximity or contact criterion;
* **sustained capture**: the system remains locked for a required duration or satisfies a hold condition;
* **escape**: the system fails to remain captured;
* **timeout**: the trajectory does not complete the required event within the observation time.

This distinction is essential because high-noise trajectories may still show frequent first hits while failing to maintain sustained capture.

---

## Reduced dynamic structure

A simplified B10-type model contains:

* a boundary distance or proximity variable,
* internal activation variables,
* a dynamic channel gate,
* stochastic forcing,
* and event definitions for first hit, sustained capture, escape, and timeout.

In B10.2-style scans, the dynamic channel may depend on internal variables such as resonance-like and gate-like modes. A representative shorthand is:

```text
dynamic_Rq gate
```

where the capture channel opens only when the relevant internal conditions are sufficiently activated.

---

## Main result

The main B10 result is a finite-noise capture window.

Qualitatively:

```text
low noise
    -> channel rarely activates
    -> sustained capture is unlikely

intermediate noise
    -> channel activates and remains coherent
    -> sustained capture becomes likely

high noise
    -> approach or first hit may still occur
    -> sustained capture is disrupted
```

This is described as **stochastic-resonance-like** behavior.

The term means that noise can help access a dynamical channel, but only within a finite range.

---

## Representative B10.2 diagnostic

In the B10.2 canonical dynamic-gate scan, the dynamic_Rq mode shows a finite-noise sustained-capture window.

A representative summary is:

```text
control mode: dynamic_Rq
peak sigma: approximately 0.40
peak sustained-capture probability: approximately 0.91--0.92
high-noise sustained capture: collapses toward zero
```

This should be read as a model-level numerical result under the specified equations, parameters, scan range, and event definitions.

The exact values are not universal constants.

---

## Interpretation

B10 suggests that boundary capture is not simply a matter of distance.

A successful capture event requires at least three ingredients:

1. **approach**
   The systems must come close enough.

2. **channel activation**
   Internal degrees of freedom must open the capture channel.

3. **sustained locking**
   The coupled state must persist long enough to count as capture.

This gives B10 its role within BIG:

```text
boundary approach
    -> internal activation
    -> sustained capture
```

---

## Important limitations

BIG-B10 is **not** a quantitative model of nuclear fusion.

It does not model:

* Coulomb-barrier penetration,
* quantum tunneling,
* nuclear potentials,
* plasma kinetics,
* reaction cross sections,
* thermodynamic fusion yield,
* or real fusion energy release.

The term “fusion-like” refers only to the structural sequence of approach, activation, capture, and sustained locking in a reduced boundary model.

B10 should therefore be read as a reduced dynamical study of boundary capture, not as a physical theory of nuclear fusion.

---

## Relation to the BIG programme

Within BIG, B10 plays the role of the **capture / fusion-like branch**.

It connects naturally to:

* **B9**, which studies fission-like separation from boundary cost and nonlocal repulsion;
* **B11**, which studies what happens after capture: assimilation or hidden-depth inheritance;
* **B12**, which integrates boundary approach, finite-noise resonance locking, and hidden-depth inheritance in a unified reduced model.

The conceptual sequence is:

```text
B9: separation / fission-like branching
B10: finite-noise capture / fusion-like locking
B11: post-capture inheritance versus assimilation
B12: unified boundary dynamics
```

---

## Recommended wording

Preferred:

> BIG-B10 studies stochastic-resonance-like finite-noise capture in a reduced boundary-dynamical model.

Preferred:

> B10 distinguishes first contact from sustained capture.

Preferred:

> B10 provides model-level numerical evidence for a finite-noise sustained-capture window.

Avoid unless carefully qualified:

> BIG-B10 explains nuclear fusion.

> BIG-B10 predicts fusion rates.

> BIG-B10 is a nuclear fusion model.

> First hit means fusion.

---

## Zenodo record

Primary BIG-B10 record:

https://doi.org/10.5281/zenodo.20819427

Additional B10.2 diagnostic and robustness records may be listed here as they are finalized.

---

## Folder contents

Suggested future contents:

```text
papers/B10_finite_noise_capture/
├── README.md
├── figures/
├── data_summaries/
├── scripts/
└── notes/
```

Large raw datasets should remain archived on Zenodo. This repository should contain lightweight summaries, representative figures, and reproducibility notes.
