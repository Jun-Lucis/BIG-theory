# BIG-B19E — External Flow Validation
## Design audit v0.2 — NOT FROZEN

**Author:** Jun Lucis  
**Date:** 2026-09-26  
**Status:** DESIGN AUDIT COMPLETE FOR NEXT-STAGE PLANNING; B19E.1/B19E.2 NOT FROZEN  
**Frozen parent instrument stage:** B19E.0 (BIG_B19E_0_EXTERNAL_DATASET_AUDIT_v1_0)  
**B19E.0 semantic SHA-256:** 8fa8123f1346183d1032036d1195bad053752305e473c26842812bedd5d441a1

## 1. Design principle

B19E is not a literal replay of the published B19 classifier on an external field.

The main external-validation question is:

> Do boundary/core descriptors developed from the BIG vorticity program add prospective information about future intense-vorticity amplification in an independently generated Navier–Stokes DNS, beyond a strong standard local-flow baseline?

This formulation deliberately makes external predictive increment, rather than recovery of one synthetic threshold, the primary scientific object.

## 2. Historical internal evidence used for design only

The design audit may use archived B19-related numerical history, including material not promoted to the integrated B19 paper. These records guide measurement choices but do not count as external evidence.

### Published B19 lesson

The integrated B19 study supports a channel-family interpretation rather than one robust ray-independent upstream scalar. Positive local stretching and signed gate-local openness were not sufficient by themselves; finite-window outcomes were better organized by evolving production-versus-dissipation balance.

### B19.17a / B19.17b

Local signed continuation around a fragile late-delayed state produced direction-dependent growth/decay brackets. Within the B19.17a synthetic continuation, the sign of time-integrated total balance matched the finite-window growth sign for all mapped cases. B19.17b then refined the directional boundaries and tested resolution/timestep sensitivity.

Design consequence:
- the external comparator must be physically strong;
- BIG geometry should be tested for incremental information beyond stretching/balance-type information;
- resolution/sampling robustness must be explicit.

### B19.18 / B19.19

The archived reduction programme searched for a reduced control-variable collapse and minimal two-coordinate portrait.

Design consequence:
- do not force an external universal scalar or two-coordinate phase portrait;
- allow a compact multivariate boundary/core representation, but keep model complexity deliberately low.

### B19.20

Directional mechanism decomposition retained different upstream responses across directions while downstream outcomes approached a common finite-window production/dissipation organization.

Design consequence:
- separate "standard local mechanism" features from "boundary/core geometry";
- measure whether geometry adds information after standard mechanism variables are already present.

### B19.21C

Temporal-channel-separation calculations explicitly studied when refined growth/decay pairs diverge.

Design consequence:
- horizon is part of the prediction problem;
- use more than one future horizon, with exactly one declared primary horizon.

### B19.22C / B19.22F

Extended-horizon continuation showed horizon-dependent loss/escape of detected response boundaries, and deterministic thinning tests preserved the p03 decreasing-to-mixed-to-increasing ordering under the tested sampling variants.

Design consequence:
- absence of an event in a sampled domain must not be interpreted as nonexistence;
- deterministic temporal/spatial thinning checks should be included;
- a one-horizon result is insufficient for mechanism claims.

## 3. External dataset

Primary candidate remains the Johns Hopkins Turbulence Database forced isotropic turbulence dataset isotropic1024coarse.

Reasons:
- independently generated DNS;
- 1024^3 periodic pseudo-spectral Navier–Stokes simulation;
- long stored time series;
- full velocity-gradient queries and particle tracking are supported;
- periodic homogeneous geometry is close enough to the synthetic B19 numerical setting to make diagnostic translation feasible without pretending the datasets are identical.

The external flow is forced, unlike the synthetic B19 finite-window setup. This difference is scientifically useful and must not be hidden.

## 4. Critical distinction: local balance is not imported as an identity

For the global periodic synthetic B19 calculation,

\[
B_{\rm B19}=\int \omega\cdot S\omega\,dV-\nu\int |\nabla\omega|^2\,dV
\]

was the total enstrophy-balance readout used in the finite-window tests.

For a local region of an externally forced DNS, a simple local "stretch minus viscous-gradient" quantity is not automatically the exact future local enstrophy balance because transport/flux and forcing contributions also enter.

Therefore B19E will not use a local B19-style balance proxy as an exact law.

It belongs in the standard baseline / diagnostic layer unless the missing transport and forcing terms are explicitly reconstructed.

## 5. Target design

### 5.1 Existing B19E.0 reserved point target

B19E.0 already reserves a later Lagrangian point target,

\[
Y_H=
\log\frac{|\omega(X(t_0+H),t_0+H)|+\epsilon}
{|\omega(x_0,t_0)|+\epsilon}.
\]

This remains a valid low-cost endpoint.

### 5.2 Recommended primary upgrade for B19E.1/B19E.2

Before B19E.1 is frozen, test the feasibility of a material-core target on development times only.

For one initial connected intense-vorticity core C_0, seed a deterministic quasi-uniform particle set x_j(t_0) in C_0, advect it with JHTDB particle tracking, and define

\[
G_H=
\log\frac{\frac1m\sum_j|\omega(X_j(t_0+H),t_0+H)|^2}
{\frac1m\sum_j|\omega(x_j(t_0),t_0)|^2}.
\]

Recommended interpretation:
- material-core G_H: preferred primary endpoint if B19E.0/E1 feasibility is adequate;
- pointwise Y_H: low-cost secondary endpoint and audit comparator.

