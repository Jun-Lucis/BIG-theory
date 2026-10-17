# B20 recovered definitions and saved-result audit

The complete Zenodo archive contains the clarified paper, 11 recovered B20 notebook candidates, 1,692 Drive result files, the inherited B19.22-C solver notebook, immutable original public ZIP and two extracted stage packages.

With Python 3, NumPy and pandas, point this repository copy at the extracted complete Zenodo archive:

```bash
python code/B20_recovered/verify_saved_results.py --root /path/to/BIG_B20_v1_1_COMPLETE
python code/B20_recovered/load_definitions.py
```

Saved-data recomputation passes 9,052 check groups / 157,400 numeric or label comparisons. It checks 455 saved scalar-diagnostic histories / 36,855 rows, including shared cases and overlapping checks rather than independent observations. No ODE/PDE integration is performed. Formal outcomes remain B20.4 PASS, B20.5 PASS, B20.6 INCONCLUSIVE.

The definition-only loader exposes 137 unchanged top-level definitions in four namespaces (three B20 notebooks plus 25 inherited solver functions). It runs no notebook acquisition orchestration or Drive mounts. Calls require original stage globals, parameter inputs and path adaptation. The 24 shared inherited core helpers have identical syntax trees. Earlier B20.2/3 candidates are provenance outside the integrated B20.4-6 evidence.

**Precision finding:** the B20.6 restart used a six-decimal Qw and twelve-decimal base. Its raw directions differ from the earlier high-precision Phase1B table by up to 2.87465058e-7 per component. The rounded basis orthonormality residual is 1.419049e-6. The verifier checks the actual 30-point restart manifest and consistent downstream 126-point scan manifest; it does not falsely certify identity with the high-precision table. The audit receipt records the difference separately. Its effect on fresh PDE outcomes is not independently recomputed.

The recovered notebooks retain historical assertions, runtime errors, repairs and checkpoints. The complete final refinement-acquisition writer was not separately located; the frozen bisection rule, six checkpoints and history support saved arithmetic verification. Historical hashes/timestamps establish internal provenance, not an independent certification of every execution's chronology.

Assessment: **Basically reproducible at the archived methods and saved-output level; independent end-to-end rerun audit not completed.** No independent continuum, new-family or external validation is claimed.

Project: https://github.com/Jun-Lucis/BIG-theory
