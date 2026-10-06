# BIG-EV6 — Prospective External Numerical Holdout Validation

**Preprint title:** *Prospective External Numerical Holdout Validation of a Frozen Boundary-Response Transfer Rule*  
**Subtitle:** *Particle-laden gravity-current front trajectories across unseen particle-volume-fraction conditions*  
**Author:** Jun Lucis  
**Zenodo DOI:** https://doi.org/10.5281/zenodo.23198141  
**Status:** published, v1.2

The English manuscript is the authoritative version. The same Zenodo record also includes a Japanese reference translation and a compact reproducibility/audit package.

## Purpose

EV6 tests whether a frozen response-transfer rule can quantitatively transfer experimental particle-laden gravity-current front trajectories to unseen particle-volume-fraction conditions in the public PALAGRAM dataset.

The selected subgroup contains ten conditions from one experimental family. Five conditions were fixed for calibration and five interleaved conditions were held out. The primary observable is the dimensionless front trajectory

```text
X = x_front / L0
5 <= tau <= 30
```

The frozen predictor is piecewise-linear interpolation of the full trajectory in `log(phi)`. The preregistered comparator is the nearest calibration trajectory in `log(phi)`.

## Pre-outcome integrity history

EV6 v1.0 was blocked before outcome exposure because the integrity check detected an administrative run-ID / phi mapping error.

At the block:

- evaluator executions: 0;
- selected `x_front` trajectories opened: 0;
- NRMSE values calculated: 0;
- Gates A–E graded: 0;
- result plots inspected: 0.

EV6 v1.1 corrected only the run-ID / phi association and preserved the scientific design, evaluator, thresholds, no-tuning rule, and claim boundary unchanged. The v1.0 blocked record is retained and is not retroactively regraded.

## Formal result

After the v1.1 integrity checks passed, the unchanged evaluator was executed once.

```text
EV6_NUMERICAL_HOLDOUT_SUPPORTIVE
```

Frozen evaluation results:

| Gate | Frozen criterion | Result | Status |
|---|---|---:|---|
| A | holdout evaluable | 5/5 | PASS |
| B | median NRMSE <= 0.10 | 0.036538 | PASS |
| C | NRMSE <= 0.15 | 5/5 | PASS |
| D | aggregate RMSE improvement >= 20% | 32.55% | PASS |
| E | beats nearest-condition baseline | 5/5 | PASS |

## Claim boundary

Supported:

> The preregistered response-transfer rule achieved prospective quantitative trajectory transfer across the tested unseen particle-volume-fraction conditions within the selected experimental family.

Not established:

- a unique BIG-specific physical mechanism;
- superiority to established gravity-current theory;
- extrapolation to arbitrary apparatus, particles, slopes, laboratories, or observables;
- prospective discovery of the qualitative particle-volume-fraction dependence;
- independent replication by an external investigator.

The external source data are third-party experimental data; the EV6 analysis itself is part of the BIG research programme.

## External source

PALAGRAM public repository, version 1.0.0:

https://doi.org/10.5281/zenodo.10854247

The EV6 source audit records the numerical-sealing status and the noncritical metadata caveat separately.

## Citation

```text
Lucis, J. Prospective External Numerical Holdout Validation of a Frozen
Boundary-Response Transfer Rule. Boundary Information Geometry (BIG-EV6), 2026.
DOI: 10.5281/zenodo.23198141.
```

Zenodo: https://doi.org/10.5281/zenodo.23198141

The Zenodo record is the canonical academic citation for EV6. GitHub serves as the navigational overview of the continuing BIG research programme.
