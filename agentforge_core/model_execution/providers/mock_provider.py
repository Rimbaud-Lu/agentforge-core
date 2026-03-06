from __future__ import annotations

from agentforge_core.model_execution.providers.base import BaseProvider


class MockProvider(BaseProvider):
    name = "mock"

    def generate(self, prompt: str, **kwargs) -> str:
        return f"[mock-generated]\n{prompt}"
