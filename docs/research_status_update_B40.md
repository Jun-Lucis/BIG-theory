# BIG-B40 — Clock-Family Transfer and Target-Excluded Relational Reconstruction

**Preprint title:** *Clock-Family Transfer and Target-Excluded Relational Reconstruction in a Finite Boundary-Response Model*  
**Author:** Jun Lucis  
**Zenodo DOI:** https://doi.org/10.5281/zenodo.23153688  
**Publication date:** 2026-10-05  
**Status:** B40 closed; Zenodo v1.1 published

## Programme question

B40 asks how far the B39.3-P2 finite-model clock-map covariance survives when the clock construction itself is changed, and then whether the prescribed clock map can be removed from the primary reconstruction coordinate.

The programme retains the prospective discipline used in B37–B39:

```text
diagnostic/calibration
    -> response-blind freeze
    -> fresh claim-bearing evaluation
    -> retain FAILs
```

No successor stage retroactively upgrades a parent FAIL.

## B40.1 — clock-map family transfer

B40.1 replaced the preceding exponential clock-map family with response-independently selected parabolic and sinusoidal monotone families,

```text
w_b(q) = q + b q(1-q),       |b| = 0.50
w_a(q) = q + [a/(2pi)] sin(2pi q),   |a| = 0.65
```

while retaining the inherited finite semi-discrete physical model, cases, observables, lag grid, integration controls, and tolerances.

Formal result:

`CLOCK_MAP_FAMILY_TRANSFER_FAIL`

The failure was narrow: one primary sinusoidal D0 comparison landed at zero on the frozen coarse lag grid. The parabolic family, representative subcell phases, cross-resolution checks, response traces, final fields, and information-path quantities remained within the frozen covariance tolerances.

A prospectively frozen ten-times-finer lag test then returned:

`LAG_GRID_QUANTIZATION_LOCALIZATION_PASS`

with the parent FAIL retained. The formerly failing D0 case resolved to a negative fine-grid shift, while Dt remained positive.

## B40.2 — target-excluded relational reconstruction

B40.2 removed the prescribed clock map from reconstruction analysis. It used the `evolving_Dt_dual` readout and a target-excluded offline Fisher/Hellinger progress coordinate,

```text
L_F(n) = sum_{j<n} 2 arccos( sum_i sqrt(p_i^(j) p_i^(j+1)) )
tau_F(n) = L_F(n) / L_F(final)
```

where the held-out target edge is excluded from the driver probability. Because endpoint normalization uses the final path endpoint, this is an **offline relational progress coordinate**, not an intrinsic clock.

The initial prospective test returned:

`TARGET_EXCLUDED_RELATIONAL_RECONSTRUCTION_FAIL`

The resolution holdout passed, but phase holdout and nontrivial-advantage components failed. The parent FAIL remains part of the record.

## Localization and covariance sequence

| Stage | Formal result | Retained interpretation |
| --- | --- | --- |
| B40.2-P1B | `PHASE_RESOLUTION_LOCALIZATION_PASS` | `PERSISTENT_Y_ORIENTATION_LIMIT_SUPPORTED` |
| B40.2-P1C | `AXIS_SWAP_ORIENTATION_LOCALIZATION_PASS` | `SOURCE_RELATIVE_ORIENTATION_SWAP_SUPPORTED` |
| B40.2-P1D | `NEGATIVE_PHASE_AXIS_SWAP_REPLICATION_PASS` | `NEGATIVE_PHASE_SOURCE_RELATIVE_SWAP_SUPPORTED` |
| B40.2-P1E | `ORIENTATION_REVERSING_COVARIANCE_TRANSFER_PASS` | fresh 23°/67° covariance transfer |
| B40.2-P1F | `THIRD_ANGLE_ORIENTATION_REVERSING_COVARIANCE_REPLICATION_PASS` | third-angle 17°/73° replication |

The orientation-reversing transformation combines:

- spatial exchange `x <-> y`;
- source phase `theta_a x_{+/-1/3} <-> theta_b y_{+/-1/3}`;
- channel permutation `[2,1,0]`;
- directed target-side reversal `minus <-> plus`.

P1E at 23°/67° passed all frozen covariance components with reconstruction categorical match fraction 1.0.

P1F independently replicated the same rule at 17°/73°. Its reconstruction categorical match fraction was again 1.0. Two fresh reconstruction threshold failures remained, but they occurred as one transformed covariance-partner pair. Thus reconstruction is not uniformly successful; rather, the limitation itself transforms covariantly under the tested finite-grid rule.

## Integrated conclusion

The strongest supported B40 statement is deliberately finite:

> In the tested semi-discrete boundary-response model, reconstruction success and failure are organized by a reproducible orientation-reversing covariance relating source/readout orientation to directed-side reversal.

B40 does **not** establish:

- arbitrary reparameterization invariance;
- a universal relational clock;
- emergent physical time;
- continuum rotational covariance;
- physical anisotropy;
- a continuum theorem.

The next information-bearing tests would be parameter and discretization transfer — for example pre-delta, phase magnitude, grid geometry, boundary implementation, and alternative discretizations — rather than adding more symmetry-angle pairs.

## Archive

Zenodo DOI: https://doi.org/10.5281/zenodo.23153688

The Zenodo record contains the English preprint, a Japanese reference translation, and a compact reproducibility/audit package.
