from agentforge_core.dashboard.api import DashboardAPI
from agentforge_core.observability.event_store import EventStore
from agentforge_core.observability.history import ExecutionHistory


def test_dashboard_summary_has_metrics(tmp_path):
    store = EventStore(root=str(tmp_path))
    history = ExecutionHistory(store=store)
    history.record_execution({
        "task": "build api",
        "status": "success",
        "skill": "backend",
        "model": "mock-model",
        "provider": "mock",
        "workflow_id": "wf-1",
        "session_id": "session-1",
    })
    api = DashboardAPI(history=history)
    payload = api.get_summary()
    assert "events" in payload
    assert "metrics" in payload
    assert payload["metrics"]["total_events"] == 1
