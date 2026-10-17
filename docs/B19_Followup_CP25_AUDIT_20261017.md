# BIG B19追補 B19.21–22 CP25監査記録

日付: 2026-10-17 JST  
評価: **基本的に再現可能。独立した再実行監査は未了**  
改訂版: v1.1、DOI 10.5281/zenodo.23427904（公開済み・公開再取得確認済み）  
旧公開版: https://zenodo.org/records/22769513  
GitHub: https://github.com/Jun-Lucis/BIG-theory

保存データと実装・出典を監査し、科学数値、原表2件の全セル、原画像4件、原claim ledgerの正式分類を保持した。今回の監査では新しいODE/PDE軌道を生成していない。原計算の回復時に行われた歴史的再計算と、現在の保存値検算を区別する。

## 回収と版の照合

原ノート18件（2,620,167 bytes）とDrive結果98件（13,171,598 bytes）を回収した。旧公開ZIPは4,466,498 bytes、26 members、MD5 `cfbd52e2a86dd0967acb5939d579cea9`、SHA-256 `95bb284141a56687696ab2d07fa54558857a0eb557df38006c5d11418be6d272`。CRCは正常。内包する7段階のpackageを展開して保存した。

旧top-level manifest25件、現行段階package内81件、内包するlegacy C manifest26件はすべて一致し、歴史的hash検査は合計132件通過。5つの段階ZIPはDriveコピーとバイト一致。complete CはZIP容器のbytesが異なるが、23メンバーのファイル内容はすべてDriveコピーとバイト一致した。D packageは原公開ZIPと対応する実行出力付きノートを出典とする。

提供英語PDF v1.0は11ページ、439,606 bytes、MD5 `4ce205411d6945c88f71bf973aeb17c1`で公開metadataのchecksumと一致。SHA-256は `b8695fa1b4df175b8f0d454230276a875e6c6349c8caf644383d1c44371d71e5`。旧公開英語DOCXと日本語reference DOCXも取得した。日本語v1.0は未改訂の以前の版として保持し、今回v1.1と同版の翻訳とは扱わない。

10公開ノートについて、選んだ実行履歴付き原ノートの最終関数定義とのsyntax-tree照合がすべて一致した。全cellテキストの一致を全件では主張しない。setup/export cellや追加helper、重複定義、履歴・実行順序の差は保持した。258個のトップレベル定義を本文無変更で10名前空間に抽出し、実験ループを走らせずにロードした。48種の関数名を含む。

B19.22-Cにはcheckpoint優先の `dz` helperと、その後の再定義が同居する。上から通した際の最終定義と公開ノートは一致するが、元履歴はcleanなfresh-run認証とは扱わない。A/Cの履歴には中断や出力補助のエラーが残る。B19.21-A/Bの独立した原ノートは未回収であり、公開21B表とその代数・順序の検算を根拠とする。

## 保存結果の検算

`code/verify_saved_results.py` は原公開packageのCSV/JSONを読み、**2,100検査群・85,045数値またはラベル比較で全件一致**した。これらは同一資料の再利用・重複検査を含み、独立標本数ではない。

- B19.21-C/A/B/Cの保存時系列についてbalance、半enstrophy差、台形積分、積分残差を再計算。
- 21Cの6件のevent readoutと、Aとの共通246サンプルの同一性を確認。最初の正のbalance保存時刻は6件とも丸めて0.005。
- Aの48 horizon readoutと24 survival行を再計算。T=0.010は3方向とも分離を保持、T=0.012では0/3。
- Bの75 scalar casesとCの38 scalar casesの全保存horizon readoutを時系列から再取得。Cは38×81=3,078行を確認。
- 歴史的な欠落19件の回復監査57 readoutについて、旧値・新値・差・toleranceとcomplete Cとの対応を確認。これは既に保存された歴史的回復記録であり、本監査で独立に19軌道を再実行したものではない。
- 21BのG0=C0×theta0、K0=(1−C0)×omega_max0、coarse順序1/3、refined順序0/3と全6側のchi0=0を保持。
- Dの3,078 response samples、2,835隣接epsilon secants、243時刻別分類、80 root rowsを再構成。35件はT=0の自明なsampled zero、45件がsign change。
- Eの45 root geometry行、secant速度・加速度、raw slope-extremaの正負交差補間、方向別集計を再検算。根の内訳はp01=19、p02=23、p03=3。
- Fの全epsilon/time thinning、分類、交差時刻、集計を再計算。DとFの非ゼロ時刻full-grid分類240件は一致。6/6・10/10は同一38履歴から作る依存したdeterministic controlsとして扱う。

## 説明上の訂正と残件

