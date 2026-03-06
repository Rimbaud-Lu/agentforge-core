from agentforge_core.app import AgentForgeApp


def test_execute_task_returns_structure():
    app = AgentForgeApp()
    result = app.execute_task("create api")
    assert "skill" in result
    assert "model" in result
    assert "output" in result
    assert result["output"]["status"] == "success"
