# B13 recovered computational source

Original computational source: `Untitled66.ipynb`, preserved in the complete [B13 Version 1.1 archive](https://zenodo.org/records/23392538).

`B13_recovered_functions.py` contains eighteen unchanged computational function bodies recovered from the original notebook. `reproduce_b13.py` configures output paths and invokes the original functions without running Colab mounts or the two notebook cells containing pasted output logs.

Requirements: Python 3, NumPy, pandas, SciPy and Matplotlib. The original runtime environment was not sealed; the archive preserves original source, parameters, data, figures and audit evidence.

From this directory, an explicit opt-in invocation is:

```sh
python reproduce_b13.py --stage baseline --output rerun_baseline
```

Other stages: `sweep`, `robustness`, `observer`, `self`, `noise`. The stage names invoke the original experiment parameters documented in the adapter and notebook. Computational cost varies. Imports do not start experiments.

**基本的に再現可能。独立した再実行監査は未了**

Reproduction is supported in principle; independent rerun auditing is not yet complete. The October 2026 audit compared saved data and static source (86 groups / 4508 values) and did not generate new simulation trajectories. [Audit](../../docs/B13_publication_audit_2026_10_15.md) · [Methods and source clarification](../../docs/B13_methods_and_source_clarification_2026_10_15.md).
