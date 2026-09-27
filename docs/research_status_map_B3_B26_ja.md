# BIG研究状況マップ — B3からB26まで（B23A普遍性監査を含む）

## 何が成立し、何が限定され、何が支持されなかったのか

このページは、Boundary Information Geometry（BIG）の **B3からB26まで** と、その後に閉じた **B23A 構造的普遍性監査** を一つに統合した、現在の研究状況マップです。

旧B3–B23版は、programme-level status note の歴史的基礎として保存します。

- B3–B23 status-note DOI: https://doi.org/10.5281/zenodo.22939024

後続の正式記録:

- B24–B25 Phase I: https://doi.org/10.5281/zenodo.22956894
- B25 Phase II: https://doi.org/10.5281/zenodo.22967474
- B26: https://doi.org/10.5281/zenodo.22972985
- B23A universality audit: https://doi.org/10.5281/zenodo.22994445

ここで「成立」と書く場合、その意味は **明示した縮約モデル・パラメータ族・有限解像度・凍結した数値手順の範囲内** に限定されます。普遍定理、あるいは現実の物理・生物・認知・技術系における定量法則が成立した、という意味ではありません。

基本的な区別は次です。

```text
モデル内の結果
    != programme全体の定量的普遍性
    != 普遍定理
    != 自然界の実証法則
```

---

## 1. 統合研究状況マップ

