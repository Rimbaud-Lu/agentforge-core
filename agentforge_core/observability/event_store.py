from __future__ import annotations

import json
from pathlib import Path


class EventStore:
    def __init__(self, root: str = "data/observability"):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)
        self.path = self.root / "events.jsonl"

    def append(self, event: dict) -> None:
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(event, ensure_ascii=False) + "\n")

    def list_events(self, limit: int = 100) -> list[dict]:
        if not self.path.exists():
            return []
        lines = self.path.read_text(encoding="utf-8").splitlines()
        selected = lines[-limit:]
        return [json.loads(line) for line in selected if line.strip()]
