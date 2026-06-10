from pathlib import Path
import zipfile


RAW_ZIP = Path("data/raw/data_gaap.zip")
EXTRACT_DIR = Path("data/processed/source")


def extract_all():
    EXTRACT_DIR.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(RAW_ZIP, "r") as zf:
        zf.extractall(EXTRACT_DIR)

    print("ZIP extraction complete")


if __name__ == "__main__":
    extract_all()