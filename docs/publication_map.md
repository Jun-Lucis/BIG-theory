# BIG Publication Map

This page summarizes the current publication and record structure of **Boundary Information Geometry (BIG)**.

BIG is a developing boundary-centered research programme. The entries below should be read as a map of reduced models, numerical studies, and structural comparisons, not as a single completed physical theory.

---

## Overview

| Series | Main theme                                                | Role in BIG                                        |
| ------ | --------------------------------------------------------- | -------------------------------------------------- |
| B3--B4 | Boundary-layer formation and quadratic landing            | Local boundary structure                           |
| B7     | Free-boundary exponent near runaway transition            | Local boundary regularity under global instability |
| B8     | Boundary anisotropy and finite-time separatrix thresholds | Geometry-controlled finite-amplitude stability     |
| B9     | Boundary cost versus nonlocal repulsion                   | Fission-like metastable energy landscape           |
| B10    | Finite-noise sustained capture                            | Stochastic-resonance-like boundary capture         |
| B11    | Post-capture hidden-depth inheritance                     | Non-assimilative post-fusion memory retention      |
| B12    | Unified boundary dynamics                                 | Reduced integration of B9, B10, and B11            |

---

## Core BIG sequence

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

The later B-series, especially B9--B12, was not originally designed to reproduce a specific target system.

Rather, the internal boundary logic of BIG led to reduced models whose structures later showed qualitative correspondences with familiar patterns such as surface-versus-repulsion competition, finite-noise capture windows, and inheritance-versus-assimilation transitions.

These are structural correspondences, not claims of direct quantitative equivalence.

---

## B-series records

### B3--B4: Boundary-layer formation and quadratic landing

**Theme:**
Compact-support-like boundary formation, local boundary-layer scaling, and quadratic landing.

**Core motif:**

$$
\phi(s) \sim A s^\nu,\qquad \nu \approx 2
$$

where (s) is the distance from the boundary.

**Role in BIG:**
B3--B4 established the recurring local boundary motif: the boundary behaves not as a passive edge, but as a finite-width layer with robust local scaling.

**Status:**
Numerical boundary-layer studies.

**Record / DOI:**
To be listed.

---

### B7: Free-boundary exponent near runaway transition

**Theme:**
Persistence of local free-boundary structure across a runaway transition.

**Core claim:**
The local free-boundary exponent remains approximately stable even when the global system approaches runaway. This suggests that runaway can arise from global dynamical instability rather than local boundary breakdown.

**Role in BIG:**
B7 separates local boundary regularity from global stability.

**Status:**
Numerical observation report.

**Record / DOI:**
To be listed.

---

### B8: Boundary anisotropy and finite-time separatrix thresholds

**Theme:**
Finite-time survival/runaway thresholds controlled by boundary anisotropy.

**Core claim:**
Boundary shape is not merely an initial condition; it can shift the finite-time separatrix. In the B8.8 scan, more anisotropic boundaries lowered the finite-time threshold.

**Recommended cautious wording:**

```text
Numerical evidence for a geometry-dependent finite-time separatrix
in a degenerate mixed-gradient dissipative field.
```

**Important limitation:**
The reported thresholds are finite-time values under the adopted observation time and runaway criterion. They are not asymptotic stability thresholds.

**Role in BIG:**
B8 turns the statement “boundary matters” into a measurable relation between boundary geometry and finite-amplitude stability.

**Record / DOI:**
Zenodo record:
https://zenodo.org/records/20645317

B7-related DOI mentioned in supporting notes:
https://doi.org/10.5281/zenodo.20603601

---

### B9: Minimal boundary-energy model for fission-like metastability

**Theme:**
A minimal competition between boundary cost and nonlocal repulsion.

**Core energy:**

$$
E(\Omega;\lambda)=\sigma P(\Omega)+\lambda C(\Omega)
$$

where (P(\Omega)) is a boundary cost and (C(\Omega)) is a Coulomb-like nonlocal repulsion term.

**Core result:**
The model produces a fission-like metastable landscape: a compact state protected by boundary cost, a finite pinch/scission barrier, and a separated branch favored by sufficiently strong nonlocal repulsion.

**Representative numerical landmarks:**

```text
near-scission threshold scale: lambda_near ≈ 55.9
open-boundary finite scan:    lambda_scan ≈ 48.06
far-separated estimate:       lambda_infty ≈ 42--44
```

**Structural comparison:**
B9 was not built as a nuclear-fission model. However, after the model was developed, its energy structure showed a qualitative correspondence with the classical surface-versus-Coulomb competition in macroscopic fission intuition.

**Important limitation:**
BIG-B9 is not a quantitative model of nuclear fission. It does not include shell corrections, quantum tunneling, pairing effects, fragment yields, cross sections, excitation dependence, or calibration to physical nuclei.

**Role in BIG:**
B9 shows that boundary cost versus nonlocal repulsion alone can generate fission-like metastability in a reduced geometric model.

