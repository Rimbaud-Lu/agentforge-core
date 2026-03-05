"""
Kafka Queue for distributed task messaging
"""

try:
    from kafka import KafkaProducer, KafkaConsumer
    import json
    
    class KafkaQueue:
        """Kafka-based message queue for distributed task processing"""
        
        def __init__(self, topic="agent_tasks", bootstrap_servers="localhost:9092"):
            self.topic = topic
            self.bootstrap_servers = bootstrap_servers
            self._producer = None
            self._consumer = None
        
        @property
        def producer(self):
            """Lazy initialization of producer"""
            if self._producer is None:
                self._producer = KafkaProducer(
                    bootstrap_servers=self.bootstrap_servers,
                    value_serializer=lambda v: json.dumps(v).encode("utf-8")
                )
            return self._producer
        
        def publish(self, task):
            """Publish a task to the queue"""
            self.producer.send(self.topic, task)
            self.producer.flush()
        
        def create_consumer(self, group_id="agent-workers"):
            """Create a consumer for the queue"""
            return KafkaConsumer(
                self.topic,
                bootstrap_servers=self.bootstrap_servers,
                value_deserializer=lambda m: json.loads(m.decode("utf-8")),
                group_id=group_id,
                auto_offset_reset='earliest'
            )

except ImportError:
    # Fallback implementation using in-memory queue
    import json
    import threading
    
    class KafkaQueue:
        """In-memory fallback for Kafka queue"""
        
        def __init__(self, topic="agent_tasks", bootstrap_servers="localhost:9092"):
            self.topic = topic
            self.bootstrap_servers = bootstrap_servers
            self._queue = []
            self._lock = threading.Lock()
        
        def publish(self, task):
            """Publish a task to the queue"""
            with self._lock:
                self._queue.append(task)
        
        def create_consumer(self, group_id="agent-workers"):
            """Create a consumer (returns an iterator)"""
            return InMemoryConsumer(self._queue)


class InMemoryConsumer:
    """In-memory consumer fallback"""
    
    def __init__(self, queue):
        self.queue = queue
        self._index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index >= len(self.queue):
            raise StopIteration
        item = self.queue[self._index]
        self._index += 1
        return MockMessage(item)
    
    def close(self):
        pass


class MockMessage:
    """Mock Kafka message"""
    
    def __init__(self, value):
        self.value = value
