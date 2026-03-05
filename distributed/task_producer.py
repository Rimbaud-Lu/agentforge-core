from distributed.kafka_queue import KafkaQueue


class TaskProducer:
    """Task Producer for sending tasks to distributed workers"""
    
    def __init__(self, topic="agent_tasks", bootstrap_servers="localhost:9092"):
        self.queue = KafkaQueue(topic=topic, bootstrap_servers=bootstrap_servers)
        self.sent_count = 0
    
    def send_task(self, task):
        """Send a task to the queue"""
        self.queue.publish(task)
        self.sent_count += 1
        return {"status": "sent", "task": task}
    
    def send_tasks(self, tasks):
        """Send multiple tasks to the queue"""
        results = []
        for task in tasks:
            result = self.send_task(task)
            results.append(result)
        return results
    
    def send_task_with_priority(self, task, priority=1):
        """Send a task with priority"""
        task_with_priority = {
            **task,
            "priority": priority
        }
        return self.send_task(task_with_priority)
    
    def close(self):
        """Close the producer"""
        if hasattr(self.queue, 'producer') and self.queue._producer:
            self.queue.producer.close()
