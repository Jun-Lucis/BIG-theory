# BIG-B12 Figures

This directory contains representative figures for **BIG-B12**, the unified reduced boundary-dynamical model connecting boundary approach, finite-noise R-lock, and hidden-depth inheritance.

The figures are intended for visual orientation and documentation. They should be read together with the BIG-B12 paper notes, Zenodo records, and the limitation statements in the main repository.

BIG-B12 is **not** a completed physical unification theory and is not a quantitative model of nuclear fusion, biological inheritance, or real energy release. It is a reduced variational-stochastic model.

---

## Core B12 idea

B12 connects the earlier B-series motifs:

```text
B9  -> boundary-energy competition and fission-like separation
B10 -> stochastic-resonance-like finite-noise capture
B11 -> post-capture hidden-depth inheritance
```

The central B12 sequence is:

```text
boundary approach
    -> noise-assisted R-lock
    -> hidden-depth inheritance
```

A strict success event requires both sustained lock and inherited hidden-depth structure:

```text
full success = strict R-lock AND hidden-depth inheritance
```

---

## Representative figures

### Figure 1: Unified boundary architecture

![Unified boundary architecture](figure_01_unified_boundary_architecture.png)

**Figure:** Conceptual architecture of the reduced BIG-B12 system. Boundary proximity activates the resonance sector; sustained R-lock opens an effective inheritance channel; hidden-depth dynamics then select assimilation or inheritance.

---

### Figure 2: Finite-noise R-lock window

![Finite-noise R-lock window](figure_02_finite_noise_R_lock_window.png)

**Figure:** B12.1d-refined finite-noise window. Low noise fails to ignite the resonance sector; intermediate noise produces sustained R-lock and full success; higher noise retains boundary approach but progressively disrupts sustained locking.

---

### Figure 3: Full success versus resonance noise

![Full success versus resonance noise](figure_03_full_success_vs_noise.png)

**Figure:** Approximate full-success probability across resonance-noise values in the B12.1d refined scan. Full success is stricter than final-state similarity because it requires strict R-lock together with hidden-depth inheritance.

---

### Figure 4: Hit, lock, and full success comparison

![Hit, lock, and full success comparison](figure_04_hit_lock_full_success_comparison.png)

**Figure:** Comparison of approximate hit, lock, and full-success probabilities across resonance-noise values. The distinction among hit, lock, and full success prevents overcounting trajectories that approach or transiently resemble inheritance without satisfying the sustained-lock criterion.

---

### Figure 5: Refined window metrics summary

![Refined window metrics summary](figure_05_refined_window_metrics_summary.png)

**Figure:** Summary of reported B12.1d refined finite-noise window metrics, including peak lock, peak full success, FWHM, trajectories per noise value, and total raw rows recorded.

---

## Structural interpretation

The main B12 mechanism can be summarized as:

```text
low noise
    -> R-sector does not cross the ignition barrier
    -> no strict R-lock

intermediate noise
    -> fluctuations help ignite R
    -> sustained R-lock and hidden-depth inheritance become likely

high noise
    -> boundary approach may still occur
    -> coherent sustained locking is disrupted
```

The key distinction is:

```text
P_hit != P_lock != P_full_success
```

---

## Representative refined scan values

In the B12.1d refined d2 scan:

```text
sigma_R at peak lock:      approximately 0.070
P_lock at peak:            approximately 0.861
P_full_success at peak:    approximately 0.856
total raw rows recorded:   5940
```

These are model-level numerical values, not universal constants.

---

## Important caution

The figures in this directory should not be presented as quantitative physical predictions.

In particular:

- d(t) is a reduced boundary-distance/proximity variable;
- R(t) is a reduced resonance sector, not a calibrated physical or nuclear mode;
- h(t) is a hidden-depth inheritance state, not biological genetics;
- full success is a model-defined event criterion;
- the numerical thresholds depend on the selected model, parameters, noise grid, and event definitions;
- no real fusion energy release or biological inheritance mechanism is claimed.

---

## Recommended wording

Preferred wording:

```text
finite-noise R-lock window in a reduced B12 model
```

```text
boundary approach -> R-lock -> hidden-depth inheritance
```

```text
full success requires strict R-lock and hidden-depth inheritance
```

Avoid unqualified wording such as:

```text
B12 explains nuclear fusion
```

```text
B12 proves biological inheritance
```

```text
B12 is a physical unification theory
```

---

## Relation to Zenodo

Primary BIG-B12 record:

```text
DOI to be added
```

Related records:

```text
BIG-B9:  https://doi.org/10.5281/zenodo.20799131
BIG-B10: https://doi.org/10.5281/zenodo.20819427
BIG-B11: https://doi.org/10.5281/zenodo.20828439
```

Full-resolution figures, CSV summaries, run logs, source files, and reproducibility packages should remain archived on Zenodo. GitHub figures are for quick browsing and documentation.

---

## File list

Expected files in this directory:

```text
figures/B12/
├── README.md
├── figure_01_unified_boundary_architecture.png
├── figure_02_finite_noise_R_lock_window.png
├── figure_03_full_success_vs_noise.png
├── figure_04_hit_lock_full_success_comparison.png
└── figure_05_refined_window_metrics_summary.png
```
