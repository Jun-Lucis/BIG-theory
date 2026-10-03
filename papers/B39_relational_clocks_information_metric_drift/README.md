# BIG-B39 — Relational Clocks, Information-Metric Drift, and Clock Reparameterization

**Preprint title:** *Relational Clocks, Information-Metric Drift, and Clock Reparameterization in a Finite Boundary-Response Model*  
**Author:** Jun Lucis  
**Zenodo DOI:** https://doi.org/10.5281/zenodo.23113994  
**Status:** B39.3-P2 complete; v1.0 Zenodo package prepared

The English manuscript is the authoritative version. A Japanese reference translation and a supplementary reproducibility package are prepared for the same Zenodo record.

---

## Why B39 matters

B38 showed that the measured source/receiver timing asymmetry depends strongly on operator, source, receiver, and readout relation. B39 asks a different question:

> Which temporal structures remain when the same response history is re-expressed through relational or reparameterized clocks?

The programme therefore separates three issues:

1. whether a target-excluded relational clock changes the residual timing relation;
2. whether directed order is better represented by scalar entropy or by information-metric structure;
3. whether path-based temporal quantities remain stable under a prospectively nontrivial integration-level clock reparameterization.

B39 does **not** claim that physical time has emerged from boundary relations.

---

## Retained sequence

| Stage | Formal status | Main role |
| --- | --- | --- |
| B39.1-P0 | non-claim-bearing calibration | Constructed a target-excluded relational path clock from symmetric response relations. |
| B39.1-P1 | `RELATIONAL_CLOCK_WEIGHTED_RESIDUAL_PERSISTENCE_PASS` | The remaining D-weighted timing residual persisted with comparable normalized magnitude and preserved direction in the frozen relational clock. |
| B39.2-P0 | non-claim-bearing information-geometry audit | Scalar Shannon entropy was strongly nonmonotone; Fisher/JS path length and directed D0→Dt metric drift were retained as separate candidates. |
| B39.2-P1 | `INFORMATION_METRIC_DRIFT_DIRECTED_ORDER_PASS` | Fresh D0/Dt shifts retained opposite signs while the predefined D0→Dt metric drift retained negative directed structure across geometry, phase, and resolution. |
| B39.3-P0 | non-claim-bearing reparameterization audit | Path-defined quantities were numerically stable under monotone post-hoc reparameterizations while coordinate-dependent slopes and shift coordinates changed. |
| B39.3-P1 | `INTEGRATION_LEVEL_REPARAMETERIZATION_COVARIANCE_FAIL` | The first fresh integration-level protocol remained a formal FAIL. Matched physical-time covariance was strong, but the frozen response-dependent intervention sentinel and a one-tick floating-boundary predicate prevented PASS. |
| B39.3-P1A | `NOT_READY_FOR_B39_3_P2_STRONGER_CLOCK_INTERVENTION_FREEZE` | Diagnostic localization only; no regrade of P1. |
| B39.3-P1B | `READY_FOR_B39_3_P2_FRESH_INTRINSIC_CLOCK_INTERVENTION_FREEZE` | Replaced response-dependent intervention strength with response-independent clock-map criteria and selected (|k|=1.4). |
| B39.3-P2 | `INTRINSIC_CLOCK_MAP_INTEGRATION_COVARIANCE_PASS` | Fresh response-independent clock intervention preserved matched physical-time responses and the predefined path structures within the retained tolerances. |

---

## B39.1 — relational clock persistence

B39.1 uses a target-excluded cumulative path coordinate built from symmetric relations between the other response pairs. The clock still inherits event ordering from the external-time simulation.

The fresh claim-bearing test retained:

`RELATIONAL_CLOCK_WEIGHTED_RESIDUAL_PERSISTENCE_PASS`

Across 36 weighted pair cases:

- Dt relational/external ratio: 0.9333–1.0500, mean 0.97947;
- D0 relational/external ratio: 0.8000–1.1200, mean 0.92483;
- weighted shift-sign agreement: 100%.

This shows persistence under the frozen relational re-expression; it does not show that external time is unnecessary.

---

## B39.2 — information geometry and directed order

B39.2 first audited Shannon entropy, Fisher-Rao path length, Jensen-Shannon path length, and a directed D0→Dt readout-metric drift.

The scalar Shannon entropy was substantially nonmonotone and was not retained as a primary order variable. B39.2-P1 then prospectively tested the directed metric-drift hypothesis.

Formal verdict:

`INFORMATION_METRIC_DRIFT_DIRECTED_ORDER_PASS`

For the primary fresh geometry cases:

