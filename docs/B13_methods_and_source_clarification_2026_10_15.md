# BIG-B13 methods and source clarification — Version 1.1

This supplement accompanies the source-based restoration of the B13 manuscript. It preserves the original numerical results, classifications and scope. The original PDF, original 37-file result package and recovered Colab source are retained.

**Reproduction is supported in principle; independent rerun auditing is not yet complete.**

## 1. Published figures and the restored manuscript

The original 16-page PDF used reconstructed illustrations, as its Appendix A mentioned. Those illustrations are not identical to the original run PNGs; in Figures 1 and 2, the difference includes the represented basin-map domain and the shape of the baseline selection curve. They should not be treated as exact plots of the archived CSVs.

The corrected PDF restores all twelve figure panels. Eleven use the original Colab PNGs. Figure 3 is redrawn directly from the saved 48-cell RMSE table, with discrete tested values labeled on both axes. The original imshow extent treated nonuniform parameter grids as uniformly spaced. No table entry is changed. The inserted image canvases preserve aspect ratio; resampling and white padding are recorded.

The two broken gradient operators in equations (10) and (29) are repaired. The table of contents is updated to body page labels 1–16. A correction note precedes the body.

## 2. Actual binary update

The original functions use

$$
E_A(h)=a(\|h\|^2-1)^2+b h_+^2 h_-^2
-\lambda_{\rm obs}F_{\rm align}h^T\widehat H.
$$

The observer vector is normalized when nonzero. For example, the displayed axis (0.71,0.71) is the rounded label for (1/sqrt(2),1/sqrt(2)), not the exact vector passed with those rounded entries.

At each step, with independent standard two-dimensional normal vectors,

$$
\widetilde h_{n+1}=h_n-\eta\nabla E_A(h_n)
+\sigma\sqrt{\eta}\,\xi_n.
$$

The default implementation then applies componentwise projection onto the nonnegative quadrant, followed by a norm cap of 5. Both are part of the executed algorithm. The terminal outcome is + when |h_+|>|h_-|, − for the opposite inequality, and tie for exact equality.

This is a finite-step, finite-horizon projected stochastic model. The noise coefficient is multiplied by sqrt(eta) in code. A generic per-step noise symbol in the original equations should be read with that convention when referring to these runs. No fluctuation–dissipation or physical-temperature interpretation was tested.

The numerical experiments set F_align=1 and hold the observer axis fixed. They do not evolve spatial boundary fields or the joint system–observer equations. Equation (9)'s energy-decrease statement applies to deterministic gradient flow with a fixed energy landscape; a time-dependent external gate would add explicit energy dependence.

## 3. Saved protocol

| Stage | Parameters and sampling |
| --- | --- |
| Baseline | a=4, b=8, sigma=0.08, eta=0.01; 600 steps; 25 theta points; 300 trials per theta; seed 123 |
| Basin map | Same generator after the baseline curve; 31×31 initial-state grid on [0,1]^2; 40 trials per cell |
| Barrier/noise sweep | b=(0.5,1,2,4,8,16); sigma=(0,0.02,0.05,0.08,0.12,0.18,0.25,0.35); 400 steps; 17 theta points; 120 trials; seed reset to 123 for each condition |
| Seed check | Selected b=1, sigma=0.35; 400 steps; 31 theta points; 300 trials; seeds 101,202,303,404,505 |
| Observer sweep | Four normalized axes, six coupling strengths (0,0.05,0.1,0.2,0.4,0.8); a=4, b=1, sigma=0.35; 400 steps; 25 theta points; 240 trials; seed reset to 123 for each condition |
| Self fixed-point search | Main eta_update=0.05; 10 structured starts plus 80 random directions at radius 2; seed 123; minimization step 0.01, at most 3000 steps, gradient stopping threshold 1e-8, norm cap 20, merge tolerance 1e-2 |
| Self classification map | 25×25 eta/lambda grid; 10 structured plus 40 random starts per condition; at most 2000 minimization steps |
| Self-noise transitions | 8 noise levels × 4 starting basins × 300 trials; eta=0.01; 2500 steps; seed 123; initial Gaussian perturbation with coefficient 0.02; norm cap 20 |

