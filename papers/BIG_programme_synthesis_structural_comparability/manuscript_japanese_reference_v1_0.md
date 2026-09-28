# 境界情報幾何学における定量的普遍性検査から構造的比較可能性へ

## BIG-B19 から BIG-B26 までのプログラム統合

**Jun Lucis**  
独立研究者  
Boundary Information Geometry (BIG)  
**参考日本語訳 v1.0 - 2026年9月27日**  
**英語学術版を正文とする**  
**Zenodo 予約 DOI:** 10.5281/zenodo.23006170

---

## 要旨

Boundary Information Geometry（BIG／境界情報幾何学）は、境界を能動的な力学的・幾何学的・履歴的・応答生成的構造として扱う、一連の縮約数理モデルおよび数値モデルを通じて発展してきた。初期段階では、コンパクトに近い境界の着地、有限時間異方性閾値、分離様の準安定性、履歴を担う界面、境界依存のreadoutなど、繰り返し現れる局所現象に重点を置いた。後期プログラムでは、これらの反復構造を少数の移植可能な定量則へ圧縮できるか、というより強い問いを検査した。

本稿は、B19E の外部検証分枝および B23A の構造的普遍性監査を含む、後期 B19-B26 プログラムの証拠を統合する。B19 は、検査された合成渦度familyにおいて、ray に依存しない頑健な上流scalar collapseを与えなかった。B19E はその後、強い標準baselineに対し、凍結されたBIG追加特徴が一次外部holdoutで前向きな追加予測情報を与えることを確立できなかった。結果は ΔR² = -0.00284577、階層bootstrap 95%区間 [-0.01016985, 0.00421586] であり、正式判定は `NULL_OR_INCONCLUSIVE` と保持された。別個の厳密local-budget監査では、有限control-volumeの解像済みbookkeepingがほぼ機械精度で閉じたが、これは予測結果を救済しなかった。B20-B22 はそれでも、制限された凍結branchおよび部分空間内で、有用な有限解像度局所応答幾何を確立した。B23 は短時間branch-levelで好ましい証拠を得た一方、元のaggregate判定は INCONCLUSIVE のまま保持した。B23A はさらに、再構成設定をまたぐより強い移植主張を検査し、構造的・形式的比較可能性は定量移植より広く残る、という限定的結論で閉じた。

別系統の B24-B26 プログラムも、別の方向から同じ区別に到達した。B24 は、既に存在する一つの共通operatorではなく、複数のnative boundary classを示した。B25 はその後、前向きに成功するfamily限定のtransfer relationを新たに構成し、検査されたellipse family内では固定周長係数まで圧縮した。B26 はさらに、有効なtopology-straddling two-center testを実現し、同じ固定係数が前向きに失敗することを示した。相対誤差中央値は42.91%、最大値は44.79%であった。

全体の記録が支持する解釈は意図的に限定される。現時点のBIGは、一つの普遍的な定量境界則というより、**系固有の境界幾何、応答、履歴、分枝構造、再構成を比較するための共通形式言語**として記述する方が証拠に適合する。negative、inconclusive、implementation-invalid、transfer-failure の各結果は、後から修理すべき失敗ではなく、主張境界を定める証拠として扱う。

**キーワード:** Boundary Information Geometry; response boundary; free boundary; structural universality; prospective numerical test; branch geometry; transfer limit; predeclaration; model falsification; reproducibility

---

## 1. 範囲と目的

Boundary Information Geometry は、境界は必ずしも受動的な縁ではない、という整理原理から始まった。縮約モデルでは、境界は力学的界面、幾何学的コスト、保持履歴の担体、readout構造、branch identifier、あるいは有限時間発展と観測によって生成されるzero setとして働きうる。

初期B-seriesは、この見方が異なるmodel familyにおいて再現可能な数理構造を生むことを示した。例として、ほぼ二乗的なcompact-like boundary landing、有限時間異方性依存、境界コストと非局所反発が作る分離様エネルギー地形、履歴を保持し再利用するmoving free boundary、測定可能な局所幾何をもつfinite-window response boundaryがある。

