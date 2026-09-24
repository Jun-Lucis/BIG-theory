# BIG研究状況マップ — B3からB23まで

## 何が成立し、何がまだ仮説なのか

このページは、Boundary Information Geometry（BIG）のB3からB23までを、**証拠の強さと未解決点を分けて**整理した研究地図です。

ここで「成立」と書くとき、その意味は限定されています。すなわち、**明示した縮約モデル・パラメータ族・有限解像度・観測手順の範囲で、数理構造、数値パターン、または前向き検査が確認された**という意味です。普遍定理として証明された、あるいは現実の物理・生物・認知・技術系の定量法則として検証された、という意味ではありません。

基本的な区別は次です。

```text
モデル内で成立した結果
    != 普遍定理
    != 自然界の実証法則
```

---

## 1. 研究状況マップ

| 系列 | 主な問い | 現時点で成立しているもの | まだ未確立のもの | 状態 |
| --- | --- | --- | --- | --- |
| **B3–B4** | compact-like境界はどうゼロへ着地するか | 検査した退化混合勾配PDEでは、局所境界が \(\phi\sim As^\nu,\ \nu\approx2\) という二乗着地を頑健に示す。B4.3の \((\mu,\gamma)\) 格子では、指数はほぼ2のまま、層幅と振幅整合性が大きく変わる。 | より広いPDE族を含むuniversality class、厳密な連続体自由境界定理。 | **強い数値結果** |
| **B7–B8** | 局所境界のregularityとglobal runawayは分離できるか。形状は閾値を動かすか | 局所境界構造と有限時間の大域的運命は同一ではない。B8の楕円族では、survival/runawayの有限時間閾値が境界異方性と単調に変化し、絶対値は動くもののN=96からN=120の検証でも順序は保たれた。 | 真の漸近separatrix、普遍的異方性則、一般PDE定理。 | **数値的に支持** |
| **B9** | boundary costとnonlocal repulsionだけで分離型metastabilityは出るか | \(E=\sigma P+\lambda C\) の縮約エネルギーでcompact branch、有限deformation/pinch barrier、separated branchを構成できる。open-boundary auditと公開データ再集計も主要閾値構造を支持する。 | 定量的核分裂理論、shell/pairing/tunnelling/excitation/yieldなど。 | **縮約モデル内で成立** |
| **B10** | captureはfirst contactと同じか | first hitとsustained captureは分離する。sustained captureは中間noiseで現れ、高noiseではfirst-hit probabilityが高くても破壊される。 | 実際の核融合や外部系のstochastic resonanceとの定量対応。 | **強い数値結果** |
| **B11–B12** | capture後に非同化のまま残れるか | B11ではassimilationとtwo-parent hidden-depth inheritanceの競合を構成し、critical inheritance-coupling curveを得る。B12ではapproach、resonance lock、post-lock inheritanceを一つの縮約系に接続する。 | 生物遺伝、実在する融合、一般的個体性理論。 | **縮約力学として成立** |
| **B13–B15** | observation-like selection、trace、historyを共通言語で扱えるか | B13ではbasin selectionとself-observationのtoy dynamicsを構成。B14では明示的boundary-history fieldにwriting、retention、fusion compression、division partition、lineage persistenceを導入。B15ではobservation traceとboundary historyを共通のoperator-oriented representationで比較し、mapをlinear/affine/nonlinear/state-dependentへ分類できる。 | 量子測定、Born則、意識、生物遺伝の導出。 | **表現体系は成立／物理解釈は未確立** |
| **B16** | moving free boundaryは履歴を保持し再利用できるか | moving free boundaryへhistory fieldを結合し、retained historyがfeedbackを通じて後の局所応答を変えることをkept/erased controlで分離。shifted-stimulus testでも空間局所性を確認。 | 高次元自由境界の一般memory law、実在生物・材料への検証。 | **縮約PDEで成立** |
| **B17–B18** | 保存された履歴の何が実際に読まれるか | B17ではglobal history massより現在のmoving-boundary frameでlocally readableな履歴が応答をよく組織する。B18では別符号のfront modelへ拡張し、path-integrated interface/core-gated readoutがread-start local loadより有効な整理変数となる。 | 普遍的memory/readout law、domain-independent operator。 | **readout原理を数値的に支持** |
| **B19** | 増大・減衰は単一upstream thresholdで整理できるか | 仮定したshrinking-core modelでは \(s_*=5/4\)。動力学側では21 single observablesと8個の事前指定two-coordinate portraitsでray-independent collapseが得られず、direction-dependent channel familyとlocal separatrixの記述がより適切。下流ではtotal production-versus-dissipation balanceに組織化される。 | Navier–Stokesの普遍指数、global separatrix、blow-up/regularity criterion。 | **重要な否定結果＋構造結果** |
| **B20** | finite-window response zero setを作用素生成境界として扱えるか | \(\mathcal B_T=\{P:F_T(P)=0\}\) の到達可能性はdirection-dependent。frozen normalized 4D Family-C subspaceではlocal normalが二差分尺度で安定し、未知のdirectional derivativeを前向きに予測。B20.6はinformative crossingが1件のみなので **INCONCLUSIVE**。 | global smoothness、invariant manifold、単一universal separatrix。 | **局所response geometryは成立／finite-distance一般化は未完** |
| **B21** | response gradientの運動は通常の局所輸送で閉じるか | \(Dg/dT=\partial_Tg+H_S\dot P_B\) 自体はchain ruleであり新法則ではない。各項を独立測定すると、最終前向きclosure residualは有限root bracketが与える一次不確かさより小さく、追加のeffective boundary-dynamical termを必要とする再現可能残差は分離されなかった。 | 新しい運動方程式、continuum Hessian theorem、full-space closure。 | **局所kinematic closureを数値確認** |
| **B22** | 二次幾何まで未知の未来境界を予測できるか | restricted Hessian、shape operator、principal curvature/direction、normal rotationを二つの差分尺度で安定測定。一つのreserved branchで二段のheld-out short-time forecastを行い、root、normal、Hessian、resolved principal modesの全gateを通過。 | continuum curvature theorem、普遍的boundary-motion law、T0だけからの長期forecast。 | **一分枝でprospective finite-resolution geometry成立** |
| **B23** | B22のshort-horizon constructionは別分枝へ移るか | 4分枝・3ray方向で、実際に有効評価できたposition/normal forecastはすべて基準を通過。二つのfull-geometry sentinelもHessian、主曲率、主方向のgateを通過。当初aggregate planは、endpoint近傍の二対象で対称search-window protocolが実行不能だったため **INCONCLUSIVE** のまま。補足修正版・訂正runは元計画の成功へ遡及加算していない。 | Family-Cを越えた移植、完全に独立したendpoint-safe confirmation、空間・時間解像度のcontinuum convergence。 | **cross-branch evidenceあり／一般化は未完** |

