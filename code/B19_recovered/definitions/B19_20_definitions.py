# Extracted definitions only. Function bodies unchanged; no notebook top-level execution.

def first_crossing_time(d, col, threshold=0.0, direction="positive"):
    z=d[[time_col,col]].dropna().sort_values(time_col)
    if not len(z): return np.nan
    if direction=="positive":
        hit=z[z[col]>threshold]
    else:
        hit=z[z[col]<threshold]
    return float(hit.iloc[0][time_col]) if len(hit) else np.nan
