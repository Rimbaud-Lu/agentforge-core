class TaskStore:
    """Task Store for managing tasks"""
    
    def __init__(self):
        self.tasks = {}
    
    def add_task(self, task):
        """Add a task to the store"""
        self.tasks[task.id] = task
    
    def get_task(self, id):
        """Get a task by ID"""
        return self.tasks.get(id)
    
    def all_tasks(self):
        """Get all tasks"""
        return list(self.tasks.values())
    
    def get_tasks_by_status(self, status):
        """Get tasks by status"""
        return [t for t in self.tasks.values() if t.status == status]
    
    def clear(self):
        """Clear all tasks"""
        self.tasks = {}
