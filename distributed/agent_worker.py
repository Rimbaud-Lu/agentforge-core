from distributed.task_consumer import TaskConsumer


class AgentWorker:
    """Agent Worker for distributed task execution"""
    
    def __init__(self, runtime=None, topic="agent_tasks", worker_id=None):
        self.runtime = runtime
        self.consumer = TaskConsumer(topic=topic)
        self.worker_id = worker_id or f"worker-{id(self)}"
        self.executed_count = 0
        self.running = False
    
    def execute_task(self, task):
        """Execute a single task"""
        if self.runtime:
            return self.runtime.execute(task)
        else:
            # Default execution
            task_name = task.get("task", "unknown") if isinstance(task, dict) else str(task)
            result = {
                "worker_id": self.worker_id,
                "task": task_name,
                "status": "completed"
            }
            return result
    
    def start(self, max_tasks=None):
        """Start listening for and executing tasks"""
        self.running = True
        print(f"Worker {self.worker_id} started")
        
        try:
            for task in self.consumer.listen(max_messages=max_tasks):
                print(f"Worker {self.worker_id} received task: {task}")
                result = self.execute_task(task)
                print(f"Worker {self.worker_id} executed task: {result}")
                self.executed_count += 1
                
                if max_tasks and self.executed_count >= max_tasks:
                    break
        except KeyboardInterrupt:
            print(f"Worker {self.worker_id} stopped")
        finally:
            self.running = False
    
    def stop(self):
        """Stop the worker"""
        self.running = False
    
    def get_stats(self):
        """Get worker statistics"""
        return {
            "worker_id": self.worker_id,
            "executed_count": self.executed_count,
            "running": self.running
        }
