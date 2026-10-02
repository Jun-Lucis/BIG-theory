# BIG Later-Phase Research Status — B37 to B38

**Date:** 2026-10-02  
**Scope:** transition from absolute peak-timing sensitivity to prospective relational timing and weighted measurement duality

Earlier formal verdicts are retained unchanged. This document does not regrade B30–B36 or any earlier stage.

## B37 — why absolute peak timing became a questionable primitive

B37 followed the B36 timing decomposition by replacing angular sampling with intrinsic boundary-contour arc length and then fixing the intrinsic support geometry.

Two frozen claim-bearing tests remained negative:

- B37.1: `INTRINSIC_CONTOUR_REPARAMETERIZATION_FAIL`
- B37.2: `FIXED_ARC_SUPPORT_TIMING_COLLAPSE_FAIL`

The B37.2 failure was localized to the absolute peak-time cross-resolution threshold. Subsequent non-claim diagnostics showed substantial grid-phase sensitivity of outer-probe peak timing. The outer-minus timing anomaly was comparable to subcell phase effects, and a phase-averaged absolute timing quantity became much flatter than the unshifted one.

A separate existing-data alignment analysis then showed that the nonoscillatory pulse traces shared a highly reproducible common waveform after temporal rephasing and affine adjustment. Relative lag versus intrinsic probe distance was much more stable than the raw absolute peak time.

B37 therefore motivated a change of observable rather than a retrospective repair of the failed peak-time claims.

## B38.1 — prospective relative boundary lag

B38.1 prospectively tested relative lag with the nearest intrinsic probe as reference.

Formal verdict:

`RELATIVE_BOUNDARY_LAG_GEOMETRY_PASS`

Key retained landmarks:

- minimum primary pair (R^2): 0.9849076
- minimum shifted correlation: 0.9962552
- maximum within-geometry phase relative slope span: 1.0067%
- representative N128/N160 relative slope difference: 0.0256%

This supports a coherent relative-lag relation in the tested finite model. It does not establish a wave, front, propagation speed, resonance, dispersion relation, continuum theorem, or universal law.

## B38.2 — directed source/receiver swap response

B38.2-P1 prospectively swapped source and receiver roles under the same dual-support construction.

Formal verdict:

`DIRECTED_SOURCE_RECEIVER_SWAP_ASYMMETRY_PASS`

The fresh direct trace defects were approximately 0.0678–0.0748 and best-shift magnitudes approximately 0.230–0.300. The shifted waveforms remained extremely similar, with minimum shifted correlation above 0.99997.

This establishes reproducible directed swap asymmetry only in the tested finite reduced model.

## B38.3 — tangent-operator structure

B38.3-P1 found that the exact semi-discrete tangent operator is non-self-adjoint in the standard metric but nearly symmetric under the D weighting.

Formal verdict:

`D_WEIGHTED_NEAR_SYMMETRY_WITH_DIAGONAL_CYCLE_OBSTRUCTION_PASS`

At N160, D weighting reduced the edge-asymmetry measure by roughly 456–466 times.

A compatible-discretization control then separated a large discretization contribution from a smaller gamma-dependent residual. B38.3-P2-P1 retained:

`COMPATIBLE_GAMMA_RESIDUAL_CYCLE_WITH_DISCRETIZATION_DOMINANCE_PASS`

The compatible gamma=0 control closed the D-weighted metric defect and plaquette-cycle obstruction to roundoff, while the compatible directional cubic tangent restored a much smaller finite-grid residual.

No continuum persistence or fundamental non-reciprocity follows.

## B38.4 — prospective operator-to-response bridge

B38.4-P1 froze all tangent predictions before any fresh nonlinear response trajectory.

Formal verdict:

`TIME_DEPENDENT_TANGENT_RESPONSE_BRIDGE_PASS`

Key N160 prediction metrics:

- maximum directed trace defect: 0.0007851
- minimum directed trace correlation: 0.99999923
- maximum swap-defect absolute error: 7.14e-05
- maximum best-shift error: 0.0025

Thus the evolving tangent field operator predicts the tested small-amplitude nonlinear directed-response structure with high accuracy.

## B38.5 — gamma is not the dominant timing contribution

B38.5-P1 prospectively tested whether the large swap rephasing survives under the time-dependent D-compatible gamma=0 control.

Formal verdict:

`D_COMPATIBLE_GAMMA0_REPHASING_RETENTION_PASS`

The minimum C0/observed absolute-shift ratio was 0.93. Removing gamma in the original tangent changed the extracted best shift by 0 at the frozen timestep resolution, while the maximum compatible (C_gamma-C_0) timing increment was below 0.93% of the O1 shift.

The result does not identify nonautonomous time dependence as the unique cause.

## B38.6 — prospective weighted measurement duality

B38.6-P0 was historical calibration only and assigned no scientific verdict. It selected a final prospective measurement-duality hypothesis.

B38.6-P1 froze the protocol before any fresh B38.6-P1 baseline or tangent source trajectory.

Formal verdict:

`D_WEIGHTED_DUAL_READOUT_SUPPRESSION_PASS`

Key fresh results:

- minimum standard absolute best shift: 0.235
- maximum frozen-D dual / standard absolute-shift ratio: 0.14737
- maximum instantaneous-D dual / standard absolute-shift ratio: 0.17021
- mean frozen-D ratio: 0.09299
- mean instantaneous-D ratio: 0.15537
- frozen-C0 weighted-dual maximum swap defect: 3.14e-16
- frozen-C0 weighted-dual maximum absolute best shift: 4.44e-16

The large standard-readout timing rephasing is therefore strongly suppressed by the D-weighted dual receiver convention across the frozen fresh geometry, subcell-phase, and resolution checks.

## Terminal B38 interpretation

The B38 sequence supports a relational interpretation of the measured timing observable:

```text
absolute peak timing becomes numerically fragile
    -> relative lag remains coherent
    -> source/receiver swap asymmetry is reproducible
    -> the time-dependent tangent operator predicts that asymmetry
    -> gamma is not its dominant timing contribution
    -> operator-compatible D-weighted dual readout suppresses most of the large rephasing
```

The strongest supported statement is not that the model contains a fundamental one-way time law. It is that the observed timing asymmetry is strongly dependent on the relation between operator, source, receiver, and readout.

The remaining evolving weighted-dual residual is unresolved. B38 does not establish that this residual is fundamental, irreducible, observer-limited, or uniquely caused by nonautonomous time ordering.

## Publication

**B38 title:** *Relational Timing and Weighted Measurement Duality in a Finite Nonlinear Boundary Field Model*  
**Subtitle:** *From Directed Source–Receiver Rephasing to Operator-Compatible Readout*  
**DOI:** https://doi.org/10.5281/zenodo.23104248

Repository entry: [papers/B38_relational_timing_weighted_duality](../papers/B38_relational_timing_weighted_duality)
