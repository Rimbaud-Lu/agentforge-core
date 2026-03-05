from task_graph.task_store import TaskStore
from task_graph.dag_engine import DAGEngine


class WorkflowEngine:
    """Workflow Engine for orchestrating task execution"""
    
    def __init__(self):
        self.store = TaskStore()
        self.dag = DAGEngine(self.store)
        self.execution_history = []
    
    def add_tasks(self, tasks):
        """Add tasks to the workflow"""
        for t in tasks:
            self.store.add_task(t)
    
    def next_tasks(self):
        """Get next tasks ready to execute"""
        return self.dag.get_ready_tasks()
    
    def execute_workflow(self, executor):
        """Execute the entire workflow"""
        results = []
        
        while True:
            ready_tasks = self.next_tasks()
            
            if not ready_tasks:
                # Check if all tasks are done
                pending = self.store.get_tasks_by_status("pending")
                if not pending:
                    break
                else:
                    # Deadlock - tasks pending but none can run
                    raise Exception("Workflow deadlock: circular dependency or missing dependencies")
            
            # Execute ready tasks
            for task in ready_tasks:
                task.status = "running"
                result = executor.execute(task.task)
                task.status = "done"
                results.append({
                    "task_id": task.id,
                    "task": task.task,
                    "result": result
                })
                self.execution_history.append(task.id)
        
        return results
    
    def get_status(self):
        """Get workflow status"""
        return {
            "total": len(self.store.all_tasks()),
            "pending": len(self.store.get_tasks_by_status("pending")),
            "running": len(self.store.get_tasks_by_status("running")),
            "done": len(self.store.get_tasks_by_status("done"))
        }
