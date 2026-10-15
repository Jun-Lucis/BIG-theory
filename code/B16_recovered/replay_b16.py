"""Local I/O adapter for recovered B16 notebooks; defaults to definitions only."""
from pathlib import Path
import argparse,json,os
os.environ.setdefault('MPLBACKEND','Agg')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
HERE=Path(__file__).resolve().parent
STAGES=['core','intervention','locality','moving','robustness']

def load_definitions(output_dir):
    result={}
    for stage in STAGES:
        target=Path(output_dir)/stage
        def convert(obj):
            if isinstance(obj,dict):return {str(k):convert(v) for k,v in obj.items()}
            if isinstance(obj,(tuple,list)):return [convert(v) for v in obj]
            if isinstance(obj,np.ndarray):return obj.tolist()
            if isinstance(obj,np.generic):return obj.item()
            return obj
        def save_csv(df,name,_dir=target):
            _dir.mkdir(parents=True,exist_ok=True);p=_dir/name;df.to_csv(p,index=False);return p
        def save_json(obj,name,_dir=target):
            _dir.mkdir(parents=True,exist_ok=True);p=_dir/name;p.write_text(json.dumps(convert(obj),indent=2,ensure_ascii=False)+'\n');return p
        def save_figure(name,dpi=180,_dir=target):
            _dir.mkdir(parents=True,exist_ok=True);p=_dir/name;plt.tight_layout();plt.savefig(p,dpi=dpi);plt.close();return p
        ns={'np':np,'pd':pd,'plt':plt,'Path':Path,'json':json,'display':print,'OUTDIR':target,
            'save_csv':save_csv,'save_json':save_json,'save_figure':save_figure,'to_jsonable':convert}
        p=HERE/'recovered_code'/f'{stage}_functions.py'
        exec(compile(p.read_text(),str(p),'exec'),ns);result[stage]=ns
    return result

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--mode',choices=['definitions','full-run'],default='definitions')
    ap.add_argument('--stage',choices=['all',*STAGES],default='all')
    ap.add_argument('--output',type=Path,default=Path('b16_replay_output'))
    args=ap.parse_args();ns=load_definitions(args.output)
    if args.mode=='definitions':print('12 computational definitions loaded in five namespaces; no PDE run executed.');return
    cells=json.loads((HERE/'recovered_code/original_execution_cells.json').read_text())
    for stage in STAGES if args.stage=='all' else [args.stage]:
        for cell in cells[stage]:
            exec(compile(cell['source'],f'original_B16_{stage}_cell_{cell["cell_index_zero_based"]}','exec'),ns[stage])
    print('Explicit original numerical workflow completed with local output paths.')

if __name__=='__main__':main()
