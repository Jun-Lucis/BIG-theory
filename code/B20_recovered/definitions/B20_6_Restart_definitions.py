def sha256(p):
 h=hashlib.sha256();
 with open(p,'rb') as f:
  for b in iter(lambda:f.read(1<<20),b''): h.update(b)
 return h.hexdigest()

def find_key(o,key):
 if isinstance(o,dict):
  if key in o: return o[key]
  for v in o.values():
   z=find_key(v,key)
   if z is not None:return z
 if isinstance(o,list):
  for v in o:
   z=find_key(v,key)
   if z is not None:return z

class Tx(ast.NodeTransformer):
 def visit_Assign(self,node):
  if isinstance(node.value,ast.Call) and isinstance(node.value.func,ast.Name) and node.value.func.id=='point_on_ray':
   return ast.parse("params=dict(supplied_params); ray_label=str(params['variant_id']); epsilon=0.0").body
  return self.generic_visit(node)

def params_from_row(r):
 p={k:float(r[k]) for k in PARAMS}; p.update({'handedness':-1,'nu':.003,'Emax':30.,'variant_id':str(r.case_id)}); return p

def run_one_manifest_case(case_id):
 r=manifest[manifest.case_id==case_id].iloc[0]; cf=CACHE/f'{case_id}.json'
 if cf.exists():
  q=json.load(open(cf)); assert q['status']=='COMPLETE'; print('CACHED',case_id,q['F_DeltaZ']); return q
 t=time.time(); res=run_case(params_from_row(r),N=48,L=8.,dt_cap=5e-5,keep_timeseries=True); elapsed=time.time()-t
 # inherited runner expected to expose timeseries; robust extraction
 if 'timeseries' in res:
  ts=res['timeseries']; ts=ts if isinstance(ts,pd.DataFrame) else pd.DataFrame(ts); F=float(ts.enstrophy_half.iloc[-1]-ts.enstrophy_half.iloc[0])
 elif 'enstrophy_half_initial' in res and 'enstrophy_half_final' in res: F=float(res['enstrophy_half_final']-res['enstrophy_half_initial'])
 else: raise RuntimeError('Cannot extract F; keys='+repr(sorted(res.keys())))
 rec={'status':'COMPLETE','case_id':case_id,'s':float(r.s),'F_DeltaZ':F,'elapsed_seconds':elapsed,'result_keys':sorted(res.keys())}
 # capture lightweight diagnostics if present
 for k in ['steps','dt_min','dt_max','max_div_omega_l2','div_omega_l2']:
  if k in res:
   try: rec[k]=float(res[k])
   except: rec[k]=str(res[k])
 tmp=Path(str(cf)+'.tmp'); json.dump(rec,open(tmp,'w'),indent=2,sort_keys=True); tmp.replace(cf)
 print(json.dumps(rec,indent=2)); return rec

def load_fast_count(name):
    return sum(
        1
        for ins in instructions
        if ins.opname == "LOAD_FAST"
        and ins.argval == name
    )

def run_case_B206_fixed(
    supplied_params,
    N=48,
    L=8.0,
    dt_cap=5e-5,
    keep_timeseries=False,
):
    return _raw_B206_runner(
        supplied_params,
        0.0,
        N=N,
        L=L,
        dt_cap=dt_cap,
        keep_timeseries=keep_timeseries,
    )

