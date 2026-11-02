import json
from pathlib import Path
HISTORY_FILE = Path(__file__).parent / "history.json"
def record_move(source, target):
    data = []
    if HISTORY_FILE.exists():
        try:
            data = json.loads(HISTORY_FILE.read_text())
        except json.JSONDecodeError:
            pass
    data.append({"from": str(source), "to": str(target)})
    HISTORY_FILE.write_text(json.dumps(data, indent=2))