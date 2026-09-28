# BIG-B27.1 Frozen Predeclaration v1.0

## Same-Current-Geometry Test of History-Conditioned Response Geometry

**Status:** FROZEN BEFORE ANY B27.1 CLAIM-BEARING TRAJECTORY  
**Protocol ID:** BIG_B27_1_HISTORY_RESPONSE_GEOMETRY_v1_0  
**Date frozen:** 2026-09-28  
**Parent:** BIG-B27.0 frozen architecture; BIG-B27-P0 calibration record.

---

## 1. Question

Starting from exactly the same present \(\phi\) field, does retaining versus erasing a previously written boundary-history field \(m\) change the local response geometry beyond frozen numerical uncertainty?

B27.1 tests a finite reduced response operator. It does not test personal identity, consciousness, subjective continuity, or AI personhood.

---

## 2. Frozen equations and parameters

The model is the B16-aligned 2D history-feedback realization frozen in B27.0/P0.

Inherited constants:
\[
\phi_{\rm thr}=0.030,\quad
D_0=0.12,\quad
\phi_c=0.10,\quad
\epsilon_D=0.010,
\]
\[
\gamma=0.0004,\quad
\mu_0=0.11,\quad
\alpha=0.01,\quad
\beta=3.0,\quad
D_m=0.006,\quad
w_\phi=0.025.
\]

History feedback during the read phase:
\[
\eta_S=10.
\]

Domain and base source:
\[
(x,y)\in[-8,8]^2,
\]
\[
S_{\rm base}(r)=0.08(1-r^2/2^2)_+^2.
\]

Resolution pair:
- \(N=128,\ \Delta t=0.003\)
- \(N=160,\ \Delta t=0.0025\)

Baseline formation time:
\[
T_{\rm base}=20.
\]

---

## 3. Frozen history-writing protocols

Each claim-bearing history state is written by one Gaussian pulse centered on the current threshold boundary at a held-out angle \(\theta\).

Pulse:
- amplitude \(0.035\)
- spatial width \(0.35\)
- duration \(0.8\)
- feedback disabled during writing
- B16 boundary mask writes \(m\)
- rest duration after write \(1.0\)

The four held-out write angles are

\[
\boxed{
\theta\in\{30^\circ,75^\circ,165^\circ,255^\circ\}.
}
\]

The P0 angle \(0^\circ\) is forbidden as B27.1 evidence.

No replacement angle is permitted if a claim-bearing angle is inconvenient or unfavorable.

---

## 4. Same-\(\phi\) intervention

Immediately before the read phase, save one \(\phi\) snapshot and its retained \(m\).

From that exact same \(\phi\), create:

\[
X_{\rm kept}=(\phi,m,q),
\]

\[
X_{\rm erased}=(\phi,0,q),
\]

and

\[
X_{\eta=0}=(\phi,m,q;\eta_S=0\ {\rm during\ read}).
\]

Thus any kept-versus-erased difference begins from identical present geometry.

During the read phase:
\[
\beta_{\rm read}=0.
\]

The response probes are not allowed to write new history.

---

## 5. Frozen probe basis

In normalized body-centered coordinates
\[
\xi=(x-c_x)/R,\qquad
\upsilon=(y-c_y)/R,
\]
use an annular envelope
\[
w=\exp[-(\sqrt{\xi^2+\upsilon^2}-1)^2/(2\sigma_r^2)],
\qquad
\sigma_r=0.18.
\]

The five modes are
\[
u_0=w,\quad
u_x=\xi w,\quad
u_y=\upsilon w,
\]
\[
u_{2c}=(\xi^2-\upsilon^2)w,\quad
u_{2s}=2\xi\upsilon w.
\]

Each discrete mode is normalized to maximum absolute value one.

Probe amplitudes:
\[
h_1=0.002,\qquad h_2=0.001.
\]

Primary operator: \(h_2\).  
\(h_1\) is a numerical stability check.

Read horizon:
\[
T_{\rm read}=0.25.
\]

---

## 6. Frozen primary readout

Using a smooth threshold
\[
H_\epsilon(\phi-\phi_{\rm thr})
=
\left[
1+\exp\left(-\frac{\phi-\phi_{\rm thr}}{0.004}\right)
\right]^{-1},
\]
compute anchor area \(A_0\), center \(c\), and \(R_0=\sqrt{A_0/\pi}\).

