# BIG-B16 — Memory-Bearing Free Boundaries


> 🇯🇵 **日本語要約**  
> B16では、履歴場 $m(x,t)$ を動く自由境界に直接結合し、「過去の局在刺激が後の境界応答を変えられるか」を数値的に検査します。履歴を保持する条件と消去する条件、刺激位置、境界移動、フィードバックの有無を比較し、保持された履歴が後の局所応答に影響する構造を確認しました。これにより履歴は単なる記録ではなく、後の境界運動へ戻る内部状態変数になります。

## Purpose

BIG-B16 couples a moving free-boundary field to a history field.

The reduced one-dimensional model couples a BIG-type free-boundary field $\phi(x,t)$ to a boundary-history field $m(x,t)$. Localized stimulation writes $m$ near a moving threshold boundary; retained history then decays, diffuses, and feeds back into later local boundary response.

The numerical program consists of six connected stages: core experiments, $\alpha$--$\eta_S$ parameter scans, kept/erased intervention tests, shifted-stimulus locality tests, moving-boundary-frame analysis, and robustness checks. The central diagnostic is the kept-minus-erased response, which isolates the contribution of retained boundary history from ordinary free-boundary drift.

Across the reduced simulations, adaptive response is controlled by history retention, feedback strength, and locally sampled retained-history load. In this model, boundary history therefore functions as an internal state variable for later local boundary response.

## Representative figure

![Response versus retained load robustness](../../figures/B16/B16_5_response_vs_retained_load_robustness.png)

*Robustness diagnostic relating retained history load to later response in the reduced memory-bearing free-boundary model.*

## Scope

This is a minimal reduced structural test showing that a moving free boundary can carry a retained local history field and reuse it through feedback coupling. It does not derive biological memory, learning, wound healing, neural adaptation, consciousness, or quantum measurement.

## Publication

Zenodo: https://zenodo.org/records/22660005

Author: Jun Lucis
