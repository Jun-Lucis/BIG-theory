# BIG-B30–B36 — Integrated Response-to-Pulse-Timing Programme

**Integrated preprint DOI:** https://doi.org/10.5281/zenodo.23048197

**Title:** *From History-Conditioned Boundary Response to Geometry-Conditioned Pulse Timing in a Finite Reduced Model*

B30–B36 form a linked sequence of prospectively frozen finite-model tests. The sequence moves from history-conditioned angular response geometry to localized harmonic transfer, single-pulse timing, and a fresh geometry-by-readout decomposition test.

## Retained verdict ledger

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

Earlier FAILs remain FAILs. B33 does not regrade B32; B35A does not regrade B35.1; B36A does not regrade B36.1; and B36.2 asks a new prospectively frozen question.

## Evidence chain

```text
history-conditioned transverse suppression
    -> reflection parity
    -> complex periodic response (formal FAIL)
    -> period-dependent soft-node lifting
    -> spatial complex transfer kernel
    -> distance-dependent pulse timing
    -> no common orientation-independent sampling-stable linear timing law
    -> approximate geometry/readout decomposition on a fresh finite grid
```

## Terminal supported statement

B36.2 supports only the following finite-grid statement:

> Within the tested fresh finite numerical grid, the fitted peak-timing slope admits an approximately additive decomposition into a geometry-conditioned component and a readout-sampling component, while geometry ordering is preserved across the tested sampling shifts.

The terminal PASS does not establish a universal (b(q)) law, sampling-invariant absolute slope, physical propagation speed, ballistic transport, finite-speed propagation, a propagating or standing wave, a wave equation, resonance, or a dispersion relation.

## Numerical implementation note

The B30–B36 reduced model uses the implemented directional component-wise cubic flux

[
partial_x[gamma(partial_xphi)^3]
+
partial_y[gamma(partial_yphi)^3],
]

not an isotropic replacement (
ablacdot(gamma|
ablaphi|^2
ablaphi)).

## Archive

The authoritative English preprint, Japanese reference translation, and reproducibility package are archived at Zenodo under DOI:

https://doi.org/10.5281/zenodo.23048197

See also: [B27–B36 later-phase status](../../docs/research_status_update_B27_B36.md).
