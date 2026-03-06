from __future__ import annotations

from control_plane.planner.planner import plan_task
from router.skill_router import SkillRouter
from router.model_router import ModelRouter
from workflow.workflow_executor import WorkflowExecutor
from observability.token_tracker import TokenTracker
from agentforge_core.model_execution.adapters.executor import ModelExecutor
from agentforge_core.result_types import TaskResult


class AgentForgeApp:
    def __init__(self):
        self.skill_router = SkillRouter()
        self.model_router = ModelRouter()
        self.workflow_executor = WorkflowExecutor()
        self.model_executor = ModelExecutor()
        self.token_tracker = TokenTracker()

    def execute_task(self, task: str, model_override: str | None = None) -> dict:
        plan = plan_task(task)
        skill = self.skill_router.route(task)
        selected_model = model_override or self.model_router.select_model(skill)

        exec_payload = self.model_executor.execute(
            role=skill,
            prompt=f"Task: {task}\nPlan: {plan}\nSkill: {skill}",
        )

        workflow_result = self.workflow_executor.execute({
            "task": task,
            "plan": plan,
            "skill": skill,
            "model": selected_model,
            "provider_output": exec_payload["output"],
        })

        result = TaskResult(
            status=workflow_result.get("status", "success"),
            task=task,
            skill=skill,
            model=selected_model,
            output=workflow_result,
            error=None,
        )
        payload = result.to_dict()
        payload["plan"] = plan
        payload["provider"] = exec_payload["provider"]
        payload["provider_model"] = exec_payload["model"]
        payload["token_report"] = self.token_tracker.report()
        return payload