これらの結果は、より強い問いを生んだ。

> 反復して現れる構造は、一つの移植可能な定量則の表れなのか。それとも、共通形式言語で記述できる系固有の幾何として理解すべきなのか。

後期プログラムでは、凍結protocol、held-out test、明示的stop rule、source audit、数値validity gate、negativeまたはinconclusiveな結果の保持を、次第に強く採用した。本統合稿の目的は、局所的な成功をprogramme-wideな主張へ格上げせず、この証拠系列を整理することにある。

中心結論は次である。

> **異なる系は異なる境界幾何を持ちうるが、それでも共通の形式的構造を通して比較可能である。**

本稿は各B-series論文を置き換えるものではない。数値値と正式判定は、それぞれ対応する保存済み記録に従う。

---

## 2. 普遍性の三つの意味

### 2.1 構造的普遍性

構造的普遍性とは、**boundary、response、history、branch、reconfiguration** といった語で表現される構成上の反復を指す。すべての系で同じ係数、同じ方程式、同じ局所幾何を要求しない。

### 2.2 形式的普遍性

形式的普遍性とは、異なる系を比較可能な数学的対象で表現できることを意味する。たとえば、boundary field、response zero set、local normal、Hessian、history/readout map、branch label、piecewise reconfiguration mapなどである。

A canonical later example is

$$
F_T(P)=Z[U_T(P)]-Z[P],
\qquad
\mathcal B_T=\{P:F_T(P)=0\}.
$$

同じ形式対象を用いることは、異なる系で数値的に同じ幾何が現れることを意味しない。

### 2.3 定量的普遍性

定量的普遍性は、より強い主張である。一つの低次元数値対象、たとえばscalar threshold、normal field、reset amplitude、critical rate、fixed coefficientなどが広範囲に移植されることを要求する。

B19-B26プログラムは、このレベルを前向きに検査する比重を高めていった。結果は非対称である。形式的比較可能性は有用なまま残る一方、最も強い定量移植主張は、null、inconclusive、invalid、negativeという結果によって繰り返し境界づけられた。

---

## 3. B3-B18 からの背景

この節の目的は各論文を再レビューすることではなく、後期検査を動機づけた反復モチーフを示すことである。

### 3.1 境界形成と局所着地

検査されたdegenerate mixed-gradient PDE familyでは、compactまたはcompact-like profileが、指定された有限解像度の範囲で、反復してほぼ二乗的な局所着地を示した。

$$
\phi(s)\sim A s^\nu,\qquad \nu\approx2.
$$

### 3.2 形状依存の有限時間運命

B7-B8系列は、局所境界正則性と大域的有限時間運命を分離した。検査されたellipse familyでは、局所境界構造を失わないまま、異方性が有限時間survival/runaway thresholdを移動させた。

### 3.3 境界エネルギーと再構成

B9 は縮約幾何エネルギー

$$
E(\Omega;\lambda)=\sigma P(\Omega)+\lambda C(\Omega)
$$

を導入した。ここでは境界コストが非局所反発項と競合する。モデルはcompact branch、有限の変形・pinch barrier、separated branchを生成する。これはfission-like metastabilityの縮約構造類似であり、定量的な核分裂計算ではない。

### 3.4 履歴を担う境界とreadout

B14-B18 は、保存されたhistoryと、現在の状態から動的にreadableなhistoryを段階的に分離した。後期readout構成では、履歴の効果がglobal stored massだけでなく、現在のinterface position、path exposure、local accessibilityに依存しうることを強調した。

これらは反復する語彙を与えたが、一つの共通定量則が全sectorを支配することを確立したわけではない。

---

## 4. B19 と B19E: 低次元scalar reductionの限界

### 4.1 B19: 方向依存channel family

B19 は合成divergence-free vorticity fieldへ進み、有限時間の増幅・減衰を一つの頑健な上流scalar thresholdへ圧縮できるかを検査した。プログラムはboundary-core concentration measure、Biot-Savart strain、signed strain alignment、high-vorticity gate、短時間粘性力学、robustness controlを組み合わせた。