def run_one_manifest_case_fixed(case_id):

    rows = manifest_df[
        manifest_df["case_id"] == case_id
    ]

    assert len(rows) == 1, (
        f"{case_id}: expected exactly one manifest row, "
        f"got {len(rows)}"
    )

    r = rows.iloc[0]

    cf = cache_dir / f"{case_id}.json"
    tf = cache_dir / f"{case_id}__timeseries.csv"

    # Resume completed case.
    if cf.exists():

        with open(
            cf,
            "r",
            encoding="utf-8"
        ) as f:
            q = json.load(f)

        assert q["status"] == "COMPLETE"

        print(
            "CACHED",
            case_id,
            q["F_DeltaZ"]
        )

        return q

    params = params_from_row(r)

    print()
    print("-" * 72)
    print("RUN:", case_id)

    if "s" in r.index:
        print("s =", float(r["s"]))

    print("-" * 72)

    wall0 = time.time()

    # Corrected Cell 7D wrapper.
    res = run_case(
        params,
        N=48,
        L=8.0,
        dt_cap=5e-5,
        keep_timeseries=True,
    )

    elapsed = float(
        time.time() - wall0
    )

    # --------------------------------------------------------
    # CRITICAL FIX:
    # inherited runner returns (summary, ts)
    # --------------------------------------------------------

    assert isinstance(res, tuple), (
        f"Expected tuple return, got {type(res)}"
    )

    assert len(res) == 2

    summary, ts = res

    assert isinstance(summary, dict)

    if not isinstance(ts, pd.DataFrame):
        ts = pd.DataFrame(ts)

    assert len(ts) >= 2
    assert "enstrophy_half" in ts.columns

    z = ts["enstrophy_half"].to_numpy(
        dtype=float
    )

    assert np.all(np.isfinite(z))

    F = float(
        z[-1] - z[0]
    )

    assert np.isfinite(F)

    # --------------------------------------------------------
    # Save timeseries FIRST
    # --------------------------------------------------------

    tmp_tf = Path(
        str(tf) + ".tmp"
    )

    ts.to_csv(
        tmp_tf,
        index=False
    )

    tmp_tf.replace(tf)

    assert tf.exists()
    assert tf.stat().st_size > 0

    with open(tf, "rb") as f:
        ts_sha = hashlib.sha256(
            f.read()
        ).hexdigest()

    # --------------------------------------------------------
    # Compact summary serialization
    # --------------------------------------------------------

    serial_summary = {}

    for k, v in summary.items():

        if isinstance(v, (bool, np.bool_)):
            serial_summary[k] = bool(v)

        elif isinstance(v, (int, np.integer)):
            serial_summary[k] = int(v)

        elif isinstance(v, (float, np.floating)):
            serial_summary[k] = float(v)

        elif isinstance(v, str):
            serial_summary[k] = v

        elif v is None:
            serial_summary[k] = None

        # Skip arrays / complex objects in compact JSON.

    record = {
        "status":
            "COMPLETE",

        "case_id":
            str(case_id),

        "F_DeltaZ":
            float(F),

        "elapsed_seconds":
            elapsed,

        "timeseries_rows":
            int(len(ts)),

        "timeseries_file":
            tf.name,

        "timeseries_sha256":
            ts_sha,

        "summary":
            serial_summary,

        "crossing_scan_performed":
            False,

        "timestamp_utc":
            pd.Timestamp.now(
                tz="UTC"
            ).isoformat(),
    }

    # Include manifest metadata without guessing names.
    for col in [
        "trajectory",
        "point_label",
        "s",
        "T",
    ]:
        if col in r.index:

            val = r[col]

            if isinstance(
                val,
                (np.integer, int)
            ):
                val = int(val)

            elif isinstance(
                val,
                (np.floating, float)
            ):
                val = float(val)

            else:
                val = str(val)

            record[col] = val

    # --------------------------------------------------------
    # COMPLETE JSON LAST
    # --------------------------------------------------------

    tmp_cf = Path(
        str(cf) + ".tmp"
    )

    with open(
        tmp_cf,
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            record,
            f,
            indent=2,
            sort_keys=True
        )

    tmp_cf.replace(cf)

    # --------------------------------------------------------
    # Re-read persistence
    # --------------------------------------------------------

    with open(
        cf,
        "r",
        encoding="utf-8"
    ) as f:
        check = json.load(f)

    assert check["status"] == "COMPLETE"
    assert check["case_id"] == case_id
    assert abs(
        float(check["F_DeltaZ"]) - F
    ) < 1e-15

    ts_check = pd.read_csv(tf)

    assert len(ts_check) == len(ts)

    print()
    print("F_DeltaZ =", f"{F:+.12e}")
    print(
        "elapsed =",
        f"{elapsed/60.0:.2f} min"
    )
    print(
        "timeseries rows =",
        len(ts)
    )
    print("Drive persistence: PASS")

    return record

