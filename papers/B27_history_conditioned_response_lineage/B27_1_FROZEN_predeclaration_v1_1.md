# BIG-B27.1 Frozen Predeclaration v1.1

## History-Conditioned Response Geometry at Identical Present \(\phi\)

**Status:** FROZEN BEFORE FIRST HELD-OUT B27.1 TRAJECTORY  
**Protocol ID:** BIG_B27_1_HISTORY_RESPONSE_GEOMETRY_v1_1  
**Freeze date:** 2026-09-28

**Supersession note:** v1.1 tightens only the pre-run verdict/validity logic and adds Drive/checkpoint persistence. No B27.1 held-out trajectory had been run when this version was frozen. The dynamical model, held-out angles, probe basis, history protocol, read horizon, and effect thresholds are unchanged from v1.0.

## Primary question

Given the exact same present boundary-carrying field \(\phi\), does retained history \(m\) change the local boundary-response geometry beyond frozen numerical uncertainty?

For each held-out write angle, construct from the same saved \(\phi\) snapshot:

\[
X_{\rm kept}=(\phi,m,q),\qquad
X_{\rm erased}=(\phi,0,q),
\]

and the null-readability control

\[
X_{\eta=0}=(\phi,m,q;\eta_S=0).
\]

## Held-out cases

The P0 write angle \(0^\circ\) is excluded. Frozen B27.1 angles:

\[
30^\circ,\quad 75^\circ,\quad 165^\circ,\quad 255^\circ.
\]

Resolutions:

\[
N=128,\quad N=160.
\]

No held-out angle may be replaced after execution begins.

## Frozen operator and readout

Probe space: five modes \((l=0,l=1_x,l=1_y,l=2_c,l=2_s)\).

Primary probe amplitude \(h=0.001\); secondary numerical-stability amplitude \(h=0.002\).

Primary readout:

\[
Z=(A/A_0,c_x/R_0,c_y/R_0,q_1,q_2).
\]

The local finite-window response operator is

\[
K=D_a\mathcal R_T|_{a=0},
\]

and the normalized response pullback form is

\[
G=\frac{K^\top K}{\operatorname{tr}(K^\top K)}.
\]

The structural history effect is

\[
\Delta_G=
\frac{\|G_{\rm kept}-G_{\rm erased}\|_F}
{\|G_{\rm kept}\|_F+\|G_{\rm erased}\|_F}.
\]

The gain effect is

\[
\Delta_{\rm gain}
=
\left|
\log\frac{\|K_{\rm kept}\|_F}{\|K_{\rm erased}\|_F}
\right|.
\]

## Frozen numerical gates

- \(G\) numerical floor: 0.003
- resolved structural threshold: \(\Delta_G>0.009\)
- log-gain numerical floor: 0.005
- resolved gain threshold: \(\Delta_{\rm gain}>0.015\)
- maximum within-resolution probe-scale \(G\) defect: 0.001
- maximum branchwise cross-resolution \(G\) defect: 0.01
- minimum retained-history maximum: \(10^{-4}\)

The \(\eta_S=0\) null-control defects must remain below the numerical floors:

\[
\Delta_{G,\eta=0}\le0.003,\qquad
\Delta_{{\rm gain},\eta=0}\le0.005.
\]

## Frozen verdict logic

An angle counts as a structural history-response angle only if \(\Delta_G>0.009\) at both \(N=128\) and \(N=160\).

An angle counts as gain-only only if \(\Delta_{\rm gain}>0.015\) at both resolutions while \(\Delta_G\le0.009\) at both resolutions.

If any mandatory numerical validity gate fails, the stage is INCONCLUSIVE.

Otherwise:

- at least 3 of 4 structural angles -> HISTORY_RESPONSE_GEOMETRY_PASS
- otherwise at least 3 of 4 gain-only angles -> HISTORY_GAIN_ONLY
- otherwise -> HISTORY_CONDITIONING_NOT_SUPPORTED

## Interpretation boundary

A PASS means only that, in this finite reduced model and frozen protocol, retained history changes the measured local response geometry even when the present \(\phi\) field is held exactly fixed at intervention time.

It does not establish personal identity, subjective continuity, consciousness, AI individuality, or a universal law of individuation.

## Anti-rescue

After the first held-out angle starts: no angle replacement, probe-basis replacement, \(\eta_S\) change, readout addition, threshold relaxation, read-horizon change, coefficient refit, P0 promotion, or invalid-case replacement.
