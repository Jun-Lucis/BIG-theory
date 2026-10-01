# BIG Later-Phase Research Status — B27 through B36

**Date:** 2026-09-30  
**Scope:** later-phase update following the B3–B26 integrated status map

This document records the retained status of BIG-B27 through BIG-B36. Earlier formal verdicts are not regraded by later stages.

## B27 — history-conditioned response geometry and reconfiguration

B27 closed with two distinct results.

- **B27.1:** `HISTORY_RESPONSE_GEOMETRY_PASS`
- **B27.2:** `RECONFIGURATION_COVARIANCE_FAIL`

At identical present `phi`, retained readable history changed normalized local response geometry in the tested reduced model. However, after controlled connected-to-disconnected reconfiguration, the frozen identity covariance map failed on all three valid prospective targets.

B27 therefore supports:

```text
history-conditioned response
    !=
reconfiguration-invariant response lineage
```

The valid B27.2 failure closed B27 under its stop rule; B27.3 was not run.

## B28 — geometry-conditioned lineage transport

B28 replaced the failed identity-covariance hypothesis with a geometry-only component-resolved 1-to-2 split transport.

After calibration stages, B28.1 was run prospectively on fresh split targets

[
delta_{m post}=5.3, 5.6, 5.9.
]

All three targets were numerically valid, but their lineage-transport defects were approximately

[
0.15334,quad 0.15247,quad 0.15644,
]

well above the frozen PASS threshold

[
epsilon_{m split}le 0.009.
]

Formal verdict:

`GEOMETRY_CONDITIONED_LINEAGE_TRANSPORT_FAIL`

Because B28.1 validly failed, B28.2 was not opened under the frozen rule.

## B29 — incremental predictive information beyond instantaneous geometry

B29 was closed **before any B29.1 held-out evaluation**.

B29-P0 established a response-blind 36-case grid and a frozen 27-training / 9-held-out split. B29-T1 then found only

[
18/27
]

training cases valid under the inherited readability and numerical-validity gates.

The terminal training status was

`T1_valid=False`.

All training cases at relative history-write angles (25^circ) and (55^circ) were valid, whereas all cases at (85^circ) failed the frozen response-readability gate. This angular concentration was treated as hypothesis-generating only.

No held-out prediction set was frozen, no held-out post-response was evaluated, and no predictive verdict for M0/M1/M2 was issued. The correct terminal interpretation is that the frozen B29 training domain was not uniformly response-readable.

**Integrated B28–B29 Zenodo record:** https://doi.org/10.5281/zenodo.23050390

The integrated record preserves the B28 prospective FAIL and the B29 pre-held-out closure as distinct outcomes; it does not reinterpret `T1_valid=False` as a predictive-performance FAIL.

## B30–B36 — integrated response-to-timing programme

The B30–B36 sequence was later integrated into one preprint:

**From History-Conditioned Boundary Response to Geometry-Conditioned Pulse Timing in a Finite Reduced Model**

DOI: https://doi.org/10.5281/zenodo.23048197

The retained claim-bearing verdicts are:

| Stage | Retained verdict |
| --- | --- |
| B30.1 | `TRANSVERSE_HISTORY_RESPONSE_SUPPRESSION_PASS` |
| B31.1 | `REFLECTION_PARITY_MODE_PASS` |
| B32.1 | `DYNAMIC_COMPLEX_PARITY_MODE_FAIL` |
| B33 primary | `FREQUENCY_DEPENDENT_TRANSVERSE_NODE_LIFTING_PASS` |
| B33 second grid | `PERIOD_DEPENDENT_TRANSVERSE_NODE_LIFTING_PASS` |
| B34.1 | `SPATIALLY_STRUCTURED_COMPLEX_TRANSFER_KERNEL_PASS` |
| B35.1 | `DISTANCE_ORDERED_APPROX_LINEAR_PEAK_TIMING_FAIL` |
| B35.2 | `HIGHER_RESOLUTION_SAMPLING_STABLE_APPROX_LINEAR_PEAK_TIMING_FAIL` |
| B36.1 | `GEOMETRY_CONDITIONED_PEAK_TIMING_ORDERING_FAIL` |
| B36.2 | `ADDITIVE_GEOMETRY_SAMPLING_DECOMPOSITION_PASS` |

The sequence should not be read as a monotone chain of successes. B32.1, B35.1, B35.2, and B36.1 remain formal FAILs.

The terminal B36.2 result supports only the following narrow statement:

> Within the tested fresh finite numerical grid, the fitted peak-timing slope admits an approximately additive decomposition into a geometry-conditioned component and a readout-sampling component, while geometry ordering is preserved across the tested sampling shifts.

For the fresh B36.2 grid, all twelve lattice cells passed, the geometry row-mean span was (0.00690625), the interaction fraction was (0.0786605le0.20), and the normalized maximum interaction was (0.0503345le0.10).

This does **not** establish a universal quantitative (b(q)) law, sampling-invariant absolute slope, physical propagation speed, ballistic transport, finite-speed propagation, a propagating or standing wave, a wave equation, resonance, or a dispersion relation.

## Integrated later-phase interpretation

The retained B27–B36 sequence is:

```text
history-conditioned response
    -> failed simple reconfiguration covariance
    -> failed geometry-only lineage transport
    -> training-domain readability boundary
    -> transverse suppression and reflection parity
    -> dynamic suppression FAIL
    -> period-dependent soft-node lifting
    -> spatial complex transfer kernel
    -> structured pulse timing but no common stable linear law
    -> approximate geometry/readout decomposition on a fresh finite grid
```

The methodological point is as important as the positive results: negative prospective tests are retained and used to narrow later questions rather than being retroactively repaired.
