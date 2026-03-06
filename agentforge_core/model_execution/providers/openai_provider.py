from __future__ import annotations

import os

from agentforge_core.model_execution.providers.base import BaseProvider


class OpenAIProvider(BaseProvider):
    name = "openai"

    def generate(self, prompt: str, **kwargs) -> str:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is not configured")
        # Placeholder for real API call integration.
        return f"[openai-simulated]\n{prompt}"
