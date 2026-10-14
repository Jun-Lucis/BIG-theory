# BIG-B3.1

## Boundary-Layer Position Fits and Limits of the Quadratic-Layer Interpretation

B3.1 reports empirical boundary-layer position fits in a degenerate mixed-gradient dissipative field model. Original figures and fitted values are retained, with narrower interpretation of the proposed scaling and local balance.

### Publication status — checked 14 October 2026 (UTC)

- **Current record:** [10.5281/zenodo.23342986](https://doi.org/10.5281/zenodo.23342986).
- **Original record:** [10.5281/zenodo.20465842](https://doi.org/10.5281/zenodo.20465842).
- **PDF correction remains pending:** the current title and description contain the interpretive correction, but the downloadable PDF is byte-identical to the original six-page manuscript. It does not match the prepared seven-page corrected PDF. The new DOI alone does not confirm publication of the corrected manuscript.

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
