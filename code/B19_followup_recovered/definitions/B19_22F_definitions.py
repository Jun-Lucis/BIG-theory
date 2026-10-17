# Original definitions only; no experiment or notebook top-level orchestration.

def epsilon_variants(eps):
    eps=np.array(sorted(np.unique(eps)),float)
    out={"full":eps}
    if len(eps)>=5:
        out["alternate_even"]=eps[::2]
        out["alternate_odd"]=eps[1::2]
    if len(eps)>=6:
        out["drop_lowest"]=eps[1:]
        out["drop_highest"]=eps[:-1]
        out["interior_every2_keep_ends"]=np.unique(np.r_[eps[0],eps[1:-1:2],eps[-1]])
    return {k:v for k,v in out.items() if len(v)>=3}


def classify_at_time(g, tol=1e-12):
    g=g.sort_values("epsilon")
    e=g.epsilon.to_numpy(float); y=g.deltaZ.to_numpy(float)
    s=np.diff(y)/np.diff(e)
    mn=float(np.min(s)); mx=float(np.max(s))
    if np.all(s > tol): c="increasing"
    elif np.all(s < -tol): c="decreasing"
    elif np.any(s > tol) and np.any(s < -tol): c="mixed"
    else: c="flat_or_tolerance"
    return mn,mx,c,len(s)


def crossing(g,col):
    q=g[g["T"]>1e-12].sort_values("T").reset_index(drop=True)
    T=q["T"].to_numpy(float); y=q[col].to_numpy(float)
    for i in range(len(T)-1):
        if y[i] < 0 and y[i+1] > 0:
            tc=T[i]-y[i]*(T[i+1]-T[i])/(y[i+1]-y[i])
            return tc,T[i],T[i+1],y[i],y[i+1]
    return (np.nan,)*5


def thin_times(g,k,offset=0):
    ts=np.array(sorted(g.loc[g["T"]>1e-12,"T"].unique()),float)
    kept=ts[offset::k]
    if len(ts) and ts[-1] not in kept: kept=np.r_[kept,ts[-1]]
    return g[(g["T"]<=1e-12) | g["T"].isin(kept)]


def rec(df,ray,col):
    q=df[df.ray_label==ray]
    return float(q.iloc[0][col]) if len(q) else np.nan


def sha256(p):
    h=hashlib.sha256()
    with open(p,"rb") as f:
        for b in iter(lambda:f.read(1<<20),b""): h.update(b)
    return h.hexdigest()
