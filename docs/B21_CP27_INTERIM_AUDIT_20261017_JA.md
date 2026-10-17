# BIG-B21 CP27 作業中監査・B22元資料所在 checkpoint

2026-10-17。状態：**INTERIM_AUDIT_RECORDED / REVISED_PUBLICATION_PENDING**。

標準評価：**基本的に再現可能。独立した再実行監査は未了。**

## 公開状態

B19 CP24（10.5281/zenodo.23427540）、B19.21–22追補 CP25（10.5281/zenodo.23427904）、B20 CP26（10.5281/zenodo.23428205）は公開と再取得照合を完了済み。これらの完了記録は変更しない。

B21の現在の科学公開版は v1.0、DOI **10.5281/zenodo.22876813**。本checkpointはGitHub上の説明補足と検算記録であり、新しいZenodo版の公開完了ではない。原表・原図・元の数値・正式分類は変更していない。

## B21 元資料の保全済み記録

元ノート4件、Drive結果255件、継承入力2件を含む261 source files / 3,335,004 bytesを回収した作業記録がある。初期source checkpoint：

- ファイル：BIG_B21_CP27_SOURCE_RECOVERY_20261017.zip
- サイズ：8,038,153 bytes
- SHA-256：5c518b8ebfeacebb95367d86393fad860b77470cbb135313154088c9b024520f

このsource checkpointは最終科学公開ZIPではない。最終の全体検算結果を現環境から読み戻せていないため、全体検算を完了扱いにしない。

## 今回独立して再照合した範囲

元E12ノート、B21_E12_FINAL_RESULT.json、B21_E12_FINAL_COMPONENTS.csv、凍結プロトコル、根区間CSV、E10 runtimeの基底CSVを再読取りした。

保存表の観測勾配差、transport、prediction、residual、速度、根区間尺度、ノルム、相対値、角度の**23比較がPASS**。入力snapshot、実行した数値本体を含むJavaScript、JSON receiptを同梱した。JavaScriptの数値本体は実行済み。ファイル入出力を含むNode CLIの起動確認は現環境では未実施。

- 残差ノルム：0.003901172984973377
- 相対残差：0.0012421543366251708（従来表示0.1242154%を保持）
- 角度：0.06989347694774377度（従来表示0.0698935度を保持）
- 観測側の根位置一次尺度：0.0068304254864559695
- その相対尺度：0.0021748439947874483（従来表示0.2174844%を保持）

これは保存表の代数的再計算であり、元PDE軌道、全101 scalar histories、全notebook実行の独立監査を完了したことは意味しない。

## 指摘1：0.2174844%の適用先と共通入力の相関

元コードの尺度は、中央のHVPを使い、根区間の半幅から観測側のDg/Dtへ伝播させた一次尺度である。同じ根が、予測側のboundary speedを通じてtransportにも入る。

したがって、この値をそのまま「観測−予測」の残差全体の誤差上限とは扱えない。根位置変動に対する端点勾配感度をa_minus, a_plus、中央HVPによる感度をa0とすると、

    delta_r ≈ ((a_plus − a0) delta_epsilon_plus
               − (a_minus − a0) delta_epsilon_minus) / Delta_T

となる。a_minus=a_plus=a0と条件付きで仮定した四隅の代数例では、観測と予測がそれぞれ最大約0.0068304変化しても、両者の共通の一次変化は残差で相殺する。

これは条件付きの代数診断であり、実際の残差の不確かさがゼロという主張ではない。端点での感度変化・高次項・基底精度・空間解像度・時間積分・内部差分の影響は統合して囲い込まれていない。0.1242154%と0.2174844%の数値的大小は保持するが、大小関係だけで追加項の不在や不確かさを考慮した閉包を証明しない。

## 指摘2：初期探索とE10・E12の基底精度

元E1は6桁表示の7×4 QWをnp.linalg.qrで再直交化する。E10・E12は高精度B20.5 QWを復元する。E12が用いる固定PのE4時間勾配は初期探索由来であるため、比較全体を厳密に同一座標の結果とは記述できない。

元の丸め行列に独立したHouseholder QRを施し、高精度runtime CSVと比較した。

- 最大基底成分差：約4.12432168×10^-7
- 部分空間射影行列差のspectral norm：約6.49660497×10^-7
- 双方の直交性残差：浮動小数点精度内

両基底はそれぞれ直交していても、完全に同じframe・部分空間ではない。原数値を回転・置換せず、差がPDE結果に及ぼす効果は未監査として明記する。

## 継続作業

1. 保存済み全体検算JSONの最終状態を読み戻す。
2. 原DOCX/PDFを保持し、上記二点、保存時刻とreadout、historical exportの由来、再実行の限界を本文へ補足する。
3. 元の全表セルと全図画素を保持し、新PDFの全頁表示検査を行う。
4. 新版DOIを実際のdraftで確認し、完全ZIPを一度だけ固定する。
5. Zenodo公開後、公開ZIP再取得・全バイト・CRC・内部hashを確認する。
6. 完了台帳、GitHub、保存先を同期し、その後B22以降B41まで順に進める。

現在の環境では以前のログイン済み公開用ブラウザーを引き継げず、ローカル実行・ファイル操作も応答を返していない。この接続状態をZenodoによるAI拒否の証拠とは扱わない。B21新版の作成・公開は本checkpointでは行っていない。

## B22 元資料所在

GitHubのB22 publication READMEと、Driveの元Colab・E1〜E5直下metadataを確認した。**所在同定のみ**であり、ダウンロード完了、hash照合、科学監査完了とはしない。

元ノート5件、metadata上の合計2,102,566 bytes：

