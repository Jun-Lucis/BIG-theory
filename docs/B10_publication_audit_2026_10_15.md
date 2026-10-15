# B10 publication audit and archived-data supplement — 15 October 2026

**Current record:** https://doi.org/10.5281/zenodo.23386662. Version 1.1 identifies an added documentation/data supplement. The original eight-page manuscript is retained as v1.0; it has not been rewritten. **Original v1:** https://doi.org/10.5281/zenodo.20819427. All 16 original package files are preserved byte for byte.

## Result and evidence

The saved integer counts, replicate means/standard deviations/standard errors, public parameters, and all four manuscript tables agree within their recorded tolerances across 23 check groups. The four tables contain 141 numeric entries and five Boolean entries. All eight pages were visually inspected; the four embedded figures match the original archived PNGs pixel for pixel. The current original ZIP was freshly downloaded byte identical to the saved archive; its contained PDF matches the Drive and Library copies. The original standalone PDF's public checksum also matches; its first browser download did not materialize locally, so that attempted download is not counted as a separate byte verification.

I2 has 90 saved replicate rows (700 trajectories each), L2 has 360 (600 each), and B10.1 has 306 (700 each). These are archived results, not newly run trajectories. I2 peaks at 0.9142857143 and L2 dynamic_Rq at 0.91625, both at sigma=0.40. The largest I2/L2 difference remains 0.0290476190 at sigma=0.30. The retained `consistent` result and the J branch's `strong_difference`/exclusion are unchanged.

| Publication issue | Treatment |
|---|---|
| Missing replicate/source provenance in original compact package | Recovered counts and 11 source fingerprints added; complete historical execution authentication remains open |
| 21/90 compact L2 cells retain coarser precision | Separate full-precision count-derived table and explicit differences added; original CSV retained |
| Hit/hold relationship insufficiently explicit | Exact discrete predicates and the absence of a prior-hit requirement documented; code unchanged |
| B10.1 seeds recur across grid points | Disclosed; cross-grid independence is not assumed |
| Finite-grid width and zero-count interpretation | Sampling scope stated; no continuous-boundary or probability-zero theorem claimed |
| Original PDF citation placeholder and isolated section-10 heading | Retained as minor editorial issues in the unchanged historical PDF; current record citation supplied by metadata |

The compact L2 precision differences are at most 0.0000333333333332, within four-decimal rounding. Original counts and full summaries agree. Restoring the available precision in an additional table changes no underlying Monte Carlo outcome, peak finding, adopted claim, or original file.

## Event and implementation scope

[The methods note](B10_methods_and_event_definitions_2026_10_15.md) gives the actual canonical drifts, force and sequential discrete update. First hit requires d<=1.35 and R,q>=0.75. Hold uses d<=1.45 and R,q>=0.70 for 400 consecutive sampled updates at dt=0.005. The preserved sustained predicate does not require a prior hit flag. Aggregate n_sustained<=n_hit cannot prove per-trajectory set inclusion. The methods note's threshold counterexample is a logical example, not a new simulated trajectory.

Eleven recovered files match the historical loaded-source SHA-256 prefixes. Only eight are reachable from the canonical simulator; potential-related candidate functions must not be substituted for the adopted force/drifts. The exact sigmoid/summary utilities, full L2 control-dispatch runner, historical environment and full trajectory histories are not recovered. The B10.1 complete source-to-output chain also remains unauthenticated. This is a static/source-and-count audit, not independent simulator replication.

B10.1 contains 186 distinct seeds across 306 rows, with seeds recurring in 120 additional cross-grid rows. Each grid point's three replicate seeds are distinct. Reported pointwise statistics reproduce, but cross-grid independence is not inferred. The window width is last-minus-first sampled sigma with observed mean P>=0.5. Zero closed-control captures in 43,200 represented trials are observed counts, not an exact-zero-probability proof.

## Files and integrity

| File | Bytes | SHA-256 |
|---|---:|---|
| Unchanged original PDF | 440457 | `4c92d5a5012e105310fde08f3f730a1334279ec951167c1ad68f41f4917ffbd9` |
| v1.1 archived-output and methods supplement ZIP | 1478487 | `94156201c482a3e849763070aeceda44790d89e79e59fbc7aed5f694e668dc84` |

The supplement ZIP contains 66 files, including the original 16-file package, original ZIP, 38 recovered source/data records, a source-role map, the methods note, precision extension/difference list, checksum manifest, and read-only verifier. The verifier uses the Python standard library and never imports or executes the recovered simulators. A clean extraction reproduces the verification JSON. The release receipt records fresh post-publication file verification separately.

No new stochastic trajectory, PDE calculation, prospective success rule, or formal research verdict is introduced. B10 remains a reduced finite model of stochastic-resonance-like capture, not a quantitative nuclear-fusion theory.
