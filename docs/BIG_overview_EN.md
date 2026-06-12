# Boundary Information Geometry (BIG): Overview

**Boundary Information Geometry (BIG)** is an exploratory research program that studies boundaries as information-carrying structures.

The guiding idea is that stable structures are not determined only by their interiors.
They are also organized by the boundaries that separate, preserve, and mediate information.

In ordinary descriptions, one often focuses on the bulk: the interior of a material, the content of a biological system, the internal state of a model, or the members of a social system.

BIG shifts part of the focus toward the boundary.

> A boundary is not merely an edge.
> It is the place where distinction, stability, interaction, and transformation are organized.

---

## 1. Core idea

The central intuition of BIG is:

> Individuality is not pure isolation.
> Individuality is a structure that preserves a boundary while remaining capable of interaction across that boundary.

If everything fully mixes, individuality disappears.
If everything is completely isolated, interaction disappears.

Thus, BIG focuses on the intermediate structure:

> A system remains itself by preserving a boundary, but it remains alive or active by interacting across that boundary.

This is the conceptual basis of BIG.

The numerical work in this repository attempts to turn this idea into concrete mathematical models.

---

## 2. Boundary as an information gradient

BIG describes a structure using a scalar field

$$
\phi(x,t).
$$

This field may be interpreted abstractly as density, order, information concentration, or structural intensity.

The boundary is not defined only by where $\phi$ is nonzero.
It is more naturally associated with where $\phi$ changes rapidly.

Such changes are measured by the gradient

$$
\nabla \phi.
$$

A conventional gradient energy has the form

$$
|\nabla \phi|^2.
$$

BIG also emphasizes stronger nonlinear boundary contributions such as

$$
|\nabla \phi|^4.
$$

This quartic-gradient term plays an important role in the current numerical series.
It gives strong weight to boundary layers and allows compact-support-like structures to form and persist.

---

## 3. Representative model

A representative model studied in the current BIG numerical series is

$$
\partial_t \phi
===============

## \nabla\cdot(\phi^m\nabla\phi)

## \mu\phi

\gamma\nabla\cdot(|\nabla\phi|^2\nabla\phi).
$$

Here:

* $\phi$ is a scalar information-like field.
* $m$ controls degenerate mobility.
* $\mu$ is a linear damping parameter.
* $\gamma$ controls quartic-gradient stiffness.
* The term $-\gamma\nabla\cdot(|\nabla\phi|^2\nabla\phi)$ emphasizes strong nonlinear boundary gradients.

This equation is not claimed to be the complete mathematical definition of BIG.
It is a model system used to study how boundaries form, persist, deform, and fail.

---

## 4. B3–B4: Quadratic boundary landing

The B3–B4 numerical series studied compact-support structures and their boundary layers.

A key observation was that the field near the detected free boundary often follows a power-law landing:

$$
\phi(s) \sim A s^\nu,
$$

where $s$ is the distance from the boundary.

The measured exponent was close to

$$
\nu \approx 2.
$$

This suggests that the boundary is not a sharp numerical cutoff.
Instead, the field appears to land smoothly, approximately quadratically, at the boundary.

This behavior is referred to as **quadratic boundary landing**.

The importance of this result is that the boundary becomes a structured layer rather than a simple edge.

---

## 5. B5: Boundary shape and anisotropy

After the quadratic landing behavior was observed, the next question was whether boundary shape matters.

Real boundaries are rarely perfect circles.
They can be elongated, curved, compressed, distorted, or anisotropic.

The B5 direction explored how boundary geometry affects local boundary behavior.

This led to a broader question:

> If a boundary supports individuality or stability, does its shape affect the fate of the whole structure?

This question becomes central in the B8 series.

---

## 6. B7: Local boundary regularity and global runaway

The B7 series examined behavior near critical parameter regimes.

An important lesson from B7 was that local boundary regularity and global dynamical fate are not the same thing.

The local boundary profile may remain relatively regular, while the global field dynamics may still move toward runaway behavior.

This distinction introduced a new level of analysis:

* local boundary geometry,
* boundary-layer structure,
* global survival or runaway,
* and the separatrix between different dynamical fates.

In this sense, B7 shifted the focus from boundary formation to boundary fate.

---

## 7. B8: Finite-amplitude threshold

The B8 series introduced a finite-amplitude threshold.

The initial amplitude $A$ is varied, and the system is classified as either surviving up to a fixed observation time or entering runaway.

The critical amplitude is denoted by

$$
A_c.
$$

For a fixed observation time

$$
T=0.4,
$$

the interpretation is

$$
A < A_c
\quad \Rightarrow \quad
\text{survival up to } T=0.4,
$$

and

$$
A > A_c
\quad \Rightarrow \quad
\text{runaway before } T=0.4.
$$

This should be interpreted carefully.

$A_c$ is a **finite-time threshold**, not an infinite-time stability threshold.

Still, it is useful because it allows the robustness of a boundary-supported structure to be measured numerically.

---

## 8. B8.8: Boundary anisotropy controls the threshold

The B8.8 series studied compact elliptical initial conditions:

$$
\phi_0(x,y)
===========

A
\left(
1-\frac{x^2}{a^2}
-\frac{y^2}{b^2}
\right)_+^2.
$$

The ellipse ratio

$$
b/a
$$

controls the anisotropy of the initial boundary.

* $b/a=1.00$ corresponds to a circular boundary.
* $b/a=0.70$ corresponds to a moderately elongated ellipse.
* $b/a=0.40$ corresponds to a strongly elongated ellipse.

The numerical scan showed that the finite-time critical amplitude increases almost monotonically with $b/a$.

