# Boundary Information Geometry (BIG)

Boundary Information Geometry (BIG) is an exploratory research program investigating how stable structures emerge through boundary formation, nonlinear gradients, and information-preserving interfaces.

The current numerical work focuses on quadratic boundary universality in degenerate mixed-gradient dissipative fields.

---

## Current Status

### Mathematical Results

* Boundary asymptotics established
* Quadratic landing behavior identified
* Compact-support boundary structures observed
* Robust boundary exponent:

[
\nu \approx 2
]

across a wide parameter range.

### Numerical Reports

| Report   | Topic                                                                     |
| -------- | ------------------------------------------------------------------------- |
| BIG-B3.1 | Boundary-layer scaling and quadratic landing                              |
| BIG-B4.1 | Universality of quadratic boundary layers                                 |
| BIG-B4.3 | Stability, compression, and recovery under joint ((\mu,\gamma)) variation |

---

## Key Observation

The most robust numerical observation obtained so far is:

[
\phi(s)
\sim
A s^2
]

near detected free boundaries.

The exponent

[
\nu \approx 2
]

appears remarkably stable under variations of dissipation strength, initial conditions, and quartic-gradient stiffness.

---

## Numerical Model

The primary evolution equation studied is

[
\partial_t \phi
===============

## \nabla \cdot (\phi^2 \nabla \phi)

## \mu \phi

\gamma
\nabla \cdot
\left(
|\nabla\phi|^2
\nabla\phi
\right)
+
S(x)
]

where

* (\phi) : scalar information field
* (\mu) : dissipation parameter
* (\gamma) : quartic-gradient stiffness
* (S(x)) : localized source

---

## Repository Structure

```text
BIG-theory/

├── papers/
│   ├── BIG-B3.1
│   ├── BIG-B4.1
│   ├── BIG-B4.3
│   └── archive/

├── simulations/
│   ├── B4_1/
│   ├── B4_3/
│   └── utilities/

├── figures/
│   ├── B4_1/
│   ├── B4_3/
│   └── summary/

└── docs/
    ├── overview/
    ├── roadmap/
    └── terminology/
```

---

## Latest Zenodo Reports

Add DOI links below.

### BIG-B4.3

Boundary-Layer Stability and Compression under Joint Parameter Variation in Degenerate Mixed-Gradient Dissipative Fields

DOI:
https://doi.org/10.5281/zenodo.20465842

---

### BIG-B4.1

Quadratic Boundary Universality Scan

DOI:
(Insert DOI)

---

### BIG-B3.1

Boundary-Layer Scaling and Quadratic Landing

DOI:
https://doi.org/10.5281/zenodo.20465842

---

## Research Roadmap

### Completed

* Boundary asymptotics
* Quadratic landing
* Universality scans
* Boundary compression mapping

### Ongoing

* Width scaling laws
* Multi-boundary interaction
* Critical scaling analysis

### Future

* Higher-dimensional boundary dynamics
* Hierarchical boundary structures
* Generalized boundary geometry

---

## Disclaimer

Boundary Information Geometry is an independent exploratory research program.

The numerical reports focus on observable mathematical behavior of nonlinear dissipative systems. Broader interpretations remain speculative and are clearly separated from established numerical results.

---

## Author

Jun Lucis

Independent Research

GitHub:
https://github.com/Jun-Lucis/BIG-theory
