# B8: Boundary Anisotropy and Finite-Time Separatrix Thresholds

This document summarizes the B8 numerical series of Boundary Information Geometry (BIG), especially the B8.8 eccentricity scan and the B8.8d resolution validation.

The central question of B8 is:

> How does boundary geometry affect the finite-time fate of a nonlinear dissipative field?

Earlier BIG stages focused mainly on the formation of compact-support boundary layers.
B8 moves one step further: it studies whether a boundary-supported structure survives or enters runaway, and how this finite-time fate depends on boundary shape.

---

## 1. Model

The representative model studied in B8 is

```math
\partial_t \phi
=
\nabla\cdot(\phi^m\nabla\phi)
-
\mu\phi
-
\gamma\nabla\cdot(|\nabla\phi|^2\nabla\phi).
```

The main parameters used in the B8.8 analysis are

```math
m=1.0,\quad \mu=0.3,\quad \gamma=0.8735.
```

The observation time is

```math
T=0.4.
```

The model combines:

* degenerate mobility,
* linear damping,
* quartic-gradient stiffness,
* compact-support-like boundary behavior,
* finite-time survival or runaway classification.

The equation is used here as an exploratory nonlinear dissipative field model for studying boundary-supported structures.

---

## 2. Initial condition

B8.8 uses compact elliptical initial conditions of the form

```math
\phi_0(x,y)
=
A
\left(
1-\frac{x^2}{a^2}
-\frac{y^2}{b^2}
\right)_+^2.
```

Here:

* `$A$` is the initial amplitude.
* `$a$` is the long-axis scale.
* `$b$` is the short-axis scale.
* `$b/a$` is the ellipse ratio.

The ellipse ratio controls boundary anisotropy.

* `$b/a=1.00$` corresponds to a circular boundary.
* `$b/a=0.70$` corresponds to a moderately elongated ellipse.
* `$b/a=0.40$` corresponds to a strongly elongated ellipse.


---

## 3. Finite-time threshold

For each ellipse ratio, the initial amplitude $A$ is varied.

The goal is to find a critical finite-time threshold

$$
A_c.
$$

The interpretation is:

$$
A < A_c
\quad \Rightarrow \quad
\text{survival up to } T=0.4,
$$

$$
A > A_c
\quad \Rightarrow \quad
\text{runaway before } T=0.4.
$$

This threshold should be interpreted carefully.

It is a **finite-time threshold**, not an asymptotic stability threshold.

In other words, $A_c$ measures the observed separatrix between survival and runaway up to the chosen finite time horizon.

---

## 4. B8.8 eccentricity scan at N=96

At resolution $N=96$, the ellipse ratio $b/a$ was scanned.

The representative critical amplitudes were:

| ellipse ratio $b/a$ | critical amplitude $A_c$ |
| ------------------: | -----------------------: |
|                0.40 |                    0.113 |
|                0.55 |                    0.166 |
|                0.70 |                    0.230 |
|                0.85 |                    0.296 |
|                1.00 |                    0.346 |

The ordering is monotone:

$$
A_c(0.40)
<
A_c(0.55)
<
A_c(0.70)
<
A_c(0.85)
<
A_c(1.00).
$$

Thus, more elongated boundaries become unstable at smaller amplitudes, while more circular boundaries tolerate larger amplitudes.

A simple linear fit gives approximately

$$
A_c \approx -0.0473 + 0.3966(b/a).
$$

This is one of the clearest results in the B8 series.

It suggests that boundary anisotropy is not merely a visual feature of the initial condition.
It acts as a structural control parameter for the finite-time separatrix.

---

## 5. Boundary-energy reparameterization

B8.8c also examined the critical boundary-gradient energy

$$
E_{24,c}=E_{2,c}+E_{4,c}.
$$

Here:

* $E_{2,c}$ is the ordinary gradient energy at the critical initial state,
* $E_{4,c}$ is the quartic-gradient energy at the critical initial state,
* $E_{24,c}$ is their sum.

The critical amplitudes were approximately organized by

