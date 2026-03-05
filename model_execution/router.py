"""
Model Router - Routes tasks to appropriate model based on task type
"""

from model_execution.codex.codex_runner import CodexRunner
from model_execution.deepseek.deepseek_runner import DeepSeekRunner
from model_execution.claude.claude_runner import ClaudeRunner

# Model routing rules
MODEL_RULES = {
    "codex": ["generate", "api", "code", "function", "class"],
    "claude": ["architecture", "design", "explain", "refactor"],
    "deepseek": ["test", "debug", "optimize", "fix"]
}

def route_task(task: str) -> str:
    """Route task to appropriate model"""
    task_lower = task.lower()
    
    for model, keywords in MODEL_RULES.items():
        for keyword in keywords:
            if keyword in task_lower:
                return model
    
    # Default to codex for code generation
    return "codex"

def execute_with_router(task: str):
    """Execute task with appropriate model"""
    model = route_task(task)
    
    print(f"Routing task to: {model}")
    
    if model == "codex":
        runner = CodexRunner()
        return runner.generate(task)
    elif model == "deepseek":
        runner = DeepSeekRunner()
        return runner.generate(task)
    elif model == "claude":
        runner = ClaudeRunner()
        return runner.generate(task)
    else:
        raise ValueError(f"Unknown model: {model}")
