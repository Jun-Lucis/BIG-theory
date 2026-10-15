# B17 source and implementation clarification (CP22)

Assessment: **Basically reproducible; an independent full rerun audit has not yet been completed.**

The archive preserves five executed notebooks and all 153 original result files, including ancillary B17.0. Its four previously published notebooks have identical code cells to the executed originals. Recovery retains 37 computational definitions, 27 unique names, in five separate namespaces, including nested bodies. Setup, backup, file search and plot-only helpers are excluded from that count. Original code, arrays, diagnostic labels, all three scientific table bodies and nine published image pixels are retained.

## Read windows and response definitions

| Stage | Model and sampling | Historical adaptive response |
|---|---|---|
| B17.1 | PDE, write and read at the fixed laboratory location R_initial - 0.05; Gaussian-weighted phi and m diagnostics | Difference of branch increments: max phi over read [0,2] minus mean phi over [0,0.2] |
| B17.2 | Reanalysis of the same 81 B17.1 rows, merged with 27 write-state rows | Identical B17.1 response; no new dynamics or independent population |
| B17.3 | Prescribed boundary motion, scalar response, 512-point auxiliary memory field; probe follows current R - 0.55 | Terminal kept-minus-erased scalar response at read time 3 |
| B17.4 | PDE, 384-point field; each branch's probe follows its current threshold R - 0.55 | Terminal difference of the two branch-specific Gaussian-weighted phi readouts at time 3 |

The B17.1 baseline is during stimulus onset. It is not an instantaneous pre-read state. Its fixed laboratory read window does not leave an unchanged trace as the boundary moves. B17.2 depth correlations are descriptive: boundary-mask writing, elapsed time, forgetting, diffusion and pulse count all change the retained history. A coordinate translation y = x - R_read does not transport memory. B17.3/4 use a different, following probe. Their branch-specific sampling locations can differ at the terminal measurement.

## Writing and feedback

For B17.1 and B17.4, history writing is beta times a boundary-layer mask times a maximum-normalized Gaussian while writing is active. External pulse amplitude does not multiply that history source. The amplitude does drive phi. B17.1 weights its Gaussian threshold-layer mask by normalized absolute gradient. B17.4 additionally normalizes the combined mask by its own maximum and evaluates it after the field update.

B17.1 source feedback is pointwise, S_read(x,t) times [1 + etaS*m(x,t)], after the memory update. The reported calls have etaMu = 0. B17.4 uses a scalar weighted mean m_local(t), sampled before each phi step, to amplify the entire probe source. Read-start load is a regression predictor, not a gain frozen throughout the read. No new writing occurs during readout. The etaS = 0 field-branch identity follows algebraically from the chosen uncoupled update rules.

## Reduced control and artificial transport

B17.3 prescribes boundary speed 0.155 during writing and zero during gaps/rest. During readout, q_dot = 0.030*(1 + etaS*m_local) - 0.10*(q - 0.155), and R_dot = 0.040*(1 + etaS*m_local). Its tabulated phi is this scalar q. The quartic spatial profile is a plotting diagnostic rather than a simulated phi field. Local-load coupling is built into the equations.

Original B17.3 read-memory decay is multiplied by zero; alpha acts during write/rest, while readout only diffuses memory. Its artificial advection linearly interpolates m(x - dR), with zero exterior values, during writing only. The step is 0.01, write duration 1.2, inter-write gap 0.8, read duration 3; memory is clipped below at zero.

B17.4 artificially shifts memory during writing, gaps and post-write rest, then stops this transport at read start. Read memory continues to forget and diffuse. Thus neither control continuously attaches memory to the moving boundary throughout reading. Shift interpolation may smooth or lose mass. Comparisons do not isolate a general superiority of new writing over continuous material transport.

## Numerical conventions

Both PDE stages use endpoints-inclusive x in [-8,8], N = 384, dx = 16/(N-1), dt = 0.002, explicit Euler, edge-averaged mobility and zero endpoint flux. D0 = 0.12 and epsD = 0.010 imply D(0) = 0.0012 > 0. The measured boundary is an interpolated threshold crossing at phi = 0.030, not an established compact-support or Stefan interface. The gradient-cubic term is in a second-order nonlinear flux divergence. No fourth-order regularizer is used. Fields are clipped to phi in [0,2] and m in [0,20].

B17.1 writes with beta = 3, Dm = 0.006, pulse duration 1.5, gap 3, write amplitude 0.030, read amplitude 0.025, width 0.28, and offset -0.05. Its loops record before updating and include an extra update after the final recorded row. The returned write state is one step beyond the final write/rest trajectory row. Read increments use the recorded grid, not that extra final step.

B17.4 uses cubic coefficient 0.00035, fixed decay mu = 0.11, pre-equilibration 10, pulse duration 1.5, gap 0.8, read duration 3, write/read amplitudes 0.020/0.018, width 0.28 and offsets -0.55. The order is phi update, optional history shift, then memory update. Selected representative read traces record initial time and sparse post-update points; they need not contain the actual terminal state used in metrics. All parameters and exact call cells are archived.

## Fits and evidence scope

B17.2 uses 54 nonzero-feedback rows, B17.3 uses 162 and B17.4 uses 108. Fits, standardized features and R2 are in sample. No holdout or external empirical test was used. Main global-mass-only comparisons omit etaS while the local-load predictor includes it; they do not exclude every global-history alternative. Adding predictors can improve training R2 without establishing prediction or a mechanism.

Full-reduced design ranks, including intercept, are 9/10, 11/14 and 12/14 columns in B17.2, B17.3 and B17.4. All protocol dummy columns plus an intercept, and dependent geometry coordinates, produce rank deficiency. Fitted predictions can be reproduced, while individual coefficients do not have unique independent interpretations.

Saved-output verification reapplies original analysis cells to preserved CSVs and checks original trajectory-derived summaries: 7,670 checks / 22,429 numeric values passed. The 15 common former-public/original CSVs match on 26,368 numeric values, including nested public ZIPs. All nine selected public images match original Drive images in RGB pixels. B17.2's local replay of analysis and plotting was tested without dynamics steps. Full independent PDE/reduced-dynamics regeneration, continuum convergence, biological applicability and intrinsic surface-history transport remain unestablished.

## Local use

From the complete archive root, run `python verify_b17_saved_results.py` for the saved-output checks. `python supplement/replay_b17.py` loads computational definitions only. Numerical regeneration requires explicit `--mode full-run`, `--stage 0|1|2|3|4|all`, and an empty or new `--output` directory. Stage 2 requires the original B17.1 pair/state CSVs; the default input is `sources/drive_run`, and no toy fallback is supplied. The adapter replaces Colab mount, file I/O and original packaging cells with local I/O, retaining original numerical/analysis cells. Full regeneration has not been audited end to end.

The Japanese v1.0 reference is historical and has not been revised. All-version DOI: https://doi.org/10.5281/zenodo.22677580. Historical v1.0: https://zenodo.org/records/22677581. Repository: https://github.com/Jun-Lucis/BIG-theory.
