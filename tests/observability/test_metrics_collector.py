from agentforge_core.observability.metrics_collector import MetricsCollector


def test_metrics_summary_counts():
    collector = MetricsCollector()
    summary = collector.summarize([
        {"status": "success", "skill": "backend", "provider": "mock"},
        {"status": "success", "skill": "backend", "provider": "mock"},
        {"status": "failed", "skill": "frontend", "provider": "openai"},
    ])
    assert summary["total_events"] == 3
    assert summary["status_counts"]["success"] == 2
    assert summary["provider_counts"]["mock"] == 2
