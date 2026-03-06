class WorkflowExecutor:
    """Workflow Executor for running tasks"""

    def __init__(self, runtime=None):
        self.runtime = runtime

    def execute(self, task):
        if self.runtime:
            return self.runtime.execute(task)

        if isinstance(task, dict):
            return {
                "status": "success",
                "mode": "provider-backed-simulated",
                "task": task.get("task"),
                "skill": task.get("skill"),
                "model": task.get("model"),
                "message": f"Executed task via {task.get('skill')} on {task.get('model')}",
                "provider_output_preview": str(task.get("provider_output", ""))[:300],
            }

        return {
            "status": "success",
            "mode": "local-simulated",
            "task": task,
            "message": f"Executed task: {task}"
        }

    def execute_batch(self, tasks):
        return [self.execute(task) for task in tasks]
