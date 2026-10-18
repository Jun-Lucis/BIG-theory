# BIG-B33 Output-Collision Recovery Audit v1.0

**Date:** 2026-09-29

The shared Drive checkpoint contained **384** records because two distinct, already-computed
protocol grids wrote to the same `B33_1_OUTPUT/B33_1_checkpoint.json`.

- Pre-existing grid: **216 records**
- Current frozen grid: **168 records**
- Total: **384 records**

The current frozen grid is uniquely identified by:

- N=128 source orientations: 27°, 51°, 73°
- relative angles: 60°, 90°, 120°
- target periods: 0.60, 1.10, 1.60, 1.90
- N=160 verification: theta=51°, periods 0.60 and 1.90

Exactly 168 unique records match this grid. No response recomputation is required.

The pre-existing 216 records are not deleted or reinterpreted. They belong to an earlier B33.1
protocol and must remain a separate result.

Applying only the already-frozen current protocol rules to the recovered 168 records gives:

`PERIOD_DEPENDENT_TRANSVERSE_NODE_LIFTING_PASS`

This administrative recovery does not alter any scientific threshold or criterion.
