"""Load definition-only B19 namespaces without running experiments or Drive code.

This is a source-inspection adapter, not a full stage runner. Notebook top-level
configuration, cached inputs and orchestration are intentionally not evaluated.
Supply required stage globals explicitly before invoking a recovered function.
"""
from pathlib import Path
import ast
import json
import math
import itertools
import shutil
import zipfile
import numpy as np
import pandas as pd

def load_all():
    namespaces = {}
    for p in sorted((Path(__file__).parent/'definitions').glob('B19_*_definitions.py')):
        tree=ast.parse(p.read_text())
        if any(not isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)) for node in tree.body):
            raise ValueError('Unexpected executable top-level source: '+p.name)
        namespace={'np':np,'pd':pd,'math':math,'Path':Path,'json':json,'itertools':itertools,'shutil':shutil,'zipfile':zipfile}
        exec(compile(tree,str(p),'exec'),namespace)
        namespaces[p.stem.removesuffix('_definitions')]=namespace
    return namespaces

if __name__=='__main__':
    namespaces=load_all()
    print(json.dumps({'status':'PASS','namespaces_loaded':len(namespaces),'experiment_functions_invoked':0,'note':'Definitions only. Full notebook rerun not performed.'},indent=2))
