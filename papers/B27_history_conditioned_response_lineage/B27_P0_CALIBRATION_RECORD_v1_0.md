# BIG-B27-P0 Calibration Record v1.0

**Status:** CALIBRATION-ONLY / NON-CLAIM-BEARING  
**Date:** 2026-09-28  
**Purpose:** establish numerical executability before B27.1.  
**Claim use:** prohibited.

## 1. Inherited model constants

The calibration uses the published B16 baseline constants as the starting numerical scale:

- \(\phi_{\rm thr}=0.030\)
- \(D_0=0.12\)
- \(\phi_c=0.10\)
- \(\epsilon_D=0.010\)
- \(\gamma=0.0004\)
- \(\mu_0=0.11\)
- \(\alpha=0.01\)
- \(\beta=3.0\)
- \(D_m=0.006\)
- \(w_\phi=0.025\)

B27 uses the B16 history-susceptibility channel \(S_{\rm read}(1+\eta_Sm)\). During response-operator measurement, history writing is disabled.

## 2. P0 2D realization

The calibration-only 2D source is a compact polynomial disk,

\[
S_{\rm base}(r)=0.08\,(1-r^2/2^2)_+^2
\]

on \([-8,8]^2\), with zero-normal-flux finite-volume differencing.

The calibration write pulse is a Gaussian centered on the \(+x\) threshold boundary:
- amplitude \(0.035\)
- width \(0.35\)
- write duration \(0.8\)
- feedback disabled during writing
- rest duration \(1.0\)

The response probe uses an annular body-frame envelope with \(\sigma_r=0.18\), five modes
\[
l=0,\quad l=1_x,\quad l=1_y,\quad l=2_c,\quad l=2_s,
\]
and two symmetric finite-difference amplitudes \(h=0.002\) and \(h/2=0.001\).

Read horizon: \(T_{\rm read}=0.25\).

## 3. Successful calibration observations

These values are calibration diagnostics only.

### N = 80, dt = 0.005

After baseline formation and the write/rest protocol:

- \(\max\phi \approx 0.31713\)
- smooth support area \(\approx 19.7808\)
- smooth perimeter estimate \(\approx 15.0058\)
- \(\max m \approx 0.03709\)
- retained-history mass \(\approx 0.02110\)
- full-\(K\) two-probe-scale relative difference \(\approx 3.17\times10^{-3}\)

The history-freeback control at \(\eta_S=0\) reproduced the erased-history response operator to numerical precision in this pilot.

### N = 96, dt = 0.004

- \(\max\phi \approx 0.31911\)
- \(\max m \approx 0.03862\)
- smooth support area \(\approx 20.6232\)
- smooth perimeter estimate \(\approx 15.5287\)
- full-\(K\) two-probe-scale relative difference \(\approx 3.27\times10^{-3}\)

For the normalized response form after removing the perimeter channel, the two-probe-scale defect was approximately \(5.62\times10^{-5}\).

### N = 128, dt = 0.003

- \(\max\phi \approx 0.31948\)
- \(\max m \approx 0.04051\)
- smooth support area \(\approx 20.6542\)
- smooth perimeter estimate \(\approx 16.0319\)
- full-\(K\) two-probe-scale relative difference \(\approx 1.64\times10^{-3}\)
- normalized-form two-probe-scale defect without perimeter \(\approx 5.21\times10^{-5}\)

### N = 160, dt = 0.0025

- \(\max\phi \approx 0.31965\)
- \(\max m \approx 0.04087\)
- smooth support area \(\approx 20.6705\)
- smooth perimeter estimate \(\approx 16.1429\)
- full-\(K\) two-probe-scale relative difference \(\approx 1.43\times10^{-3}\)
- normalized-form two-probe-scale defect without perimeter \(\approx 3.73\times10^{-5}\)

## 4. Readout selection by numerical convergence only

Using all six candidate outputs, including the smooth perimeter estimate, the normalized response-form defect between \(N=128\) and \(N=160\) was about \(4.53\times10^{-2}\).

Removing the perimeter channel reduced the same defect to

\[
\varepsilon_{G,128\to160}\approx2.89\times10^{-3}.
\]

This P0 selection is based only on numerical convergence, not on kept-versus-erased effect size.

Therefore the B27.1 primary output vector is frozen as

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

The perimeter diagnostic remains secondary.

The frozen numerical response-form floor is conservatively rounded upward to

\[
\epsilon_{G,\rm num}=0.003.
\]

The corresponding three-floor resolved threshold is

\[
3\epsilon_{G,\rm num}=0.009.
\]

For the dimensionless response gain, the \(N=128\to160\) log-norm difference was approximately \(0.00435\); the frozen gain floor is rounded to \(0.005\), giving a three-floor resolved threshold \(0.015\).

## 5. P0 history-readout executability

A P0-only retained-versus-erased pilot was run only to verify that the measurement path is nondegenerate and that the zero-feedback control behaves correctly. These values are **not evidence for B27.1** and may not be cited as a B27.1 result.

At the published B16 high-feedback endpoint \(\eta_S=10\), the pilot normalized-form kept/erased separation was approximately \(0.0355\) at \(N=128\) and \(0.0357\) at \(N=160\). The cross-resolution difference of that pilot effect was small. These values are recorded solely for audit transparency; B27.1 uses new write angles.

## 6. P0 topology executability

A normalized two-center source family with fixed total source integral was tested in lower-resolution calibration only.

At both \(N=80\) and \(N=96\), after a 20-unit source-reconfiguration relaxation:

- \(\delta=5.25\) remained connected at the \(\phi=0.03\) threshold;
- \(\delta=5.50\) was disconnected.

Thus the selected 2D core is capable of controlled threshold-topology reconfiguration. These P0 cases are permanently excluded from B27.2 evidence.

A separate B27.2 predeclaration will require topology realization again at its own frozen claim resolutions before any covariance verdict is allowed.

## 7. P0 outcome

**P0_CALIBRATION_EXECUTABLE**

The following are frozen for B27.1:
- claim resolution pair \(N=\{128,160\}\);
- time steps \(0.003,0.0025\);
- primary probe scale \(h=0.001\);
- secondary probe scale \(h=0.002\);
- primary output vector without perimeter;
- \(\epsilon_{G,\rm num}=0.003\);
- gain-log numerical floor \(0.005\);
- read horizon \(0.25\);
- B16 high-feedback endpoint \(\eta_S=10\).

No B27.1 claim has been evaluated in P0.
