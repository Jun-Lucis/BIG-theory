# B15 recovered computational definitions

Three unchanged original notebooks and all original arrays are archived in [Zenodo v1.1](https://zenodo.org/records/23401700). `recovered_code/source_provenance.json` records notebook SHA-256, cells and the unchanged bodies of all 36 computational definitions / 32 unique names. Separate namespaces retain repeated function names. The adapter supplies local I/O; it runs no experiment on import.

Python 3, NumPy, pandas and Matplotlib are required. From the repository root:

```bash
python code/B15_recovered/replay_b15.py --mode definitions
```

This loads definitions only. Explicit full regeneration uses the archived B14 input:

```bash
python code/B15_recovered/replay_b15.py --mode full-run --output b15_replay_output --b14-profiles code/B15_recovered/inputs/B14_0_memory_profiles.csv
```

The adapter raises an error for missing/incomplete B14 input; no silent toy fallback is used. Full regeneration and upstream B13/B14 stochastic simulations were not performed as an independent audit in CP20. The original public regenerator remains in the historical Zenodo material.

For archived-output verification, download and extract the complete Zenodo ZIP, then run `python verify_b15_saved_results.py` and `python compare_b15_public_archive.py` from that package. The verifiers need the original notebooks and arrays included there. Their receipts are mirrored under `docs/B15_CP20`.

Assessment: basically reproducible; an independent full rerun audit has not yet been completed.
