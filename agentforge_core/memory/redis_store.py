from __future__ import annotations

import json
import os

import redis

from agentforge_core.memory.base import BaseMemoryStore


class RedisStore(BaseMemoryStore):
    def __init__(self, redis_url: str | None = None):
        self.redis_url = redis_url or os.getenv("REDIS_URL", "redis://localhost:6379/0")
        self.client = redis.from_url(self.redis_url, decode_responses=True)

    def _key(self, namespace: str, key: str) -> str:
        return f"agentforge:{namespace}:{key}"

    def save(self, namespace: str, key: str, value: dict) -> None:
        self.client.set(self._key(namespace, key), json.dumps(value, ensure_ascii=False))

    def load(self, namespace: str, key: str) -> dict | None:
        raw = self.client.get(self._key(namespace, key))
        if raw is None:
            return None
        return json.loads(raw)

    def list_keys(self, namespace: str) -> list[str]:
        pattern = f"agentforge:{namespace}:*"
        keys = self.client.keys(pattern)
        prefix = f"agentforge:{namespace}:"
        return [k[len(prefix):] for k in keys]
