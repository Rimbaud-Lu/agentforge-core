from agentforge_core.app import AgentForgeApp


def test_app_execute_and_resume():
    app = AgentForgeApp()
    result = app.execute_task("create api")
    workflow_id = result["workflow_id"]
    resumed = app.resume_workflow(workflow_id)
    assert resumed is not None
    assert resumed["workflow_id"] == workflow_id
    assert resumed["status"] == "completed"