def run_one_manifest_case_fixed(case_id):

    rows = manifest[
        manifest["case_id"] == case_id
    ]

    assert len(rows) == 1, (
        f"{case_id}: manifest rows={len(rows)}"
    )

    r = rows.iloc[0]

    json_file = CACHE / f"{case_id}.json"
    ts_file = CACHE / f"{case_id}__timeseries.csv"

    # ----------------------------------------
    # Resume only a COMPLETE saved result
    # ----------------------------------------

    if json_file.exists():

        with open(
            json_file,
            "r",
            encoding="utf-8"
        ) as f:
            saved = json.load(f)

        assert saved["status"] == "COMPLETE"

        assert ts_file.exists(), (
            "COMPLETE JSON exists but timeseries is missing."
        )

        print(
            "CACHED:",
            case_id,
            f"F={float(saved['F_DeltaZ']):+.12e}"
        )

        return saved

    # ----------------------------------------
    # Build already-frozen case parameters
    # ----------------------------------------

    params = params_from_row(r)

    print()
    print("-" * 72)
    print("RUN:", case_id)

    if "s" in r.index:
        print("s =", float(r["s"]))

    print("-" * 72)

    # ----------------------------------------
    # ONE PDE
    # ----------------------------------------

    wall0 = time.time()

    res = run_case(
        params,
        N=48,
        L=8.0,
        dt_cap=5e-5,
        keep_timeseries=True,
    )

    elapsed = float(time.time() - wall0)

    # ----------------------------------------
    # Audited return schema
    # ----------------------------------------

    assert isinstance(res, tuple)
    assert len(res) == 2

    summary, ts = res

    assert isinstance(summary, dict)

    if not isinstance(ts, pd.DataFrame):
        ts = pd.DataFrame(ts)

    assert len(ts) >= 2
    assert "enstrophy_half" in ts.columns

    z = ts["enstrophy_half"].to_numpy(dtype=float)

    assert np.all(np.isfinite(z))

    F = float(z[-1] - z[0])

    assert np.isfinite(F)

    # ----------------------------------------
    # SAVE TIMESERIES FIRST
    # ----------------------------------------

    tmp_ts = Path(str(ts_file) + ".tmp")

    ts.to_csv(tmp_ts, index=False)
    tmp_ts.replace(ts_file)

    assert ts_file.exists()
    assert ts_file.stat().st_size > 0

    with open(ts_file, "rb") as f:
        ts_sha256 = hashlib.sha256(
            f.read()
        ).hexdigest()

    # ----------------------------------------
    # JSON-safe summary
    # ----------------------------------------

    compact_summary = {}

    for k, v in summary.items():

        if isinstance(v, (bool, np.bool_)):
            compact_summary[k] = bool(v)

        elif isinstance(v, (int, np.integer)):
            compact_summary[k] = int(v)

        elif isinstance(v, (float, np.floating)):
            compact_summary[k] = float(v)

        elif isinstance(v, str):
            compact_summary[k] = v

        elif v is None:
            compact_summary[k] = None

    record = {
        "status": "COMPLETE",
        "case_id": str(case_id),
        "F_DeltaZ": F,
        "elapsed_seconds": elapsed,
        "timeseries_rows": int(len(ts)),
        "timeseries_file": ts_file.name,
        "timeseries_sha256": ts_sha256,
        "summary": compact_summary,
        "crossing_scan_performed": False,
        "crossing_prediction_computed": False,
        "timestamp_utc": pd.Timestamp.now(
            tz="UTC"
        ).isoformat(),
    }

    # Preserve available frozen manifest metadata.
    for col in [
        "trajectory",
        "point_label",
        "s",
        "T",
    ]:
        if col in r.index:

            v = r[col]

            if isinstance(v, (np.integer, int)):
                record[col] = int(v)

            elif isinstance(v, (np.floating, float)):
                record[col] = float(v)

            else:
                record[col] = str(v)

    # ----------------------------------------
    # COMPLETE JSON LAST
    # ----------------------------------------

    tmp_json = Path(str(json_file) + ".tmp")

    with open(
        tmp_json,
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            record,
            f,
            indent=2,
            sort_keys=True
        )

    tmp_json.replace(json_file)

    # ----------------------------------------
    # Persistence audit
    # ----------------------------------------

    with open(
        json_file,
        "r",
        encoding="utf-8"
    ) as f:
        check = json.load(f)

    assert check["status"] == "COMPLETE"
    assert check["case_id"] == case_id
    assert abs(
        float(check["F_DeltaZ"]) - F
    ) < 1e-15

    ts_check = pd.read_csv(ts_file)

    assert len(ts_check) == len(ts)

    print()
    print("RUNNER RETURN: PASS")
    print("F_DeltaZ =", f"{F:+.12e}")
    print("elapsed =", f"{elapsed/60.0:.2f} min")
    print("timeseries rows =", len(ts))
    print("Drive persistence: PASS")

    return record

