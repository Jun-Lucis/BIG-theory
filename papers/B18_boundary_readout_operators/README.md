# BIG-B18 — Boundary Readout Operators in Boundary Information Geometry

## Subtitle

From Read-Start Local History to Interface-Core Path Exposure in a Reaction-Diffusion-Inspired Front Model


> 🇯🇵 **日本語要約**  
> B18では、B17の「読み出し可能な履歴」をさらに進め、境界が時間発展の途中で実際にどの履歴へ曝露されたかを readout operator として記述します。read-start時点の局所履歴だけでなく、境界・interface-core が経路上で受ける履歴曝露を積分すると、後の応答をよりよく整理できる場合が確認されました。BIGの履歴概念はここで、保存された痕跡から動的に読み出される情報へ拡張されます。

## Purpose

BIG-B18 asks what readout operator turns retained history into later response.

A representative form is

$$
\mathcal{L}_{\mathrm{read}}
=
\int_{t_0}^{t_1}\lambda(t)
\int m(x,t)W(x;R(t))G_\Sigma[\Phi](x,t)\,dx\,dt.
$$

In the B17 positive-feedback regime, this readout reduces approximately to a read-start local load. In the B18 reaction-diffusion-inspired inhibitory front model, later front suppression is better organized by path-integrated interface-core / threshold-gated trace exposure than by read-start local trace or global trace mass.

The B18 diagnostics therefore suggest the operational hierarchy

> stored history → local readable history → path readable history → interface-core path exposure.

For a representative condition ($\alpha=0.01$, $\kappa=6$, rest delay $=1$, read width $=0.35$, read duration $=3.2$), the raw threshold-gated path exposure and suppression response increase together across the reported protocols; for example, front-anchored writing changes from $(E_{\mathrm{path}}^{G0.15},\Delta R_{\mathrm{supp}})=(1.119,0.909)$ at one write to $(1.755,1.325)$ at three writes. These are representative model values rather than universal coefficients.

The resulting operator-level statement is:

> Retained history becomes dynamically effective after projection through a boundary-dependent readout operator.

## Representative figure

![Stored to readable history flow](../../figures/B18/B18_4_stored_to_readable_history_flow.png)

*B18 summary diagnostic: stored history becomes dynamically effective only after boundary-dependent readout, motivating the progression from retained trace to readable/path-exposed history.*

## Scope

The front-and-trace model is a reduced numerical and operator-level study. It does not claim to derive reaction-diffusion chemistry, material interface physics, biological adaptation, wound healing, immune memory, neural memory, learning, consciousness, or quantum measurement. The reaction-diffusion front is used as a physically recognizable reduced test bed for the stored-history versus readable-history distinction.

## Publication

Zenodo: https://zenodo.org/records/22690970

Author: Jun Lucis
