# Numbered-series DOI inventory audit

**Follow-up — 15 October 2026 (JST):** the B3.1 attachment mismatch identified in this audit is resolved. The seven-page corrected PDF is publicly available under the same v2 DOI and its download matches the uploaded file. See the [verification record](B3_1_file_correction_2026_10_15.md).

**Checked:** 14 October 2026 (UTC). **Repository baseline:** [`aa1eecd`](https://github.com/Jun-Lucis/BIG-theory/commit/aa1eecd2fb04d7ce2a6886329c1cccf7327b1a8a).

The audit searched tracked repository text, the main DOI table, publication map, and per-paper entries. It reconciled all pre-existing linked Zenodo record IDs plus the identified additions: **47/47 records returned public metadata with a DOI and file listing**. This checks record identity and discoverability; it is not an independent scientific re-audit or full content verification of all 47 archives. PDF byte comparisons for B3.1/B4.1/B4.3 and the B5 clarification state are recorded [separately](publication_corrections_B3_1_B5_2026_10_14.md).

## Gaps found and changes made

| Entry | Before this update | Reconciliation |
| --- | --- | --- |
| B3.1/B4.1/B4.3 | Per-paper pages linked original DOIs; main DOI table omitted them; publication map said “To be listed”. | Added current and original DOI links and correction status. The B3.1 PDF mismatch found at the initial audit is retained in the history and was resolved on 15 October (see follow-up above). |
| B5 | No primary B5 entry or DOI in repository text. | Added DOI 20575991, a paper entry, index rows, and description-only correction status. This was a repository navigation omission, not a missing DOI registration. |
| B7 | Main table already linked its DOI; paper page and publication map still had placeholders. | Replaced placeholders with verified DOI 20603601. |
| B12 | Main table already linked its DOI; paper and figure READMEs still had placeholders. | Replaced placeholders with verified DOI 20872005. |
| B26.1 | Frozen protocol page linked related B25 Phase II but omitted the completed B26 publication. | Added shared B26 DOI 22972985 without changing the frozen protocol. |
| B27 | Current entry pointed only to original v1.0 DOI 23024324. | Added published v1.1 source–implementation correction DOI 23368996, preserving v1.0 and all formal outcomes. |
| B41 / EV6 | Own DOI existed elsewhere in the README but was absent from its consolidated DOI table. | Added the existing verified DOI to that table. |
| B6 / B37 | No standalone DOI mapping identified in the repository. | Added explicit unresolved entries; no DOI invented or neighboring record substituted. |

No pre-existing linked Zenodo record failed the metadata retrieval check. Missing navigation and a missing publication are different states.

## Unresolved mappings

- **B6:** methodology history names “B6 retained-scan reuse”, but the repository does not identify a standalone B6 publication. The earlier *Boundary Asymptotics and Quadratic Landing in Degenerate Mixed-Gradient Dissipative Fields* record, [10.5281/zenodo.20309519](https://doi.org/10.5281/zenodo.20309519), has a PDF filename containing **BIG6.5**. Its filename is not sufficient evidence that it is the later B-series B6 study. Keep these labels distinct pending source confirmation.
- **B37:** [B37–B38 research status](research_status_update_B37_B38.md) documents B37.1/B37.2 and retains both formal FAILs, but no standalone B37 DOI was identified. [B38 DOI 23104248](https://doi.org/10.5281/zenodo.23104248) explicitly archives B38.1–B38.6; it is a related successor record, not an authenticated substitute for a B37 archive.

“Unconfirmed” means the mapping was not established from the reviewed sources. It does not prove that no DOI exists or that the study was never published. Combined B24–B25, B28–B29, and B30–B36 records are legitimate shared publications, not missing per-number DOIs. Decimal protocol stages likewise do not require independent DOI records.

The literal D-number check found **D0** (metric/readout notation) and **D5** (an audit checkpoint), with no standalone D-series publication entry. B42 appears in an audit-source label, without a numbered paper entry whose DOI could be established here; it is not treated as a confirmed missing published record.

## Reconciled index

All DOI links below were matched to live record metadata. Original-version links are retained where a correction record is listed. Status entries do not upgrade numerical verdicts.

| Series / record | DOI | Verification or mapping state |
| --- | --- | --- |
| B3.1 | [10.5281/zenodo.23342986](https://doi.org/10.5281/zenodo.23342986) · [10.5281/zenodo.20465842](https://doi.org/10.5281/zenodo.20465842) | Corrected seven-page public PDF verified after 15 October attachment repair |
| B4.1 | [10.5281/zenodo.23342902](https://doi.org/10.5281/zenodo.23342902) · [10.5281/zenodo.20541748](https://doi.org/10.5281/zenodo.20541748) | Corrected PDF byte match verified |
| B4.3 | [10.5281/zenodo.23342705](https://doi.org/10.5281/zenodo.23342705) · [10.5281/zenodo.20564435](https://doi.org/10.5281/zenodo.20564435) | Corrected PDF byte match verified |
| B5 | [10.5281/zenodo.20575991](https://doi.org/10.5281/zenodo.20575991) | Description-only clarification; original ZIP retained |
| B6 | Unconfirmed | Standalone publication mapping unconfirmed |
| B7 | [10.5281/zenodo.20603601](https://doi.org/10.5281/zenodo.20603601) | Metadata and record identity verified |
| B8 | [10.5281/zenodo.20645317](https://doi.org/10.5281/zenodo.20645317) | Metadata and record identity verified |
| B9 | [10.5281/zenodo.20799131](https://doi.org/10.5281/zenodo.20799131) | Metadata and record identity verified |
| B9 empirical Phase II | [10.5281/zenodo.23128738](https://doi.org/10.5281/zenodo.23128738) | Metadata and record identity verified |
| B10 | [10.5281/zenodo.20819427](https://doi.org/10.5281/zenodo.20819427) | Metadata and record identity verified |
| B11 | [10.5281/zenodo.20828439](https://doi.org/10.5281/zenodo.20828439) | Metadata and record identity verified |
| B12 | [10.5281/zenodo.20872005](https://doi.org/10.5281/zenodo.20872005) | Metadata and record identity verified |
| B13 | [10.5281/zenodo.21072783](https://doi.org/10.5281/zenodo.21072783) | Metadata and record identity verified |
| B13.1 | [10.5281/zenodo.21108338](https://doi.org/10.5281/zenodo.21108338) | Metadata and record identity verified |
| B14 | [10.5281/zenodo.21144373](https://doi.org/10.5281/zenodo.21144373) | Metadata and record identity verified |
| B15 | [10.5281/zenodo.21173333](https://doi.org/10.5281/zenodo.21173333) | Metadata and record identity verified |
| Layered framework | [10.5281/zenodo.22161614](https://doi.org/10.5281/zenodo.22161614) | Metadata and record identity verified |
| B16 | [10.5281/zenodo.22660005](https://doi.org/10.5281/zenodo.22660005) | Metadata and record identity verified |
| B17 | [10.5281/zenodo.22677581](https://doi.org/10.5281/zenodo.22677581) | Metadata and record identity verified |
| B18 | [10.5281/zenodo.22690970](https://doi.org/10.5281/zenodo.22690970) | Metadata and record identity verified |
| B19 | [10.5281/zenodo.22726848](https://doi.org/10.5281/zenodo.22726848) | Metadata and record identity verified |
| B19 follow-up | [10.5281/zenodo.22769513](https://doi.org/10.5281/zenodo.22769513) | Metadata and record identity verified |
| B19E | [10.5281/zenodo.22996961](https://doi.org/10.5281/zenodo.22996961) | Metadata and record identity verified |
| B20 | [10.5281/zenodo.22846729](https://doi.org/10.5281/zenodo.22846729) | Metadata and record identity verified |
| B21 | [10.5281/zenodo.22876813](https://doi.org/10.5281/zenodo.22876813) | Metadata and record identity verified |
| B22 | [10.5281/zenodo.22893912](https://doi.org/10.5281/zenodo.22893912) | Metadata and record identity verified |
| B23 | [10.5281/zenodo.22936794](https://doi.org/10.5281/zenodo.22936794) | Metadata and record identity verified |
| B23A | [10.5281/zenodo.22994445](https://doi.org/10.5281/zenodo.22994445) | Metadata and record identity verified |
| B24–B25 Phase I | [10.5281/zenodo.22956894](https://doi.org/10.5281/zenodo.22956894) | Integrated publication; separate DOI per stage not required |
| B25 Phase II | [10.5281/zenodo.22967474](https://doi.org/10.5281/zenodo.22967474) | Metadata and record identity verified |
| B26 | [10.5281/zenodo.22972985](https://doi.org/10.5281/zenodo.22972985) | Shared B26/B26.1/B26.2 publication |
| B27 | [10.5281/zenodo.23368996](https://doi.org/10.5281/zenodo.23368996) · [10.5281/zenodo.23024324](https://doi.org/10.5281/zenodo.23024324) | v1.1 correction record; v1.0 retained |
| B28–B29 | [10.5281/zenodo.23050390](https://doi.org/10.5281/zenodo.23050390) | Integrated publication; separate DOI per stage not required |
| B30–B36 | [10.5281/zenodo.23048197](https://doi.org/10.5281/zenodo.23048197) | Integrated publication; separate DOI per stage not required |
| B37 | Unconfirmed | Standalone publication mapping unconfirmed |
| B38 | [10.5281/zenodo.23104248](https://doi.org/10.5281/zenodo.23104248) | Metadata and record identity verified |
| B39 | [10.5281/zenodo.23113994](https://doi.org/10.5281/zenodo.23113994) | Metadata and record identity verified |
| B40 | [10.5281/zenodo.23153688](https://doi.org/10.5281/zenodo.23153688) | Metadata and record identity verified |
| B41 | [10.5281/zenodo.23249677](https://doi.org/10.5281/zenodo.23249677) | Metadata and record identity verified |
| EV6 | [10.5281/zenodo.23198141](https://doi.org/10.5281/zenodo.23198141) | Metadata and record identity verified |
| Methodology companion | [10.5281/zenodo.23171698](https://doi.org/10.5281/zenodo.23171698) | Metadata and record identity verified |

Related earlier archive: [BIG6.5 file-label record, 10.5281/zenodo.20309519](https://doi.org/10.5281/zenodo.20309519). Its B6 mapping remains unconfirmed.

The [machine-readable audit](doi_inventory_audit_2026_10_14.json) lists record titles, API sources, concept families, filenames, sizes, and Zenodo checksums for all 47 checked records. The initial GitHub index update did not change Zenodo. The 15 October follow-up documents the separately completed B3.1 attachment repair.