数値記録は、検査されたcontinuation directionを横断する、一つの頑健なray-independent upstream scalar collapseを支持しなかった。代わりに、異なるdirection-dependent upstream channel familyが、共通する下流のproduction-versus-dissipation organizationへ流入する、と記述する方がデータに合った。

保持された解釈は、negativeであると同時にstructuralである。

> **B19 は一つの頑健な上流scalar lawを同定しないが、再現可能な有限familyのchannel organizationを同定する。**

### 4.2 B19E: 前向き外部holdout

B19E は、凍結されたBIG型boundary/core追加特徴が、独立生成されたflow settingにおいて、強い標準local-flow baselineを超える追加予測情報を与えるかを検査した。

最終外部系には、独立に保守されているTIDE solverを用いた。未閲覧の一次holdoutはseed 4, 5、合計1,536行であった。凍結modelは同じridge regularizationを用いた。一次結果は

$$
R^2(M_2)=0.3285226325,
$$

$$
R^2(M_{\mathrm{full}})=0.3256768635,
$$

したがって

$$
\Delta R^2=-0.0028457690.
$$

階層bootstrap 95%区間は

$$
[-0.0101698477,\;0.0042158635]
$$

であった。

保持された正式判定は

**`NULL_OR_INCONCLUSIVE`**

である。

point estimateはわずかに負だが、区間は0を跨ぐ。したがってB19Eは、凍結追加特徴が追加予測情報を与えることを確立しない。同時に、あらゆるboundary/core情報が無関係であるという、より強い否定定理も正当化しない。

### 4.3 B19E: 厳密finite-control-volume budget

別個に凍結したStage-B監査は、新しいseed 6, 7を用い、4,608個のfinite-control-volume行を評価した。解像済みlocal enstrophy budgetは

$$
\dot Z_\Omega=P-D+A+V_b+F+C_{\mathrm{filt}}
$$

である。

relative closure errorの中央値は約4.87×10⁻¹⁷、最大値は約8.44×10⁻¹⁶であり、`BUDGET_CLOSURE_PASS` となった。

しかし一次16η control-volume scaleでは、歴史的proxy

$$
B_{\mathrm{proxy}}=P-D
$$

は依然として弱かった。sign agreementは0.5625、proxy relative error中央値は0.85155、解像済みlocal rateとのSpearman相関は0.15894であった。省略補正はadvective transportが支配的だった。

したがって、

> **厳密なlocal budget closureは、低次元予測十分性と同値ではない。**

B19E v1.0 は DOI 10.5281/zenodo.22996961 で正式公開されている。

---

## 5. B20-B22: 局所応答幾何はなお予測的でありうる

一つのglobal scalar collapseが存在しないことは、有用な幾何の存在を否定しない。B20 は対象をupstream scalar thresholdから、operator-generated finite-window response zero setへ変更した。

### 5.1 B20: response boundary と local normal

B20 は

$$
F_T(P)=Z[U_T(P)]-Z[P],
\qquad
\mathcal B_T=\{P:F_T(P)=0\}
$$

を用いた。

B20.5 は事前宣言されたnormalized four-dimensional Family-C subspace内でlocal response gradientを再構成した。一次held-out directional derivativeの符号は24/24比較で一致し、cross-scale normal差も非常に小さかった。

B20.6 は次に、前向きfinite-distance crossing predictionを試みた。6本の独立凍結trajectoryのうち、事前宣言domain内で情報を持つcrossingが得られたのは1本だけだった。そのorientationは正しく予測され、凍結linear location estimateと精密化midpointとの差は約1.66%だった。しかし、事前宣言criterionが複数のinformative crossingを要求していたため、正式statusは **INCONCLUSIVE** のまま保持された。

### 5.2 B21: 局所運動学的閉包

B21 は、解像されたFamily-C r10 response-boundary branchに沿って、局所transport identity

$$
\frac{Dg}{dT}=\partial_T g+H_S\dot P_B
$$

を検査した。

