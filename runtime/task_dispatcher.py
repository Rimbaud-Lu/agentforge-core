class TaskDispatcher:
    """Task Dispatcher for distributing tasks to executors"""
    
    def __init__(self, executor):
        self.executor = executor
    
    def dispatch(self, tasks):
        """Dispatch tasks to executor"""
        return self.executor.execute_batch(tasks)
    
    def dispatch_single(self, task):
        """Dispatch a single task"""
        return self.executor.execute(task)
    
    def dispatch_parallel(self, tasks):
        """Dispatch multiple tasks in parallel"""
        # For now, execute sequentially
        # Could be extended to use multiprocessing/threading
        results = []
        for task in tasks:
            result = self.executor.execute(task)
            results.append(result)
        return results
