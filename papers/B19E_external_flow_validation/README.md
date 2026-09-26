# BIG-B19E — External Flow Validation

**Author:** Jun Lucis  
**Status:** DESIGN ACTIVE; B19E.0 frozen before JHTDB field query  
**Parent arc:** B19 boundary-core / vorticity diagnostics  
**Primary external dataset:** JHTDB `isotropic1024coarse`  
**B19E.0 semantic SHA-256:** `8fa8123f1346183d1032036d1195bad053752305e473c26842812bedd5d441a1`

## Purpose

B19E asks whether boundary/core geometry developed independently within BIG carries prospective predictive information when transferred to an independently generated high-resolution Navier–Stokes DNS.

The primary question is deliberately stronger than a literal replay of one B19 scalar threshold:

> Do BIG-style boundary/core geometric descriptors add held-out predictive information about future Lagrangian vorticity amplification beyond a strong classical local-flow baseline?

The first target dataset is the Johns Hopkins Turbulence Database forced isotropic turbulence simulation, `isotropic1024coarse`.

## Why B19E does not force a universal B19 threshold

The B19 programme found direction-dependent channel families rather than a robust ray-independent upstream scalar reduction. Later finite-window studies also showed that detected growth/decay boundaries depend on observation horizon. B19E therefore treats horizon as part of the prediction problem and tests incremental external predictive information rather than demanding recovery of one synthetic-family threshold.

## Frozen external time split

The split is fixed before any B19E field-level performance study:

- development: t0 = 1.0, 1.5, 2.0
- calibration/model selection: t0 = 3.5, 4.0
- primary holdout: t0 = 6.5, 7.0
- replication holdout: t0 = 9.0, 9.5

Primary horizon: Δt = 0.05  
Secondary horizon: Δt = 0.10

Primary/replication holdout fields and future outcomes must remain unopened until the B19E.2 predictor and evaluation rules are frozen.

## Primary target

For an initial point x0, B19E will use JHTDB particle tracking and define a Lagrangian vorticity-amplification target,

[
Y_{Delta t}
=
log
rac{|omega(X(t_0+Delta t),t_0+Delta t)|+epsilon}
{|omega(x_0,t_0)|+epsilon}.
]

The primary endpoint is continuous Y at Δt=0.05. Binary amplification sign and Δt=0.10 are secondary.

## Classical baseline

The classical pointwise baseline is intentionally strong and may include:

- vorticity magnitude;
- normalized stretching (omega^T Somega/|omega|^2);
- strain eigenvalues;
- vorticity/strain-eigenvector alignments;
- velocity-gradient invariants Q and R.

## BIG geometry layer

A spatially spread subcohort will receive t0-only local neighborhood queries. Candidate geometry descriptors include connected relative-vorticity core volume, boundary-area proxy, compactness, anisotropy, centroid offset, boundary-thickness proxy, vorticity-direction coherence, signed-stretching fractions, and core-versus-boundary stretching contrast.

Development may choose among a small predeclared set of neighborhood scales using development/calibration data only. The final representation must be frozen before holdout access.

## Stage structure

- **B19E.0 — External Dataset Audit and Measurement Contract**  
  Interface, metadata, component ordering, derivative reconstruction, periodic wrapping, particle tracking, repeatability. No predictive-transfer claim.

- **B19E.1 — Development and Diagnostic Translation**  
  Development/calibration blocks only. Build the strong classical baseline and select the frozen external boundary/core representation.

- **B19E.2 — Frozen Prospective External Validation**  
  Untouched primary and replication holdouts. Formal external-transfer verdict.

- **B19E.3 — Cross-flow replication**  
  Optional later replication in a second external flow family after B19E.2 is closed.

## Claim boundary

A positive B19E result would support only that the frozen BIG boundary/core geometry carries incremental prospective information in the tested external DNS beyond the chosen baseline.

B19E does not establish a Navier–Stokes blow-up criterion, regularity theorem, universal turbulence law, laboratory validation, or universal BIG scalar threshold.
