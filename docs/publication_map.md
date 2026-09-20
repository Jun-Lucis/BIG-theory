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
| B13    | Boundary folding and observation-like state selection      | Reduced observation / self-measurement model        |
| B13.1  | Rotated-basis observation and empirical selection kernel   | Basis-dependent selection diagnostics               |
| B14    | Boundary history and lineage-level persistence              | Writing, fusion, division, and trace retention      |
| B15    | Observation traces and boundary history                     | Operator representation of history-dependent update |
| B16    | Memory-bearing free boundaries                              | History as an internal state affecting later response |
| B17    | Stored history versus readable history                      | Moving-boundary-frame readability                   |
| B18    | Boundary readout operators                                  | Interface-core path exposure                        |
| B19    | Boundary-core channel diagnostics                           | Direction-dependent upstream channel families       |
| B20    | Finite-window response boundaries                           | Operator-generated response geometry in parameter space |

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
    -> observation-like boundary folding
    -> boundary history and operator representation
    -> memory-bearing moving boundaries
    -> boundary-dependent readout
    -> boundary-core channel families
    -> operator-generated finite-time response boundaries
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
https://doi.org/10.5281/zenodo.20872005


---

### B13: Boundary folding as a reduced model of observation and self-measurement

**Theme:** Observation-like interaction as boundary folding and hidden-depth state selection.

B13 studies a reduced observer--system interaction in which boundary overlap couples hidden-depth states and changes basin selection. The numerical comparison includes Born-like reference curves, but the model does **not** derive quantum measurement, the Born rule, uncertainty, consciousness, or AI perception.

**Record / DOI:**  
https://doi.org/10.5281/zenodo.21072783

---

### B13.1: Rotated-basis observation and the empirical BIG selection kernel

**Theme:** Extension of B13 to rotated-basis observation and an empirical state-selection kernel.

**Record / DOI:**  
https://doi.org/10.5281/zenodo.21108338

---

### B14: Boundary history and lineage-level persistence

**Theme:** Explicit boundary-history fields and reduced operators for writing, forgetting, fusion, division, and multi-generation trace retention.

B14 introduces an explicit history field on the boundary and tests whether localized traces can survive transformation at a lineage level. It is a reduced operator model, not a quantitative model of biological heredity, fertilization, or cell division.

**Record / DOI:**  
https://doi.org/10.5281/zenodo.21144373

---

### B15: Observation traces and boundary history

**Theme:** A reduced operator representation connecting B13/B13.1 observation traces with B14 boundary history.

B15 distinguishes normalized density-like history representation from absolute history amplitude and classifies update maps as linear, affine, nonlinear, or state-dependent. The Hilbert-like notation is representational; it is not a derivation of quantum mechanics.

**Record / DOI:**  
https://doi.org/10.5281/zenodo.21173333

---

### Layered Mathematical Framework

A consolidation paper organizes BIG as a **layered family of models**, rather than one universal equation. It connects boundary formation, landing, global stability, shape/topology transition, capture, state selection, and boundary history while auditing results through B15.

**Zenodo record:**  
https://zenodo.org/records/22161614

---

### B16: Memory-bearing free boundaries

**Theme:** Coupling a moving free-boundary field to an internal history field.

The key structural test is whether a past localized stimulus can be retained and alter a later local response when feedback coupling is present. The model is reduced and exploratory, not a calibrated biological-memory model.

**Zenodo record:**  
https://zenodo.org/records/22660005

---

### B17: Stored history versus readable history

**Theme:** Retention alone is not sufficient; history must remain readable from the current moving-boundary frame.

B17 distinguishes global stored history from the locally sampleable history that can affect a later response. Boundary-anchored and laboratory-fixed writing provide controls for this distinction.

**Zenodo record:**  
https://zenodo.org/records/22677581

---

### B18: Boundary readout operators in Boundary Information Geometry

**Theme:** From read-start local history to interface-core path exposure.

A representative readout has the form

$
\mathcal{L}_{\mathrm{read}}
=
\int_{t_0}^{t_1}\lambda(t)
\int m(x,t)W(x;R(t))G_\Sigma[\Phi](x,t)\,dx\,dt.
$

Across the reduced front-and-trace diagnostics, path-integrated threshold/interface-core exposure organizes later response better than global trace mass or read-start local load alone. The result is an operator-level statement: retained history becomes dynamically effective after projection through a boundary-dependent readout operator.

**Zenodo record:**  
https://zenodo.org/records/22690970

---

### B19: Boundary-core channel diagnostics

**Theme:** Boundary-core, Biot--Savart strain, signed alignment, and finite-window enstrophy-balance diagnostics in synthetic divergence-free 3D vorticity fields.

The integrated B19 result does not support a single ray-independent scalar threshold. Instead, the numerical diagnostics identify direction-dependent upstream boundary-core channel families feeding a common downstream production-versus-dissipation / total-balance organization.

This is a reduced finite-window numerical diagnostic. It does **not** prove Navier--Stokes blow-up or regularity.

**Integrated Zenodo record:**  
https://zenodo.org/records/22726848

**Finite-time response follow-up:**  
https://zenodo.org/records/22769513

---

### B20: Operator-generated finite-window response boundaries

**Theme:** Response boundaries generated by finite-time evolution and a chosen readout.

B20 uses

$
F_T(P)=Z[U_T(P)]-Z[P],
\qquad
\mathcal{B}_T=\{P:F_T(P)=0\},
$

so the relevant boundary need not be a physical membrane or free boundary: it can be a zero set in parameter space generated by the evolution operator and readout.

B20.5 reconstructed local response gradients within a predeclared normalized four-dimensional subspace. The primary prospective directional-derivative test gave 24/24 sign agreement in the tested finite synthetic family. This is a local finite-window result, not a full parameter-space gradient, invariant manifold, universal Navier--Stokes separatrix, or regularity/singularity theorem.

B20.6 then moved to prospective finite-distance crossing prediction under a frozen protocol. Its evidential status should be kept separate from the B20.5 local-gradient result; the integrated publication record is the canonical source for the final interpretation.

**Zenodo record:**  
https://zenodo.org/records/22846729


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
BIG-B12 -> cite the B12 Zenodo DOI
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

Planned repository work now focuses on:

* lightweight per-series landing pages for B13--B20,
* representative figures and compact summary data where useful,
* reproducibility links to the corresponding Zenodo archives,
* and continued separation of model-level results from domain-specific interpretation.