Seed reuse produces paired/common-random-number comparisons. Repeated zero-coupling rows across observer axes are identical by construction and are not independent replications. The parameter sweep selects the lowest empirical RMSE; the seed check evaluates that selected regime on new seeds, not across new model classes. The reported RMSE standard deviation uses sample ddof=1. The shaded interval is the source's normal approximation mean ±1.96 SD/sqrt(5) across five seeds, not an exact binomial or simultaneous confidence band.

## 4. Self-observation energy and fixed points

With A=diag(A1,A2), the actual energy is

$$
E_B(h)=\frac{\alpha}{4}(\|h\|^2-1)^2
+w h_1^2h_2^2
-\frac{\lambda_s}{2}h^TAh
+\frac{\gamma}{4}\|h\|^4+\frac K2\|h\|^2.
$$

The recovered analytic gradient and Hessian agree with finite differences at the audit sentinels. The main parameters are alpha=1, w=2, lambda_s=0.5, gamma=0.5, K=0 and A=(1,0.8). Writing q=alpha+gamma=1.5 and c_i=alpha+lambda_s A_i−K, stationary points satisfy

$$
h_1[q h_1^2+(q+2w)h_2^2-c_1]=0,
\qquad
h_2[(q+2w)h_1^2+q h_2^2-c_2]=0.
$$

The four reported locally stable points are (±1,0) and (0,±sqrt(14/15)). Their energies and Hessian spectra reproduce the archived values. Four off-axis saddles and the unstable origin also satisfy the stationary equations. Therefore “four fixed points” in the main numerical summary describes the four locally stable minima found by the search, not the complete stationary set.

The classifier checks, in order: any negative Hessian eigenvalue among found points; discrete instability eta_update times maximum eigenvalue ≥2; multistability; rigidity; sensitivity; then stable. Its finite-search labels concern the set of returned points. In particular, at lambda_self=0, exact structured starts retain diagonal saddle points, giving the label “unstable” even though stable minima also exist. The original labels are preserved. Reconstructing this found-set interpretation from the analytic polynomial agrees with all 625 saved map rows; it does not independently rerun the search.

## 5. Meaning of noise persistence

The self-noise update uses the same sigma sqrt(eta) convention. The final basin is assigned by the larger absolute coordinate and its sign; an absolute-coordinate tie is assigned to the x basin.

The reported stay probability is

$$
P(\text{terminal basin label}=\text{initial basin label}),
$$

not the probability of never leaving the basin. Exit and return events are not resolved by the saved transition table. The 128 transition rows aggregate 9600 trajectories into 32 conditions; their probabilities, diagonal stay table and 4×4 high-noise matrix agree exactly up to CSV floating-point precision.

## 6. Source recovery and portable execution

Source: original Drive notebook Untitled66.ipynb, last modified 2026-06-30. Its SHA-256 and every extracted function fingerprint appear in B13_Source_Recovery.json.

The original notebook contains two output logs pasted into code cells (indices 9 and 11). Those are preserved in the original notebook; they are not computational model definitions and are skipped by the portable entry point. The extracted module preserves all eighteen computational function bodies exactly, omitting only notebook top-level experiment calls and the Colab-specific mount setup. The adapter supplies local file-output helpers without changing model functions.

Use a separate writable output directory:

    python supplement/code/reproduce_b13.py --stage baseline --output rerun_baseline
    python supplement/code/reproduce_b13.py --stage sweep --output rerun_sweep
    python supplement/code/reproduce_b13.py --stage robustness --output rerun_robustness
    python supplement/code/reproduce_b13.py --stage observer --output rerun_observer
    python supplement/code/reproduce_b13.py --stage self --output rerun_self
    python supplement/code/reproduce_b13.py --stage noise --output rerun_noise

Requirements: Python, NumPy, pandas and Matplotlib. The archive verifier additionally uses Pillow and PyMuPDF. The audit environment is recorded separately; the original dependency versions were not sealed.

The audit adds no stochastic trajectory and makes no change to the original scientific outcomes. B13 remains a reduced observation-like state-selection and self-model stability study. Its Born-like curves are reference comparisons; no quantum measurement, Born rule or consciousness derivation is claimed, and this present scope does not rule out separately testable future extensions.

Project repository: https://github.com/Jun-Lucis/BIG-theory

