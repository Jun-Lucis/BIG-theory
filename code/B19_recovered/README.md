# B19 recovered source and saved-result checks

The integrated scope is B19.0 through B19.20, including 17a and 17b. Original notebook and output bytes are preserved under `sources/` in that complete archive. B19.21-22 and B19E are separate studies. Six later B19.21C files co-located in the historical B19.17b source folder are provenance only and are not integrated-study evidence.

The complete data and original notebooks are distributed in the Zenodo ZIP. With Python 3, NumPy and pandas, point this repository copy of the verifier at the extracted archive:

```bash
python code/B19_recovered/verify_saved_results.py --root /path/to/BIG_B19_v1_1_COMPLETE
python code/B19_recovered/load_definitions.py
```

The first command recomputes saved-data diagnostics and writes a JSON receipt under `audit/`. It does not integrate ODE/PDE trajectories. The second loads 22 isolated namespaces containing 449 unchanged top-level definitions. It executes no notebook experiment loops, Drive mounts or file-export orchestration. It is an inspection adapter, not a complete stage runner; provide notebook configuration globals and mapped inputs explicitly before calling recovered functions.

Canonical source selection and exact definition hashes are recorded in `audit/B19_Canonical_Source_Definitions.json`. Stage 2 uses the executed v1.3 notebook; stage 15 uses the larger executed v1.1 notebook. All 27 original candidates remain available. Raw notebook execution history contains errors, interruptions, Colab paths and checkpoint dependencies. Those histories have not been erased or represented as a successful fresh run.

The original `/content/drive/MyDrive/BIG_B19_colab_outputs/B19_N_run_001/<analysis>/` outputs correspond to `sources/drive_run/B19_N_run_001/` in this archive. Stage 14 package contents are additionally extracted under `sources/extracted_stage14/`. A fresh Colab run requires adapting paths and restoring stage configuration/input state. Independent end-to-end rerun audit is not completed.

Verification counts include checkpoint and input-copy repetitions; they are not independent experimental sample counts. Scalar `upstream_candidate` is a historical grouping containing retrospective final/median/minimum variables. The 27 mapped rows include a common seed on three rays. The 2D method is a training-scaled nearest-centroid rule with internal ray holdouts, not external validation.

Project: https://github.com/Jun-Lucis/BIG-theory  
Assessment: Basically reproducible from archived methods and saved outputs; independent rerun audit not completed.
