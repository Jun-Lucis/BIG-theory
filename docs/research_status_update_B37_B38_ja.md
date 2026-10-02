# BIG 後期研究状況 — B37からB38

**日付:** 2026-10-02  
**範囲:** 絶対ピーク時刻の感度問題から、相対的時間構造と重み付き測定双対性への転換

過去の正式判定は変更しない。本稿はB30–B36以前の結果を再評価するものではない。

## B37 — 絶対ピーク時刻を基本量とみなすことへの疑問

B37では、角度座標ではなく境界輪郭の固有弧長を使い、さらに読み出しsupportの固有幾何を固定してピーク時刻を検査した。

正式判定は、

- B37.1: `INTRINSIC_CONTOUR_REPARAMETERIZATION_FAIL`
- B37.2: `FIXED_ARC_SUPPORT_TIMING_COLLAPSE_FAIL`

であり、いずれもFAILのまま保持される。

B37.2の失敗は絶対ピーク時刻のcross-resolution閾値に局在した。その後の非claim診断では、外側probeのピーク時刻がsubcell grid phaseに大きく依存することが分かった。一方、同じ非振動pulse traceを時間シフトとaffine調整で比較すると、共通波形は非常に高く再現された。

このため、B37は失敗を救済するのではなく、「絶対時刻」から「相対lag」へ観測量を変更する動機になった。

## B38.1 — 相対境界lag

B38.1では、最も近い固有probeを基準にrelative lagを前向き検査した。

正式判定:

`RELATIVE_BOUNDARY_LAG_GEOMETRY_PASS`

主要値:

- primary pairの最小 (R^2): 0.9849076
- 最小shifted correlation: 0.9962552
- geometry内phase relative slope span最大: 1.0067%
- N128/N160代表relative slope差: 0.0256%

これは tested finite model 内のcoherentなrelative-lag relationを支持する。wave、front、propagation speed、resonance、dispersion、continuum theorem、universal lawは主張しない。

## B38.2 — source/receiver swap

B38.2-P1では、同一dual-support構成でsourceとreceiverを入れ替えた。

正式判定:

`DIRECTED_SOURCE_RECEIVER_SWAP_ASYMMETRY_PASS`

fresh direct trace defectは約0.0678–0.0748、best-shift magnitudeは約0.230–0.300だった。時間rephasing後の最小相関は0.99997を超えた。

したがって、tested finite reduced model内で再現可能なdirected swap asymmetryを支持する。

## B38.3 — tangent operatorの構造

B38.3-P1は、exact semi-discrete tangent operatorがstandard metricではnon-self-adjointだが、D-weighted metricでは著しくnear-symmetricであることを前向きに確認した。

正式判定:

`D_WEIGHTED_NEAR_SYMMETRY_WITH_DIAGONAL_CYCLE_OBSTRUCTION_PASS`

N160ではD weightingによりedge asymmetry measureが約456–466倍縮小した。

compatible discretization controlを導入したB38.3-P2-P1では、

`COMPATIBLE_GAMMA_RESIDUAL_CYCLE_WITH_DISCRETIZATION_DOMINANCE_PASS`

を保持した。compatible gamma=0 controlはD-weighted defectとcycle obstructionをroundoffまで閉じ、directional cubic tangentはより小さなfinite-grid residualを再導入した。

continuum persistenceやfundamental non-reciprocityは結論しない。

## B38.4 — operatorからresponseへの前向きbridge

B38.4-P1は、fresh nonlinear responseを1本も実行する前にtangent predictionを凍結した。

正式判定:

`TIME_DEPENDENT_TANGENT_RESPONSE_BRIDGE_PASS`

N160の主要予測値:

- directed trace defect最大: 0.0007851
- directed trace correlation最小: 0.99999923
- swap-defect absolute error最大: 7.14e-05
- best-shift error最大: 0.0025

したがって、evolving tangent field operatorはtested small-amplitude nonlinear directed responseを高精度に前向き予測した。

## B38.5 — gammaは大きなtiming rephasingの主成分ではない

B38.5-P1では、time-dependent D-compatible gamma=0 controlの下でも大きなswap rephasingが残るかを前向きに検査した。

正式判定:

`D_COMPATIBLE_GAMMA0_REPHASING_RETENTION_PASS`

C0/observed absolute-shift ratioの最小は0.93だった。original tangentからgammaを外したとき、frozen timestep resolutionでbest shiftは変化せず、compatible (C_gamma-C_0) timing increment最大もO1 shiftの0.93%未満だった。

これはnonautonomous time dependenceを唯一の原因として確定するものではない。

## B38.6 — 重み付き測定双対性

B38.6-P0はhistorical calibrationでありscientific verdictは付与していない。そこから最終のprospective hypothesisを選択した。

B38.6-P1はfresh B38.6-P1 trajectoryを1本も実行する前にprotocolをfreezeした。

正式判定:

`D_WEIGHTED_DUAL_READOUT_SUPPRESSION_PASS`

fresh結果:

- standard absolute best shift最小: 0.235
- frozen-D dual / standard ratio最大: 0.14737
- instantaneous-D dual / standard ratio最大: 0.17021
- frozen-D ratio平均: 0.09299
- instantaneous-D ratio平均: 0.15537
- frozen-C0 weighted-dual swap defect最大: 3.14e-16
- frozen-C0 weighted-dual absolute best shift最大: 4.44e-16

したがって、standard readoutで見えていた大きなtiming rephasingの大部分は、operator-compatibleなD-weighted dual receiverへ測定関係を変えることで強く抑制された。

## B38終端解釈

B38の流れは次のように整理できる。

```text
絶対peak timingの数値的不安定性
    -> coherentなrelative lag
    -> 再現可能なsource/receiver swap asymmetry
    -> time-dependent tangent operatorによる前向き予測
    -> gammaは大きなtiming contributionの主成分ではない
    -> D-weighted dual readoutで大部分のrephasingが抑制
```

最も強く支持されるのは「fundamentalな一方向時間法則」ではない。観測されるtiming asymmetryが、operator・source・receiver・readoutの関係に強く依存するという有限モデル上の結果である。

残るevolving weighted-dual residualの起源は未解決である。これをfundamental、irreducible、observer-limited、あるいはnonautonomous time orderingのみに起因すると解釈しない。

## 公開

**B38タイトル:** *Relational Timing and Weighted Measurement Duality in a Finite Nonlinear Boundary Field Model*  
**副題:** *From Directed Source–Receiver Rephasing to Operator-Compatible Readout*  
**DOI:** https://doi.org/10.5281/zenodo.23104248

Repository entry: [papers/B38_relational_timing_weighted_duality](../papers/B38_relational_timing_weighted_duality)
