# B14 recovered computational definitions

Source: original `Untitled68.ipynb`, SHA-256 `773954ea7ca5bc6db5f8a1d44aa0ce8e170bb88cf6d9813a6bbeb08068e878d5`. The full unchanged notebook and all original data are in [Zenodo v1.1](https://zenodo.org/records/23400901).

38 computational function definitions / 31 unique names were extracted without changing their bodies. The adapter supplies local file I/O and imports. Python 3, NumPy, pandas and Matplotlib are required.

```bash
python code/B14_recovered/replay_b14.py --mode definitions --output b14_definitions_check
```

This only loads definitions. To execute the stable-paper workflow explicitly:

```bash
python code/B14_recovered/replay_b14.py --mode full-run --output b14_replay_output
```

The superseded unstable fusion attempt remains in the recovered source for provenance; full-run skips it and executes original stages 1, 3, 4, 5 and 6. It generates new stochastic simulations and was not run in CP19.

For saved-data verification, download and extract the complete Zenodo ZIP and run `python verify_b14_saved_results.py` and `python compare_b14_public_archive.py` from that package. Those tools need the archived arrays and original notebook included there. Their receipts are also under `docs/B14_CP19`.

Assessment: basically reproducible; an independent full rerun audit has not yet been completed.
