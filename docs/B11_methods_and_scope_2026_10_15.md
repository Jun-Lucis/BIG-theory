# BIG-B11 archived methods and interpretation supplement

Jun Lucis. Audit date: 15 October 2026.

The original five-page v1.0 paper and all 20 original package files are preserved byte for byte. Version 1.1 identifies the prepared documentation/data supplement. No stochastic dynamics was rerun, outcome label or seed changed, or research verdict regraded.

The documentation/data supplement v1.1 is prepared and verified. Its Zenodo draft description and version were saved, but file-upload finalization could not be verified after the browser timed out. No publish action was performed. Reserved DOI 10.5281/zenodo.23387434 is not a published release; the current published record remains 10.5281/zenodo.20828439.

## Recovered records

| Stage | Grid points | Endpoints per point | Saved endpoint rows | Role |
|---|---:|---:|---:|---|
| B11.1 | 240 | 240 | 57,600 | Initial construction, not the decisive competitive result |
| B11.2 | 1,000 | 80 | 80,000 | Competitive landscape and five initialization modes |
| B11.2b | 255 | 250 | 63,750 | Main high-resolution neutral-mixture threshold scan |

Fourteen recovered CSV/JSON files contain 201,350 saved endpoint/diagnostic rows and 1,495 grid summaries. Files named replicates.csv contain one row per trajectory, rather than complete trajectory time series or independent Monte Carlo batches. Outcome frequencies, partitions, means and sample standard deviations with ddof=1 reproduce. Each dataset's seeds are distinct across its rows; this alone does not authenticate the RNG or prove independence.

The original public PDF and ZIP were freshly downloaded byte identical to the saved copies. All five PDF pages were visually inspected. All 105 manuscript table entries agree at the displayed three-decimal precision, including a half-unit rounding tie. The original compact CSV's 195 numeric cells agree within six-decimal rounding with the complete saved threshold table, with maximum absolute difference below 0.0000005. Five embedded PDF figures match original PNG pixels; all seven representative GitHub PNGs match their archived counterparts by Git blob identity.

## Empirical threshold construction

B11.2b uses N=8, T=22, dt=0.02, five rho values, three noise values (0.08, 0.14, 0.22), 17 amp_I values from 0.75 to 1.55 in steps of 0.05 and 250 endpoints per point. The full recovered parameter file supplements the abbreviated original public parameter file.

For target p=0.5 or p=0.9, adjacent sampled amplitudes x0<x1 with observed fractions y0<p<=y1 give

    x_c = x0 + (p-y0) * (x1-x0) / (y1-y0).

All 30 saved thresholds reproduce, with one upward crossing of each target on each curve. They are empirical finite-grid interpolants conditional on this initialization, classification, observation horizon, step size and model. They are not exact bifurcation points, continuum limits, confidence intervals or universal critical constants. No retrospective uncertainty interval or new success criterion is introduced.

The saved thresholds decrease with rho and increase across the three scanned noise values. Eight local downward steps occur in the full empirical probability curves; global monotonicity of every observed probability is not asserted. Twelve curves have tied maxima. A saved amp_I_at_max_P_inheritance is an amplitude attaining the maximum, not necessarily its first occurrence.

## Meaning of the near-transition diagnostics

For saved endpoints, release_drop = U0 - U_final and, where recorded, conflict_drop = Uconf0 - Uconf_final. The competitive/high-resolution final conflict term agrees with

    E_conflict = k_conflict * (1-rho) * nA**2 * nB**2,

where nA=||h_A||, nB=||h_B|| and k_conflict=2. The saved geometry satisfies

    ||h|| = sqrt(nA**2+nB**2),
    sim_I = (sim_A + sim_B) / sqrt(2).

The paper's near-transition release/conflict values average all 250 endpoints at the sampled amp_I whose observed inheritance fraction is closest to 0.5. They are neither interpolated at x_c nor conditional means over inheritance-only outcomes. For example, at sigma=0.08 and rho=0 the diagnostic uses amp_I=1.25 and observed P=0.36, while the interpolated 50% threshold is about 1.2619863. Original selection rules and values are retained.

These are effective landscape diagnostics, not physical heat, mass defects, entropy production or measured released energy. Their variation compares different constructed landscapes and selected sampled amplitudes.

## Finite-time and model scope

The saved probabilities are terminal classifications at T=22 for B11.2/B11.2b; the initial B11.1 model uses T=35. A stability_var diagnostic is recorded, but its exact tail-window implementation remains unauthenticated. Terminal fractions do not prove infinite-time stability, stochastic permanence or residence-time properties.

The inheritance template I=normalize(a,b) is explicitly supplied. The model tests competition within a landscape containing that well and an explicit (1-rho) conflict penalty. A=(a,0) and B=(0,b) occupy separate sectors, so A dot B=0 even when a dot b=rho in the original parent space. The observed similarity trend is a result within this constructed model family, rather than an independent universal law of inheritance or unique empirical validation of BIG.

B11 independently initializes its post-capture hidden state. The recovered archive does not demonstrate a transfer of B10 capture trajectories into B11 or an end-to-end capture-and-inheritance experiment. Later B12/B42 definitions, including R-lock conditions, are not retroactively applied.

## Open historical source authentication

B11.2 and B11.2b records report CODE_SHA16 values 3c43a66f1b4b660d and e5867d9002262267. They agree internally, but complete corresponding source bodies were not recovered. These are reported fingerprints, not freshly authenticated source hashes.

The original source/create_b11_package.py is a document/figure packaging script, not the historical stochastic solver. The full potential and gradient, Gaussian-well and vector construction, RNG and stepping, clipping, exact classifier comparison boundaries and precedence, tail-window definitions, environment and full time histories remain unauthenticated. Parameter thresholds alone do not specify an ordered classifier. No inferred replacement is presented as original code.

The newly written standard-library-only verify_b11_archive.py recomputes 28 groups of archived arithmetic and integrity. A clean extraction produced the same verification JSON. The utility never imports or executes an original scientific or packaging program, makes no network request and generates no new trajectory. PDF table tokens and visual checks were extracted separately and bound with the original files by the archive checksum manifest.

Documents/data retain CC BY 4.0 and original provenance. Only the new verification utility is MIT licensed under LICENSE_CODE.txt. Complete historical solver/classifier authentication remains OPEN.
