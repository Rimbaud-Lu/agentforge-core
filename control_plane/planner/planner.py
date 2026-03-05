def plan_task(task: str):
    print("Planning task:", task)
    
    return {
        "type": "generate_project",
        "task": task
    }
