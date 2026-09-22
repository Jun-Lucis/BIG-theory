# BIG Terminology

This document summarizes key terms used in **Boundary Information Geometry (BIG)**.

The purpose of this file is not to impose final definitions, but to clarify how important terms are used within the current BIG research programme.

BIG is a developing boundary-centered framework. Many terms below should be read as terms for reduced mathematical and numerical models, not as completed physical theories.

---

## Boundary

In BIG, a **boundary** is not merely an outer contour or geometric edge.

A boundary is treated as an active structure that can:

* separate a system from its environment,
* preserve individuality,
* mediate interaction,
* resist complete assimilation,
* deform under stress,
* fail or reconnect,
* and carry memory-like structure across transformation.

In this sense, a boundary is both geometric and informational.

---

## Non-assimilation

**Non-assimilation** refers to the preservation of distinction during interaction.

A non-assimilative boundary allows contact, resonance, exchange, or transformation without collapsing all participating structures into a single undifferentiated state.

A short BIG formulation is:

> Interaction without total assimilation.

Non-assimilation does not mean isolation.
It means that interaction occurs while some boundary-supported individuality remains.

---

## Individuality

In BIG, **individuality** is not assumed to be a fixed substance inside a system.

Instead, individuality is understood as a boundary-supported structure:

* something is distinguishable,
* it maintains internal coherence,
* it resists complete assimilation,
* and it can interact across its boundary.

This is why BIG treats boundary dynamics as central to the emergence and persistence of individual systems.

---

## Boundary layer

A **boundary layer** is a finite-width transition region near the edge of a field-supported structure.

In several BIG numerical models, the boundary layer does not behave like a simple exponential tail. Instead, it can show compact-support-like behavior and quadratic landing.

A typical local form is:

$$
\phi(s) \sim A s^\nu,\qquad \nu \approx 2
$$

where (s) is the distance from the boundary.

---

## Quadratic landing

**Quadratic landing** refers to a boundary profile where the field approaches zero approximately as a second-order power of the distance to the boundary.

In simplified notation:

$$
\phi(s) \sim A s^2
$$

or more generally:

$$
\phi(s) \sim A s^\nu,\qquad \nu \approx 2.
$$

In BIG, this is interpreted as a recurring local boundary motif in certain reduced PDE models.

---

## Quartic-gradient stiffness

A **quartic-gradient stiffness** term is a nonlinear gradient contribution of the form:

$$
|\nabla \phi|^4.
$$

In BIG, this term is interpreted as a mathematical expression of boundary stiffness or non-assimilative tension.

It penalizes sharp gradient structures differently from the ordinary quadratic gradient term:

$$
|\nabla \phi|^2.
$$

This quartic-gradient contribution is one of the recurring mathematical motifs in BIG boundary models.

---

## Compacton-like boundary

A **compacton-like boundary** refers to a field configuration whose support appears finite or effectively finite.

Instead of decaying smoothly to infinity with a long tail, the field approaches zero at a boundary in a compact-support-like manner.

In the current BIG context, this is a model-level numerical and structural feature, not a claim that all physical boundaries are compactons.

---

## Finite-time separatrix

A **finite-time separatrix** is a threshold that separates different outcomes over a specified observation time.

For example, in some BIG models, a system may show:

* survival-like behavior below a certain amplitude,
* runaway-like behavior above it,

within a fixed simulation time.

This is not necessarily an asymptotic stability threshold.
It depends on the model, parameters, observation time, and event criterion.

---

## Boundary anisotropy

**Boundary anisotropy** refers to directional dependence in boundary shape or boundary deformation.

In BIG, anisotropy is not treated merely as a visual feature. It can affect stability thresholds, boundary failure, and finite-time runaway behavior.

In the B8 series, boundary anisotropy is associated with shifts in finite-time separatrix thresholds.

---

## Boundary cost

**Boundary cost** refers to the energetic or effective penalty associated with maintaining a boundary.

In B9-type geometric models, this is represented by a perimeter-like term:

$$
\sigma P(\Omega),
$$

where (P(\Omega)) denotes the boundary length or perimeter-like measure of the domain (\Omega), and (\sigma) is a boundary-cost coefficient.

---

## Nonlocal repulsion

