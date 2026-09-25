# BIG 研究状況更新 — B24-B25 Phase I

**日付:** 2026-09-25  
**主要DOI:** https://doi.org/10.5281/zenodo.22956894

このノートは、既存のB3-B23研究状況マップをB24-B25 Phase Iまで更新するものです。過去の凍結判定を書き換えるものではありません。

## 1. B24で何が変わったか

B24では、これまでに構築されたBIGの複数sectorが、すでに一つの非自明な共通数学operatorを共有しているかを監査しました。

出典監査付きの凍結mapping protocolでは、広い意味での「境界」という語彙は共通していても、必要条件を満たすcross-sectorのexact / coordinate-equivalentなsubstantive recurrenceは確認されませんでした。

**B24.2判定:** `MULTIPLE_BOUNDARY_CLASSES_INDICATED`

これは過去のBIG結果が無効という意味ではありません。むしろ、BIGが複数の数学的に異なるboundary classを形成してきたことを明確にした結果です。

## 2. B25で何が変わったか

B25では「統一」の問いを変更しました。

全sectorに同じnative operatorを要求するのではなく、sector固有のobject同士をtyped transferで接続できるかを検査します。

$$
X \to \Sigma \to J \to (X',H') \to F \to \mathcal B_R.
$$

最初のA→B constant-density reductionは失敗しました。

**B25.1判定:** `AB_CONSTANT_DENSITY_FAIL`

その後、保存済みprofileだけを使ったretrospective coarea decompositionからlevel-resolved transfer relationを構成し、新しいtrajectoryを計算する前に凍結しました。

新しいshape / resolution 9ケースで全基準を通過しました。

**B25.1b判定:** `AB_LEVEL_RESOLVED_BRIDGE_PASS`

主要数値は次の通りです。

```text
valid cases:                  9 / 9
最大relative error:          17.76%
中央値relative error:         9.49%
旧predictor中央値error:      29.79%
中央値error改善率:            68.15%
fine-resolution stability:    PASS
```

## 3. 現時点でのprogramme全体の解釈

現状の証拠から「BIGには一つの普遍operatorがすでに成立した」とは言えません。

一方で、次の限定的な主張は支持されます。

> 数学的に異なるboundary class同士であっても、少なくとも検査したcanonical settingでは、新しく構成したlevel-resolved transfer functionalによって接続でき、その関係が事前指定されたheld-out numerical testを通過した。

これは単なる類似より強く、sector間の完全な導出より弱い結果です。

## 4. 保持する判定

以下は変更しません。

- B19: robust ray-independent upstream scalar / robust 2D portraitは得られていない
- B20.6: `INCONCLUSIVE`
- B21: generic kinematic identityを新法則とは扱わない
- B23 original aggregate: `INCONCLUSIVE`
- B24.1b: `RESOLUTION_STABLE_FAIL`
- B24.1d: `PARAMETER_ROBUST_FAIL`
- B24.2: `MULTIPLE_BOUNDARY_CLASSES_INDICATED`
- B25.1: `AB_CONSTANT_DENSITY_FAIL`
- B25.1R: retrospective diagnostic only
- B25.1b: `AB_LEVEL_RESOLVED_BRIDGE_PASS`

## 5. 次のPhase

B25 Phase Iはここで終了です。

今後の候補は、

- thin-layer limitでの $\sigma_{\mathrm{eff}}P$ への縮約
- A由来boundary termをB9型shape-energyへ移す新しいheld-out test
- 独立したC→D bridge
- 新source family、異なるp、外部実装によるreplication

です。

これらはPhase Iの成果を成立させるための未完了作業ではなく、新しい研究段階です。
