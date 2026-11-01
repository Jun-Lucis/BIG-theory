# BIG-B5 v1.2 — source-linked numerical replication and conditional PDE limits

**Author:** Jun Lucis  
**Publication date:** 1 November 2026  
**Current version-specific DOI:** [10.5281/zenodo.23850139](https://doi.org/10.5281/zenodo.23850139)  
**Zenodo record:** [B5 v1.2](https://zenodo.org/records/23850139) — **Preprint**, **CC BY 4.0**  
**Version family:** [B5 v1.0 (20575991)](https://doi.org/10.5281/zenodo.20575991) → [B5 v1.1 (23381643)](https://doi.org/10.5281/zenodo.23381643) → **B5 v1.2 (23850139)**. [All-version DOI 10.5281/zenodo.20575990](https://doi.org/10.5281/zenodo.20575990).

## Public files and scope

The current Zenodo record lists exactly three public files:

1. `BIG_B5_Revised_Preprint_EN_v1_2.pdf`
2. `BIG_B5_Japanese_Reference_v1_2.pdf`
3. `BIG_B5_v1_2_Reproducibility_Supplement.zip`

These names, the published date, three-version lineage and CC BY 4.0
were checked against the displayed public record. Zenodo displayed MD5
digests `1a5464f516823d39d140dad376d2526f` (EN PDF),
`fbdf4e6c5cce8b0678532f5330ddb8df` (JA PDF) and
`aae8e90f2ab94187a67bfba1b29141d0` (ZIP).
This GitHub documentation synchronization does **not** claim that a
fresh binary download was hash-checked independently.

The v1.2 publication adds a source-linked research preprint and a
comprehensive reproducibility supplement to the historical B5 dataset.
It does not erase the earlier dataset or revise the old numerical outcomes.

## Historical finite-grid experiment

For `m = 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.90, 1.00`,
the original B5.11 centered finite-difference scheme used
`N=220`, `gamma=0.10`, `mu=0.3`, `dt=1e-6`, `T=0.24`.
All nine runs reached the **240000-step cap**. This is not
a stationary-convergence test.

At the original finite positive-level-contour fit definition, the
selected mean effective exponent ranges from approximately **2.160614**
at `m=.5` to **1.816683** at `m=1`, with intermediate
mobility dependence and selection sensitivity. It is not an exact
support-edge asymptotic law or universal exponent.

## Recovered source and B5.11 CP6 replay

The original Colab notebook was recovered and its recorded source
and saved output statistics linked to the nine B5.11 archives:
the tracked parameter fields and **144/144** tabulated source-output
statistics match. Archived terminal fields were independently checked
with the historical negative-quartic-flux discrete RHS.

A separate source-aligned implementation independently replayed
**9/9** full `T=.24` histories and the original source-sliced
contour-fitting extraction. The maximum observed absolute
final-grid difference was about **5.55e-17**.
A **FTZ/DAZ subnormal-floating-point mode** was used in the
reproduction and is disclosed: this is close numerical agreement,
not bit-for-bit identity of all historical floating-point operations,
not third-party verification of the historical execution logs,
and not spatial or temporal continuum convergence.

## CP7 grid, clipping, timestep and smoothing controls

CP7 added **22 short-window numerical controls** and **54 fit-definition
comparisons** on the nine unchanged archived terminal fields.

At `m=1`, `t=.002`, the central-stencil numerical proportion of
positive cells with a negative parallel principal coefficient changed
with grid:

| N | Negative principal-coefficient cells among cells with phi > 1e-8 |
| ---: | ---: |
| 96 | 8.27% |
| 128 | 6.25% |
| 160 | 4.61% |
| 220 | 3.34% |
| 320 | 1.93% |

These diagnosed cells were confined to very weak positive
boundary-region fields (`phi < 1e-4` in the tested controls).
Removing nonnegative clipping, halving the timestep, and changing
the spatial discretization did not **alone** remove the phenomenon.
A post-hoc Gaussian smoothing of width `0.5` grid cells did remove
the negative-cell detection in specified tests. **A smoothed
postprocessed field is not another solution to the same PDE.**
The shrinking *grid-cell percentage* is not by itself a convergence
theorem or proof that the negative region disappears in the continuum.

At `m=.9`, negative cells were also observed in some very-early
tests, while none was detected at the tested later states.
There is no proved universal critical mobility separating
mathematically stable and unstable dynamics.

## Formal equation, counterexample and conditional proof

The formal **unprojected** B5 equation in the positive interior is

```text
phi_t = div(phi^m grad(phi) - gamma |grad(phi)|^2 grad(phi)) - mu phi
```

For a smooth strictly positive profile `phi`, its spatial
linearization has the principal matrix

```text
A(phi) = [phi^m - gamma |grad(phi)|^2] I
         - 2 gamma grad(phi) tensor grad(phi)

lambda_parallel   = phi^m - 3 gamma |grad(phi)|^2
lambda_transverse = phi^m - gamma |grad(phi)|^2.
```

For the *historical B5 elliptical initial profile* and `m∈[.5,1]`,
the parallel coefficient is positive at the strictly positive initial
interior. This is not a time-uniform guarantee.

Separately, the strictly positive smooth periodic test field
`psi(x)=0.15+0.04 sin((2*pi*45/8)x)` provides, for `gamma=.1`,
a region with `lambda_parallel<0` for all `m∈[.5,1]`.
Thus the formal negative-flux B5 model is **not forward parabolic
for every smooth strictly positive state**. The associated
**time-frozen, spatially variable-coefficient linearized operator**
also has a **conditional L2 C0-semigroup-generation obstruction**
on suitable operator realizations that contain the required
smooth local perturbations and agree with the differential expression.

**This is not** a proof of failure of nonlinear well-posedness for
the historical elliptical initial-value problem, nor a nonlinear
finite-time blow-up theorem. It cannot be transferred to the
**positive-quartic-gradient energy family** by analogy.

## Boundary-exponent observation sensitivity

Changing the chosen positive contour and fitting window yields
different absolute mean fitted exponents. The original 9/9
source-sliced fit is reproduced, and, over six tested fit definitions,
`mean_nu(m=.5) > mean_nu(m=1)` remained true.

This supports a **bounded, finite-grid comparative observation**,
not an exact power-law universality class or a physical prediction
independently calibrated in a laboratory.

## Evidence register and exclusions

| Evidence claim | Status |
| --- | --- |
| Original nine B5.11 finite-grid observations | **RETAINED** |
| Original Colab to archived results and fields | **SOURCE-LINKED QA PASS** |
| Independent original-scheme trajectories / original fit replays | **9/9 SOURCE-ALIGNED NUMERICAL PASS**, FTZ/DAZ disclosed |
| CP7 22 controls / 54 fit-definition comparisons | **NUMERICAL SUPPORT, DEFINITION SENSITIVITY** |
| Negative principal coefficient for a distinct positive profile | **MATHEMATICAL COUNTEREXAMPLE** |
| Fixed-profile linearization semigroup obstruction | **CONDITIONAL MATHEMATICAL CLAIM** |
| Historical elliptic nonlinear continuum well-posedness | **UNRESOLVED** |
| Exact support-edge exponent and independent physical calibration | **NOT ESTABLISHED** |

B7 and B8 each have separately published, scoped audits
([B7 v1.1](https://doi.org/10.5281/zenodo.23835715),
[B8 v0.3](https://doi.org/10.5281/zenodo.23832946)).
The negative-flux issue is **not automatically inherited** by
the distinct B9 onward mathematical families or by the
separate positive-quartic-gradient energy/flux models.
All historical FAIL and INCONCLUSIVE records and B42's
overall **SCIENCE NONE** verdict remain unchanged.

See the [B5 research README](../papers/B5_mobility_dependent_boundary_exponents/README.md)
and [B3.1–B5 historical correction register](publication_corrections_B3_1_B5_2026_10_14.md).