The primary output is

\[
Z=
\left(
A/A_0,\;
c_x/R_0,\;
c_y/R_0,\;
q_1,\;
q_2
\right).
\]

The perimeter channel is excluded from the primary response operator because P0 found materially poorer cross-resolution convergence. It may be recorded only as a secondary diagnostic.

---

## 7. Local response operator and response form

For each branch and probe mode:

\[
K
=
D_a\mathcal R_T|_{a=0}
\]

is estimated by symmetric finite differences.

Define

\[
G=\frac{K^\top K}{\operatorname{tr}(K^\top K)}.
\]

The primary history-geometry separation is

\[
\Delta_G
=
\frac{\|G_{\rm kept}-G_{\rm erased}\|_F}
{\|G_{\rm kept}\|_F+\|G_{\rm erased}\|_F}.
\]

The gain diagnostic is

\[
\Delta_{\rm gain}
=
\left|
\log
\frac{\|K_{\rm kept}\|_F}
{\|K_{\rm erased}\|_F}
\right|.
\]

Zero-feedback controls use the same quantities against the erased branch.

---

## 8. Frozen numerical gates

P0 numerical floors:

\[
\epsilon_{G,\rm num}=0.003,
\qquad
\epsilon_{{\rm gain},\rm num}=0.005.
\]

Resolved thresholds:

\[
\boxed{\Delta_G>0.009}
\]

and

\[
\boxed{\Delta_{\rm gain}>0.015}.
\]

Per-angle validity additionally requires:

1. finite solver completion;
2. response-form trace above machine-noise floor;
3. primary \(h_2\) operator finite;
4. two-probe-scale response-form defect
\[
\varepsilon_{G,h}\le0.001;
\]
5. coarse/fine \(N=128\to160\) primary response-form comparison not exceeding
\[
0.01
\]
for the corresponding branch;
6. nondegenerate written history:
\[
\max m>10^{-4};
\]
7. zero-feedback control does not itself exceed the resolved structural threshold.

No failed/invalid angle may be replaced.

---

## 9. Frozen verdict logic

All four held-out angle families must produce valid fine-resolution kept/erased/control operators. Otherwise the stage is \`INCONCLUSIVE\`, unless a common numerical implementation failure prevents evaluation, in which case it is \`IMPLEMENTATION_INVALID\`.

### HISTORY_RESPONSE_GEOMETRY_PASS

Require:

- at least 3 of 4 held-out angles have
\[
\Delta_G>0.009
\]
at \(N=160\);
- the same angles remain directionally consistent at \(N=128\);
- all zero-feedback controls satisfy
\[
\Delta_{G,\eta=0}\le0.009.
\]

### HISTORY_GAIN_ONLY

If \`HISTORY_RESPONSE_GEOMETRY_PASS\` is not met, but at least 3 of 4 angles have

\[
\Delta_{\rm gain}>0.015
\]

with zero-feedback gain controls not exceeding \(0.015\), classify \`HISTORY_GAIN_ONLY\`.

### HISTORY_CONDITIONING_NOT_SUPPORTED

If all four angle families are valid and neither structural nor gain-only conditions are met, classify

\`HISTORY_CONDITIONING_NOT_SUPPORTED\`.

No post-hoc weaker PASS category is permitted.

---

## 10. Anti-rescue and stop rule

After the first B27.1 held-out angle is evaluated:

- no change of write amplitude, width, duration, or rest time;
- no change of \(\eta_S\);
- no replacement or rotation of the held-out angle set;
- no replacement probe basis;
- no addition of perimeter or history variables to primary \(Z\);
- no change of read horizon;
- no relaxation of numerical or verdict gates.

B27.1 terminates after the four frozen angle families are evaluated.

If B27.1 validly returns \`HISTORY_CONDITIONING_NOT_SUPPORTED\`, later B27 stages may study geometry covariance only as a separate structural question; they may not claim a history-conditioned response lineage.

---

## 11. Claim boundary

A B27.1 PASS means only that, in this frozen finite reduced model, retained boundary history changes the measured local response form from the same present \(\phi\) state beyond the frozen numerical floor.

It does not establish a universal law of individuality or a theorem of identity.
