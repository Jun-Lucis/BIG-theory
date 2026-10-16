# Extracted definitions only. Function bodies unchanged; no notebook top-level execution.

def interp_at_critical(df, ray, xcol, ycol, xc):
    d = df[df["ray_label"] == ray][[xcol,ycol]].dropna().drop_duplicates(xcol).sort_values(xcol)
    if len(d) < 2:
        return np.nan
    x = d[xcol].to_numpy(float)
    y = d[ycol].to_numpy(float)
    if xc < x.min() or xc > x.max():
        return np.nan
    return float(np.interp(xc, x, y))
