# BIG-B40 — Clock-Family Transfer and Target-Excluded Relational Reconstruction

**Preprint title:** *Clock-Family Transfer and Target-Excluded Relational Reconstruction in a Finite Boundary-Response Model*  
**Subtitle:** *Failure localization and prospective orientation-reversing covariance*  
**Author:** Jun Lucis  
**Zenodo DOI:** https://doi.org/10.5281/zenodo.23153688  
**Status:** published, v1.1

The English manuscript is the authoritative version. The same Zenodo record also includes a Japanese reference translation and a compact reproducibility/audit package.

## Main result

B40 preserves both negative and positive prospective outcomes rather than compressing them into one aggregate PASS.

The retained chain is:

```text
B40.1-P1  CLOCK_MAP_FAMILY_TRANSFER_FAIL
    -> B40.1-P1B  LAG_GRID_QUANTIZATION_LOCALIZATION_PASS

B40.2-P1  TARGET_EXCLUDED_RELATIONAL_RECONSTRUCTION_FAIL
    -> P1B  PHASE_RESOLUTION_LOCALIZATION_PASS
    -> P1C  AXIS_SWAP_ORIENTATION_LOCALIZATION_PASS
    -> P1D  NEGATIVE_PHASE_AXIS_SWAP_REPLICATION_PASS
    -> P1E  ORIENTATION_REVERSING_COVARIANCE_TRANSFER_PASS
    -> P1F  THIRD_ANGLE_ORIENTATION_REVERSING_COVARIANCE_REPLICATION_PASS
```

The parent FAILs remain formal FAILs.

## What is new

B40.1 shows that clock-family transfer is not formally universal under the frozen coarse directed-lag gate, even though the underlying matched response covariance remains numerically strong. A prospectively refined lag test localizes the single aggregate failure to lag-grid quantization without retroactive regrading.

B40.2 constructs an **offline target-excluded relational progress coordinate** from non-target `evolving_Dt_dual` relations. The first held-out reconstruction test is formally negative. Successor tests then show that the limitation is structured: it persists across resolution, swaps with source-relative orientation, transfers across translation sign, and obeys a prospectively frozen orientation-reversing rule at fresh 23°/67° and 17°/73° angle pairs.

In the final third-angle replication, two reconstruction failures remain, but they are a transformed partner pair. The covariance result therefore concerns the organization of success **and failure**, not universal reconstruction success.

## Claim boundary

Supported only for the tested finite semi-discrete implementation.

Not established:

- arbitrary reparameterization invariance;
- a universal relational clock;
- emergent physical time;
- continuum rotational covariance;
- physical anisotropy;
- continuum convergence or theorem-level symmetry.

## Citation

```text
Lucis, J. Clock-Family Transfer and Target-Excluded Relational
Reconstruction in a Finite Boundary-Response Model.
Boundary Information Geometry (BIG-B40), 2026.
DOI: 10.5281/zenodo.23153688.
```

Zenodo: https://doi.org/10.5281/zenodo.23153688

Status note: [docs/research_status_update_B40.md](../../docs/research_status_update_B40.md)  
日本語状況: [docs/research_status_update_B40_ja.md](../../docs/research_status_update_B40_ja.md)
