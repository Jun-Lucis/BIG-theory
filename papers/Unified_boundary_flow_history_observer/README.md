# Boundary–Flow–History Coupling with Observer Backaction (U0; post-B42 study)

**Published paper:** *Boundary–Flow–History Coupling with Observer Backaction: Mathematical Structure, Numerical Verification, and Predictive Limits*  
**Author:** Jun Lucis (independent researcher)  
**Publication:** Zenodo Preprint v1.0, **26 October 2026**  
**Version-specific DOI:** [10.5281/zenodo.23650894](https://doi.org/10.5281/zenodo.23650894)  
**All-version (concept) DOI:** [10.5281/zenodo.23650893](https://doi.org/10.5281/zenodo.23650893)  
**Public record and files:** https://zenodo.org/records/23650894

This is a **new, independent post-B42 preprint**, not a new numbered B-series paper, a replacement for the [programme-wide flagship](https://doi.org/10.5281/zenodo.23486616), or a revision of the separate [Fluid History study](https://doi.org/10.5281/zenodo.23635004). Its coupled equations are a **candidate model within specified assumptions**, not a universal equation for all BIG model families.

## Model and scope

The study brings together incompressible fluid velocity `u`, a degenerate structural field `φ`, internal history `h`, and thermal state `T` within a candidate coupled model referred to as **U0**. Conditional statements about energy and thermal-entropy balances require smoothness, positive temperature, and compatible boundary/work/heat ports. The selected positive-sign compact-support comparison equation and the **bulk** Navier–Stokes equations arise as restricted reductions; the historical cylinder outlet prescription is **not automatically zero symmetric traction**.

The original U0 **passively reads** state-dependent observations; it does not originally include apparatus backaction. Later **R0–R2 observer extensions** introduce an apparatus state `q` and reciprocal power-exchange terms. These allow restricted results about energy-consistent backaction, conditional state reconstruction, second- and third-order history-to-readout delay, noncontact controls, and the distinction between apparatus reset and target-history erasure.

These are **mathematical/model-internal constructions**, not independently calibrated physical sensors, quantum-measurement laws, or universal information–disturbance limits.

## Evidence and preserved outcomes

| Study | Evidence/status | Qualification |
| --- | --- | --- |
| P0–P2 | Candidate U0, specified reductions, conditional energy/entropy and observational distinctions | No general coupled PDE existence/uniqueness or universal sharp 2D support theorem |
| P3–P3.2 | Selected periodic shear and 2D coupled-model numerical QA, moving localized structures and cross-discretization checks | P3.1a initial integration-protocol deviation and P3.2 initial Nyquist-gate FAIL preserved; discretization losses are not physical heat |
| P3.3a | **Prospectively sealed synthetic relative-clock prediction: NO GAIN / FAIL** | The predeclared improvement gate fails; ID improvement ≈0.51%, OOD clock predictor worse by ≈10.15% than ordinary comparator |
| P3.3b | **Prospectively sealed 2D synthetic clock prediction: FAIL** | Clock representation worse than best ordinary predictor by ≈7.91% (ID) and ≈0.32% (OOD) |
| P3.4 | **Synthetic heat-observation improvement gate FAIL; same-observation clock gate FAIL** | Additional noisy simulated heat readings gave no ≥10% gain (ID slightly worse; OOD ≈0.94% better), and recoding the same observations added no conditional information |
| Observer R0–R1 | Idealized energy-exchange apparatus; conditional reconstruction and information/backaction/reset analysis; internal QA passes | No independent material/device calibration or logical-erasure cost |
| Observer R2 | 2D localized structural-field coupling; formal power cancellation; delayed weak history signal; internal numerical QA passes | Third-order short-time prediction assumes sufficient smoothness; threshold contours are not a sharp free-boundary theorem |

**Scientific status:** An ordinary internal-variable viscosity model can be made **algebraically equivalent** by renaming `c=φ` and `z=h`. **BIG-specific additional predictive value is NOT DEMONSTRATED.** Observer R0–R2 internal PASS results **do not reverse** P3.3a, P3.3b or P3.4 FAIL outcomes. The programme's earlier B42 overall science verdict **NONE** and RTM2 CP13/CP14 **NO_GAIN** are unchanged.

## Public files and reproducibility

The authoritative files are on [Zenodo record 23650894](https://zenodo.org/records/23650894):

- `BIG_Paper_EN_v1_0.pdf` — English primary preprint.
- `BIG_Paper_JP_Reference_v1_0.pdf` — Japanese reference translation/reorganization, **not necessarily word-for-word**.
- `BIG_Unified_Reproducibility_v1_0.zip` — combined reproduction archive with the 12 unchanged stage source archives, code, frozen inputs, saved outputs, failure records, manifests and local reproduction instructions.
- `README.md`, `PUBLICATION_AUDIT.md`, `LICENSES.md`, `SHA256SUMS.txt` — public release and verification aids.

The release audit reports CRC checks on **12/12 stage ZIPs** and **458/458 primary-manifest SHA256 matches**. These are **archive-integrity checks, not a fresh independent full-PDE solver rerun or physical experiment**. Basic reproduction is documented; independent third-party rerun auditing remains incomplete. The papers and new release documentation are CC BY 4.0; historical code and third-party dependencies retain their own rights (see published `LICENSES.md`). No private Google Drive access should be needed to inspect the public reproduction bundle.

## Citation

For this candidate equation, its exact scope, numerical outcomes, or the R0–R2 backaction constructions, cite the **version-specific DOI**:

> Lucis, J. (2026). *Boundary–Flow–History Coupling with Observer Backaction: Mathematical Structure, Numerical Verification, and Predictive Limits* (Version 1.0). Zenodo. https://doi.org/10.5281/zenodo.23650894

For general programme context cite the [flagship](https://doi.org/10.5281/zenodo.23486616); for the **separate ordinary-Navier–Stokes Fluid History tests** cite [10.5281/zenodo.23635004](https://doi.org/10.5281/zenodo.23635004).

See also [Publication map](../../docs/publication_map.md), [Limitations](../../docs/limitations.md), and [Citation policy](../../docs/citation_policy.md).
