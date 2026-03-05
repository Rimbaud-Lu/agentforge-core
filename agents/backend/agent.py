from skills.router import select_skill
from model_execution.router import select_model
from tools.filesystem.writer import write_file

def run_agent(plan):
    task = plan["task"]
    
    skill = select_skill(task)
    
    if skill:
        result = skill(task)
    else:
        model = select_model(task)
        result = model(task)
    
    write_file("generated_project/output.py", result)
    
    return result
