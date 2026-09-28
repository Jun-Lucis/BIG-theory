# BIG-B27.0 — Frozen Programme Architecture

## History-Conditioned Boundary Response and Reconfiguration Covariance

**Status:** FROZEN BEFORE B27 PILOT AND CLAIM-BEARING TRAJECTORIES  
**Protocol ID:** BIG_B27_HISTORY_CONDITIONED_RESPONSE_LINEAGE_ARCHITECTURE_v1_0  
**Date frozen:** 2026-09-28  
**Author:** Jun Lucis

---

## 1. Programme question

BIG-B27 asks a new question after closure of the B19-B26 evidential programme:

> Can a boundary-conditioned response structure, shaped by retained history, remain measurably related across branch or topology reconfiguration even when the state, geometry, and absolute response change?

The target is not literal state identity. The target is a **response lineage**: a reproducible relation between pre- and post-reconfiguration response structures.

This programme is motivated by the conceptual statement that individuality may be carried not by an unchanged internal content, but by a characteristic boundary-mediated way of receiving perturbations, folding interactions into history, and transferring that response organization through reconfiguration.

That philosophical statement is motivation only. B27 will test finite numerical operators and their transformation properties.

---

## 2. Inherited evidence and non-retroactivity

B27 is not a repair of B19-B26.

It inherits only the following established distinctions:

- B16: retained boundary history can feed back into later local boundary response in a reduced model.
- B17: stored history and currently readable history are not equivalent.
- B18: retained history becomes dynamically effective after projection through a boundary-dependent readout operator.
- B20-B22: finite-window local response geometry can be measured and can be prospectively useful in restricted frozen families.
- B23/B23A: favorable local or branch-level structure does not imply unrestricted quantitative transfer.
- B24-B26: different boundary classes need not share one fixed quantitative law; a family-local transfer relation may succeed and fail under a valid geometry transfer.

All archived verdicts remain unchanged.

---

## 3. State, boundary, history, and branch

The B27 state is written abstractly as

\[
X_t=(\phi_t,m_t,q_t),
\]

where:

- \(\phi_t\) is the active boundary-carrying field;
- \(m_t\) is a retained history field;
- \(q_t\) is a discrete branch/configuration label determined by a frozen geometric classifier.

A numerical boundary \(\Sigma[X_t]\) will be extracted by one frozen representative-level/support rule after the non-claim-bearing calibration stage and before any B27.1 claim-bearing run.

The programme will use a two-dimensional extension of the B16-B18 history/readout architecture. The admissible model class is

\[
\partial_t\phi
=
\mathcal F_{\rm BIG}[\phi]
+
S_{\rm base}(x,t;q)
+
\eta\,m\,W_\Sigma[\phi]
+
u_a(x,t),
\]

\[
\partial_t m
=
D_m\Delta m-\lambda_m m
+
\alpha\,W_\Sigma[\phi]\,Q_{\rm write}(x,t).
\]

Here \(\mathcal F_{\rm BIG}\) is an inherited compact/free-boundary BIG-type evolution core, \(W_\Sigma\) localizes writing/readout near the numerical boundary, \(\eta\) is history-to-response feedback, and \(u_a\) is a small external probe.

The exact inherited core realization, numerical coefficients, grid, time step rule, representative boundary rule, and stable parameter window are **not claim-bearing in B27.0**. They may be selected only in the calibration-only stage B27-P0 under the firewall in Section 10, and must then be frozen before B27.1.

No new functional coupling term may be introduced after B27-P0 solely because a claim-bearing result is unfavorable.

---

## 4. Canonical finite-dimensional probe space

B27 will not compare arbitrary perturbations. It will use a fixed low-order probe basis in normalized body-centered coordinates

\[
\xi=\frac{x-c}{R},
\]

with a frozen radial envelope \(w(|\xi|)\).

The candidate canonical input basis is

\[
u_0=w,
\qquad
u_x=\xi_x w,
\qquad
u_y=\xi_y w,
\]

\[
u_{2c}=(\xi_x^2-\xi_y^2)w,
\qquad
u_{2s}=2\xi_x\xi_y w.
\]

Thus the probe coefficient vector is

\[
a=(a_0,a_x,a_y,a_{2c},a_{2s})\in\mathbb R^5.
\]

The body center \(c\), scale \(R\), orientation convention, and radial envelope are frozen in B27-P0 using geometry only. They may not use target response outcomes.

Under a frame rotation by angle \(\theta\), the input map is fixed analytically:

\[
A(\theta)
=
1\oplus R(\theta)\oplus R(2\theta),
\]

where \(R(\theta)\) is the ordinary \(2\times2\) rotation matrix.

No coefficients of \(A\) may be fitted to response data.

---

## 5. Boundary response operator

Let \(\mathcal U_T(X;a)\) be the finite-window evolution from anchor state \(X\) under probe coefficients \(a\), and let \(Z(X)\in\mathbb R^r\) be the frozen boundary-readout vector.

The primary readout may contain only geometry/dynamics observables chosen from the following predeclared set:

