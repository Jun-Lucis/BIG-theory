# BIG-B28-P0 Frozen Calibration Predeclaration v1.1

**Protocol ID:** BIG_B28_P0_COMPONENT_RESOLVED_SPLIT_CALIBRATION_v1_1  
**Status:** FROZEN CALIBRATION-ONLY BEFORE B28-P0  
**Freeze date:** 2026-09-29  
**Claim-bearing:** NO

## Purpose

Calibrate the component-resolved 1-to-2 split representation before any B28 claim-bearing response trajectory.

P0 tests only:

- fresh-family topology realization;
- component extraction and deterministic ordering;
- source-axis-aligned child-local probe bases;
- geometry-only split-operator conditioning;
- weighted reconstruction error;
- two-probe-scale response stability;
- cross-resolution stability;
- retained-history readout executability.

No P0 case may be promoted to B28 evidence.

## Fresh geometry family

The P0 source family is an equal two-center compact-polynomial family rotated by

\[
\theta=25^\circ.
\]

Preparation:

\[
\phi=0
\rightarrow
\text{single-center }(T=20)
\rightarrow
\delta_-=4.60,\;\theta=25^\circ\;(T=20).
\]

The pre-anchor must remain one primary threshold component.

History is written on the body/source-relative ray

\[
\psi_{\rm write}=95^\circ,
\]

equivalently \(120^\circ\) in the global frame.

Frozen topology-scan values:

\[
5.15,\;5.35,\;5.55,\;5.75,\;5.95.
\]

These scan points are calibration-only and are permanently excluded from later B28 claim evidence.

## Numerical pair

\[
N=128,\quad dt=0.003,
\]

\[
N=160,\quad dt=0.0025.
\]

The v1.1 protocol supersedes v1.0 before any P0 trajectory solely to strengthen the calibration pair from the initially drafted lower-resolution pair.

## Probe spaces

Pre:

\[
\mathbb R^5.
\]

Post:

\[
\mathbb R^{10}
=
\mathbb R^5\oplus\mathbb R^5.
\]

Both use the low-order \(l=0,1,2\) probe family in the frozen source-axis-aligned frame.

Primary/secondary probe amplitudes:

\[
h=0.001,\qquad 0.002.
\]

## Geometry-only split operator

The split operator

\[
S_\Gamma:\mathbb R^5\to\mathbb R^{10}
\]

is computed by weighted ridge projection of the pre spatial probe fields onto the two child-local post bases.

The construction may use only:

- threshold component geometry;
- child centers and radii;
- frozen source-axis frame;
- frozen boundary-envelope weights.

It may not use:

- \(K\);
- \(G\);
- kept-versus-erased response differences;
- \(H_G\);
- \(L_G\);
- target verdicts.

## P0 output

The notebook must write the topology scan, selected calibration split, geometry-projection reconstruction error, split-operator condition number, pre/post probe-scale lineage defects, cross-resolution pre/post lineage defects, cross-resolution post response-form defects, zero-feedback control, and a suggested numerical floor based only on numerical mismatch diagnostics.

Any kept-versus-erased transport defect calculated in P0 is explicitly non-claim-bearing.

## Stop rule

After B28_P0_summary.json is produced, stop.

B28.1 target values, final numerical gates, and verdict logic must be separately frozen before any B28.1 response trajectory.
