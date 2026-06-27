# BIG Figures

This directory collects representative figures for **Boundary Information Geometry (BIG)**.

The figures in this repository are intended for quick browsing, documentation, and visual orientation. Large raw outputs, full numerical datasets, and complete reproducibility archives should remain on Zenodo.

---

## Organization

Suggested structure:

```text
figures/
├── README.md
├── B9/
│   ├── figure_01_energy_landscape.png
│   ├── figure_02_threshold_scan.png
│   └── figure_03_empirical_structural_comparison.png
├── B10/
│   ├── figure_01_finite_noise_window.png
│   ├── figure_02_first_hit_vs_sustained_capture.png
│   └── figure_03_outcome_map.png
├── B11/
│   ├── figure_01_hidden_depth_landscape.png
│   ├── figure_02_inheritance_threshold.png
│   └── figure_03_outcome_phase_map.png
└── B12/
    ├── figure_01_unified_boundary_dynamics.png
    ├── figure_02_R_lock_window.png
    └── figure_03_full_success_vs_noise.png
```

The exact filenames may be adjusted as the repository is updated.

---

## Recommended naming convention

Use lowercase, descriptive filenames:

```text
figure_01_energy_landscape.png
figure_02_threshold_scan.png
figure_03_structural_comparison.png
```

Avoid vague names such as:

```text
image1.png
final.png
new_plot.png
screenshot.png
```

Recommended format:

```text
figures/B9/figure_01_energy_landscape.png
figures/B10/figure_01_finite_noise_window.png
figures/B11/figure_01_hidden_depth_landscape.png
figures/B12/figure_01_unified_boundary_dynamics.png
```

---

## Figure policy

Figures included in GitHub should be:

* representative rather than exhaustive;
* lightweight enough for browsing;
* directly connected to README files or documentation;
* linked to the corresponding Zenodo record when possible;
* accompanied by a short caption or explanation.

Full raw plotting outputs should be archived on Zenodo rather than committed directly to GitHub.

---

## Suggested figure sets by series

### B9

Recommended figures:

1. B9 energy landscape
2. Threshold or lambda scan
3. Empirical structural comparison with representative actinides
4. Two-disk or separated-branch schematic

### B10

Recommended figures:

1. Finite-noise sustained-capture window
2. First hit versus sustained capture
3. Outcome classification map
4. Representative trajectory

### B11

Recommended figures:

1. Hidden-depth landscape
2. Assimilation versus inheritance phase map
3. Inheritance threshold as a function of coupling or similarity
4. Representative post-capture trajectories

### B12

Recommended figures:

1. Unified boundary dynamics schematic
2. Finite-noise R-lock window
3. Full success versus noise
4. Lock / inheritance / assimilation outcome comparison
5. Representative low-noise, peak-noise, and high-noise traces

---

## Captions

Each figure should ideally have a caption in the corresponding paper-folder README.

Example:

```markdown
![B12 finite-noise R-lock window](../../figures/B12/figure_02_R_lock_window.png)

**Figure:** Finite-noise R-lock window in the reduced B12 model. Intermediate resonance noise enables sustained R-lock and hidden-depth inheritance, while low noise fails to ignite the R-sector and high noise disrupts strict locking.
```

---

## Relation to Zenodo

GitHub figures are for orientation and documentation.

Zenodo should remain the primary archive for:

* full-resolution figure sets,
* raw CSV data,
* simulation logs,
* plotting scripts,
* reproducibility packages,
* and versioned publication PDFs.

Whenever possible, each figure used in GitHub should correspond to a Zenodo record or reproducibility package.
