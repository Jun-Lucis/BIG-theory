# BIG B26 研究状況更新

**Zenodo DOI:** https://doi.org/10.5281/zenodo.22972985  
**関連 B25 Phase-II DOI:** https://doi.org/10.5281/zenodo.22967474  
**関連 B24–B25 Phase-I DOI:** https://doi.org/10.5281/zenodo.22956894  
**著者:** Jun Lucis

B26 は、B25.1e で前向きに得られた fixed perimeter coefficient が、held-out ellipse family から、connected / disconnected representative contour を実際に跨ぐ canonical equal-injection two-center family へ、再較正なしで移植できるかを検査した。

係数は B26 全体で固定した。

\[
\sigma_{\rm cal}=9.434181431178162\times10^{-8},
\]

primary predictor は

\[
J_{\rm pred}=\sigma_{\rm cal}P_{\rm total,rep}
\]

である。B26 target の outcome、peak amplitude、full level-set perimeter family、topology label、geometry を用いた coefficient refit は禁止した。

## 証拠系列

    B26
      topology を跨ぐ transfer を意図
      -> 6/6 numerical cases valid
      -> topology span 未実現
      -> TOPOLOGY_SPAN_NOT_REALIZED

    B26.1
      topology-only adaptive refinement
      -> 4/4 new cases valid
      -> N=384 で 4.175 < delta_* < 4.250
      -> TOPOLOGY_BRACKET_REFINED

    B26.2
      new topology-straddling held-out targets
      -> 6/6 numerical cases valid
      -> fine-resolution topology gate 実現
      -> fixed-coefficient error は大きく、resolution pair では安定
      -> AB_TOPOLOGY_STRADDLING_FIXED_COEFFICIENT_TRANSFER_FAIL

## B26

最初の B26 は

\[
\delta\in\{4.4,5.4,6.2\},\qquad N\in\{384,448\}
\]

を用いた。

6 trajectory はすべて frozen numerical validity gate を通過した。しかし fine resolution では3つの separation がすべて2つの primary representative contour を持ち、事前指定した connected / disconnected topology span は実現しなかった。

**正式判定:** TOPOLOGY_SPAN_NOT_REALIZED

## B26.1

B26.1 は fixed-coefficient action error を adaptive decision から完全に外し、representative-level topology のみで4回の bisection を行った。

    delta=3.800 -> 1 primary representative contour
    delta=4.100 -> 1
    delta=4.250 -> 2
    delta=4.175 -> 1

4ケースすべて valid で、有限解像度 transition bracket は

\[
4.175<\delta_*<4.250
\]

まで絞られた。幅は \(0.075\)。

**正式判定:** TOPOLOGY_BRACKET_REFINED

## B26.2

B26.1 で独立に局在化した topology bracket だけを用い、それまで未計算だった新規点

\[
\delta\in\{3.95,4.2125,4.35\},\qquad N\in\{384,448\}
\]

を凍結した。

6 trajectory はすべて numerical validity gate を通過した。\(N=448\) では

    delta=3.95   -> 1
    delta=4.2125 -> 1
    delta=4.35   -> 2

となり、frozen topology gate は実現した。

その条件下でも fixed-coefficient predictor は、

- median relative error: **42.91%**
- maximum relative error: **44.79%**
- median amplitude-aware comparator error: **27.29%**

となった。

resolution-pair の \(|\Delta q|\) は **0.0271**, **0.0212**, **0.0142** で、すべて frozen stability gate 内だった。したがって terminal failure は topology gate 未達や、検査した resolution-pair instability によるものではない。

**正式判定:** AB_TOPOLOGY_STRADDLING_FIXED_COEFFICIENT_TRANSFER_FAIL

frozen terminal stop rule が発動し、B26 はここで閉じる。

## 支持される記述

tested finite-resolution canonical setting の範囲では、B25.1e で held-out ellipse shapes に前向き移植できた fixed perimeter coefficient は、tested equal-injection two-center family には要求精度で移植できなかった。B26 は、この fixed-coefficient perimeter closure の **geometry-transfer boundary** を解像した。

ただし、B26.2 では connected side ですでに大きな error が存在するため、「topology change そのものが failure の唯一の原因」とは結論しない。

## 未確立事項

B26 は以下を確立しない。

- continuum theorem
- universal / source-independent perimeter law
- topology change 単独が transfer failure を生むという因果
- B9 の nonlocal term \(C(\Omega)\)
- 完全な B9 energy \(E=\sigma P+\lambda C\)
- external physical validity

学術上の正文は英語版 Zenodo preprint であり、日本語版は参考翻訳である。
