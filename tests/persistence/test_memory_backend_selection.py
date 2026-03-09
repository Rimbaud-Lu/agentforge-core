from agentforge_core.memory.manager import MemoryManager


def test_memory_manager_defaults_to_inmemory():
    manager = MemoryManager()
    assert manager.store is not None
