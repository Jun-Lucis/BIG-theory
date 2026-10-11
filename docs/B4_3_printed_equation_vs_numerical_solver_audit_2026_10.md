# BIG-B4.3 — clarification of the printed equation and numerically supported solver (12 October 2026)

**Status:** retrospective source-to-output audit; clarification pending an amended manuscript. **This note does not change the original B4.3 classifications or claim a new continuum theorem.**

## What needs clarification

The published B3.1/B4.3 manuscripts print a quartic-gradient term of the form

```text
    - gamma * div(|grad(phi)|^2 * grad(phi)).
```

A subsequently recovered B4.3 *pilot* finite-volume solver instead computes the face flux

```text
    Q = (phi_face^2 + epsilon) * grad_face(phi)
        + 4 * gamma * |grad(phi)|_face^2 * grad_face(phi),
```

with zero outer-face flux, and uses `phi_t = div(Q) - mu*phi + S` with a non-cutoff Gaussian source. The difference is **both the sign and the factor 4**; these formulations must not be treated as equivalent.

The recovered solver is labeled for the B4.3 pilot (`N=220`, `L=8`, Gaussian source, initial `mu=0.3, gamma=0.5`) and points to the same B4.3 output-folder convention. The executed notebook/commit and all original run hashes have **not** been independently attested.

## Retrospective verification against six archived output arrays

For six archived B4.3 `phi.npy` fields (three `mu` values at `gamma=0.5, 2.0`), the recovered **+4 gamma** finite-volume spatial operator gives final-field residual norms close to `1e-8`. Replacing only the quartic face-flux coefficient with the **printed -gamma** gives much larger residuals on those *same arrays and stencil*:

| mu | gamma | residual, recovered +4 gamma | residual, printed -gamma |
| ---: | ---: | ---: | ---: |
| 0.3 | 0.5 | 9.997712e-9 | 0.006704 |
| 0.3 | 2.0 | 9.999316e-9 | 0.010339 |
| 0.7 | 0.5 | 9.991781e-9 | 0.003480 |
| 0.7 | 2.0 | 9.997972e-9 | 0.006229 |
| 1.0 | 0.5 | 9.987269e-9 | 0.002136 |
| 1.0 | 2.0 | 9.994100e-9 | 0.004345 |

The source checks its stopping norm **before** writing the final explicit-Euler update. Accounting for this difference by reversing the last step reproduces the six archived *pre-update* stopping norms with relative discrepancies below `4e-11`. This is **strong numerical evidence** connecting the six outputs to the recovered **+4 gamma** operator, beyond matching names or parameters. It is not cryptographic proof of the complete original execution history.

The B4.3 nine-condition summary remains archival evidence. Corresponding raw arrays for the three `gamma=1.0` conditions have **not** been checked in this source-to-output comparison. The B3.1 executed solver was **not** established by this audit.

## Why the amplitude formula has 96

For the *positive-coefficient* continuum prototype

```text
phi_t = div((phi^2 + epsilon) grad(phi)
            + 4 gamma |grad(phi)|^2 grad(phi))
        - mu phi + S,
```

substituting the one-dimensional candidate `phi = A*(R-x)^2` (`s=R-x`) into the stationary equation **without S** yields

```text
2 epsilon A + (96 gamma A^3 - mu A) s^2 + 10 A^3 s^4.
```

In an **intermediate layer**, *if* the Gaussian source, `epsilon`-term and higher-order term are negligible relative to the quadratic terms, the leading balance gives `A = sqrt(mu/(96 gamma))`. This explains the coefficient 96 in the numerical comparison; it **does not prove exact quadratic landing at a zero-support edge**. The recovered solver has `epsilon > 0` and a Gaussian source positive throughout the finite domain; the archived six `phi.npy` grids had no exactly zero cells.


## Additional earlier-source lineage check (12 October 2026)

A separately recovered user-supplied source labeled **BIG v1.9 — focused high-resolution mu=0.6 quadratic-layer scan**, with run-directory name `2026-05-30_mu_0p6_focused_highres_quadratic_detection`, uses the **same positive `+4 gamma` finite-volume face-flux function** as the later B4.3 pilot. An AST-level comparison of the two `compute_rhs_and_dt` function **bodies** found them **identical**; only the argument signatures differ (`(phi)` versus `(phi, mu, gamma)`). On the v1.9 `N=240, mu=0.6, gamma=1.0` synthetic initial field, one RHS-only evaluation from each extracted implementation gave bitwise-identical arrays and the same time step.

This extends the **provided source-text lineage**, not the authenticated run provenance. The claimed May 30 date is part of a directory name and is not an independently verified execution timestamp. The v1.9 numerical outputs, original B3.1 executed notebook, and B4.3 `gamma=1` raw arrays have not been independently matched to these texts. The v1.9 and B4.3 **measurement protocols differ** (e.g. 110 vs 120 radial shells; offset fit scan `0–0.20` vs `0–0.28`), so the equality of their PDE stepping functions does not imply identical boundary-layer classifications.

**Conclusion remains:** B4.3's six archived raw fields strongly support the `+4 gamma` solver; original printed `-gamma` differs; B3.1 executable provenance remains open; published finite-width numerical verdicts are retained unchanged.

## Scope, preservation, and next editorial step

- Preserve B4.3's original finite-width numerical boundary-layer observations and historical Stable/Recovered, Compressed, Residual classifications. Do **not** retrospectively change their verdicts.
- Do **not** infer that B3.1 used this same executable solver or that the three other B4.3 runs have been checked.
- The published **-gamma** equation and the strongly supported **+4 gamma** numerical solver should be explicitly distinguished in citations and summaries until an amended manuscript clarifies the discrepancy.
- This audit concerns model/source consistency, **not a new physical validation, exact compact-support theorem, or unique BIG-specific law**.

**Archival references:** [B4.3 original Zenodo record](https://doi.org/10.5281/zenodo.20564435); [B42 PB2-D5 source-to-output audit report (Google Drive; access may be restricted)](https://docs.google.com/document/d/1-dBJLEXO3Xew0zdK4x6Z7rCCp3fKjVB5VKOCNjGibIQ/edit). The audit is retrospective; no original raw files were overwritten.

**Publication recommendation:** Add a clearly dated clarification to the **existing Zenodo description** promptly, retaining its DOI. If a revised PDF formally corrects the displayed equation and explains affected derivations, publish it as a **new Zenodo version** with a separate version DOI and link back to the original. Do not silently replace the original scientific record.