1. enclosed/support measure;
2. total representative boundary measure;
3. normalized centroid vector;
4. normalized traceless quadrupole components.

Retained-history mass or local-history load may be recorded as explanatory secondary variables but may not be part of the primary \(Z\), so that history conditioning is not detected trivially by directly reading out the history field.

Define the finite-window perturbation response

\[
\mathcal R_T(X;a)
=
Z(\mathcal U_T(X;a))
-
Z(\mathcal U_T(X;0)).
\]

The local response operator is

\[
K(X)
=
D_a\mathcal R_T(X;a)\big|_{a=0}.
\]

Numerically, \(K\) must be estimated by symmetric finite differences at two frozen probe amplitudes \(h\) and \(h/2\). Cross-scale stability is a validity requirement, not a post-hoc quality label.

---

## 6. Response pullback form

Because absolute response amplitude may change across reconfiguration, B27 separates response **shape** from global gain.

Let \(W_Z\) be a frozen positive diagonal output-weight matrix determined only from B27-P0 calibration scales.

Define

\[
G(X)
=
\frac{K(X)^\top W_ZK(X)}
{\operatorname{tr}\!\left(K(X)^\top W_ZK(X)\right)}.
\]

\(G\) is a normalized positive-semidefinite response pullback form on the probe space. If it is positive definite it may be interpreted as a local response metric; otherwise it is retained as a semidefinite response form.

This normalization deliberately removes one overall response-amplitude degree of freedom. Absolute gain is retained separately through \(\|K\|_F\).

If the trace in the denominator is below the frozen numerical informativeness floor, that anchor is non-informative and cannot be promoted to a positive or negative covariance claim.

---

## 7. B27.1 — Does history change the response structure?

For every B27.1 anchor, two states are created from the **same saved \(\phi\) snapshot**:

\[
X_{\rm kept}=(\phi,m,q),
\qquad
X_{\rm erased}=(\phi,0,q).
\]

Thus present boundary geometry is identical at intervention time and only the retained-history state is changed.

A third control retains \(m\) but sets history feedback to zero during the read phase:

\[
X_{\eta=0}=(\phi,m,q;\eta=0).
\]

Primary structural history separation is

\[
\Delta_G
=
\frac{\|G_{\rm kept}-G_{\rm erased}\|_F}
{\|G_{\rm kept}\|_F+\|G_{\rm erased}\|_F}.
\]

Global-gain separation is recorded independently as

\[
\Delta_{\rm gain}
=
\left|
\log
\frac{\|K_{\rm kept}\|_F}
{\|K_{\rm erased}\|_F}
\right|.
\]

B27.1 must distinguish at least three possibilities:

- **structural history conditioning:** the normalized response form changes beyond frozen numerical uncertainty;
- **gain-only history conditioning:** only overall response magnitude changes reproducibly;
- **no resolved history conditioning:** neither effect exceeds the frozen uncertainty criterion.

Exact case counts and numerical uncertainty multipliers are frozen after B27-P0 and before B27.1 trajectories. The selection rule for those gates is itself frozen in Section 10.

---

## 8. B27.2 — Reconfiguration covariance

A reconfiguration event is a transition

\[
q^-\rightarrow q^+
\]

under one frozen branch/topology classifier.

For pre- and post-reconfiguration anchor states \(X^-\) and \(X^+\), the geometry-only frame map produces a fixed input transformation \(A\). The primary lineage prediction is

\[
G_{\rm pred}^{+}
=
A^\top G^- A.
\]

The primary covariance defect is

\[
\varepsilon_G
=
\frac{
\|G^+-A^\top G^-A\|_F
}{
\|G^+\|_F+\|A^\top G^-A\|_F
}.
\]

No response value from \(X^+\) may be used to alter \(A\).

A direct operator-level comparator may also be recorded,

\[
\varepsilon_{\rm op}
=
\frac{
\|\widehat K^+A-C\widehat K^-\|_F
}{
\|\widehat K^+A\|_F+\|C\widehat K^-\|_F
},
\]

where \(\widehat K=K/\|K\|_F\) and \(C\) is the output-coordinate transformation induced analytically by the same geometry-only frame rotation. The primary verdict, however, is based on \(\varepsilon_G\), because it removes arbitrary output-coordinate rotations and one global gain factor.

---

## 9. B27.3 — Prospective held-out transfer

If B27.1 resolves a history-conditioned response structure and B27.2 yields an executable covariance test, B27.3 applies the **unchanged** construction to a new held-out reconfiguration family.

Before any B27.3 target trajectory is run, the following must be frozen:

- held-out geometry family;
- history-writing protocols;
- branch/topology classifier;
- boundary extraction rule;
- body-frame rule;
- probe envelope and amplitudes;
- output vector and weights;
- transformation rule \(A\);
- numerical validity gates;
- PASS / FAIL / INCONCLUSIVE criteria.

B27.3 is the first stage allowed to support a transfer claim beyond the family used to construct the B27.2 relation.

---

## 10. Calibration firewall and anti-rescue rule

### B27-P0 calibration-only stage

A non-claim-bearing calibration stage is permitted before B27.1 solely to establish numerical executability.

