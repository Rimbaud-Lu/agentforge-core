class WorkflowExecutor:
    """Workflow Executor for running tasks"""
    
    def __init__(self, runtime=None):
        self.runtime = runtime
    
    def execute(self, task):
        """Execute a single task"""
        if self.runtime:
            return self.runtime.execute(task)
        else:
            # Default execution - just print and return success
            print(f"Executing: {task}")
            return {"status": "success", "task": task}
    
    def execute_batch(self, tasks):
        """Execute multiple tasks"""
        results = []
        for task in tasks:
            result = self.execute(task)
            results.append(result)
        return results
