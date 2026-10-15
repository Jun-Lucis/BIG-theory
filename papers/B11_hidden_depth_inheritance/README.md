# BIG-B11: Hidden-Depth Inheritance and Non-Assimilative Post-Capture Stabilization

**BIG-B11** studies what happens after capture in a reduced hidden-depth model.

This folder is the main explanatory entry point for BIG-B11.

Representative figures are stored in:

```text
../../figures/B11/
```

---

## Core idea

BIG-B11 asks:

> After capture, does the fused state collapse into one parent-like attractor, or can it preserve multiple parent-like memories without total assimilation?

This follows directly from the BIG principle of non-assimilation.

B10 asks whether sustained capture can occur.
B11 asks what kind of state exists after capture.

```text
B10: approach -> activation -> sustained capture
B11: post-capture state -> assimilation or hidden-depth inheritance
```

---

## Hidden-depth state

B11 introduces a hidden-depth state,

$$
h=(h_A,h_B),
$$

where:

* (h_A) represents memory or attraction toward parent-like state A,
* (h_B) represents memory or attraction toward parent-like state B.

The word “memory” is used in a reduced-model sense.

It does not mean biological memory, genetic inheritance, nuclear structure, or physical material memory unless a domain-specific model is added.

---

## Representative figure

![BIG-B11 hidden-depth model schematic](../../figures/B11/figure_01_hidden_depth_model_schematic.png)

**Figure:** Conceptual structure of the B11 hidden-depth model. A post-capture hidden-depth state may fall into parent assimilation or into non-assimilative inheritance if hidden-depth coupling is strong enough.

More figures are available here:

[../../figures/B11](../../figures/B11)

---

## Assimilation versus inheritance

In B11, the post-capture state can fall into different outcome classes:

```text
A-assimilation
B-assimilation
two-parent hidden-depth inheritance
annihilation-like collapse
emergent or mixed states
```

The central distinction is:

```text
assimilation
    -> collapse toward one dominant parent-like attractor

hidden-depth inheritance
    -> retention of multiple parent-like memories
```

This is the non-assimilative core of B11.

The model asks whether capture must destroy distinction, or whether a post-capture state can retain distinguishable hidden-depth structure.

---

## Main result

The main B11 result is a transition between assimilation-dominated and inheritance-dominated finite-time outcome frequencies in the archived post-capture scans.

Qualitatively:

```text
weak inheritance coupling
    -> post-capture state tends to collapse into A or B assimilation

stronger inheritance coupling
    -> more endpoints are classified as inheritance at the finite observation horizon

higher noise
    -> robust inheritance generally requires stronger stabilization
```

Parent similarity also affects the inheritance threshold.

When the two parent-like states are more compatible, hidden-depth inheritance can become easier to stabilize.

These are reduced-model results, not universal constants.

---

## Additional representative figures

### Critical inheritance threshold at P = 0.5

![Critical inheritance threshold at P = 0.5](../../figures/B11/figure_02_critical_inheritance_threshold_P05.png)

**Figure:** Critical inheritance coupling for reaching approximately 50% inheritance probability.

---

### Critical inheritance threshold at P = 0.9

![Critical inheritance threshold at P = 0.9](../../figures/B11/figure_03_critical_inheritance_threshold_P09.png)

**Figure:** Critical inheritance coupling for robust inheritance probability.

---

### Threshold heatmap at P = 0.5

![Threshold heatmap at P = 0.5](../../figures/B11/figure_04_threshold_heatmap_P05.png)

**Figure:** Heatmap of the estimated inheritance threshold for the 50% inheritance criterion.

---

### Threshold heatmap at P = 0.9

![Threshold heatmap at P = 0.9](../../figures/B11/figure_05_threshold_heatmap_P09.png)

**Figure:** Heatmap of the estimated inheritance threshold for the 90% inheritance criterion.

---

### Reorganization energy drop

![Reorganization energy drop near threshold](../../figures/B11/figure_06_reorganization_energy_drop_threshold.png)

**Figure:** Model-defined reorganization energy drop over all endpoints at the sampled coupling whose observed inheritance fraction is closest to 0.5. It is not interpolated at the threshold or conditioned on inheritance-only endpoints, and it is not real thermodynamic or nuclear energy release.

