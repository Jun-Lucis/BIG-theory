# BIG-B41 — 軌道空間応答幾何と有限パラメータ転送

**論文:** *Prospective Trajectory-Space Response Geometry and Second-Order Finite-Parameter Transfer*  
**著者:** Jun Lucis  
**Zenodo DOI:** https://doi.org/10.5281/zenodo.23249677  
**研究の状態:** B41正式終了。P1・P2・P3の元の判定は変更しない。

## 研究目的と対象

B41は、局所パラメータ変化から得た応答の接線・二階差分が、まだ計算していない有限距離のパラメータにおける応答軌道をどこまで予測するかを検査する。

対象は、B20系列を継承する**三次元周期領域の粘性ベクトル渦度モデル**である。六つの固定時間窓で読み出した半エンストロフィー応答を六次元ベクトルとして扱い、Family-Cの正規化された四次元パラメータ部分空間で数値的な局所接線 `V_h` と二階応答 `A_h` を測る。ここでいう「軌道」は応答の六時間窓ベクトルであり、物理空間の物体軌跡や自由境界そのものではない。

## 固定判定の連鎖

| 段階 | 正式判定 | 主な結果 |
| --- | --- | --- |
| P1 | `TRAJECTORY_RESPONSE_GEOMETRY_TRANSFER_PASS` | 32/32で一次接線転送がnearestを上回り、pooled weighted RMSE改善97.7883%。全Gate A–F PASS |
| P2 | **`DIMENSIONLESS_REMAINDER_TRANSFER_FAIL`** | 新規48件で一次転送は88.1862%改善したが、スカラー二階余剰の20%不一致基準を満たしたのは24セル中19セル。Gate C/E FAIL |
| P2事後診断 | 原判定を変更しない | 不一致5セルを接線・二階応答が強く反平行な2群へ局在化 |
| P3 | `FULL_SECOND_ORDER_GEOMETRIC_REMAINDER_TRANSFER_PASS` | 別の新規48件で一次転送93.1041%改善。full二階予測が24/24セルで20%以内。全Gate A–E PASS |

**P2のFAILはP3のPASSによって救済・再判定されない。**

## P2で判明した限界

P2で凍結したスカラー指標は

```text
Q2_scalar(dp) = (|dp|/2) * ||A_h|| / ||V_h||
```

であり、`V_h` と `A_h` のなす向きの情報を使わない。20%を超えた5セルは `E_u10`（3セル）と `H_u16`（2セル）に集中し、両者の角度余弦はそれぞれ約 `-0.998970`、`-0.985142` だった。

この診断を受け、向きと符号を残す新しい無fit予測量を提案した。

```text
Q2_full(dp) = [0.5 * dp^2 * ||A_h||]
              / [||dp * V_h + 0.5 * dp^2 * A_h|| + eps]
```

P2の結果を開封した後の計算は**事後診断**であり、前向き成功とは呼ばない。

## P3の前向き結果

P3は新しいアンカー I–L・方向 u17–u24 に対し、target PDE実行前に予測を凍結した。凍結時点では局所幾何8/8群PASS、fresh target PDEは0/48件。正式evaluatorは1回だけ実行された。

- tangent転送がnearestより良かった対象：**48/48**
- pooled weighted RMSE：nearest `0.01638094006` → tangent `0.00112961088`（**93.1041%改善**）
- full二階予測と観測不一致のSpearman順位相関：**0.9973913**
- full二階予測の相対不一致中央値：**0.6792%**
- 20%不一致基準以内：**24/24セル**
- 8h・16h・24hの各距離で順位相関 **1.0**
- 新規の強い反平行例 `J_u20`（`-0.972471`）、`K_u22`（`-0.996708`）を含む

**比較上の重要な留保:** P3のfresh setでは非主判定のscalar `Q2_scalar` も24/24セル達成、相対不一致中央値 **0.6755%**、Spearman相関 **0.9973913** だった。したがってfull版の一般的優越性、方向情報が常に必須であることは証明していない。

## 射程と資料

支持されたのは、**特定の有限合成応答系において、事前に固定した二階幾何量が新しいパラメータ対象の相対転送誤差を無fitで定量予測できたこと**である。

これはBIG固有のTaylor定理、連続体定理、任意再パラメータ変換不変性、実物理系の普遍則、Navier–Stokes正則性証明、外部実験検証ではない。

**正式英語論文・日本語参考翻訳・凍結アーカイブ:** https://doi.org/10.5281/zenodo.23249677  
**English status:** [research_status_update_B41.md](research_status_update_B41.md)  
**論文案内:** [papers/B41_trajectory_space_response_geometry](../papers/B41_trajectory_space_response_geometry/README.md)  
**失敗保存の研究方法論:** https://github.com/Jun-Lucis/failure-preserving-research

正式判定の歴史は `P1 PASS → P2 FAIL → P2事後診断 → P3 fresh prospective PASS` として保存する。
