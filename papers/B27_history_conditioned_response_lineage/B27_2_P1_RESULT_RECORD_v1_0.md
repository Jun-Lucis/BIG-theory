# BIG-B27.2-P1 Result Record — Training Anchor Topology Gate Failure

**Protocol:** BIG_B27_2_P1_PRE_RECONFIGURATION_LINEAGE_ANCHOR_v1_0  
**Status:** COMPLETED / INVALID FOR COVARIANCE GATE FREEZE  
**Date:** 2026-09-28  
**Formal stage verdict:** \`P1_ANCHOR_TOPOLOGY_GATE_FAIL\`

## Frozen requirement

The P1 protocol required the pre-reconfiguration anchor at

\[
\delta_-=4.90
\]

to realize exactly one primary threshold component at both \(N=128\) and \(N=160\).

## Observed topology

The completed run returned:

| N | component count before write | component count at anchor |
|---:|---:|---:|
| 128 | 2 | 2 |
| 160 | 2 | 2 |

Therefore the frozen connected-anchor gate failed at both resolutions.

## Diagnostic numerical values

The run also produced finite response-lineage diagnostics, including a cross-resolution \(L_G\) defect of approximately \(0.00833\) and a mechanically computed provisional covariance gate of \(0.025\).

These quantities are **not adopted** as B27.2 covariance evidence or as the final B27.2 gate because the mandatory anchor-topology condition failed.

## Cause identified at protocol level

P0 topology calibration and P1 did not use the same branch-preparation path. P0 reached the two-center family by continuation from a pre-existing single-body state, whereas P1 initialized the two-center source directly from zero. The direct initialization selected a disconnected finite-resolution branch already at \(\delta=4.90\).

This is a design/branch-selection issue, not a failure of the B27.2 covariance hypothesis.

## Consequence

No post-reconfiguration target has been run.

Per the frozen P1 anti-rescue rule, B27.2 is redesigned under a new training-anchor substage before any target response is evaluated.

The failed P1 run remains archived and is never promoted to evidence.
