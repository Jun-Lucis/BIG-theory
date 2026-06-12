# Zenodo Records

This page lists the main Zenodo records associated with the Boundary Information Geometry (BIG) numerical series.

GitHub is used as the project map and entry point.
Zenodo is used for archival storage, DOI assignment, citation, and preservation of numerical packages.

---

## Current main record

### BIG-B8: Boundary Anisotropy and Finite-Time Separatrix Thresholds

* Record: `20645317`
* DOI: `10.5281/zenodo.20645317`
* URL: `https://zenodo.org/records/20645317`
* Status: current B8 package
* Topic: finite-time separatrix thresholds controlled by boundary anisotropy
* Main result: boundary anisotropy shifts the finite-time runaway threshold in a degenerate mixed-gradient dissipative field
* Important caution: thresholds are finite-time thresholds at `T = 0.4`, not asymptotic stability thresholds

Recommended citation description:

> Numerical evidence for boundary-anisotropy-controlled finite-time separatrix thresholds in a degenerate mixed-gradient dissipative field.

Recommended short label:

```text
BIG-B8: Boundary anisotropy and finite-time separatrix thresholds
```

---

## Related previous record

### BIG-B7: Critical transition and runaway onset

* DOI: `10.5281/zenodo.20603601`
* Topic: critical transition, runaway onset, and persistence of local boundary regularity
* Relation to B8: B7 identifies the transition regime; B8 develops finite-amplitude threshold and boundary-anisotropy analysis

Recommended short label:

```text
BIG-B7: Critical mobility and runaway transition
```

---

## Conceptual sequence

The current BIG numerical sequence can be read as follows.

| Stage | Main focus                  | Role                                                  |
| ----- | --------------------------- | ----------------------------------------------------- |
| B3    | quadratic boundary landing  | discovery of smooth compact-support boundary behavior |
| B4    | universality and state maps | parameter scans and boundary-layer classification     |
| B7    | critical transition         | local boundary regularity near global runaway         |
| B8    | finite-amplitude separatrix | survival/runaway threshold detection                  |
| B8.8  | anisotropic separatrix      | boundary geometry controls finite-time threshold      |
| B8.8d | resolution validation       | N=120 confirmation of monotone geometry dependence    |

---

## Recommended wording for GitHub

The following wording is recommended when referencing the B8 Zenodo record from the README or documentation pages:

> The B8 numerical package is archived on Zenodo. It provides finite-time numerical evidence that boundary anisotropy controls separatrix thresholds in a degenerate mixed-gradient dissipative field. The absolute threshold values are resolution-dependent, but the monotone ordering with respect to ellipse ratio `b/a` remains robust under N=96 to N=120 validation.

---

## Recommended wording for technical citation

A more technical citation description:

> This record contains numerical data, figures, and summaries for the BIG-B8 series. The dataset studies compact elliptical initial conditions in a degenerate mixed-gradient dissipative field and identifies finite-time amplitude thresholds separating survival from runaway up to observation time `T = 0.4`. The results show a monotone dependence of the critical amplitude on ellipse ratio `b/a`, with a three-point N=120 validation confirming the structural ordering observed at N=96.

---

## Important caution

The BIG-B8 results should be interpreted carefully.

* The reported values of `A_c` are finite-time thresholds.
* The observation time is `T = 0.4`.
* The thresholds are not infinite-time stability thresholds.
* The absolute values of `A_c` depend on numerical resolution.
* The N=120 validation confirms the monotone ordering for three representative ratios, not a full high-resolution scan.
* The model is an exploratory nonlinear dissipative field model.

---

## Data policy

Heavy numerical fields and large ZIP packages should be stored on Zenodo rather than directly in this GitHub repository.

GitHub should contain:

* overview documents,
* selected figures,
* lightweight summaries,
* links to Zenodo records,
* reproduction notes,
* citation metadata.

Zenodo should contain:

* ZIP packages,
* CSV summaries,
* figures,
* numerical outputs,
* README files,
* metadata files.

---

## To be added later

Additional records may be added here as the BIG series is reorganized.

Suggested future entries:

```text
B3.1: Quadratic boundary-layer discovery
B4.1: Universality scan
B4.3: State map
B5: Boundary anisotropy diagnostics
B7: Critical transition
B8: Finite-time separatrix
```

---

## Citation note

When citing BIG numerical results, prefer the most specific record that contains the relevant data.

For example:

* cite B7 for critical transition and local boundary regularity,
* cite B8 for boundary-anisotropy-controlled finite-time thresholds,
* cite earlier B3/B4 records for quadratic boundary landing and boundary-layer universality.
