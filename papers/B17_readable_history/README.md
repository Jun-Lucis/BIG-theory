# BIG-B17 — Stored History versus Readable History


> 🇯🇵 **日本語要約**  
> B17では、「履歴が保存されていること」と「現在の境界がその履歴を読み出せること」を分離します。移動境界に追随して書かれた履歴と実験室座標に固定された履歴などを比較すると、履歴の総量が残っていても境界から局所的にアクセスできなければ後の応答は弱くなり得ます。したがって後の応答を組織するのは単なる保存量ではなく、現在の境界座標系で読み出し可能な履歴です。

## Purpose

BIG-B17 sharpens the B16 result:

> stored history is not automatically readable history.

A retained history field affects later response only when the relevant component remains locally sampleable in the current moving-boundary frame.

Boundary-anchored writing, laboratory-fixed writing, and controls on history transport test this distinction.

## Representative figure

![Read branches with advected memory](../../figures/B17/B17_4_read_branches_advected_memory_n5.png)

*Representative read-branch diagnostic used to test whether retained history remains dynamically readable in the moving-boundary frame.*

## Scope

The result is model-level and concerns a reduced moving-boundary system. It is not a general theory of biological or cognitive memory.

## Publication

Zenodo: https://zenodo.org/records/22677581

Author: Jun Lucis
