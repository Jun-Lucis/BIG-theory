# B16 recovered computational definitions

The five unchanged executed notebooks and all 85 original result files are in [Zenodo draft v0.4](https://zenodo.org/records/23402231). Their code cells exactly match the five earlier public notebooks. `recovered_code/source_provenance.json` records notebook hashes, cells and unchanged bodies of 12 top-level computational definitions / eight unique names, including nested function bodies. Setup I/O and plot-only helpers are excluded from that count. Separate namespaces retain repeated names.

Python, NumPy, pandas and Matplotlib are required. From the repository root:

```bash
python code/B16_recovered/replay_b16.py --mode definitions
```

This only loads functions; it executes no PDE step. Explicit regeneration of a stage:

```bash
python code/B16_recovered/replay_b16.py --mode full-run --stage core --output b16_replay_output
```

Other stages: intervention, locality, moving, robustness; all selects all five. The adapter executes original numerical/analysis cells with local I/O. Full regeneration was not performed as an independent audit in CP21. It retains original pulse gating, update order, clipping and time-label conventions rather than substituting the earlier manuscript's different writing law.

For saved-output verification, extract the complete Zenodo ZIP and run `python verify_b16_saved_results.py` and `python compare_b16_public_archive.py`. They require the original notebooks and archived data provided there. Receipts are mirrored under `docs/B16_CP21`.

Assessment: basically reproducible; an independent full rerun audit has not yet been completed.