At $N=96$, the representative values were:

| ellipse ratio $b/a$ | critical amplitude $A_c$ |
| ------------------: | -----------------------: |
|                0.40 |                    0.113 |
|                0.55 |                    0.166 |
|                0.70 |                    0.230 |
|                0.85 |                    0.296 |
|                1.00 |                    0.346 |

The approximate linear relation was

$$
A_c \approx -0.0473 + 0.3966(b/a).
$$

The interpretation is direct:

> More circular boundaries tolerate larger amplitudes.
> More elongated boundaries become unstable at smaller amplitudes.

This is one of the strongest current numerical results in the BIG series.

It suggests that boundary shape is not merely an initial condition.
Boundary shape can act as a structural control parameter for nonlinear fate.

---

## 9. Boundary-energy reparameterization

The B8.8c regression analysis also examined the critical boundary-gradient energy

$$
E_{24,c}=E_{2,c}+E_{4,c}.
$$

Here:

* $E_{2,c}$ is the ordinary gradient energy at the critical initial state.
* $E_{4,c}$ is the quartic-gradient energy at the critical initial state.
* $E_{24,c}$ is their sum.

The observed relation was approximately

$$
A_c \sim E_{24,c}^{0.575}.
$$

Since $0.575$ is close to $1/2$, this can be read as an approximate square-root scaling:

$$
A_c \sim E_{24,c}^{1/2}.
$$

This should not be overinterpreted as a fully independent causal law, because $E_{24,c}$ is computed from the critical initial field itself.

The safer interpretation is:

> The critical points become well organized when reparameterized by boundary-gradient energy.

---

## 10. N=120 resolution validation

To test whether the B8.8 result was merely a coarse-grid artifact, a three-point validation was performed at $N=120$.

The tested ellipse ratios were

$$
b/a=0.40,\quad 0.70,\quad 1.00.
$$

The absolute critical amplitudes decreased under refinement, but the ordering remained unchanged:

$$
A_c(0.40)<A_c(0.70)<A_c(1.00).
$$

The comparison was:

| ellipse ratio $b/a$ | $A_c$ at N=96 | $A_c$ at N=120 | relative shift |
| ------------------: | ------------: | -------------: | -------------: |
|                0.40 |         0.113 |         0.0948 |         -16.2% |
|                0.70 |         0.230 |          0.203 |         -11.7% |
|                1.00 |         0.346 |          0.320 |          -7.3% |

This means:

> The absolute threshold values are resolution-dependent, but the monotone geometry dependence remains robust.

This is the most cautious and accurate interpretation of the B8.8d result.

---

## 11. Current interpretation

The current BIG numerical series supports the following interpretation:

> Boundary geometry affects the finite-time fate of nonlinear dissipative structures.

More specifically:

* Compact-support structures form organized boundary layers.
* These boundaries can land smoothly with an exponent near $\nu\approx2$.
* Local boundary regularity does not guarantee global survival.
* Finite-amplitude thresholds can be measured.
* Boundary anisotropy shifts those thresholds.
* More elongated boundaries become unstable at lower amplitudes.
* Boundary-gradient energy provides a useful reparameterization of critical states.

The current strongest claim is:

> In a degenerate mixed-gradient dissipative field, finite-time runaway thresholds depend systematically on boundary anisotropy. Although the absolute threshold values are resolution-dependent, the monotone ordering with respect to the ellipse ratio $b/a$ remains robust under N=96 to N=120 validation.

---

## 12. Scientific meaning

The BIG numerical work is related to several areas:

* nonlinear dissipative systems,
* free-boundary problems,
* compact-support structures,
* degenerate diffusion,
* gradient-flow-like dynamics,
* pattern formation,
* finite-amplitude stability,
* separatrix analysis.

The distinctive feature of BIG is that it treats the boundary not as a secondary surface, but as a primary information-bearing structure.

The B8 result is especially important because it moves from observing boundary formation to measuring how boundary geometry controls nonlinear fate.

---

## 13. Practical meaning

The present results are not yet a direct engineering model for a specific physical system.

However, they suggest a general design principle:

> Boundary shape affects structural robustness.

In many systems, distorted or elongated boundaries may be more sensitive to perturbation, while more symmetric boundaries may tolerate larger excitation.

This may eventually be relevant to interface dynamics, pattern control, membrane-like structures, information geometry, and state-space robustness.

Such applications require separate modeling and validation.

---

## 14. Limitations

The present results should be read with care.

* The model is exploratory.
* The thresholds are finite-time thresholds at $T=0.4$.
* The absolute values of $A_c$ depend on resolution.
* The N=120 validation is a three-point validation, not a full high-resolution scan.
* The results are numerical evidence, not rigorous mathematical proofs.
* Broader interpretations involving life, cognition, AI, or civilization remain speculative unless separately modeled.
* The boundary-energy scaling is a useful reparameterization, not a fully independent causal explanation.

---

## 15. Summary

BIG studies how boundaries form, persist, deform, and fail.

The current numerical sequence suggests the following progression:

1. Boundaries can emerge as compact-support structures.
2. They can land smoothly with a quadratic-like profile.
3. Their local structure can remain regular even near global runaway.
4. Finite-amplitude thresholds can separate survival and runaway.
5. Boundary anisotropy shifts those thresholds.
6. More elongated boundaries are less robust.
7. Boundary-gradient energy organizes the critical states.

The central message is:

> Boundary shape is not merely geometry.
> It can control the fate of a nonlinear structure.

Or more simply:

> The boundary is not just where a structure ends.
> It is part of what determines whether the structure survives.
