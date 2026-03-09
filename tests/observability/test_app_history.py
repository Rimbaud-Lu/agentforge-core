from agentforge_core.app import AgentForgeApp


def test_app_execute_records_history():
    app = AgentForgeApp()
    result = app.execute_task("create api")
    summary = app.dashboard_summary()
    assert result["status"] == "success"
    assert summary["metrics"]["total_events"] >= 1
