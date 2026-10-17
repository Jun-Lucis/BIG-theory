"""Definition-only inspection adapter. No experiments, mounts or notebook orchestration."""
from pathlib import Path
import ast,hashlib,inspect,itertools,json,math,os,time,traceback,types
import numpy as np
import pandas as pd
def load_all():
    out={}
    for p in sorted((Path(__file__).parent/'definitions').glob('*_definitions.py')):
        t=ast.parse(p.read_text())
        if any(not isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)) for n in t.body):raise ValueError(p)
        ns={k:v for k,v in globals().items() if not k.startswith('_')}
        exec(compile(t,str(p),'exec'),ns)
        out[p.stem.removesuffix('_definitions')]=ns
    return out
if __name__=='__main__':
    ns=load_all()
    print(json.dumps({'status':'PASS','namespaces_loaded':len(ns),'experiment_functions_invoked':0,'note':'Definitions only; original stage globals and path adaptation required for calls. Independent full rerun not completed.'},indent=2))
