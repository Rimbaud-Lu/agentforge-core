from agentforge_core.model_execution.adapters.executor import ModelExecutor


def test_provider_fallback_to_mock(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    executor = ModelExecutor()
    result = executor.execute("planner", "create api")
    assert "provider" in result
    assert "output" in result
