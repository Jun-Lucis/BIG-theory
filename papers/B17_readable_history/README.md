# BIG-B17 — Stored History versus Readable History


> 🇯🇵 **日本語要約**  
> B17では、「履歴が保存されていること」と「現在の境界がその履歴を読み出せること」を分離します。移動境界に追随して書かれた履歴と実験室座標に固定された履歴などを比較すると、履歴の総量が残っていても境界から局所的にアクセスできなければ後の応答は弱くなり得ます。したがって後の応答を組織するのは単なる保存量ではなく、現在の境界座標系で読み出し可能な履歴です。

## Purpose

BIG-B17 sharpens the B16 result:

> stored history is not automatically readable history.

Using reduced write/read protocols, B17 separates the writing of boundary history from its later feedback-mediated readout. The numerical program proceeds through four connected stages: write/read separation, moving-frame decomposition of the write-count effect, boundary-anchored writing with advected-memory controls, and full-PDE consistency checks.

The central result is that later adaptive response is not controlled primarily by global retained history mass. Instead, it is organized by the effective locally sampled retained-history load, approximately $\eta_S\,m_{\mathrm{local}}$, available to the read probe in the current moving-boundary frame. Controls with $\eta_S=0$ vanish, confirming that retained history does not affect later response without feedback coupling.

Boundary-anchored writing preserves local readability and produces stronger adaptive response. Laboratory-fixed writing can leave written traces deeper inside the moving-boundary frame and weaken readout. Artificial memory advection partially stabilizes readout, but does not fully reproduce the amplification obtained by genuine boundary-anchored writing.

## Representative figure

![Read branches with advected memory](../../figures/B17/B17_4_read_branches_advected_memory_n5.png)

*Representative read-branch diagnostic used to test whether retained history remains dynamically readable in the moving-boundary frame.*

## Scope

The result is a reduced structural test of how moving free boundaries can write, retain, and selectively read boundary history. It does not derive biological learning, neural memory, wound healing, immune adaptation, consciousness, or quantum measurement.

## Publication

Zenodo: https://zenodo.org/records/22677581

Author: Jun Lucis
