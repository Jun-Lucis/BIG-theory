# BIG-B27.1 Result Record — History-Conditioned Response Geometry

**Protocol:** BIG_B27_1_HISTORY_RESPONSE_GEOMETRY_v1_1  
**Status:** COMPLETED  
**Date:** 2026-09-28  
**Formal verdict:** \`HISTORY_RESPONSE_GEOMETRY_PASS\`

## Frozen question

Starting from the same saved boundary-carrying field \(\phi\), does retaining versus erasing the stored history field \(m\) change the normalized local response form

\[
G=\frac{K^\top K}{\operatorname{tr}(K^\top K)}
\]

beyond the predeclared numerical floor, while a zero-feedback control remains null?

The frozen structural gate was

\[
\Delta_G>0.009
\]

at **both** \(N=128\) and \(N=160\), for at least 3 of 4 held-out write angles. The numerical floor was \(0.003\).

## Held-out results

| write angle | \(\Delta_G\), N=128 | \(\Delta_G\), N=160 | structural gate |
|---:|---:|---:|:---:|
| 30° | 0.03569357 | 0.03595205 | PASS |
| 75° | 0.03522695 | 0.03592077 | PASS |
| 165° | 0.03522695 | 0.03592077 | PASS |
| 255° | 0.03522695 | 0.03592077 | PASS |

All four held-out angles exceeded the frozen structural threshold at both resolutions.

The fine-resolution mean was

\[
\overline{\Delta_G}_{N=160}=0.03592859,
\]

approximately \(3.99\times\) the frozen resolved threshold and \(11.98\times\) the numerical floor.

## Gain response

The retained-history branch also changed the absolute operator gain:

| write angle | \(\Delta_{\rm gain}\), N=128 | \(\Delta_{\rm gain}\), N=160 |
|---:|---:|---:|
| 30° | 0.02585909 | 0.02616262 |
| 75° | 0.02561486 | 0.02615833 |
| 165° | 0.02561486 | 0.02615833 |
| 255° | 0.02561486 | 0.02615833 |

However, because the normalized response form \(G\) itself changed beyond threshold, the result is **not** classified as gain-only.

## Null control

For every angle and both resolutions,

\[
\Delta_G(\eta_S=0)=0,
\qquad
\Delta_{\rm gain}(\eta_S=0)=0.
\]

Thus retained history by itself did not alter the measured response when the history-to-response feedback channel was disabled.

This is primarily an implementation/readout control, not independent evidence for the broader B27 hypothesis.

## Numerical validity

Two-probe-scale response-form defects were of order

\[
3.6\times10^{-5}\text{ to }5.2\times10^{-5},
\]

well below the frozen structural floor.

Cross-resolution response-form defects at \(N=160\) were:

- kept: \(0.00207\)–\(0.00257\);
- erased: \(0.00228\)–\(0.00243\);
- zero-feedback: \(0.00228\)–\(0.00243\).

All were below the frozen \(0.01\) cross-resolution validity gate. The machine-readable run reported \`valid_all=true\`.

## Frozen verdict

The protocol required structural separation in at least 3 of 4 held-out angles at both resolutions.

Observed:

\[
4/4
\]

held-out angles passed.

Therefore the frozen terminal verdict is

\[
\boxed{\texttt{HISTORY\_RESPONSE\_GEOMETRY\_PASS}}.
\]

## Interpretation

Within this finite reduced B27 model, two states with the **same instantaneous \(\phi\) field** but different retained-history states have measurably different local response geometry. The effect is not exhausted by one scalar gain factor because the normalized response form \(G\) also changes.

This supports the narrow B27.1 statement:

> Retained boundary history can condition the geometry of subsequent local response, not merely its overall amplitude, in the tested finite model.

It does **not** establish personal identity, subjective continuity, consciousness, AI personhood, or a universal law of individuality.

## Next stage

B27.2 may now test the distinct question of whether the history-conditioned response structure remains related across a controlled branch/topology reconfiguration through the predeclared geometry-only covariance map.

B27.1 parameters, thresholds, and verdict are frozen and must not be revised by B27.2 outcomes.