Reason:
the material-core target is closer to the boundary/core scientific object and avoids treating a fixed Eulerian box as a material region.

If material-core tracking is unstable, too expensive, or under-resolved, retain the already-reserved pointwise target as primary rather than changing the definition after held-out outcomes are seen.

## 6. Event construction

Proposed development-only event finder:

1. deterministic scrambled Sobol probe points from the frozen B19E.0 generator;
2. query velocity gradients at the anchor time;
3. reconstruct omega and rank intense-vorticity candidates;
4. impose periodic spatial separation and macroblock coverage;
5. obtain a local high-resolution cutout around each retained candidate;
6. refine to a local |omega| maximum;
7. construct the connected component containing that maximum at relative vorticity levels;
8. reject any outer component touching the analysis-cutout boundary.

Initial relative levels to test on development data:
- inner core: |omega| >= 0.50 A;
- outer core: |omega| >= 0.25 A;
- shell: outer component minus inner core.

The exact levels are NOT frozen for B19E.1 until development-time stability, event counts, and cutout-boundary sensitivity have been checked.

## 7. Predictor architecture

The primary scientific comparison should be nested.

### Standard baseline M_std

Candidate features:
- log |omega|;
- normalized stretching omega-hat^T S omega-hat;
- strain magnitude and strain eigenvalues;
- alignment of vorticity with strain eigenvectors;
- velocity-gradient invariants Q,R;
- local viscous-gradient proxy where numerically stable;
- optionally local forcing magnitude or omega dot curl(f) if its meaning and derivative quality are validated in B19E.0/E1.

### Boundary/core augmentation M_BC

Candidate features:
- connected core volume;
- outer/core volume ratio;
- surface-area proxy;
- compactness;
- equivalent radius;
- nested-level thickness/equivalent-radius ratio;
- inertia-tensor anisotropy;
- peak-to-centroid offset;
- vorticity-direction coherence in core and shell;
- signed-stretch coherence in shell;
- core-versus-shell stretching contrast;
- core-versus-shell enstrophy-density contrast.

Primary model class:
standardized low-complexity ridge regression.

The scientific comparison is M_std versus M_BC = M_std + frozen boundary/core descriptors.

B19E should not claim success merely because M_BC beats a null/chance predictor.

## 8. Time-block firewall

B19E.0 already froze:

- development: t0 = {1.0,1.5,2.0};
- calibration/model-selection: t0 = {3.5,4.0};
- primary holdout: t0 = {6.5,7.0};
- replication holdout: t0 = {9.0,9.5};
- primary horizon H = 0.05;
- secondary horizon H = 0.10.

Do not change this split after field-level performance is inspected.

B19E.1 may use development and calibration blocks only.

B19E.2 must freeze:
- event finder;
- feature definitions;
- preprocessing;
- model class;
- coefficients / calibration rule;
- exact primary target;
- evaluation metrics;
- formal gates;

before primary-holdout future outcomes are retrieved.

Replication holdout remains untouched until the primary test is closed.

## 9. Evaluation

Recommended primary metric:
paired out-of-sample squared-error difference between M_std and M_BC.

Additional metrics:
- held-out R^2;
- Spearman correlation;
- secondary sign AUC for G_H>0 or Y_H>0;
- per-anchor-time performance;
- block bootstrap by anchor time / spatial macroblock rather than treating nearby cores as independent iid observations.

A future PASS rule should require:
1. positive lower confidence bound for incremental predictive improvement;
2. a predeclared nontrivial effect-size floor;
3. improvement at most or all predeclared primary anchor times, according to a frozen rule;
4. no gross degradation under deterministic thinning / boundary-threshold sensitivity controls.

Exact numerical gates are deliberately NOT set in this design audit. They must be calibrated from development/calibration blocks and frozen before B19E.2.

## 10. Robustness layer

At minimum, before a positive external-transfer claim:
- deterministic candidate thinning;
- alternate nested-core threshold pair fixed before holdout;
- cutout-size / boundary-touch audit;
- derivative operator/interpolation audit;
- repeated-query reproducibility;
- pointwise versus material-core endpoint comparison as a secondary diagnostic;
- horizon 0.05 versus 0.10 comparison.

No robustness repair may redefine the primary held-out success criterion after outcomes are known.

## 11. Stage sequence

**B19E.0 — External Dataset and Measurement Audit**  
Already frozen. No predictive-transfer claim.

**B19E.1 — Development and Diagnostic Translation**  
Development/calibration only. Select one stable external boundary/core representation and one low-complexity nested predictor architecture.

**B19E.2 — Frozen Prospective External Validation**  
Untouched primary holdout. Formal incremental-transfer verdict.

**B19E.3 — Frozen Temporal Replication**  
Apply the B19E.2 predictor unchanged to the untouched replication block. No refit.

**B19E.4 / B20E — optional later branches**  
Cross-flow family or external response geometry only after B19E.2/B19E.3 are closed.

## 12. Claim boundary

A positive result would support:

> A frozen BIG-derived boundary/core representation contains incremental prospective information about future vorticity amplification in the tested independent DNS, beyond the specified standard local-flow baseline.

It would NOT establish:
- a Navier–Stokes blow-up or regularity result;
- a universal separatrix;
- a universal turbulence law;
- a unique causal role for "boundary";
- laboratory/experimental validation;
- continuum convergence outside the tested query/interpolation/resolution controls.

A negative result would also be informative: it would show that the chosen B19-derived boundary/core representation did not add transferable predictive information under the frozen external-DNS protocol.
