# BIG-B27.2-P1 Frozen Training-Anchor Protocol

## Pre-reconfiguration history-response lineage anchor

**Status:** FROZEN BEFORE B27.2-P1 TRAINING-ANCHOR RUN  
**Protocol ID:** BIG_B27_2_P1_PRE_RECONFIGURATION_LINEAGE_ANCHOR_v1_0  
**Freeze date:** 2026-09-28  
**Role:** non-terminal training/calibration side only; no post-reconfiguration target is evaluated here.

## 1. Purpose

B27.1 established prospectively that retained history changes the normalized response form \(G\) at identical present \(\phi\). The machine-readable B27.1 record reports \`HISTORY_RESPONSE_GEOMETRY_PASS\`, with all four held-out angles structural and all mandatory validity gates satisfied.

B27.2 asks a harder question: whether the **history-induced part of response geometry** can be tracked across topology reconfiguration without fitting the post-reconfiguration outcome.

To prevent a post-hoc covariance tolerance, B27.2 begins with a pre-target training-anchor stage. P1 measures only the connected pre-reconfiguration anchor. It does not evaluate any disconnected post-reconfiguration response.

## 2. Primary lineage object

For one common present \(\phi\), define

\[
G_{\rm kept}
=
\frac{K_{\rm kept}^{\top}K_{\rm kept}}
{\operatorname{tr}(K_{\rm kept}^{\top}K_{\rm kept})},
\qquad
G_{\rm erased}
=
\frac{K_{\rm erased}^{\top}K_{\rm erased}}
{\operatorname{tr}(K_{\rm erased}^{\top}K_{\rm erased})}.
\]

The history-induced response deformation is

\[
H_G
=
G_{\rm kept}-G_{\rm erased}.
\]

Provided \(\|H_G\|_F\) is informative, define the normalized lineage form

\[
L_G
=
\frac{H_G}{\|H_G\|_F}.
\]

B27.2 will prospectively test the orientation/shape of \(L_G\) across reconfiguration, while recording \(\|H_G\|_F\) separately as lineage amplitude.

This choice isolates the part of response geometry caused by readable retained history rather than the background response geometry of the current shape.

## 3. Frozen P1 pre-anchor

The source family is the normalized equal two-center compact-polynomial family used only as a geometry generator.

Pre-anchor geometry:

\[
\delta_- = 4.90,\qquad \theta_-=0^\circ.
\]

This value was not used in P0 topology calibration.

The source is evolved from zero initial \(\phi\) for the inherited baseline time \(T=20\). The pre-anchor is valid only if the threshold set \(\phi>0.03\) has exactly one primary connected component at both \(N=128\) and \(N=160\).

## 4. Frozen history write

A single local Gaussian write pulse is centered at the outward \(\phi=0.03\) threshold crossing along the body-frame ray

\[
\psi_{\rm write}=40^\circ.
\]

Parameters are inherited unchanged from B27.1:

- amplitude 0.035;
- width 0.35;
- write duration 0.8;
- feedback disabled during writing;
- rest duration 1.0;
- \(\alpha=0.01\), \(\beta=3\), \(D_m=0.006\);
- read feedback \(\eta_S=10\).

The 40° write ray was not used in P0 or B27.1.

## 5. Frozen response measurement

Resolutions:

\[
N=128,\qquad N=160.
\]

Time steps:

\[
dt_{128}=0.003,\qquad dt_{160}=0.0025.
\]

Read horizon: \(T_{\rm read}=0.25\).

Probe basis:

\[
(l=0,l=1_x,l=1_y,l=2_c,l=2_s).
\]

Primary/secondary probe amplitudes:

\[
h=0.001,\qquad 0.002.
\]

Primary readout remains

\[
Z=(A/A_0,c_x/R_0,c_y/R_0,q_1,q_2).
\]

No perimeter channel may be restored.

## 6. P1 numerical outputs

P1 records:

- topology component count at each resolution;
- retained-history maximum and mass;
- \(G_{\rm kept}\), \(G_{\rm erased}\);
- \(H_G\), \(\|H_G\|_F\), \(L_G\);
- two-probe-scale defects of \(G\) and \(L_G\);
- cross-resolution defects of \(G_{\rm kept}\), \(G_{\rm erased}\), and \(L_G\);
- zero-feedback control.

P1 also saves the fine-resolution \(L_G^-\) matrix and its SHA-256 hash for later prediction freeze.

## 7. Gate-freeze rule for B27.2

P1 may determine only a **numerical covariance floor**. It may not evaluate any post-reconfiguration target.

Let

\[
\epsilon_{\rm pre}
=
\max\{
\epsilon_{L,\rm probe}^{128},
\epsilon_{L,\rm probe}^{160},
\epsilon_{L,\rm cross-res},
0.003
\}.
\]

After P1, the B27.2 primary covariance tolerance will be frozen at

\[
\epsilon_{\rm cov,resolved}=3\,\epsilon_{\rm pre}
\]

rounded upward to the next \(10^{-3}\).

The floor must be fixed before any B27.2 post-reconfiguration response operator is evaluated.

## 8. Anti-rescue

P1 is training/calibration only. After a post-target protocol is frozen:

- no new lineage definition;
- no replacement of \(L_G\) by absolute \(G\);
- no post-target scalar fit;
- no response-derived rotation;
- no target-dependent change of source separation, rotation angle, history write, probe basis, readout, or tolerance;
- no reuse of P0 topology cases as B27.2 evidence.

If P1 cannot produce an informative and numerically stable \(L_G^-\), B27.2 is redesigned under a new substage before any target run. No post target is run under an invalid anchor.
