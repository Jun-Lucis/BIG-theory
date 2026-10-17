"""B20.4-6 saved-data recomputation. No ODE/PDE integration or notebook orchestration."""
from pathlib import Path
import argparse,hashlib,json
import numpy as np
import pandas as pd

PARAMS=['R','sep_factor','pair_angle','twist_factor','imbalance','axial_coupling','phase']

def verify(root):
    old=root/'old_public/unpacked/BIG_B20_Zenodo_Release_v1_0'
    packages=root/'sources/public_stage_packages'
    raw=root/'sources/drive_run'
    records=[]
    def check(name,a,e,category='saved_recompute',atol=5e-12,rtol=2e-9):
        a,e=np.asarray(a),np.asarray(e)
        if a.shape!=e.shape:ok=False;err=None
        elif a.dtype.kind in 'biufc' and e.dtype.kind in 'biufc':
            a,e=a.astype(float),e.astype(float);ok=np.allclose(a,e,atol=atol,rtol=rtol,equal_nan=True)
            mask=np.isfinite(a)&np.isfinite(e);err=float(np.max(abs(a[mask]-e[mask]))) if mask.any() else 0.
        else:ok=np.all((a==e)|(pd.isna(a)&pd.isna(e)));err=None
        records.append({'name':name,'category':category,'values':int(a.size),'status':'PASS' if ok else 'FAIL','max_abs_error':err})
    def public_path(name):
        paths=[p for p in [*old.glob(name),*packages.rglob(name)] if p.is_file()]
        if len(paths)!=1:raise ValueError((name,len(paths)))
        return paths[0]
    def read(name):return pd.read_csv(public_path(name))
    def js(name):return json.loads(public_path(name).read_text())
    def at_time(d,T):return d.iloc[np.argmin(abs(d.t-T))]
    def get_ts(folder,case):
        p=raw/folder/(case+'_timeseries.csv')
        if not p.exists():
            hits=list((raw/folder).glob('*'+case+'*timeseries.csv'))
            if len(hits)!=1:raise ValueError((folder,case,len(hits)))
            p=hits[0]
        return pd.read_csv(p).sort_values('t')

    # Every saved diagnostic history in the integrated study's three stages,
    # including historical checkpoint copies. These are not independent trials.
    history_count=0;history_rows=0;history_index={}
    for p in sorted(raw.rglob('*timeseries.csv')):
        rel=p.relative_to(raw)
        if not rel.parts[0].startswith(('B20_4_','B20_5_','B20_6_')):continue
        d=pd.read_csv(p).sort_values('t');required={'balance_total','stretch_total','dissipation_total','enstrophy_half','delta_enstrophy'}
        if not required.issubset(d):continue
        name='history/'+rel.as_posix();history_count+=1;history_rows+=len(d)
        check(name+'/balance',d.balance_total,d.stretch_total-d.dissipation_total,'trajectory_bookkeeping')
        check(name+'/deltaZ',d.delta_enstrophy,d.enstrophy_half-d.enstrophy_half.iloc[0],'trajectory_bookkeeping')
        t=d.t.to_numpy();bal=d.balance_total.to_numpy();integral=np.r_[0.,np.cumsum((bal[1:]+bal[:-1])*np.diff(t)/2)]
        if 'integrated_balance_to_t' in d:check(name+'/integral',d.integrated_balance_to_t,integral,'trajectory_bookkeeping')
        if 'balance_integral_error_to_t' in d:check(name+'/integral_residual',d.balance_integral_error_to_t,d.delta_enstrophy-integral,'trajectory_bookkeeping')
        if rel.parts[0] in ['B20_4_stageA_prospective','B20_4_stageB_refinement']:
            history_index[(rel.parts[0],str(d.ray_label.iloc[0]),round(float(d.epsilon.iloc[0]),12))]=d
    check('history/positive_coverage',history_count>0,True,'coverage')

    # B20.4: frozen affine geometry, all horizon readouts, secants and strict brackets.
    declaration=js('B20_4_FINAL_PREDECLARATION_FROZEN.json')
    points=read('B20_4_FamilyC_FINAL_68_parameter_points.csv')
    for ray,g in points.groupby('ray_label'):
        check('4/grid/'+ray,g.epsilon,np.linspace(0,2,17),'geometry')
        for k in PARAMS:
            check('4/affine/'+ray+'/'+k,g[k],declaration['base'][k]+g.epsilon*(declaration['endpoints'][ray][k]-declaration['base'][k]),'geometry')
    response=read('B20_4_stageA_response_408.csv')
    for i,r in response.iterrows():
        d=history_index[('B20_4_stageA_prospective',r.ray_label,round(r.epsilon,12))];q=at_time(d,r['T'])
        for c,v in {'F':q.delta_enstrophy,'t_saved':q.t,'time_error':abs(q.t-r['T']),'enstrophy_half':q.enstrophy_half,'balance_total':q.balance_total,'div_omega_l2':q.div_omega_l2,'tail_fraction_70':q.tail_fraction_70,'tail_fraction_85':q.tail_fraction_85,'outside_dealias_fraction':q.outside_dealias_fraction}.items():check('4/response/'+str(i)+'/'+c,r[c],v,'readout')
    cells=read('B20_4_stageA_accessibility_24cells.csv');secants=read('B20_4_stageA_directional_secants.csv');brackets=read('B20_4_stageA_strict_brackets.csv')
    for _,r in cells.iterrows():
        g=response[(response.ray_label==r.ray_label)&np.isclose(response['T'],r['T'])].sort_values('epsilon');x,y=g.epsilon.to_numpy(),g.F.to_numpy();dy=np.diff(y)/np.diff(x);d2=np.diff(dy)/((x[2:]-x[:-2])/2);strict=np.where(y[:-1]*y[1:]<0)[0]
        edge=y[-1]*dy[-1];label='acquired' if len(strict) else ('tangential_or_unresolved' if not np.isfinite(edge) or dy[-1]==0 or y[-1]==0 else 'approaching_nonacquired' if edge<0 else 'receding_nonacquired')
        vals={'access_class':label,'acquired_strict':len(strict)>0,'n_strict_brackets':len(strict),'exact_zero_sample':bool(np.any(y==0)),'response_gap_g':min(abs(y)),'gap_epsilon':x[np.argmin(abs(y))],'F_epsilon_min':y[0],'F_epsilon_max':y[-1],'D_epsilon_F_edge':dy[-1],'D2_epsilon_F_edge':d2[-1],'F_edge_times_D_edge':edge,'D2_used_for_classification':False}
        tag=r.ray_label+'/'+str(r['T'])
        for c,v in vals.items():check('4/access/'+tag+'/'+c,r[c],v,'classification')
        s=secants[(secants.ray_label==r.ray_label)&np.isclose(secants['T'],r['T'])]
        check('4/secants/'+tag+'/first',s[s.order==1].sort_values('i').D_epsilon_F,dy,'secants')
        check('4/secants/'+tag+'/second',s[s.order==2].sort_values('i').D2_epsilon_F,d2,'secants')
        z=brackets[(brackets.ray_label==r.ray_label)&np.isclose(brackets['T'],r['T'])].sort_values('epsilon_lo')
        for c,v in {'epsilon_lo':x[strict],'epsilon_hi':x[strict+1],'F_lo':y[strict],'F_hi':y[strict+1]}.items():check('4/brackets/'+tag+'/'+c,z[c],v,'bracket_recompute')
    hist=pd.read_csv(raw/'B20_4_stageB_refinement/B20_4_stageB_REFINEMENT_HISTORY.csv');initial=read('B20_4_stageB_INITIAL_19_brackets_FROZEN.csv');final=read('B20_4_stageB_FINAL_19_refined_brackets.csv')
    for _,r in initial.iterrows():
        lo,hi,flo,fhi=r.epsilon_lo,r.epsilon_hi,r.F_lo,r.F_hi;h=hist[hist.stageB_bracket_id==r.stageB_bracket_id].sort_values('level')
        check('4/refine/'+r.stageB_bracket_id+'/levels',len(h),6,'bracket_recompute')
        for _,q in h.iterrows():
            mid=(lo+hi)/2;d=history_index[('B20_4_stageB_refinement',r.ray_label,round(mid,12))];fm=at_time(d,r['T']).delta_enstrophy;tag=r.stageB_bracket_id+'/'+str(q.level)
            for c,v in {'epsilon_lo_before':lo,'epsilon_hi_before':hi,'epsilon_mid':mid,'F_lo_before':flo,'F_hi_before':fhi,'F_mid':fm,'width_before':hi-lo}.items():check('4/refine/'+tag+'/'+c,q[c],v,'bracket_recompute')
            if flo*fm>0:lo,flo=mid,fm
            else:hi,fhi=mid,fm
            for c,v in {'epsilon_lo_after':lo,'epsilon_hi_after':hi,'F_lo_after':flo,'F_hi_after':fhi,'width_after':hi-lo}.items():check('4/refine/'+tag+'/'+c,q[c],v,'bracket_recompute')
        f=final[final.stageB_bracket_id==r.stageB_bracket_id].iloc[0]
        for c,v in {'epsilon_lo':lo,'epsilon_hi':hi,'F_lo':flo,'F_hi':fhi,'width':hi-lo,'epsilon_midpoint':(lo+hi)/2}.items():check('4/final/'+r.stageB_bracket_id+'/'+c,f[c],v,'headline_recompute')
    check('4/formal_verdict',js('B20_4_FINAL_VERDICT.json')['verdict'],'PASS','retained_verdict')

    # B20.5: reconstruct normalized geometry and all 64 finite differences.
    basis=read('B20_5_normalized_subspace_basis.csv');Q=basis.iloc[:,1:].to_numpy(float)
    scale=np.sqrt(np.mean(np.array([[declaration['endpoints'][r][k]-declaration['base'][k] for k in PARAMS] for r in ['r09','r10','r11','r12']])**2,axis=0))
    check('5/basis_orthonormal',Q.T@Q,np.eye(4),'geometry')
    anchors=read('B20_5_frozen_boundary_anchors.csv');pert=read('B20_5_frozen_gradient_perturbations_64.csv');inventory=read('B20_5_STAGEA_TRAJECTORY_INVENTORY.csv')
    for i,r in pert.iterrows():
        a=anchors[anchors.anchor_id==r.anchor_id].iloc[0]
        expected=a[PARAMS].to_numpy(float)+r['sign']*r.h*scale*Q[:,int(r.basis_direction)-1]
        check('5/perturbation/'+str(i),r[PARAMS].to_numpy(float),expected,'geometry')
    for i,r in inventory.iterrows():
        d=get_ts('B20_5_stageA_prospective/trajectory_cache',r.trajectory_id);check('5/gradient_raw/'+str(i),r.F_observe,at_time(d,r['T']).delta_enstrophy,'readout')
    gradients=read('B20_5_STAGEA_GRADIENTS_8.csv');G={}
    for _,r in gradients.iterrows():
        g=inventory[(inventory.anchor_id==r.anchor_id)&(inventory.h_label==r.h_label)];values=[]
        for k in range(1,5):
            q=g[g.basis_direction==k].set_index('sign');values.append((q.loc[1].F_observe-q.loc[-1].F_observe)/(2*r.h))
        v=np.array(values);norm=np.linalg.norm(v);G[(r.anchor_id,r.h_label)]=v
        check('5/gradient/'+r.anchor_id+'/'+r.h_label,r[[f'dF_dq{k}' for k in range(1,5)]].to_numpy(float),v,'gradient_recompute')
        check('5/normal/'+r.anchor_id+'/'+r.h_label,r[[f'normal_q{k}' for k in range(1,5)]].to_numpy(float),v/norm,'gradient_recompute')
        check('5/gradient_norm/'+r.anchor_id+'/'+r.h_label,r.gradient_norm,norm,'gradient_recompute')
    consistency=read('B20_5_STAGEA_CROSS_SCALE_NORMAL_CONSISTENCY.csv')
    for _,r in consistency.iterrows():
        a,c=G[(r.anchor_id,'h1')],G[(r.anchor_id,'h2')];n1,n2=np.linalg.norm(a),np.linalg.norm(c);dot=np.dot(a/n1,c/n2);angle=np.degrees(np.arccos(np.clip(dot,-1,1)))
        for col,val in {'gradient_norm_h1':n1,'gradient_norm_h2':n2,'norm_ratio_h2_over_h1':n2/n1,'signed_normal_dot':dot}.items():check('5/cross_scale/'+r.anchor_id+'/'+col,r[col],val,'gradient_recompute')
        check('5/cross_scale/'+r.anchor_id+'/angle',r.normal_angle_deg,angle,'gradient_recompute',atol=1e-7)
    centers=read('B20_5_CENTER_RESULTS_4.csv');Fc={}
    for _,r in centers.iterrows():
        d=get_ts('B20_5_center_acquisition/trajectory_cache','B20_5_center_'+r.anchor_id);Fc[r.anchor_id]=at_time(d,r.T_observe).delta_enstrophy;check('5/center/'+r.anchor_id,r.Fc,Fc[r.anchor_id],'readout')
    holdout=read('B20_5_holdout_directions.csv');coeffs={r.holdout_id:Q.T@r[[f'normalized_direction_{k}' for k in PARAMS]].to_numpy(float) for _,r in holdout.iterrows()}
    predictions=read('B20_5_HOLDOUT_PAIR_PREDICTIONS_24_FROZEN.csv')
    for i,r in predictions.iterrows():
        v=G[(r.anchor_id,'h1' if np.isclose(r.h,1/32) else 'h2')];dv=np.dot(v,coeffs[r.holdout_id]);fc=Fc[r.anchor_id]
        for col,val in {'Fc':fc,'D_pred':dv,'predicted_derivative_sign':np.sign(dv),'F_pred_minus':fc-r.h*dv,'F_pred_plus':fc+r.h*dv}.items():check('5/frozen_prediction/'+str(i)+'/'+col,r[col],val,'prediction_recompute')
    obs=read('B20_5_HOLDOUT_RAW_RESULTS_48.csv')
    for i,r in obs.iterrows():
        d=get_ts('B20_5_holdout_prospective/trajectory_cache',r.case_id);q=at_time(d,r.T_observe);check('5/holdout_raw/'+str(i),r.F_obs,q.delta_enstrophy,'readout')
    ev=read('B20_5_PRIMARY_DERIVATIVE_EVALUATION_24.csv');cross=read('B20_5_CROSS_SCALE_HOLDOUT_12.csv')
    recomputed=[]
    for i,r in ev.iterrows():
        pair=obs[(obs.anchor_id==r.anchor_id)&(obs.holdout_id==r.holdout_id)&np.isclose(obs.h,r.h)].set_index('sign_label');a,c=pair.loc['minus'],pair.loc['plus'];dv=(c.F_obs-a.F_obs)/(2*r.h);pred=c.D_pred
        vals={'D_obs':dv,'D_pred':pred,'derivative_error':dv-pred,'abs_derivative_error':abs(dv-pred),'relative_derivative_error':abs(dv-pred)/abs(pred),'D_obs_over_D_pred':dv/pred,'derivative_sign_pred':np.sign(pred),'derivative_sign_obs':np.sign(dv),'derivative_sign_agree':np.sign(pred)==np.sign(dv),'F_minus_pred':a.F_pred,'F_minus_obs':a.F_obs,'F_minus_residual':a.F_obs-a.F_pred,'F_minus_sign_agree':np.sign(a.F_pred)==np.sign(a.F_obs),'F_plus_pred':c.F_pred,'F_plus_obs':c.F_obs,'F_plus_residual':c.F_obs-c.F_pred,'F_plus_sign_agree':np.sign(c.F_pred)==np.sign(c.F_obs)}
        for col,val in vals.items():check('5/primary/'+str(i)+'/'+col,r[col],val,'headline_recompute')
        recomputed.append(vals)
    for i,r in cross.iterrows():
        g=ev[(ev.anchor_id==r.anchor_id)&(ev.holdout_id==r.holdout_id)].set_index('h_label');a,c=g.loc['h32'].D_obs,g.loc['h64'].D_obs
        for col,val in {'D_obs_h32':a,'D_obs_h64':c,'cross_scale_sign_agree':np.sign(a)==np.sign(c),'cross_scale_abs_difference':abs(a-c),'cross_scale_relative_difference':abs(a-c)/max(abs(a),abs(c))}.items():check('5/holdout_cross/'+str(i)+'/'+col,r[col],val,'headline_recompute')
    closure=js('B20_5_FINAL_SCIENTIFIC_CLOSURE.json');errors=np.array([r['relative_derivative_error'] for r in recomputed]);res=obs.F_obs-obs.F_pred
    for col,val in {'median_relative_derivative_error':np.median(errors),'max_relative_derivative_error':max(errors),'mean_relative_derivative_error':np.mean(errors)}.items():check('5/closure/'+col,closure['primary_results'][col],val,'headline_recompute')
    secondary=closure['secondary_results']
    for col,val in {'raw_F_MAE':np.mean(abs(res)),'raw_F_RMSE':np.sqrt(np.mean(res**2)),'raw_F_correlation':np.corrcoef(obs.F_pred,obs.F_obs)[0,1],'raw_F_sign_disagreements':sum(np.sign(obs.F_pred)!=np.sign(obs.F_obs))}.items():check('5/closure/'+col,secondary[col],val,'headline_recompute')
    check('5/primary_sign_count',sum(r['derivative_sign_agree'] for r in recomputed),24,'headline_recompute')
    check('5/raw_sign_count',sum(np.sign(obs.F_pred)==np.sign(obs.F_obs)),47,'headline_recompute')
    check('5/formal_verdict',closure['scientific_verdict'],'PASS','retained_verdict')

    # B20.6: affine geometry, local saved data and the frozen extrapolation.
    phase=raw/'B20_6_crossing_geometry/PHASE2A_LOCAL_INFORMATION_PROSPECTIVE_RESTART'
    geometry=raw/'B20_6_crossing_geometry/PHASE1B_FAMILY_D_GEOMETRY_FROZEN'
    base=pd.read_csv(geometry/'B20_6_FAMILY_D_BASE_FROZEN.csv').iloc[0]
    directions=pd.read_csv(geometry/'B20_6_FAMILY_D_TRAJECTORIES_6_FROZEN.csv');direction={r.trajectory:r[[f'direction_{k}' for k in PARAMS]].to_numpy(float) for _,r in directions.iterrows()}
    coeff=directions[[f'coeff_q{k}' for k in range(1,5)]].to_numpy(float)
    check('6/direction_rank',np.linalg.matrix_rank(coeff),4,'geometry')
    check('6/unit_coefficients',np.linalg.norm(coeff,axis=1),np.ones(6),'geometry')
    check('6/raw_directions',np.array(list(direction.values())),(Q@coeff.T).T*scale,'geometry')
    check('6/base',base[PARAMS].to_numpy(float),anchors[PARAMS].mean().to_numpy()+scale*(Q@np.array([.31,-.27,.19,.23])),'geometry')
    manifest=read('B20_6_LOCAL_MANIFEST_FROZEN_30.csv');frozen=js('BIG_B20_6_CROSSING_PREDICTION_FREEZE.json');prediction=read('BIG_B20_6_CROSSING_PREDICTIONS_FROZEN.csv');local={}
    # The restart explicitly used a six-decimal Qw and twelve-decimal base.
    # Verify its ACTUAL frozen manifest, while reporting the earlier full-precision
    # difference separately rather than weakening this comparison's tolerance.
    actual_direction={r.trajectory:scale*(np.round(Q,6)@r[[f'coeff_q{k}' for k in range(1,5)]].to_numpy(float)) for _,r in directions.iterrows()}
    for i,r in manifest.iterrows():
        check('6/local_geometry/'+str(i),r[PARAMS].to_numpy(float),np.round(base[PARAMS].to_numpy(float),12)+r.s*actual_direction[r.trajectory],'geometry')
        p=phase/'trajectory_cache'/(r.case_id+'.json');j=json.loads(p.read_text());local[(r.trajectory,r.point_label)]=j['F_DeltaZ'];d=pd.read_csv(p.parent/j['timeseries_file'])
        check('6/local_checkpoint/'+r.case_id,j['F_DeltaZ'],at_time(d,r['T']).delta_enstrophy,'readout')
        check('6/local_hash/'+r.case_id,hashlib.sha256(p.read_bytes()).hexdigest(),frozen['phase2a_checkpoint_sha256'][r.case_id],'frozen_lineage')
        check('6/local_series_hash/'+r.case_id,hashlib.sha256((p.parent/j['timeseries_file']).read_bytes()).hexdigest(),j['timeseries_sha256'],'frozen_lineage')
    check('6/local_same_side',min(local.values())>0,True,'geometry')
    for i,r in prediction.iterrows():
        fc=local[(r.trajectory,'center')]
        for htag in ['h1','h2']:
            h=r[htag];fm=local[(r.trajectory,htag+'_minus')];fp=local[(r.trajectory,htag+'_plus')];dv=(fp-fm)/(2*h);shat=r.s0-fc/dv
            for col,val in {'F0':fc,'F_'+htag+'_minus':fm,'F_'+htag+'_plus':fp,'Dv_'+htag:dv,'shat_'+htag:shat,'shat_'+htag+'_in_frozen_domain':-.5<=shat<=2}.items():check('6/frozen_prediction/'+str(i)+'/'+col,r[col],val,'prediction_recompute')
        check('6/primary/'+str(i),r.primary_shat,r.shat_h2,'prediction_recompute')
    check('6/only_one_predicted_in_domain',sum(prediction.primary_shat_in_frozen_domain),1,'headline_recompute')
    scan=read('BIG_B20_6_COARSE_RESPONSE_TABLE.csv');scanroot=phase/'PHASE2C_FROZEN_COARSE_CROSSING_SCAN';cache={}
    scan_manifest=pd.read_csv(scanroot/'BIG_B20_6_COARSE_SCAN_MANIFEST.csv')
    for i,r in scan_manifest.iterrows():
        check('6/scan_geometry/'+str(i),r[PARAMS].to_numpy(float),np.round(base[PARAMS].to_numpy(float),12)+r.s*actual_direction[r.trajectory],'geometry')
    for p in (scanroot/'trajectory_cache').glob('*.json'):
        j=json.loads(p.read_text())
        if 'trajectory' in j and 's' in j and 'F_DeltaZ' in j:cache[(j['trajectory'],round(j['s'],12))]=j
    for i,r in scan.iterrows():
        j=cache[(r.trajectory,round(r.s,12))];check('6/scan_checkpoint/'+str(i),r.F_DeltaZ,j['F_DeltaZ'],'readout')
        if 'timeseries_file' in j:
            ts=scanroot/'trajectory_cache'/j['timeseries_file'];expected_hash=j['timeseries_sha256']
        else:
            ts=phase/'trajectory_cache'/Path(j['source_timeseries_path']).name;expected_hash=j['source_timeseries_sha256']
        d=pd.read_csv(ts);check('6/scan_timeseries/'+str(i),r.F_DeltaZ,d.delta_enstrophy.iloc[-1],'readout')
        check('6/scan_series_hash/'+str(i),hashlib.sha256(ts.read_bytes()).hexdigest(),expected_hash,'frozen_lineage')
    common=scan[np.isclose(scan.s,0)].F_DeltaZ.to_numpy()
    check('6/common_base_samples',common,np.full(6,common[0]),'lineage')
    check('6/local_center_reuse_count',sum(scan.source=='REUSED_PHASE2A_CENTER'),6,'lineage')
    detected=[]
    for trajectory,g in scan.groupby('trajectory'):
        g=g.sort_values('s');x,y=g.s.to_numpy(),g.F_DeltaZ.to_numpy();check('6/grid/'+trajectory,x,np.linspace(-.5,2,21),'coverage')
        for i in np.where(y[:-1]*y[1:]<0)[0]:detected.append((trajectory,x[i],x[i+1],y[i],y[i+1]))
    brackets6=read('BIG_B20_6_COARSE_BRACKETS_DETECTED.csv');check('6/crossing_count',len(detected),1,'headline_recompute')
    for i,(trajectory,lo,hi,flo,fhi) in enumerate(detected):
        r=brackets6.iloc[i]
        for col,val in {'trajectory':trajectory,'s_left':lo,'s_right':hi,'F_left':flo,'F_right':fhi}.items():check('6/coarse_bracket/'+col,r[col],val,'bracket_recompute')
    lo,hi,flo,fhi=detected[0][1:];history6=read('BIG_B20_6_REFINEMENT_HISTORY.csv');refinecache=scanroot/'PHASE2D_FROZEN_BRACKET_REFINEMENT/trajectory_cache';values={}
    for p in refinecache.glob('*.json'):
        j=json.loads(p.read_text())
        if 'F_DeltaZ' in j and 's' in j:values[round(j['s'],12)]=j['F_DeltaZ']
    for _,r in history6.sort_values('iteration').iterrows():
        mid=(lo+hi)/2;fm=values[round(mid,12)]
        for col,val in {'left_before':lo,'right_before':hi,'mid':mid,'F_left_before':flo,'F_right_before':fhi,'F_mid':fm}.items():check('6/refinement/'+str(r.iteration)+'/'+col,r[col],val,'bracket_recompute')
        if flo*fm>0:lo,flo=mid,fm
        else:hi,fhi=mid,fm
    final6=js('BIG_B20_6_REFINED_BRACKET_FINAL.json');pred=prediction[prediction.trajectory=='d03'].shat_h2.iloc[0];mid=(lo+hi)/2
    for col,val in {'final_left':lo,'final_right':hi,'final_width':hi-lo,'final_F_left':flo,'final_F_right':fhi,'refined_midpoint':mid,'frozen_prediction_s_hat':pred,'prediction_minus_refined_midpoint':pred-mid,'prediction_inside_final_bracket':lo<=pred<=hi}.items():check('6/final/'+col,final6[col],val,'headline_recompute')
    check('6/prediction_orientation',np.sign(prediction[prediction.trajectory=='d03'].Dv_h2.iloc[0]),np.sign(fhi-flo),'headline_recompute')
    check('6/frozen_prediction_hash',hashlib.sha256(public_path('BIG_B20_6_CROSSING_PREDICTIONS_FROZEN.csv').read_bytes()).hexdigest(),frozen['prediction_csv_sha256'],'frozen_lineage')
    check('6/formal_verdict',read('BIG_B20_CLAIM_LEDGER.csv').iloc[2].verdict,'INCONCLUSIVE','retained_verdict')
    return {'status':'PASS' if all(r['status']=='PASS' for r in records) else 'FAIL','scope':'Saved data, frozen geometry and derived numerical checks only; no new ODE/PDE trajectories','independent_full_rerun_audit':'NOT_COMPLETED','check_groups':len(records),'numeric_or_label_comparisons':sum(r['values'] for r in records),'saved_history_files_checked':history_count,'saved_history_rows_including_copies':history_rows,'failed_checks':[r for r in records if r['status']!='PASS'],'records':records}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);p.add_argument('--output',type=Path);a=p.parse_args();result=verify(a.root)
    out=a.output or a.root/'audit/B20_Saved_Result_Verification.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2));raise SystemExit(0 if result['status']=='PASS' else 1)
