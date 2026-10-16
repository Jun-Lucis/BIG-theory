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


def has_required_files(folder):
    folder = Path(folder)
    return all((folder / name).exists() for name in REQUIRED_FILES)


def find_b19_14_dir():
    # 1. Exact expected locations.
    candidates = [
        Path("/content/drive/MyDrive/BIG_B19_colab_outputs/B19_14_run_001/spectral_tail_boxsize_robustness"),
        Path("/content/B19_14_run_001_spectral_tail_boxsize_robustness"),
        Path("/content/b19_14_analysis"),
        Path("/content"),
    ]

    for c in candidates:
        if has_required_files(c):
            return c

    # 2. Search by the main required CSV.
    required = REQUIRED_FILES[0]
    roots = [
        Path("/content/drive/MyDrive"),
        Path("/content/drive"),
        Path("/content"),
    ]

    for root in roots:
        if root.exists():
            hits = list(root.rglob(required))
            for h in hits:
                if has_required_files(h.parent):
                    return h.parent

    return None


def find_b19_14_zip():
    zip_names = [
        "BIG_B19_14_spectral_tail_boxsize_robustness_package_v1.zip",
        "BIG_B19_14_spectral_tail_boxsize_robustness_package_v1 (1).zip",
    ]
    roots = [
        Path("/content/drive/MyDrive"),
        Path("/content/drive"),
        Path("/content"),
    ]

    for root in roots:
        if root.exists():
            for name in zip_names:
                hits = list(root.rglob(name))
                if hits:
                    return hits[0]
            hits = list(root.rglob("*B19_14*spectral_tail*package*.zip"))
            if hits:
                return hits[0]
    return None


def extract_b19_14_zip(zip_path):
    zip_path = Path(zip_path)
    extract_dir = Path("/content/B19_14_extracted_for_B19_15")
    extract_dir.mkdir(parents=True, exist_ok=True)

    print("Extracting B19.14 package:")
    print("  zip:", zip_path)
    print("  to :", extract_dir)

    with zipfile.ZipFile(zip_path, "r") as zf:
        zf.extractall(extract_dir)

    # Sometimes files are at root of zip; sometimes inside a subfolder.
    if has_required_files(extract_dir):
        return extract_dir

    for p in extract_dir.rglob(REQUIRED_FILES[0]):
        if has_required_files(p.parent):
            return p.parent

    return extract_dir


def classify_row(row):
    if bool(row["initially_total_open_all_boxes"]) and bool(row["growth_positive_all_boxes"]):
        if row["growth_mean"] > 0.002:
            return "strong_initial_persistent_channel"
        return "weak_initial_persistent_channel"
    if bool(row["initially_total_closed_all_boxes"]) and bool(row["growth_positive_all_boxes"]):
        if row["positive_balance_fraction_min"] >= 0.9:
            return "early_delayed_persistent_channel"
        return "late_delayed_persistent_channel"
    if bool(row["growth_positive_all_boxes"]):
        return "finite_window_positive_channel"
    return "nonpersistent_or_subcritical_channel"


def activation_class(row):
    if row["B0"] > 0:
        return "initial_activation"
    if np.isfinite(row["first_activation_time"]):
        if row["first_activation_time"] <= 0.001:
            return "early_delayed_activation"
        return "late_delayed_activation"
    return "no_activation"
