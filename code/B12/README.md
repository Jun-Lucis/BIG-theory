# B12 recovered numerical source

The recovered simulator, full parameters, seed rule and saved data support reproduction in principle. Independent from-scratch rerun auditing is not yet complete. See [methods](../../docs/B12_methods_and_scope_2026_10_15.md), [source provenance](../../docs/B12_source_recovery_2026_10_15.json), and the [complete archival supplement](https://zenodo.org/records/23391364).

`B12_refined_core_extracted.py` copies pure function bodies from zero-based cells 0 and 16 of the original `Untitled65.ipynb` (Drive ID `1pvE787dKmTanQA6yi4PgST2_M16sxhza`); imports/version constants are packaging additions. No scan runs on import. The original notebook and exact historical cells, including scan/checkpoint/summary code, are in the supplement.

To configure the refined model, read `B12_1d_refined_d2_params.json`, copy `p_base_ref`, then update it with `D2_MID_BARRIER`. The canonical function is `simulate_unified_one_B12_1d(seed, rho, amp_I, sigma_R, p_config, keep_trace=False)`. The archived runner overwrites returned code-version fields with the refined run's version identifiers; the core retains the original B12.1d function's identifiers. The corrected protocol file records settings and a commented loop; it is not itself a full launcher.

Historical `CODE_SHA16` fields hash version-name strings, not code bodies. The source receipt provides current notebook/cell/function SHA256 values. Historical environment details and exact executed-byte authentication are still audit items. No stochastic trajectory was run for this audit. Original data and outcome labels are preserved. For arithmetic-only verification, use `audit_b12_saved_data.py` and the unchanged saved-data layout in the supplement.
