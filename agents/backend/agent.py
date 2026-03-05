from model_execution.codex.codex_runner import generate_code
from tools.filesystem.writer import write_file

def run_agent(plan):
    print("Running agent with plan:", plan)
    
    code = generate_code(plan["task"])
    
    write_file("generated_project/main.py", code)