前向きに凍結したE12 testでは、closure residualは0.1242154%であり、root bracket由来の一次不確かさ上限0.2174844%を下回った。prediction-observation angleは0.0698935度だった。追加の有効boundary-dynamical termを必要とする再現可能なresidualは分離されなかった。

これは有限解像度の数値closure resultであり、新しい運動方程式の発見ではない。

### 5.3 B22: 二次の前向き幾何

B22 は局所構成をHessian、tangent-space shape operator、principal curvatureとdirection、temporal normal rotationへ拡張した。予約されたlower-epsilon r09 branch上で、二段階のsequential held-out short-horizon testが凍結gateを通過した。

第2段階では、root予測0.150632に対し観測midpointは0.159421、future-normal angle errorは約0.3744度、Hessian relative errorは約0.00859、3本すべてのresolved principal-direction errorは0.379度未満だった。

要点は次である。

> **programme-wide scalar lawがなくても、局所有限解像度幾何は前向きに有用でありうる。**

---

## 6. B23: 後知恵で格上げしないbranch-level transfer

B23 は、B22のshort-horizon response-boundary constructionが、同じnormalized Family-C subspace内の事前宣言済み未使用branchへ移植できるかを検査した。

primary scaleでは、有効に評価できた4本のfirst-stage recordにおいて、root-midpoint errorは約0.000336から0.001358、normal-angle errorは約0.0248度から0.5671度であった。後続のfull-geometry sentinel testでも、有限解像度Hessianおよびprincipal mode errorは小さかった。

しかし、endpointに近い2 targetでは、対称prediction-centered search-window protocolが実行不能であり、元のaggregate planを厳密に実行できなかった。補助的なrepaired/corrected runは補助証拠として保持したが、元の凍結planの成功として事後的に数えなかった。

したがって元のaggregate verdictは **INCONCLUSIVE** のままである。

この凍結protocol保持原則は、後続のuniversality auditで重要になる。

---

## 7. B23A: 構造的普遍性と検査された限界

B23A は構造的・形式的普遍性と定量的普遍性を明示的に分離し、frozen anti-rescue ruleの下でP1-P6 branchを閉じた。

P1は、新しいB9 reconfiguration familyへのunchanged smooth-normal transferを支持しなかった。P2Bは、より弱いB9内部のconnected-versus-separated branch orientation patternを保持した。P3は、凍結されたthreshold-support geometry vectorに対するtopology-sensitive piecewise/reset representationを前向きに支持したが、outer-boundary-onlyのpost-hoc auditは未解決のままだった。P4とP5は、より強いnon-topological reset/locality claimについて数値的にinconclusiveとなった。P6はさらに、P5後に生じたrate-ordering hypothesisを前向きに検査し、numerical integrity gateが通過した状態で、凍結joint criteriaを満たさなかった。

B23Aの終端結論は次である。

> **Boundary Information Geometry は、普遍的な定量境界則というより、系固有の境界幾何に対する普遍的形式として、より強く支持される。**

B23A branchは DOI 10.5281/zenodo.22994445 のP6で正式に閉じている。

---

## 8. B24-B26: 複数boundary classから、境界づけられたtransfer relationへ

### 8.1 B24: 複数のnative boundary class

B24は、以前のBIG sectorが、既に一つの実質的でoperation-preservingな数学的coreを共有しているかを検査した。generic boundary notationやgeneric chain-rule/coarea identityはBIG固有法則として数えなかった。source-audited frozen mappingは、必要とされたexactまたはcoordinate-equivalent recurrenceを支持しなかった。

保持された判定は

**`MULTIPLE_BOUNDARY_CLASSES_INDICATED`**

である。

これは以前の結果を無効化しない。それらが最初から一つのcommon native operatorのmanifestationだった、という仮説を制限する。

### 8.2 B25 Phase I: 単純bridgeの失敗とlevel-resolved bridgeの成功

最初のconstant-density A-to-B bridge

$$
J_{\mathrm{pred}}=\sigma_{1D}P_{\mathrm{rep}}
$$

は凍結quantitative gateを通過しなかった。`AB_CONSTANT_DENSITY_FAIL` はそのまま保持された。

