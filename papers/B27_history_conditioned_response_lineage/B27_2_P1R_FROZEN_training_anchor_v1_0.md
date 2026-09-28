# BIG-B27.2-P1R Frozen Training-Anchor Protocol

## Continuation-Prepared Connected Lineage Anchor

**Status:** FROZEN BEFORE B27.2-P1R RUN  
**Protocol ID:** BIG_B27_2_P1R_CONTINUATION_ANCHOR_v1_0  
**Freeze date:** 2026-09-28  
**Role:** training/calibration side only; no post-reconfiguration target.

## 1. Reason for P1R

B27.2-P1 failed its mandatory topology gate because direct initialization of the two-center source at \(\delta=4.90\) produced two threshold components at both claim resolutions.

P1R changes only the **geometry branch-preparation path**. No post-reconfiguration target has been evaluated, no covariance outcome has been seen, and no target tolerance has been frozen.

## 2. Lineage object

The primary object remains unchanged:

\[
H_G=G_{\rm kept}-G_{\rm erased},
\qquad
L_G=\frac{H_G}{\|H_G\|_F}.
\]

The scalar \(\|H_G\|_F\) remains secondary lineage amplitude.

## 3. Frozen branch preparation

At each resolution:

1. initialize \(\phi=0,m=0\);
2. evolve under the single-center compact source for \(T=20\);
3. with feedback disabled and no history writing, switch to the normalized equal two-center source
   \[
   \delta_-=4.75,\qquad \theta_-=0^\circ
   \]
   and evolve for another \(T=20\);
4. require exactly one primary \(\phi>0.03\) component before any history write.

This continuation path is the only branch-preparation change from failed P1.

The value \(\delta_-=4.75\) was not used in P0 or failed P1.

## 4. Frozen history write

To avoid reusing the failed-P1 write direction, P1R uses the new body-frame ray

\[
\psi_{\rm write}=55^\circ.
\]

Inherited write parameters:

- Gaussian amplitude 0.035;
- width 0.35;
- write duration 0.8;
- feedback disabled during writing;
- rest duration 1.0;
- \(\alpha=0.01,\beta=3,D_m=0.006\);
- read feedback \(\eta_S=10\).

The anchor must remain one component after write/rest at both resolutions.

## 5. Response measurement

Unchanged from B27.1/P1:

- \(N=128,160\);
- \(dt=0.003,0.0025\);
- \(T_{\rm read}=0.25\);
- five probe modes \((l0,l1_x,l1_y,l2_c,l2_s)\);
- \(h=0.001\) primary, \(0.002\) secondary;
- \(Z=(A/A_0,c_x/R_0,c_y/R_0,q_1,q_2)\);
- no perimeter channel.

## 6. Mandatory P1R validity

P1R is valid only if:

1. component count = 1 before write at both resolutions;
2. component count = 1 at the response anchor at both resolutions;
3. retained history maximum \(>10^{-4}\);
4. finite response operators;
5. probe-scale \(G\) defects \(\le 0.001\);
6. branchwise cross-resolution \(G\) defects \(\le 0.01\);
7. \(H_G\) is informative.

If topology fails, stop again. No post target may be run.

## 7. Covariance-floor freeze rule

Only after all P1R validity gates pass, define

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

Then freeze

\[
\epsilon_{\rm cov,resolved}
=
3\epsilon_{\rm pre}
\]

rounded upward to the next \(10^{-3}\).

This tolerance is frozen before any post-reconfiguration response evaluation.

## 8. Anti-rescue

No post target is evaluated in P1R. After P1R, the post-target geometry, geometry-only map \(A\), topology gate, and verdict logic must be frozen before the first post response run.

Failed P1 numerical lineage values are not used to choose the P1R response definition or covariance tolerance.
