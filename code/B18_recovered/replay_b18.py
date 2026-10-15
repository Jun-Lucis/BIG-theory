"""Portable B18 adapter. Default: load definitions only. Full runs require explicit opt-in."""
from pathlib import Path
import argparse,json,contextlib,io,shutil,zipfile
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
HERE=Path(__file__).resolve().parent
def load_definitions():
    stages={}
    for stage in range(5):
        ns={'np':np,'pd':pd,'plt':plt,'Path':Path}
        p=HERE/'recovered_code'/f'stage{stage}_functions.py'
        exec(compile(p.read_text(),str(p),'exec'),ns)
        stages[stage]=ns
    return stages
def run_stage(stage,output,source_dir):
    out=Path(output);out.mkdir(parents=True,exist_ok=True)
    ns=load_definitions()[stage];ns.update(OUTDIR=out,display=lambda *a,**k:None,json=json,shutil=shutil,zipfile=zipfile)
    def save_csv(df,name):p=out/name;df.to_csv(p,index=False);return p
    def save_json(obj,name):p=out/name;p.write_text(json.dumps(obj,indent=2,default=lambda v:v.item() if isinstance(v,np.generic) else v.tolist() if isinstance(v,np.ndarray) else str(v)));return p
    def save_figure(name,dpi=180):p=out/name;plt.tight_layout();plt.savefig(p,dpi=dpi);plt.close();return p
    ns.update(save_csv=save_csv,save_json=save_json,save_figure=save_figure,save_text=lambda text,name:(out/name).write_text(text),backup_to_drive=lambda p:None)
    cells=json.loads((HERE/'recovered_code/original_execution_cells.json').read_text())[str(stage)]
    if stage<4:
        first=4 if stage==0 else 5
        selected=[c for c in cells if first<=c['cell_index_zero_based']<cells[-1]['cell_index_zero_based']]
    else:
        # Read original saved CSVs strictly. Original Colab file discovery and silent fallback are replaced.
        d=Path(source_dir);required=['B18_0_rd_front_inhibitor_trace_metrics.csv','B18_1_read_path_integrated_load_metrics.csv','B18_2_active_front_weighted_readout_metrics.csv','B18_3_operator_ranking.csv']
        for name in required:
            if not (d/name).is_file():raise FileNotFoundError(d/name)
        ns['loaded']={f'B18_{s}':{p.name:pd.read_csv(p) for p in d.glob(f'B18_{s}_*.csv')} for s in range(4)}
        selected=[c for c in cells if 5<=c['cell_index_zero_based']<cells[-1]['cell_index_zero_based']]
    for c in selected:
        exec(compile(c['source'],f'original_stage{stage}_cell{c["cell_index_zero_based"]}','exec'),ns)
    return {'stage':stage,'mode':'full-run' if stage<4 else 'saved-input-synthesis','original_cells_executed':[c['cell_index_zero_based'] for c in selected],'pde_run':stage<4}
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--mode',choices=['definitions','full-run'],default='definitions');ap.add_argument('--stage',choices=['0','1','2','3','4','all'],default='all');ap.add_argument('--output',type=Path);ap.add_argument('--source-dir',type=Path,default=HERE.parent/'sources/drive_run');a=ap.parse_args()
    if a.mode=='definitions':
        n=load_definitions();print(json.dumps({'mode':'definitions','loaded_namespaces':len(n),'new_PDE_trajectories':0}));return
    if a.output is None:ap.error('--output is required for full-run')
    if a.output.exists() and any(a.output.iterdir()):ap.error('--output must be new or empty')
    stages=range(5) if a.stage=='all' else [int(a.stage)]
    receipts=[run_stage(s,a.output/f'stage{s}',a.source_dir) for s in stages]
    (a.output/'execution_receipt.json').write_text(json.dumps(receipts,indent=2)+'\n')
if __name__=='__main__':main()
