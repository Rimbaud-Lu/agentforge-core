from __future__ import annotations

from agentforge_core.workflow.store import WorkflowStore
from agentforge_core.workflow.task_graph import TaskGraph


class WorkflowManager:
    def __init__(self, store=None):
        self.store = store or WorkflowStore()

    def create_workflow(self, task: str, plan: str, skill: str, model: str) -> str:
        graph = TaskGraph()
        graph.add_node("plan", {"task": task, "plan": plan})
        graph.add_node("execute", {"skill": skill, "model": model})
        graph.add_edge("plan", "execute")

        payload = {
            "status": "created",
            "task": task,
            "plan": plan,
            "skill": skill,
            "model": model,
            "task_graph": graph.to_dict(),
            "events": [],
        }
        return self.store.create(payload)

    def append_event(self, workflow_id: str, event: dict) -> dict:
        payload = self.store.load(workflow_id)
        if not payload:
            raise ValueError(f"Workflow not found: {workflow_id}")
        payload.setdefault("events", []).append(event)
        self.store.save(workflow_id, payload)
        return payload

    def mark_completed(self, workflow_id: str, result: dict) -> dict:
        payload = self.store.load(workflow_id)
        if not payload:
            raise ValueError(f"Workflow not found: {workflow_id}")
        payload["status"] = "completed"
        payload["result"] = result
        self.store.save(workflow_id, payload)
        return payload

    def mark_failed(self, workflow_id: str, error: str) -> dict:
        payload = self.store.load(workflow_id)
        if not payload:
            raise ValueError(f"Workflow not found: {workflow_id}")
        payload["status"] = "failed"
        payload["error"] = error
        self.store.save(workflow_id, payload)
        return payload

    def resume(self, workflow_id: str) -> dict | None:
        return self.store.load(workflow_id)
