from __future__ import annotations

import json
from pathlib import Path
from uuid import uuid4


class WorkflowStore:
    def __init__(self, root: str = "data/workflows"):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)

    def create(self, payload: dict) -> str:
        workflow_id = f"wf-{uuid4().hex[:12]}"
        path = self.root / f"{workflow_id}.json"
        payload = {"workflow_id": workflow_id, **payload}
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        return workflow_id

    def save(self, workflow_id: str, payload: dict) -> None:
        path = self.root / f"{workflow_id}.json"
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    def load(self, workflow_id: str) -> dict | None:
        path = self.root / f"{workflow_id}.json"
        if not path.exists():
            return None
        return json.loads(path.read_text(encoding="utf-8"))

    def list_ids(self) -> list[str]:
        return sorted(p.stem for p in self.root.glob("*.json"))
