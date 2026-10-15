"""Audit B13.1 saved results without generating stochastic trajectories.

The optional deterministic Gaussian quadrature recomputes reported derived
curves. This is not an independent rerun of the original simulations.
"""
from pathlib import Path
import argparse
import json
import hashlib
import numpy as np
import pandas as pd
from scipy.special import expit
from numpy.polynomial.hermite import hermgauss


def audit(root):
    root = Path(root)
    data = root / "data"
    tables = {p.stem: pd.read_csv(p) for p in data.glob("*.csv")}
    summaries = {p.stem: json.loads(p.read_text()) for p in data.glob("*.json")}
    checks = []

    def check(name, actual, expected, atol=2e-11, rtol=3e-10):
        x, y = np.asarray(actual, dtype=float), np.asarray(expected, dtype=float)
        match = x.shape == y.shape and np.allclose(x, y, atol=atol, rtol=rtol, equal_nan=True)
        delta = np.abs(x-y) if x.shape == y.shape else np.array([np.inf])
        finite = delta[np.isfinite(delta)]
        checks.append(dict(name=name, passed=bool(match), compared_values=int(x.size),
                           maximum_absolute_difference=float(finite.max()) if finite.size else 0.0,
                           atol=atol, rtol=rtol))

    def metric_row(frame, error):
        e = np.asarray(frame[error], float)
        return [np.sqrt(np.mean(e*e)), np.mean(e), np.max(np.abs(e))]

    # References, coordinate conversions, probabilities, and count consistency.
    for name, t in sorted(tables.items()):
        if "alpha" in t and "alpha_deg" in t:
            check(name+": alpha units", np.rad2deg(t.alpha), t.alpha_deg)
        if "theta" in t and "theta_deg" in t:
            check(name+": theta units", np.rad2deg(t.theta), t.theta_deg)
        if "delta" in t and "delta_deg" in t:
            check(name+": delta units", np.rad2deg(t.delta), t.delta_deg)
        if "width_rad" in t and "width_deg" in t:
            check(name+": width units", np.rad2deg(t.width_rad), t.width_deg)
        if "p_ref_cos2_theta_minus_alpha" in t:
            ref = np.cos(t.theta-t.alpha)**2
            check(name+": reference", ref, t.p_ref_cos2_theta_minus_alpha)
            if "error" in t:
                check(name+": error", t.p_plus-ref, t.error)
        if "delta" in t and "theta" in t:
            check(name+": shifted coordinate", t.theta-t.alpha, t.delta)
            check(name+": shifted reference", np.cos(t.delta)**2, t.p_ref_delta)
        if "ref_cos2_delta" in t:
            check(name+": sequential reference", np.cos(np.deg2rad(t.delta_deg))**2, t.ref_cos2_delta)
        if "stage2_n_plus" in t:
            check(name+": count probability", t.stage2_n_plus/t.stage2_n_total, t.P_plus2_given_plus1)
        if "stage1_n_plus" in t and "stage2_n_total" in t:
            check(name+": parent counts", t.stage1_n_plus, t.stage2_n_total)
        if "error_cos2" in t and ("P_plus2_given_plus1" in t or "P_plus2" in t):
            pp = t.P_plus2_given_plus1 if "P_plus2_given_plus1" in t else t.P_plus2
            check(name+": cos2 error", pp-t.ref_cos2_delta, t.error_cos2)
            check(name+": logistic error", pp-t.ref_logistic_delta, t.error_logistic)

    # Seed-wise and basis-wise robustness.
    t=tables["A_rotated_basis_robust_curves_all_seeds"]
    by=tables["A_rotated_basis_robust_summary_by_seed"]
    expected=[]
    for r in by.itertuples():
        g=t[(t.seed==r.seed)&np.isclose(t.alpha,r.alpha)]
        expected.append(metric_row(g,"error"))
    check("rotated robustness: seed summaries", expected,
          by[["rmse_vs_basis_born_like","mean_shift","max_abs_error"]].values)
    agg=tables["A_rotated_basis_robust_summary_agg"]
    expected=[]
    for r in agg.itertuples():
        g=by[np.isclose(by.alpha,r.alpha)]
        expected.append([g.rmse_vs_basis_born_like.mean(),g.rmse_vs_basis_born_like.std(ddof=1),
                         g.rmse_vs_basis_born_like.min(),g.rmse_vs_basis_born_like.max(),
                         g.mean_shift.mean(),g.mean_shift.std(ddof=1),g.max_abs_error.mean()])
    check("rotated robustness: across-seed aggregates",expected,
          agg[["mean_rmse","std_rmse","min_rmse","max_rmse","mean_shift","std_shift","mean_max_abs_error"]].values)
    single=tables["A_rotated_basis_selection_curves"]
    stored=tables["A_rotated_basis_rmse_summary"]
    check("final-seed curves preserved",single.p_plus.values,t[t.seed==505].p_plus.values)
    check("final-seed metrics",[metric_row(single[np.isclose(single.alpha,r.alpha)],"error") for r in stored.itertuples()],
          stored[["rmse_vs_basis_born_like","mean_shift","max_abs_error"]].values)

    # Shifted-coordinate collapse and empirical logistic kernels.
    collapse=tables["A_rotated_basis_collapse_all_points"]
    check("collapse preserves all robust probabilities",collapse.p_plus.values,t.p_plus.values)
    cs=summaries["A_rotated_basis_curve_collapse_summary"]
    check("collapse global metrics",metric_row(collapse,"error_delta"),
          [cs["global_rmse_vs_cos2_delta"],cs["global_mean_shift"],cs["global_max_abs_error"]])
    bins=tables["A_rotated_basis_collapse_by_delta_bin"]
    expected=[]
    for r in bins.itertuples():
        g=collapse[np.isclose(collapse.delta_bin,r.delta_bin)]
        expected.append([g.p_plus.mean(),g.p_plus.std(ddof=1),len(g),g.p_ref_delta.mean(),g.error_delta.mean(),g.error_delta.std(ddof=1)])
    check("collapse bin aggregates",expected,bins[["mean_p_plus","std_p_plus","n","mean_ref","mean_error","std_error"]].values)
    ab=tables["A_rotated_basis_collapse_by_alpha"]
    check("collapse alpha aggregates",[metric_row(collapse[np.isclose(collapse.alpha,r.alpha)],"error_delta") for r in ab.itertuples()],
          ab[["rmse_delta","mean_shift_delta","max_abs_error_delta"]].values)
    fit=tables["A_rotated_basis_empirical_kernel_fit_metrics"].set_index("model")
    fine=tables["A_rotated_basis_empirical_kernel_fit_curves"]
    check("smooth cos2 reference",np.cos(np.deg2rad(fine.delta_deg))**2,fine.cos2_ref)
    for model,column in [("logistic_cos2delta","logistic_kernel"),("logistic_cos2delta_bias","logistic_kernel_bias")]:
        r=fit.loc[model];bias=0.0 if np.isnan(r.bias) else r.bias
        k=lambda d:expit(r.kappa*(np.cos(2*d)-r.c)+bias)
        check(model+": stored smooth curve",k(np.deg2rad(fine.delta_deg)),fine[column])
        check(model+": raw RMSE",np.sqrt(np.mean((k(collapse.delta)-collapse.p_plus)**2)),r.raw_rmse)
        check(model+": binned RMSE",np.sqrt(np.mean((k(np.deg2rad(bins.delta_bin))-bins.mean_p_plus)**2)),r.binned_rmse)
    # c and additive logit bias are exactly redundant, not extra shape degrees.
    r=fit.loc["logistic_cos2delta_bias"]
    effective_c=float(r.c-r.bias/r.kappa)
    parameter_notes={"baseline_kernel":fit.loc["logistic_cos2delta",["kappa","c"]].to_dict(),
                     "biased_fit_effective_c":effective_c,
                     "bias_identifiability":"Only -kappa*c+bias is identifiable at fixed kappa"}

    # Barrier-noise grid and reported scaling laws.
    raw=tables["B13_2_kernel_scaling_all_points"]
    binned=tables["B13_2_kernel_scaling_binned_curves"]
    scale=tables["B13_2_kernel_scaling_summary"]
    expected=[]
    for r in scale.itertuples():
        g=raw[np.isclose(raw.b,r.b)&np.isclose(raw.sigma,r.sigma)]
        h=binned[np.isclose(binned.b,r.b)&np.isclose(binned.sigma,r.sigma)]
        k=lambda d:expit(r.kappa*(np.cos(2*d)-r.c))
        expected.append([np.sqrt(np.mean((h.mean_p_plus-np.cos(np.deg2rad(h.delta_bin))**2)**2)),
                         np.sqrt(np.mean((h.mean_p_plus-k(np.deg2rad(h.delta_bin)))**2)),
                         np.sqrt(np.mean((g.p_plus-g.p_ref_delta)**2)),
                         np.sqrt(np.mean((g.p_plus-k(g.delta))**2))])
    check("20 scaling-condition fit metrics",expected,
          scale[["rmse_cos2_binned","rmse_kernel_binned","raw_rmse_cos2","raw_rmse_kernel"]].values)
    for suffix,value in [("kappa","kappa"),("kernel_rmse","rmse_kernel_binned"),("cos2_rmse","rmse_cos2_binned")]:
        piv=tables["B13_2_kernel_scaling_"+suffix+"_pivot"].set_index("b")
        check(suffix+": pivot",scale.pivot(index="b",columns="sigma",values=value).values,piv.values)
    sp=tables["B13_2_kernel_scaling_law_fit_points"]
    y=np.log(sp.kappa.values); lb=np.log(sp.b.values);ls=np.log(sp.sigma.values)
    fm=tables["B13_2_kernel_scaling_law_fit_metrics"].set_index("model")
    scaling_results={}
    for label,X,prefix in [("power_law",np.c_[np.ones(len(y)),lb,-ls],"power"),
                           ("ratio_law",np.c_[np.ones(len(y)),lb-2*ls],"ratio")]:
        coef=np.linalg.lstsq(X,y,rcond=None)[0];yp=X@coef;kp=np.exp(yp)
        rr=1-np.sum((y-yp)**2)/np.sum((y-y.mean())**2)
        metrics=[np.exp(coef[0]),rr,np.sqrt(np.mean((y-yp)**2)),np.sqrt(np.mean((sp.kappa-kp)**2))]
        row=fm.loc["power_law_C_b^p_sigma^-q" if label=="power_law" else "ratio_law_C_(b_sigma^-2)^r"]
        check(label+": fit metrics",metrics,[row.C,row.R2_log,row.RMSE_log,row.RMSE_kappa])
        check(label+": predictions",kp,sp["kappa_pred_"+prefix])
        check(label+": log predictions",yp,sp["log_kappa_pred_"+prefix])
        check(label+": residuals",sp.kappa-kp,sp["residual_"+prefix])
        if label=="power_law":check(label+": exponents",coef[1:],[row.p,row.q])
        else:check(label+": exponent",coef[1],row.r)
        scaling_results[label]={"C":metrics[0],"exponents":coef[1:].tolist(),"R2_log":rr}

    # Sequential tests: distinct raw-row and mean-curve RMSE conventions.
    sequential=tables["B13_3_sequential_robust_all_points"]
    reset=tables["B13_3b_sequential_reset_comparison_all_points"]
    clouds=tables["B13_3c_cloud_width_all_points"]
    for source,summary,key in [
        (sequential,"B13_3_sequential_robust_by_alpha1","alpha1_deg"),
        (reset,"B13_3b_sequential_reset_comparison_by_mode","mode"),
        (reset,"B13_3b_sequential_reset_comparison_by_mode_alpha1",["mode","alpha1_deg"]),
        (clouds,"B13_3c_cloud_width_summary_by_width","width_deg")]:
        st=tables[summary]; keys=[key] if isinstance(key,str) else key
        values=[]
        for r in st.to_dict("records"):
            mask=np.ones(len(source),bool)
            for k in keys:
                mask &= source[k].eq(r[k]).values if source[k].dtype==object else np.isclose(source[k],r[k])
            g=source[mask];values.append([*metric_row(g,"error_cos2")[:2],*metric_row(g,"error_logistic")[:2]])
        check(summary+": RMSE and mean shift",values,st[["rmse_cos2","mean_shift_cos2","rmse_logistic","mean_shift_logistic"]].values)
    js=summaries["B13_3_sequential_robust_summary"]["metrics"]
    check("sequential global RMSE",[metric_row(sequential,"error_cos2")[0],metric_row(sequential,"error_logistic")[0]],
          [js["global_rmse_cos2"],js["global_rmse_logistic"]])

    # Reconstruct all reported Gaussian convolution curves on the unchanged targets.
    targets=tables["B13_3d_gaussian_cloud_convolution_curves_all"]
    widths=tables["B13_3d_gaussian_cloud_convolution_width_fit_all"]
    cm=tables["B13_3d_gaussian_cloud_convolution_metrics"].set_index("target")
    nodes,weights=hermgauss(100)
    convolution_results={}
    for target,g in targets.groupby("target",sort=False):
        g=g.sort_values("delta_deg");r=cm.loc[target]
        w=widths[widths.target==target].sort_values("width_deg")
        grid=np.deg2rad(w.width_deg.values)
        delta=np.deg2rad(g.delta_deg.values)
        angles=delta[None,:,None]+np.sqrt(2)*grid[:,None,None]*nodes[None,None,:]
        predictions=(expit(r.kappa*(np.cos(2*angles)-r.c))*weights).sum(axis=-1)/np.sqrt(np.pi)
        error=predictions-g.P_target.values
        rmse=np.sqrt(np.mean(error**2,axis=1));best=int(np.argmin(rmse))
        check(target+": all 241 width RMSE",rmse,w.rmse_to_target.values)
        check(target+": all width mean shifts",error.mean(axis=1),w.mean_shift.values)
        check(target+": all width max errors",np.abs(error).max(axis=1),w.max_abs_error.values)
        check(target+": optimum width",np.rad2deg(grid[best]),r.best_width_deg)
        check(target+": optimum RMSE",rmse[best],r.best_rmse_to_target)
        check(target+": best convolution curve",predictions[best],g.K_cloud_best.values)
        check(target+": point kernel curve",predictions[0],g.K_BIG_w0.values)
        check(target+": residual sign",error[best],g.error_best.values)
        convolution_results[target]={"width_deg":float(r.best_width_deg),"rmse_mean_curve":float(r.best_rmse_to_target)}
    for r in tables["B13_3d_centroid_norm_width_estimates"].itertuples():
        check(r.source+": equivalent angular width",np.rad2deg(np.sqrt(-2*np.log(r.mean_centroid_norm))),r.estimated_width_deg_from_R)
    parameter_notes["sequential_kernel"]={"kappa":float(cm.iloc[0].kappa),"c":float(cm.iloc[0].c)}
    grid_baseline=scale[np.isclose(scale.b,1)&np.isclose(scale.sigma,.35)].iloc[0]
    check("sequential kernel comes from scaling grid",[cm.iloc[0].kappa,cm.iloc[0].c],[grid_baseline.kappa,grid_baseline.c])

    result={"paper":"B13.1","checkpoint":"CP18","scope":"Stored-data arithmetic, deterministic quadrature and publication provenance; no stochastic rerun",
            "csv_files":len(tables),"csv_rows":sum(len(x) for x in tables.values()),
            "json_files":len(summaries),"check_groups":len(checks),
            "compared_values":sum(x["compared_values"] for x in checks),
            "passed_groups":sum(x["passed"] for x in checks),"checks":checks,
            "parameter_provenance":parameter_notes,"scaling_laws":scaling_results,
            "convolution_recalculation":convolution_results,
            "new_stochastic_trajectories":0,"scientific_verdict_changes":0,
            "original_simulation_source_recovered":True,
            "source_recovery_receipt":"supplement/recovered_code/source_provenance.json",
            "independent_full_rerun_audit":"NOT_YET_COMPLETED"}
    result["status"]="PASS" if all(x["passed"] for x in checks) else "REVIEW_DIFFERENCES"
    return result


if __name__ == "__main__":
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("archive_root",type=Path)
    ap.add_argument("--output",type=Path,required=True)
    args=ap.parse_args()
    result=audit(args.archive_root)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2,ensure_ascii=False,allow_nan=False)+"\n")
    print(json.dumps({k:result[k] for k in ["status","csv_files","csv_rows","check_groups","compared_values","passed_groups"]}))
    for c in result["checks"]:
        if not c["passed"]:print(json.dumps(c))