**Record / DOI:**
https://doi.org/10.5281/zenodo.20799131

---

### B10: Stochastic-resonance-like fusion capture in a dynamic boundary model

**Theme:**
Finite-noise access to sustained capture.

**Core idea:**
Boundary capture is not defined by contact alone. It requires spatial proximity, internal-mode activation, and sustained locking.

**Core result:**
A finite-noise window appears: weak noise fails to activate sustained capture, intermediate noise enables capture, and strong noise destroys sustained locking.

**Important distinction:**

```text
first hit != sustained capture
```

At high noise, first contact may remain likely while sustained capture collapses.

**Important limitation:**
BIG-B10 is not a quantitative theory of nuclear fusion. It does not model Coulomb barriers, quantum tunneling, nuclear potentials, plasma kinetics, reaction cross sections, or real fusion energy release.

**Role in BIG:**
B10 gives the dynamic counterpart to B9: if B9 studies separation, B10 studies capture.

**Record / DOI:**
https://doi.org/10.5281/zenodo.20819427

---

### B11: Post-fusion boundary inheritance and non-assimilative stabilization

**Theme:**
Post-capture hidden-depth inheritance versus assimilation.

**Core question:**
After capture, does the fused boundary collapse into one parent state, or can it preserve both parent memories?

**Core model:**
A hidden-depth state

$$
h=(h_A,h_B)
$$

evolves in a stochastic gradient landscape with competing attractors for parent assimilation and two-parent inheritance.

**Core result:**
A transition from parent assimilation to hidden-depth inheritance occurs when the inheritance coupling exceeds a critical value. The critical coupling decreases with parent similarity and increases under stronger noise for robust inheritance thresholds.

**Important limitation:**
BIG-B11 is not a quantitative theory of biological inheritance, nuclear fusion, or real thermodynamic energy release. Energy drops are model-defined effective decreases in the post-fusion landscape.

**Role in BIG:**
B11 introduces the idea that fusion-like capture need not imply assimilation.

**Record / DOI:**
https://doi.org/10.5281/zenodo.20828439

---

### B12: Unified boundary dynamics with cross-sector coupling

**Theme:**
A reduced unified model connecting boundary approach, noise-assisted resonance locking, and hidden-depth inheritance.

**Core reduced variables:**

```text
d(t): boundary distance / proximity
R(t): internal resonance vector
h(t): hidden-depth inheritance state
```

**Core sequence:**

```text
boundary approach
    -> R-ignition
    -> sustained R-lock
    -> hidden-depth inheritance
```

**Core result:**
Introducing an ignition barrier into the resonance sector restores a finite-noise R-lock window in the unified model.

**Refined d2 scan:**

```text
sigma_R at peak lock:      approximately 0.070
P_lock at peak:            approximately 0.861
P_full_success at peak:    approximately 0.856
total raw rows:            5940
```

**Important distinction:**

```text
full success = strict R-lock AND hidden-depth inheritance
```

This distinction matters because high-noise trajectories may transiently resemble inheritance without satisfying sustained lock.

**Important limitation:**
BIG-B12 is a reduced variational-stochastic model. It is not a completed physical unification theory and does not claim quantitative modeling of nuclear, biological, or material systems.

**Role in BIG:**
B12 integrates the B9/B10/B11 motifs into a single reduced boundary-dynamical language.

**Record / DOI:**
DOI to be added after Zenodo publication.

---

## Suggested citation policy

For general discussion of the BIG research programme, cite the GitHub repository:

```text
Lucis, J. Boundary Information Geometry (BIG). GitHub repository.
https://github.com/Jun-Lucis/BIG-theory
```

For specific numerical or structural claims, cite the corresponding Zenodo record.

Examples:

```text
BIG-B9  -> cite the B9 Zenodo DOI
BIG-B10 -> cite the B10 Zenodo DOI
BIG-B11 -> cite the B11 Zenodo DOI
BIG-B12 -> cite the B12 Zenodo DOI once assigned
```

---

## Notes on certainty levels

The BIG repository contains materials with different certainty levels.

| Level                 | Description                                             |
| --------------------- | ------------------------------------------------------- |
| Conceptual frame      | Boundary-centered interpretation and research direction |
| Mathematical motif    | Reduced equations or structural mechanisms              |
| Numerical evidence    | Reproducible model-level computation                    |
| Structural comparison | Qualitative analogy with known phenomena                |
| Speculative extension | Possible future adaptation to other domains             |

Readers should not treat all statements as having the same evidential status. Numerical claims should be read together with the corresponding model equations, parameters, event definitions, and limitations.

---

## Future updates

Planned updates include:

* adding final DOI information for B12,
* adding direct links to Zenodo records,
* adding lightweight summary CSVs,
* separating raw data archives from GitHub-hosted summaries,
* adding per-series README files,
* and clarifying which materials are conceptual, numerical, or speculative.
