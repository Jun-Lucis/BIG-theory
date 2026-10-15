"""Portable adapter for recovered B15 definitions; no experiment runs on import."""
from pathlib import Path
import argparse,json,os
os.environ.setdefault('MPLBACKEND','Agg')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
HERE=Path(__file__).resolve().parent

def load_definitions(output_dir):
    output_dir=Path(output_dir)
    def convert(obj):
        if isinstance(obj,dict):return {str(k):convert(v) for k,v in obj.items()}
        if isinstance(obj,(list,tuple)):return [convert(v) for v in obj]
        if isinstance(obj,np.ndarray):return obj.tolist()
        if isinstance(obj,np.generic):return obj.item()
        return obj
    def save_csv(df,name):
        output_dir.mkdir(parents=True,exist_ok=True);p=output_dir/name;df.to_csv(p,index=False);return p
    def save_json(obj,name):
        output_dir.mkdir(parents=True,exist_ok=True);p=output_dir/name;p.write_text(json.dumps(convert(obj),indent=2,ensure_ascii=False)+'\n');return p
    def save_fig(name,dpi=180):
        output_dir.mkdir(parents=True,exist_ok=True);p=output_dir/name;plt.tight_layout();plt.savefig(p,dpi=dpi);plt.close();return p
    common={'np':np,'pd':pd,'plt':plt,'Path':Path,'json':json,'display':print,'OUTDIR':output_dir,
            'save_csv':save_csv,'save_json':save_json,'save_fig':save_fig,'save_figure':save_fig,'to_jsonable':convert}
    namespaces={}
    for key in ['cloud_kernel','history','maps']:
        p=HERE/'recovered_code'/f'{key}_functions.py';ns=dict(common)
        exec(compile(p.read_text(),str(p),'exec'),ns);namespaces[key]=ns
    return namespaces

def load_history_input(path):
    path=Path(path)
    if not path.is_file():raise FileNotFoundError(f'B14 input required; toy fallback is disabled: {path}')
    d=pd.read_csv(path);mapping={'stimulus_shape':'stimulus_shape','post_write_history':'post_write_memory','final_history':'final_memory'}
    missing={'s',*mapping.values()}-set(d.columns)
    if missing:raise ValueError(f'B14 input columns missing: {sorted(missing)}')
    return d.s.to_numpy(float),{key:d[col].to_numpy(float) for key,col in mapping.items()}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--mode',choices=['definitions','full-run'],default='definitions')
    ap.add_argument('--output',type=Path,default=Path('b15_replay_output'))
    ap.add_argument('--b14-profiles',type=Path,default=HERE.parent/'sources/B14_dependency/B14_0_memory_profiles.csv')
    args=ap.parse_args();ns=load_definitions(args.output)
    if args.mode=='definitions':print('36 definitions loaded in three namespaces; no experiment executed.');return
    grid,profiles=load_history_input(args.b14_profiles)
    statements=json.loads((HERE/'recovered_code/original_stage_statements.json').read_text())
    ns['history'].update({'s':grid,'history_profiles':profiles,'profile_path':args.b14_profiles})
    for stage,key in [('cloud','cloud_kernel'),('kernel','cloud_kernel'),('history','history'),('maps','maps')]:
        exec(compile(statements[stage],f'original_B15_{stage}_statements','exec'),ns[key])
    print('Completed original B15 numerical stages with an explicit archived B14 dependency.')

if __name__=='__main__':main()
