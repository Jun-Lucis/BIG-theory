def simple_linear_fit(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    mask = np.isfinite(x) & np.isfinite(y)
    x = x[mask]
    y = y[mask]

    if len(x) < 2 or np.std(x) <= 1e-15:
        return {
            "slope": np.nan,
            "intercept": np.nan,
            "r2": np.nan,
            "corr": np.nan,
            "n": int(len(x)),
        }

    A = np.vstack([x, np.ones_like(x)]).T
    slope, intercept = np.linalg.lstsq(A, y, rcond=None)[0]
    yhat = slope * x + intercept
    ss_res = float(np.sum((y - yhat) ** 2))
    ss_tot = float(np.sum((y - np.mean(y)) ** 2))
    r2 = 1.0 - ss_res / (ss_tot + 1e-15)
    corr = float(np.corrcoef(x, y)[0, 1])

    return {
        "slope": float(slope),
        "intercept": float(intercept),
        "r2": float(r2),
        "corr": corr,
        "n": int(len(x)),
    }

def multi_linear_fit(X_df, y_series):
    X = X_df.to_numpy(dtype=float)
    y = y_series.to_numpy(dtype=float)

    mask = np.isfinite(y)
    for j in range(X.shape[1]):
        mask &= np.isfinite(X[:, j])

    X = X[mask]
    y = y[mask]

    if len(y) < X.shape[1] + 1:
        return {
            "r2": np.nan,
            "n": int(len(y)),
            "intercept": np.nan,
            **{f"coef_{c}": np.nan for c in X_df.columns},
        }

    X_aug = np.column_stack([X, np.ones(len(X))])
    coef = np.linalg.lstsq(X_aug, y, rcond=None)[0]
    yhat = X_aug @ coef
    ss_res = float(np.sum((y - yhat) ** 2))
    ss_tot = float(np.sum((y - np.mean(y)) ** 2))
    r2 = 1.0 - ss_res / (ss_tot + 1e-15)

    out = {
        "r2": float(r2),
        "n": int(len(y)),
        "intercept": float(coef[-1]),
    }
    for c, v in zip(X_df.columns, coef[:-1]):
        out[f"coef_{c}"] = float(v)
    return out

def zscore_series(s):
    s = pd.Series(s).astype(float)
    sd = float(s.std(ddof=0))
    if sd <= 1e-15:
        return s * 0.0
    return (s - float(s.mean())) / sd
