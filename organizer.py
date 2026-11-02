import shutil
from pathlib import Path
from history import record_move

CATEGORY_FOLDERS = {"Documents", "Spreadsheets", "Images", "Archives", "Others", "Directories"}

def get_correct_destination(extension):
    if extension in [".pdf",".docx",".txt"]:
        return "Documents"
    elif extension in [".xlsx",".csv"]:
        return "Spreadsheets"
    elif extension in [".png",".jpg",".jpeg"]:
        return "Images"
    elif extension in [".rar",".7z",".zip"]:
        return "Archives"
    else:
        return "Others"


def organize_directory(directory_to_organize):
    dir_path = Path(directory_to_organize)
    moved = 0
    if not dir_path.is_dir():
        return None
    for file_path in list(dir_path.iterdir()): # list() as we are changing the directory in place 
        directory = ""
        if file_path.is_dir() and file_path.name in CATEGORY_FOLDERS:
            continue  
        if file_path.is_file():
            folder = dir_path / get_correct_destination(file_path.suffix.lower())
        else:
            folder = dir_path / "Directories"
        folder.mkdir(exist_ok=True)
        target = folder / file_path.name
        if target.exists():              # avoid name collisions
            print(f"Skipped (already exists): {target}")
            continue
        shutil.move(str(file_path), str(target))
        record_move(file_path, target)
        moved += 1
    return moved

from history import record_move, load_history, save_history

def undo_moves(directory):
    base = Path(directory).resolve()
    entries = load_history()
    remaining = []
    restored = 0

    for e in reversed(entries):
        src, dst = Path(e["from"]), Path(e["to"])
        # only touch entries that belong to this directory
        if base not in src.resolve().parents:
            remaining.append(e)
            continue
        if not dst.exists():
            print(f"Missing, can't restore: {dst}")
            continue                      # drop stale entry
        if src.exists():
            print(f"Original spot taken, skipped: {src}")
            remaining.append(e)           # keep it, try again later
            continue
        shutil.move(str(dst), str(src))
        restored += 1

    save_history(list(reversed(remaining)))   # restore original order

    # remove category folders that are now empty
    for name in CATEGORY_FOLDERS:
        folder = base / name
        if folder.is_dir() and not any(folder.iterdir()):
            folder.rmdir()
    return restored