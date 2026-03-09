# Test distributed AgentWorker
from distributed.agent_worker import AgentWorker


def test_agent_worker_initialization():
    """Test AgentWorker can be initialized"""
    worker = AgentWorker(runtime=None, topic="test_topic", worker_id="test_worker")
    assert worker.worker_id == "test_worker"
    assert worker.executed_count == 0
    assert worker.running == False


def test_execute_task_without_runtime():
    """Test executing task without runtime"""
    worker = AgentWorker(runtime=None, worker_id="test_worker")
    task = {"task": "test_task", "data": "test_data"}
    result = worker.execute_task(task)
    
    assert result["worker_id"] == "test_worker"
    assert result["task"] == "test_task"
    assert result["status"] == "completed"


def test_execute_task_with_string():
    """Test executing string task"""
    worker = AgentWorker(runtime=None, worker_id="test_worker")
    result = worker.execute_task("simple_task")
    
    assert result["worker_id"] == "test_worker"
    assert result["task"] == "simple_task"
    assert result["status"] == "completed"


def test_get_stats():
    """Test getting worker statistics"""
    worker = AgentWorker(runtime=None, worker_id="test_worker")
    worker.executed_count = 5
    
    stats = worker.get_stats()
    assert stats["worker_id"] == "test_worker"
    assert stats["executed_count"] == 5
    assert stats["running"] == False


def test_stop():
    """Test stopping the worker"""
    worker = AgentWorker(runtime=None, worker_id="test_worker")
    worker.running = True
    worker.stop()
    assert worker.running == False