---

## 2. 現在のBIGの「硬い核」

現時点で最も強く言える共通命題は、「境界＝個」が自然法則として証明された、ということではありません。

より限定した形なら、次が支持されています。

> **境界を、動的場、幾何コスト、履歴を持つinterface、readout構造、あるいは作用素生成response zero setとして明示的にモデル化すると、BIGの縮約モデルでは再現可能な局所構造が繰り返し現れ、後半系列ではそれを測定し前向きに検査できる。**

研究系列は大きく四層に整理できます。

```text
B3–B8
境界形成、着地、local/global stability、anisotropy

B9–B12
separation、capture、non-assimilative post-capture state

B13–B18
observation-like update、explicit history、memory-bearing boundary、readout

B19–B23
boundary-core channel、operator-generated response geometry、
local kinematics、curvature、prospective / cross-branch prediction
```

これらは一つの境界中心言語でつながっていますが、**まだ一つの統一定理から導出された同一構造ではありません**。

---

## 3. 本当にまだ仮説であるもの

B23後の中心的な数学的未解決問題は、次です。

> **B3–B23に繰り返し現れた構造は、一つの共通した数学的universality classの異なる表現なのか。それとも、互いに関連はあるが別々の有用な縮約モデル群にすぎないのか。**

特に、次の対象を一つの共通formal coreから導けるかは未解決です。

- B3–B4のquadratic-like boundary landing
- B7–B8のanisotropy-controlled finite-time threshold
- B9のboundary-cost / nonlocal-repulsion competition
- B14–B18のhistory field / readout operator
- B19のdirection-dependent channel family
- B20–B23のoperator-generated response zero setと局所幾何

もう一つの未解決問題は外部妥当性です。

> **これらの縮約構造のどれが、domain-specific equation、単位、parameter calibration、empirical validationを導入した後にも残るのか。**

現時点のBIGは、そこまで成立したとは主張していません。

---

## 4. 一文での現状

> **BIGは、複数の縮約数理・数値モデルにおいて再現可能な境界中心の構造を構成してきた。未解決なのは、それらが共通の数学的普遍構造に属するのか、また実在系の定量記述へ持ち出しても成立するのかである。**

---

## 5. なぜB23が自然な区切りなのか

B23まででresponse-geometry系列が一つの弧を完成させています。

```text
B20  response boundary
  -> B21 local kinematic transport
  -> B22 Hessian / curvature / normal rotation
  -> B23 cross-branch short-horizon transfer
```

したがって、ここから先は大きく二方向に分けられます。

1. **confirmation / hardening** — 新しいheld-out family、endpoint-safe protocol、空間・時間収束、独立再現。
2. **unification / abstraction** — これまでのboundary、history、readout、response geometryを結ぶ最小共通数理を抽出する。

前者は証拠の強度を上げる方向です。  
後者は、BIGが「関連する縮約モデルの系列」を越えて共通数理核を持つのかを問う方向です。

---

## 6. 読み方

このページは研究状況の地図であり、各論文やreproducibility archiveの代わりではありません。

個別の数値主張については対応するpaper folderとZenodo recordを参照してください。  
programme-wideな限界は [limitations.md](limitations.md) を参照してください。  
公開物の一覧は [publication_map.md](publication_map.md) を参照してください。
