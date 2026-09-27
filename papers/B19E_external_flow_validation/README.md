# BIG-B19E — External Flow Validation and Local-Budget Audit

**Author:** Jun Lucis  
**Status:** CLOSED — primary external holdout and Stage-B local-budget audit completed  
**Date:** 2026-09-27

## Final executed external system

The final frozen B19E execution used the independently maintained **TIDE** solver rather than the earlier JHTDB candidate described in preliminary design notes.

**External solver:** TIDE  
**Repository:** `Dyloong1/TIDE-dataset-benchmark`  
**Frozen commit:** `464882a26e29afff2fd9c4520873407d47ceb830`  
**Primary numerical grid:** (N=160), fp64

The verified TIDE formulation is rotational-form incompressible Navier–Stokes with stochastic OU forcing and (2/3) dealiasing. The B19E source audit froze the relevant solver semantics before the final claim-bearing stages.

---

## Purpose

B19E asks whether a small set of B19-derived boundary/core descriptors carries **prospective incremental predictive information** about finite-window Lagrangian vorticity amplification beyond a strong standard local-flow baseline.

The primary comparison is deliberately not a replay of one synthetic B19 threshold. B19 itself did not support one robust ray-independent upstream scalar classifier.

The frozen primary models were:

[
M_2=
{
|omega|,|S|,Q,R,
	ext{strain-eigenvector alignments},
p_0=omegacdot Somega
},
]

and

[
M_{m full}
=
M_2+
{
C_{m coh},
Theta_{m signed},
B_{m proxy}
}.
]

Here the B19 additions are the frozen gate/coherence/balance descriptors. No future-response quantity was used as a predictor.

---

## A1 — Frozen prospective external holdout

### Holdout design

The final untouched holdout used:

- flow realizations / seeds: **4 and 5**;
- total rows: **1536**;
- development training seeds: **0, 1, 2** only;
- validation seed 3 excluded from final model fitting;
- frozen ridge regularization: (alpha=10) for both models;
- primary target: finite-window continuous Lagrangian response at the frozen (1	au_eta) horizon;
- final uncertainty: hierarchical bootstrap over realization, anchor, and spatial block.

No feature, gate, neighborhood, horizon, threshold, or model rescue was permitted after holdout access.

### Primary result

The frozen primary holdout produced

[
R^2(M_2)=0.3285226325,
]

[
R^2(M_{m full})=0.3256768635,
]

so that

[
Delta R^2
=
R^2(M_{m full})-R^2(M_2)
=
-0.0028457690.
]

The frozen hierarchical bootstrap 95% interval was

[
[-0.0101698477,;0.0042158635].
]

The formal decision rule required:

- positive support only if (Delta R^2>0) and the lower 95% bound (>0);
- a negative verdict only if the upper 95% bound (<0);
- otherwise null / inconclusive.

Therefore the retained final A1 verdict is

[
oxed{	exttt{NULL_OR_INCONCLUSIVE}}.
]

The point estimate is slightly negative, but the interval crosses zero. B19E therefore does **not** establish incremental predictive information from the frozen B19 additions beyond (M_2), and it also does not support a stronger negative-universality conclusion.

### Per-realization and sensitivity checks

The per-seed primary increments were:

[
Delta R^2_{m seed,4}=-0.00402531,
]

[
Delta R^2_{m seed,5}=-0.00151885.
]

A uniform-only sensitivity analysis gave

[
Delta R^2=-0.00465919.
]

Secondary frozen horizons produced small positive (Delta R^2) values, but they are secondary by design and do not replace or rescue the primary result.

The saved audit explicitly records:

[
	exttt{no_rescue_performed=true}.
]

---

## B — Exact finite-control-volume local budget

Stage B was frozen after the A1 null/inconclusive result and was explicitly defined as **not an A1 rescue**.

It used two new TIDE realizations, seeds **6 and 7**, and evaluated **4608** finite-control-volume rows.

The resolved local enstrophy budget was

