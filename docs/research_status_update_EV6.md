# EV6 — Prospective External Numerical Holdout Status

**Date:** 2026-10-07  
**Status:** CLOSED — published  
**Zenodo DOI:** https://doi.org/10.5281/zenodo.23198141  
**Formal retained verdict:** `EV6_NUMERICAL_HOLDOUT_SUPPORTIVE`

## Scope

EV6 is a prospective external-dataset validation branch in the BIG programme. It tests a frozen response-transfer rule against experimental particle-laden gravity-current front trajectories from the public PALAGRAM repository.

The external dataset is third-party experimental material. The EV6 analysis is not an independent replication by an external investigator.

## Frozen design

Ten particle-volume-fraction conditions from one experimental family were selected. Five were fixed for calibration and five interleaved conditions were held out.

Primary observable:

```text
X = x_front / L0
5 <= tau <= 30
```

Frozen rule: piecewise-linear interpolation of the full trajectory in `log(phi)`.

Frozen comparator: nearest calibration trajectory in `log(phi)`.

## Integrity history

EV6 v1.0 was blocked before outcome exposure after an administrative run-ID / phi mapping error was detected.

At the v1.0 block:

```text
evaluator executions = 0
selected x_front trajectories opened = 0
NRMSE calculated = 0
Gates A-E graded = 0
result plots inspected = 0
```

EV6 v1.1 corrected only the run-ID / phi mapping and was refrozen before outcome opening. The scientific protocol, evaluator, thresholds, no-tuning rule, and claim boundary were unchanged.

The v1.0 blocked record is retained and is not retroactively regraded.

## Frozen v1.1 result

| Gate | Result | Status |
|---|---:|---|
| A — holdout evaluable | 5/5 | PASS |
| B — median NRMSE <= 0.10 | 0.036538 | PASS |
| C — NRMSE <= 0.15 | 5/5 | PASS |
| D — aggregate RMSE improvement >= 20% | 32.55% | PASS |
| E — beats nearest baseline | 5/5 | PASS |

Formal verdict:

```text
EV6_NUMERICAL_HOLDOUT_SUPPORTIVE
```

## Interpretation

EV6 supports prospective quantitative trajectory transfer by the frozen rule across the tested unseen particle-volume-fraction conditions within the selected experimental family.

It does not establish:

- a unique BIG-specific physical mechanism;
- superiority to established gravity-current theory;
- a universal BIG quantitative law;
- extrapolation beyond the tested experimental family;
- prospective discovery of qualitative literature trends;
- independent replication by an external investigator.

## Records

EV6 paper entry: [../papers/EV6_external_numerical_holdout/README.md](../papers/EV6_external_numerical_holdout/README.md)

EV6 Zenodo: https://doi.org/10.5281/zenodo.23198141

External PALAGRAM source: https://doi.org/10.5281/zenodo.10854247
