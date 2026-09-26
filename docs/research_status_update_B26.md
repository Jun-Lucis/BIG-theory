# BIG B26 Research Status Update

**Zenodo DOI:** https://doi.org/10.5281/zenodo.22972985  
**Related B25 Phase-II DOI:** https://doi.org/10.5281/zenodo.22967474  
**Related B24–B25 Phase-I DOI:** https://doi.org/10.5281/zenodo.22956894  
**Author:** Jun Lucis

B26 tests whether the fixed perimeter coefficient obtained prospectively in B25.1e transfers without recalibration from the held-out ellipse family to a canonical equal-injection two-center family that genuinely spans connected and disconnected representative contours.

The coefficient remains fixed throughout B26:

\[
\sigma_{\rm cal}=9.434181431178162\times10^{-8},
\]

with primary predictor

\[
J_{\rm pred}=\sigma_{\rm cal}P_{\rm total,rep}.
\]

No B26 target outcome, peak amplitude, full level-set perimeter family, topology label, or geometry was allowed to refit this coefficient.

## Evidence sequence

    B26
      intended topology-straddling transfer
      -> all 6 numerical cases valid
      -> topology span not realized
      -> TOPOLOGY_SPAN_NOT_REALIZED

    B26.1
      topology-only adaptive refinement
      -> 4/4 new cases valid
      -> 4.175 < delta_* < 4.250 at N=384
      -> TOPOLOGY_BRACKET_REFINED

    B26.2
      new topology-straddling held-out targets
      -> 6/6 numerical cases valid
      -> fine-resolution topology gate realized
      -> fixed-coefficient error remained large and stable
      -> AB_TOPOLOGY_STRADDLING_FIXED_COEFFICIENT_TRANSFER_FAIL

## B26

The first B26 test used

\[
\delta\in\{4.4,5.4,6.2\},\qquad N\in\{384,448\}.
\]

All six trajectories passed the frozen numerical validity gates. At the fine resolution, however, all three tested separations already had two primary representative contours. The predeclared connected/disconnected topology span was therefore not realized.

**Formal verdict:** TOPOLOGY_SPAN_NOT_REALIZED.

The descriptive fixed-coefficient errors from this stage are retained but are not promoted to a formal transfer FAIL.

## B26.1

B26.1 deliberately removed fixed-coefficient action error from the adaptive decision and used only representative-level topology. Four frozen bisection trajectories at \(N=384\) gave:

    delta=3.800 -> 1 primary representative contour
    delta=4.100 -> 1
    delta=4.250 -> 2
    delta=4.175 -> 1

All four were numerically valid, refining the finite-resolution transition bracket to

\[
4.175<\delta_*<4.250
\]

with width \(0.075\).

**Formal verdict:** TOPOLOGY_BRACKET_REFINED.

## B26.2

Using only the independently localized B26.1 topology bracket, B26.2 froze three new separations not previously simulated:

\[
\delta\in\{3.95,4.2125,4.35\},\qquad N\in\{384,448\}.
\]

All six trajectories passed the numerical validity gates. At \(N=448\), the representative-level primary contour counts were:

    delta=3.95   -> 1
    delta=4.2125 -> 1
    delta=4.35   -> 2

so the frozen topology gate was realized.

The fixed-coefficient predictor nevertheless had:

- median relative error: **42.91%**;
- maximum relative error: **44.79%**;
- median amplitude-aware comparator error: **27.29%**.

The resolution-pair \(|\Delta q|\) values were **0.0271**, **0.0212**, and **0.0142**, all within the frozen stability gate. The terminal failure is therefore not attributed to a failed topology gate or to the tested resolution-pair instability.

**Formal verdict:** AB_TOPOLOGY_STRADDLING_FIXED_COEFFICIENT_TRANSFER_FAIL.

The frozen terminal stop rule is triggered and B26 is closed.

## Supported statement

Within the tested finite-resolution canonical setting, the fixed perimeter coefficient that transferred prospectively across held-out ellipse shapes in B25.1e does **not** transfer with the required accuracy to the tested equal-injection two-center family. B26 therefore resolves a **geometry-transfer boundary** of that fixed-coefficient perimeter closure.

The result does not establish that topology change itself is the unique cause of failure: substantial error is already present on the connected side of the B26.2 family.

## Not established

B26 does not establish:

- a continuum theorem;
- a universal or source-independent perimeter law;
- that topology change alone causes the transfer failure;
- the B9 nonlocal term \(C(\Omega)\);
- the complete B9 energy \(E=\sigma P+\lambda C\);
- external physical validity.

The English Zenodo preprint is the authoritative academic version. A Japanese reference translation is included in the release.
