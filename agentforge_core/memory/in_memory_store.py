from __future__ import annotations

from collections import defaultdict

from agentforge_core.memory.base import BaseMemoryStore


class InMemoryStore(BaseMemoryStore):
    def __init__(self):
        self._db = defaultdict(dict)

    def save(self, namespace: str, key: str, value: dict) -> None:
        self._db[namespace][key] = value

    def load(self, namespace: str, key: str) -> dict | None:
        return self._db.get(namespace, {}).get(key)

    def list_keys(self, namespace: str) -> list[str]:
        return list(self._db.get(namespace, {}).keys())
