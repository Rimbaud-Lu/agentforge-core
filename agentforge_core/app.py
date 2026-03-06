from __future__ import annotations

from control_plane.planner.planner import plan_task
from router.skill_router import SkillRouter
from router.model_router import ModelRouter
from workflow.workflow_executor import WorkflowExecutor
from observability.token_tracker import TokenTracker
from agentforge_core.model_execution.adapters.executor import ModelExecutor
from agentforge_core.result_types import TaskResult
from agentforge_core.memory.manager import MemoryManager
from agentforge_core.workflow.manager import WorkflowManager


class AgentForgeApp:
    def __init__(self):
        self.skill_router = SkillRouter()
        self.model_router = ModelRouter()
        self.workflow_executor = WorkflowExecutor()
        self.model_executor = ModelExecutor()
        self.token_tracker = TokenTracker()
        self.memory = MemoryManager()
        self.workflow_manager = WorkflowManager()

    def execute_task(self, task: str, model_override: str | None = None, project_key: str = "default") -> dict:
        session_id = self.memory.create_session(task)
        plan = plan_task(task)
        skill = self.skill_router.route(task)
        selected_model = model_override or self.model_router.select_model(skill)

        workflow_id = self.workflow_manager.create_workflow(
            task=task,
            plan=plan,
            skill=skill,
            model=selected_model,
        )

        self.memory.append_event(session_id, {"type": "plan_created", "plan": plan})
        self.workflow_manager.append_event(workflow_id, {"type": "session_bound", "session_id": session_id})

        exec_payload = self.model_executor.execute(
            role=skill,
            prompt=f"Task: {task}\nPlan: {plan}\nSkill: {skill}",
        )

        self.memory.append_event(session_id, {
            "type": "provider_output",
            "provider": exec_payload["provider"],
            "provider_model": exec_payload["model"],
        })

        workflow_result = self.workflow_executor.execute({
            "task": task,
            "plan": plan,
            "skill": skill,
            "model": selected_model,
            "provider_output": exec_payload["output"],
        })

        self.memory.save_project_context(project_key, {
            "last_task": task,
            "last_skill": skill,
            "last_model": selected_model,
            "last_workflow_id": workflow_id,
        })

        self.workflow_manager.mark_completed(workflow_id, workflow_result)

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
        payload["session_id"] = session_id
        payload["workflow_id"] = workflow_id
        payload["project_context"] = self.memory.get_project_context(project_key)
        return payload

    def resume_workflow(self, workflow_id: str) -> dict | None:
        return self.workflow_manager.resume(workflow_id)