**Nonlocal repulsion** refers to a repulsive interaction that depends on the global configuration, not only on local boundary shape.

In B9, this is represented by a Coulomb-like term:

$$
\lambda C(\Omega),
$$

where (C(\Omega)) is a nonlocal repulsion functional and (\lambda) controls its strength.

The competition between boundary cost and nonlocal repulsion can produce a fission-like metastable landscape in the reduced B9 model.

---

## Fission-like

The term **fission-like** means that a reduced model shows a structural pattern resembling fission:

* compact state,
* deformation or pinch,
* finite barrier,
* separated branch.

In BIG, “fission-like” does **not** mean that the model is a quantitative theory of nuclear fission.

BIG-B9 does not explicitly resolve shell corrections, pairing effects, quantum tunneling, excitation-energy dependence, fragment yields, cross-section normalization, or calibration to nuclear observables in the present minimal model.

However, this limitation should not be read as a claim that such effects are incompatible with the BIG framework. In future extensions, such effects may be represented through effective boundary corrections, state-dependent coefficients, hidden-depth mode contributions, barrier-crossing dynamics, or other higher-level structures built upon the B9 energy landscape.

Thus, “fission-like” should be read as a macroscopic structural comparison, not as a quantitative nuclear calculation.

---

## Fusion-like

The term **fusion-like** means that a reduced model shows a structural pattern resembling capture or merging:

* approach,
* contact or near-contact,
* internal activation,
* sustained locking,
* post-capture stabilization.

In BIG, “fusion-like” does **not** mean that the model is a quantitative theory of nuclear fusion.

BIG-B10 and BIG-B12 do not model Coulomb-barrier penetration, quantum tunneling, nuclear potentials, plasma kinetics, reaction cross sections, or real fusion energy release.

---

## Capture

**Capture** means that two boundary-supported systems enter a sustained coupled state.

In BIG, capture is not defined by first contact alone.

A trajectory may show a first hit or transient approach without achieving sustained capture.

This distinction is especially important in B10 and B12.

---

## Resonance locking

**Resonance locking** refers to a sustained state in which internal modes remain sufficiently aligned or activated after boundary approach.

In B10 and B12, resonance locking is used to distinguish transient contact from stable capture.

A key idea is:

```text
first hit != sustained capture
```

---

## Finite-noise window

A **finite-noise window** is a range of noise intensity where a desired dynamical outcome is enhanced.

In BIG-B10 and BIG-B12:

* too little noise may fail to activate the relevant internal channel,
* intermediate noise may enable sustained capture or R-lock,
* too much noise may destroy sustained locking.

This is described as stochastic-resonance-like behavior.

---

## Hidden depth

**Hidden depth** refers to internal degrees of freedom that are not visible in the primary boundary geometry but can affect post-capture memory and stabilization.

In B11 and B12, hidden-depth variables are used to represent whether post-capture states collapse into assimilation or preserve multiple parent-like memories.

---

## Hidden-depth inheritance

**Hidden-depth inheritance** refers to the preservation of more than one parent-like memory after a capture or fusion-like event.

In a simplified B11/B12 notation, a hidden-depth state may be written as:

$$
h=(h_A,h_B).
$$

Here, inheritance does not mean biological inheritance in the quantitative genetic sense.
It means memory retention in a reduced hidden-state landscape.

---

## Assimilation

**Assimilation** means collapse toward one dominant parent-like or attractor-like state.

In B11, assimilation competes with hidden-depth inheritance.

A post-capture state may either:

* collapse toward parent A,
* collapse toward parent B,
* or preserve both parent memories in a hidden-depth inheritance state.

---

## Structural correspondence

A **structural correspondence** is a qualitative similarity between the behavior of a reduced BIG model and a known pattern in another field.

For example:

* B9 structurally resembles surface-versus-repulsion competition in macroscopic fission intuition.
* B10 structurally resembles stochastic-resonance-like capture.
* B11 structurally resembles inheritance-versus-assimilation competition.
* B12 connects boundary approach, resonance locking, and hidden-depth inheritance in one reduced model.

A structural correspondence is not the same as a quantitative physical prediction.

---

## Reduced model

A **reduced model** is a simplified mathematical model designed to isolate a structural mechanism.

