# B17 recovered definitions and local I/O

37 unchanged computational definitions / 27 unique names are retained in five namespaces, including nested bodies. Setup, backup/search and plot-only helpers are excluded from that count. The prepared complete v1.1 ZIP contains five unchanged executed notebooks and all 153 original result files. Its Zenodo publication is pending after a service error; the current published record remains https://zenodo.org/records/22677581.

Python, NumPy, pandas and Matplotlib are required. From the repository root:

```bash
python code/B17_recovered/replay_b17.py
```

This defaults to definitions only and executes no dynamics step. Explicit regeneration uses `--mode full-run --stage 0|1|2|3|4|all --output NEW_DIRECTORY`. Stage 2 also requires `--inputs` pointing to actual B17.1 pair/state CSVs, available in the prepared complete ZIP. It has no toy fallback. The archive adapter defaults to its archived inputs; this GitHub mirror does not duplicate binary/CSV archives. The output must be new/empty.

The adapter replaces Colab setup, mounts, file I/O and original packaging cells with local I/O. It retains original numerical and analysis cells, equations, update order, clipping and time conventions. Separate namespaces retain repeated function names. Stage-2 saved-input analysis/plots were tested; full PDE/reduced-dynamics regeneration has not been independently audited end to end.

Methods: `docs/B17_CP22_METHODS_CLARIFICATIONS.md`. Receipts: `docs/B17_CP22/`. Complete saved-output checks contain 7,670 groups / 22,429 values; no new dynamics trajectories were run in this audit. Assessment: basically reproducible; an independent full rerun audit has not yet been completed.
