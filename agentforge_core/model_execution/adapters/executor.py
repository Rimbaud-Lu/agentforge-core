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
        provider, fallback = self.registry.get_with_fallback(provider_name)

        try:
            output = provider.generate(prompt, model=model_name)
            used_provider = provider.name
        except Exception:
            output = fallback.generate(prompt, model="mock-model")
            used_provider = fallback.name

        return {
            "provider": used_provider,
            "model": model_name if used_provider != "mock" else "mock-model",
            "output": output,
        }
