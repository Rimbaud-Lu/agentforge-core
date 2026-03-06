from agentforge_core.model_execution.providers.registry import ProviderRegistry


def test_registry_has_default_mock():
    registry = ProviderRegistry()
    assert "mock" in registry.list_names()