Reduced models are useful for exploring possible principles, but they do not automatically provide calibrated predictions for real systems.

Most current BIG results should be read as reduced-model results.

---

## Model-level claim

A **model-level claim** is a claim that holds within the specified equations, parameters, numerical methods, and event definitions of a given model.

Many BIG claims are currently model-level claims.

They should not be treated as direct claims about real physical, biological, or technological systems without additional domain-specific validation.

---

---

## Observation-like state selection

**Observation-like state selection** is the reduced B13/B13.1 mechanism in which a boundary-mediated coupling changes which hidden-depth basin is selected.

The word *observation-like* is deliberately limited: it denotes a state-selection mechanism inside the model. It is not a derivation of quantum measurement, the Born rule, consciousness, or perception.

---

## Boundary history

**Boundary history** is an explicit state variable used to retain traces of earlier boundary-localized interactions.

In B14 and later work, history may be written, relaxed, partitioned, compressed, transported, or sampled by later dynamics. Retained history is therefore treated as part of the evolving state rather than only as an external record.

---

## Stored history and readable history

**Stored history** means that a history field remains present in the model.

**Readable history** means that the retained field is positioned and coupled so that the current boundary dynamics can actually sample it.

B17 emphasizes the distinction:

```text
stored history != readable history
```

A large global history mass can coexist with weak later response if the relevant trace is no longer locally accessible to the moving boundary.

---

## Boundary readout operator

A **boundary readout operator** maps retained history into a quantity that can affect later dynamics through the current boundary or interface geometry.

B18 extends read-start local sampling toward path-integrated and interface-core exposure. A representative form is

$
L_{\mathrm{read}}=\int \lambda(t)\int m(x,t)\,W(x;R(t))\,G_{\Sigma}[\Phi](x,t)\,dx\,dt.
$

This is a reduced operator construction, not a calibrated theory of biological, neural, chemical, or material memory.

---

## Interface-core path exposure

**Interface-core path exposure** is a B18 readout diagnostic that accumulates history encountered by the dynamically relevant interface/core region along its path.

It distinguishes history that merely exists somewhere in the domain from history that is actually exposed to the evolving boundary.

---

## Boundary-core channel

A **boundary-core channel** is a direction-dependent diagnostic organization used in B19 synthetic divergence-free vorticity experiments. It combines upstream boundary/core information with downstream strain-alignment and production-versus-dissipation behavior over a finite observation window.

The observed channel classes are finite-family numerical diagnostics. They are not a universal Navier--Stokes classification or a blow-up criterion.

---

## Finite-window response function

For a state or parameter point $P$, finite-time evolution $U_T$, and readout $Z$, B20 uses the response function

$
F_T(P)=Z[U_T(P)]-Z[P].
$

Its value depends on the chosen evolution operator, readout, observation window, and parameter family.

---

## Response boundary

A **response boundary** is the zero set

$
\mathcal{B}_T=\{P:F_T(P)=0\}.
$

In B20 this is generally a **parameter-space boundary generated by an operator and a finite observation window**. It should not automatically be interpreted as a physical-space interface, invariant manifold, asymptotic separatrix, or universal threshold.

---

## Operator-generated boundary

An **operator-generated boundary** is a boundary defined by the action of an evolution/readout construction rather than assumed in advance as a material or geometric interface.

B20 uses this idea to extend the BIG vocabulary from boundaries represented directly in physical space to boundaries that emerge in finite-time response geometry.

---

## Response gradient

The **response gradient** in B21 is

$
g(T,P)=\nabla_S F_T(P),
$

where the gradient is taken only in the exact normalized four-dimensional B20.5 subspace $S$. It is not a full intrinsic gradient in the unrestricted parameter space.

---

## Hessian-vector transport

**Hessian-vector transport** refers to the term $H_S\dot P_B$, which describes the change in the local response gradient caused by motion of the boundary point through parameter space. Here $H_S$ is the finite-dimensional subspace Hessian.

---

## Local kinematic closure

**Local kinematic closure** means that the observed transport of the response gradient along a tracked boundary branch is explained, within numerical uncertainty, by

$
\frac{Dg}{dT}=\partial_T g+H_S\dot P_B.
$

