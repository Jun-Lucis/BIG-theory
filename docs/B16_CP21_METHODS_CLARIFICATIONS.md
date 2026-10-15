# B16 source/implementation clarification - CP21

Date: 16 October 2026 JST. **Basically reproducible; an independent full rerun audit has not yet been completed.** No new PDE or stochastic trajectories were generated. Original result arrays, scientific table values, seven published image composites and archived diagnostic labels are preserved.

## Exact source and archive scope

Five original executed Colab notebooks were recovered. Their code-cell sources exactly match the five notebooks already in the former public archive, which omits most execution outputs. Twelve top-level computational definitions (eight unique names, including their nested bodies) are extracted unchanged into five namespaces. Setup I/O and plot-only helpers are excluded from that count. Original numerical/analysis cells and call parameters are retained separately. The local adapter supplies I/O and runs no experiment by default.

All 85 original result files are included: 21 CSVs / 45,834 rows, 14 JSON files (including package manifests), 45 PNGs and five earlier analysis ZIPs. Of these, 68 are byte-identical to a counterpart in the former public archive. Four PNG counterparts differ in bytes and are kept separately; 13 files were absent, including the detailed robustness metrics, prehistory metrics and summary. All 520,038 numeric values in the 19 common CSVs agree. Historical copies are kept unchanged and clearly distinguished from the current clarified manuscript. The old Japanese reference PDF remains historical and has not been revised to this English clarification.

## Implemented history-writing law

In the archived simulations, the pulse source is a(t) G(x), where G is a Gaussian normalized by its sampled maximum. The write term is **beta B_sigma G(x) 1[a(t)>0]**, additionally gated by the memory/write flags. It is not beta B_sigma a(t) G(x). The earlier manuscript equation multiplied writing by S_pulse; the clarified equation gives the actual gated writing convention without a direct amplitude factor. This corrects the description rather than changing the solver or retrospectively substituting another equation's results.

The mask is exp[-(phi-phi_thr)^2/(2 phi_width^2)] times |grad phi|/(max |grad phi|+1e-15) when the maximum gradient exceeds 1e-15. If not, the original code leaves the Gaussian factor unweighted. This exceptional branch is recorded as a numerical convention, not a different model claim.

The core and alpha/etaS scan permit decay feedback mu_eff=mu0/(1+etaMu m), with etaMu=0.5 by default. The scan uses N=320 and a 40-step recording interval instead of the core's N=384 and 25-step interval. It enables feedback only for etaS>0, simultaneously activating the decay channel; that zero-to-positive comparison does not isolate source feedback alone. The kept/erased, locality, moving-frame and robustness probes explicitly use etaMu=0 and disable writing during the second pulse. Feedback is off during their shared prehistory, and phi is copied identically before retaining or erasing m. For these staged probes, etaS=0 therefore gives identical phi branches by construction; the zero control checks this implementation identity.

## Threshold boundary and numerical scheme

The code evolves Eulerian arrays on N equally spaced points including both ends of [-8,8], dx=16/(N-1), with zero exterior edge flux. It uses explicit Euler updates, edge-averaged mobility and cubic edge-gradient flux, a no-flux three-point Laplacian for m, centered interior gradients and one-sided endpoint gradients for the writing mask. Each step updates/clips m to [0,20] before using the updated m in the phi update, then clips phi to [0,2]. No claim is made that these safeguards are inactive between saved snapshots. The gamma cubic-gradient flux is a nonlinear second-order diffusion term, not a biharmonic fourth derivative.

The mobility floor is strictly positive: D(0)=D0 epsD=0.0012 for baseline values. Thus the reported 'free boundary' is an interpolated threshold level set, not a demonstrated compact-support boundary or Stefan interface. Boundary interpolation uses the outermost sample above phi_thr=0.030. A finite ten-unit base-source warm-up precedes the main experiment; it is not certified equilibration.

Pulse intervals are tested inclusively at main times [2,5] and [16,19]. Snapshots/trajectory rows are recorded before each update. Loops that run through steps+1 perform an additional update after their final labelled trajectory row; the core 'final' profile bears the nominal final label but contains that extra step. Integer step counts truncate nonintegral duration/dt. These original conventions are retained for replay, including the time-step variants. They are reasons not to infer formal convergence from the small sensitivity grid.

## Diagnostic definitions and frame

Core increments subtract the mean over [15.5,16] from the maximum over [16,19]. In B16.2-B16.5, the historical column phi_before_probe instead averages [16,16.2], which includes stimulus onset; its increment is max_[16,19] phi minus that onset mean. This is not an instantaneous pre-stimulus value. The R increment uses the same windows. All original table values and column names remain available; captions and methods now clarify this convention.

The phi readout is at the nearest grid point to the probe center. The history load is the discrete Gaussian-weighted mean sum(m G)/(sum G+1e-15); the two are different sampling operations. Kept-minus-erased subtracts these legacy increments, and the ratio uses the erased increment plus 1e-15. These are model-internal causal interventions on the retained field under the specified dynamics, not empirical memory measurements.

The core boundary offset subtracts mean R over [1.5,2] from mean R over [15.5,16], rather than measuring a final displacement after relaxation. It includes ordinary boundary drift.

The history m stays on the fixed Eulerian grid and decays/diffuses after writing; the solver has no material boundary advection or intrinsic surface transport. The plotted branch coordinate y=x-R_probe subtracts the threshold location at probe start and is fixed during that probe. The additional recorded y_probe_now=x_probe-R(t) uses the current boundary. Replotting in y does not itself move history or establish transport by the boundary. B16.3 and B16.4 repeat the same deterministic locality design with added frame diagnostics. All 840 common numeric pair-metric values match; this is not independent validation across models or held-out data.

## Fits and robustness scope

Locality R^2=0.9935 and r=0.9967 summarize a pooled in-sample ordinary linear fit with intercept over the 28 nonzero-feedback conditions (four forgetting rates, seven shifts, etaS=10). Robustness R^2 about 0.988 uses the 24 nonzero-feedback cases across 12 variants and two forgetting rates. The forcing already contains etaS m, so these correlations quantify the chosen model's response organization; they are not independent empirical validation, a universal linear law, or held-out prediction.

The robustness protocol tests 12 variants and three conditions per variant at shift=0.25. It includes N=256,320,512 in addition to baseline 384, dt=0.0015 and 0.003 in addition to 0.002, Dm=0.003/0.012, stimulus widths 0.22/0.36 and mask widths 0.020/0.035. The positive sign and relative suppression are stable over these archived cases. They do not prove mesh/time convergence, a numerical error bound or absence of artifacts for the continuum model. Most robustness cases store summaries without their full trajectories, so this audit verifies reductions of available saved outputs rather than rerunning the PDE.

## Verification and explicit replay

From the extracted complete ZIP:

```bash
python verify_b16_saved_results.py
python compare_b16_public_archive.py
python supplement/replay_b16.py --mode definitions
```

Saved-output verification passed 691 groups / 37,334 values, including unchanged source bodies, trajectory-derived increments, paired controls, profile/frame identities, sampled history loads, pooled fits and robustness reductions. No PDE time stepping occurs in these checks.

To explicitly regenerate a stage, use `python supplement/replay_b16.py --mode full-run --stage core --output b16_replay_output`. Other stages are intervention, locality, moving and robustness; `--stage all` selects all five. This executes the original numerical/analysis cells through local I/O. Full regeneration was not run as an independent audit in CP21.

Repository: https://github.com/Jun-Lucis/BIG-theory