def checkpoint_state(case_id):

    jf = CACHE / f"{case_id}.json"
    tf = CACHE / f"{case_id}__timeseries.csv"

    if not jf.exists():
        return "MISSING"

    try:
        with open(
            jf,
            "r",
            encoding="utf-8"
        ) as f:
            q = json.load(f)

    except Exception:
        return "INVALID_JSON"

    if q.get("status") != "COMPLETE":
        return "INCOMPLETE_JSON"

    if not tf.exists():
        return "MISSING_TIMESERIES"

    if tf.stat().st_size <= 0:
        return "EMPTY_TIMESERIES"

    try:
        F = float(q["F_DeltaZ"])

        if not np.isfinite(F):
            return "NONFINITE_F"

    except Exception:
        return "INVALID_F"

    return "COMPLETE"

def save_run_log():

    tmp = Path(
        str(run_log_file) + ".tmp"
    )

    with open(
        tmp,
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            run_log,
            f,
            indent=2,
            sort_keys=True
        )

    tmp.replace(run_log_file)

def load_complete_case(case_id):

    jf = CACHE / f"{case_id}.json"
    tf = CACHE / f"{case_id}__timeseries.csv"

    assert jf.exists(), (
        f"Missing JSON: {case_id}"
    )

    assert tf.exists(), (
        f"Missing timeseries: {case_id}"
    )

    with open(
        jf,
        "r",
        encoding="utf-8"
    ) as f:
        q = json.load(f)

    assert q.get("status") == "COMPLETE"
    assert q.get("case_id") == case_id

    F = float(q["F_DeltaZ"])

    assert np.isfinite(F)

    return q

def scan_params_from_row(r):

    p = {
        "Emax":
            float(r["Emax"]),

        "R":
            float(r["R"]),

        "axial_coupling":
            float(r["axial_coupling"]),

        "handedness":
            int(r["handedness"]),

        "imbalance":
            float(r["imbalance"]),

        "nu":
            float(r["nu"]),

        "pair_angle":
            float(r["pair_angle"]),

        "phase":
            float(r["phase"]),

        "sep_factor":
            float(r["sep_factor"]),

        "twist_factor":
            float(r["twist_factor"]),

        "variant_id":
            str(r["variant_id"]),
    }

    assert set(p.keys()) == REQUIRED_SOLVER_KEYS

    return p

def scan_json_path(cid):
    return SCAN_CACHE / f"{cid}.json"

def scan_ts_path(cid):
    return SCAN_CACHE / f"{cid}__timeseries.csv"

def write_json_atomic(path, obj):

    tmp = Path(
        str(path) + ".tmp"
    )

    with open(
        tmp,
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            obj,
            f,
            indent=2,
            sort_keys=True,
        )

    tmp.replace(path)

def scan_checkpoint_state(cid):

    jf = scan_json_path(cid)

    if not jf.exists():
        return "MISSING"

    try:
        with open(
            jf,
            "r",
            encoding="utf-8"
        ) as f:
            q = json.load(f)

    except Exception:
        return "INVALID_JSON"

    if q.get("status") != "COMPLETE":
        return "INCOMPLETE"

    try:
        F = float(q["F_DeltaZ"])
    except Exception:
        return "INVALID_F"

    if not np.isfinite(F):
        return "NONFINITE_F"

    return "COMPLETE"