| ID | 内容 | 対応 |
|---|---|---|
| B19F-A01 | nu=0.003、初期energy=30、periodic Biot–Savart、Fourier射影・zero mode除去、2/3 mask、RK4、adaptive dtを明示 | 本文追記 |
| B19F-A02 | complete trajectoryは保存scalar diagnostic historyを指し、全時刻の3D場ではない | 本文追記 |
| B19F-A03 | Cの歴史的19件回復再計算・57 readout照合と、今回の保存値検算を区別 | 本文追記 |
| B19F-A04 | BASE・ray endpoint・boundsと9個の主要計算関数はB19.17bと一致。epsilonは制御された有限の継続座標 | 出典照合保存 |
| B19F-A05 | D/E/Fは同じ38履歴のpost-processing。thinningは独立反復、PDE収束、外部検証ではない | 本文追記 |
| B19F-A06 | Dは一方のsignが存在し他方がない分類、Fは全secantが同符号という分類。現データの非ゼロ時刻では一致 | 定義差を明記 |
| B19F-A07 | rootはstrict sign changeと線形補間、T=0除外、速度・加速度もsecant。globalは検査したepsilon区間内 | 本文追記 |
| B19F-A08 | activationは最初の正の保存sample。balance積分は保存点での台形積分。短長窓prefixは共通履歴 | 本文追記 |
| B19F-A09 | cone-inspired G/KはB19のheuristic量でOpenAIの解析的stress cone変数ではない。21A/B元実行・事前登録履歴は未認証 | 代数結果保持・限界明記 |
| B19F-A10 | 元ノートのpath、checkpoint、helper再定義、履歴エラーを保全。fresh-run成功とはみなさない | 限界明記 |
| B19F-A11 | 原Figure 1はT=0.010の延長epsilon域だけを表示し、全表示値が負でzero crossingは図内にない | 図の画素は保ちcaptionを訂正 |
| B19F-A12 | bounded-domainの検出結果とglobal topologyの証明を区別 | 本文表現を限定 |
| B19F-A13 | OpenAI原資料・公式告知との出典整合を確認。proof、Lean、prize statusを独立認証しない | 主張の階層を維持 |
| B19F-A14 | 日本語v1.0 referenceは旧版。英語v1.1の同版訳ではない | 版を明記 |
| B19F-A15 | 独立した全ODE/PDE再実行、別discretization・連続極限、別初期family、外部transfer検証 | OPEN／本監査では未実施 |

Figure 1のT=0.010での最大DeltaZもp01=約−0.053856、p02=約−0.031304、p03=約−0.004214であり、3方向とも表示域内のzero crossingを示さない。refined reference rootsは表示epsilon下限0.5より小さい。このcaption修正で図や科学値は変更していない。

元claim ledgerの `REJECTED`、`PARTIAL / INSUFFICIENT`、`SUPPORTED IN ARCHIVED FAMILY`、`NOT SUPPORTED BY TESTED THINNING`、`NOT CLAIMED`、`NOT TESTED / NOT CLAIMED` を保持した。原表2件の全セル・formal outcome、原図4件を変更せず、本文とcaptionの解釈・再現性説明を訂正した。

外部資料の確認先はOpenAI公式告知 https://openai.com/index/navier-stokes-solution/ 、そこから示された原論文 https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf 、公式問題記述 https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf 。比較は供給原論文のTheorem 1.1とSection 2.1を対象とし、外部proofの独立検証をこの数値監査と混同しない。

この記録は公開前の固定時点の監査結果である。DOI予約、原資料回収、保存結果検算、改訂PDF14ページの全頁目視確認、原表2件・原画像4件の保持、258定義のソース同一性を確認した。公開後のZIP再取得・メタデータ確認・同期は別の最終receiptに記録し、最終公開状態はGitHubのCP25記録を参照する。


## CP25公開確認

https://zenodo.org/records/23427904 （v1.1、2026-10-17）。固定後のZIPは再構築せず、一つの完全版ZIPを公開した。公開リンクから再取得したファイルは固定版と全バイト一致し、25,020,630 bytes、279 members、CRCと内部278件のSHA-256を確認した。SHA-256 `5f921f90f450e1adfd84a78e9ececf1ccd150f3c849c4d9980356348af2e8332`、MD5 `98fa50848a6c0ae1c5b3e1d7fb68f88f`。別フォルダへの再展開検算は2,100群・85,045比較が一致し、receipt自体も同一。全10名前空間を実験なしでロードした。

公開JSONの16条件を確認。題名・著者・CC-BY 4.0・Preprint・keywordを保持し、既存のContinues DOI 22726848を保持。統合v1.1の23427540へのReferences DOIとGitHubのReferences / URL / Otherを追加し、説明文にもGitHubを記載した。原図・原表・科学値・正式判定は不変。A15の独立した全再実行監査・連続極限・別family・外部transferは未了。アーカイブ内の報告は公開前固定時点を保全し、この公開後追記は別管理する。

監査資料：https://drive.google.com/drive/folders/11ciDuh5UjbxLJ8O-y7hxwIwVeSJpB734
