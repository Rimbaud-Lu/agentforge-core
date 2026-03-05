from model_execution.router import execute_with_router, route_task
from tools.filesystem.writer import write_file

def run_agent(plan):
    """Run agent with task plan using model router"""
    task = plan["task"]
    
    print("Agent executing task:", task)
    
    # Use model router to determine which model to use
    model = route_task(task)
    print(f"Selected model: {model}")
    
    # Generate code using appropriate model
    code = execute_with_router(task)
    
    # Write generated code
    write_file("generated_project/main.py", code)
    
    return code
