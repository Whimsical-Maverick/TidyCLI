import json
from datetime import datetime
from pathlib import Path
HISTORY_FILE = Path(__file__).parent / "history.jsonl"
def record_move(source, target):
    entry = {
        "from": str(source),
        "to": str(target),
        "time": datetime.now().isoformat(),
    }
    with HISTORY_FILE.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")
def load_history():
    if not HISTORY_FILE.exists():
        return []
    with HISTORY_FILE.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]