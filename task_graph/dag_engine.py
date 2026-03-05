class DAGEngine:
    """DAG Engine for managing task dependencies"""
    
    def __init__(self, task_store):
        self.task_store = task_store
    
    def get_ready_tasks(self):
        """Get tasks that are ready to execute (all dependencies done)"""
        ready = []
        
        for task in self.task_store.all_tasks():
            if task.status == "pending":
                # Check if all dependencies are done
                deps_done = True
                for dep_id in task.dependencies:
                    dep_task = self.task_store.get_task(dep_id)
                    if dep_task is None or dep_task.status != "done":
                        deps_done = False
                        break
                
                if deps_done:
                    ready.append(task)
        
        return ready
    
    def get_task_status(self, task_id):
        """Get status of a specific task"""
        task = self.task_store.get_task(task_id)
        return task.status if task else None
    
    def has_circular_dependency(self, task_id, visited=None):
        """Check for circular dependencies"""
        if visited is None:
            visited = set()
        
        if task_id in visited:
            return True
        
        visited.add(task_id)
        task = self.task_store.get_task(task_id)
        
        if task:
            for dep in task.dependencies:
                if self.has_circular_dependency(dep, visited.copy()):
                    return True
        
        return False