$$
A_c \sim E_{24,c}^{0.575}.
$$

Since $0.575$ is close to $1/2$, this can be read as an approximate square-root scaling:

$$
A_c \sim E_{24,c}^{1/2}.
$$

This should not be interpreted as a fully independent causal law, because $E_{24,c}$ is computed from the critical initial field itself.

A safer interpretation is:

> Critical states become well organized when reparameterized by boundary-gradient energy.

---

## 6. N=120 resolution validation

To test whether the B8.8 result was only a coarse-grid artifact, a three-point validation was performed at $N=120$.

The tested ellipse ratios were

$$
b/a=0.40,\quad 0.70,\quad 1.00.
$$

The comparison was:

| ellipse ratio $b/a$ | $A_c$ at N=96 | $A_c$ at N=120 | relative shift |
| ------------------: | ------------: | -------------: | -------------: |
|                0.40 |         0.113 |         0.0948 |         -16.2% |
|                0.70 |         0.230 |          0.203 |         -11.7% |
|                1.00 |         0.346 |          0.320 |          -7.3% |

The absolute thresholds decreased under refinement from $N=96$ to $N=120$.

However, the ordering remained the same:

$$
A_c(0.40)<A_c(0.70)<A_c(1.00).
$$

This supports the main structural conclusion:

> The absolute value of the threshold is resolution-dependent, but the monotone dependence on boundary anisotropy remains robust.

---

## 7. Interpretation

The main interpretation of B8 is:

> Boundary geometry affects the finite-time fate of nonlinear dissipative structures.

More specifically:

* More circular boundaries have higher finite-time thresholds.
* More elongated boundaries have lower finite-time thresholds.
* Boundary anisotropy narrows the survival basin.
* The finite-time separatrix shifts systematically with ellipse ratio $b/a$.
* Boundary-gradient energy provides a useful reparameterization of the critical states.

In intuitive terms:

> Rounder boundaries are more robust.
> More distorted boundaries are more fragile.

In BIG language:

> Boundary shape is not merely an initial condition.
> It can act as a structural control parameter for nonlinear fate.

---

## 8. Relation to BIG

BIG studies boundaries as information-bearing structures.

B3–B4 showed that compact-support boundaries can form smooth quadratic-like boundary layers.

B7 showed that local boundary regularity and global runaway fate can differ.

B8 shows that the finite-time separatrix between survival and runaway is affected by boundary anisotropy.

Thus, B8 moves BIG from the study of boundary formation to the study of boundary-controlled fate.

The key conceptual advance is:

> The boundary does not only mark where a structure ends.
> Its shape can influence whether the structure survives.

---

## 9. Safe claim

The safest current technical claim is:

> In a degenerate mixed-gradient dissipative field, finite-time runaway thresholds depend systematically on boundary anisotropy. Although the absolute threshold values are resolution-dependent, the monotone ordering with respect to the ellipse ratio $b/a$ remains robust under N=96 to N=120 validation.

This wording is intentionally cautious.

It avoids claiming:

* universal law,
* asymptotic stability,
* rigorous proof,
* direct physical universality.

It states only what the numerical evidence currently supports.

---

## 10. Limitations

The B8 results should be interpreted with the following cautions:

* $A_c$ is a finite-time threshold at $T=0.4$.
* It is not an infinite-time stability threshold.
* The absolute values of $A_c$ are resolution-dependent.
* The N=120 validation is a three-point validation, not a full high-resolution scan.
* The model is an exploratory nonlinear dissipative field model.
* Broader applications require separate modeling and validation.
* The boundary-energy scaling is a useful reparameterization, not an independent causal explanation.

---

## 11. Summary

The B8 result can be summarized in one sentence:

> Boundary anisotropy controls finite-time separatrix thresholds in a model degenerate mixed-gradient dissipative field.

Or more intuitively:

> The shape of the boundary affects how easily the structure enters runaway.

This is the current strongest bridge between the mathematical BIG model and the broader BIG idea that boundaries carry structural information.
