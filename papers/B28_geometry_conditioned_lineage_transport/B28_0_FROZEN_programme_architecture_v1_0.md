# BIG-B28 — Geometry-Conditioned Response-Lineage Transport

**Status:** FROZEN PROGRAMME ARCHITECTURE / NO CLAIM-BEARING B28 TRAJECTORY YET  
**Architecture ID:** BIG_B28_GEOMETRY_CONDITIONED_LINEAGE_TRANSPORT_v1_0  
**Freeze date:** 2026-09-29

## 1. Motivation

B27 established two distinct finite-model results:

1. retained readable history changed local response geometry at identical present \(\phi\);
2. the normalized history-induced response form did not remain invariant across the tested connected-to-disconnected topology reconfiguration under the frozen identity map.

B28 therefore does **not** ask whether one lineage form is invariant.

It asks:

> Can the transformation of history-induced response structure across a 1-to-2 topology split be predicted from the geometry of the split, without fitting the held-out post-response?

This is a new hypothesis and is not a rescue or regrading of B27.

## 2. Primary strategy: component-resolved split transport

A one-component pre-state and a two-component post-state do not naturally share the same global five-mode representation.

B28 therefore uses

\[
\mathcal P^- \simeq \mathbb R^5
\]

before the split and

\[
\mathcal P^+ \simeq \mathbb R^5\oplus\mathbb R^5
\]

after the split.

The post state is represented by two child-local five-mode probe spaces.

## 3. Frozen pre probe basis

For the connected pre-state, use the same normalized low-order basis family as B27:

\[
u_0=w,\quad
u_x=\xi_x w,\quad
u_y=\xi_y w,\quad
u_{2c}=(\xi_x^2-\xi_y^2)w,\quad
u_{2s}=2\xi_x\xi_yw,
\]

with body-centered normalized coordinates

\[
\xi=(x-c^-)/R^-.
\]

## 4. Post component identification

At a valid split anchor, the threshold set

\[
\{\phi>\phi_{\rm thr}\}
\]

must contain exactly two primary components at both claim resolutions.

The two components are ordered deterministically by projection of their centroids onto the frozen source axis. No response value is used in component ordering.

For each component \(j\in\{1,2\}\), record geometry-only anchor data

\[
(c_j^+,R_j^+).
\]

## 5. Frozen post component-resolved basis

Each child receives its own five-mode basis

\[
v_{j,0},\;
v_{j,x},\;
v_{j,y},\;
v_{j,2c},\;
v_{j,2s}
\]

in local normalized coordinates

\[
\zeta_j=(x-c_j^+)/R_j^+.
\]

The child basis is multiplied by a frozen smooth geometry-only partition of unity \(p_j(x)\), derived only from child centers and radii.

Thus the post probe space is ten-dimensional.

## 6. Geometry-only split operator

Let \(U^-\) denote the sampled pre probe fields and \(U^+\) the sampled ten child-resolved post probe fields.

Define a geometry-only weighted least-squares split operator

\[
S_\Gamma:\mathbb R^5\rightarrow\mathbb R^{10}
\]

by

\[
S_\Gamma
=
\arg\min_S
\left\|
W_\Gamma^{1/2}
\left(
U^+S-U^-
\right)
\right\|_F^2
+
\lambda_{\rm reg}\|S\|_F^2.
\]

The weight \(W_\Gamma\) is a frozen post-boundary geometry weight. The regularizer is fixed numerically from geometry only.

No kept/erased response, \(K\), \(G\), \(H_G\), or \(L_G\) may enter construction of \(S_\Gamma\).

## 7. Response operators

Pre-state response operator:

\[
K_b^-:\mathbb R^5\to\mathbb R^5,
\]

where \(b\in\{\mathrm{kept},\mathrm{erased}\}\).

Post-state component-resolved response operator:

\[
K_b^+:\mathbb R^{10}\to\mathbb R^{10}.
\]

The post operator is pulled back to the pre probe space using only the frozen geometry map:

\[
\bar K_b^+
=
K_b^+S_\Gamma.
\]

## 8. Response forms and lineage

Define

\[
G_b^-
=
\frac{(K_b^-)^\top K_b^-}
{\operatorname{tr}[(K_b^-)^\top K_b^-]},
\]

