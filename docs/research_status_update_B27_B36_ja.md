# BIG 後期研究状況 — B27からB36

**日付:** 2026-09-30  
**範囲:** B3–B26統合status map以後の更新

この文書はBIG-B27からB36までのretained statusをまとめます。後続結果によって過去のformal verdictを再評価・格上げしません。

## B27 — history-conditioned response geometry と reconfiguration

B27は二つの異なる結果で終了しました。

- **B27.1:** `HISTORY_RESPONSE_GEOMETRY_PASS`
- **B27.2:** `RECONFIGURATION_COVARIANCE_FAIL`

同一の現在 `phi` に対しても、保持されたreadable historyは、検査した縮約モデルの正規化local response geometryを変化させました。一方、connected-to-disconnected reconfiguration後では、凍結したidentity covariance mapは3つの有効prospective targetすべてで失敗しました。

したがってB27は、

```text
history-conditioned response
    !=
reconfiguration-invariant response lineage
```

を支持します。B27.2の有効FAILによりstop ruleが発動し、B27.3は実行されませんでした。

## B28 — geometry-conditioned lineage transport

B28では、B27で失敗したidentity covarianceの代わりに、geometry-onlyのcomponent-resolved 1-to-2 split transportを検査しました。

calibration後、B28.1はfresh split target

[
delta_{m post}=5.3, 5.6, 5.9
]

でprospectiveに実行されました。3対象はすべて数値的に有効でしたが、lineage-transport defectはおよそ

[
0.15334,quad 0.15247,quad 0.15644
]

で、凍結PASS閾値

[
epsilon_{m split}le0.009
]

を大きく上回りました。

formal verdict:

`GEOMETRY_CONDITIONED_LINEAGE_TRANSPORT_FAIL`

B28.1が有効にFAILしたため、frozen ruleに従いB28.2は開かれませんでした。

## B29 — instantaneous geometryを越えるincremental predictive information

B29は **B29.1 held-out evaluationを一度も行わずに終了** しました。

B29-P0でresponse-blindな36-case gridと27 training / 9 held-out splitを凍結しましたが、B29-T1でreadability / numerical-validity gateを通過したtraining caseは

[
18/27
]

だけでした。

terminal training statusは

`T1_valid=False`

です。

relative history-write angleが (25^circ) と (55^circ) のtraining caseはすべて有効でしたが、(85^circ) stratumはすべてfrozen response-readability gateを満たしませんでした。この角度依存性はhypothesis-generatingとしてのみ保持されました。

held-out prediction setは凍結されず、held-out post-responseも計算されていません。したがってM0/M1/M2のpredictive performanceについてのformal verdictはありません。正しいterminal interpretationは「凍結したB29 training domainが一様にresponse-readableではなかった」です。

## B30–B36 — responseからpulse timingへの統合programme

B30–B36は後に一つのpreprintへ統合されました。

**From History-Conditioned Boundary Response to Geometry-Conditioned Pulse Timing in a Finite Reduced Model**

DOI: https://doi.org/10.5281/zenodo.23048197

claim-bearing stageのretained verdictは次の通りです。

| Stage | Retained verdict |
| --- | --- |
| B30.1 | `TRANSVERSE_HISTORY_RESPONSE_SUPPRESSION_PASS` |
| B31.1 | `REFLECTION_PARITY_MODE_PASS` |
| B32.1 | `DYNAMIC_COMPLEX_PARITY_MODE_FAIL` |
| B33 primary | `FREQUENCY_DEPENDENT_TRANSVERSE_NODE_LIFTING_PASS` |
| B33 second grid | `PERIOD_DEPENDENT_TRANSVERSE_NODE_LIFTING_PASS` |
| B34.1 | `SPATIALLY_STRUCTURED_COMPLEX_TRANSFER_KERNEL_PASS` |
| B35.1 | `DISTANCE_ORDERED_APPROX_LINEAR_PEAK_TIMING_FAIL` |
| B35.2 | `HIGHER_RESOLUTION_SAMPLING_STABLE_APPROX_LINEAR_PEAK_TIMING_FAIL` |
| B36.1 | `GEOMETRY_CONDITIONED_PEAK_TIMING_ORDERING_FAIL` |
| B36.2 | `ADDITIVE_GEOMETRY_SAMPLING_DECOMPOSITION_PASS` |

B32.1、B35.1、B35.2、B36.1はformal FAILのままであり、後のPASSによって救済・再評価しません。

B36.2が支持するterminal statementは限定的です。

> 検査したfresh finite numerical grid内では、fitted peak-timing slopeはgeometry-conditioned componentとreadout-sampling componentへ近似的に加法分解でき、かつgeometry orderingは検査したsampling shiftすべてで保持された。

fresh B36.2 gridでは12 lattice cellすべてがpassし、geometry row-mean spanは (0.00690625)、interaction fractionは (0.0786605le0.20)、normalized maximum interactionは (0.0503345le0.10) でした。

これはuniversal quantitative (b(q)) law、sampling-invariant absolute slope、physical propagation speed、ballistic transport、finite-speed propagation、propagating / standing wave、wave equation、resonance、dispersion relationを確立するものではありません。

## B27–B36の統合的解釈

```text
history-conditioned response
    -> simple reconfiguration covariance FAIL
    -> geometry-only lineage transport FAIL
    -> training-domain readability boundary
    -> transverse suppression and reflection parity
    -> dynamic suppression FAIL
    -> period-dependent soft-node lifting
    -> spatial complex transfer kernel
    -> structured pulse timing, but no common stable linear law
    -> fresh finite grid上のapproximate geometry/readout decomposition
```

positive resultだけでなく、prospective FAILを保持し、それを次の問いを狭めるために使うことがこの後期programmeの重要な方法論的特徴です。
