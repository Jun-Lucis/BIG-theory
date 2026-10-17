"""Independent saved-data recomputation for B19.21-22. No PDE integration."""
from pathlib import Path
import argparse,json
import numpy as np
import pandas as pd

def verify(root):
    package=root/'sources/public_stage_packages'
    old=root/'old_public/unpacked/BIG_B19_21_22_Reproducibility_Archive_v1_0'
    records=[]
    def path(name):
        hits=list(package.rglob(name))
        if len(hits)!=1:raise ValueError((name,len(hits)))
        return hits[0]
    def read(name):return pd.read_csv(path(name))
    def check(name,a,e,category='saved_recompute'):
        a,e=np.asarray(a),np.asarray(e)
        if a.shape!=e.shape:
            ok=False;err=None
        elif a.dtype.kind in 'biufc' and e.dtype.kind in 'biufc':
            a,e=a.astype(float),e.astype(float);ok=np.allclose(a,e,rtol=2e-9,atol=5e-12,equal_nan=True)
            finite=np.isfinite(a)&np.isfinite(e);err=float(np.max(abs(a[finite]-e[finite]))) if finite.any() else 0.
        else:
            ok=np.all((a==e)|(pd.isna(a)&pd.isna(e)));err=None
        records.append({'name':name,'category':category,'values':int(a.size),'status':'PASS' if ok else 'FAIL','max_abs_error':err})
    def frame(name,actual,expected,keys):
        check(name+'/rows',len(actual),len(expected))
        a=actual.sort_values(keys).reset_index(drop=True);e=expected.sort_values(keys).reset_index(drop=True)
        check(name+'/columns',list(a),list(e))
        for c in e:check(name+'/'+c,a[c],e[c])
    def first(t,y):
        hit=np.where(np.asarray(y)>0)[0];return float(t[hit[0]]) if len(hit) else np.nan
    def crossing(t,y):
        t,y=np.asarray(t),np.asarray(y);mask=t>1e-12;t,y=t[mask],y[mask]
        for i in range(len(t)-1):
            if y[i]<0<y[i+1]:return (t[i]-y[i]*(t[i+1]-t[i])/(y[i+1]-y[i]),t[i],t[i+1],y[i],y[i+1])
        return (np.nan,)*5

    # Authoritative archived time histories, not original simulation execution.
    series={
        '21C':read('B19_21C_refined_pair_timeseries.csv'),
        '22A':read('B19_22A_timeseries_checkpoint.csv'),
        '22B':read('B19_22B_all_timeseries.csv'),
        '22C':read('B19_22C_all_timeseries_COMPLETE_38of38.csv')}
    for stage,d in series.items():
        check(stage+'/balance',d.balance_total,d.stretch_total-d.dissipation_total,'trajectory_bookkeeping')
        for (ray,eps),g in d.groupby(['ray_label','epsilon']):
            g=g.sort_values('t');t=g.t.to_numpy();z=g.enstrophy_half.to_numpy();b=g.balance_total.to_numpy()
            integral=np.r_[0,np.cumsum((b[1:]+b[:-1])*np.diff(t)/2)]
            label=stage+'/'+ray+'/'+format(eps,'.12g')
            for col,v in [('delta_enstrophy',z-z[0]),('integrated_balance_to_t',integral),('balance_integral_error_to_t',z-z[0]-integral)]:check(label+'/'+col,g[col],v,'trajectory_bookkeeping')

    # Exact refined bracket event readouts.
    events=read('B19_21C_event_times.csv')
    for _,r in events.iterrows():
        g=series['21C'][(series['21C'].ray_label==r.ray_label)&np.isclose(series['21C'].epsilon,r.epsilon)].sort_values('t')
        t=g.t.to_numpy();vals={'first_balance_positive':first(t,g.balance_total),'first_integrated_balance_positive':first(t,g.integrated_balance_to_t),'first_deltaZ_positive':first(t,g.delta_enstrophy),'theta_min':g.theta_signed_gate.min(),'theta_max':g.theta_signed_gate.max(),'final_integrated_balance':g.integrated_balance_to_t.iloc[-1],'final_deltaZ':g.delta_enstrophy.iloc[-1]}
        for c,v in vals.items():check('21C/events/'+r.ray_label+'/'+r.critical_side+'/'+c,r[c],v,'headline_recompute')
    check('21C/all_first_balance_rounded',np.round(events.first_balance_positive,6),np.full(6,.005),'headline_recompute')

    # Same initial cases at the longer horizon; common samples are not independent repeats.
    c=series['21C'];a=series['22A'];joined=c.merge(a,on=['ray_label','epsilon','step'],suffixes=('_short','_long'))
    check('21C_22A/shared_prefix_rows',len(joined),len(c),'lineage')
    for col in ['t','enstrophy_half','delta_enstrophy','balance_total','integrated_balance_to_t']:
        check('21C_22A/shared_prefix/'+col,joined[col+'_short'],joined[col+'_long'],'lineage')

    readouts=read('B19_22A_horizon_readout.csv')
    for i,r in readouts.iterrows():
        g=a[(a.ray_label==r.ray_label)&np.isclose(a.epsilon,r.epsilon)]
        q=g.iloc[np.argmin(abs(g.t-r.T_requested))]
        for col,v in {'t_sample':q.t,'balance_total':q.balance_total,'integrated_balance':q.integrated_balance_to_t,'deltaZ':q.delta_enstrophy,'theta_signed_gate':q.theta_signed_gate}.items():check('22A/readout/'+str(i)+'/'+col,r[col],v,'headline_recompute')
    survival=read('B19_22A_boundary_survival.csv')
    for i,r in survival.iterrows():
        g=readouts[(readouts.ray_label==r.ray_label)&np.isclose(readouts.T_requested,r['T'])].set_index('critical_side')
        lo=g.loc['growth'];hi=g.loc['decay']
        for col,v in {'growth_deltaZ':lo.deltaZ,'decay_deltaZ':hi.deltaZ,'fixed_bracket_survives':lo.deltaZ>0 and hi.deltaZ<0,'growth_integrated_balance':lo.integrated_balance,'decay_integrated_balance':hi.integrated_balance}.items():check('22A/survival/'+str(i)+'/'+col,r[col],v,'headline_recompute')
    check('22A/reference_survives',int(survival[np.isclose(survival['T'],.010)].fixed_bracket_survives.sum()),3,'headline_recompute')
    check('22A/extension_012_survives',int(survival[np.isclose(survival['T'],.012)].fixed_bracket_survives.sum()),0,'headline_recompute')

    # Scalar checkpoints against every archived endpoint/horizon.
    for stage,horizons in [('22B',[.010,.012,.015,.020]),('22C',[.012,.015,.020])]:
        cp=read('B19_'+stage+'_case_checkpoint.csv');d=series[stage]
        for i,r in cp.iterrows():
            g=d[(d.ray_label==r.ray_label)&np.isclose(d.epsilon,r.epsilon,atol=1e-12,rtol=0)].sort_values('t')
            check(stage+'/case_present/'+str(i),len(g)>0,True,'coverage')
            for T in horizons:
                q=g.iloc[np.argmin(abs(g.t-T))];check(stage+'/scalar/'+str(i)+'/'+str(T),r[f'deltaZ_T{T:.3f}'],q.delta_enstrophy,'checkpoint_recompute')
                if stage=='22C':check(stage+'/scalar_integral/'+str(i)+'/'+str(T),r[f'I_T{T:.3f}'],q.integrated_balance_to_t,'checkpoint_recompute')
    check('22C/complete_cases',len(series['22C'][['ray_label','epsilon']].drop_duplicates()),38,'coverage')
    check('22C/rows_per_case',series['22C'].groupby(['ray_label','epsilon']).size(),np.full(38,81),'coverage')
    rec=read('B19_22C_missing_case_recovery_audit.csv')
    check('22C/historical_recovery_readouts',len(rec),57,'coverage')
    check('22C/historical_recovery_delta_error',rec.abs_diff_deltaZ,abs(rec.new_deltaZ-rec.old_deltaZ),'checkpoint_recompute')
    check('22C/historical_recovery_integral_error',rec.abs_diff_integrated_balance,abs(rec.new_integrated_balance-rec.old_integrated_balance),'checkpoint_recompute')
    check('22C/historical_recovery_tolerance',rec.within_tol,np.ones(57,bool),'checkpoint_recompute')
    for i,r in rec.iterrows():
        g=series['22C'][(series['22C'].ray_label==r.ray_label)&np.isclose(series['22C'].epsilon,r.epsilon,atol=1e-12,rtol=0)]
        q=g.iloc[np.argmin(abs(g.t-r['T']))]
        check('22C/recovery_new_delta/'+str(i),r.new_deltaZ,q.delta_enstrophy,'checkpoint_recompute')
        check('22C/recovery_new_integral/'+str(i),r.new_integrated_balance,q.integrated_balance_to_t,'checkpoint_recompute')
    for name,stage in [('B19_22B_moving_boundary.csv','22B'),('B19_22C_extended_boundary_status.csv','22C')]:
        cp=read('B19_'+stage+'_case_checkpoint.csv');d=read(name)
        for i,r in d.iterrows():
            if not np.isfinite(r.get('eps_lo',np.nan)):continue
            check(stage+'/midpoint/'+str(i),r.eps_mid,(r.eps_lo+r.eps_hi)/2,'bracket_recompute')
            for side in ['lo','hi']:
                q=cp[(cp.ray_label==r.ray_label)&np.isclose(cp.epsilon,r['eps_'+side],atol=1e-12,rtol=0)].iloc[0]
                check(stage+'/bracket/'+str(i)+'/'+side,r['deltaZ_'+side],q[f'deltaZ_T{r["T"]:.3f}'],'bracket_recompute')

    # Cone table: refined degeneracy is independent of a small denominator regularizer.
    cone=pd.read_csv(old/'data/B19_21B_refined_initial_cone_test.csv')
    check('21B/G',cone.G0,cone.C0*cone.theta0,'cone_recompute')
    check('21B/K',cone.K0,(1-cone.C0)*cone.omega_max0,'cone_recompute')
    bracket=pd.read_csv(old/'data/B19_21B_refined_bracket_summary.csv')
    check('21B/refined_chi_growth',bracket.chi_growth,np.zeros(3),'cone_recompute');check('21B/refined_chi_decay',bracket.chi_decay,np.zeros(3),'cone_recompute')
    check('21B/refined_ordering_support',bracket.ordering_supported,np.zeros(3,bool),'cone_recompute')
    coarse=[]
    for ray,lo,hi in [('loss_ray_p01',0.,.25),('loss_ray_p02',0.,.25),('loss_ray_p03',.25,.5)]:
        q=cone[cone.ray_label==ray];low=q[np.isclose(q.epsilon,lo,atol=1e-12,rtol=0)].iloc[0];high=q[np.isclose(q.epsilon,hi,atol=1e-12,rtol=0)].iloc[0]
        coarse.append(bool(high.chi0>low.chi0))
    check('21B/coarse_ordering_by_ray',coarse,[False,False,True],'cone_recompute')
    check('21B/coarse_ordering_supported_count',sum(coarse),1,'cone_recompute')

    # Recreate response samples, adjacent epsilon secants, classes and detected roots.
    expected=series['22C'][['ray_label','epsilon_22C','t','delta_enstrophy']].rename(columns={'epsilon_22C':'epsilon','delta_enstrophy':'deltaZ'}).drop_duplicates(['ray_label','epsilon','t']).sort_values(['ray_label','t','epsilon']).reset_index(drop=True)
    response=read('B19_22D_response_samples.csv');frame('22D/response',response,expected,['ray_label','t','epsilon'])
    slope_rows=[];class_rows=[];root_rows=[]
    for (ray,T),g in response.groupby(['ray_label','t']):
        g=g.sort_values('epsilon');e=g.epsilon.to_numpy();y=g.deltaZ.to_numpy();s=np.diff(y)/np.diff(e);pos=int((s>1e-12).sum());neg=int((s< -1e-12).sum())
        cls='increasing' if pos and not neg else ('decreasing' if neg and not pos else ('mixed' if pos and neg else 'flat_or_undetermined'))
        class_rows.append(dict(ray_label=ray,T=T,response_class=cls,n_positive_slopes=pos,n_negative_slopes=neg,min_slope=s.min(),max_slope=s.max()))
        for i,v in enumerate(s):slope_rows.append(dict(ray_label=ray,T=T,eps_left=e[i],eps_right=e[i+1],slope=v,slope_sign=int(np.sign(v))))
        for i in range(len(e)-1):
            if y[i]==0:root_rows.append(dict(ray_label=ray,T=T,eps_root_linear=e[i],eps_left=e[i],eps_right=e[i],status='sampled_zero'))
            elif y[i]*y[i+1]<0:root_rows.append(dict(ray_label=ray,T=T,eps_root_linear=e[i]-y[i]*(e[i+1]-e[i])/(y[i+1]-y[i]),eps_left=e[i],eps_right=e[i+1],status='sign_change'))
    slopes=pd.DataFrame(slope_rows);classes=pd.DataFrame(class_rows);roots=pd.DataFrame(root_rows)
    frame('22D/slopes',read('B19_22D_epsilon_secant_slopes.csv'),slopes,['ray_label','T','eps_left'])
    frame('22D/classes',read('B19_22D_response_class_by_time.csv'),classes,['ray_label','T'])
    frame('22D/roots',read('B19_22D_zero_crossings_descriptive.csv'),roots,['ray_label','T','eps_left'])
    check('22D/sign_change_roots',int((roots.status=='sign_change').sum()),45,'headline_recompute')

    geometry=read('B19_22E_zero_contour_geometry.csv')
    signroots=roots[roots.status=='sign_change'].sort_values(['ray_label','T']).reset_index(drop=True)
    ordered=geometry.sort_values(['ray_label','T']).reset_index(drop=True)
    for col in ['ray_label','T','eps_root_linear','eps_left','eps_right']:check('22E/root_lineage/'+col,ordered[col],signroots[col],'geometry_recompute')
    for i,r in geometry.iterrows():
        g=response[(response.ray_label==r.ray_label)&np.isclose(response.t,r['T'],atol=1e-12,rtol=0)]
        for col,eps in [('deltaZ_left',r.eps_left),('deltaZ_right',r.eps_right)]:
            val=g[np.isclose(g.epsilon,eps,atol=1e-12,rtol=0)].deltaZ.iloc[0]
            check('22E/endpoint/'+str(i)+'/'+col,r[col],val,'geometry_recompute')
    for ray,g in geometry.groupby('ray_label'):
        g=g.sort_values('T');T=g['T'].to_numpy();e=g.eps_root_linear.to_numpy();v=np.r_[np.nan,np.diff(e)/np.diff(T)];acc=np.r_[np.nan,np.nan,np.diff(v[1:])/np.diff(T[1:])]
        check('22E/velocity/'+ray,g.contour_velocity,v,'geometry_recompute');check('22E/acceleration/'+ray,g.contour_acceleration_secant,acc,'geometry_recompute')
        check('22E/local_slope/'+ray,g.local_epsilon_slope,(g.deltaZ_right-g.deltaZ_left)/(g.eps_right-g.eps_left),'geometry_recompute')
    summary_e=read('B19_22E_ray_geometry_summary.csv')
    for _,r in summary_e.iterrows():
        g=geometry[geometry.ray_label==r.ray_label].sort_values('T');v=g.contour_velocity.dropna();s=g.local_epsilon_slope
        vals={'n_sign_change_roots':len(g),'T_first_root':g['T'].min(),'T_last_root':g['T'].max(),'eps_first_root':g.eps_root_linear.iloc[0],'eps_last_root':g.eps_root_linear.iloc[-1],'root_moves_outward_monotonically':bool(np.all(np.diff(g.eps_root_linear)>0)),'velocity_min':v.min(),'velocity_max':v.max(),'local_epsilon_slope_min':s.min(),'local_epsilon_slope_max':s.max(),'local_slope_all_negative':bool((s<0).all()),'local_slope_all_positive':bool((s>0).all())}
        for col,value in vals.items():check('22E/summary/'+r.ray_label+'/'+col,r[col],value,'headline_recompute')
    reversal=read('B19_22E_orientation_reversal_times.csv')
    for _,r in reversal.iterrows():
        g=classes[classes.ray_label==r.ray_label].sort_values('T');lo=crossing(g['T'],g.max_slope);hi=crossing(g['T'],g.min_slope)
        for col,v in zip(['T_loss_of_globally_decreasing_linear','T_maxslope_left','T_maxslope_right','maxslope_left','maxslope_right'],lo):check('22E/reversal/'+r.ray_label+'/'+col,r[col],v,'geometry_recompute')
        for col,v in zip(['T_onset_globally_increasing_linear','T_minslope_left','T_minslope_right','minslope_left','minslope_right'],hi):check('22E/reversal/'+r.ray_label+'/'+col,r[col],v,'geometry_recompute')

    # Recreate all deterministic epsilon and time thinning variants.
    derived=[]
    for ray,g in response.groupby('ray_label'):
        e=np.sort(g.epsilon.unique());variants={'full':e,'alternate_even':e[::2],'alternate_odd':e[1::2],'drop_lowest':e[1:],'drop_highest':e[:-1],'interior_every2_keep_ends':np.unique(np.r_[e[0],e[1:-1:2],e[-1]])}
        for label,keep in variants.items():
            if len(keep)<3:continue
            for T,q in g[g.epsilon.isin(keep)].groupby('t'):
                q=q.sort_values('epsilon');s=np.diff(q.deltaZ)/np.diff(q.epsilon)
                cls='increasing' if np.all(s>1e-12) else ('decreasing' if np.all(s< -1e-12) else ('mixed' if np.any(s>1e-12) and np.any(s< -1e-12) else 'flat_or_tolerance'))
                derived.append(dict(ray_label=ray,variant=label,T=T,min_slope=s.min(),max_slope=s.max(),response_class=cls,n_secants=len(s)))
    derived=pd.DataFrame(derived);frame('22F/classes',read('B19_22F_class_by_epsilon_variant.csv'),derived,['ray_label','variant','T'])
    epsrev=read('B19_22F_epsilon_sampling_reversal_times.csv')
    for _,r in epsrev.iterrows():
        g=derived[(derived.ray_label==r.ray_label)&(derived.variant==r.variant)].sort_values('T');lo=crossing(g['T'],g.max_slope);hi=crossing(g['T'],g.min_slope)
        for col,v in zip(['T_loss_decreasing','T_loss_left','T_loss_right','max_left','max_right'],lo):check('22F/epsilon/'+r.ray_label+'/'+r.variant+'/'+col,r[col],v,'sampling_recompute')
        for col,v in zip(['T_onset_increasing','T_inc_left','T_inc_right','min_left','min_right'],hi):check('22F/epsilon/'+r.ray_label+'/'+r.variant+'/'+col,r[col],v,'sampling_recompute')
    time=read('B19_22F_time_sampling_reversal_times.csv')
    full=derived[derived.variant=='full']
    label_check=classes.merge(full,on=['ray_label','T'],suffixes=('_D','_F'));label_check=label_check[label_check['T']>1e-12]
    check('22D_22F/nonzero_time_class_agreement',label_check.response_class_D,label_check.response_class_F,'sampling_recompute')
    for i,r in time.iterrows():
        g=full[full.ray_label==r.ray_label].sort_values('T');times=np.sort(g.loc[g['T']>1e-12,'T'].unique());keep=times[int(r.time_offset)::int(r.time_stride)];keep=np.unique(np.r_[keep,times[-1]])
        q=g[(g['T']<=1e-12)|g['T'].isin(keep)];lo=crossing(q['T'],q.max_slope);hi=crossing(q['T'],q.min_slope)
        for col,v in {'n_nonzero_times':int((q['T']>1e-12).sum()),'T_loss_decreasing':lo[0],'T_onset_increasing':hi[0]}.items():check('22F/time/'+str(i)+'/'+col,r[col],v,'sampling_recompute')
    for name,data in [('B19_22F_epsilon_sampling_summary.csv',epsrev),('B19_22F_time_sampling_summary.csv',time)]:
        summ=read(name)
        for _,r in summ.iterrows():
            g=data[data.ray_label==r.ray_label];vals={'loss_detected_fraction':g.T_loss_decreasing.notna().mean(),'onset_detected_fraction':g.T_onset_increasing.notna().mean(),'loss_T_min':g.T_loss_decreasing.min(),'loss_T_max':g.T_loss_decreasing.max(),'onset_T_min':g.T_onset_increasing.min(),'onset_T_max':g.T_onset_increasing.max()}
            for col,v in vals.items():check(name+'/'+r.ray_label+'/'+col,r[col],v,'headline_recompute')

    return {'status':'PASS' if all(r['status']=='PASS' for r in records) else 'FAIL','scope':'Saved CSV/JSON recomputation only; no new ODE/PDE trajectories','independent_full_rerun_audit':'NOT_COMPLETED','check_groups':len(records),'numeric_or_label_comparisons':sum(r['values'] for r in records),'failed_checks':[r for r in records if r['status']!='PASS'],'records':records}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);p.add_argument('--output',type=Path);args=p.parse_args();result=verify(args.root)
    output=args.output or args.root/'audit/B19_Followup_Saved_Result_Verification.json';output.parent.mkdir(parents=True,exist_ok=True);output.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2));raise SystemExit(0 if result['status']=='PASS' else 1)
