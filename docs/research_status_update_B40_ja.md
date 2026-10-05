# BIG-B40 — 時計写像族転送と標的除外関係再構成

**論文:** *Clock-Family Transfer and Target-Excluded Relational Reconstruction in a Finite Boundary-Response Model*  
**著者:** Jun Lucis  
**Zenodo DOI:** https://doi.org/10.5281/zenodo.23153688  
**公開日:** 2026-10-05  
**状態:** B40 closed / Zenodo v1.1 公開済み

## 研究の問い

B40は、B39.3-P2で得られた有限モデル内のclock-map covarianceが、時計構成そのものを変えたときにどこまで残るかを調べ、その後、外部から与えた時計写像を主再構成座標から外したときに、非標的関係だけからheld-out responseを再構成できるかを検査した。

方法論はB37–B39と同じく、

```text
diagnostic / calibration
    -> response-blind freeze
    -> fresh claim-bearing evaluation
    -> FAILを保持
```

である。後続stageによって親FAILを遡及的にPASSへ変更しない。

## B40.1 — clock-map family transfer

先行する指数型clock-map familyを、応答を見ずに選択した放物型・正弦型の単調写像へ置き換えた。

```text
w_b(q) = q + b q(1-q),       |b| = 0.50
w_a(q) = q + [a/(2pi)] sin(2pi q),   |a| = 0.65
```

正式判定は

`CLOCK_MAP_FAMILY_TRANSFER_FAIL`

である。主条件の正弦型D0比較1件が、凍結した粗いlag grid上で0 tickとなったためである。一方、parabolic family、subcell phase、cross-resolution、response trace、final field、information-path量は凍結した共変性閾値内にあった。

続く10倍細密なlag gridを用いた前向き局在化では、

`LAG_GRID_QUANTIZATION_LOCALIZATION_PASS`

となった。ただし親FAILは保持する。

## B40.2 — target-excluded relational reconstruction

B40.2ではclock mapを再構成解析から外し、`evolving_Dt_dual`の非標的関係からFisher/Hellinger累積経路を作った。

```text
L_F(n) = sum_{j<n} 2 arccos( sum_i sqrt(p_i^(j) p_i^(j+1)) )
tau_F(n) = L_F(n) / L_F(final)
```

終点正規化を使うため、これは**offline relational progress coordinate**であり、intrinsic clockとは呼ばない。

最初の正式判定は

`TARGET_EXCLUDED_RELATIONAL_RECONSTRUCTION_FAIL`

である。resolution holdoutはPASSしたが、phase holdoutとnontrivial advantageが一様には成立しなかった。このFAILは保持される。

## 局在化と共変性

| Stage | Formal result | Retained interpretation |
| --- | --- | --- |
| B40.2-P1B | `PHASE_RESOLUTION_LOCALIZATION_PASS` | `PERSISTENT_Y_ORIENTATION_LIMIT_SUPPORTED` |
| B40.2-P1C | `AXIS_SWAP_ORIENTATION_LOCALIZATION_PASS` | `SOURCE_RELATIVE_ORIENTATION_SWAP_SUPPORTED` |
| B40.2-P1D | `NEGATIVE_PHASE_AXIS_SWAP_REPLICATION_PASS` | `NEGATIVE_PHASE_SOURCE_RELATIVE_SWAP_SUPPORTED` |
| B40.2-P1E | `ORIENTATION_REVERSING_COVARIANCE_TRANSFER_PASS` | fresh 23°/67° transfer |
| B40.2-P1F | `THIRD_ANGLE_ORIENTATION_REVERSING_COVARIANCE_REPLICATION_PASS` | third-angle 17°/73° replication |

最終的に凍結したorientation-reversing transformationは、`x <-> y` の空間交換、phase対応、channel permutation `[2,1,0]`、およびdirected target sideの `minus <-> plus` 反転を組み合わせる。

P1Eの23°/67°では全covariance componentがPASSし、categorical match fraction=1.0であった。P1Fの17°/73°でも同じ規則が再現され、categorical match fraction=1.0となった。P1Fにはfresh reconstruction failureが2件残るが、その2件自身が変換対を形成した。したがって「再構成が常に成功する」のではなく、**失敗する構造そのものまで同じ変換規則に従う**という結果である。

## 統合結論

最も強く支持されるのは、検査した有限半離散境界応答モデルにおいて、

> 再構成の成功と失敗が、source/readout orientationとdirected-side reversalを結ぶ再現可能なorientation-reversing covarianceによって組織される。

という限定された構造的結論である。

B40は、任意再パラメータ不変性、普遍的relation clock、emergent physical time、連続体回転共変性、物理的異方性、連続体定理を示していない。

## 公開記録

Zenodo DOI: https://doi.org/10.5281/zenodo.23153688

Zenodoには英語正式プレプリント、日本語参考翻訳、およびcompact reproducibility/audit packageを収録している。
