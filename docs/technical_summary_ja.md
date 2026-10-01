# BIG 技術サマリー — 1ページ証拠ガイド

**境界情報幾何学（Boundary Information Geometry; BIG）** は、境界を明示的な数理対象として扱う数理・数値研究プログラムです。境界を、動的場、幾何コスト、履歴を持つinterface、readout構造、branch / reconfiguration geometry、有限時間response zero setなどとしてモデル化します。

## 現在のprogramme-level結論

> **BIGは、系固有の境界幾何・応答・履歴・branch structure・reconfigurationを比較するための共通形式言語を提供する。現時点の証拠は、programme全体に一つの普遍的定量境界則があることを確立していない。**

重要な区別は、

```text
構造的 / 形式的な比較可能性
    !=
定量的普遍性
```

です。現在の証拠は前者を研究上の整理原理として支持しますが、後者は確立していません。

## 検査した縮約モデル内で何が成立しているか

複数の系列で、再現可能またはprospectiveに検査された構造があります。

- **境界形成と着地:** 検査した退化混合勾配PDEでは、compact-likeな局所境界とおよそ二次の着地 (phisim As^
u, 
uapprox2) が頑健に現れる。
- **有限時間安定性幾何:** 検査したprotocolでは、境界異方性がsurvival/runaway閾値を動かす。
- **分離型metastability:** B9の
  [
  E(Omega;lambda)=sigma P(Omega)+lambda C(Omega)
  ]
  はcompact branch、有限barrier、separated branchを生成する。
- **historyとreadout:** B14–B18では明示的history-bearing boundaryを構成し、stored historyとlocally/path-readable historyを区別する。
- **operator-generated response geometry:** B20で
  [
  F_T(P)=Z[U_T(P)]-Z[P],qquad
  mathcal B_T={P:F_T(P)=0}
  ]
  を定義し、B20–B22では限定されたfrozen branch / subspace内でlocal normal、Hessian、曲率、short-horizon forecastが有限解像度で有用。
- **family内prospective transfer:** B25 Phase I / IIでは、検査したfamily内でprospectiveに成功するboundary-functional reductionが得られ、ellipse familyではfixed perimeter coefficientまで縮約できた。

## より強い主張はどこで止まったか

後半では、局所成功をより広い定量法則へ昇格できるかを意図的に検査しました。

- **B19:** 検査したray-independent upstream scalar collapseは得られない。
- **B19E:** frozen TIDE holdoutでは、3つのB19追加量はstrong baselineを越える追加予測情報を確立せず（\(\Delta R^2=-0.00285\)、95% CIは0を跨ぐ）、判定は **NULL_OR_INCONCLUSIVE**。別Stageのexact local budgetはほぼmachine precisionで閉じたが、primary predictive resultは救済しない。
- **B20.6:** frozen finite-distance crossingはinformative caseが1件だけで **INCONCLUSIVE**。
- **B23:** branch-transfer evidenceは良好だが、endpoint近傍2対象で凍結したsymmetric-window ruleが実行不能だったため、元のaggregate planは **INCONCLUSIVE**。
- **B23A:** 新B9 familyへのsmooth-normal transferは支持されず、P3ではtopology-sensitiveなpiecewise/reset representationを支持。P4–P5の強いnon-topological reset/locality主張は数値的にinconclusive。新規held-out条件のP6ではmonotonic rate-ordering仮説は、numerical integrity gate通過後に **NOT SUPPORTED**。
- **B24:** 監査したBIG各sectorが最初から一つの実質的operatorを共有していたことは確立せず、**MULTIPLE_BOUNDARY_CLASSES_INDICATED**。
- **B26:** ellipse family内で移植できたfixed coefficientは、新しいtopology-straddling two-center familyではprospectiveに失敗し、median relative error **42.91%**、maximum **44.79%**。

これらはpost-hoc tuningで消すべき失敗ではなく、理論の適用範囲を決める証拠として保持します。


## 後期update — B27からB36

後期のresponse-lineage / response-to-timing programmeでも、局所的成功をより強い普遍則へ昇格することには明確な境界が残ります。

- **B27:** retained readable historyはlocal response geometryをprospectiveに変化させました（`HISTORY_RESPONSE_GEOMETRY_PASS`）が、単純なtopology-reconfiguration covarianceは失敗しました（`RECONFIGURATION_COVARIANCE_FAIL`）。
- **B28:** geometry-only component-resolved 1-to-2 lineage transportをfresh targetでprospectiveに検査し、3つの有効targetすべてで `GEOMETRY_CONDITIONED_LINEAGE_TRANSPORT_FAIL`。stop ruleによりB28.2は開かれませんでした。
- **B29:** inherited readability / validity gateを満たしたtraining caseが18/27にとどまり、held-out prediction前にprogrammeをclose。M0/M1/M2のheld-out predictive verdictはありません。

B28–B29統合preprint DOI: https://doi.org/10.5281/zenodo.23050390

- **B30–B36:** PASSとFAILを両方保持した統合programmeです。history-conditioned transverse suppression、reflection parity、period-dependent lifting、spatially structured complex transfer kernelを得る一方、dynamic suppressionと共通linear pulse-timing lawの強い主張はFAILのままです。最終B36.2は、fresh finite grid上でfitted peak-timing slopeがgeometry-conditioned componentとreadout-sampling componentへ近似的に加法分解できるという、より限定された主張をprospectiveにPASSしました。

B30–B36統合preprint DOI: https://doi.org/10.5281/zenodo.23048197

B36.2はphysical propagation speed、ballistic transport、finite-speed propagation、propagating / standing wave、wave equation、resonance、dispersion relationを確立しません。

## 現在BIGが主張していないこと

BIGは現時点で、次を確立していません。

- 一つの普遍的boundary equationやscalar invariant
- universal response-normal field、reset law、critical rate
- continuum free-boundary / curvature theorem
- Navier–Stokes blow-up / regularity result
- 核分裂・核融合・生物・認知・AI・宇宙論の定量理論
- domain-specific calibrationなしの外部実証妥当性

## 何がまだopenか

現在のopen questionはかなり限定されています。

1. 座標やmodel familyが変わっても残るtransformation / covariance ruleとしてformal objectを定式化できるか。
2. 何がbranch-local invariantで、何がfamily-dependent coefficientで、何が単なる便利な座標なのか。
3. finite-resolution prospective resultの一部をcontrolled continuum statementへ持ち上げられるか。
4. domain-specific equation、unit、calibration、empirical comparisonを課した後でも残るBIG構造はあるか。

## 推奨される解釈

現在もっとも強く保持できるまとめは、

> **複数のBIG縮約モデルでは、有用な局所・family-restricted境界幾何が得られる。一方、prospective testはprogramme-wideな定量transferに明確な限界を与えている。**

です。

詳細は以下を参照してください。

- [B27–B36 後期研究状況](research_status_update_B27_B36_ja.md)
- [統合research status map — B3からB26＋B23A](research_status_map_B3_B26_ja.md)
- [Limitations and scope](limitations.md)
- [Publication map / DOI index](publication_map.md)
- [引用方針](citation_policy_ja.md)