その後、保存済みprofileのみを使うretrospective coarea decompositionから代替predictorを構成し、新しい2D trajectoryの前に凍結した。

$$
J_{\mathrm{LR,pred}}
=\kappa_p\phi_{\max}^{(2D)}
\int P(r)g_{1D}(r)^{p-1}\,dr.
$$

新しいheld-out shape/resolution 9 caseでは、9/9がvalidだった。最大relative errorは17.76%、medianは9.49%、旧comparatorに対するmedian error改善率は68.15%だった。正式判定は `AB_LEVEL_RESOLVED_BRIDGE_PASS` である。

### 8.3 B25 Phase II: family限定の固定係数

transfer relationはさらに前向きに縮約された。事前宣言されたcircular calibration stateから

$$
\sigma_{\mathrm{cal}}=9.434181431178162\times10^{-8}
$$

を固定し、held-out ellipse predictionでは

$$
J_{\mathrm{pred}}=\sigma_{\mathrm{cal}}P_{\mathrm{rep}}
$$

のみを用いた。

有効なheld-out ellipse 6 caseで、relative error中央値は4.65%、最大値は14.30%だった。したがってfixed-coefficient closureは、**検査されたellipse family内では**前向きに機能した。

後続B25.2のtwo-center geometry-transfer attemptはformal transfer failureではなく `IMPLEMENTATION_INVALID` である。凍結されたvalidity条件とconnected/disconnected topology-span条件が同時に実現しなかったためである。

### 8.4 B26: 有効に実行されたgeometry-transfer failure

B26は係数をそのまま保持し、意図したtransfer testを実行可能にするためのgeometryだけを変更した。B26.1はtopology-only adaptive refinementを用い、N=384におけるrepresentative-level transitionを

$$
4.175<\delta_*<4.250
$$

へ局在化した。

B26.2はその後、新しい3 separationを凍結し、N=384と448で新しい6 caseを評価した。すべてnumerical validity gateを通過し、fine-resolution topology gateはrepresentative contour count 1, 1, 2として実現した。

同じfixed coefficientの結果は、

- relative error中央値: **42.91%**
- relative error最大値: **44.79%**
- amplitude-aware comparator error中央値: **27.29%**

であった。

終端正式判定は

**`AB_TOPOLOGY_STRADDLING_FIXED_COEFFICIENT_TRANSFER_FAIL`**

である。

B26は、検査されたfixed-coefficient closureの有限解像度 **geometry-transfer boundary** を同定する。ただし、connected sideですでに大きなerrorがあるため、topology changeそれ自体が失敗の唯一原因であることを確立しない。

---

## 9. 証拠マップ

| Stage | 問い | 保持されたstatus | programme-levelでの意味 |
|---|---|---|---|
| B19 | 一つの頑健なupstream scalar classifierか | ray-independent collapseとしては未支持 | direction-dependent channel familyは有用 |
| B19E A1 | 凍結BIG追加特徴は外部で追加予測情報を与えるか | `NULL_OR_INCONCLUSIVE` | baselineを超える前向きincremental gainは未確立 |
| B19E B | 解像済みlocal finite-volume budgetは閉じるか | `BUDGET_CLOSURE_PASS` | 厳密bookkeepingは予測十分性を意味しない |
| B20.6 | 複数の独立prospective finite-distance crossingか | `INCONCLUSIVE` | 1本のinformative crossingは支持的だが不十分 |
| B21 | 測定されたkinematicsでlocal gradient motionが閉じるか | tested resolutionで支持 | 追加effective termは分離されず |
| B22 | sequential held-out local geometry forecastか | 予約branchで凍結gate通過 | local second-order geometryは予測的になりうる |
| B23 | 元のaggregate plan下でcross-branch short-horizon transferか | `INCONCLUSIVE` | 好ましいbranch evidenceはあるが元planは格上げしない |
| B23A | reconfiguration settingをまたぐ一つのquantitative lawか | mixed; strongest claimsは未支持/inconclusive | structural/formal comparabilityの方が広く残る |
| B24 | sector間に既存の一つのsubstantive common operatorがあるか | `MULTIPLE_BOUNDARY_CLASSES_INDICATED` | native operator/classは区別される |
| B25 Phase I | 新しいtyped transfer relationを構成できるか | `AB_LEVEL_RESOLVED_BRIDGE_PASS` | 前向きtransferはfamily限定かつ明示的に構成可能 |
| B25 Phase II | ellipse family内で一つのfixed coefficientまで圧縮できるか | `AB_FIXED_COEFFICIENT_PERIMETER_PASS` | fixed coefficientはtested family内で機能 |
| B25.2 | 最初のtwo-center testへ同じfixed coefficientを移植できるか | `IMPLEMENTATION_INVALID` | 宣言通りのtestが実行不能 |
| B26 | topology-spanning testを実現した後もfixed coefficientは移植されるか | `AB_TOPOLOGY_STRADDLING_FIXED_COEFFICIENT_TRANSFER_FAIL` | geometry-transfer boundaryを同定 |

