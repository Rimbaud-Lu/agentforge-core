from agentforge_core.memory.manager import MemoryManager


def test_memory_session_create_and_append():
    manager = MemoryManager()
    session_id = manager.create_session("build api")
    manager.append_event(session_id, {"type": "started"})
    session = manager.get_session(session_id)
    assert session is not None
    assert session["task"] == "build api"
    assert len(session["events"]) == 1
