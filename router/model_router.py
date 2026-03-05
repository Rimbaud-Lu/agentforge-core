"""
Model Router for routing tasks to appropriate models
"""


class ModelRouter:
    """Router for selecting appropriate AI model based on skill"""
    
    def __init__(self):
        self.model_map = {
            "generate_api": "codex",
            "generate_tests": "deepseek",
            "deploy_service": "deepseek",
            "debug_code": "deepseek",
            "write_docs": "claude",
            "refactor_code": "claude",
            "generate_frontend": "codex",
            "generate_backend": "codex",
            "general_task": "claude",
        }
        
        self.model_descriptions = {
            "codex": "Best for code generation, APIs, functions",
            "deepseek": "Best for debugging, testing, optimization",
            "claude": "Best for architecture, documentation, refactoring",
            "gpt4": "General purpose, best for complex reasoning",
        }
    
    def select_model(self, skill):
        """Select appropriate model for the given skill"""
        return self.model_map.get(skill, "claude")
    
    def get_model_description(self, model):
        """Get description of a model"""
        return self.model_descriptions.get(model, "General purpose model")
    
    def add_model_mapping(self, skill, model):
        """Add or update a skill to model mapping"""
        self.model_map[skill] = model
    
    def list_mappings(self):
        """List all skill to model mappings"""
        return dict(self.model_map)
    
    def get_best_model(self, task_type):
        """Get best model for a task type"""
        type_map = {
            "code_generation": "codex",
            "testing": "deepseek",
            "debugging": "deepseek",
            "documentation": "claude",
            "architecture": "claude",
            "refactoring": "claude",
        }
        return type_map.get(task_type, "claude")