and

\[
\bar G_b^+
=
\frac{(\bar K_b^+)^\top\bar K_b^+}
{\operatorname{tr}[(\bar K_b^+)^\top\bar K_b^+]}.
\]

History-induced deformations:

\[
H_G^-=G_{\rm kept}^- - G_{\rm erased}^-,
\]

\[
H_G^+=\bar G_{\rm kept}^+ - \bar G_{\rm erased}^+.
\]

Normalized lineage forms:

\[
L_G^-=\frac{H_G^-}{\|H_G^-\|_F},
\qquad
L_G^+=\frac{H_G^+}{\|H_G^+\|_F}.
\]

Primary transport defect:

\[
\epsilon_{\rm split}
=
\frac{\|L_G^+-L_G^-\|_F}
{\|L_G^+\|_F+\|L_G^-\|_F}.
\]

The amplitude ratio

\[
\|H_G^+\|_F/\|H_G^-\|_F
\]

is secondary and does not replace the primary normalized-form test.

## 9. Component-resolved post readout

At the post anchor, each child has a frozen smooth partition \(p_j\). The response readout contains, for each child,

\[
Z_j=
\left(
A_j/A_{j,0},
\Delta c_{j,x}/R_{j,0},
\Delta c_{j,y}/R_{j,0},
q_{j,1},
q_{j,2}
\right).
\]

The combined post readout is

\[
Z^+=(Z_1,Z_2)\in\mathbb R^{10}.
\]

The partition and anchor normalizations are frozen before response probes are applied.

## 10. B28 stages

### B28-P0 — calibration firewall

Non-claim-bearing only.

P0 may determine:

- a fresh rotated two-center geometry family;
- connected and split calibration anchors;
- stable resolution pair and time-step pair;
- component extraction and ordering rules;
- soft partition scale;
- split-map regularization;
- probe-scale stability;
- geometry-projection reconstruction error;
- numerical uncertainty floors.

P0 cases may never become claim-bearing evidence.

### B28.1 — prospective within-family split transport

After P0, freeze a set of **new** split targets from the same geometry family, excluding all P0 values.

The split operator for each target is computed from that target geometry alone, before any response operator is evaluated.

B28.1 tests whether component-resolved geometry-only transport predicts history-induced response lineage within that family.

### B28.2 — held-out family transfer

B28.2 is run only if B28.1 survives its frozen terminal criterion.

A distinct held-out geometry family is frozen before any B28.2 response trajectory. No transport coefficient or response-derived correction is refit.

## 11. Firewall against B27 reuse

B27 T1-T3 are archived negative evidence and are not B28 held-out confirmation.

B27 data may motivate the B28 representation and provide scale intuition, but:

- no B27 target may be relabeled as B28 evidence;
- no B28 threshold is chosen to make B27 targets pass;
- no B27 response value may fit \(S_\Gamma\).

## 12. Anti-rescue

After the first B28.1 claim-bearing target begins:

- no replacement of the component-resolved representation;
- no response-derived modification of \(S_\Gamma\);
- no change of primary readout;
- no target-dependent response rescaling;
- no threshold relaxation;
- no invalid-target replacement;
- no promotion of P0 cases to evidence.

A failed B28.1 transport map may motivate a new B-series, but may not be repaired inside the failed frozen stage.

## 13. Stop rules

1. If P0 cannot produce a numerically stable component-resolved split representation, B28 stops before claim-bearing computation.
2. If B28.1 validly fails, B28.2 is not run.
3. If B28.1 is inconclusive because mandatory validity gates fail, any redesign must be frozen as a new substage before new claim trajectories.
4. B28 never modifies B27 verdicts.

## 14. Claim boundary

B28 tests only finite reduced-model predictability of response-structure transformation.

It does not establish:

- personal identity;
- subjective continuity;
- consciousness;
- AI personhood;
- biological inheritance;
- a universal law of individuality;
- a continuum theorem for topology-changing free boundaries.

## 15. Target interpretation

A successful B28 result would support

\[
\boxed{
\text{different topology, geometry-conditioned related response structure}
}
\]

not preservation of the same state or the same response geometry.
