from __future__ import annotations

from agentforge_core.observability.history import ExecutionHistory


class DashboardAPI:
    def __init__(self, history=None):
        self.history = history or ExecutionHistory()

    def get_summary(self, limit: int = 100) -> dict:
        return self.history.dashboard_summary(limit=limit)

    def get_recent_events(self, limit: int = 20) -> list[dict]:
        return self.history.recent_events(limit=limit)
