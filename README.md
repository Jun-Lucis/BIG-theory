# Boundary Information Geometry (BIG)

![State Map](figures/B4_3/B4_3_state_map.png)

Boundary Information Geometry (BIG) investigates
boundary formation, compact-support structures,
and quadratic boundary universality in nonlinear
dissipative systems.

## Main Numerical Result

ν ≈ 2

across a broad parameter range.


# Boundary Information Geometry (BIG)

Boundary Information Geometry (BIG) is an exploratory research program investigating how stable boundary structures emerge through nonlinear gradients, degenerate diffusion, and information-preserving interfaces.

The current numerical work focuses on **quadratic boundary universality** in degenerate mixed-gradient dissipative fields.

---

## Key Numerical Findings

The most robust observation obtained so far is:

```text
φ(s) ~ A s^ν
```

with

```text
ν ≈ 2
```

near detected free boundaries.

Across the BIG-B4 series, the exponent ν remains highly stable, while the boundary-layer width and amplitude consistency vary with model parameters.

Main findings:

* ν ≈ 2 remains robust across tested parameter ranges.
* Boundary-layer width changes significantly with μ and γ.
* Increasing γ improves amplitude consistency.
* Stable / Compressed / Residual regimes emerge in the B4.3 parameter map.

---

## Numerical Model

The primary evolution equation studied is:

```text
∂tφ = ∇·(φ²∇φ)
      − μφ
      − γ∇·(|∇φ|²∇φ)
      + S(x)
```

where:

* φ : scalar information field
* μ : dissipation parameter
* γ : quartic-gradient stiffness
* S(x) : localized source

---

## Latest Reports

### BIG-B4.3

**Boundary-Layer Stability and Compression under Joint Parameter Variation in Degenerate Mixed-Gradient Dissipative Fields**

Project page: [papers/BIG-B4.3](./papers/BIG-B4.3)

DOI:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20564435.svg)](https://doi.org/10.5281/zenodo.20564435)

---

### BIG-B4.1

**Quadratic Boundary Universality Scan**

Project page: [papers/BIG-B4.1](./papers/BIG-B4.1)

DOI:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20541748.svg)](https://doi.org/10.5281/zenodo.20541748)

---

### BIG-B3.1

**Boundary-Layer Scaling and Quadratic Landing**

Project page: [papers/BIG-B3.1](./papers/BIG-B3.1)

DOI:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20465842.svg)](https://doi.org/10.5281/zenodo.20465842)

---

## Repository Structure

```text
BIG-theory/

├── papers/
│   ├── BIG-B3.1/
│   ├── BIG-B4.1/
│   └── BIG-B4.3/
│
├── simulations/
│   ├── B4_1/
│   ├── B4_3/
│   └── utilities/
│
├── figures/
│   ├── B4_1/
│   ├── B4_3/
│   └── summary/
│
└── docs/
    ├── overview/
    ├── roadmap/
    └── terminology/
```

---

## Research Roadmap

### Completed

* Boundary-layer asymptotics
* Quadratic landing behavior
* Reproducibility scans
* μ-direction universality test
* Joint (μ, γ) boundary-compression map

### Ongoing

* Boundary-layer width scaling
* Amplitude consistency analysis
* Multi-boundary interaction studies

### Future

* Critical scaling analysis
* Higher-dimensional boundary dynamics
* Hierarchical boundary structures

---

## Interpretation

The current numerical results suggest a distinction between:

* **boundary geometry**
  measured by the exponent ν

* **boundary-layer state**
  measured by layer width and amplitude consistency

The exponent ν ≈ 2 appears highly robust, while the observable boundary layer can be stable, compressed, or residual depending on parameters.

---

## Disclaimer

Boundary Information Geometry is an independent exploratory research program.

The numerical reports focus on observable mathematical behavior of nonlinear dissipative systems. Broader interpretations remain speculative and are separated from established numerical results.

---

## Author

Jun Lucis

Independent Research

Repository:

https://github.com/Jun-Lucis/BIG-theory
