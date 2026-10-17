# B21 CP27 再開時の公開前確認（2026-10-17 JST）

状態：**CP27_WORKING / MANUSCRIPT_FOLLOWUP_REQUIRED / PUBLICATION_NOT_EXECUTED_IN_THIS_SESSION**

標準評価：**基本的に再現可能。独立した再実行監査は未了。**

本記録は今回の読取り確認と修正案のcheckpointである。原稿修正済み、Zenodo現況確認済み、新版公開済み、全バイト再照合済みとは扱わない。CP24〜CP26の完了記録と科学的正式分類を変更しない。

## 今回確認できた保存状態

- 再開時および書込み直前のmain：`a0c9a1d95ee60b7f77a416607f5cfd4838c0b635`。
- 指定されたB21 interim記録、README、入力snapshot、保存表receipt、基底精度receipt、再構成検算コード・結果、Drive readback receipt、公開準備manifestを取得。
- [Drive作業フォルダ](https://drive.google.com/drive/folders/1GUJUuKAkDHK55C3MOnkSvD1fKHQUb4dj)に13ファイルを確認。
- Library作業フォルダに対応する12ファイルを確認し、Drive metadataとのファイル名・サイズ一致を確認。source checkpoint ZIPはDriveに8,038,153 bytesとして存在する。Library直下のsource ZIPの今回の再取得・hash照合は未実施。
- Libraryの両既存台帳はversion 7で、最新完了CP26を維持している。
- 保存済み再構成検算結果は101 CSV / 7,335行 / 14,670行内比較、72 summaryから120比較、manifest48行、根区間2件。これは過去の保存receiptの読取りであり、今回の再実行ではない。
- 英日v1.1 DRAFT PDFは各15ページとして全文テキストを取得。全頁の目視検査は未完了。ページ画像読取りは画像ポインタを返し、本セッションでは画素の視認確認を完了できていない。
- メタデータ案はJun Lucis、preprint、v1.1、CC BY 4.0を含み、GitHub URLもRelated identifiersに存在する。これはdraftファイル内容の確認であり、Zenodo保存済みmetadataの確認ではない。

## 公開前に反映する本文修正案

以下は修正案であり、現DOCX/PDFへ未適用。数値、表セル、画像、原ベクトル、既存数式、正式判定、停止規則を保持する。

### 1. 基底精度の本文整合

英語§3.1（4頁）および§9項目2（12頁）は、研究全体を「exact normalized four-dimensional ... B20.5 subspace」と記述している。付録C.2の初期探索とE10/E12の基底差の説明に合わせ、全段階で厳密同一との読みを避ける。

英語§3.1の該当文の置換案：

> It probes the local response-boundary branch r10 using the normalized four-dimensional coordinate construction inherited from B20.5, subject to the stage-dependent basis-precision qualification in Appendix C.2. E1 uses QR reorthogonalization of a six-decimal displayed basis; E10 and E12 restore the high-precision basis. The fixed-parameter E4 temporal derivative inherited by E12 belongs to the initial exploratory lineage.

英語§9項目2の置換案：

> The closure comparison is local to the Family-C r10 branch near T = 0.012 and the B20.5-derived normalized four-dimensional coordinate construction, with the basis-precision difference described in Appendix C.2. Its effect on the PDE outcomes has not been measured.

日本語も対応箇所を「B20.5由来の正規化四次元座標構成」に揃え、初期探索とE10/E12の精度差およびPDE影響未監査を明記する。E10自身を高精度基底使用と記す§5は、この全段階同一性の問題とは区別する。

### 2. 英日§8.4の主張の整合

英語§8.4末尾には「requires no extra term」が残る。日本語には限定説明が既にある一方、「利用可能な有限解像度で、検査した有限解像度で」という重複がある。

英語末尾の置換案：

> B21 closes with the limited finding that no distinct additional effective boundary-dynamical term was identified in the frozen finite-resolution comparison. This does not establish the absence of such a term or certify uncertainty-resolved closure.

日本語末尾の置換案：

> B21は、凍結した有限解像度の比較において、独立した追加の有効境界力学項を識別しなかった、という限定的な結論で閉じる。その不在や、不確かさを囲い込んだ意味での閉包を証明したわけではない。

### 3. 原表セルを保持した直近注記

§7.4の原表にはuncertainty bound、付録Aの原表にはroot bound、付録BにはNo residual above tested uncertaintyが残っている。原表セル保持の指示に従い、セルは変更せず、付録A/Bの各表直後にも歴史的表記であることを明示する。

英語注記案：

> Historical table wording and classifications are retained. The 0.2174844% root-bracket quantity is a first-order reference scale for the directly observed gradient derivative using the central HVP. It is not a verified upper bound on the correlated closure residual. The table wording does not establish the absence of an additional term; see Sections 7.4 and Appendix C.1.

日本語注記案：

> 表内の歴史的表記と分類は保持した。0.2174844%は中央HVPを用いた観測側の勾配時間差分の一次参考尺度であり、相関を含む閉包残差全体の検証済み上限ではない。表の表記から追加項の不在を証明したとは解釈しない。§7.4および付録C.1参照。

### 4. 最新の保存検算範囲を明記

metadata案の72 readout comparisonsは以前の部分検算の記述であり、最新receiptは72 summaryから120比較である。単に旧検算を復元したとは書かず、新しく再構成した保存成果物検算として追記する。本文C.4も同様に旧全体検算未発見と新検算を区別する。

追記候補：

> A newly reconstructed saved-artifact validator checked 101 CSV time series containing 7,335 rows, with 14,670 row-algebra comparisons, 120 stored readout comparisons from 72 summaries, 48 frozen-manifest entries, and two E12 root brackets. This is a consistency check of saved artifacts, not recovery of the earlier whole-source verifier and not an independent PDE rerun.

metadataのpublication draft notes、pending DOI、および旧版を説明するData availabilityは、実際の予約DOIと最終内容を確認した後で最終化する。未確認DOIを記入しない。

## 表示確認の残件

英日PDF10頁の抽出テキストではg(T_plus)の式が「g¿」等として欠落しているように見える。これは**抽出上の異常候補**であり、実際のPDF描画欠陥と断定しない。日本語付録表・参考文献見出しにも抽出上の欠字候補がある。元DOCXの数式XML保持だけで描画正常とは判断せず、原PDFとの比較および新PDF全頁の目視確認が必要。原ベクトルを推測して置換しない。

## 現在の実行制約

- ローカル実行を二度確認したが、利用可能な実行環境がないとの応答。ファイル復元、PDF再生成、ZIP固定、全バイトhash検証は実施できていない。
- Browserの現行一覧はChrome extension一件のみ。ユーザー指定のWorkクラウドブラウザーは利用可能一覧にない。端末側ブラウザーでZenodoを代替操作していない。
- Zenodo旧版の現況、ログイン、既存draft、新版予約DOIは今回未確認。既存draftなしと判断していない。
- New version、DOI予約、ZIP作成、アップロード、Publishは今回未実行。B42 draftを含む無関係なレコードも変更していない。
- TinyFishおよびサブエージェントは不使用。

## 再開順序

実行環境とWorkクラウドブラウザーが利用可能になったら、Zenodoの現況と既存draftを先に確認する。上記本文補足を原稿へ反映し、表・図・数式の保持と全頁表示を確認。実予約DOI取得後に一度だけ完全ZIP固定、公開、公開ZIP全バイト・SHA-256・MD5・CRC・内部チェックサム再取得検証を行う。その後に既存両台帳、Drive、Library、GitHubを同期してCP27を完了とし、B22へ進む。

このcheckpointはGitHubのみへの中間記録であり、Drive・Library・両台帳の完了同期を意味しない。研究の正式判定変更は0、独立したPDE再実行は0。
