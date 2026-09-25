# BIG Research Status Update — B24-B25 Phase I

**Date:** 2026-09-25  
**Primary DOI:** https://doi.org/10.5281/zenodo.22956894

This note updates the earlier B3-B23 research-status map. It does not replace or rewrite the frozen verdicts from earlier stages.

## 1. What B24 changed

B24 asked whether the existing BIG sectors already shared one substantive common mathematical operator.

Under a source-audited frozen mapping protocol, the answer was not established. Broad boundary vocabulary recurred, but no required cross-sector exact/coordinate-equivalent substantive recurrence was found.

**B24.2 verdict:** `MULTIPLE_BOUNDARY_CLASSES_INDICATED`.

The correct interpretation is not that earlier BIG results are invalid. It is that the programme had accumulated several mathematically distinct boundary classes.

## 2. What B25 changed

B25 changed the unification question.

Instead of requiring the same native operator in every sector, it asks whether sector-specific objects can be connected by a typed transfer:

$$
X \to \Sigma \to J \to (X',H') \to F \to \mathcal B_R.
$$

The first A-to-B constant-density reduction failed:

**B25.1 verdict:** `AB_CONSTANT_DENSITY_FAIL`.

A retrospective coarea decomposition then motivated a new level-resolved transfer relation. That relation was frozen before new trajectories and tested on nine new shape/resolution combinations.

**B25.1b verdict:** `AB_LEVEL_RESOLVED_BRIDGE_PASS`.

Primary metrics:

```text
9/9 cases valid
maximum relative error:      17.76%
median relative error:        9.49%
old comparator median:       29.79%
median-error improvement:     68.15%
fine-resolution stability:    PASS
```

## 3. Current programme-level interpretation

The current evidence does **not** support saying that BIG has one already-established universal mathematical operator.

It now supports a more limited and more testable statement:

> Distinct boundary classes can, in at least one tested canonical setting, be connected by a newly constructed level-resolved transfer functional that survives a predeclared held-out numerical test.

This result is stronger than analogy and weaker than a derivation of one sector from another.

## 4. Preserved verdicts

The following remain unchanged:

- B19: no robust ray-independent upstream scalar / no robust 2D portrait
- B20.6: `INCONCLUSIVE`
- B21: generic kinematic identities are not new laws
- B23 original aggregate: `INCONCLUSIVE`
- B24.1b: `RESOLUTION_STABLE_FAIL`
- B24.1d: `PARAMETER_ROBUST_FAIL`
- B24.2: `MULTIPLE_BOUNDARY_CLASSES_INDICATED`
- B25.1: `AB_CONSTANT_DENSITY_FAIL`
- B25.1R: retrospective diagnostic only
- B25.1b: `AB_LEVEL_RESOLVED_BRIDGE_PASS`

## 5. Next phase

B25 Phase I is closed.

Possible later studies include:

- thin-layer reduction toward an effective $\sigma_{\mathrm{eff}}P$ form;
- transfer of an independently derived A-side boundary term into a new B9-style shape-energy test;
- an independent C-to-D bridge;
- replication under new source families, p values, or external implementations.

None of these is required to preserve the Phase-I result.
