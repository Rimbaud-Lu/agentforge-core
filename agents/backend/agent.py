from skills.code.generate_api import generate_api

def run_agent(plan):
    task = plan["task"]
    
    print("Agent executing task:", task)
    
    if "api" in task:
        result = generate_api("sample")
        print(result)
    else:
        print("No skill matched task")
