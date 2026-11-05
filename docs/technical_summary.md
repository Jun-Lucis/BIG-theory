# BIG Technical Summary — One-Page Evidence Guide


**New standalone 5 November 2026 preprints (not B-series versions):** [BIG-MATH-01 v1.0 RevB / DOI 10.5281/zenodo.23969711](https://doi.org/10.5281/zenodo.23969711) gives source-scoped, conditional mathematical analysis for the corrected **positive +4γ flux** B4-type prototype: bounded weak existence, same-coefficient L¹ contraction/uniqueness and selected porous-medium limits. Forward uniqueness **does not** identify coefficients; strict support, historical negative-flux equations and independent physical validity remain unproved. [BIG-OC3 C19–P92 v1.0 RevA / DOI 10.5281/zenodo.23965486](https://doi.org/10.5281/zenodo.23965486) examines synthetic internal history, external readout and conventional viscoelastic comparator transfer against three P92 steel specimens. Limited conventional within-RF holdout success coexists with C19 readout **FAIL**, E9D and E9G cross-protocol **FAIL**, and no BIG-specific incremental prediction. No inference is transferred between the independent mathematical PDE and material-history models. See [paper indices](publication_map.md).

**Current programme-wide synthesis (20 October 2026):** [Flagship Preprint v1.0, DOI 10.5281/zenodo.23486616](https://doi.org/10.5281/zenodo.23486616), including an English paper, Japanese reference translation, and English technical appendix. This older technical guide remains a model-focused introduction; for later B37–B42 limitations consult the [research status pages](publication_map.md) and the flagship. The B42 overall formal scientific verdict is **NONE**; the candidate CA16 physical experiments have **not** been performed and no independently calibrated BIG-specific physical discriminator is established.


**Boundary Information Geometry (BIG)** is a boundary-centered mathematical and numerical research programme. It studies reduced systems in which boundaries are represented explicitly as dynamical fields, geometric costs, history-bearing interfaces, readout structures, branch/reconfiguration geometry, or finite-time response zero sets.

## Current programme-level conclusion

> **BIG provides a common formal language for comparing system-dependent boundary geometry, response, history, branch structure, and reconfiguration. Current evidence does not establish one universal numerical boundary law across the programme.**

This distinction matters:

```text
structural / formal comparability
    !=
quantitative universality
```

The present evidence supports the first as an organizing framework. The second is not established.

## What is established inside tested reduced models?

Several recurring structures have survived direct numerical or prospective tests:

- **Early compact-support-like boundary numerics (B3.1–B5):** B3.1 source/implementation reconciliation and B4.1/B4.3 finite-width near-two signatures have their own operator and provenance limits. [B5 v1.2](https://doi.org/10.5281/zenodo.23850139) preserves the N220, T=.24 mobility-dependent effective-exponent observations, with recovered source, 9/9 same-scheme independent numerical trajectories (FTZ/DAZ arithmetic disclosed), 22 short-window numerical controls, and 54 measurement-definition fits ([B5 audit](B5_v1_2_source_replay_grid_and_fit_audit_2026_11_01.md)). The original negative-quartic-flux formal PDE is **not globally forward parabolic on all positive smooth profiles**; the fixed-profile linearization semigroup obstruction is conditional. These data do not establish a nonlinear continuum blow-up theorem, exact universal support-edge exponent, stationary convergence or physical calibration. See [the original early-series correction register](publication_corrections_B3_1_B5_2026_10_14.md).
- **Finite-time stopping and fitted boundary geometry (B7–B8):** B7 v1.1 ([DOI 10.5281/zenodo.23835715](https://doi.org/10.5281/zenodo.23835715)) retains its N160 finite-window local-exponent and gamma-bracket observations, with original Colab source linked to archived outputs, 3/9 source-aligned full trajectory replays, and numerical STOP sensitivity to grid and spatial discretization ([B7 audit](B7_v1_1_source_numerical_and_linearization_audit_2026_10_31.md)). B8 v0.3 ([DOI 10.5281/zenodo.23832946](https://doi.org/10.5281/zenodo.23832946)) separately retains ellipse-dependent finite-grid thresholds and source/scheme audits ([B8 audit](B8_v0_3_source_and_mathematical_audit_2026_10_31.md)). Both formal unprojected negative-flux equations have **conditional fixed-profile, time-frozen linearization** semigroup-generation obstructions at specified initial fields; neither nonlinear continuum blow-up nor a mesh-independent separatrix, universality or physical law is established.
- **Separation-like metastability:** the reduced B9 energy
  [
  E(Omega;lambda)=sigma P(Omega)+lambda C(Omega)
  ]
  produces compact, barrier, and separated branches.
- **History and readout:** B14–B18 construct explicit history-bearing boundaries and distinguish stored history from locally/path-readable history.
- **Operator-generated response geometry:** B20 defines
  [
  F_T(P)=Z[U_T(P)]-Z[P],qquad
  mathcal B_T={P:F_T(P)=0},
  ]
  and B20–B22 show that local finite-resolution normals, Hessians, curvature, and short-horizon forecasts can be useful on restricted frozen branches/subspaces.
- **Prospective transfer within a family:** B25 Phase I and Phase II obtain prospectively successful, family-restricted boundary-functional reductions, including a fixed perimeter coefficient within the tested ellipse family.

## Where do the stronger claims stop?

The later programme deliberately tested whether local successes could be promoted into broader quantitative laws.

- **B19:** no robust tested ray-independent upstream scalar collapse.
- **B19E:** in the frozen TIDE holdout, the three B19 additions did not establish incremental predictive information beyond the strong baseline (\(\Delta R^2=-0.00285\), 95% CI crossing zero; **NULL_OR_INCONCLUSIVE**). A separate exact local-budget stage closed to near machine precision but did not rescue the predictive result.
- **B20.6:** only one informative frozen finite-distance crossing; verdict remains **INCONCLUSIVE**.
- **B23:** favorable branch-transfer evidence, but the original aggregate protocol remains **INCONCLUSIVE** because two endpoint-near targets could not be evaluated under the frozen symmetric-window rule.
- **B23A:** smooth-normal transfer to a new B9 family is not supported; topology-sensitive piecewise/reset structure is supported in P3; stronger non-topological reset/locality tests P4–P5 remain numerically inconclusive; the held-out P6 monotonic rate-ordering hypothesis is **NOT SUPPORTED** with numerical integrity gates passing.
- **B24:** a single already-existing substantive operator shared across audited BIG sectors is not established; verdict: **MULTIPLE_BOUNDARY_CLASSES_INDICATED**.
- **B26:** the fixed coefficient that transferred within the ellipse family fails prospectively in a new topology-straddling two-center family, with median relative error **42.91%** and maximum **44.79%**.

These are retained results, not outcomes to be removed by retrospective tuning.


## Later-phase update — B27 through B36

The later response-lineage and response-to-timing programmes sharpen the same boundary on overgeneralization.

- **B27:** retained readable history prospectively changes local response geometry (`HISTORY_RESPONSE_GEOMETRY_PASS`), but the simplest frozen topology-reconfiguration covariance fails (`RECONFIGURATION_COVARIANCE_FAIL`).
- **B28:** a geometry-only component-resolved 1-to-2 lineage-transport map is tested prospectively and fails on all three valid fresh targets (`GEOMETRY_CONDITIONED_LINEAGE_TRANSPORT_FAIL`); B28.2 is not opened.
- **B29:** the programme closes before held-out prediction because only 18/27 training cases satisfy the inherited readability/validity gates. No M0/M1/M2 held-out predictive verdict is issued.

Integrated B28–B29 preprint DOI: https://doi.org/10.5281/zenodo.23050390

- **B30–B36:** the integrated programme retains both PASS and FAIL stages. It establishes transverse history-response suppression, reflection parity, period-dependent lifting of a suppressed sector, and a spatially structured complex transfer kernel, while retaining the dynamic-suppression and common linear pulse-timing failures. The final B36.2 test passes a narrower fresh-grid claim: an approximately additive geometry/readout decomposition of fitted peak-timing slope.

Integrated B30–B36 preprint DOI: https://doi.org/10.5281/zenodo.23048197

The terminal B36.2 result does **not** establish physical propagation speed, ballistic transport, finite-speed propagation, a propagating or standing wave, a wave equation, resonance, or a dispersion relation.

## What BIG currently does not claim

BIG does **not** currently establish:

- one universal boundary equation or scalar invariant;
- one universal response-normal field, reset law, or critical rate;
- a continuum free-boundary or curvature theorem;
- a Navier–Stokes blow-up / regularity result;
- a quantitative theory of nuclear fission, nuclear fusion, biology, cognition, AI, or cosmology;
- empirical validity in an external domain without domain-specific calibration and validation.

## What remains open?

The main questions are now narrower:

1. Can the common formal objects be characterized by transformation / covariance rules that survive changes of coordinates and model family?
2. Which quantities are branch-local invariants, which are family-dependent coefficients, and which are only convenient coordinates?
3. Can any finite-resolution prospective result be promoted to a controlled continuum statement?
4. Which BIG structures, if any, survive domain-specific equations, units, calibration, and empirical comparison?

## Recommended interpretation

The strongest current synthesis is:

> **useful local and family-restricted boundary geometry exists in several reduced BIG models, while prospective tests place clear limits on programme-wide quantitative transfer.**

For the full evidence map, see:

- [Integrated research status map — B3 through B26 + B23A](research_status_map_B3_B26.md)
- [Limitations and scope](limitations.md)
- [Publication map / DOI index](publication_map.md)
- [Citation policy](citation_policy.md)
