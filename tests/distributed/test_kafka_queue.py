# Test distributed Kafka queue
from distributed.kafka_queue import KafkaQueue, InMemoryConsumer, MockMessage


def test_kafka_queue_initialization():
    """Test KafkaQueue can be initialized"""
    queue = KafkaQueue(topic="test_topic", bootstrap_servers="localhost:9092")
    assert queue.topic == "test_topic"
    assert queue.bootstrap_servers == "localhost:9092"


def test_kafka_queue_publish():
    """Test publishing tasks to queue"""
    queue = KafkaQueue(topic="test_topic")
    task = {"task": "test_task", "data": "test_data"}
    queue.publish(task)
    # In-memory fallback doesn't persist, just verify no error


def test_kafka_queue_create_consumer():
    """Test creating a consumer"""
    queue = KafkaQueue(topic="test_topic")
    consumer = queue.create_consumer(group_id="test_group")
    assert consumer is not None


def test_in_memory_consumer():
    """Test InMemoryConsumer iteration"""
    queue_data = [
        {"task": "task1"},
        {"task": "task2"},
        {"task": "task3"}
    ]
    consumer = InMemoryConsumer(queue_data)
    tasks = list(consumer)
    assert len(tasks) == 3
    assert tasks[0].value == {"task": "task1"}


def test_mock_message():
    """Test MockMessage"""
    msg = MockMessage({"test": "data"})
    assert msg.value == {"test": "data"}
