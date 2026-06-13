# Boundary Information Geometry (BIG)

**Boundary Information Geometry (BIG)** is an independent exploratory research program that studies boundaries as information-carrying structures.

The central idea is simple:

> Stable individuality is not only a property of the bulk interior.  
> It is organized by boundaries that separate, preserve, and mediate information.

This repository collects papers, figures, numerical reports, and project notes related to BIG.

The current numerical focus is on nonlinear dissipative field models where compact-support structures, quadratic boundary layers, finite-time runaway thresholds, and geometry-dependent separatrix shifts appear.

---

## Current status

The BIG numerical series has progressed through three main stages.

### 1. B3-B4: Quadratic boundary-layer universality

Compact-support structures form smooth free boundaries with a robust local landing exponent close to:

**nu approx 2**

This suggests that the boundary is not a sharp cutoff, but a self-organized layer where the field smoothly lands to zero.

### 2. B7: Critical transition and runaway onset

Near a critical parameter region, the local boundary profile can remain regular while the global dynamics transitions toward runaway behavior.

This distinction is important:

- The local boundary layer may remain structured.
- The global field dynamics may still cross into a different fate.
- Runaway is therefore not simply local boundary collapse.

### 3. B8: Finite-amplitude separatrix and boundary anisotropy

Recent B8 results show that finite-time runaway thresholds are controlled by boundary geometry.

In particular, elliptical initial boundaries with stronger anisotropy have lower critical amplitudes.

The current strongest numerical statement is:

> Boundary anisotropy shifts the finite-time separatrix.  
> More elongated boundaries become unstable at smaller amplitudes, while more circular boundaries tolerate larger amplitudes.

This should be interpreted as **finite-time numerical evidence**, not as an asymptotic stability theorem.

---

## Representative figures

### Boundary anisotropy controls the finite-time threshold

![B8.8 Ac vs ellipse ratio](figures/B8_8_Ac_vs_ratio.png)

The critical amplitude A_c increases almost linearly with the ellipse ratio b/a. More elongated boundaries have lower finite-time runaway thresholds.

---

### Boundary-energy reparameterization

![B8.8 Ac vs E24](figures/B8_8_Ac_vs_E24_power.png)

The critical points collapse smoothly when re-expressed by the critical boundary-gradient energy E24_c.

---

### Resolution validation

![B8.8d N96 vs N120](figures/B8_8d_N96_vs_N120_Ac.png)

The N=120 validation preserves the monotone ordering with respect to b/a, although the absolute thresholds decrease under refinement.

## Main model

A representative field equation studied in the current BIG numerical series is:

**d phi / dt = div(phi^m grad phi) - mu phi - gamma div(|grad phi|^2 grad phi)**

Here:

- **phi** is a scalar information-like field.
- **m** controls degenerate mobility.
- **mu** is a linear dissipation parameter.
- **gamma** controls quartic-gradient stiffness.
- The quartic-gradient term emphasizes strong boundary layers.

Earlier versions also studied localized source terms such as **S(x)**.

The present B8 separatrix analysis focuses on compact initial data without source forcing.

---

## Conceptual motivation

BIG starts from the idea that boundaries are not secondary surfaces around a bulk object.

Instead, boundaries can be interpreted as active structures that:

- separate inside from outside,
- preserve individuality,
- mediate interaction,
- store gradient information,
- control stability and failure.

In this view, a stable individual structure is not simply a dense interior.

It is a field configuration whose boundary prevents complete assimilation while still allowing interaction.

A short conceptual summary is:

> A structure becomes individual not by being isolated, but by maintaining a boundary through which it can resonate without being absorbed.

---

## Key numerical findings

### 1. Quadratic boundary landing

Across the B3-B4 series, compact-support structures exhibit a smooth boundary landing of the form:

**phi(s) approx A s^nu**

where **s** is the distance from the detected free boundary.

The measured exponent is close to:

**nu approx 2**

This suggests that the boundary is not a discontinuous edge but a smooth self-organized layer.

---

### 2. Finite-time runaway threshold

In the B8 series, the initial amplitude **A** is varied to locate a finite-time threshold **A_c**.

For a fixed observation time **T = 0.4**, initial conditions below **A_c** survive up to **T**, while those above **A_c** enter runaway according to the numerical criterion.

This threshold is a finite-time separatrix indicator:

**A < A_c means survival**

**A > A_c means runaway**

It should not be read as an infinite-time stability threshold.

---

### 3. Boundary anisotropy controls the threshold

For elliptical compact initial conditions, the initial profile is:

**phi0(x,y) = A(1 - x^2/a^2 - y^2/b^2)_+^2**

The ellipse ratio **b/a** controls the threshold.

At **N = 96**, the eccentricity scan gave approximately:

| ellipse ratio b/a | critical amplitude A_c |
|---:|---:|
| 0.40 | 0.113 |
| 0.55 | 0.166 |
| 0.70 | 0.230 |
| 0.85 | 0.296 |
| 1.00 | 0.346 |

The relationship is nearly linear:

**A_c approx -0.0473 + 0.3966(b/a)**

Thus, circular boundaries tolerate larger amplitudes, while elongated boundaries become unstable at smaller amplitudes.

This is the current central B8 result.

---

### 4. Boundary-energy reparameterization

The critical points can also be re-expressed using the boundary-gradient energy:

**E24_c = E2_c + E4_c**

Numerically, the critical amplitude approximately follows:

**A_c ~ E24_c^0.575**

