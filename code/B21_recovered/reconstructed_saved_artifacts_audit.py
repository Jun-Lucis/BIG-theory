#!/usr/bin/env python3
"""Independent saved-artifact consistency checks only; no PDE rerun, no verdict change.

Uses fixed B21 recovered ZIP. Hash manifest and scientific result files remain original.
Does not rewrite source files, tolerances, or historical classifications.
"""
import argparse,csv,hashlib,io,json,math,os,zipfile
from collections import Counter
from pathlib import Path


def rows(z,n): return list(csv.DictReader(io.StringIO(z.read(n).decode('utf-8-sig'))))
def j(z,n): return json.loads(z.read(n))
def err(got,want): return abs(float(got)-float(want))

def main(source,out):
 out=Path(out)
 with zipfile.ZipFile(source) as z:
  names=z.namelist();root='BIG_B21_CP27_SOURCE_RECOVERY/'
  times=sorted(n for n in names if n.endswith('timeseries.csv') and n.startswith(root+'sources/drive_run/'))
  failures=[];len_dist=Counter();terminal=Counter();row_cnt=0;value_checks=0
  max_delta=0.;max_balance=0.
  for n in times:
   rr=rows(z,n)
   if not rr:failures.append(f'empty_history:{n}');continue
   len_dist[len(rr)]+=1;row_cnt+=len(rr); t=[float(r['t']) for r in rr]
   if any(not math.isfinite(x) for x in t):failures.append(f'nonfinite_time:{n}')
   if any(b<=a for a,b in zip(t,t[1:])):failures.append(f'nonmonotone_time:{n}')
   if abs(t[0])>1e-14: failures.append(f'nonzero_start:{n}')
   terminal[round(t[-1],6)]+=1
   base=float(rr[0]['enstrophy_half'])
   for i,r in enumerate(rr):
    dz=err(float(r['enstrophy_half'])-base,r['delta_enstrophy'])
    bal=err(float(r['stretch_total'])-float(r['dissipation_total']),r['balance_total'])
    max_delta=max(max_delta,dz);max_balance=max(max_balance,bal)
    if dz>1e-11:failures.append(f'delta:{n}:{i}:{dz}')
    if bal>1e-11:failures.append(f'balance:{n}:{i}:{bal}')
    value_checks+=2
  summaries=sorted(n for n in names if n.endswith('__summary.json') and n.startswith(root+'sources/drive_run/'))
  summary_comps=0;summary_mismatches=[]
  for n in summaries:
   s=j(z,n);p=n[:-len('__summary.json')]+'__timeseries.csv'
   if p not in names: failures.append(f'missing_history_for_summary:{n}');continue
   rr=rows(z,p)
   targets=[(float(s['T_target']),s['F_target'],'F_target')] if 'T_target' in s else [(float(k[3:]),s[k],k) for k in s if k.startswith('F_T')]
   for target,expected,key in targets:
    hits=[r for r in rr if err(r['t'],target)<1e-10]
    if len(hits)!=1:failures.append(f'target_time_resolution:{n}:{key}:{len(hits)}');continue
    val=float(hits[0]['enstrophy_half'])-float(rr[0]['enstrophy_half']);d=err(val,expected)
    if d>1e-11:summary_mismatches.append({'name':n,'field':key,'diff':d})
    summary_comps+=1
  if summary_mismatches:failures+=['summary_F:'+x['name'] for x in summary_mismatches]
  manifests={
   'E10_h1':(root+'sources/drive_run/B21_E10_RUNTIME_PACKAGE/B21_E10_h1_manifest_16_FROZEN.csv',root+'sources/drive_run/B21_E10_h1_local_Hv_acquisition/trajectory_cache/'),
   'E10_h2':(root+'sources/drive_run/B21_E10_h2_local_Hv_acquisition/B21_E10_h2_manifest_16_FROZEN.csv',root+'sources/drive_run/B21_E10_h2_local_Hv_acquisition/trajectory_cache/'),
   'E12_grad':(root+'sources/drive_run/B21_E12_final_local_time_refinement/B21_E12_gradient_manifest_16_FROZEN.csv',root+'sources/drive_run/B21_E12_final_local_time_refinement/gradient_cache/'),
  }
  manifest_checks={}
  for title,(f,folder) in manifests.items():
   rr=rows(z,f);fail=[]
   for r in rr:
    case=r['case_id'];fn=folder+case+'__summary.json'
    if fn not in names:fail.append('missing:'+case);continue
    s=j(z,fn)
    if s['case_id']!=case:fail.append('id:'+case)
    for k in ('q_index','fd_sign','outer_sign'):
     if k in r and k in s and err(r[k],s[k])>0:fail.append(f'{k}:{case}')
    if title=='E12_grad' and err(r['T_target'],s['T_target'])>1e-13:fail.append('T:'+case)
    if 'scientific_params' in s:
     for k in ('R','sep_factor','pair_angle','twist_factor','imbalance','axial_coupling','phase'):
      if k in r and err(r[k],s['scientific_params'][k])>1e-12:fail.append('parameter:'+k+':'+case)
   manifest_checks[title]={'rows':len(rr),'mismatches':fail}
   failures+=[f'manifest:{title}:{s}' for s in fail]
  ep=root+'sources/drive_run/B21_E12_final_local_time_refinement/'
  proto=j(z,ep+'B21_E12_PREDECLARATION_FROZEN.json');final=j(z,ep+'B21_E12_FINAL_RESULT.json');freeze=j(z,ep+'B21_E12_GRADIENT_FREEZE_RECORD.json')
  root_checks=[]
  for T,label in ((0.0115,'minus'),(0.0125,'plus')):
   r=j(z,ep+f'B21_E12_root_result_T{T:.4f}.json')
   hist=rows(z,ep+f'B21_E12_root_history_T{T:.4f}.csv')
   good=all([r['F_left']*r['F_right']<0,err(r['midpoint'],(r['left']+r['right'])/2)<1e-13,err(r['width'],r['right']-r['left'])<1e-13,r['width']<=r['target_width'],len(hist)>=2])
   if not good:failures.append(f'root:{T}')
   root_checks.append({'T':T,'status':'PASS' if good else 'FAIL','width':r['width'],'target_width':r['target_width'],'sign_change':r['F_left']*r['F_right']<0,'history_points':len(hist),'root':r['midpoint']})
   if err(r['midpoint'],final['epsilon_'+label])>1e-13:failures.append(f'final_root:{T}')
   if err(r['midpoint'],freeze[f'T_{label}_root_midpoint'])>1e-13:failures.append(f'freeze_root:{T}')
  if err(final['T_plus']-final['T_minus'],proto['central_difference_total_width'])>1e-13:failures.append('delta_T_disagreement')
  if not proto['root_bracket_extension_allowed'] is False:failures.append('root_bracket_extension')
  result={
   'audit_type':'B21 reconstructed saved-artifact cross-check, NOT an original whole-source verifier',
   'source_archive':os.path.basename(source),
   'source_sha256':hashlib.sha256(Path(source).read_bytes()).hexdigest(),
   'status':'PASS' if not failures else 'FAIL',
   'limitations':'No original PDE trajectory re-integration; no complete method-level independent rerun; no claim of uncertainty-bounded closure; no historical verdict changes.',
   'timeseries':{'files':len(times),'rows':row_cnt,'rows_per_file':dict(sorted(len_dist.items())), 'terminal_T_distribution':dict(sorted(terminal.items())), 'row_algebra_checks':value_checks,'max_abs_enstrophy_delta_error':max_delta,'max_abs_balance_total_error':max_balance},
   'summary_checks':{'paired_summary_count':len(summaries),'compared':summary_comps,'tolerance':1e-11,'mismatches':summary_mismatches},
   'manifest_checks':manifest_checks,'frozen_root_checks':root_checks,'failures':failures[:60]
  }
 out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in result.items() if k not in ('limitations','failures')},ensure_ascii=False,indent=2)); print('fail_count',len(failures));
 return bool(failures)
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('source');parser.add_argument('out');a=parser.parse_args();raise SystemExit(main(a.source,a.out))