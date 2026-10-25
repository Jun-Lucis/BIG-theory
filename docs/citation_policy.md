# BIG Citation Policy


## Current programme-wide entry: the 2026 flagship

For a recent **programme-wide synthesis**, cite: **Jun Lucis (2026), *Boundary Information Geometry: Distinct Model Families, Preserved Failures, and a Path toward Physical Measurement*, Preprint v1.0, [DOI: 10.5281/zenodo.23486616](https://doi.org/10.5281/zenodo.23486616)**. It includes English main, Japanese reference and English technical appendix.

This is not a substitute for model-level references. **Specific equations, parameters, numerical values, formal PASS/FAIL/INCONCLUSIVE, code corrections, and predeclared protocols require the source publication and its version-specific DOI.** The GitHub repository itself remains a living reference index and can be cited separately. The new synthesis does **not** establish a universal BIG physics law or independent physical validation.


## Standalone post-B42 fluid-history study (2026-10-25)

For the numerical and analytical findings of **BIG Fluid History R0–R4.5**, including the predeclared R4.4/R4.5 comparator results, preserved failures, and limitations, cite:

> Lucis, J. (2026). *Boundary History and Observability in Classical Fluid Dynamics: Prospective Numerical Tests, Classical Comparators, and Predictive Limits*. Preprint v1.0, Zenodo. [DOI: 10.5281/zenodo.23635004](https://doi.org/10.5281/zenodo.23635004).

The [all-version DOI](https://doi.org/10.5281/zenodo.23635003) tracks future record versions; use the version-specific DOI for exact reproduced quantities. [GitHub paper navigation](../papers/Fluid_History_classical_NS/README.md). This is a classical Navier–Stokes study and does not establish BIG-specific additional physics or supersede B42 or the programme-level flagship.

This page explains how to cite **Boundary Information Geometry (BIG)** at the appropriate evidential level.

The repository contains a research programme rather than one single paper. A citation should therefore match the claim being made.

The basic rule is:

```text
repository / documentation claim
    -> cite the GitHub repository

programme-level synthesis
    -> cite the relevant status record

specific numerical or structural result
    -> cite the corresponding B-series Zenodo paper
```

Do not use a broad repository citation as a substitute for the paper that actually supports a specific numerical result.

---

## 1. Citing the repository as a whole

Use the repository citation when referring to:

- BIG as a research programme;
- repository organization;
- the living documentation;
- the current integrated status map;
- code / documentation provenance at repository level.

Recommended form:

```text
Lucis, J. Boundary Information Geometry (BIG). GitHub repository.
https://github.com/Jun-Lucis/BIG-theory
```

For an exact reproducible repository state, also record the Git commit SHA.

The machine-readable repository citation is stored in [../CITATION.cff](../CITATION.cff).

---

## 2. Citing programme-level synthesis

Use a programme-level status record when discussing the evidential state of BIG across multiple B-series.

### Historical programme status through B23

**DOI:** https://doi.org/10.5281/zenodo.22939024

This is the archived programme-level status snapshot through B23. It should not be treated as if it already contained the later B23A or B24–B26 results.

### B23A structural-universality audit

**DOI:** https://doi.org/10.5281/zenodo.22994445

Use this record when discussing the prospective P1–P6 universality audit, including the distinction between structural/formal and quantitative universality.

### B24–B25 Phase I

**DOI:** https://doi.org/10.5281/zenodo.22956894

Use this record for the cross-sector audit and the first prospectively successful level-resolved transfer construction.

### B25 Phase II

**DOI:** https://doi.org/10.5281/zenodo.22967474

Use this record for the reduction to a family-restricted fixed perimeter coefficient.

### B26

**DOI:** https://doi.org/10.5281/zenodo.22972985

Use this record for the topology-localized two-center transfer test and the terminal fixed-coefficient geometry-transfer failure.

The baseline living synthesis across B3–B26 plus B23A is maintained in:

- [research_status_map_B3_B26.md](research_status_map_B3_B26.md)
- [research_status_map_B3_B26_ja.md](research_status_map_B3_B26_ja.md)

The later B27–B36 status is maintained in:

- [research_status_update_B27_B36.md](research_status_update_B27_B36.md)
- [research_status_update_B27_B36_ja.md](research_status_update_B27_B36_ja.md)

Because these are living GitHub documents, cite the repository and commit SHA if the exact current wording matters.

---

## 3. Citing a specific numerical or structural claim

For a claim tied to one B-series experiment, cite the **specific Zenodo paper / record that reports that result**.

Examples:

- a core B9 fission-like metastability claim -> cite the primary B9 record;
- a B9 empirical Phase II claim about the metastability scale hierarchy, RIPL structural placement, or retained external/near-spinodal limits -> cite DOI https://doi.org/10.5281/zenodo.23128738;
- a B20 response-normal result -> cite the B20 record;
- a B21 local kinematic-closure result -> cite the B21 record;
- a B22 prospective geometry result -> cite the B22 record;
- a B23 cross-branch result -> cite the B23 record;
- a B23A P1–P6 universality-audit claim -> cite the B23A record;
- a B26 fixed-coefficient transfer failure -> cite the B26 record.
- a B27 history-conditioned response / reconfiguration-covariance result -> cite DOI https://doi.org/10.5281/zenodo.23024324;
- a B28 lineage-transport failure or B29 training-domain readability-stop claim -> cite the integrated B28–B29 record, DOI https://doi.org/10.5281/zenodo.23050390;
- a B30–B36 response-to-pulse-timing claim -> cite DOI https://doi.org/10.5281/zenodo.23048197.

The canonical DOI list is maintained in [publication_map.md](publication_map.md).

If a claim depends on a negative, inconclusive, implementation-invalid, or resolution-sensitive outcome, cite the record that preserves that outcome rather than replacing it with a later positive result.

---

## 4. Citation hierarchy for mixed claims

When one paragraph combines an overall BIG interpretation with a specific numerical result, use both levels.

Example structure:

```text
Programme-level interpretation:
cite the relevant BIG status record.

Specific numerical statement:
cite the exact B-series paper that produced the number.
```

This avoids two opposite errors:

1. using a broad status document as if it were the primary source for every number;
2. using one successful B-series paper as evidence for a programme-wide universal claim.

---

## 5. Current citation boundary

The present repository distinguishes:

- **structural universality** — recurring organization in terms of boundary, response, history, branch, and reconfiguration;
- **formal universality** — comparable mathematical objects across systems;
- **quantitative universality** — transfer of the same numerical predictor, coefficient, reset amplitude, or rate law across systems.

The current evidence supports formal / structural comparability as a programme-level organizing statement. It does **not** establish one universal numerical BIG law.

Citations should preserve that distinction.

---

## 6. Author and repository

**Author:** Jun Lucis  
**Repository:** https://github.com/Jun-Lucis/BIG-theory

For individual paper titles, versions, files, and DOI records, use [publication_map.md](publication_map.md).
