"""
Metrics module for Prometheus monitoring
"""

try:
    from prometheus_client import Counter, Histogram, start_http_server
    
    task_counter = Counter(
        "agent_tasks_total",
        "Total number of tasks executed"
    )
    
    skill_counter = Counter(
        "skill_calls_total",
        "Total number of skill calls"
    )
    
    token_counter = Counter(
        "token_usage_total",
        "Total tokens used"
    )
    
    task_latency = Histogram(
        "task_latency_seconds",
        "Task execution latency"
    )
    
    error_counter = Counter(
        "agent_errors_total",
        "Total number of errors"
    )
    
    def start_metrics_server(port=8001):
        """Start Prometheus metrics HTTP server"""
        start_http_server(port)
        return True

except ImportError:
    # Fallback when prometheus_client is not installed
    class MockCounter:
        def inc(self, n=1): pass
    
    class MockHistogram:
        def observe(self, n): pass
    
    task_counter = MockCounter()
    skill_counter = MockCounter()
    token_counter = MockCounter()
    task_latency = MockHistogram()
    error_counter = MockCounter()
    
    def start_metrics_server(port=8001):
        """Fallback - just print"""
        print(f"Metrics server not started (prometheus_client not installed)")
        return False
