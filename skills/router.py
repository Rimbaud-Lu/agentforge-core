from skills.code.generate_api import generate_api
from skills.testing.run_tests import run_tests

def select_skill(task):
    if "api" in task:
        return generate_api
    
    if "test" in task:
        return run_tests
    
    return None
