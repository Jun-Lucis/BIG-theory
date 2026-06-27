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
