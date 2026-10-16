# Extracted definitions only. Function bodies unchanged; no notebook top-level execution.

def to_jsonable(obj):
    if isinstance(obj, dict):
        return {str(k): to_jsonable(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [to_jsonable(v) for v in obj]
    if isinstance(obj, tuple):
        return [to_jsonable(v) for v in obj]
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    if isinstance(obj, np.integer):
        return int(obj)
    if isinstance(obj, np.floating):
        return float(obj)
    if isinstance(obj, np.bool_):
        return bool(obj)
    return obj


def backup_to_drive(path):
    path = Path(path)
    try:
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)
        dst = BACKUP_DIR / path.name
        try:
            if path.resolve() == dst.resolve():
                print("Already on Drive:", dst)
                return
        except Exception:
            pass
        shutil.copy2(path, dst)
        print("Saved to Drive:", dst)
    except Exception as e:
        print("Drive backup failed:", e)


def save_csv(df, filename):
    path = OUTDIR / filename
    df.to_csv(path, index=False)
    print("Saved local:", path)
    backup_to_drive(path)
    return path


def save_json(obj, filename):
    path = OUTDIR / filename
    with open(path, "w", encoding="utf-8") as f:
        json.dump(to_jsonable(obj), f, indent=2, ensure_ascii=False)
    print("Saved local:", path)
    backup_to_drive(path)
    return path


def save_text(text, filename):
    path = OUTDIR / filename
    path.write_text(text, encoding="utf-8")
    print("Saved local:", path)
    backup_to_drive(path)
    return path


def save_figure(filename, dpi=180):
    path = OUTDIR / filename
    plt.tight_layout()
    plt.savefig(path, dpi=dpi)
    print("Saved local:", path)
    backup_to_drive(path)
    plt.show()
    plt.close()
    return path


def find_existing_file(filename):
    candidates = [
        Path("/content/drive/MyDrive/BIG_B19_colab_outputs/B19_10_run_001/activation_threshold_control_validation") / filename,
        Path("/content/B19_10_run_001_activation_threshold_control_validation") / filename,
        Path("/content") / filename,
    ]

    for p in candidates:
        if p.exists():
            return p

    for root in [Path("/content/drive/MyDrive"), Path("/content")]:
        if root.exists():
            hits = list(root.rglob(filename))
            if hits:
                return hits[0]
    return None
