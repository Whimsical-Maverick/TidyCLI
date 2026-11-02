# TidyCLI

A safe, easy-to-use command-line file organizer written in Python. TidyCLI sorts the contents of a folder into category subfolders and keeps a history of every move, so you can undo it at any time.

## Features

- **Organize** a folder by file type.
- **Undo** earlier moves using the saved history.
- **Safe by design:** it never overwrites existing files, and it skips items whose target already exists.
- **Idempotent:** running it again only handles new files. If there is nothing new, it prints `ALREADY RAN`.
- **Interactive menu** that keeps running until you choose to exit.
- **Append-only history** in `history.jsonl` (one JSON record per move).

## Requirements

- Python 3.8+
- No third-party dependencies

## Usage

```bash
python main.py
```

You'll see a menu:

```
1) Organize  2) Undo  3) Exit
```

Choose an option, then enter the full path of the folder (quotes from Windows "Copy as path" are fine).

| Option | Action |
|--------|--------|
| 1 | Organize the folder and print how many items were moved |
| 2 | Restore files moved from that folder and clean up empty category folders |
| 3 | Exit |

### Example

```
Choose: 1
Enter the complete location of the directory: C:\Users\me\Downloads
--------------------------------------------------SUCCESSFULLY ORGANIZED 14 ITEMS--------------------------------------------------
```

## How files are sorted

| Folder | Extensions |
|--------|-----------|
| `Documents` | `.pdf` `.docx` `.txt` |
| `Spreadsheets` | `.xlsx` `.csv` |
| `Images` | `.png` `.jpg` `.jpeg` |
| `Archives` | `.rar` `.7z` `.zip` |
| `Directories` | any subfolder |
| `Others` | everything else |

Extension matching is case-insensitive. Category folders are created only when needed and are never moved again on later runs.

## Behavior details

- **Re-running:** because organized files leave the top level, only new items are moved on later runs.
- **Name collisions:** if a file with the same name already exists in the target folder, it is skipped and a message is printed.
- **History:** each move is appended to `history.jsonl` as `{"from": ..., "to": ..., "time": ...}`.
- **Undo:**
  - Moves are reversed newest-first.
  - Only moves that came from the chosen folder are touched.
  - If the original location is now occupied, that file is skipped and its history entry is kept.
  - If the moved file no longer exists, its stale entry is dropped.
  - Empty category folders are removed afterwards.

## Project structure

```
TidyCLI/
├── main.py         # Interactive menu loop
├── organizer.py    # Organize and undo logic
├── history.py      # Append-only JSONL history
└── history.jsonl   # Generated move log
```

