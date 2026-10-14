# BIG-B3.1

## Boundary-Layer Position Fits and Limits of the Quadratic-Layer Interpretation

B3.1 reports empirical boundary-layer position fits in a degenerate mixed-gradient dissipative field model. Original figures and fitted values are retained, with narrower interpretation of the proposed scaling and local balance.

### Publication status — file correction verified 15 October 2026 (JST)

- **Current record:** [10.5281/zenodo.23342986](https://doi.org/10.5281/zenodo.23342986).
- **Original record:** [10.5281/zenodo.20465842](https://doi.org/10.5281/zenodo.20465842).
- **Corrected PDF now verified:** the mistaken original six-page attachment was replaced through the published-file correction workflow on 15 October 2026 (JST), retaining the existing v2 DOI. The public seven-page PDF matches the uploaded corrected manuscript byte for byte.
- **Public correction note:** the record documents the attachment error, replacement date, and unchanged historical numerical evidence. The original v1 remains separately archived.
- [File-correction verification](../../docs/B3_1_file_correction_2026_10_15.md).

The [correction register](../../docs/publication_corrections_B3_1_B5_2026_10_14.md) records file hashes and verification scope.

### Retained observations and corrected interpretation

The two original one-parameter descriptions remain separate empirical fits:

```text
Rq ≈ 2.093 + 0.606 sqrt(gamma)
Rq ≈ 0.686 + 0.899 mu^(-1/2)
```

Their additive intercepts matter. They do not establish a joint law depending only on `gamma/mu`, nor do they identify boundary-layer position with layer width.

The proposed local relation `Lq^4 ∝ gamma phi^2 / mu`, combined with `phi ≈ A Lq^2`, cancels `Lq`. It constrains an amplitude relation rather than deriving `Lq ∝ sqrt(gamma/mu)`.

For the printed negative-sign, source-free one-dimensional prototype, substituting `phi = A s^2` gives the coefficient `-(24 gamma A^3 + mu A)` at order `s^2`, which cannot cancel for positive `A`, `mu`, and `gamma`. This rejects that particular proposed balance; it is not a nonexistence theorem for forced solutions.

### Provenance and limits

The original executed B3.1 model, numerical inputs, diagnostic definitions, and source-to-figure chain remain unauthenticated. Later B4 evidence for a positive `+4 gamma` finite-volume operator does not establish the B3.1 implementation.

The finite-width-layer interpretation remains exploratory. Exact support-edge asymptotics, a universal quadratic exponent, and the proposed joint length law are not established. Historical numerical observations are preserved.

Related reports: [B4.1](../BIG-B4.1/README.md), [B4.3](../BIG-B4.3/README.md), and [B5](../B5_mobility_dependent_boundary_exponents/README.md).
