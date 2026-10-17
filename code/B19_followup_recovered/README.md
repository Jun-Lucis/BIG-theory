# B19.21-22 recovered source and saved-result verification

The complete release preserves the original public archive, its seven stage packages, 18 recovered notebook candidates and 98 recovered Drive result files. Published scientific numbers, figure rasters, table cells and formal claim statuses are retained.

The complete source/data are in the Zenodo ZIP. With Python 3, NumPy and pandas, point this repository verifier at that extracted archive:

```bash
python code/B19_followup_recovered/verify_saved_results.py --root /path/to/BIG_B19_21_22_v1_1_COMPLETE
python code/B19_followup_recovered/load_definitions.py
```

The verifier performs saved-data recomputation only and generates no ODE/PDE trajectories. Its receipt contains 2,100 check groups / 85,045 numeric or label comparisons. These include shared input and repeated checks, not independent samples. Full histories mean complete saved scalar diagnostics, not every three-dimensional field at every internal solver step.

The loader exposes 258 unchanged definitions in 10 separate namespaces and runs no notebook experiment loops, mounts or export orchestration. It is an inspection adapter; invoking recovered functions requires the original stage globals and inputs. Ordered runtime settings and exact source-definition hashes are in `audit/`. The original Colab paths and historical execution state require adaptation for a fresh run.

Final effective function syntax trees match the 10 original public notebooks. Top-level setup/export cells, duplicate `dz` definitions, checkpoint behavior and execution histories differ and are preserved. B19.21-A/B source notebooks have not been separately recovered; the archived 21B CSVs support the algebraic cone-table checks and retained 1/3 coarse and 0/3 refined ordering results.

The complete C archive includes historical recovery computations of missing cases. The 57 saved recovery readouts are audited as historical records; this verifier does not independently integrate those cases. D/E/F reuse the same 38 diagnostic histories. Deterministic thinning is a sampling-sensitivity test, with no independent PDE convergence or external-validation claim.

Assessment: **Basically reproducible at the archived methods and saved-output level; independent end-to-end rerun audit not completed.**

Project: https://github.com/Jun-Lucis/BIG-theory