| 系列 | 主な問い | 保持される結果 | 主な限界・未解決点 | 現在の状態 |
| --- | --- | --- | --- | --- |
| **B3–B4** | compact-like境界はどうゼロへ着地するか | 検査した退化混合勾配PDEで、(phisim As^
u, 
uapprox2) の二乗着地が頑健に現れる。 | 一般的universality classや厳密な連続体自由境界定理は未確立。 | **強い数値結果** |
| **B7–B8** | 局所境界regularityとglobal runawayは分離できるか。形状は有限時間閾値を動かすか | 局所境界構造と有限時間の大域的運命は分離し得る。検査した楕円族では異方性がsurvival/runaway閾値を動かし、報告した解像度検査でも順序は保たれた。 | 漸近separatrix、普遍的異方性則は未確立。 | **数値的に支持** |
| **B9** | boundary costとnonlocal repulsionだけで分離型metastabilityは出るか | (E=sigma P+lambda C) の縮約エネルギーでcompact branch、有限pinch/scission barrier、separated branchが現れる。 | 定量的核分裂理論ではなく、shell、pairing、tunnelling、yield、excitation、核データ較正を含まない。 | **縮約モデル内で成立** |
| **B10** | sustained captureはfirst contactと同じか | first hitとsustained captureは分離し、中間noiseで捕獲が現れ、高noiseで再び崩れる。 | 定量的核融合理論や外部stochastic resonance検証ではない。 | **強い数値結果** |
| **B11–B12** | capture後に非同化的な保持は可能か | assimilationとtwo-parent hidden-depth inheritanceの競合を構成でき、B12ではapproach、finite-noise lock、inheritanceを一つの縮約系に接続できる。 | 生物遺伝、実在fusion、一般的個体性法則は未確立。 | **縮約力学として成立** |
| **B13–B15** | observation-like selection、trace、historyを共通表現で扱えるか | basin-selection toy dynamics、明示的boundary-history field、operator-oriented history/update表現を構成・監査できる。 | 量子測定、Born則、意識、生物遺伝の導出ではない。 | **表現体系は成立／物理解釈は未確立** |
| **B16** | moving free boundaryは履歴を保持し再利用できるか | retained historyがfeedbackを通じて後の局所応答を変えることをkept/erased・shifted-stimulus controlで分離。 | 高次元の一般memory lawや外部較正は未確立。 | **縮約PDEで成立** |
| **B17–B18** | 保存された履歴の何が動的に読まれるか | global history massより、locally/path-readable historyが後の応答をよく整理し、B18ではinterface/core-gated readout operatorとして表現。 | 普遍的memory/readout operatorは未確立。 | **readout原理を数値的に支持** |
| **B19** | finite-window増大/減衰を単一upstream scalarで整理できるか | 検査したsingle observable / two-coordinate screenではray-independent collapseが得られず、direction-dependent channel familyの方が適切。 | Navier–Stokesの普遍指数、global separatrix、blow-up/regularity criterionではない。 | **重要な否定結果＋構造結果** |
| **B20** | finite-window response zero setをoperator-generated boundaryとして扱えるか | (mathcal B_T={P:F_T(P)=0}) の到達可能性はdirection-dependent。frozen normalized 4D Family-Cではlocal normalが安定し、未知directional derivativeを前向き予測。B20.6はinformative crossingが1件だけで **INCONCLUSIVE**。 | global smoothness、invariant manifold、universal separatrixは未確立。 | **局所response geometry成立／finite-distance evidenceは未完** |
| **B21** | response gradientの運動は局所kinematic transportで閉じるか | (Dg/dT=partial_Tg+H_Sdot P_B) と有限解像度で整合し、追加effective boundary-dynamical termを要求する再現可能残差は分離されない。 | 新しい運動方程式やcontinuum Hessian theoremではない。 | **局所kinematic closureを数値確認** |
| **B22** | 二次局所幾何で未知の未来境界を予測できるか | restricted Hessian、曲率、法線回転、主方向が検査尺度で安定し、一つのreserved branchで2段のheld-out forecastが凍結gateを通過。 | continuum curvature theorem、普遍的boundary law、T0-only長期予測ではない。 | **一分枝でprospective finite-resolution geometry成立** |
| **B23** | B22のshort-horizon constructionは別branchへ移るか | 有効評価できたbranch-transfer forecastは良好で、2つのfull-geometry sentinelも通過。ただし**当初aggregate planはINCONCLUSIVE**。endpoint近傍2対象で元の対称search-window ruleが実行不能だったため。 | Family-Cを越えたtransfer、完全独立endpoint-safe confirmationは未完。 | **cross-branch evidenceあり／元aggregateはinconclusive** |
| **B23A** | response/reconfiguration geometryをどこまで普遍化できるか | P1–P6は混合結果。P1は新B9族へのsmooth-normal transferを支持せず、P2BはB9内部branch-orientation patternを支持。P3はtopology-sensitiveなpiecewise/reset representationを支持。P4–P5は強いnon-topological reset/locality主張について **INCONCLUSIVE_NUMERICAL_SENSITIVITY**。P6はintegrity gate通過後に **NOT_SUPPORTED_RATE_ORDERED_LOCAL_RESPONSE_RECONFIGURATION**。 | 同一normal field、reset振幅、locality contrast、単調rate lawの広域transferは未確立。 | **構造的/形式的普遍性は保持／定量的普遍性は未確立** |
| **B24** | 既存BIG各sectorは最初から一つの実質的数学operatorを共有していたか | frozen source-audited mappingで、要求したcross-sector exact / coordinate-equivalent recurrenceは確立しなかった。 | programme-wide common operatorは未確立。 | **MULTIPLE_BOUNDARY_CLASSES_INDICATED** |
| **B25 Phase I** | 異なるboundary classをtyped transfer functionalで結べるか | constant-density bridgeはFAIL。その後retrospective coarea decompositionからlevel-resolved relationを作り、結果を見る前に凍結。新規9 shape/resolution caseで9/9 valid、median error 9.49%、max 17.76%。 | canonical p=4 settingに限定され、普遍bridgeではない。 | **AB_LEVEL_RESOLVED_BRIDGE_PASS** |
| **B25 Phase II** | Phase-I transferをtarget-side calibrationなしでどこまで単純化できるか | parallel-curve、nested-band、single-anchor fixed-coefficient reductionがheld-out ellipse family内でPASS。B25.1eは6 valid caseでmedian 4.65%、max 14.30%。 | 最初のtwo-center geometry/topology testは **IMPLEMENTATION_INVALID** でgeometry-family transferを確立しない。 | **family-restricted fixed-coefficient closureを支持** |
| **B26** | fixed perimeter coefficientはtopology-straddling two-center familyへ移るか | B26.1でN=384のrepresentative-level transitionを (4.175<delta_*<4.250) に独立localize。B26.2で6/6 valid、topology gate実現。しかしfixed coefficientはmedian error 42.91%、max 44.79%。 | topology changeだけが失敗原因とは言えず、connected側にも大きな誤差がある。 | **AB_TOPOLOGY_STRADDLING_FIXED_COEFFICIENT_TRANSFER_FAIL** |

---

## 2. B26・B23A後の証拠構造

現在のBIGは、一本道の「成功の積み上げ」として読むより、複数の接続された層として読む方が正確です。

```text
B3–B8
局所境界形成 / 着地 / 有限時間安定性

B9–B12
分離、捕獲、非同化的post-capture state

B13–B18
observation-like update、明示的history、readable history、boundary-dependent readout

B19–B23
finite-window channel構造とoperator-generated local response geometry

B23A
そのgeometry / reconfiguration languageがどこまでtransferできるかのprospective audit

B24–B26
別系統のcross-sector transfer programme:
multiple native boundary classes
    -> constructed level-resolved bridge
    -> family-restricted fixed coefficient
    -> new two-center familyでgeometry-transfer fail
```

これらは境界中心の共通言語で接続されていますが、**一つの普遍方程式、一つの定量的不変量から導出されたわけではありません。**

---

## 3. 現在もっとも強く保持できるprogramme-level命題

B3–B23時点では、「最終的に一つのmathematical universality classへ収束するか」は大きなopen questionでした。

