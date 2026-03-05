"""
Telemetry module for tracking agent operations
"""

import time
from observability.metrics import task_counter, task_latency, skill_counter, error_counter


class Telemetry:
    """Telemetry for tracking agent operations"""
    
    def __init__(self):
        self.task_start_times = {}
    
    def record_task_start(self, task_name):
        """Record the start of a task"""
        start = time.time()
        task_counter.inc()
        self.task_start_times[task_name] = start
        return start
    
    def record_task_end(self, task_name, start_time):
        """Record the end of a task"""
        duration = time.time() - start_time
        task_latency.observe(duration)
        return duration
    
    def record_skill_call(self):
        """Record a skill call"""
        skill_counter.inc()
    
    def record_error(self):
        """Record an error"""
        error_counter.inc()
    
    def track_task(self, task_name):
        """Context manager for tracking task duration"""
        return TaskTracker(self, task_name)


class TaskTracker:
    """Context manager for tracking task execution"""
    
    def __init__(self, telemetry, task_name):
        self.telemetry = telemetry
        self.task_name = task_name
    
    def __enter__(self):
        self.start = self.telemetry.record_task_start(self.task_name)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.telemetry.record_task_end(self.task_name, self.start)
        if exc_type:
            self.telemetry.record_error()
