from __future__ import annotations

import os
from typing import Any


class VectorMemoryStore:
    def __init__(self, url: str | None = None):
        self.url = url or os.getenv("QDRANT_URL", "http://localhost:6333")
        self._client = None

    @property
    def client(self):
        if self._client is None:
            from qdrant_client import QdrantClient
            self._client = QdrantClient(url=self.url)
        return self._client

    def upsert_text(self, collection: str, item_id: int, text: str, metadata: dict | None = None) -> dict:
        return {
            "collection": collection,
            "item_id": item_id,
            "text": text,
            "metadata": metadata or {},
            "mode": "stub",
        }

    def search_text(self, collection: str, query: str, limit: int = 5) -> list[dict[str, Any]]:
        return [{
            "collection": collection,
            "query": query,
            "limit": limit,
            "mode": "stub",
        }]
