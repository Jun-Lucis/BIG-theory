# BIG-B10 archived methods and event clarification, supplement v1.1

Jun Lucis. Documentation audit: 15 October 2026.

This note documents archived code and saved counts. It does not introduce a new stochastic simulation, alter an event definition, or regrade the original I2/L2 consistency outcome. The eight-page v1.0 manuscript and all 16 files in its original package are retained byte for byte.

## Adopted implementation and source provenance

The archived L2 loaded-source manifest lists 11 extracted functions. Each recovered file matches the manifest's recorded SHA-256 prefix (16 hexadecimal digits); this supplement also supplies its newly calculated full SHA-256. Starting at `simulate_dynamic_channel_sigma`, the static call graph reaches eight of those functions:

`simulate_dynamic_channel_sigma`, `drift_R`, `drift_q`, `distance_acceleration`, `dynamic_channel_gate`, `close_gate_d`, `gate_above`, `gate_below`.

The same loaded list includes `phi_Rq_grad`, `distance_potential_and_grads`, and `distance_gate`, but those three are not reached by that simulator's call graph. They must not be substituted for the adopted drift and force functions. Other recovered simulator candidates are retained as historical forensic evidence, not promoted as the canonical I2/L2 model. The earlier J branch remains excluded from final quantitative claims.

The utility definitions `sigmoid_stable`, `safe_mean`, and `safe_median`, the complete L2 dispatch/runner, its software environment, and complete per-trajectory histories were not recovered. No replacement utility or runner is silently presented as historical code. Source fingerprints plus saved-output consistency do not authenticate the entire original execution, and this supplement is not a standalone simulation replay release.

## Drift and force in the recovered I2 body

Let S(z) denote the logistic gate intended by the archived gate calls. Define

$$
D(d)=S((d_{int}-d)/\ell_d),\quad
G_R(R)=S((R-R_{gate})/\ell_R),
$$

$$
G_{att}(R,q)=S((R-R_{att})/\ell_{att})S((q-q_{att})/\ell_{att}),\quad
H(d)=S((d_{fuse}-d)/\ell_{fuse}).
$$

The recovered default uses channel_power=1. The canonical drifts and distance acceleration are

$$
b_R(R,d)=-2A_RR(1-R)(1-2R)+H_RD(d),
$$

$$
b_q(q,R,d)=-2A_qq(1-q)(1-2q)+H_qD(d)G_R(R),
$$

$$
b_v(d,v,R,q)=-\gamma_dv+\frac{K_{rep}}{(d+\epsilon_d)^2}-A_{att}G_{att}(R,q)H(d).
$$

These are the adopted reduced dynamics. A joint gradient flow of the other archived potential functions is not assumed. In particular, the distance-force denominator is `(d + eps_d)**2`, and the canonical separation update uses a negative initial approach velocity; a different candidate's `d*d + eps_d**2` denominator or opposite velocity convention is not interchangeable with it.

## Sequential discrete update

With h=0.005, independent standard-normal arrays drawn in R, q, velocity order for currently active trajectories, and projection Pi to [0,1], the recovered body applies

$$
R'=\Pi(R+h b_R(R,d)+\sigma\sqrt h\,\xi_R),
$$

$$
q'=\Pi(q+h b_q(q,R',d)+\sigma\sqrt h\,\xi_q),
$$

$$
v'=v+h b_v(d,v,R',q')+\sigma_v\sqrt h\,\xi_v,\qquad d'=d+h v'.
$$

The q update uses the newly updated R. The distance force uses both new internal coordinates. Initially, `v = -v0 + sigma_v * Normal`, with v0=1.3 and sigma_v=0.02. The hard floor clamps d to 0.35 and replaces inward velocity by max(v,0); the numerical ceiling clamps d at 12 without a corresponding velocity reset. Already captured or escaped trajectories are no longer advanced. The RNG is NumPy `default_rng(seed)` in the recovered body; exact historical replay would additionally require the unrecovered runner and environment.

The parameter JSONs retain the other constants and all scan settings unchanged. I2 used 700 trajectories at each of five replicates per noise value; L2 used 600 at each of four replicates, for each of five controls. T=70 and 18 noise values were scanned. Control labels are dynamic_Rq, R_only, q_only, always_open, closed. Their archived outputs are verified; the missing full control-dispatch wrapper is not reconstructed here.

## Event predicates and their relationship

| Quantity | Exact archived predicate or rule |
|---|---|
| first hit | active trajectory, d<=1.35, R>=0.75, q>=0.75 |
| hold sample | active trajectory, d<=1.45, R>=0.70, q>=0.70 |
| sustained capture | 400 consecutive successful hold samples; a failed sample resets the counter |
| escape | after capture classification, still active, d>=8.8, v>0, and t>1 |
| timeout | neither captured nor escaped when the finite run ends |

The hold counter is evaluated on sampled discrete updates; it is not a continuous-path monitoring theorem. The recovered sustained-capture expression does **not** require a previously set first-hit flag. Consequently, no strict per-trajectory inclusion `sustained subset of first_hit` is asserted. As a logical predicate example, 400 samples at d=1.4 and R=q=0.72 satisfy the hold rule without satisfying the stricter hit rule. This is not a newly simulated trajectory or a claim about its likelihood.

First hit can overlap the final outcome categories. Sustained, escape and timeout partition the final counts; the four reported probabilities must not all be added as mutually exclusive alternatives. All saved rows have n_sustained<=n_hit, but aggregate inequalities cannot establish paired trajectory inclusion without the original event histories.

## Precision and statistical scope

All original integer counts and full saved summaries agree. The public compact L2 sustained-probability table contains 90 cells; 21 retain coarser precision than six-decimal rounding of the original counts. The largest difference is 0.0000333333333332, within four-decimal rounding. `derived_full_precision/` adds full-precision count-derived tables and an explicit difference list; it does not overwrite any original CSV, PDF or figure. Original peak values and adopted/rejected research outcomes are unchanged.

B10.1 has 306 saved replicate rows and 186 distinct seeds. The three replicates at each grid point have distinct seeds, but seeds recur across grid points in 120 additional rows. The saved means and pointwise standard errors reproduce; cross-grid independence is not assumed. Counts are not relabelled as independent draws across the entire scan.

The B10.1 window width is the last minus first sampled noise value whose observed mean capture probability is at least 0.5. It is not an interpolated continuous boundary or a confidence interval. Closed control has zero observed captures in its 43,200 represented trials across the scanned grid, not a proof of identically zero probability. The selected finite-noise pattern and the stochastic-resonance-like description remain model- and event-dependent, not a quantitative theory of physical nuclear fusion.

## What has and has not been verified

The accompanying verifier checks saved integer counts, probabilities, replicate statistics, published parameter values, and numeric tokens extracted from all four manuscript tables. The four manuscript figures were checked visually and their decoded pixels match the four original archived PNGs. The verifier performs CSV arithmetic and static AST inspection only; it never imports or executes a recovered simulator. It runs with the Python standard library and makes no network request.

The audit leaves the historical I2/L2 `consistent` result and J `strong_difference` result unchanged. No new significance threshold, success criterion, simulation trajectory, or physical-fusion claim is introduced.
