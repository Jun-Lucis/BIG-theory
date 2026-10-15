"""Portable I/O adapter for recovered B14 computational definitions. No experiment runs on import."""
from pathlib import Path
import argparse,json,os
os.environ.setdefault('MPLBACKEND','Agg')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
HERE=Path(__file__).resolve().parent

def load_definitions(output_dir):
    output_dir=Path(output_dir);output_dir.mkdir(parents=True,exist_ok=True)
    def save_csv_local(df,name):
        p=output_dir/name;df.to_csv(p,index=False);return p
    def save_json_local(obj,name):
        p=output_dir/name;p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n');return p
    def save_fig_local(name):
        p=output_dir/name;plt.tight_layout();plt.savefig(p,dpi=180);plt.close();return p
    ns={'np':np,'pd':pd,'plt':plt,'json':json,'Path':Path,'display':print,'OUTDIR':output_dir,
        'BACKUP_DIR':None,'save_csv_local':save_csv_local,'save_json_local':save_json_local,
        'save_fig_local':save_fig_local}
    stages=json.loads((HERE/'recovered_code/original_stage_calls.json').read_text())
    for stage in stages:
        p=HERE/'recovered_code'/stage['definitions'];exec(compile(p.read_text(),str(p),'exec'),ns)
    return ns,stages

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--mode',choices=['definitions','full-run'],default='definitions')
    ap.add_argument('--output',type=Path,default=Path('b14_replay_output'))
    args=ap.parse_args();ns,stages=load_definitions(args.output)
    if args.mode=='definitions':
        print('Definitions loaded; no simulation executed.');return
    for stage in stages:
        if stage['superseded_unstable_attempt']:
            continue
        p=HERE/'recovered_code'/stage['definitions'];exec(compile(p.read_text(),str(p),'exec'),ns)
        for call in stage['original_calls']:exec(compile(call,f"original_cell_{stage['cell_index_zero_based']}_call",'exec'),ns)
    print('Completed the stable-paper workflow. The superseded unstable fusion attempt was skipped.')

if __name__=='__main__':main()
