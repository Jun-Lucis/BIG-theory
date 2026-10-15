# B9 publication audit and documentation correction — 15 October 2026

The empirical comparison's corrected v4.0 is https://doi.org/10.5281/zenodo.23385951. It replaces the preceding comparison record 20942812 (record v3 / file v5) in the same version family. The integrated primary preprint 20799131, original open-boundary dataset 20798687, and later Phase II 23128738 remain unchanged and answer different publication/research purposes.

## Corrected documentation

The preceding public comparison PDF was 5,503 bytes, two pages, MD5 `8704e586c6c95e8d12c11d47f718b98b`. It contained captions for three absent figures and did not display the intended Greek symbols. The corrected four-page PDF restores the three original archived image pixels, typesets the model equation, and gives per-value provenance. No simulated quantity, formal PASS/FAIL result, or numerical table cell is changed.

The five inner-barrier heights in the original plot are the Table I $E_A$ entries in [Bertsch et al., arXiv:1502.05985v1](https://arxiv.org/html/1502.05985v1): Th-232 5.80, U-236 5.00, U-238 6.30, Pu-240 6.05, Cm-244 6.18 MeV. The six-nucleus representative illustration/table remains unchanged. Cf-252 is not in that cited inner-barrier subset and no extra value is invented. The later Phase II uses a separate 52-nucleus sample and a max(inner, outer) primary-barrier definition; those are not interchangeable observables.

| Released file | Bytes | SHA-256 |
|---|---:|---|
| Corrected comparison PDF | 464106 | `2e58d7589237b991fd2aaac10c562e68c28ff5c1c680a8e63ad2cfcba5f2e268` |
| Source, archived tables and arithmetic audit ZIP | 2489670 | `401b039fcffeb5ef5462b430883625928c113c8c761cf0c35aacabebba310b5d` |

The ZIP contains 35 files, a checksum manifest, the original Phase II ZIP, 21 recovered numerical CSV/JSON files (19 matching the original dataset manifest and two verified against Phase II only), the three legacy figure images, LaTeX source, and a read-only arithmetic verifier. A clean extraction reproduces the recorded verification JSON. This documentation audit is separate from scientific research verdicts.

## Checked numerical scope

Fourteen groups of arithmetic and table-consistency checks agree within their recorded tolerances. They include the Cassini energy identity and near preference 55.9178261851, finite open-boundary threshold 48.0644639984, the two previously specified last-55-point tail fits (42.0061831542 / 43.9880290638), RIPL mapping for 52 nuclei, descriptive residual metrics, and the arithmetic of the mixed external two-case check.

Cassini has 182 archived shape rows, of which 144 are valid and 38 invalid. Its 2304 energy rows correspond to the valid 144 shapes at 16 lambda values; invalid shapes are excluded. The open branch has 220 valid two-component candidates with no edge contact. Matching periodic-large-box and open C tables at shared dx does not independently authenticate the original convolution implementation.

The Phase II package passes its 54 SHA-256 entries and ZIP CRC. Seven inherited B9 files match the recovered originals byte for byte. Nineteen original data files match the historical dataset manifest. Fresh re-download of the entire original 8.6 MB dataset ZIP timed out, so this audit does not claim a new whole-ZIP byte verification.

The about-42–44 range is the spread of retained self-energy and tail-fit estimates, not a confidence interval, proven upper/lower bound, or grid-convergence certificate. Far/near preference, finite-amplitude coexistence, local spinodal, and pinch-envelope zero remain distinct scales.

## Open reproducibility gaps

The checked original code and notebooks folders were empty. Two missing Cassini files were recovered from the data folders and verified against the later Phase II archive. This establishes their identity to that archive, not independently their original-run provenance, and it does not recover the original solver. The Phase II release retains numerical summaries, not every raw run, frozen IIC protocol, or executable implementation. A summary's predeclaration hash does not independently establish its timing. The new verifier reproduces archived arithmetic only.

The primary preprint's isolated Summary heading on page 12 is a minor remaining layout issue. The primary PDF was not replaced in this correction.

Both newly published files were re-downloaded byte identical to the validated local files. Their SHA-256 and MD5 checksums match; the downloaded ZIP's CRC also passes.

## Scientific outcomes retained

Phase IIC P1/P4 retain PASS; IIC P2/P3 and IID P1/P2 retain FAIL. The quartic coefficient remains unresolved. The external two-case check remains mixed; it was not pristine blind and had no predeclared PASS/FAIL threshold. No new simulation, model selection, formal research regrading, or claim of quantitative nuclear-fission prediction is introduced.

The two B9 GitHub explanatory pages also have their corrupted TeX escape/control characters repaired. Changes elsewhere in the programme are outside this correction.
