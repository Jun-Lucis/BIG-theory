# Boundary Information Geometry (BIG)

**Boundary Information Geometry (BIG)** is a boundary-centered research programme developed by **Jun Lucis**.

BIG starts from a simple organizing idea:

> Stable individuality is not only a property of what is inside a system.
> It is also formed, maintained, and transformed by boundaries.

In this view, boundaries are not passive edges. They are active structures that separate, preserve, mediate, deform, reconnect, and sometimes transmit memory across interaction.

BIG studies these processes through reduced mathematical models, numerical experiments, and structural comparisons.

BIG is **not presented as a completed physical theory**. It is a developing research framework organized around boundary formation, non-assimilation, finite-time stability, resonance, separation, capture, and inheritance.

---

## Core idea

The central intuition of BIG is that individuality and persistence require **non-assimilative boundaries**.

A boundary must be strong enough to preserve distinction, but not so closed that interaction becomes impossible. Stable systems may therefore be understood as structures that:

* maintain a boundary,
* resist total assimilation,
* interact across the boundary,
* reorganize under stress,
* and sometimes preserve memory through transformation.

This idea is explored through mathematical motifs such as compact boundary layers, quadratic landing, quartic-gradient stiffness, finite-time separatrix thresholds, boundary-energy competition, finite-noise capture, and hidden-depth inheritance.

---

## Current mathematical motifs

The current BIG model family includes several recurring structures.

### Boundary-layer formation

A scalar field may form compact or compact-like boundary layers rather than diffusing into a homogeneous bulk. In several numerical settings, the local boundary profile exhibits a quadratic landing form,

$$
\phi(s) \sim A s^\nu,\qquad \nu \approx 2
$$

where `s` is the distance from the boundary.

### Quartic-gradient boundary stiffness

A recurring BIG term is a quartic-gradient contribution,

$$
|\nabla \phi|^4
$$

which acts as a nonlinear boundary stiffness or non-assimilative tension.

### Finite-time separatrix

Some BIG models show a finite-amplitude threshold separating survival-like behavior from runaway-like behavior over a fixed observation time. Boundary geometry, especially anisotropy, can shift this threshold.

### Boundary energy versus nonlocal repulsion

A minimal geometric energy of the form

$$
E(\Omega;\lambda)=\sigma P(\Omega)+\lambda C(\Omega)
$$

can generate a fission-like metastable landscape: compact state, finite pinch barrier, and separated branch.

### Finite-noise resonance locking

In dynamic boundary models, noise can play a constructive and destructive role. Too little noise may fail to activate an internal channel; intermediate noise can enable sustained capture; excessive noise can destroy sustained locking.

### Hidden-depth inheritance

Post-capture states need not collapse into total assimilation. A hidden-depth state can retain multiple parent memories if inheritance coupling is sufficiently strong.

---

## B-series map

The BIG papers and notes are organized as a series of reduced models and numerical studies.

| Series | Main role                                                               | Status                               |
| ------ | ----------------------------------------------------------------------- | ------------------------------------ |
| B3--B4 | Compact-support-like boundary layers and quadratic landing              | numerical boundary-layer studies     |
| B7     | Persistence of free-boundary exponent near runaway transition           | numerical observation                |
| B8     | Boundary anisotropy and finite-time separatrix thresholds               | numerical evidence                   |
| B9     | Fission-like metastability from boundary cost versus nonlocal repulsion | reduced structural model             |
| B10    | Stochastic-resonance-like finite-noise sustained capture                | reduced dynamic model                |
| B11    | Post-fusion hidden-depth inheritance versus assimilation                | stochastic gradient model            |
| B12    | Unified boundary dynamics connecting B9, B10, and B11                   | reduced variational-stochastic model |

---

## Development path

The current BIG development can be read as a sequence of increasingly coupled boundary questions:

```text
boundary formation
    -> local boundary regularity
    -> finite-time stability thresholds
    -> separation / fission-like branching
    -> finite-noise capture
    -> post-capture inheritance
    -> unified cross-sector boundary dynamics
```

The later BIG series, especially B9--B12, was **not originally designed to reproduce any specific physical phenomenon** such as nuclear fission, nuclear fusion, biological inheritance, or material-interface dynamics.

The starting point was instead the internal logic of Boundary Information Geometry:

> If individuality is maintained by non-assimilative boundaries, then one should ask how boundaries form, stabilize, deform, separate, reconnect, and preserve memory across interaction.

From that perspective, several reduced models were explored.

B9 studied a minimal competition between boundary cost and nonlocal repulsion. Only after the model was developed did a structural correspondence with the classical surface-versus-repulsion intuition of liquid-drop fission become apparent.

