# B18 recovered computational definitions

76 unchanged top-level definitions /31 distinct names are retained across five namespaces, with nine nested definitions inside the retained bodies. Setup, backup/file-discovery and plot-only helpers are excluded. The complete published archive contains five original notebooks and 124 original outputs: https://zenodo.org/records/23427115. Its public redownload is byte-identical to the frozen ZIP, with CRC and 182 internal hashes verified. The old public notebook code-cell sets and22 common data files are authenticated.

From the repository root:

```bash
python code/B18_recovered/replay_b18.py
```

Default behavior loads definitions only, with no PDE time stepping. Full regeneration requires explicit `--mode full-run --stage 0|1|2|3|4|all --output NEW_EMPTY_DIRECTORY`. Stages0--3 retain original numerical/analysis/figure cells with local I/O replacing Colab setup, mount, backup and package cells. Stage4 is saved-input synthesis and requires `--source-dir` pointing to actual extracted original CSVs; this code-only mirror does not include binary/data archives. Its strict local loading replaces silent package discovery. It may substitute a precise source B18.3 ranking for the original rounded fallback.

The fresh archive extraction passed default definition loading and reproduced the saved-analysis receipt byte for byte:604 groups / 314,972 values and 44 categorical checks. Independent full PDE regeneration has not been audited end to end. Original results and diagnostic labels are unchanged.

Assessment: **Basically reproducible; an independent full rerun audit has not yet been completed.** See `docs/B18_CP23_METHODS_CLARIFICATIONS.md` for the distinction between diagnostic gates and actual distributed inhibition, realized path information, branch-specific forcing, comparator differences and in-sample gate selection.
