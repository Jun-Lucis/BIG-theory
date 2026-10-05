# Research Methodology Companion

Boundary Information Geometry (BIG) is the mathematical and numerical research programme documented in this repository.

A separate companion repository is being established for the **research-development methodology** that emerged during the programme:

**Failure-Preserving AI-Assisted Research**  
https://github.com/Jun-Lucis/failure-preserving-research

The companion project treats BIG as a longitudinal case study rather than as a premise. Its methodological claims are intended to remain logically distinct from the correctness or generality of BIG itself.

## Why a separate repository?

The two repositories answer different questions.

- **BIG-theory:** What mathematical and numerical structures were tested, and what evidence was obtained?
- **failure-preserving-research:** How was the research process organized so that large-scale exploration, prospective freezing, retained failures, recovery, and later salvage could be used as research assets?

The methodological programme focuses on four linked practices:

1. **Expanded individual research bandwidth** through AI-assisted coding, numerical experiment design, debugging, data organization, and comparison.
2. **Freedom to fail** in individual research, where exploratory branches can be pursued without consuming a team’s shared labor budget.
3. **Failure preservation** through retained parameters, outputs, verdicts, checkpoints, manifests, and audit records.
4. **Failure salvage** in which earlier negative, inconclusive, or abandoned results can later constrain the search space or motivate a successful route.

The central methodological proposition is deliberately narrower than a claim that AI “automates science”:

> AI can change not only the cost of successful experiments, but also the economics and future value of failed experiments.

## Evidence linkage

The companion methodology repository will point back to concrete BIG records where appropriate, including retained FAIL, INCONCLUSIVE, implementation-invalid, recovery, and prospective PASS histories.

Conversely, this repository will link to the methodology repository so that readers can distinguish:

```text
research method and process
        <-> 
actual BIG numerical record
        <->
archived BIG papers and reproducibility packages
```

## Publication architecture

The intended public structure is:

```text
Methodology paper (Zenodo)
        <->
Methodology GitHub repository
        <->
BIG-theory GitHub repository
        <->
BIG papers / data / reproducibility archives (Zenodo)
```

The methodology paper DOI will be added after the first formal release.

## Scope boundary

This methodological project does **not** claim that retained failures automatically become useful, that unlimited computation is free, or that AI removes the need for scientific judgment. Human time, verification, compute, energy, and error control remain real costs.

The narrower claim is that AI-assisted individual research can substantially lower the marginal cost of generating, implementing, checking, and revisiting computational experiments, while disciplined preservation can give failed exploration nonzero future value.