[
dot Z_Omega
=
P-D+A+V_b+F+C_{m filt},
]

where:

- (P): stretching production;
- (D): viscous volume loss;
- (A): advective transport;
- (V_b): viscous boundary transport;
- (F): forcing contribution;
- (C_{m filt}): resolved spectral filter/dealias commutator.

The historical B19-style local proxy is only

[
B_{m proxy}=P-D.
]

### Closure result

Across all 4608 rows:

- minimum (k_{max}eta): **1.6301**;
- median relative closure error: **4.87×10⁻¹⁷**;
- maximum relative closure error: **8.44×10⁻¹⁶**.

The frozen budget gate passed:

[
oxed{	exttt{BUDGET_CLOSURE_PASS}}.
]

This is an implementation/bookkeeping result: the resolved local operator budget closes to near machine precision.

It is **not** independent evidence for B19 predictive universality.

### Primary 16(eta) control-volume result

At the primary side length (16eta):

- proxy sign agreement: **0.5625**;
- median proxy relative error: **0.85155**;
- Spearman correlation (B_{m proxy}) vs. (dot Z_Omega): **0.15894**.

The omitted correction was dominated by advective transport. The median absolute advective contribution was approximately **0.8043**, compared with approximately **0.0889** for viscous boundary transport, **0.0345** for forcing, and **0.0040** for the filter commutator.

The proxy improves as control-volume size increases, but remains weak at the tested local scales.

Thus:

> exact local budget closure does not imply that (P-D) is a sufficient low-dimensional local predictor.

The Stage-B audit explicitly preserves

[
	exttt{A1_rescue=false}.
]

---

## Integrated interpretation

The combined B19/B19E result is narrower than a universal boundary-core law.

B19 found direction-dependent upstream channel families rather than one robust ray-independent scalar threshold.

B19E then tested whether three frozen B19 additions supplied incremental external predictive information beyond a strong standard baseline. The primary held-out answer is **NULL_OR_INCONCLUSIVE**.

The exact local-budget extension shows that part of the limitation is mechanistic: finite-volume local evolution contains transport and boundary terms that are omitted by the simple (P-D) proxy.

The strongest retained interpretation is therefore:

> **B19-style boundary/core structure remains a useful diagnostic language, but the tested frozen additions do not establish a transferable low-dimensional predictive law in the executed external TIDE validation.**

---

## What B19E does not establish

B19E does **not** establish:

- a Navier–Stokes blow-up or regularity criterion;
- a universal turbulence law;
- a universal BIG scalar threshold;
- a universal invariant manifold;
- a universal boundary/core predictor;
- laboratory validation;
- a negative theorem excluding all possible boundary/core information.

The final A1 result is specifically a null/inconclusive incremental-information result for the frozen model, features, holdout protocol, and TIDE realization family.

---

## Provenance

Primary claim-bearing local artifacts:

- `B19E_A1_FINAL_HOLDOUT_FREEZE_v1_0.json`
- `B19E_A1_FINAL_HOLDOUT_RESULT_v1_0.json`
- `B19E_A1_FINAL_HOLDOUT_AUDIT_v1_0.json`
- `B19E_B_TIDE_SOURCE_AUDIT_v1_0.json`
- `B19E_B_FINITE_CONTROL_VOLUME_PREDECLARATION_v1_0.json`
- `B19E_B_FINAL_BUDGET_SUMMARY_v1_0.json`
- `B19E_B_FINAL_INDEPENDENT_AUDIT_v1_0.json`

A formal English preprint v1.0 and Japanese reference translation have now been prepared in a DOI-embedded pre-deposition package.

**Reserved Zenodo DOI:** https://doi.org/10.5281/zenodo.22996961

The DOI is reserved but should not be treated as a published Zenodo record until deposition is completed. DOI insertion changes no scientific result, protocol, verdict, or claim boundary. This README records the final audited repository status; the Zenodo record will become the canonical academic citation after deposition.