def run_one_scan_case(r):

    cid = str(r["case_id"])

    state = scan_checkpoint_state(cid)

    if state == "COMPLETE":
        return None

    assert state == "MISSING", (
        f"{cid}: unsafe checkpoint state {state}"
    )

    params = scan_params_from_row(r)

    print()
    print("-" * 78)
    print(
        "RUN:",
        cid,
        "trajectory=",
        r["trajectory"],
        "s=",
        float(r["s"])
    )
    print("-" * 78)

    wall0 = time.time()

    res = run_case(
        params,
        N=N,
        L=L,
        dt_cap=DT_CAP,
        keep_timeseries=True,
    )

    elapsed = float(
        time.time() - wall0
    )

    assert isinstance(res, tuple)
    assert len(res) == 2

    summary, ts = res

    assert isinstance(summary, dict)

    if not isinstance(
        ts,
        pd.DataFrame
    ):
        ts = pd.DataFrame(ts)

    assert len(ts) >= 2
    assert "enstrophy_half" in ts.columns

    z = ts[
        "enstrophy_half"
    ].to_numpy(
        dtype=float
    )

    assert np.all(
        np.isfinite(z)
    )

    F = float(
        z[-1] - z[0]
    )

    assert np.isfinite(F)

    # ----------------------------------------
    # Timeseries first
    # ----------------------------------------

    tf = scan_ts_path(cid)

    tmp_tf = Path(
        str(tf) + ".tmp"
    )

    ts.to_csv(
        tmp_tf,
        index=False
    )

    tmp_tf.replace(tf)

    assert tf.exists()
    assert tf.stat().st_size > 0

    with open(tf, "rb") as f:
        ts_sha = hashlib.sha256(
            f.read()
        ).hexdigest()

    # ----------------------------------------
    # Compact summary
    # ----------------------------------------

    compact_summary = {}

    for k, v in summary.items():

        if isinstance(
            v,
            (bool, np.bool_)
        ):
            compact_summary[k] = bool(v)

        elif isinstance(
            v,
            (int, np.integer)
        ):
            compact_summary[k] = int(v)

        elif isinstance(
            v,
            (float, np.floating)
        ):
            compact_summary[k] = float(v)

        elif isinstance(v, str):
            compact_summary[k] = v

        elif v is None:
            compact_summary[k] = None

    record = {
        "status":
            "COMPLETE",

        "case_id":
            cid,

        "trajectory":
            str(r["trajectory"]),

        "s":
            float(r["s"]),

        "F_DeltaZ":
            F,

        "elapsed_seconds":
            elapsed,

        "timeseries_rows":
            int(len(ts)),

        "timeseries_file":
            tf.name,

        "timeseries_sha256":
            ts_sha,

        "summary":
            compact_summary,

        "source":
            "PHASE2C_NEW_PDE",

        "prediction_sha256":
            prediction_sha,

        "domain_extended":
            False,

        "bracket_refinement":
            False,
    }

    # JSON COMPLETE last.
    jf = scan_json_path(cid)

    write_json_atomic(
        jf,
        record
    )

    # Re-read.
    assert (
        scan_checkpoint_state(cid)
        == "COMPLETE"
    )

    print(
        "F_DeltaZ =",
        f"{F:+.12e}"
    )

    print(
        "elapsed =",
        f"{elapsed/60.0:.2f} min"
    )

    print("Drive persistence: PASS")

    return record

def save_run_log():

    tmp = Path(
        str(run_log_file) + ".tmp"
    )

    with open(
        tmp,
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            run_log,
            f,
            indent=2,
            sort_keys=True,
        )

    tmp.replace(
        run_log_file
    )

def scan_state(cid):

    jf = (
        SCAN_CACHE /
        f"{cid}.json"
    )

    tf = (
        SCAN_CACHE /
        f"{cid}__timeseries.csv"
    )

    if not jf.exists():
        return "MISSING"

    try:
        with open(
            jf,
            "r",
            encoding="utf-8"
        ) as f:
            q = json.load(f)
    except Exception:
        return "INVALID_JSON"

    if q.get("status") != "COMPLETE":
        return "INCOMPLETE_JSON"

    try:
        F = float(q["F_DeltaZ"])
        if not np.isfinite(F):
            return "NONFINITE_F"
    except Exception:
        return "INVALID_F"

    source = q.get(
        "source",
        ""
    )

    if source == "REUSED_PHASE2A_CENTER":
        # Deliberately no copied Phase2C timeseries.
        return "COMPLETE_REUSED"

    if source == "PHASE2C_NEW_PDE":

        if not tf.exists():
            return "MISSING_TIMESERIES"

        if tf.stat().st_size <= 0:
            return "EMPTY_TIMESERIES"

        return "COMPLETE_PDE"

    return "UNKNOWN_SOURCE"

