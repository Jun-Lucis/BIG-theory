# BIG-B8 v0.3 — source, numerics, and mathematical audit

**Date:** 31 October 2026  
**Author:** Jun Lucis  
**Current version-specific DOI:** [10.5281/zenodo.23832946](https://doi.org/10.5281/zenodo.23832946)  
**Publication:** [Zenodo B8 v0.3 record](https://zenodo.org/records/23832946) (English revised preprint, Japanese reference translation, reproducibility supplement)  
**Historical dataset correction:** [B8 v0.2 / 10.5281/zenodo.23385079](https://doi.org/10.5281/zenodo.23385079)  
**Original archived record:** [10.5281/zenodo.20645317](https://doi.org/10.5281/zenodo.20645317)

## Scope and preservation

The B8 finite-time amplitude thresholds were obtained with a particular
periodic finite-difference discretization and a box-projected update. They
remain valid **as archived finite-model numerical classifications** under
their original input, timestep, stopping criteria, observation horizon, and
data provenance. They are not certified continuum singularity times,
asymptotic separatrices, or empirical failure thresholds.

The v0.2 archive corrected model/prediction labels, ratio identifiers,
aggregate history and figure representations **without changing** the
historical fitted coefficients, thresholds, or formal conclusions. The
v0.3 release adds a separately identified numerical and mathematical
audit; it does not overwrite the historical results or retrospectively
turn numerical observations into proofs.

## The executed B8 operator and numerical rules

For the audited \(m=1\) positive-interior branch, the *formal*
unprojected equation is

\[
\partial_t\phi
=\nabla\cdot\bigl[\phi\nabla\phi
  -\gamma|\nabla\phi|^2\nabla\phi\bigr]-\mu\phi.
\]

The source-aligned implementation uses a periodic central-gradient,
central-divergence spatial stencil, forward Euler update, elementwise
post-update clipping to the interval \([0,5]\), and an event stop if
the pre-update spatial RMS of the RHS exceeds 1 or the stipulated
peak condition is reached. The main controlled setting uses
\(\gamma=0.8735\), \(\mu=0.3\), side length \(L=8\), and
\(T=0.4\). In particular, the algorithm is **not** the exact flow
of the formal unprojected equation. It is also not equivalent to a
positive-quartic-energy gradient flow simply by changing notation.

## Retained source and reproducibility audit

A source-aligned replay of four original archived terminal fields
achieved a maximum all-cell discrepancy of \(9.36\times10^{-14}\).
This is a **limited replay check**, not authentication of every
original solver run, ray fitting calculation, or full independent
re-execution of the entire historic archive.

Earlier audit records also document that clipping changes the field
integral in selected original cases. The effect must be reported
separately from the formal PDE's unprojected integral budget.

## Spatial discretization and timestep controls

For one *newly audited* circular reference case (aspect ratio 1.0,
amplitude 0.345), the numerical stopping rule differs between the
original centered scheme and a separately implemented consistent
face-flux discretization:

| Grid | Original centered scheme | Alternative face-flux scheme |
|---|---|---|
| N=96 | No RHS stop by T=0.4 | STOP near t=0.295973 |
| N=120 | STOP; precise trigger time not recovered in this comparison | STOP near t=0.251697 |
| N=144 | STOP near t=0.285417 | STOP near t=0.225117 |
| N=160 | STOP near t=0.266403 | STOP near t=0.210211 |

These STOP times are **numerical threshold events**. At the tested
N144 and N160 central-scheme cases, grid-scaled timestep reductions
gave first trigger times close to the original runs (N160:
0.266403 vs 0.26639784). Separate timestep-control results for the
face-flux scheme at N96 and N120 were similarly close. This rules
out a *purely coarse timestep* explanation for those selected
finite-grid observations, but does not prove a convergent timestep
limit or a well-posed spatial continuum limit.

Both stencils showed numerical second-order consistency on a distinct
smooth manufactured positive test field. That manufactured-field result
does not imply nonlinear time-evolution convergence or determine which
numerical STOP sequence approximates a continuum solution.

## Conditional principal-symbol and linearization results

Write \(q=\nabla\phi_0\). In a positive smooth interior region,
the principal matrix of the time-frozen linearization is

\[
A(x)=\phi_0 I-\gamma\bigl(|q|^2I+2q\otimes q\bigr).
\]

Its gradient-parallel and transverse eigenvalues are respectively

\[
a_\parallel=\phi_0-3\gamma|q|^2,\qquad
a_\perp=\phi_0-\gamma|q|^2.
\]

For the circular initial field
\(\phi_0(r)=0.345(1-r^2/4)_+^2\),
a strictly negative parallel eigenvalue occurs on approximately
72.35% of the positive interior disk area, by an exact radial
condition and geometric area calculation. At the positive interior
point \((x,y)=(1.5,0)\) the parallel coefficient is approximately
\(-0.0682911\).

**Conditional proof claim:** for this specified initial profile,
the formal **spatially variable-coefficient**, time-frozen
linearization acting on a standard periodic \(L^2\) space cannot
generate a \(C_0\) semigroup for an operator realization whose
domain contains all smooth compactly supported interior
perturbations and on which the differential expression acts as
written. A localized high-frequency wave-packet and the
necessary semigroup resolvent bound give the contradiction.
The theorem is *not* an assertion that every nonlinear or weak
solution of B8 fails to exist, nor a proof of finite-time blow-up
in a continuum B8 trajectory. The mathematical argument has
not been independently peer reviewed.

## Regularization candidates are new models

An added positive Laplacian changes the equation. For the
specified fixed elliptical initial profiles, exact conditions
can be derived for the modified principal matrix to be
nonnegative; these do not certify future positivity or a
global nonlinear evolution. An added \(-\epsilon\Delta^2\phi\)
with \(\epsilon>0\) controls the unbounded high-wavenumber
growth of the *fixed-profile linearization* and supports a
linear analytic semigroup, but general nonnegative-data
positivity preservation fails even for the pure biharmonic
heat equation. Neither modification is a retroactive
reconstruction of the original B8 source model.

## Evidence-class register

| Claim | Retained classification |
|---|---|
| Four archived terminal field replays | **LIMITED REPRODUCIBILITY PASS** |
| Archived anisotropy-dependent amplitude thresholds | **FINITE-GRID NUMERICAL OBSERVATION** |
| Numerically defined STOP versus scheme/grids | **NUMERICAL SCHEME SENSITIVITY** |
| Negative principal eigenvalue in positive interior | **MATHEMATICAL DERIVATION** |
| Fixed-profile variable-coefficient linearization obstruction | **CONDITIONAL PROOF** |
| A continuum-invariant finite-time separatrix | **NOT ESTABLISHED** |
| General full nonlinear well-posedness or blow-up of B8 | **UNRESOLVED** |
| Any regularized model's physical validity | **NEW ASSUMPTION / UNVALIDATED** |
| Distinctive physical prediction beyond conventional baselines | **NOT ESTABLISHED** |

## Relation to later BIG studies

The B8 negative-quartic-flux dynamics must not be substituted
for the separately defined B9 perimeter/nonlocal energy model,
positive-flux p-gradient models, moving-boundary/history
systems, or B20–B23 parameter-space response geometry.
B8 cannot automatically validate or invalidate those branches.
Their numerical evidence and frozen FAIL/INCONCLUSIVE outcomes
must be assessed using their own **source-specific equations
and executed implementations**. B42's overall formal scientific
verdict remains **SCIENCE NONE**.

## Reproducibility and citation

- Cite the **version-specific v0.3 DOI** for the new mathematical
  audit and revised preprint.
- Cite the **v0.2 DOI** for its corrected finite-grid dataset and
  metadata, and preserve the original archive's historical DOI.
- Numerical source artifacts, checksums, calculation scripts and
  audit tables are provided as the separate reproducibility ZIP in
  the **v0.3 Zenodo record**. The paper and historical release
  claims should not be merged into a new or retroactively
  reclassified prospective test.
- AI-assisted drafting and code auditing do not substitute for
  independent mathematical peer review, independent full
  numerical replay, or physical calibration.