---

## 10. 統合解釈

### 10.1 局所予測可能性は大域的普遍性ではない

B20-B22は、local response boundaryが数値的に安定し、前向きに有用なgeometryを持ちうることを示す。B23は、この構成の一部がbranch間で移植されることを示す。一方B23Aは、それがreconfiguration familyを横断して、一つのunchanged smooth-normal field、reset amplitude、locality contrast、rate lawを意味しないことを示す。

### 10.2 family限定の係数は普遍係数ではない

B25.1eはheld-out ellipse family内部でpositiveなprospective fixed-coefficient resultである。B26は新しいtwo-center familyにおいて、同じ係数がvalid prospective testで失敗することを示す。両者は矛盾しない。合わせて、成立domainを局在化している。

### 10.3 厳密closureは予測十分性ではない

B19Eでは、解像済みlocal budgetがほぼ機械精度で閉じる一方、単純なproduction-minus-dissipation proxyは弱く、凍結primary external predictive incrementはnull/inconclusiveのままである。したがって、正しいidentityはmechanism理解に有用でも、十分なlow-dimensional predictorとは限らない。

### 10.4 branch identity と reconfiguration は明示的でなければならない

B9、B20-B23A、B26を通じ、branch identityは繰り返し重要になる。全regimeを一枚のglobally smooth low-dimensional surfaceで覆うより、piecewise local geometryの方が証拠と整合する。

### 10.5 自然な普遍対象は数値ではなく変換則かもしれない

現在のprogramme-levelで最も強く残る問いは、「一つの係数がどこでも同じか」ではない。system-specific boundary geometryの間に、共通のtransformation、covariance、composition、normal-form ruleが存在するか、である。

したがって普遍性探索は、

> どこでも同じscalar

から

> 系固有の幾何どうしを結ぶ同じ関係

へ移る。

初期の普遍性仮説が狭まったことは、単なる射程の喪失を意味しない。前向き検査を重ねることで、広い可能性は、「何が移植され、何がfamily固有で、どこで移植が破れるか」という、より解像された地図へ置き換えられた。その意味で、BIGは主張範囲を狭める一方、証拠内容をより具体化し、検査可能性を高めた。したがって普遍性の可能性は消えたのではなく、再定式化された。もしより深い共通則が存在するなら、それは一つのshared scalar lawではなく、異なるboundary geometry間の関係、変換、共変則、あるいはbranch-transition structureに宿る可能性がある。

---

## 11. 主張境界

本統合稿は、以下を確立しない。

- 一つの普遍的BIG方程式
- 一つの普遍的boundary scalar、normal field、reset amplitude、rate law、coefficient
- global invariant manifold
- continuum free-boundary、curvature、Hessian-existence theorem
- Navier-Stokes blow-up、regularity、singularity criterion
- 定量的な核分裂または核融合理論
- 生物学、認知、AI、宇宙論における妥当性
- programme-wideな外部実証validation

**structural universality** という語は、反復して現れるorganizationに対する作業上の記述としてのみ用いる。すべての系が同じboundary structureを持つという定理ではない。

