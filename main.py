import shutil
from pathlib import Path

# 整理したいフォルダ（適宜変更）
TARGET_DIR = Path("target")

# 拡張子ごとの振り分け先
EXTENSION_MAP = {
    ".txt": "text",
    ".csv": "csv",
    ".jpg": "images",
    ".png": "images",
    ".pdf": "pdf",
}

def organize_files():
    if not TARGET_DIR.exists():
        print("対象フォルダが存在しません")
        return

    for file in TARGET_DIR.iterdir():
        if file.is_file():
            ext = file.suffix.lower()
            folder_name = EXTENSION_MAP.get(ext, "others")

            dest_dir = TARGET_DIR / folder_name
            dest_dir.mkdir(exist_ok=True)

            shutil.move(str(file), dest_dir / file.name)

    print("ファイル整理が完了しました")

if __name__ == "__main__":
    organize_files()
