class TaskNode:
    """Task Node for DAG"""
    
    def __init__(self, id, task, dependencies=None):
        self.id = id
        self.task = task
        self.dependencies = dependencies or []
        self.status = "pending"
    
    def __repr__(self):
        return f"TaskNode(id={self.id}, task={self.task}, status={self.status})"
