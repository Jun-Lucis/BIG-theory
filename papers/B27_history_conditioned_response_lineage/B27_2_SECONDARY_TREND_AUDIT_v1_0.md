# BIG-B27.2 Secondary Trend Audit

**Status:** descriptive audit of completed B27.2 data; no new claim-bearing computation  
**Date:** 2026-09-29

## Purpose

This note summarizes secondary structure already present in the frozen B27.2 result. It does not alter the terminal verdict.

## Distance from the frozen covariance gates

The frozen PASS gate was 0.010 and the frozen PARTIAL ceiling was 0.030.

| target | epsilon_target | / PASS gate | / PARTIAL ceiling |
|---|---:|---:|---:|
| T1 | 0.1118248844 | 11.18 | 3.73 |
| T2 | 0.1276381141 | 12.76 | 4.25 |
| T3 | 0.1450767448 | 14.51 | 4.84 |

The failure is therefore not marginal.

## Numerical-separation check

The post-target cross-resolution lineage defects were approximately:

- T1: 0.000860;
- T2: 0.000827;
- T3: 0.000825.

These are about two orders of magnitude smaller than the corresponding pre/post lineage defects, so the terminal failure is not explained by the measured cross-resolution mismatch.

## History effect after reconfiguration

The history-induced response remained measurable after the topology change. The post/pre H_G norm ratios decreased across the frozen targets:

- T1: approximately 0.370;
- T2: approximately 0.364;
- T3: approximately 0.351.

The normalized lineage defect increased monotonically:

[
0.1118 ightarrow 0.1276 ightarrow 0.1451.
]

With only three frozen targets, this monotone pattern is descriptive and must not be promoted to a fitted law.

## Interpretation for programme design

The completed data separate two effects:

1. readable history continues to affect post-reconfiguration response;
2. the normalized geometry of that history-induced response changes strongly.

This is precisely why a future B28 should test a **predictable transport/transition law** rather than reusing the failed invariance hypothesis.

No response-derived transport map is fitted in this note.