This is close to a square-root scaling:

**A_c ~ sqrt(E24_c)**

This is best interpreted as a useful reparameterization of the critical points, not as an independent causal law.

---

### 5. Resolution validation

A three-point **N = 120** validation was performed for:

- **b/a = 0.40**
- **b/a = 0.70**
- **b/a = 1.00**

The absolute thresholds decreased under refinement from **N = 96** to **N = 120**, but the ordering remained robust:

**A_c(0.40) < A_c(0.70) < A_c(1.00)**

This indicates that the geometry-dependent separatrix shift is not merely a coarse-grid artifact, although the numerical location of the threshold remains resolution-dependent.

The most conservative conclusion is:

> The absolute finite-time threshold is resolution-dependent, but the monotone dependence on boundary anisotropy is structurally robust under the current validation.

---

## Numerical series overview

| Series | Main focus | Status |
|---|---|---|
| B3.1 | Quadratic boundary-layer discovery | Completed |
| B4.1 | Universality scan across parameters | Completed |
| B4.3 | State map in the mu-gamma parameter space | Completed |
| B7 | Critical transition and runaway onset | Completed |
| B8.6 | Finite-amplitude threshold detection | Completed |
| B8.8 | Boundary anisotropy scan | Completed |
| B8.8d | N=120 resolution validation | Completed |

---

## Interpretation

The BIG results suggest the following distinction.

### Local boundary geometry

Local boundary geometry is measured by boundary landing exponents such as **nu**.

This describes how the field approaches zero near the detected free boundary.

### Boundary-layer state

The boundary-layer state includes width, amplitude consistency, compression, and gradient concentration.

This describes how the boundary stores and distributes gradient energy.

### Global dynamical fate

The global fate is measured by finite-time survival or runaway.

This describes whether the entire field configuration remains within a stable basin or crosses into a runaway regime.

### Separatrix position

The separatrix position is controlled by amplitude and boundary geometry.

The B8 results suggest that boundary shape is not merely an initial condition.

It can act as a structural control parameter for nonlinear fate.

---

## Repository structure

Current structure:

- **README.md**
- **figures/**
- **papers/**
- **BIG_Theory_Full_Paper.pdf**
- **Beyond_Alignment_v2_2_Refined.pdf**

Planned organization:

- **docs/**
  - **BIG_overview_JP.md**
  - **BIG_overview_EN.md**
  - **B7_to_B8_summary.md**
- **papers/**
  - **BIG_third_party_paper_JP_no_wet_etching.pdf**
  - **BIG_B8_one_page_paper_JP.pdf**
- **zenodo/**
  - **records.md**

Heavy numerical fields and ZIP archives should be stored on Zenodo rather than directly in this GitHub repository.

---

## Zenodo records

The numerical reports and data packages are archived on Zenodo.

GitHub is used as an entry point and project map.

Zenodo is used for preservation and citation.

Current B8 package:

- Zenodo record: https://zenodo.org/records/20645317

Recommended wording for the current B8 package:

> Numerical evidence for boundary-anisotropy-controlled finite-time separatrix thresholds in a degenerate mixed-gradient dissipative field.

---

## Papers and reports

This repository contains or links to the following types of documents:

- conceptual BIG overview papers,
- numerical reports on compact-support boundary layers,
- B-series reports on quadratic boundary landing,
- B7-B8 reports on finite-time separatrix behavior,
- third-party-oriented summaries for readers new to BIG.

The current preferred introductory document is:

**BIG_third_party_paper_JP_no_wet_etching.pdf**

This document explains BIG from the beginning and summarizes the B3-B8 numerical flow for general readers.

---

## Practical meaning

BIG is currently a mathematical and numerical framework, not an engineering-ready predictive theory.

However, its boundary-centered language may be useful for thinking about systems where stability depends on interface geometry, anisotropy, and finite-amplitude perturbations.

Possible long-term areas of relevance include:

- nonlinear field dynamics,
- free-boundary problems,
- dissipative pattern formation,
- compact-support structures,
- interface stability,
- biological boundary metaphors,
- information geometry,
- AI state-space robustness.

These broader interpretations should be treated as conceptual extensions unless independently modeled.

---

## Limitations

This project is exploratory.

The current numerical results should be interpreted with the following cautions:

- The thresholds are finite-time thresholds at **T = 0.4**.
- The absolute threshold values are resolution-dependent.
- The model is a simplified nonlinear dissipative field system.
- The reported trends are numerical evidence, not rigorous mathematical proofs.
- Broader interpretations involving life, cognition, civilization, or AI remain speculative unless separately modeled.
- The term "information" in BIG is used as a structural and geometric concept, not as a fully formalized Shannon-information theory in the current numerical work.

---

## Current conclusion

The strongest current BIG numerical conclusion is:

> In a degenerate mixed-gradient dissipative field, compact boundary structures show smooth quadratic landing, and finite-time runaway thresholds are systematically shifted by boundary anisotropy.

In simpler words:

> Boundaries are not passive edges.  
> Their shape can influence whether a structure persists or fails.

## Documentation

- [BIG overview in Japanese](docs/BIG_overview_JP.md)
- [BIG overview in English](docs/BIG_overview_EN.md)
- [B7 to B8 technical summary](docs/B7_to_B8_summary.md)
- [B8 anisotropic separatrix summary](docs/B8_anisotropic_separatrix_summary.md)
- [Zenodo records](zenodo/records.md)

---

## Author

**Jun Lucis**  
Independent research

---