def scan_json_path(cid):
    return SCAN_CACHE / f"{cid}.json"

def scan_ts_path(cid):
    return SCAN_CACHE / f"{cid}__timeseries.csv"

def scan_state(cid):

    jf = scan_json_path(cid)
    tf = scan_ts_path(cid)

    if not jf.exists():
        return "MISSING"

    try:
        with open(
            jf,
            "r",
            encoding="utf-8"
        ) as f:
            q = json.load(f)
    except Exception:
        return "INVALID_JSON"

    if q.get("status") != "COMPLETE":
        return "INCOMPLETE_JSON"

    try:
        F = float(q["F_DeltaZ"])
        if not np.isfinite(F):
            return "NONFINITE_F"
    except Exception:
        return "INVALID_F"

    source = q.get("source", "")

    if source == "REUSED_PHASE2A_CENTER":
        return "COMPLETE_REUSED"

    if source == "PHASE2C_NEW_PDE":

        if not tf.exists():
            return "MISSING_TIMESERIES"

        if tf.stat().st_size <= 0:
            return "EMPTY_TIMESERIES"

        return "COMPLETE_PDE"

    return "UNKNOWN_SOURCE"

class DirectParameterInjector(
    ast.NodeTransformer
):

    def __init__(self):
        self.replacements = 0

    def visit_Assign(self, node):

        self.generic_visit(node)

        if (
            isinstance(node.value, ast.Call)
            and
            isinstance(
                node.value.func,
                ast.Name
            )
            and
            node.value.func.id
            == "point_on_ray"
        ):

            # Require assignment to params.
            assert len(node.targets) == 1
            assert isinstance(
                node.targets[0],
                ast.Name
            )
            assert (
                node.targets[0].id
                == "params"
            )

            self.replacements += 1

            return [
                ast.Assign(
                    targets=[
                        ast.Name(
                            id="params",
                            ctx=ast.Store(),
                        )
                    ],
                    value=ast.Call(
                        func=ast.Name(
                            id="dict",
                            ctx=ast.Load(),
                        ),
                        args=[
                            ast.Name(
                                id="supplied_params",
                                ctx=ast.Load(),
                            )
                        ],
                        keywords=[],
                    ),
                ),

                ast.Assign(
                    targets=[
                        ast.Name(
                            id="ray_label",
                            ctx=ast.Store(),
                        )
                    ],
                    value=ast.Call(
                        func=ast.Name(
                            id="str",
                            ctx=ast.Load(),
                        ),
                        args=[
                            ast.Subscript(
                                value=ast.Name(
                                    id="params",
                                    ctx=ast.Load(),
                                ),
                                slice=ast.Constant(
                                    value="variant_id"
                                ),
                                ctx=ast.Load(),
                            )
                        ],
                        keywords=[],
                    ),
                ),

                ast.Assign(
                    targets=[
                        ast.Name(
                            id="epsilon",
                            ctx=ast.Store(),
                        )
                    ],
                    value=ast.Constant(
                        value=0.0
                    ),
                ),
            ]

        return node

def params_from_scan_row(r):

    p = {
        "Emax":
            float(r["Emax"]),

        "R":
            float(r["R"]),

        "axial_coupling":
            float(r["axial_coupling"]),

        "handedness":
            int(r["handedness"]),

        "imbalance":
            float(r["imbalance"]),

        "nu":
            float(r["nu"]),

        "pair_angle":
            float(r["pair_angle"]),

        "phase":
            float(r["phase"]),

        "sep_factor":
            float(r["sep_factor"]),

        "twist_factor":
            float(r["twist_factor"]),

        "variant_id":
            str(r["variant_id"]),
    }

    assert set(p.keys()) == REQUIRED_PARAM_KEYS

    return p

