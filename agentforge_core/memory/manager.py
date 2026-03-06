from __future__ import annotations

from uuid import uuid4

from agentforge_core.memory.in_memory_store import InMemoryStore


class MemoryManager:
    def __init__(self, store=None):
        self.store = store or InMemoryStore()

    def create_session(self, task: str) -> str:
        session_id = f"session-{uuid4().hex[:12]}"
        self.store.save("sessions", session_id, {"task": task, "events": []})
        return session_id

    def append_event(self, session_id: str, event: dict) -> None:
        payload = self.store.load("sessions", session_id) or {"events": []}
        payload.setdefault("events", []).append(event)
        self.store.save("sessions", session_id, payload)

    def get_session(self, session_id: str) -> dict | None:
        return self.store.load("sessions", session_id)

    def save_project_context(self, project_key: str, context: dict) -> None:
        self.store.save("projects", project_key, context)

    def get_project_context(self, project_key: str) -> dict | None:
        return self.store.load("projects", project_key)
