from agentforge_core.app import AgentForgeApp


def test_execute_task_returns_structure():
    app = AgentForgeApp()
    result = app.execute_task("create api")
    assert "skill" in result
    assert "model" in result
    assert "result" in result
    assert result["result"]["status"] == "success"
