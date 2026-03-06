from agentforge_core.workflow.store import WorkflowStore


def test_workflow_store_create_and_load(tmp_path):
    store = WorkflowStore(root=str(tmp_path))
    workflow_id = store.create({"status": "created", "task": "x"})
    payload = store.load(workflow_id)
    assert payload is not None
    assert payload["workflow_id"] == workflow_id
    assert payload["task"] == "x"
