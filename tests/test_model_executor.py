from agentforge_core.model_execution.adapters.executor import ModelExecutor


def test_model_executor_returns_output():
    executor = ModelExecutor()
    result = executor.execute("planner", "create fastapi project")
    assert "provider" in result
    assert "model" in result
    assert "output" in result
