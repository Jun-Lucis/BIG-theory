"""Recompute archived B19 diagnostics. Does not run ODE/PDE trajectories."""
from pathlib import Path
import argparse, json, hashlib, warnings
import numpy as np
import pandas as pd

def verify(root):
    source = root / 'sources'
    checks = []
    def path(name):
        candidates = sorted(source.rglob(name))
        if not candidates:
            raise FileNotFoundError(name)
        return candidates[0]
    def read(name):
        return pd.read_csv(path(name))
    def check(name, actual, expected, category='saved_algebra'):
        a, e = np.asarray(actual), np.asarray(expected)
        if a.dtype.kind in 'biufc' and e.dtype.kind in 'biufc':
            a,e = a.astype(float),e.astype(float)
            ok = a.shape == e.shape and np.allclose(a,e,rtol=2e-10,atol=5e-11,equal_nan=True)
            finite = np.isfinite(a)&np.isfinite(e)
            err = float(np.max(np.abs(a[finite]-e[finite]))) if finite.any() else 0.0
        else:
            ok = a.shape == e.shape and np.all((a==e)|(pd.isna(a)&pd.isna(e)))
            err = None
        checks.append(dict(name=name,category=category,n_values=int(a.size),status='PASS' if ok else 'FAIL',max_abs_error=err))

    # Hash-level identity of all compact public CSV/JSON claim sources.
    old = root/'old_public/unpacked/BIG_B19_Zenodo_Release_v1_0/data'
    for p in sorted(old.glob('*')):
        check('public_identity/'+p.name, hashlib.sha256(path(p.name).read_bytes()).hexdigest(), hashlib.sha256(p.read_bytes()).hexdigest(), 'public_provenance')

    # Algebraic consistency of stored diagnostics, including unchanged checkpoints.
    files = [p for p in source.rglob('*.csv') if not p.name.startswith('B19_21')]
    for p in sorted(files):
        d=pd.read_csv(p); c=set(d.columns); label=p.relative_to(source).as_posix()
        def chk(col, val):
            check(label+'/'+col, d[col].to_numpy(), np.asarray(val))
        if {'stretch_total','dissipation_total','balance_total'} <= c:
            chk('balance_total',d.stretch_total-d.dissipation_total)
        if {'gradomega_total','nu','dissipation_total'} <= c:
            chk('dissipation_total',d.nu*d.gradomega_total)
        if {'positive_stretch_gate','negative_stretch_gate','signed_stretch_gate'} <= c:
            chk('signed_stretch_gate',d.positive_stretch_gate-d.negative_stretch_gate)
        if {'signed_stretch_gate','dissipation_gate','theta_signed_gate'} <= c:
            chk('theta_signed_gate',d.signed_stretch_gate/np.maximum(d.dissipation_gate,1e-300))
        if {'positive_stretch_gate','negative_stretch_gate','signed_stretch_gate','coherence_gate'} <= c:
            chk('coherence_gate',d.signed_stretch_gate/np.maximum(d.positive_stretch_gate+d.negative_stretch_gate,1e-300))
        if {'balance_total','total_balance_open'} <= c:
            chk('total_balance_open',d.balance_total>0)
        if {'signed_stretch_gate','dissipation_gate','gate_open'} <= c:
            chk('gate_open',d.signed_stretch_gate>d.dissipation_gate)
        if {'initial_enstrophy_half','final_enstrophy_half','final_delta_enstrophy'} <= c:
            chk('final_delta_enstrophy',d.final_enstrophy_half-d.initial_enstrophy_half)
            if 'final_relative_growth' in c:
                chk('final_relative_growth',(d.final_enstrophy_half-d.initial_enstrophy_half)/np.maximum(abs(d.initial_enstrophy_half),1e-300))
        if {'final_delta_enstrophy','growth_positive'} <= c:
            chk('growth_positive',d.final_delta_enstrophy>0)
        if {'integrated_balance_final','integrated_balance_positive'} <= c:
            chk('integrated_balance_positive',d.integrated_balance_final>0)
        if {'integrated_balance_final','final_delta_enstrophy','balance_integral_error_final'} <= c:
            chk('balance_integral_error_final',d.final_delta_enstrophy-d.integrated_balance_final)
        if {'growth_positive','integrated_balance_positive','integrated_sign_correct'} <= c:
            chk('integrated_sign_correct',d.growth_positive==d.integrated_balance_positive)
        if {'eps_lo','eps_hi','bracket_width','epsilon_c_midpoint'} <= c:
            chk('bracket_width',d.eps_hi-d.eps_lo)
            chk('epsilon_c_midpoint',(d.eps_hi+d.eps_lo)/2)
        if {'p','q','s','finite_core_energy','enstrophy_blowup','stretching_dominates_leakage','compatible_window'} <= c:
            energy=2*d.p<=5*d.q; enstrophy=2*d.p>3*d.q; stretch=d.p>2*d.q*d.s
            chk('finite_core_energy',energy);chk('enstrophy_blowup',enstrophy)
            chk('stretching_dominates_leakage',stretch);chk('compatible_window',energy&enstrophy&stretch)

    # Integrals are trapezoidal quadratures on archived diagnostic samples.
    timeseries_count=0
    for p in sorted(source.rglob('*timeseries.csv')):
        if p.name.startswith('B19_21'):continue
        d=pd.read_csv(p); c=set(d.columns)
        if not {'t','enstrophy_half','balance_total'}<=c:continue
        key='variant_id' if 'variant_id' in c else ('case_id' if 'case_id' in c else None)
        if key is None:continue
        for ident,g in d.groupby(key):
            g=g.sort_values('t').drop_duplicates('t',keep='last')
            z=g.enstrophy_half.to_numpy();t=g.t.to_numpy();b=g.balance_total.to_numpy()
            integ=np.r_[0,np.cumsum((b[1:]+b[:-1])*np.diff(t)/2)]
            label=p.name+'/'+str(ident)
            timeseries_count+=1
            for col, val in [('delta_enstrophy',z-z[0]),('relative_enstrophy_change',(z-z[0])/max(z[0],1e-300)),('integrated_balance_to_t',integ),('balance_integral_error_to_t',z-z[0]-integ)]:
                if col in c:check(label+'/'+col,g[col],val,'timeseries_recompute')

    # B19.11: independently derive the headline 4/4/16 classes from B19.10.
    t10=read('B19_10_dynamic_threshold_control_timeseries.csv')
    d11=read('B19_11_integrated_balance_case_classification.csv').set_index('case_id')
    classes=[]
    for ident,g in t10.groupby('case_id'):
        g=g.sort_values('t'); b=g.balance_total.to_numpy();z=g.enstrophy_half.to_numpy();t=g.t.to_numpy()
        ib=np.sum((b[1:]+b[:-1])*np.diff(t)/2);dz=z[-1]-z[0]
        cls='initially_activated_growth' if b[0]>0 and dz>0 else ('delayed_activation_growth' if b[0]<=0 and max(b)>0 and dz>0 else ('subcritical_decay' if b[0]<=0 and ib<=0 and dz<=0 else 'other'))
        classes.append(cls);r=d11.loc[ident]
        for k,v in {'integrated_balance':ib,'delta_enstrophy':dz,'B0':b[0],'B_final':b[-1],'class':cls,'balance_integral_error':dz-ib}.items():check('B19.11/'+str(ident)+'/'+k,r[k],v,'headline_recompute')
    for cls,n in [('initially_activated_growth',4),('delayed_activation_growth',4),('subcritical_decay',16)]:check('B19.11/count/'+cls,classes.count(cls),n,'headline_recompute')

    d7=read('B19_7_short_time_vorticity_dynamics_case_summary.csv')
    growth7=next(c for c in ['relative_enstrophy_change','final_relative_enstrophy_change'] if c in d7)
    check('B19.7/net_growth_count',int((d7[growth7]>0).sum()),1,'headline_recompute')
    for filename,n in [('B19_9_dynamic_convergence_case_summary.csv',12),('B19_13_finite_window_convergence_case_summary.csv',24),('B19_14_dynamic_box_spectral_case_summary.csv',12)]:
        d=read(filename); col=next(c for c in ['final_relative_growth','relative_enstrophy_change','final_relative_enstrophy_change'] if c in d)
        check(filename+'/positive_growth',int((d[col]>0).sum()),n,'headline_recompute')

    # B19.17b: local brackets and the two retained integral/sign disagreements.
    conv=read('B19_17b_convergence_case_summary.csv'); brackets=read('B19_17b_boundary_convergence_summary.csv')
    check('B19.17b/valid_brackets',int(brackets.bracket_valid.sum()),18,'headline_recompute')
    check('B19.17b/growth_sign_agreement',int(((conv.final_delta_enstrophy>0)==(conv.integrated_balance_final>0)).sum()),130,'headline_recompute')
    check('B19.17b/all_bracket_signs',(brackets.deltaZ_lo>0)&(brackets.deltaZ_hi<0),np.ones(len(brackets),bool),'headline_recompute')
    shifts=brackets.groupby(['ray_label','N']).epsilon_c_midpoint.agg(lambda x:x.max()-x.min())
    spread=brackets.groupby(['ray_label','dt_cap']).epsilon_c_midpoint.agg(lambda x:x.max()-x.min())
    check('B19.17b/max_dt_midpoint_shift',shifts.max(),0.0,'headline_recompute')
    check('B19.17b/max_resolution_midpoint_spread',spread.max(),.0234375,'headline_recompute')

    # Recompute retention, numerical-safety maxima, and reported JSON values.
    retained=read('B19_16_local_neighborhood_dynamic_classification.csv')
    retention=read('B19_16_neighborhood_retention_summary.csv').set_index('parent_label')
    retention_columns={'growth_positive_fraction':'growth_positive','final_balance_positive_fraction':'final_balance_positive','integrated_balance_positive_fraction':'integrated_balance_positive','spectral_safe_fraction':'spectral_safe','static_gate_robust_fraction':'static_gate_robust','parent_class_retention_fraction':'parent_class_retained','carry_forward_fraction':'carry_forward_neighbor'}
    for parent,g in retained.groupby('parent_label'):
        r=retention.loc[parent]
        for target,col in retention_columns.items():
            if col in g:check('B19.16/retention/'+parent+'/'+target,r[target],g[col].mean(),'headline_recompute')
    d13=read('B19_13_finite_window_convergence_case_summary.csv')
    check('B19.13/manuscript_max_final_divergence_rounded',format(d13.final_div_omega_l2.max(),'.3g'),'1.12e-13','headline_recompute')
    check('B19.13/manuscript_max_final_highk_rounded',format(d13.final_highk_fraction.max(),'.3g'),'4.13e-27','headline_recompute')
    for prefix,filename,columns in [
        ('B19_14','B19_14_dynamic_box_spectral_case_summary.csv',{'max_outside_dealias_fraction':'final_outside_dealias_fraction','max_tail_fraction_70':'final_tail_fraction_70','max_tail_fraction_85':'final_tail_fraction_85'})]:
        summary=json.loads(path(prefix+'_main_summary.json').read_text());d=read(filename)
        for key,col in columns.items():
            if key in summary and col in d:check(prefix+'/headline/'+key,summary[key],d[col].max(),'headline_recompute')

    # B19.18: reconstruct interpolation, collapse scores, scalar folds.
    m=read('B19_17a_ray_expanded_map.csv'); crit=read('B19_18_critical_observable_values.csv')
    score=read('B19_18_scalar_collapse_scores.csv').set_index('observable')
    folds=read('B19_18_leave_one_ray_out_threshold_test.csv')
    obs=[c for c in crit if c not in ['ray_label','epsilon_c']]
    derived_crit={}
    for _,r in crit.iterrows():
        ray=r.ray_label;ec=r.epsilon_c;derived_crit[ray]={}
        for col in obs:
            d=m[m.ray_label==ray][['epsilon',col]].dropna().drop_duplicates('epsilon').sort_values('epsilon')
            val=float(np.interp(ec,d.epsilon,d[col])) if len(d)>=2 and d.epsilon.min()<=ec<=d.epsilon.max() else np.nan
            derived_crit[ray][col]=val;check('B19.18/interpolation/'+ray+'/'+col,r[col],val,'reduction_recompute')
    for col,r in score.iterrows():
        a=np.array([derived_crit[ray][col] for ray in sorted(derived_crit)])
        pooled=m[col].replace([np.inf,-np.inf],np.nan).dropna().to_numpy()
        iqr=np.diff(np.quantile(pooled,[.25,.75]))[0]; ran=np.ptp(a)
        vals={'critical_mean':a.mean(),'critical_sd':a.std(),'critical_range':ran,'critical_cv_abs':a.std()/abs(a.mean()) if abs(a.mean())>1e-12 else np.nan,'critical_range_over_pooled_iqr':ran/iqr if iqr>1e-12 else np.nan}
        for k,v in vals.items():check('B19.18/collapse/'+col+'/'+k,r[k],v,'reduction_recompute')
    for _,r in folds.iterrows():
        col=r.observable; held=r.held_out_ray
        tr=m[m.ray_label!=held][[col,'growth_positive']].dropna();te=m[m.ray_label==held][[col,'growth_positive']].dropna()
        threshold=np.mean([d[col] for ray,d in derived_crit.items() if ray!=held])
        with warnings.catch_warnings():
            warnings.simplefilter('ignore');corr=np.corrcoef(tr[col].astype(float),tr.growth_positive.astype(int))[0,1]
        orientation=1 if corr>=0 else -1
        acc=(((te[col]-threshold)*orientation>=0)==te.growth_positive).mean()
        check('B19.18/fold/'+col+'/'+held+'/accuracy',r.held_out_accuracy,acc,'reduction_recompute')
        check('B19.18/fold/'+col+'/'+held+'/threshold',r.threshold_from_other_two,threshold,'reduction_recompute')

    # B19.19: training-only robust scale, nearest centroids, held-out counts.
    f19=read('B19_19_2d_leave_one_ray_out_folds.csv')
    for _,r in f19.iterrows():
        x,y,held=r.x,r.y,r.held_out_ray
        tr=m[m.ray_label!=held][[x,y,'growth_positive']].dropna();te=m[m.ray_label==held][[x,y,'growth_positive']].dropna()
        Xtr=tr[[x,y]].to_numpy(float);Xte=te[[x,y]].to_numpy(float)
        center=np.median(Xtr,axis=0);scale=np.diff(np.quantile(Xtr,[.25,.75],axis=0),axis=0)[0]
        std=np.std(Xtr,axis=0);scale=np.where(np.isfinite(scale)&(scale>=1e-12),scale,std);scale=np.where(np.isfinite(scale)&(scale>=1e-12),scale,1.)
        Xtr=(Xtr-center)/scale;Xte=(Xte-center)/scale
        yt=tr.growth_positive.to_numpy(bool);ye=te.growth_positive.to_numpy(bool)
        c0=Xtr[~yt].mean(axis=0);c1=Xtr[yt].mean(axis=0)
        pred=np.sum((Xte-c1)**2,axis=1)<=np.sum((Xte-c0)**2,axis=1)
        tp=int(np.sum(pred&ye));tn=int(np.sum(~pred&~ye));fp=int(np.sum(pred&~ye));fn=int(np.sum(~pred&ye))
        vals={'tp':tp,'tn':tn,'fp':fp,'fn':fn,'n_test':len(ye),'accuracy':np.mean(pred==ye),'balanced_accuracy':.5*(tp/(tp+fn)+tn/(tn+fp))}
        for k,v in vals.items():check('B19.19/'+r.pair+'/'+held+'/'+k,r[k],v,'reduction_recompute')

    s19=read('B19_19_2d_pair_summary.csv')
    for _,r in s19.iterrows():
        g=f19[(f19.level==r.level)&(f19.pair==r.pair)]
        for target,col,op in [('mean_accuracy','accuracy','mean'),('min_accuracy','accuracy','min'),('mean_balanced_accuracy','balanced_accuracy','mean'),('min_balanced_accuracy','balanced_accuracy','min')]:
            check('B19.19/summary/'+r.pair+'/'+target,r[target],getattr(g[col],op)(),'reduction_recompute')
    check('B19.19/passing_pairs',int(((s19.mean_balanced_accuracy>=.80)&(s19.min_balanced_accuracy>=.70)).sum()),0,'headline_recompute')

    # B19.20: coarse-map nearest-side differences, not derivatives at refined roots.
    local=read('B19_20_local_separatrix_changes.csv')
    for i,r in local.iterrows():
        d=m[m.ray_label==r.ray_label]
        lo=d[np.isclose(d.epsilon,r.epsilon_below)].iloc[0][r.observable]
        hi=d[np.isclose(d.epsilon,r.epsilon_above)].iloc[0][r.observable]
        for k,v in {'value_below':lo,'value_above':hi,'jump_above_minus_below':hi-lo,'local_slope_dobs_deps':(hi-lo)/(r.epsilon_above-r.epsilon_below)}.items():check('B19.20/'+str(i)+'/'+k,r[k],v,'mechanism_recompute')

    return dict(status='PASS' if all(x['status']=='PASS' for x in checks) else 'FAIL',scope='Saved-data recomputation only; no ODE/PDE or new trajectories',independent_full_rerun_audit='NOT_COMPLETED',checks=len(checks),numeric_or_label_values=sum(x['n_values'] for x in checks),timeseries_case_groups=timeseries_count,failed_checks=[x for x in checks if x['status']!='PASS'],records=checks)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);p.add_argument('--output',type=Path)
    args=p.parse_args();result=verify(args.root)
    output=args.output or args.root/'audit/B19_Saved_Result_Verification.json';output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))
    raise SystemExit(0 if result['status']=='PASS' else 1)
