# B18 CP23 implementation and interpretation clarifications

Assessment: **Basically reproducible; an independent full rerun audit has not yet been completed.** Original outputs, diagnostic labels and solver bodies are retained.

The authoritative source inventory records five original B18.0--B18.4 notebooks and 124 saved result files (19 CSV / 6,415 rows, nine JSON, 85 PNG, four old ZIP and seven text/outline files). There are 76 recovered top-level computational definitions with 31 distinct names, including nine nested definitions within their unchanged bodies. Five separate namespaces retain repeated function names. Setup, backup, file-discovery and plot-only helpers are excluded from that count. Original ordered code cells and their execution counts are also retained.

## Dynamics and diagnostic operators

The actual read-phase inhibitory term is `-kappa * m * max(u*(1-u),0)`, throughout the spatial field. The external drive is `read_amp * read_profile * max(u*(1-u),0)`. The diagnostic read window W and threshold/gradient gates do not gate inhibition in the PDE. The schematic operator is an empirical diagnostic projection, not an identity derived from that equation.

During writing, inhibition is off. The trace source is `beta * front_write_mask(updated_u) * write_profile`. The external write amplitude acts on the front drive and does not directly multiply the trace source. The mask is absolute centered front gradient times a threshold Gaussian, normalized by its spatial maximum when above 1e-15. The Gaussian write/read windows are peak normalized. The write profile is centered before the front update; the trace mask uses the updated front.

The endpoint-inclusive grid is 384 points on [-12,12], dx=24/383, dt=.004 explicit Euler. The endpoint Laplacian equals the nearest interior difference divided by dx². Parameters are Du=.045, Dm=.004, r=1, a=.28, u_thr=.5, beta=1.15, front-mask width=.10, initial front center=-3 and width=.28. Initial pre-evolution lasts3; write pulses1.3, inter-write gaps.8, write/read drive amplitudes.12/.10 and write width.35. Offsets are zero. The front is updated before trace, clipping u to[0,1.2] and m to[0,10]. The rightmost above-threshold location is linearly interpolated; no crossing yields NaN and a last-grid-point crossing yields the edge. This is a fixed-grid threshold front rather than a separately solved Stefan interface. No grid/time-step convergence study is included.

## Branches and information timing

Kept and erased branches share the read-start front field; the erased trace is zero. No trace is written during read, but the kept trace diffuses and decays. Each branch centers its external read drive at its own current front. Subsequent forcing centers therefore differ between branches. The suppression outcome R_erased_end-R_kept_end is the total effect of retained trace under this moving-drive protocol, not a difference at fixed forcing paths. The auxiliary u difference samples two branch-specific terminal windows.

Path diagnostics use the realized kept-branch front, field, gates and retained trace. They are retrospective response-time variables, not predictors available solely from read-start data. A stronger in-sample fit may benefit from shared response-path information and endogenous geometry. Gate-fit correlation does not independently establish a complete causal mechanism. Zero-coupling controls are exact deterministic implementation checks; they do not identify the preferred projection.

Path integrals accumulate instantaneous values *dt at every left endpoint before the PDE step. Sparse recorded traces are not the integration mesh, and cumulative values in a nominal sample include that first increment. Complete field trajectories are not retained for every case, so path exposures cannot all be independently reconstructed from the saved endpoint tables alone.

## Statistical population and comparators

B18.0 and B18.1 have432 cases (324 nonzero kappa); their common numerical outcomes match. B18.2 and B18.3 have1296 cases (972 nonzero kappa), adding read durations2/3.2/4.5; their common outcomes match. Gate evaluation does not change the PDE. These stage comparisons are not independent validation sets.

All regression R² values are in-sample least squares with an intercept on kappa>0. Variables are standardized for the multivariable tables. B18.0's `global_trace_mass_only` uses unscaled m_total (R².345476); B18.1's same label uses kappa*m_total (R².495546). B18.2/3's `global_mass_only` again uses unscaled m_total (R².328833). Local/path loads include kappa. The comparators therefore have different information and scaling, and their changing values are not evidence of a changed front mechanism.

B18.2's threshold gate sigma is.10 (R².793347). B18.3's best single threshold raw gate sigma.15 gives pooled R² about.807, chosen from83 candidates on the same outcomes. Fifteen robustness slices fix one value of alpha/read width/read duration/kappa/rest delay, overlap, and refit their own line. Slice means/minima are descriptive, not held-out or selection-adjusted scores. No uniqueness or universal-optimum claim follows. Full reduced ranks including intercept are12/14,16/18,20/22,25/27. Protocol dummy/intercept and geometric dependencies preclude unique coefficient interpretation.

The historical B18.4 synthesis mostly uses literal rounded fallback rows and optionally substitutes a discovered B18.3 ranking. Its table is retained as source output and checked separately against stage tables. It is not a new simulation or independent recomputation. B17's quoted.994 is a historical synthesis comparator; its differing probes, scalar/PDE stages and response conventions are not collapsed into a common B18 observable.

## Figures, manuscript and missing source comparisons

Three original scientific tables retain their values, and all seven figure rasters retain their RGB pixels from the supplied historical English PDF. None is claimed RGB-identical to the saved Drive PNGs at native dimensions. The B18.3 notebook has unexecuted plot/package cells and its Drive folder has five CSV/JSON files, no PNG/ZIP. Its three manuscript figures are preserved from the PDF. The editable v0.2 TeX was reconstructed from that supplied PDF; the original Zenodo ZIP/source comparison remains pending. Historical English/Japanese v0.1 PDFs are preserved; the Japanese text is not a v0.2 translation.

## Portable execution and completed checks

From the complete prepublication package root:

```bash
python supplement/replay_b18.py
python verify_b18_saved_results.py
```

The first command only loads definitions. The second applies original analysis cells to saved CSVs and checks unchanged bodies, endpoint differences, coordinate identities, controls, compact tables and common-case outcomes. It passed604 numerical check groups /314,972 values plus44 categorical checks. Counts include repeated representations and identities, not independent experiments. No PDE or stochastic trajectories were generated.

Full regeneration is explicit and may be expensive:

```bash
python supplement/replay_b18.py --mode full-run --stage 0 --output NEW_EMPTY_DIRECTORY
```

Stages0--3 execute original numerical/analysis/figure cells with local I/O replacing Colab setup, mounts, backup and packaging. Stage4 is saved-input synthesis and requires actual archived CSVs via `--source-dir`; local discovery is strict and replaces silent archive lookup. Its optional B18.3 ranking substitution can retain more precision than the historical rounded fallback. Default source directory in this package is sources/drive_run; the GitHub code-only mirror requires the extracted source directory explicitly for stage4. No independent end-to-end full-PDE regeneration audit has yet been completed.

## Publication state

The historical citation is10.5281/zenodo.22690970. A new B18 Zenodo draft has not been created in this checkpoint. Its metadata candidate includes the repository URL in description and as References/URL/Other, preserving existing related identifiers once retrieved. Old public ZIP/metadata comparison, publication, and public redownload verification remain pending. The prepublication ZIP is a snapshot of currently recovered material; freeze a publication ZIP only after the remaining old-source comparison.
