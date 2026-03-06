from __future__ import annotations

from agentforge_core.config_loader import load_all_configs
from agentforge_core.model_execution.providers.registry import ProviderRegistry


class ModelExecutor:
    def __init__(self):
        self.registry = ProviderRegistry()
        self.configs = load_all_configs()

    def execute(self, role: str, prompt: str) -> dict:
        models = self.configs.get("models", {})
        selected = models.get(role, {}) if isinstance(models, dict) else {}
        provider_name = selected.get("provider", "mock")
        model_name = selected.get("model", "mock-model")
        provider = self.registry.get(provider_name)
        output = provider.generate(prompt, model=model_name)
        return {
            "provider": provider_name,
            "model": model_name,
            "output": output,
        }