---

### Folding-conflict drop

![Folding-conflict drop near threshold](../../figures/B11/figure_07_folding_conflict_drop_threshold.png)

**Figure:** Model-defined folding-conflict drop at the same nearest-half sampled coupling, averaged over all outcomes in the constructed landscape.

---

## Interpretation

B11 adds a key layer to BIG:

> Fusion-like capture does not necessarily imply total assimilation.

A capture event may lead to:

1. **Assimilation**
   The fused state collapses into one parent-like identity.

2. **Annihilation-like loss**
   The previous structures fail to produce a stable inherited state.

3. **Hidden-depth inheritance**
   The fused state preserves distinguishable contributions from more than one parent-like source.

In this sense, B11 explores whether post-capture transformation can preserve difference.

This is important for BIG because non-assimilation is not only a pre-capture boundary condition.
It may also be a post-capture stabilization principle.

---

## Relation to B10

B10 studies the conditions for sustained capture.

B11 starts after capture and asks what survives.

```text
B10:
    Can two boundary-supported systems enter sustained capture?

B11:
    After capture, does the resulting state assimilate, collapse, or inherit?
```

This distinction is essential.

A successful B10 capture event does not automatically imply B11 inheritance.

---

## Important limitations

BIG-B11 is **not** a quantitative theory of biological inheritance.

It is also **not** a quantitative theory of:

* nuclear fusion,
* nuclear energy release,
* genetic recombination,
* embryology,
* thermodynamic energy production,
* material memory,
* or biological reproduction.

The terms “inheritance,” “parent,” “fusion,” and “memory” are used structurally within a reduced hidden-state model.

In particular:

* (h_A) and (h_B) are reduced hidden-depth variables, not genes;
* inheritance coupling is a model parameter, not a biological mechanism;
* model-defined energy decreases are not real thermodynamic or nuclear energy release;
* post-capture stabilization is a mathematical outcome class, not a claim about physical reproduction.

B11 should therefore be read as a reduced model of non-assimilative memory retention after capture.

---

## Relation to the BIG programme

Within BIG, B11 plays the role of the **post-capture inheritance branch**.

It connects naturally to:

```text
B9  -> separation / fission-like metastability
B10 -> finite-noise capture / fusion-like locking
B11 -> post-capture inheritance versus assimilation
B12 -> unified boundary dynamics
```

B11 moves the programme from:

```text
Can capture occur?
```

to:

```text
What kind of identity survives after capture?
```

---

## Recommended wording

Preferred:

> BIG-B11 studies hidden-depth inheritance versus assimilation in a reduced post-capture model.

Preferred:

> B11 provides a model-level framework for non-assimilative memory retention after capture.

Preferred:

> B11 distinguishes capture from inheritance.

Avoid unless carefully qualified:

> BIG-B11 explains biological inheritance.

> BIG-B11 proves fusion produces inheritance.

> BIG-B11 predicts real energy release.

> B11 is a theory of genetics.

---

## Archived-output audit - 15 October 2026

All 201,350 saved endpoint rows, 1,495 grid summaries and 30 interpolated thresholds were checked across B11.1, B11.2 and B11.2b. Twenty-eight consistency groups reproduce archived arithmetic. The original PDF and 20-file package are preserved; no stochastic simulator was rerun or research result regraded.

Thresholds are finite-grid interpolants of finite-time terminal fractions. The inheritance well and similarity-dependent conflict penalty are explicit model choices. Complete historical solver and ordered-classifier authentication remain open.

The documentation/data supplement v1.1 is prepared and verified. Its Zenodo draft description and version were saved, but file-upload finalization could not be verified after the browser timed out. No publish action was performed. Reserved DOI 10.5281/zenodo.23387434 is not a published release; the current published record remains 10.5281/zenodo.20828439.

[Audit evidence and publication status](../../docs/B11_publication_audit_2026_10_15.md)  
[Methods and interpretation](../../docs/B11_methods_and_scope_2026_10_15.md)

## Zenodo record

Primary BIG-B11 record:

https://doi.org/10.5281/zenodo.20828439
