"""Portable adapter for the recovered B13.1 notebook. Importing this file starts no experiment."""
from pathlib import Path
import argparse
import json
import os
os.environ.setdefault("MPLBACKEND", "Agg")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.polynomial.hermite import hermgauss
from scipy.optimize import curve_fit

HERE = Path(__file__).resolve().parent

def load_definitions(output_dir):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    def save_csv_local(df, name):
        path = output_dir / name
        df.to_csv(path, index=False)
        return path
    def save_json_local(obj, name):
        path = output_dir / name
        path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")
        return path
    def save_fig_local(name):
        path = output_dir / name
        plt.tight_layout()
        plt.savefig(path, dpi=180)
        plt.close()
        return path
    ns = {"np": np, "pd": pd, "plt": plt, "json": json, "Path": Path,
          "hermgauss": hermgauss, "curve_fit": curve_fit, "SCIPY_AVAILABLE": True,
          "display": print, "OUTDIR": output_dir, "BACKUP_DIR": None,
          "save_csv_local": save_csv_local, "save_json_local": save_json_local,
          "save_fig_local": save_fig_local}
    stages = json.loads((HERE / "recovered_code/original_stage_calls.json").read_text())
    for stage in stages:
        p = HERE / "recovered_code" / stage["definitions"]
        exec(compile(p.read_text(), str(p), "exec"), ns)
    return ns, stages

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--mode", choices=["definitions", "saved-analysis", "full-run"], default="definitions")
    ap.add_argument("--data", type=Path)
    ap.add_argument("--output", type=Path, default=Path("b131_replay_output"))
    args = ap.parse_args()
    ns, stages = load_definitions(args.output)
    if args.mode == "definitions":
        print("Computational definitions loaded. No experiment or stored-data analysis executed.")
        return
    if args.mode == "saved-analysis":
        if args.data is None:
            ap.error("--data must identify the original package data/ directory")
        for variable, filename in {
            "curves_rot_robust": "A_rotated_basis_robust_curves_all_seeds.csv",
            "collapse_points": "A_rotated_basis_collapse_all_points.csv",
            "collapse_binned": "A_rotated_basis_collapse_by_delta_bin.csv",
            "B13_2_summary": "B13_2_kernel_scaling_summary.csv",
            "B13_3b_agg": "B13_3b_sequential_reset_comparison_by_delta.csv",
            "B13_3b_cloud": "B13_3b_stage1_cloud_diagnostics.csv",
            "B13_3_seq_robust_agg": "B13_3_sequential_robust_by_delta.csv",
            "B13_3c_by_width_delta": "B13_3c_cloud_width_summary_by_width_delta.csv",
        }.items():
            ns[variable] = pd.read_csv(args.data / filename)
        ns["B13_3c_summary"] = json.loads((args.data / "B13_3c_cloud_width_summary.json").read_text())
    for stage in stages:
        # Reload in the original order, including the repeated logistic definition.
        p = HERE / "recovered_code" / stage["definitions"]
        exec(compile(p.read_text(), str(p), "exec"), ns)
        if args.mode == "saved-analysis" and stage["stochastic"]:
            continue
        if args.mode == "saved-analysis" and stage["cell_index_zero_based"] == 4:
            # Use the recorded bins. Recomputing ties after CSV roundtrip can
            # move values between adjacent five-degree bins; see the audit note.
            continue
        for call in stage["original_calls"]:
            exec(compile(call, f"original_cell_{stage['cell_index_zero_based']}_call", "exec"), ns)
    print("Completed mode:", args.mode)

if __name__ == "__main__":
    main()
