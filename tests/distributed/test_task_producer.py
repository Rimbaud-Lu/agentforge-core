# Test distributed TaskProducer
from distributed.task_producer import TaskProducer


def test_task_producer_initialization():
    """Test TaskProducer can be initialized"""
    producer = TaskProducer(topic="test_topic", bootstrap_servers="localhost:9092")
    assert producer.sent_count == 0


def test_send_task():
    """Test sending a single task"""
    producer = TaskProducer(topic="test_topic")
    task = {"task": "test_task", "data": "test_data"}
    result = producer.send_task(task)
    assert result["status"] == "sent"
    assert producer.sent_count == 1


def test_send_tasks():
    """Test sending multiple tasks"""
    producer = TaskProducer(topic="test_topic")
    tasks = [
        {"task": "task1"},
        {"task": "task2"},
        {"task": "task3"}
    ]
    results = producer.send_tasks(tasks)
    assert len(results) == 3
    assert producer.sent_count == 3


def test_send_task_with_priority():
    """Test sending task with priority"""
    producer = TaskProducer(topic="test_topic")
    task = {"task": "test_task"}
    result = producer.send_task_with_priority(task, priority=5)
    assert result["status"] == "sent"
    assert result["task"]["priority"] == 5
