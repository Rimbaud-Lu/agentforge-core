from distributed.kafka_queue import KafkaQueue


class TaskConsumer:
    """Task Consumer for receiving tasks from distributed workers"""
    
    def __init__(self, topic="agent_tasks", bootstrap_servers="localhost:9092", group_id="agent-workers"):
        self.queue = KafkaQueue(topic=topic, bootstrap_servers=bootstrap_servers)
        self.group_id = group_id
        self.consumed_count = 0
    
    def listen(self, max_messages=None):
        """Listen for tasks from the queue"""
        consumer = self.queue.create_consumer(group_id=self.group_id)
        
        messages_received = 0
        try:
            for message in consumer:
                yield message.value
                self.consumed_count += 1
                messages_received += 1
                
                if max_messages and messages_received >= max_messages:
                    break
        finally:
            consumer.close()
    
    def consume(self, timeout=1):
        """Consume a single task with timeout"""
        consumer = self.queue.create_consumer(group_id=self.group_id)
        try:
            for message in consumer:
                self.consumed_count += 1
                return message.value
        except StopIteration:
            return None
        finally:
            consumer.close()
    
    def close(self):
        """Close the consumer"""
        pass
