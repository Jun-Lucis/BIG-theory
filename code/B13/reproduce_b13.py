"""Portable output adapter around unchanged recovered B13 functions.

Examples:
  python reproduce_b13.py --stage baseline --output rerun_baseline
  python reproduce_b13.py --stage self --output rerun_self

Runs are intentionally opt-in; importing this file never runs an experiment.
"""
from pathlib import Path
import argparse
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import B13_recovered_functions as core


def configure_output(directory):
    directory = Path(directory).resolve()
    directory.mkdir(parents=True, exist_ok=True)
    core.OUTDIR = directory

    def save_csv(df, filename):
        p = directory / filename
        df.to_csv(p, index=False)
        return p

    def save_json(obj, filename):
        p = directory / filename
        p.write_text(json.dumps(obj, indent=2, ensure_ascii=False))
        return p

    def save_fig(filename, dpi=180):
        p = directory / filename
        plt.tight_layout()
        plt.savefig(p, dpi=dpi)
        plt.close()
        return p

    core.save_csv = save_csv
    core.save_json = save_json
    core.save_fig = save_fig
    core.backup_file = lambda path: None


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--stage", required=True,
                    choices=["baseline", "sweep", "robustness", "observer", "self", "noise"])
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    configure_output(args.output)
    # Original invocation parameters appear in notebook cells 3,4,5,6,8,10.
    # Defaults below are original function defaults except where explicitly passed.
    if args.stage == "baseline":
        core.run_experiment_A(seed=123, a=4.0, b=8.0, lambda_obs=0.0,
                              F_align=1.0, H=(1.0,1.0), sigma=0.08,
                              eta=0.01, steps=600, n_trials=300, n_theta=25,
                              map_n=31, map_trials=40)
    elif args.stage == "sweep":
        core.sweep_binary_parameters()
    elif args.stage == "robustness":
        core.robust_check_best_binary()
    elif args.stage == "observer":
        core.sweep_observer_coupling()
    elif args.stage == "self":
        core.run_experiment_B(seed=123, alpha=1.0, well_strength=2.0,
                              lambda_self=0.5, gamma=0.5, K_scale=0.0,
                              A_diag=(1.0,0.8), eta_update=0.05, n_initial=80)
    elif args.stage == "noise":
        core.run_self_noise_switching()


if __name__ == "__main__":
    main()

