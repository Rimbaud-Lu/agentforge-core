from __future__ import annotations

from datetime import datetime, timezone

from agentforge_core.observability.event_store import EventStore
from agentforge_core.observability.metrics_collector import MetricsCollector


class ExecutionHistory:
    def __init__(self, store=None, metrics=None):
        self.store = store or EventStore()
        self.metrics = metrics or MetricsCollector()

    def record_execution(self, payload: dict) -> None:
        event = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "task": payload.get("task"),
            "status": payload.get("status"),
            "skill": payload.get("skill"),
            "model": payload.get("model"),
            "provider": payload.get("provider"),
            "workflow_id": payload.get("workflow_id"),
            "session_id": payload.get("session_id"),
        }
        self.store.append(event)

    def recent_events(self, limit: int = 20) -> list[dict]:
        return self.store.list_events(limit=limit)

    def dashboard_summary(self, limit: int = 100) -> dict:
        events = self.recent_events(limit=limit)
        return {
            "events": events,
            "metrics": self.metrics.summarize(events),
        }
