# Research Methodology Companion

Boundary Information Geometry (BIG) is the mathematical and numerical research programme documented in this repository.

A separate companion repository now documents the **research-development methodology** that emerged during the programme:

**Failure-Preserving AI-Assisted Research**  
https://github.com/Jun-Lucis/failure-preserving-research

The companion project treats BIG as a longitudinal case study rather than as a premise. Its methodological claims remain logically distinct from the correctness or generality of BIG itself. The current literature audit also narrows novelty claims in light of EvoScientist, Agent-Native Research Artifacts, and Sibyl-AutoResearch; failure preservation or generic result-to-action memory is not claimed as unique.

## Why a separate repository?

The two repositories answer different questions.

- **BIG-theory:** What mathematical and numerical structures were tested, and what evidence was obtained?
- **failure-preserving-research:** How was the research process organized so that AI-assisted exploration, external numerical execution, prospective freezing, retained failures, later salvage, and experimental handoff could form a reusable research architecture?

## Core methodology

The companion project organizes the workflow into three nested cycles plus an external-validation boundary.

1. **Micro — AI / external-computation loop**  
   AI-assisted reasoning is repeatedly translated into simple executable numerical calculations and revised in response to the outputs.

2. **Meso — prospective test / redesign loop**  
   Hypotheses are frozen, tested, and assigned persistent PASS / FAIL / INCONCLUSIVE / INVALID verdicts. A successor test receives a new identity rather than rewriting the parent outcome.

3. **Macro — failure-salvage / research-memory loop**  
   Retained failures, diagnostics, parameters, and outputs can later be re-read as constraints or discovery data for a new representation.

4. **Experimental handoff**  
   When public data and simulation no longer provide the decisive physical measurement, the next step belongs to laboratories, organizations, equipment, calibration, and domain expertise.

The broader enabling conditions include expanded individual research bandwidth, freedom to fail, failure preservation, failure salvage, AI–external computation feedback, and explicit experimental handoff.

The central methodological proposition is deliberately narrower than a claim that AI “automates science”:

> **AI can change not only the cost of successful experiments, but also the economics and future value of failed experiments.**

## Current audit status

The companion repository now contains a frozen lineage-coding protocol and an explicit stage-level audit.

For the standardized B19-B40 interval, audit v0.3 identifies **25 negative or limiting source stages**, of which **22 have an explicit downstream backward link**. The resulting **88.0%** value is treated only as a descriptive statistic of the coded BIG interval; it is not a general estimate of the value of failure. Audit v0.2 reported 84%; v0.3 recovered one explicit B29-T1-to-B30 successor edge while preserving the earlier audit.

Earlier B3-B18 records are being kept analytically separate because the later PASS / FAIL / INCONCLUSIVE / INVALID vocabulary was not yet consistently used. A provenance-corrected early audit now keeps four source-backed examples in the methodology manuscript (B6 retained-scan reuse, B12 mechanism redesign, B13/B13.1 interpretation correction, and B17-B18 readout enrichment). An additional elliptic-boundary measurement-redesign candidate remains supplementary because one previously quoted exact exponent pair could not be recovered from an immutable source.

An exploratory temporal-development audit also compares the documented B19-B26 and B27-B40 epochs. Explicit backward linkage is 10/13 (76.9%) in the earlier standardized epoch and 12/12 (100%) in the later epoch. The direction is compatible with increasing reuse, but the comparison is not statistically persuasive (Fisher two-sided p≈0.220) and improved documentation itself is a major confound. The methodology paper therefore does **not** claim that failure reuse has been proven to increase over time.

A separate retained-artifact timestamp audit covers 14 comparable source-result-to-successor-freeze transitions. Their median recorded interval is about **1.20 hours** (IQR **0.49-2.03 h**), but there is **no evidence of monotonic shortening over time** (Spearman rho≈0.051, p≈0.864). Thus the later programme is more explicit about research-memory linkage, but it is not shown to be faster at converting a negative outcome into a successor frozen protocol.

Working methodology manuscript:

https://github.com/Jun-Lucis/failure-preserving-research/blob/main/paper/manuscript_v0_13.md

## Evidence linkage

The methodology repository points back to concrete BIG records, including retained FAIL, INCONCLUSIVE, implementation-invalid, diagnostic, and prospective PASS histories.

A historical FAIL is never retrospectively promoted merely because it later became useful. The companion repository explicitly distinguishes:

```text
archived failure -> discovery / redesign
fresh frozen test -> validation
```

Representative case-study chains currently include B25, B27–B29, B32–B36, B37–B40, including the later shift from fragile absolute timing observables toward relative and relational timing.

## Publication architecture

```text
Methodology paper (Zenodo)
        <->
Methodology GitHub repository
        <->
BIG-theory GitHub repository
        <->
BIG papers / data / reproducibility archives (Zenodo)
```

The methodology-paper DOI will be added after the first formal release.

## Scope boundary

The companion project does **not** claim that retained failures automatically become useful, that unlimited computation is free, that AI-generated reasoning is self-validating, or that individual computational research replaces organized experimental science.

Human verification, compute, error control, public-data limitations, and the need for new physical measurements remain real constraints.

The methodological claim is narrower: AI-assisted individual research can increase effective research bandwidth, while disciplined preservation can give part of the historical search path nonzero future scientific value.