B23AとB24–B26を経た現在、その問いはかなり絞られています。

現在もっとも安全に保持できる表現は、

> **Boundary Information Geometry は、系固有の境界幾何・応答・履歴・branch structure・reconfigurationを比較するための共通形式言語である。現時点の証拠は、programme全体に一つの普遍的定量境界則があることを確立していない。**

です。

次の強い表現は、現在の証拠からは支持できません。

```text
「全BIG sectorに同じoperatorがある」         — 未確立
「少数の同じscalarがどの系でもtransferする」 — 未確立
```

一方、「各seriesは互いに無関係」という結論でもありません。

- 局所構造は繰り返し現れる。
- family内でprospectiveに成功するpredictorが存在する。
- branch identityとreconfigurationが繰り返し重要になる。
- negative / inconclusive testが、定量transferの停止位置を実際に示している。

---

## 4. 普遍性の3段階

### 4.1 構造的普遍性

異なる系に、

```text
boundary
response
history
branch
reconfiguration
```

という抽象構造が現れ得る、というレベルです。

**現在の状態:** BIG全体を整理する構造的視点として有効。ただし「あらゆる系に必ずこの構造がある」という普遍定理ではない。

### 4.2 形式的普遍性

異なる系で、boundary field、response zero set、local gradient/normal、history/readout map、branch label、piecewise reconfigurationなどの比較可能な数学対象を定義できる、というレベルです。

**現在の状態:** programme-levelで最も強く保持できる統一的主張。

### 4.3 定量的普遍性

同じ数値係数、scalar threshold、normal field、reset振幅、locality contrast、rate lawなどが、異なる系・familyでも予測力を保つという強い主張です。

**現在の状態:** **未確立**。B19、B23A、B24、B26はいずれも、より強い定量transfer主張に対するprospective / frozen-protocolの限界を示しています。

---

## 5. 否定・限定・inconclusiveとして保持すべき結果

これらは「次の計算で救済すべき失敗」ではなく、BIGの証拠そのものとして残します。

- B19では、検査したray-independent upstream scalar collapseは得られない。
- B20.6は、frozen domain内でinformative crossingが1件しかなく **INCONCLUSIVE**。
- B23当初aggregate planは、endpoint近傍2stageが元のsymmetric-window ruleで実行不能なため **INCONCLUSIVE**。
- B23A P1は、新しいB9 familyへのunchanged smooth-normal transferを支持しない。
- B23A P4–P5は、frozen resolution gateによりnumerical inconclusive。
- B23A P6は、frozen monotonic rate-ordering hypothesisを支持しない。
- B24では、監査した全sectorに共通する既存の単一substantive operatorは見つからない。
- B25.1 constant-density transferはFAIL。
- B25.2はvalid transfer failではなくimplementation-invalid。
- B26は、凍結したaccuracy criterionの下で新しいtwo-center familyへのfixed-coefficient transferをvalidに否定する。

これらは理論の範囲を狭めています。post-hoc tuningで消すべき結果ではありません。

---

## 6. 現在、本当に開いている問い

B23時点より、open questionはかなり具体化しました。

### 数理・数値

- 座標やmodel familyを変えても残る transformation / covariance rule としてformal geometryを定式化できるか。
- 何がbranch-local invariantで、何がfamily-dependent coefficientで、何が単なる便利な座標なのか。
- finite-resolution transferの一部をcontrolled continuum statementへ持ち上げられるか。
- 独立設計した新しい系でも、同じformal objectがretuningなしにprospective predictionへ役立つか。
- B25のlevel-resolved transferを、B26で既に破れたuniversal fixed coefficientへ戻さずに、どこまで一般化できるか。

### 外部妥当性

BIGのどの縮約構造が、domain-specific equation、unit、calibration、既存理論との比較、empirical validationを課した後でも残るのか。

現時点では、BIGはこれを実証済みとは主張しません。

---

## 7. 現在の一文要約

> **BIGでは、縮約モデル内で再現可能な境界中心構造と、prospectiveに成功した局所・family-restricted transferが複数得られた。一方、その後の凍結検査は、それらからprogramme全体の単一定量境界則を導くことを支持せず、現在もっとも強い統一表現は「系固有の境界幾何を比較可能にする形式的・構造的枠組み」である。**

---

## 8. 推奨される読み順

最初にBIGの技術的状況を把握する場合は、

1. この統合research status map
2. [publication_map.md](publication_map.md)
3. [limitations.md](limitations.md)
4. 関心のある `papers/` 配下の各series
5. 対応するZenodo paper / reproducibility archive

の順を推奨します。

旧 [B3–B23研究状況マップ](research_status_map_B3_B23_ja.md) は、DOI 10.5281/zenodo.22939024 に対応する歴史的snapshotとして保存します。
