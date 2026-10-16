# Extracted definitions only. Function bodies unchanged; no notebook top-level execution.

def robust_center_scale(x):
    x = np.asarray(x, float)
    med = np.nanmedian(x)
    q25, q75 = np.nanquantile(x, [0.25,0.75])
    s = q75-q25
    if not np.isfinite(s) or s < 1e-12:
        s = np.nanstd(x)
    if not np.isfinite(s) or s < 1e-12:
        s = 1.0
    return med, s


def fold_test(data, xcol, ycol, held):
    train = data[data.ray_label != held][["ray_label",xcol,ycol,"growth01"]].dropna()
    test  = data[data.ray_label == held][["ray_label",xcol,ycol,"growth01"]].dropna()
    if len(train) < 4 or len(test) < 2 or train.growth01.nunique() < 2:
        return None

    mx,sx = robust_center_scale(train[xcol])
    my,sy = robust_center_scale(train[ycol])

    Xtr = np.c_[(train[xcol]-mx)/sx, (train[ycol]-my)/sy]
    Xte = np.c_[(test[xcol]-mx)/sx, (test[ycol]-my)/sy]
    ytr = train.growth01.to_numpy(int)
    yte = test.growth01.to_numpy(int)

    c0 = Xtr[ytr==0].mean(axis=0)
    c1 = Xtr[ytr==1].mean(axis=0)
    # nearest centroid; ties go to growth only if exactly equal
    d0 = ((Xte-c0)**2).sum(axis=1)
    d1 = ((Xte-c1)**2).sum(axis=1)
    pred = (d1 <= d0).astype(int)

    acc = float((pred==yte).mean())
    tp = int(((pred==1)&(yte==1)).sum())
    tn = int(((pred==0)&(yte==0)).sum())
    fp = int(((pred==1)&(yte==0)).sum())
    fn = int(((pred==0)&(yte==1)).sum())
    balacc = 0.5*((tp/(tp+fn) if tp+fn else np.nan) +
                  (tn/(tn+fp) if tn+fp else np.nan))
    return dict(held_out_ray=held, accuracy=acc, balanced_accuracy=float(balacc),
                n_test=len(test), tp=tp,tn=tn,fp=fp,fn=fn,
                train_center_x=mx,train_scale_x=sx,train_center_y=my,train_scale_y=sy,
                decay_centroid_x=float(c0[0]),decay_centroid_y=float(c0[1]),
                growth_centroid_x=float(c1[0]),growth_centroid_y=float(c1[1]))
