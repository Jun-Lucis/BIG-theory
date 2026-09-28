# BIG-B27 研究状況更新

**日付:** 2026-09-29  
**programme status:** CLOSED

## 範囲

B27では、有限縮約モデルにおいて次の二点を分離して検査した。

1. 現在の場が同一でも、保持履歴が局所応答幾何を変えるか。
2. その履歴由来の応答幾何が、topology再構成を越えて不変に保たれるか。

個体同一性、主観的連続性、意識、AI人格、生物学的遺伝、普遍的な「個」の法則は検査対象ではない。

## B27.1 — 履歴条件付き応答幾何

正式判定:

HISTORY_RESPONSE_GEOMETRY_PASS

同一の現在 phi 場から、履歴保持状態と履歴消去状態を比較した。前向きに固定した4つの履歴write角すべてで、N=128 と N=160 の両解像度において凍結した構造差閾値を超えた。

zero-feedback control は null のままであった。

限定的な結論:

> 検査した縮約モデルでは、読み出し可能な保持履歴は、後続応答の単なる大きさだけでなく局所応答幾何そのものを条件づけうる。

## B27.2 — topology再構成を越える共変性

continuationで準備したconnected training anchorにより、post targetを見る前に covariance threshold = 0.010 を凍結した。

その後、新しいconnected-to-disconnected target 3本を前向きに検査した。

| target | delta+ | primary lineage defect | 判定 |
|---|---:|---:|---|
| T1 | 5.40 | 0.1118248844 | FAIL |
| T2 | 5.70 | 0.1276381141 | FAIL |
| T3 | 6.00 | 0.1450767448 | FAIL |

3本すべてが数値・科学的 validity gate を通過した。

正式判定:

RECONFIGURATION_COVARIANCE_FAIL

再構成後も履歴効果自体は測定可能だったが、その正規化応答幾何は、凍結した identity covariance map の下では保存されなかった。

## 統合結論

B27が支持する区別は、

\[
\boxed{
\text{履歴条件付き応答}
\neq
\text{再構成不変な応答系譜}
}
\]

である。

検査した有限モデルでは、現在の応答は保持履歴に依存する。しかしtopology再構成は、その履歴条件付き応答の幾何を大きく変換する。

したがって次の問いは、「不変な系譜があるか」ではなく、**その変換を前向きに予測できるか**へ移る。

## 停止規則とB27.3

B27.3は実行しない。

有効なB27.2 FAILの後にcovariance mapを調整・置換することは新しい仮説になるため、凍結停止規則に従ってB27を閉じる。新しいtransport / transition lawはB28以降に属する。

## Repository記録

- papers/B27_history_conditioned_response_lineage/B27_1_RESULT_RECORD_v1_0.md
- papers/B27_history_conditioned_response_lineage/B27_2_RESULT_RECORD_v1_0.md
- papers/B27_history_conditioned_response_lineage/B27_CLOSEOUT_v1_0.md
- papers/B28_geometry_conditioned_lineage_transport/B28_0_DRAFT_architecture_v0_1.md
