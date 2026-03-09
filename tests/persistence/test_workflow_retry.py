from agentforge_core.workflow.manager import WorkflowManager
from agentforge_core.workflow.store import WorkflowStore


def test_workflow_retry_increments_count(tmp_path):
    store = WorkflowStore(root=str(tmp_path))
    manager = WorkflowManager(store=store)
    workflow_id = manager.create_workflow("build api", "plan", "backend", "mock-model")
    payload = manager.retry(workflow_id)
    assert payload["status"] == "retrying"
    assert payload["retry_count"] == 1