- BIG_B22_E1_FULL_HESSIAN_GEOMETRY_FROZEN_v1.ipynb
- BIG_B22_E2_TEMPORAL_NORMAL_ROTATION_AUDIT_v1.ipynb
- BIG_B22_E3_R09_PROSPECTIVE_NORMAL_ROTATION_v1.ipynb
- BIG_B22_E4_R09_T1_FULL_CURVATURE_COMPLETION_v1.ipynb
- BIG_B22_E5_R09_PROSPECTIVE_CURVATURE_v1.ipynb

E1〜E5直下で82 files・12 subfoldersを確認した。再帰的な全結果数は未集計。凍結予測、root scan/refinement、最終summary、comparison、Hessian/eigensystem、trajectory cachesの所在を同定した。内容は未監査であり、正式な研究判定を変更しない。



## CP27復旧後の追加監査（2026-10-17）

これは新規の保存結果照合・改訂原稿の**公開前checkpoint**。Zenodo新版公開、固定ZIP公開再取得、Drive／Library最終同期は未完了であり、CP27を完了扱いにしない。

- Library source recovery ZIP 8,038,153 bytes、SHA-256 `5c518b8ebfeacebb95367d86393fad860b77470cbb135313154088c9b024520f` を復元。ZIP CRCエラーなし。元source manifestの **261件／3,335,004 bytes** に対してサイズ・SHA-256が261/261一致。
- **101** scalar timeseries CSV、**7,335行**。行数は61行×27、63行×17、81行×57。終端は0.015、0.0155、0.020（浮動小数点表現）。均一長ではない。保存 enstrophy_half(t)−enstrophy_half(0) から再計算できる `F_T*` と対応summaryの**72比較**で差分ゼロ。101本全てにsummaryがあるわけではなく、全体検算を意味しない。
- 復元元E12最終JSON・成分CSVとB20.5 QW/scalesを用いて**23の保存表代数比較 PASS**（最大絶対差 `2.78e-17`）。これは元PDEの再実行ではない。
- 英語・日本語の改訂DOCX **各8表・151表セル・原図5枚・既存数式XML**を原版と一致確認。v1.1 DRAFTの仮PDFは各15ページまでrender。論旨上、共通根相関、0.2174844%が観測側尺度である点、座標精度差、未検証境界を本文で補足した。原数値・図画素・表セルは不変更。
- 旧Zenodo v1.0メタデータのDescriptionにはGitHubが存在するが、Related worksにはGitHub URLの項目がない。新版で追加する。実際の新DOIは未取得なので**固定完全ZIPはまだ作らない**。
- Browser読み取りは起動元拡張コンテキスト不足で失敗。Zenodo draft作成・Publishはまだ実行していない。TinyFishの保存プロファイルにZenodoログイン登録が見えないため、有料実行を勝手に開始しない。

引き続き**「基本的に再現可能。独立した再実行監査は未了」**。全体検算の旧最終JSONは依然未確認で、上記72＋23比較をこれに代えない。


## CP27追加checkpoint：保存系列の全行照合と二重保存（2026-10-17）

**状態：CP27_WORKING / NEW_ZENODO_VERSION_NOT_PUBLISHED**。完了済みCP24〜CP26の記録は変更しない。標準評価は **「基本的に再現可能。独立した再実行監査は未了」**。

復旧済みの原資料ZIP（SHA-256 `5c518b8ebfeacebb95367d86393fad860b77470cbb135313154088c9b024520f`）だけを入力とした新規保存成果物検算を作成・実行。旧全体検算の最終JSONを発見したわけではない。

- `code/B21_recovered/reconstructed_saved_artifacts_audit.py` および `docs/B21_CP27_INTERIM/Reconstructed_Saved_Artifacts_Audit_Result_20261017.json` を追加。独立した**保存済みデータの整合性検査**であり、PDE軌道の再計算ではない。
- 時系列101 CSV / 7,335行、各行の `enstrophy_half - enstrophy_half(t=0)` と `delta_enstrophy`、および `stretch_total - dissipation_total` と `balance_total` の合計 **14,670件が一致**。終端時刻は0.015/0.0155/0.020で混在。
- 対応する72 summaryの **120個のF(T)** を保存済みenstrophy_halfから再構成し照合一致。
- E10-h1, E10-h2, E12-gradientの凍結manifest合計48行とsummary ID・適用条件を照合一致。
- E12のT=0.0115/0.0125における2つの根区間：符号反転、中点・幅、事前固定幅、凍結記録との照合一致。これは根の物理的妥当性を独立に証明しない。
- 原文と図・数値を保持した改訂EN/JA DOCX・PDF、検算receipt、メタデータdraft各8件をChatGPT Library保存し、Driveにも保存。Driveを再ダウンロードした**8/8件がバイト一致**。照合JSON：`docs/B21_CP27_INTERIM/Drive_Readback_Receipt_20261017.json`。
- Library作業フォルダ：`/BIG_B21_CP27_WORKING_20261017/`。Drive作業フォルダ：`https://drive.google.com/drive/folders/1GUJUuKAkDHK55C3MOnkSvD1fKHQUb4dj`（**PENDING**）。前回のLibraryアップロード接続障害は再試行で解消した。
- Zenodoブラウザーのログイン表示は取得できたが、開いていたのは別研究B42のdraftであり、変更しなかった。現行Browser接続はread-onlyでありB21の新規版作成・予約DOI・publishは実行していない。未確認のdraftを重複作成しない。

**検査境界：** 原データの既存列内整合性と保存summary・manifest・凍結根の照合に限定。元PDEコードを独立に走らせて再生成したこと、誤差の全体包絡を得たこと、歴史的な正式PASS/FAILを変更することを意味しない。完全ZIPは実際の新版DOI取得後に一度だけ固定する。
