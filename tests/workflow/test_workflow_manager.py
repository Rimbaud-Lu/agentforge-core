from agentforge_core.workflow.manager import WorkflowManager
from agentforge_core.workflow.store import WorkflowStore


def test_workflow_manager_complete(tmp_path):
    store = WorkflowStore(root=str(tmp_path))
    manager = WorkflowManager(store=store)
    workflow_id = manager.create_workflow("build api", "plan", "backend", "mock-model")
    manager.append_event(workflow_id, {"type": "running"})
    payload = manager.mark_completed(workflow_id, {"status": "success"})
    assert payload["status"] == "completed"
    assert payload["result"]["status"] == "success"
