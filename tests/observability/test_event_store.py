from agentforge_core.observability.event_store import EventStore


def test_event_store_append_and_list(tmp_path):
    store = EventStore(root=str(tmp_path))
    store.append({"task": "a", "status": "success"})
    events = store.list_events()
    assert len(events) == 1
    assert events[0]["task"] == "a"
