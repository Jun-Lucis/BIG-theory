# BIG B22・B23・B24–B25 Phase I — Zenodo改訂版公開同期（2026-10-19）

著者：Jun Lucis。既存の公開同期記録 `publication_sync_B19_B41_2026_10_19_JA.md` の**後続追記**。以前の台帳はその時点の履歴として変更しない。

## Zenodo版履歴

| 出版単位 | 現行版 DOI / Zenodo | 旧版 DOI / Zenodo | 今回の状態 |
| --- | --- | --- | --- |
| B22 | [10.5281/zenodo.23467311](https://zenodo.org/records/23467311) / v1.1 | [10.5281/zenodo.22893912](https://zenodo.org/records/22893912) / v1.0 | 英日PDF改訂、既存再現ZIP保持 |
| B23 | [10.5281/zenodo.23467455](https://zenodo.org/records/23467455) / v1.1 | [10.5281/zenodo.22936794](https://zenodo.org/records/22936794) / v1.0 | 英日PDF改訂、既存再現ZIP保持 |
| B24–B25 Phase I | [10.5281/zenodo.23467490](https://zenodo.org/records/23467490) / v1.1 | [10.5281/zenodo.22956894](https://zenodo.org/records/22956894) / v1.0 | 英日PDF改訂、既存英日ZIP保持 |

## 公開ファイル

**B22**
- `BIG_B22_EN_REVISED_PREPRINT_20261019.pdf`
- `BIG_B22_JA_JAPANESE_REFERENCE_20261019.pdf`
- `BIG_B22_Zenodo_Release_v1_0.zip`（既存ファイル保持）

**B23**
- `BIG_B23_EN_REVISED_PREPRINT_20261019.pdf`
- `BIG_B23_JA_JAPANESE_REFERENCE_20261019.pdf`
- `BIG_B23_Zenodo_Reproducibility_Package_v1_0.zip`（既存ファイル保持）

**B24–B25 Phase I**
- `BIG_B24B25_EN_REVISED_PREPRINT_20261019.pdf`
- `BIG_B24B25_JA_JAPANESE_REFERENCE_20261019.pdf`
- `BIG_B24_B25_English_Zenodo_Upload_Package_v1_0_DOI_zenodo_22956894.zip`（既存ファイル保持）
- `BIG_B24_B25_Japanese_Reference_Package_v1_0_DOI_zenodo_22956894.zip`（既存ファイル保持）

## 科学的な訂正範囲

- **B22**：E2の不確かさの帰属とnormal-rate尺度、E3/E5の前向き評価における既知情報と逐次性を明確化。有限解像度・Family-C限定、元の正式判定を維持。
- **B23**：E3Rのwrong-ray実装修正、E3R2の訂正再計算という証拠区分、観測済みT1を使用する逐次一段予測を明確化。原aggregate verdict `INCONCLUSIVE` は変更なし。
- **B24–B25 Phase I**：B24.2の凍結した対応表・出典・候補範囲、歴史的 `DRAFT_NOT_FROZEN` を明示。B25.1 `AB_CONSTANT_DENSITY_FAIL` とB25.1b `AB_LEVEL_RESOLVED_BRIDGE_PASS` を区別し、再分類しない。

**基本的に再現可能。独立した再実行監査は未了。**

## 更新・検証の境界

- Zenodo v1.1公開・ファイル名・更新PDFの添付MD5一致、保持ZIPの旧版MD5一致は、著者が依頼したWorkの公開完了報告に基づく。GitHub側の同期は別途本リポジトリのコミットで確認する。
- 元のv1.0は引用可能な歴史版。現行論文を引用する場合はv1.1の版固有DOIを使用する。旧版との番号を混同しない。
- 既存再現ZIPの名称に `v1_0` または旧版DOIが含まれていても、ZIP内容を変更していないため、その名称は意図的に維持した。
- 改訂PDFの公開は、当時の凍結条件・データ取得の独立な再認証やPDE独立再実行を意味しない。
- B25 Phase II・B23A・B27・B28以降、B37独立公開は今回のファイル更新対象外。