より強く保持されるprogramme-level formulationは、

> **system-dependent boundary geometryのためのcommon formal language**

である。

---

## 12. 未解決問題と新しいB-seriesへの引き継ぎ

閉じたB19-B26プログラムは、以下の問いを残す。ただし、これらは保存済み判定を書き換える延長ではなく、新たに独立凍結された研究としてのみ扱う。

1. **Transformation and covariance laws.** boundary-response objectは、明示的なcoordinate、scale、topology、representation changeの下で関係づけられるか。
2. **Branch-local invariants.** cross-branch quantitative transferが失敗しても、同じbranch内で安定する量は何か。
3. **Piecewise normal forms.** reconfiguration eventを、少数のlocal geometric pieceとtransition mapからなる文法として表現できるか。
4. **Continuum control.** 有限解像度結果のうち、controlled continuum limitを持つものと、本質的にnumerical observableであるものを区別できるか。
5. **External validation.** domain-specific equation、unit、calibration、強い既存baselineとの比較を経ても残るstructural/formal BIG objectは何か。

これらに答える新プログラムは、新しいB-series identifierとfresh predeclarationを持つべきである。本稿で要約した正式判定を変更してはならない。

---

## 13. 結論

B19-B26系列は、Boundary Information Geometryの解釈を変えた。証拠は、一つの普遍scalar lawへ一直線に進む構図を支持しない。代わりに、次の層構造を示す。

- 局所的に再現可能なgeometry
- 前向きに有用なfamily限定reduction
- 明示的なbranch / reconfiguration dependence
- 前向きに同定されたtransfer limit

この像はより限定的だが、より検査可能である。

> **同じgeometryがどこにでも現れる必要はない。系固有のgeometryを表現・比較・変換するための同じ規則の方が、より妥当な普遍対象かもしれない。**

この意味で、現在のBIGは、一つの普遍的定量境界則の理論というより、**difference-preserving comparability（差異を保った比較可能性）**の形式として、より強く支持される。

したがってB19-B26プログラムは、B19EおよびB23A audit branchを含め、本稿に記録されたevidential levelで閉じる。新しい研究はこれを基礎にできるが、閉じた記録を事後修理するのではなく、新しいseriesとして開始する。

---

## データ・コード・公開系譜

個別のclaim-bearing stageは、それぞれのZenodo recordに保存され、BIG GitHub repositoryからリンクされている。本統合で主要に用いたrecordは以下である。

1. **B19 integrated study:** https://doi.org/10.5281/zenodo.22726848
2. **B19 finite-time response follow-up:** https://doi.org/10.5281/zenodo.22769513
3. **B19E external validation and local-budget audit:** https://doi.org/10.5281/zenodo.22996961
4. **B20 operator-generated response boundaries:** https://doi.org/10.5281/zenodo.22846729
5. **B21 local kinematic closure:** https://doi.org/10.5281/zenodo.22876813
6. **B22 prospective local geometry:** https://doi.org/10.5281/zenodo.22893912
7. **B23 cross-branch geometric prediction:** https://doi.org/10.5281/zenodo.22936794
8. **B23A structural universality and limits:** https://doi.org/10.5281/zenodo.22994445
9. **B24-B25 Phase I:** https://doi.org/10.5281/zenodo.22956894
10. **B25 Phase II:** https://doi.org/10.5281/zenodo.22967474
11. **B26 topology-realized fixed-coefficient transfer:** https://doi.org/10.5281/zenodo.22972985

Repository: https://github.com/Jun-Lucis/BIG-theory

本統合稿は新しい数値実験を導入しない。上記保存記録のevidential integrationである。

---

## 本版の推奨引用

Jun Lucis. *From Quantitative Universality Tests to Structural Comparability in Boundary Information Geometry: Programme Synthesis from BIG-B19 to BIG-B26.* Preprint v1.0, 2026. Zenodo DOI: 10.5281/zenodo.23006170.

**注:** 本日本語版は英語学術版を読むための参考翻訳である。引用・version control・数値値・正式判定・主張境界については英語版を正文とする。
