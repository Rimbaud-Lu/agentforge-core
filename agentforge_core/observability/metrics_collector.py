from __future__ import annotations

from collections import Counter


class MetricsCollector:
    def summarize(self, events: list[dict]) -> dict:
        status_counter = Counter()
        skill_counter = Counter()
        provider_counter = Counter()

        for event in events:
            if "status" in event:
                status_counter[event["status"]] += 1
            if "skill" in event:
                skill_counter[event["skill"]] += 1
            if "provider" in event:
                provider_counter[event["provider"]] += 1

        return {
            "total_events": len(events),
            "status_counts": dict(status_counter),
            "skill_counts": dict(skill_counter),
            "provider_counts": dict(provider_counter),
        }
