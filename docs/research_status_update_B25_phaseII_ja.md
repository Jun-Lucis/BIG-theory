# BIG B25 Phase II 研究状況更新

**公開 DOI:** https://doi.org/10.5281/zenodo.22967474  
**関連 Phase-I DOI:** https://doi.org/10.5281/zenodo.22956894  
**著者:** Jun Lucis

B25 Phase II は、Phase I で構成された prospective な境界汎関数 transfer を、target 側較正を減らしながらどこまで縮約できるかを検査した。

## 証拠系列

```text
B25.1c  parallel-curve reduction
         -> AB_PARALLEL_CURVE_REDUCTION_PASS

B25.1d  nested-band single-perimeter reduction
         -> AB_NESTED_BAND_SINGLE_PERIMETER_PASS

B25.1e  single-anchor fixed-coefficient closure
         -> AB_FIXED_COEFFICIENT_PERIMETER_PASS

B25.2   B9-like two-center geometry transfer
         -> IMPLEMENTATION_INVALID
```

以前の B24.2 と B25.1 の判定は変更しない。

```text
B24.2 -> MULTIPLE_BOUNDARY_CLASSES_INDICATED
B25.1 -> AB_CONSTANT_DENSITY_FAIL
```

## B25.1c

held-out 側の level-set perimeter family 全体を、1本の representative perimeter と、archived 1D relative-level gradient profile から作る固定 no-fit parallel-curve correction に縮約した。

正式判定: `AB_PARALLEL_CURVE_REDUCTION_PASS`

## B25.1d

凍結済み nested relative-level band を狭めることで explicit parallel-curve correction を縮小し、最狭 band でも amplitude-aware single-perimeter predictor が凍結済み accuracy / stability gate を通過した。

正式判定: `AB_NESTED_BAND_SINGLE_PERIMETER_PASS`

## B25.1e

新しい円形 calibration state 1本から

[
sigma_{m cal}=9.434181431178162	imes10^{-8}
]

を固定した。その後の6つの held-out ellipse では primary prediction に target representative perimeter のみを用いた。

[
J_{m pred}=sigma_{m cal}P_{m rep}.
]

6ケースすべて valid、held-out median relative error は **4.65%**、maximum relative error は **14.30%** で、fine-resolution pair gate もすべて通過した。

正式判定: `AB_FIXED_COEFFICIENT_PERIMETER_PASS`

これは B25 で初めて、primary held-out predictor が target peak amplitude と full target level-set perimeter family を必要としなくなった段階である。

## B25.2

B25.1e の係数をそのまま固定し、connected / disconnected representative contour を跨ぐことを意図した equal-injection two-center geometry family への transfer を事前宣言付きで検査した。

しかし、事前宣言した test は有効に実現しなかった。

- coarse resolution の3ケースが、凍結済み minimum three-grid-cell claim-band thickness を下回った。
- fine resolution でも全ケースの primary representative contour 数が1のままで、要求した topology span が実現しなかった。

正式判定: `IMPLEMENTATION_INVALID`

invalid test から得た descriptive error は archive に保持するが、formal transfer FAIL へ昇格させない。

## Phase II で支持される記述

tested canonical (p=4) finite-resolution ellipse family の範囲では、Phase-I boundary-functional transfer は、事前指定した円形 calibration state 1本から得た fixed perimeter coefficient へ prospectively 縮約でき、held-out ellipse shape へ target perimeter だけを用いて移植できた。

geometry-family transfer と topology transfer は未解決である。

## 未確立事項

Phase II は以下を確立しない。

- continuum perimeter theorem
- universal / source-independent な (sigma P) law
- 1D information のみから導出された coefficient
- B9 の nonlocal term (C(Omega))
- 完全な B9 energy (E=sigma P+lambda C)
- 外部物理系に対する妥当性

学術上の正文は英語版 Zenodo preprint であり、日本語版は参考翻訳である。
