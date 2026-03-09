"""
Kafka Queue for distributed task messaging
"""
import json
import threading

# Use in-memory fallback by default (Kafka is optional)
_USE_KAFKA = False

try:
    from kafka import KafkaProducer, KafkaConsumer
    _USE_KAFKA = True
except ImportError:
    pass


# Module-level queue storage for in-memory mode
_queue_storage = {}
_storage_lock = threading.Lock()


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


class KafkaQueue:
    """Kafka-based message queue with in-memory fallback"""
    
    def __init__(self, topic="agent_tasks", bootstrap_servers="localhost:9092", use_memory_fallback=True):
        self.topic = topic
        self.bootstrap_servers = bootstrap_servers
        self._producer = None
        self._consumer = None
        self._use_memory = use_memory_fallback or not _USE_KAFKA
        self._lock = threading.Lock()
        
        # Get or create shared queue for this topic
        with _storage_lock:
            if topic not in _queue_storage:
                _queue_storage[topic] = []
            self._queue = _queue_storage[topic]
    
    @property
    def producer(self):
        """Lazy initialization of producer"""
        if self._use_memory:
            return None
        if self._producer is None:
            try:
                self._producer = KafkaProducer(
                    bootstrap_servers=self.bootstrap_servers,
                    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
                    api_version_auto_timeout_ms=2000
                )
            except Exception:
                self._use_memory = True
                return None
        return self._producer
    
    def publish(self, task):
        """Publish a task to the queue"""
        if self._use_memory or self.producer is None:
            with self._lock:
                self._queue.append(task)
            return
        
        try:
            self.producer.send(self.topic, task)
            self.producer.flush()
        except Exception:
            # Fallback to in-memory
            with self._lock:
                self._queue.append(task)
    
    def create_consumer(self, group_id="agent-workers"):
        """Create a consumer for the queue"""
        if self._use_memory:
            return InMemoryConsumer(self._queue)
        
        try:
            return KafkaConsumer(
                self.topic,
                bootstrap_servers=self.bootstrap_servers,
                value_deserializer=lambda m: json.loads(m.decode("utf-8")),
                group_id=group_id,
                auto_offset_reset='earliest',
                api_version_auto_timeout_ms=2000
            )
        except Exception:
            # Fallback to in-memory
            return InMemoryConsumer(self._queue)