- D0 best shifts: -0.0325 to -0.0100;
- Dt best shifts: +0.0400 to +0.0450;
- metric-drift slope: -0.02664 to -0.01809;
- metric-drift endpoint change: -0.02252 to -0.01094;
- all frozen geometry, subcell-phase, and cross-resolution gates passed.

The supported statement is coexistence and reproducibility of directed timing order with directed readout-metric drift. Causation is not established.

---

## B39.3 — reparameterization audit, retained FAIL, and fresh repaired test

### P0: archived-path audit

B39.3-P0 reparameterized already-generated response paths. Endpoint drift, total variation, monotonicity ratio, and Fisher/JS path lengths were stable to numerical resampling error, while OLS slope and constant best-shift coordinates were explicitly parameter-dependent.

This was readiness only, not a scientific verdict.

### P1: first integration-level test

B39.3-P1 used 9 fresh baseline cells and 27 fresh branch integrations.

Formal verdict:

`INTEGRATION_LEVEL_REPARAMETERIZATION_COVARIANCE_FAIL`

The FAIL is retained permanently. It is not regraded.

Importantly, the fresh matched-physical-time response covariance itself was numerically strong:

- maximum weighted-trace relative L2 defect: about (6.4	imes10^{-5});
- minimum trace correlation: above 0.9999999996;
- final-field and path-quantity differences were also small.

The frozen protocol nevertheless failed because the intervention-nontriviality sentinel had been defined through a downstream response-slope change and because three D0 cases landed on a one-tick floating-point boundary representation.

### P1A/P1B: design diagnostics, not rescue

P1A localized the original failures without changing the P1 verdict.

P1B then defined intervention strength from the clock map itself, not from response. The selected fresh P2 clock family was

[
|k|=1.4.
]

For the two nonidentity directions:

- maximum normalized clock deviations: 0.10457 and 0.11971;
- analysis-window rate ratios: 2.32749 and 2.63815;
- both maps were strictly monotone.

### P2: fresh intrinsic-clock-map intervention

B39.3-P2 was frozen before any fresh P2 trajectory. It used:

- fresh geometries 4.46, 4.65, 4.77;
- representative geometry 4.65;
- 9 fresh baseline cells;
- 27 branch integrations;
- 81 equivalent simultaneous-source trajectories;
- identity, (k=+1.4), and (k=-1.4) branches.

Formal verdict:

`INTRINSIC_CLOCK_MAP_INTEGRATION_COVARIANCE_PASS`

All six frozen components passed.

Primary-case landmarks:

- maximum D0 trace relative L2 defect: (4.71	imes10^{-5});
- maximum Dt trace relative L2 defect: (4.86	imes10^{-5});
- minimum correlations: above 0.9999999996;
- maximum final-field relative L2 defect: (1.63	imes10^{-7});
- maximum final tangent-state symmetric relative defect: (7.16	imes10^{-5});
- maximum Fisher/JS relative differences: about (1.64	imes10^{-4});
- D0 lag ticks: -4 to -1;
- Dt lag ticks: +5 to +7;
- (DeltaGamma<0) throughout the frozen primary gate.

Subcell-phase and N128/N160/N192 cross-resolution checks also passed.

The earlier P1 FAIL remains unchanged.

---

## Interpretation

The retained B39 sequence is:

```text
weighted-dual residual survives a target-excluded relational clock
    -> scalar entropy is not a clean directed-order variable
    -> directed information-metric drift is prospectively reproducible
    -> archived path quantities are stable under monotone reparameterization
    -> first fresh integration-level protocol FAILS under its frozen design
    -> response-independent clock-map calibration replaces the flawed sentinel
    -> new fresh P2 integration-level covariance test PASSES
```

The strongest supported finite-model statement is:

> Under the prospectively frozen response-independent clock-map intervention used in B39.3-P2, matched physical-time response trajectories and the predefined path-based metric/information temporal structures were preserved within the retained tolerances, while the directed D0/Dt lag signs remained readable on the frozen discrete lag grid.

This does **not** establish emergent physical time, that external time is unreal or gauge-like, arbitrary reparameterization invariance, a continuum theorem, fundamental non-reciprocity, wave propagation, Lorentz structure, quantum structure, or a universal law.

---

## Citation

```text
Lucis, J. Relational Clocks, Information-Metric Drift, and Clock
Reparameterization in a Finite Boundary-Response Model.
Boundary Information Geometry (BIG-B39), 2026.
DOI: 10.5281/zenodo.23113994.
```

Zenodo: https://doi.org/10.5281/zenodo.23113994