P0 may determine:

- one stable inherited BIG-type 2D evolution core;
- a finite grid/resolution pair;
- time-step cap;
- one history-writing amplitude window;
- one feedback window;
- representative boundary level/support rule;
- body-frame stability criterion;
- probe amplitudes \(h,h/2\);
- output normalizations \(W_Z\);
- numerical uncertainty floors;
- a finite set of claim-bearing parameter values chosen without observing their outcomes.

P0 may not be used as positive evidence for B27.1-B27.3.

### Frozen gate-selection rule

Exact numerical thresholds for B27.1 and B27.2 must be derived only from calibration reproducibility and numerical uncertainty, not from claim-target effect sizes.

The default uncertainty rule is:

\[
\text{resolved effect} > 3\times \text{frozen numerical uncertainty}.
\]

Within-branch reproducibility defect is measured in P0 and frozen as \(\varepsilon_{\rm rep}\). B27.2 covariance gates must be expressed relative to this pre-target floor, with no target-dependent relaxation.

### Anti-rescue rule

After the first claim-bearing B27.1 trajectory is evaluated:

- no new coupling term;
- no replacement response basis;
- no new primary readout component;
- no change of history intervention;
- no target-dependent remapping;
- no coefficient fit using held-out outcomes;
- no domain extension solely to acquire a desired reconfiguration;
- no reclassification of pilot data as held-out evidence

may be used to rescue an unfavorable result.

A repaired design, if scientifically justified, must receive a new substage identifier and may not overwrite the original verdict.

---

## 11. Numerical validity gates

Every claim-bearing anchor must satisfy all frozen numerical gates, including at minimum:

1. finite values and solver completion;
2. negligible domain-edge interaction under a predeclared boundary-distance rule;
3. two-resolution consistency;
4. two-probe-scale stability of \(K\);
5. stable boundary extraction under the frozen representative rule;
6. stable body-frame orientation, with a non-degenerate second-moment eigenvalue gap;
7. informative response norm above the frozen noise floor;
8. realized branch/topology classification where required.

If a required validity gate fails, the case is **IMPLEMENTATION_INVALID** or the stage is **INCONCLUSIVE** according to the predeclared case-count rule. Invalid cases are never silently replaced.

---

## 12. Verdict logic to be frozen before each claim stage

B27.0 freezes the semantic categories now; exact numerical cutoffs and required held-out case counts are frozen after P0 and before the first claim-bearing run.

### B27.1 semantic outcomes

- \`HISTORY_RESPONSE_GEOMETRY_PASS\`
- \`HISTORY_GAIN_ONLY\`
- \`HISTORY_CONDITIONING_NOT_SUPPORTED\`
- \`INCONCLUSIVE\`
- \`IMPLEMENTATION_INVALID\`

### B27.2 semantic outcomes

- \`RECONFIGURATION_COVARIANCE_PASS\`
- \`RECONFIGURATION_COVARIANCE_PARTIAL\`
- \`RECONFIGURATION_COVARIANCE_FAIL\`
- \`INCONCLUSIVE\`
- \`IMPLEMENTATION_INVALID\`

### B27.3 semantic outcomes

- \`HELDOUT_RESPONSE_LINEAGE_TRANSFER_PASS\`
- \`HELDOUT_RESPONSE_LINEAGE_TRANSFER_PARTIAL\`
- \`HELDOUT_RESPONSE_LINEAGE_TRANSFER_FAIL\`
- \`INCONCLUSIVE\`
- \`IMPLEMENTATION_INVALID\`

A PASS is family- and resolution-bounded. It is not a theorem of individual identity or universal boundary covariance.

---

## 13. Stop rules

1. If B27.1 validly finds no resolved history conditioning, B27.2 may be run only as an explicitly secondary geometry diagnostic; no history-lineage claim may be made.
2. If B27.2 validly fails covariance, B27.3 does not tune \(A\) on the failed family. A new mapping hypothesis requires a new numbered subprogramme.
3. B27.3 terminates after the frozen held-out family is evaluated, regardless of outcome.
4. No B27 result changes any B19-B26 verdict.

---

## 14. Claim boundary

B27 does **not** test or establish:

- personal identity;
- subjective continuity;
- consciousness;
- AI personhood;
- an invariant soul/core;
- a universal law of individuality;
- biological inheritance;
- a continuum theorem for topology-changing free boundaries.

The AI analogy that motivated part of the discussion is non-claim-bearing. A successful B27 result would establish only that a finite reduced boundary-history model exhibits a measurable, prospectively testable response-lineage relation across specified reconfiguration events.

---

## 15. Intended research logic

The programme is deliberately ordered as

\[
\text{history writes response structure}
\rightarrow
\text{response structure is measured}
\rightarrow
\text{reconfiguration occurs}
\rightarrow
\text{covariant lineage is predicted}
\rightarrow
\text{held-out transfer is tested}.
\]

The strongest desired result is not

\[
\text{same state before and after},
\]

but

\[
\boxed{
\text{different states, related response geometry}
}.
\]

That is the B27 mathematical form of the present BIG hypothesis.