B10 studied whether sustained capture can occur only within a finite-noise window.

B11 studied whether a post-capture state must collapse into parent assimilation, or whether hidden-depth inheritance can preserve more than one parent memory.

B12 then connected these motifs into a reduced unified model:

```text
boundary approach
    -> noise-assisted resonance locking
    -> hidden-depth inheritance
```

These correspondences should be understood as **structural convergences**, not as claims of direct quantitative equivalence.

---

## Important limitations

BIG is a developing mathematical and numerical research programme. The current models are intentionally reduced.

In particular:

* BIG-B9 is not a quantitative theory of nuclear fission.
* BIG-B10 is not a quantitative theory of nuclear fusion.
* BIG-B11 is not a quantitative theory of biological inheritance, nuclear fusion, or real energy release.
* BIG-B12 is not a completed physical unification theory.
* Reported thresholds are model-level numerical results and depend on the adopted equations, parameters, discretization, and event definitions.
* Applications to nuclear physics, materials science, biology, cognition, AI, or cosmology require domain-specific extensions before any quantitative claim can be made.

The current value of BIG is therefore not in claiming final physical explanation, but in providing a boundary-centered language in which stability, separation, capture, memory, and non-assimilation can be studied together.

---

## Structural comparison and future adaptation

Some BIG models have shown unexpectedly good structural alignment with established patterns in other fields.

For example, B9 was not built as a nuclear model, but its boundary-cost versus nonlocal-repulsion landscape naturally resembles the macroscopic surface-versus-Coulomb competition used in fission-barrier intuition. The comparison remains structural and qualitative.

This motivates a broader research direction:

> Test whether boundary-centered reduced models can be adapted to other fields where stability, interface geometry, separation, capture, memory, anisotropy, or failure thresholds are central.

Possible areas for future comparison include:

* interface and free-boundary problems,
* phase separation,
* membrane dynamics,
* material-interface failure,
* finite-amplitude stability,
* stochastic resonance,
* biological fusion and inheritance as structural analogies,
* AI individuality and non-assimilative interaction,
* and other systems where boundaries are active rather than passive.

---

## Zenodo records

A more detailed publication map will be maintained in:

```text
docs/publication_map.md
```

Current and planned entries include:

| Series | Title                                                                                              | DOI / record                            |
| ------ | -------------------------------------------------------------------------------------------------- | --------------------------------------- |
| B7     | Persistence of the Free-Boundary Exponent Across a Runaway Transition                              | to be listed                            |
| B8     | Boundary anisotropy and finite-time separatrix thresholds                                          | https://zenodo.org/records/20645317     |
| B9     | Minimal boundary-energy model for fission-like metastability                                       | https://doi.org/10.5281/zenodo.20799131 |
| B10    | Stochastic-Resonance-Like Fusion Capture in a Dynamic Boundary Model                               | https://doi.org/10.5281/zenodo.20819427 |
| B11    | Post-Fusion Boundary Inheritance and Non-Assimilative Stabilization                                | https://doi.org/10.5281/zenodo.20828439 |
| B12    | Unified Boundary Dynamics with Finite-Noise Resonance Locking and Post-Fusion Boundary Inheritance | DOI to be added                         |

---

## Repository structure

The repository is expected to evolve toward the following organization:

```text
BIG-theory/
├── README.md
├── CITATION.cff
├── LICENSE
├── docs/
│   ├── BIG_overview.md
│   ├── publication_map.md
│   ├── terminology.md
│   └── limitations.md
├── papers/
│   ├── B7_boundary_exponent/
│   ├── B8_finite_time_separatrix/
│   ├── B9_fission_like_metastability/
│   ├── B10_finite_noise_capture/
│   ├── B11_hidden_depth_inheritance/
│   └── B12_unified_boundary_dynamics/
├── figures/
│   ├── B9/
│   ├── B10/
│   ├── B11/
│   └── B12/
├── data/
│   ├── summaries/
│   └── small_reference_tables/
└── code/
    ├── B9/
    ├── B10/
    ├── B11/
    └── B12/
```

Large raw datasets should preferably be archived on Zenodo. GitHub should contain lightweight summary tables, reproducibility scripts, representative figures, and links to DOI records.

---

## Recommended citation

For general discussion of the BIG research programme, cite the GitHub repository:

```text
Lucis, J. Boundary Information Geometry (BIG). GitHub repository.
https://github.com/Jun-Lucis/BIG-theory
```

For specific numerical or structural claims, please cite the corresponding Zenodo DOI.

---

## Author

**Jun Lucis**
Independent researcher
Boundary Information Geometry (BIG)

Repository:
https://github.com/Jun-Lucis/BIG-theory