def run_case(
    supplied_params,
    N=48,
    L=8.0,
    dt_cap=5e-5,
    keep_timeseries=False,
):

    return raw_direct_runner(
        supplied_params,
        N=N,
        L=L,
        dt_cap=dt_cap,
        keep_timeseries=keep_timeseries,
    )

def write_json_atomic(
    path,
    obj,
):

    tmp = Path(
        str(path) + ".tmp"
    )

    with open(
        tmp,
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            obj,
            f,
            indent=2,
            sort_keys=True,
        )

    tmp.replace(path)

def run_one_missing_case(r):

    cid = str(
        r["case_id"]
    )

    state = scan_state(cid)

    if state in {
        "COMPLETE_REUSED",
        "COMPLETE_PDE",
    }:
        return None

    assert state == "MISSING", (
        f"{cid}: unsafe state {state}"
    )

    p = params_from_scan_row(r)

    print()
    print("-" * 78)
    print(
        "RUN:",
        cid,
        "| trajectory=",
        r["trajectory"],
        "| s=",
        float(r["s"]),
    )
    print("-" * 78)

    wall0 = time.time()

    result = run_case(
        p,
        N=48,
        L=8.0,
        dt_cap=5e-5,
        keep_timeseries=True,
    )

    elapsed = float(
        time.time() - wall0
    )

    # Previously audited exact schema.
    assert isinstance(
        result,
        tuple
    )
    assert len(result) == 2

    summary, ts = result

    assert isinstance(
        summary,
        dict
    )

    if not isinstance(
        ts,
        pd.DataFrame
    ):
        ts = pd.DataFrame(ts)

    assert len(ts) >= 2

    assert (
        "enstrophy_half"
        in ts.columns
    )

    z = ts[
        "enstrophy_half"
    ].to_numpy(
        dtype=float
    )

    assert np.all(
        np.isfinite(z)
    )

    F = float(
        z[-1] - z[0]
    )

    assert np.isfinite(F)

    # ----------------------------------------
    # Save timeseries FIRST
    # ----------------------------------------

    tf = scan_ts_path(cid)

    tmp_tf = Path(
        str(tf) + ".tmp"
    )

    ts.to_csv(
        tmp_tf,
        index=False,
    )

    tmp_tf.replace(tf)

    assert tf.exists()
    assert tf.stat().st_size > 0

    with open(
        tf,
        "rb"
    ) as f:
        ts_sha = hashlib.sha256(
            f.read()
        ).hexdigest()

    # ----------------------------------------
    # Compact serializable summary
    # ----------------------------------------

    compact_summary = {}

    for k, v in summary.items():

        if isinstance(
            v,
            (bool, np.bool_)
        ):
            compact_summary[k] = bool(v)

        elif isinstance(
            v,
            (int, np.integer)
        ):
            compact_summary[k] = int(v)

        elif isinstance(
            v,
            (float, np.floating)
        ):
            compact_summary[k] = float(v)

        elif isinstance(v, str):
            compact_summary[k] = v

        elif v is None:
            compact_summary[k] = None

    # ----------------------------------------
    # COMPLETE JSON LAST
    # ----------------------------------------

    record = {
        "status":
            "COMPLETE",

        "case_id":
            cid,

        "trajectory":
            str(r["trajectory"]),

        "s":
            float(r["s"]),

        "F_DeltaZ":
            F,

        "elapsed_seconds":
            elapsed,

        "timeseries_rows":
            int(len(ts)),

        "timeseries_file":
            tf.name,

        "timeseries_sha256":
            ts_sha,

        "summary":
            compact_summary,

        "source":
            "PHASE2C_NEW_PDE",

        "prediction_sha256":
            prediction_sha,

        "domain_extended":
            False,

        "bracket_refinement":
            False,

        "runtime_recovered_after_reset":
            True,
    }

    jf = scan_json_path(cid)

    write_json_atomic(
        jf,
        record
    )

    assert (
        scan_state(cid)
        == "COMPLETE_PDE"
    )

    print(
        "F_DeltaZ =",
        f"{F:+.12e}"
    )

    print(
        "elapsed =",
        f"{elapsed/60.0:.2f} min"
    )

    print("Drive persistence: PASS")

    return record

def save_resume_log():

    write_json_atomic(
        resume_log_file,
        resume_log,
    )
