from tools.filesystem.writer import write_file

def generate_api(name: str):
    code = f'''
from fastapi import APIRouter

router = APIRouter()

@router.get("/{name}")
def get_{name}():
    return {{"message": "{name} endpoint"}}
'''
    
    write_file(f"generated_project/{name}_api.py", code)
    
    return f"{name} API created"
