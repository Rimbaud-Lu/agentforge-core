from task_graph.task_node import TaskNode


class GraphBuilder:
    """Graph Builder for creating task graphs"""
    
    def build_saas_graph(self):
        """Build a SaaS application task graph"""
        backend = TaskNode("backend", "build backend")
        
        frontend = TaskNode("frontend", "build frontend")
        
        tests = TaskNode("tests", "write tests", ["backend"])
        
        deploy = TaskNode("deploy", "deploy app", ["backend", "frontend"])
        
        return [backend, frontend, tests, deploy]
    
    def build_api_graph(self):
        """Build an API project task graph"""
        design = TaskNode("design", "design API")
        
        backend = TaskNode("backend", "implement API", ["design"])
        
        tests = TaskNode("tests", "write tests", ["backend"])
        
        return [design, backend, tests]
    
    def build_fullstack_graph(self):
        """Build a fullstack project task graph"""
        backend = TaskNode("backend", "build backend API")
        
        frontend = TaskNode("frontend", "build frontend UI")
        
        tests = TaskNode("tests", "write tests", ["backend"])
        
        deploy = TaskNode("deploy", "deploy application", ["backend", "frontend", "tests"])
        
        return [backend, frontend, tests, deploy]
    
    def build_custom_graph(self, tasks_with_deps):
        """Build a custom task graph from task definitions"""
        # tasks_with_deps: list of (id, task, dependencies)
        nodes = []
        for task_id, task_name, deps in tasks_with_deps:
            node = TaskNode(task_id, task_name, deps)
            nodes.append(node)
        return nodes
