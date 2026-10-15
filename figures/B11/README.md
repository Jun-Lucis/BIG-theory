# BIG-B11 Figures

This directory contains representative figures for **BIG-B11**, the reduced stochastic hidden-depth model for post-capture inheritance versus assimilation.

The figures are intended for visual orientation and documentation. They should be read together with the BIG-B11 paper notes, Zenodo records, and the limitation statements in the main repository.

BIG-B11 is **not** a quantitative theory of biological inheritance, nuclear fusion, reproduction, or real energy release. The terms “parent,” “inheritance,” and “fusion” are used structurally within a reduced hidden-state model.

---

## Core B11 idea

B11 asks what happens after capture:

```text
post-capture state
    -> parent assimilation
    OR
    -> hidden-depth inheritance
```

The hidden-depth state is written schematically as

$$
h=(h_A,h_B),
$$

where the two sectors represent parent-like memory components in a reduced model.

---

## Representative figures

### Figure 1: Hidden-depth model schematic

![Hidden-depth model schematic](figure_01_hidden_depth_model_schematic.png)

**Figure:** Conceptual structure of the B11 hidden-depth model. A post-capture hidden-depth state may fall into parent assimilation or into non-assimilative inheritance if hidden-depth coupling is strong enough.

---

### Figure 2: Critical inheritance threshold at P = 0.5

![Critical inheritance threshold at P = 0.5](figure_02_critical_inheritance_threshold_P05.png)

**Figure:** Critical inheritance coupling for reaching approximately 50% inheritance probability. Parent similarity lowers the coupling needed for non-assimilative inheritance.

---

### Figure 3: Critical inheritance threshold at P = 0.9

![Critical inheritance threshold at P = 0.9](figure_03_critical_inheritance_threshold_P09.png)

**Figure:** Critical inheritance coupling for robust inheritance probability. Stronger post-fusion noise raises the threshold for stable inheritance, especially under stricter probability criteria.

---

### Figure 4: Threshold heatmap at P = 0.5

![Threshold heatmap at P = 0.5](figure_04_threshold_heatmap_P05.png)

**Figure:** Heatmap of the estimated inheritance threshold for the 50% inheritance criterion across parent similarity and noise settings.

---

### Figure 5: Threshold heatmap at P = 0.9

![Threshold heatmap at P = 0.9](figure_05_threshold_heatmap_P09.png)

**Figure:** Heatmap of the estimated inheritance threshold for the 90% inheritance criterion. The stricter inheritance requirement makes the stabilizing coupling threshold more demanding.

---

### Figure 6: Reorganization energy drop near threshold

![Reorganization energy drop near threshold](figure_06_reorganization_energy_drop_threshold.png)

**Figure:** Model-defined reorganization energy drop averaged over all endpoints at the sampled coupling whose observed inheritance fraction is closest to 0.5. It is neither an interpolated-threshold value nor an inheritance-only mean.

---

### Figure 7: Folding-conflict drop near threshold

![Folding-conflict drop near threshold](figure_07_folding_conflict_drop_threshold.png)

**Figure:** Model-defined folding-conflict drop at the same selected sampled coupling, averaged over all outcomes. The explicit conflict coefficient contains (1-rho).

---

## Structural interpretation

The main B11 mechanism can be summarized as:

```text
weak inheritance coupling
    -> A-assimilation or B-assimilation dominates

stronger inheritance coupling
    -> more endpoints receive the inheritance label at the finite horizon

higher post-fusion noise
    -> robust inheritance requires stronger stabilization
```

B11 formalizes the BIG idea that fusion-like capture need not imply homogeneous assimilation.

---

## Important caution

The figures in this directory should not be presented as biological inheritance or physical fusion plots.

In particular:

- hidden-depth variables are abstract memory modes, not measured physical variables;
- parent-like sectors are not genes;
- inheritance coupling is a model parameter, not a biological mechanism;
- model-defined energy decreases are not real thermodynamic or nuclear energy release;
- the result is a reduced stochastic phase-competition model.

---

## Recommended wording

Preferred wording:

```text
hidden-depth inheritance in a reduced model
```

```text
non-assimilative post-capture stabilization
```

```text
assimilation versus inheritance phase competition
```

Avoid unqualified wording such as:

```text
B11 explains biological inheritance
```

```text
B11 predicts reproduction
```

```text
B11 proves real energy release
```

---

## Archived-figure audit - 15 October 2026

All seven representative PNGs match the original archive files. Five appear in the original PDF; two are archive heatmaps. No scientific figure was regenerated. [Audit and publication status](../../docs/B11_publication_audit_2026_10_15.md).

The audit supplement is published as [Zenodo Version 1.2](https://doi.org/10.5281/zenodo.23388916), with one complete file: BIG_B11_Archive_Audit_Supplement_v1_1.zip (32,259,200 bytes). A fresh public download is byte-identical to the saved archive; CRC and all 46 internal SHA-256 entries pass. The archive contains the unchanged original five-page v1.0 PDF, all 20 original package files, the original ZIP, 14 recovered data files, methods/scope notes and the arithmetic-only verifier. No split-file assembly is needed. The internal supplement name remains v1.1; the Zenodo release is 1.2. Version 1.1 (23387434) omitted the supplement, and its public description was corrected to disclose that omission. Complete historical solver and ordered-classifier authentication remain open.

## Relation to Zenodo

Current published BIG-B11 record (Version 1.2; one complete archive):

```text
https://doi.org/10.5281/zenodo.23388916
```

Full-resolution figures, CSV summaries, parameter files, source notes, and reproducibility packages should remain archived on Zenodo. GitHub figures are for quick browsing and documentation.

---

## File list

Expected files in this directory:

```text
figures/B11/
├── README.md
├── figure_01_hidden_depth_model_schematic.png
├── figure_02_critical_inheritance_threshold_P05.png
├── figure_03_critical_inheritance_threshold_P09.png
├── figure_04_threshold_heatmap_P05.png
├── figure_05_threshold_heatmap_P09.png
├── figure_06_reorganization_energy_drop_threshold.png
└── figure_07_folding_conflict_drop_threshold.png
```
