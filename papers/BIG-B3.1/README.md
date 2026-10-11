# BIG-B3.1

## Boundary-Layer Scaling and Quadratic Landing

BIG-B3.1 investigates boundary-layer scaling and quadratic landing behavior in degenerate mixed-gradient dissipative fields.

This report forms one of the numerical foundations for the later BIG-B4 series.

### Main Focus

* Boundary-layer asymptotics
* Quadratic landing behavior
* Compact-support-like boundary formation
* Local fitting of free-boundary profiles

### Main Observation

The key numerical observation is that local boundary profiles are well approximated by

```text
phi(s) ~ A s^nu
```

with an exponent close to

```text
nu ≈ 2
```

near detected boundary regions.

### Role in the BIG Series

BIG-B3.1 provides the asymptotic and numerical basis for:

* BIG-B4.1 — Quadratic Boundary Universality Scan
* BIG-B4.3 — Boundary-Layer Stability and Compression Map

### Equation-version provenance note (October 2026)

The B3.1 manuscript prints a negative quartic-gradient term. A later audit found that six **B4.3** archived numerical outputs strongly match a recovered solver with a **positive `+4 gamma`** quartic-gradient flux, despite the negative term printed in the B4.3 manuscript. **This B4.3 evidence does not establish which implementation generated the original B3.1 results.** The finite-width `nu ≈ 2` numerical observation is retained; exact zero-support asymptotics are not established by that fit alone.

See the [B4.3 source-versus-print audit](../../docs/B4_3_printed_equation_vs_numerical_solver_audit_2026_10.md) for the numerical evidence and limitations.

### Status

Completed numerical report.

### DOI

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20465842.svg)](https://doi.org/10.5281/zenodo.20465842)