In B21 this is a tested local identity in one finite synthetic family and one exact normalized subspace. It is not a new equation of motion or a continuum existence theorem.

---

## Frozen prospective test

A **frozen prospective test** fixes its branch, time points, differencing/refinement choices, pass criteria, and stopping rule before evaluating the terminal result. B21 uses this separation to distinguish the exploratory E1--E11 diagnostics from the terminal E12 closure test. B22 applies the same principle to the `r09` E3 and E5 stages, freezing each forecast before the corresponding future PDE evaluation.

---

## Finite-resolution local geometry

**Finite-resolution local geometry** means curvature, normal rotation, Hessian, and principal-direction descriptors reconstructed at explicitly tested finite-difference scales in normalized parameter coordinates. Cross-scale agreement supports numerical stability at those scales; it does not prove continuum differentiability or coordinate-invariant physical geometry.

---

## Shape operator and principal modes

For a regular level set with unit normal $n=g/\lVert g\rVert$, B22 projects the normalized Hessian onto the tangent space to obtain a finite-dimensional **shape operator**. Its resolved eigenvalues and eigenvectors are reported as signed principal curvatures and principal directions. Near-degenerate directions are treated as subspace-degenerate rather than individually identified.

---

## Sequential prospective stage

A **sequential prospective stage** makes a new frozen forecast from the latest observed state. B22 E5 predicts T2 from the observed T1 geometry. It is therefore prospective with respect to T2, but it is not a T0-only two-step-ahead forecast.

---

## Recommended usage

Preferred wording:

> BIG studies boundary-centered reduced models of individuality, stability, separation, capture, and inheritance.

Preferred cautious phrasing:

> fission-like structural metastability

> macroscopic structural comparison

> stochastic-resonance-like finite-noise capture

> hidden-depth inheritance in a reduced model

> model-level numerical evidence

> structural correspondence

Wording to avoid unless explicitly qualified:

> BIG proves nuclear fission

> BIG explains nuclear fusion

> BIG is a complete theory of consciousness

> BIG replaces existing physics

> BIG quantitatively predicts biological inheritance

---

## Japanese key terms

| English                       | Japanese                           |
| ----------------------------- | ---------------------------------- |
| Boundary Information Geometry | 境界情報幾何学                            |
| boundary                      | 境界                                 |
| non-assimilation              | 非同化                                |
| individuality                 | 個体性 / 個                            |
| boundary layer                | 境界層                                |
| quadratic landing             | 二次着地                               |
| quartic-gradient stiffness    | 四次勾配剛性                             |
| finite-time separatrix        | 有限時間セパラトリクス                        |
| boundary anisotropy           | 境界異方性                              |
| boundary cost                 | 境界コスト                              |
| nonlocal repulsion            | 非局所反発                              |
| fission-like                  | fission-like / 分裂様                 |
| fusion-like                   | fusion-like / 融合様                  |
| capture                       | 捕獲                                 |
| resonance locking             | 共鳴ロック                              |
| finite-noise window           | 有限ノイズ窓                             |
| hidden depth                  | hidden depth / 隠れた深度               |
| hidden-depth inheritance      | hidden-depth inheritance / 隠れた深度継承 |
| assimilation                  | 同化                                 |
| structural correspondence     | 構造対応                               |
| reduced model                 | 縮約モデル                              |
| model-level claim             | モデルレベルの主張                          |
| observation-like state selection | 観測様状態選択 |
| boundary history | 境界履歴 |
| stored history | 保存された履歴 |
| readable history | 読み出し可能な履歴 |
| boundary readout operator | 境界読み出し演算子 |
| interface-core path exposure | 界面コア経路曝露 |
| boundary-core channel | 境界コア・チャネル |
| finite-window response function | 有限時間窓応答関数 |
| response boundary | 応答境界 |
| operator-generated boundary | 演算子生成境界 |
| response gradient | 応答勾配 |
| Hessian-vector transport | Hessian–ベクトル輸送 |
| local kinematic closure | 局所運動学的閉包 |
| frozen prospective test | 凍結した前向き試験 |
| finite-resolution local geometry | 有限解像度局所幾何 |
| shape operator | 形状作用素 |
| principal curvature / direction | 主曲率 / 主方向 |
| sequential prospective stage | 逐次前向き段階 |
