from __future__ import annotations

from agentforge_core.model_execution.providers.mock_provider import MockProvider
from agentforge_core.model_execution.providers.openai_provider import OpenAIProvider


class ProviderRegistry:
    def __init__(self):
        self._providers = {
            "mock": MockProvider(),
            "openai": OpenAIProvider(),
        }

    def get(self, provider_name: str):
        return self._providers.get(provider_name, self._providers["mock"])

    def list_names(self):
        return list(self._providers.keys())
