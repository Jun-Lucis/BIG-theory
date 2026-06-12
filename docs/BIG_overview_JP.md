# Boundary Information Geometry (BIG)

**Boundary Information Geometry (BIG)** is an independent exploratory research program that studies boundaries as information-carrying structures.

The central idea is simple:

> Stable individuality is not only a property of the bulk interior.  
> It is organized by boundaries that separate, preserve, and mediate information.

This repository contains numerical reports, figures, and papers on nonlinear dissipative field models in which compact-support structures, quadratic boundary layers, and finite-time runaway thresholds emerge.

---

## Current status

The BIG numerical series has progressed through three main stages.

### 1. B3–B4: Quadratic boundary-layer universality

Compact-support structures form smooth free boundaries, with a robust local landing exponent close to

$$
\nu \approx 2.
$$

### 2. B7: Critical transition and runaway onset

Near a critical parameter region, the local boundary profile remains regular while the global dynamics may transition toward runaway behavior.

### 3. B8: Finite-amplitude separatrix and boundary anisotropy

Recent B8 results show that finite-time runaway thresholds are controlled by boundary geometry.

In particular, elliptical initial boundaries with stronger anisotropy have lower critical amplitudes.

The current strongest numerical statement is:

> Boundary anisotropy shifts the finite-time separatrix.  
> More elongated boundaries become unstable at smaller amplitudes, while more circular boundaries tolerate larger amplitudes.

This should be interpreted as **finite-time numerical evidence**, not as an asymptotic stability theorem.

---

## Main model

A representative field equation studied in the current BIG numerical series is

$$
\partial_t \phi
=
\nabla\cdot(\phi^m\nabla\phi)
-
\mu\phi
-
\gamma\nabla\cdot(|\nabla\phi|^2\nabla\phi).
$$

Here:

- $\phi$ is a scalar information-like field.
- $m$ controls degenerate mobility.
- $\mu$ is a linear dissipation parameter.
- $\gamma$ controls quartic-gradient stiffness.
- The quartic-gradient term emphasizes strong boundary layers.

Earlier versions also studied localized source terms $S(x)$.  
The present B8 separatrix analysis focuses on compact initial data without source forcing.

---

## Key numerical findings

### 1. Quadratic boundary landing

Across the B3–B4 series, compact-support structures exhibit a smooth boundary landing of the form

$$
\phi(s) \sim A s^\nu,
$$

with

$$
\nu \approx 2,
$$

where $s$ is the distance from the detected free boundary.

This suggests that the boundary is not a sharp cutoff but a self-organized layer.

---

### 2. Finite-time runaway threshold

In the B8 series, the initial amplitude $A$ is varied to locate a finite-time threshold $A_c$.

For a fixed observation time $T=0.4$, initial conditions below $A_c$ survive up to $T$, while those above $A_c$ enter runaway according to the numerical criterion.

This threshold is a finite-time separatrix indicator:

$$
A < A_c \quad \Rightarrow \quad \text{survival},
$$

$$
A > A_c \quad \Rightarrow \quad \text{runaway}.
$$

It should not be read as an infinite-time stability threshold.

---

### 3. Boundary anisotropy controls the threshold

For elliptical compact initial conditions,

$$
\phi_0(x,y)
=
A
\left(
1-\frac{x^2}{a^2}-\frac{y^2}{b^2}
\right)_+^2,
$$

the ellipse ratio $b/a$ controls the threshold.

At $N=96$, the eccentricity scan gave approximately:

| ellipse ratio b/a | critical amplitude A_c |
|---:|---:|
| 0.40 | 0.113 |
| 0.55 | 0.166 |
| 0.70 | 0.230 |
| 0.85 | 0.296 |
| 1.00 | 0.346 |

The relationship is nearly linear:

$$
A_c \approx -0.0473 + 0.3966(b/a).
$$

Thus, circular boundaries tolerate larger amplitudes, while elongated boundaries become unstable at smaller amplitudes.

---

### 4. Boundary-energy reparameterization

The critical points can also be re-expressed using the boundary-gradient energy

$$
E_{24,c}=E_{2,c}+E_{4,c}.
$$

Numerically, the critical amplitude approximately follows

$$
A_c \sim E_{24,c}^{0.575},
$$

which is close to a square-root scaling,

$$
A_c \sim E_{24,c}^{1/2}.
$$

This is best interpreted as a useful reparameterization of the critical points, not as an independent causal law.

---

### 5. Resolution validation

A three-point $N=120$ validation was performed for

$$
b/a=0.40,\quad 0.70,\quad 1.00.
$$

The absolute thresholds decreased under refinement, but the ordering remained robust:

$$
A_c(0.40)<A_c(0.70)<A_c(1.00).
$$

This indicates that the geometry-dependent separatrix shift is not merely a coarse-grid artifact, although the numerical location of the threshold remains resolution-dependent.

---

## Numerical series overview

| Series | Main focus | Status |
|---|---|---|
| B3.1 | Quadratic boundary-layer discovery | Completed |
| B4.1 | Universality scan across parameters | Completed |
| B4.3 | State map in (mu, gamma) space | Completed |
| B7 | Critical transition and runaway onset | Completed |
| B8.6 | Finite-amplitude threshold detection | Completed |
| B8.8 | Boundary anisotropy scan | Completed |
| B8.8d | N=120 resolution validation | Completed |

---

## Repository structure

Current structure:

```text
BIG-theory/
  README.md
  figures/
  papers/
  BIG_Theory_Full_Paper.pdf
  Beyond_Alignment_v2_2_Refined.pdf
```

Planned organization:

```text
docs/
  BIG_overview_JP.md
  BIG_overview_EN.md
  B7_to_B8_summary.md

papers/
  BIG_third_party_paper_JP_no_wet_etching.pdf
  BIG_B8_one_page_paper_JP.pdf

zenodo/
  records.md
```

Heavy numerical fields and ZIP archives should be stored on Zenodo rather than directly in this GitHub repository.

---

## Zenodo records

The numerical reports and data packages are archived on Zenodo.

GitHub is used as an entry point and project map.  
Zenodo is used for preservation and citation.

Recommended wording for the current B8 package:

> Numerical evidence for boundary-anisotropy-controlled finite-time separatrix thresholds in a degenerate mixed-gradient dissipative field.

---

## Interpretation

The BIG results suggest the following distinction:

- **Local boundary geometry**: measured by boundary landing exponents such as $\nu$.
- **Boundary-layer state**: measured by width, amplitude consistency, and compression.
- **Global dynamical fate**: measured by finite-time survival or runaway.
- **Separatrix position**: controlled by amplitude and boundary geometry.

The key conceptual lesson is:

> Boundary shape is not merely an initial condition.  
> It can act as a structural control parameter for nonlinear fate.

---

## Limitations

This project is exploratory.

The current numerical results should be interpreted with the following cautions:

- The thresholds are finite-time thresholds at $T=0.4$.
- The absolute threshold values are resolution-dependent.
- The model is a simplified nonlinear dissipative field system.
- Broader interpretations involving life, cognition, civilization, or AI remain speculative unless separately modeled.
- The results are numerical evidence, not rigorous mathematical proofs.

---

## Author

**Jun Lucis**  
Independent research

---

## Short description

Boundary Information Geometry studies how stable boundary structures emerge, persist, deform, and fail in nonlinear dissipative systems.
