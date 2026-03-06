from __future__ import annotations

from abc import ABC, abstractmethod


class BaseMemoryStore(ABC):
    @abstractmethod
    def save(self, namespace: str, key: str, value: dict) -> None:
        raise NotImplementedError

    @abstractmethod
    def load(self, namespace: str, key: str) -> dict | None:
        raise NotImplementedError

    @abstractmethod
    def list_keys(self, namespace: str) -> list[str]:
        raise NotImplementedError
