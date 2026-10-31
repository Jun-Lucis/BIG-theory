# BIG-B7 v1.1 — source recovery, numerical controls, and conditional linearization audit

**Author:** Jun Lucis  
**Audit date:** 31 October 2026  
**Published B7 v1.1:** [version-specific DOI 10.5281/zenodo.23835715](https://doi.org/10.5281/zenodo.23835715) · [record and files](https://zenodo.org/records/23835715) · **CC BY 4.0**  
**Original B7 record:** [10.5281/zenodo.20603601](https://doi.org/10.5281/zenodo.20603601)  
**Current publication files:** `BIG_B7_Revised_Preprint_EN_v1_1.pdf`, `BIG_B7_Japanese_Reference_v1_1.pdf`, `BIG_B7_v1_1_Reproducibility_Supplement.zip`.

## 1. Preserved historical results

BIG-B7 records a numerical classification for a **finite-resolution, finite-time,
projected** mixed-gradient evolution, with the original parameters
`m=1`, `N=160`, `L=8`, `mu=0.3`, `dt=1e-6`, and `T=0.3`.

The archived scan has `gamma=0.870–0.873` reaching the observation
horizon and `gamma=0.874–0.878` crossing a **numerical stopping criterion**.
The original bracket midpoint **`gamma_c=0.8735 ± 0.0005`**
is retained **only in this finite-grid protocol**. Likewise, the selected
positive-level-contour, finite-window fitted boundary exponent is
approximately `nu=1.9085` throughout this scan. This is **not** a
universal continuum critical coefficient or an exact support-edge exponent.

The original B7.6 critical-time scaling interpretation remains exploratory;
no universal scaling exponent was established. Published labels, tables,
parameters, failure modes and historical decisions are preserved.

## 2. Source/operator and archived-field audit

Original Colab source was recovered and linked to the archived outputs.
The implementation uses the formal negative-quartic-gradient flux:

```text
phi_t = div(phi^m grad(phi) - gamma |grad(phi)|^2 grad(phi)) - mu phi
```

Its executed finite-grid scheme additionally uses periodic **centered
gradient and centered divergence**, forward Euler, nonnegative
post-step clipping (upper clip 5), and thresholds on the peak and RMS
of the RHS. A numerical `STOP` is a rule of the **discrete solver**,
not a statement about the existence of continuous-PDE singularities.

Source dictionary parameters and archived output statistics were
matched for 9/9 cases (162/162 fields). Independent recomputation
from the nine archived fields reproduced RHS RMS, mass and peak
to floating-point roundoff; source-recovered original notebook and
source-output linkage are not a proof of complete historical
execution-time source immutability.

A separate source-aligned implementation reproduced the complete
N160 time evolution for **three** selected cases, `gamma=0.873`,
`0.874` and `0.878`. It was **not** a full independent
nine-run re-execution. For `gamma=0.874`, the first tested
RHS numerical stop occurred at step **299953**; step **299000**
is the previously saved **last-good** state, not the exact first
crossing step.

## 3. Spatial and timestep controls

The same circular/elliptical family is *not* a controlled continuum
well-posedness test. With the B7 elliptical reference
(`a=2`, `b=1.4`, amplitude `0.2`, `gamma=0.874`,
`dt=1e-6`, `T=0.3`) under the centered spatial scheme:

| Spatial grid | Numeric outcome |
| --- | --- |
| N96 | Survived to T=0.3; final RHS RMS ≈0.01375684 |
| N128 | Survived to T=0.3; final RHS RMS ≈0.01475553 |
| N160 | STOP; first trigger test near t=0.299952 |

An alternative **face-flux spatial discretization** on N96, using
the same initial field and stopping definitions, instead reached
`STOP` near `t=0.254392`. In separate controls each spatial
discretization showed near second-order consistency for a
*smooth positive manufactured-field* spatial test. This does not
validate nonlinear PDE convergence.

At N160, halving the time step moved the first stop trigger from
approximately `0.299952` to `0.2999495`, so a gross
timestep artifact does not explain the tested numerical discrepancy
by itself. No `dt→0` or `N→∞` convergence theorem is claimed.

## 4. Projection and mathematical limitation

For `m=1`, with a positive smooth reference `phi_0`
and `q=grad(phi_0)`, the principal coefficient matrix of
the **formal, unprojected, fixed-profile linearization** is

```text
A = phi_0 I - gamma ( |q|^2 I + 2 q⊗q )
a_parallel = phi_0 - 3 gamma |q|^2
a_transverse = phi_0 - gamma |q|^2
```

In the specified elliptical positive interior at `gamma=0.873`,
the parallel coefficient is negative over approximately **66.59%**
of the positive-support area; the sign computation is local and
analytical for the given initial field.

**Conditional mathematical result:** the frozen-time *spatially
variable-coefficient* linearized differential operator with an interior
negative principal direction cannot generate a standard
`L^2` `C_0` semigroup on a periodic domain for the specified
operator realizations containing smooth compactly supported
interior perturbations and agreeing with the stated differential
expression. The localized high-frequency test/resolvent argument
is a formal source-scoped operator result. It is **not** a general
nonlinear Hadamard nonexistence proof, a nonlinear blow-up theorem,
or an empirical physical instability model.

Across the nine archived fields, the clipped solver's mass is about
**0.1989–0.3793% above** the non-clipped periodic decay budget.
The nonnegativity projection can contribute positive mass relative
to this formal identity. This does **not** independently identify
the cause of the numerical stop.

## 5. Evidence classes and unresolved questions

| Claim | Status |
| --- | --- |
| Original 9-case boundary exponent and numerical gamma bracket | **HISTORICAL FINITE-GRID OBSERVATIONS RETAINED** |
| Recovered original source and saved-output linkage | **SOURCE SUPPORT** |
| Archived nine-field arithmetic/source-RHS audit | **9/9 LIMITED REPRODUCIBILITY PASS** |
| Independent full original-grid trajectories | **3/9 SOURCE-ALIGNED REPLAY PASS** |
| Grid/stencil dependence of numerical survival/STOP | **NUMERICAL SUPPORT / COUNTEREXAMPLE TO SCHEME INVARIANCE** |
| Negative interior principal coefficient | **MATHEMATICAL DERIVATION** |
| Fixed-profile linearization semigroup obstruction | **CONDITIONAL PROOF UNDER OPERATOR-DOMAIN ASSUMPTIONS** |
| Nonlinear continuum blow-up or a universal critical gamma | **UNRESOLVED / NOT ESTABLISHED** |
| Exact continuum support-edge exponent and physical applicability | **NOT ESTABLISHED / PHYSICAL VALIDATION NOT PERFORMED** |

No separate BIG family has been retroactively regraded by this audit.
In particular, B8 has its *own* v0.3 scoped audit
([10.5281/zenodo.23832946](https://doi.org/10.5281/zenodo.23832946)),
while B9 onward must be checked against their own executed models.
B42's formally retained overall scientific verdict
**SCIENCE NONE** and all historical FAIL/INCONCLUSIVE records are unchanged.

The publication's reproducibility supplement includes the retained
B7 archive, recovered original Colab and the newly documented
audit scripts, numerical results and provenance. Cite the *v1.1*
version-specific DOI for this revised mathematical/numerical audit
and the original DOI for the original archived numerical report.
