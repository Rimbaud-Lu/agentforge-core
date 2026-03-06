from __future__ import annotations

from abc import ABC, abstractmethod


class BaseProvider(ABC):
    name: str = "base"

    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> str:
        raise NotImplementedError
