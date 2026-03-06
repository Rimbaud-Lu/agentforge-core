from __future__ import annotations

from control_plane.planner.planner import plan_task
from router.skill_router import SkillRouter
from router.model_router import ModelRouter
from workflow.workflow_executor import WorkflowExecutor
from observability.token_tracker import TokenTracker


class AgentForgeApp:
    def __init__(self):
        self.skill_router = SkillRouter()
        self.model_router = ModelRouter()
        self.executor = WorkflowExecutor()
        self.token_tracker = TokenTracker()

    def execute_task(self, task: str, model_override: str | None = None) -> dict:
        plan = plan_task(task)
        skill = self.skill_router.route(task)
        model = model_override or self.model_router.select_model(skill)
        result = self.executor.execute({
            "task": task,
            "plan": plan,
            "skill": skill,
            "model": model,
        })
        return {
            "task": task,
            "plan": plan,
            "skill": skill,
            "model": model,
            "result": result,
            "token_report": self.token_tracker.report(),
        }
