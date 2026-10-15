"""Load unchanged B17 definitions, or explicitly regenerate local outputs."""
from pathlib import Path
import argparse, ast, json, shutil, zipfile
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parent
CELLS=json.loads((ROOT/'recovered_code/original_execution_cells.json').read_text())

def namespace(stage):
    env={'np':np,'pd':pd,'Path':Path,'plt':plt,'json':json,'shutil':shutil,'zipfile':zipfile,'display':lambda *a,**k:None}
    # Only original pure grid/parameter assignments; no experiment or file access.
    names={'N','XMIN','XMAX','x','dx','BASE','DEFAULT','PROTOCOLS'}
    for code in CELLS[str(stage)].values():
        tree=ast.parse(code)
        for node in tree.body:
            if isinstance(node,ast.Assign):
                assigned={n.id for target in node.targets for n in ast.walk(target) if isinstance(n,ast.Name)}
                if assigned and assigned<=names:
                    exec(compile(ast.Module(body=[node],type_ignores=[]),'original_parameter_assignment','exec'),env)
    exec((ROOT/f'recovered_code/stage{stage}_functions.py').read_text(),env)
    for node in ast.parse(CELLS[str(stage)]['1']).body:
        if isinstance(node,ast.FunctionDef) and node.name=='to_jsonable':
            exec(compile(ast.Module(body=[node],type_ignores=[]),'original_json_conversion','exec'),env)
    return env

def full(stage,out,inputs):
    env=namespace(stage);out.mkdir(parents=True,exist_ok=True)
    env.update(OUTDIR=out,BACKUP_DIR=out,backup_to_drive=lambda p:None)
    def save_csv(df,name):
        p=out/name;df.to_csv(p,index=False);return p
    def save_json(data,name):
        p=out/name;p.write_text(json.dumps(env['to_jsonable'](data),ensure_ascii=False,indent=2));return p
    def save_figure(name,dpi=180):
        p=out/name;plt.tight_layout();plt.savefig(p,dpi=dpi);plt.close();return p
    env.update(save_csv=save_csv,save_json=save_json,save_figure=save_figure)
    if stage==2:
        required={'pair':'B17_1_write_read_pair_metrics.csv','state':'B17_1_write_branch_state_metrics.csv','diagnostics':'B17_1_write_read_diagnostics.csv','summary':'B17_1_write_read_separation_summary.json'}
        paths={k:inputs/v for k,v in required.items()}
        for k in ['pair','state']:
            if not paths[k].is_file():raise FileNotFoundError(paths[k])
        env.update(paths=paths,pair_df=pd.read_csv(paths['pair']),state_df=pd.read_csv(paths['state']),diag_prev_df=pd.read_csv(paths['diagnostics']) if paths['diagnostics'].exists() else pd.DataFrame(),summary_prev=json.loads(paths['summary'].read_text()) if paths['summary'].exists() else None)
    # Setup/mount and original archive/export cells are replaced by local I/O.
    for ci,code in CELLS[str(stage)].items():
        if int(ci)<2 or int(ci)==max(map(int,CELLS[str(stage)])) or (stage==2 and int(ci)==2):continue
        exec(compile(code,f'original_B17_{stage}_cell_{ci}','exec'),env)

def main():
    p=argparse.ArgumentParser();p.add_argument('--mode',choices=['definitions','full-run'],default='definitions');p.add_argument('--stage',choices=['0','1','2','3','4','all'],default='all');p.add_argument('--output',type=Path);p.add_argument('--inputs',type=Path,default=ROOT.parent/'sources/drive_run');a=p.parse_args()
    stages=range(5) if a.stage=='all' else [int(a.stage)]
    if a.mode=='definitions':
        for stage in stages:namespace(stage)
        print('Loaded original computational definitions in separate namespaces; no dynamics steps executed.');return
    if a.output is None:p.error('--output is required for numerical regeneration')
    if a.output.exists() and any(a.output.iterdir()):p.error('--output must be empty or new')
    for stage in stages:
        inputs=a.output/'stage1' if a.stage=='all' and stage==2 else a.inputs
        full(stage,a.output/f'stage{stage}',inputs)

if __name__=='__main__':main()
