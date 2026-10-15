# B15 methods and representation clarification - CP20

Date: 16 October 2026 JST. **Basically reproducible; an independent full rerun audit has not yet been completed.** Original scientific results, published figure panels and diagnostic labels are preserved. No new stochastic trajectories were generated in this audit.

## Original source and exact input

Three original computational notebooks were recovered: `BIG_B15_colab_analysis_v1.ipynb`, `BIG_B15_cell3_boundary_history_colab.ipynb`, and `BIG_B15_cell4_map_classification_colab.ipynb`. The complete archive contains their unchanged bytes. `recovered_code/source_provenance.json` identifies every function by notebook, cell, line and SHA-256. There are 36 computational definitions and 32 unique names; function bodies are unchanged. I/O is provided by a separate local adapter.

B15.3 used the actual B14.0 256-point histories, not the optional fallback profiles. The saved B15 arrays agree with the recovered `B14_0_memory_profiles.csv` columns `stimulus_shape`, `post_write_memory`, and `final_memory`. That dependency is included under `sources/B14_dependency`, with provenance and SHA-256. The former public script can fall back silently to different toy profiles without the file. The recovered adapter requires an explicit archived input and raises an error if it is absent or incomplete.

The original 25 result files include 10 CSVs (5,494 rows), four JSON summaries, ten figure PNGs, and the earlier analysis ZIP. The source inventory is authoritative. The former public package uses `purity` for the original cloud metric `purity_Tr_rho2` and reserializes some inputs. All 24,217 common numeric CSV values match after that explicit column-name mapping. Historical copies are preserved without rewriting them.

## Density representation retains an angular moment

The cloud uses 721 equally spaced points on [-pi/2, pi/2], including projectively duplicated endpoints, and normalized weights proportional to exp(-d_pi(theta,0)^2/(2 sigma^2)). Width is the prescribed geodesic-Gaussian weight parameter, not a general measured width or the variance of a wrapped Gaussian. Response uses 361 angles from -90 to 90 degrees. Entropy is in nats, with eigenvalues floored at 1e-12 and renormalized; displayed zero entropy is rounded.

The real 2x2 cloud matrix retains only the second angular moment m2 = sum p_j exp(2 i theta_j). Its entries are [(1+Re m2)/2, Im m2/2; Im m2/2, (1-Re m2)/2] and purity is (1+|m2|^2)/2. The half-angle history embedding retains only the first angular moment m1 = integral w(s) exp(i s) ds, with the same matrix formula. History purity and circular concentration are therefore algebraically linked.

These representations are lossy. H1=1+0.4 cos(2s) and H2=1-0.4 cos(2s) are distinct nonnegative histories with the same I/2 matrix, L1, L2 and peak. An amplitude/matrix pair does not reconstruct an arbitrary history. Uniform weights for zero nonnegative mass are a numerical fallback convention.

## Kernel comparison and optimality scope

B15 fixes the pooled B13.1 kernel kappa=3.7410978332842775 and c=0.0033597884949152297. It compares 721 equally weighted angles from -90 to 90 degrees in 0.25-degree steps. The RMSE values are in-sample approximation errors to this logistic curve, not held-out prediction errors. The five-coefficient feature fit has more flexibility than the two-coefficient affine fit and does not select a physical theory by fit error alone.

The original constrained search uses 1,001 A values and 1,001 feasible B values per A. For this particular kernel and sampled quadratic objective, an additional convex optimality certificate verifies A=B=0.5 on the continuous feasible coefficient region. The gradient is approximately (0.0023429833, -0.0480379952), with nonnegative active-constraint multipliers (0.0251904892, 0.0228475059); the Hessian is positive definite. This does not establish the same optimum for other kernels or angular weights. The archived table remains unchanged.

The feature-fit validity flag originally checked sampled bounds. An additional degree-four polynomial critical-point check in x=cos(2 delta) establishes continuous bounds [0.0246247516645, 0.9746828224392] for the saved fitted coefficients.

## Map fixture and relationship to B14

The original map diagnostic is deterministic, uses N=256 periodic points and lambda=1.7, and tests one fixed profile pair (plus one fixed pair of joint fusion inputs). Norm means sqrt(ds sum H_j^2); relative denominators include +1e-12. Scores sum additivity and homogeneity errors. The translated affinity test subtracts F(0). Labels use thresholds 1e-10, 1e-3 and 0.15; they describe the fixture and do not certify every input or a physical quantum channel. All original labels remain unchanged.

The illustrative B15 fusion is (A+B) exp[-0.5 AB/(q^2+1e-12)] (1-0.35 r), q=max(max(A+B),1e-12), with nonnegative normalized overlap r. It omits B14's stable-map heat smoothing and exact global output-norm renormalization. The B15 linear division diagnostics also omit B14 noise, nonnegative flooring and daughter smoothing.

The saved fusion score 0.0002183245 comes from weak-overlap inputs. For the unchanged map, the additional deterministic joint inputs (1,0) and (0,1) instead give relative additivity error 0.7433053: separate outputs sum to 2, while the combined output is approximately 1.3 exp(-1/8). This demonstrates nonadditivity and limits the fixture's 'approximately linear' label; it does not relabel or change the archived experiment.

## Verification and replay

From the extracted complete ZIP:

```bash
python verify_b15_saved_results.py
python compare_b15_public_archive.py
python supplement/replay_b15.py --mode definitions
```

The first command verifies archived inputs, density matrices, metrics, response curves, fitted coefficients, the original deterministic map fixture, and function provenance. It passed 142 groups / 15,935 values. Additional scope diagnostics are separately identified in its JSON receipt. The second compares prior public CSVs with original output (24,217 values). The third only loads definitions and runs no experiment.

Explicit full numerical regeneration is available via `python supplement/replay_b15.py --mode full-run --output b15_replay_output`. It uses separate namespaces for the original stages, local output paths, and the archived B14 dependency. Full regeneration through every original stage and the upstream B14/B13 stochastic experiments was not performed as an independent audit here.

Repository: https://github.com/Jun-Lucis/BIG-theory
