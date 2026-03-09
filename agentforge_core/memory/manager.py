from __future__ import annotations

import os
from uuid import uuid4

from agentforge_core.memory.in_memory_store import InMemoryStore
from agentforge_core.memory.redis_store import RedisStore


class MemoryManager:
    def __init__(self, store=None, vector_store=None):
        backend = os.getenv("AGENTFORGE_MEMORY_BACKEND", "memory").lower()

        if store is not None:
            self.store = store
        elif backend == "redis":
            self.store = RedisStore()
        else:
            self.store = InMemoryStore()

        self.vector_store = vector_store
        if self.vector_store is None and os.getenv("QDRANT_URL"):
            from agentforge_core.memory.vector_store import VectorMemoryStore
            self.vector_store = VectorMemoryStore()

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
        if self.vector_store:
            self.vector_store.upsert_text(
                collection="project_context",
                item_id=abs(hash(project_key)) % 10**8,
                text=str(context),
                metadata={"project_key": project_key},
            )

    def get_project_context(self, project_key: str) -> dict | None:
        return self.store.load("projects", project_key)
