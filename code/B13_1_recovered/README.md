# Recovered B13.1 computational source

These function extracts and the portable I/O adapter come from the recovered `Untitled67.ipynb`. Computational bodies are unchanged; provenance for 31 definitions / 30 distinct names is in `recovered_code/source_provenance.json`.

Run `python replay_b131.py --mode definitions --output replay_output` to load definitions without executing experiments. To reproduce saved-input fits, supply `--mode saved-analysis --data /path/to/original/data --output replay_output`. Use the recorded collapse tables to preserve half-bin ties. The full stochastic workflow requires explicit `--mode full-run`; it was not run in this audit.

The complete original notebook, all data, figures, clarified PDF and instructions are provided in the [single complete Zenodo ZIP, version 1.1](https://zenodo.org/records/23400328). Read its methods clarification before comparing covariance claims, redundant c/bias parameters, centroid widths or RMSE aggregation. Original runtime locking was not recovered; audit environment versions are documented.

基本的に再現可能。独立した再実行監査は未了。
