# Original definitions only; no experiment or notebook top-level orchestration.

def one(name):
    hits=list(SRCDIR.rglob(name))
    if len(hits)!=1:
        raise RuntimeError(f'Expected exactly one {name}, found {len(hits)}')
    return hits[0]


def first_negative_to_positive_crossing(g, col):
    q=(g[g["T"] > T_EXCLUDE_MAX]
       .sort_values("T")
       .reset_index(drop=True))

    T=q["T"].to_numpy(dtype=float)
    y=q[col].to_numpy(dtype=float)

    for i in range(len(T)-1):
        # Genuine sign crossing only: negative on the left, positive on the right.
        if y[i] < 0.0 and y[i+1] > 0.0:
            tz=T[i]-y[i]*(T[i+1]-T[i])/(y[i+1]-y[i])
            return tz,T[i],T[i+1],y[i],y[i+1]

    return (np.nan,np.nan,np.nan,np.nan,np.nan)


def sha256(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):
            h.update(b)
    return h.hexdigest()
