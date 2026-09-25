# BIG B25 Phase II Research Status Update

**Published DOI:** https://doi.org/10.5281/zenodo.22967474  
**Related Phase-I DOI:** https://doi.org/10.5281/zenodo.22956894  
**Author:** Jun Lucis

B25 Phase II tests how far the prospective boundary-functional transfer constructed in Phase I can be reduced without target-side calibration.

## Evidence sequence

```text
B25.1c  parallel-curve reduction
         -> AB_PARALLEL_CURVE_REDUCTION_PASS

B25.1d  nested-band single-perimeter reduction
         -> AB_NESTED_BAND_SINGLE_PERIMETER_PASS

B25.1e  single-anchor fixed-coefficient closure
         -> AB_FIXED_COEFFICIENT_PERIMETER_PASS

B25.2   B9-like two-center geometry transfer
         -> IMPLEMENTATION_INVALID
```

The earlier B24.2 and B25.1 verdicts remain unchanged:

```text
B24.2 -> MULTIPLE_BOUNDARY_CLASSES_INDICATED
B25.1 -> AB_CONSTANT_DENSITY_FAIL
```

## B25.1c

The full held-out level-set perimeter family was replaced by one measured representative perimeter plus a fixed, no-fit parallel-curve correction generated from the archived one-dimensional relative-level gradient profile.

Formal verdict: `AB_PARALLEL_CURVE_REDUCTION_PASS`.

## B25.1d

The explicit parallel-curve correction was reduced over frozen nested relative-level bands. At the narrowest tested band, the amplitude-aware single-perimeter predictor remained within the frozen accuracy and stability gates.

Formal verdict: `AB_NESTED_BAND_SINGLE_PERIMETER_PASS`.

## B25.1e

A new circular calibration state fixed one perimeter coefficient,

[
sigma_{m cal}=9.434181431178162	imes10^{-8}.
]

The six held-out primary predictions then used only target representative perimeter,

[
J_{m pred}=sigma_{m cal}P_{m rep}.
]

All six held-out ellipse cases were valid. The held-out median relative error was **4.65%**, the maximum relative error was **14.30%**, and all frozen fine-resolution pair gates passed.

Formal verdict: `AB_FIXED_COEFFICIENT_PERIMETER_PASS`.

This is the first B25 stage whose primary held-out predictor does not require target peak amplitude or the full target level-set perimeter family.

## B25.2

B25.2 froze the B25.1e coefficient and attempted transfer to an equal-injection two-center geometry family intended to span connected and disconnected representative contours.

The predeclared test was not validly realized:

- three coarse-resolution cases fell below the frozen minimum three-grid-cell claim-band thickness;
- at the fine resolution, every tested case still had one primary representative contour, so the required topology span was not realized.

Formal verdict: `IMPLEMENTATION_INVALID`.

Descriptive errors from the invalid test are retained in the archive but are not promoted to a formal transfer FAIL.

## Supported Phase-II statement

Within the tested canonical (p=4), finite-resolution ellipse family, the Phase-I boundary-functional transfer can be prospectively reduced to a fixed perimeter coefficient obtained from one predeclared circular calibration state and then transferred to held-out ellipse shapes using target perimeter alone.

Geometry-family and topology transfer remain unresolved.

## Not established

Phase II does not establish:

- a continuum perimeter theorem;
- a universal or source-independent (sigma P) law;
- a coefficient derived from one-dimensional information alone;
- B9's nonlocal term (C(Omega));
- the full B9 energy (E=sigma P+lambda C);
- external physical validity.

The English Zenodo preprint is the authoritative academic version. A Japanese reference translation is included in the release.
