# Test distributed TaskConsumer
from distributed.task_consumer import TaskConsumer
from distributed.kafka_queue import KafkaQueue


def test_task_consumer_initialization():
    """Test TaskConsumer can be initialized"""
    consumer = TaskConsumer(topic="test_topic", bootstrap_servers="localhost:9092", group_id="test_group")
    assert consumer.topic == "test_topic"
    assert consumer.group_id == "test_group"
    assert consumer.consumed_count == 0


def test_task_consumer_listen():
    """Test listening to tasks"""
    # First add some tasks to the queue
    queue = KafkaQueue(topic="listen_test")
    queue.publish({"task": "task1"})
    queue.publish({"task": "task2"})
    
    consumer = TaskConsumer(topic="listen_test")
    tasks = list(consumer.listen(max_messages=2))
    assert len(tasks) == 2


def test_task_consumer_consume():
    """Test consuming a single task"""
    queue = KafkaQueue(topic="consume_test")
    queue.publish({"task": "task1"})
    queue.publish({"task": "task2"})
    
    consumer = TaskConsumer(topic="consume_test")
    task = consumer.consume()
    assert task == {"task": "task1"}
    assert consumer.consumed_count == 1
