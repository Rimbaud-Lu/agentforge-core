"""
Skill Router for routing tasks to appropriate skills
"""


class SkillRouter:
    """Router for selecting appropriate skills based on task"""
    
    def __init__(self):
        self.skill_map = {
            "generate_api": ["api", "endpoint", "route"],
            "generate_tests": ["test", "testing", "spec"],
            "deploy_service": ["deploy", "deployment", "docker"],
            "debug_code": ["debug", "fix", "bug", "error"],
            "write_docs": ["docs", "documentation", "readme"],
            "refactor_code": ["refactor", "improve", "optimize"],
            "generate_frontend": ["frontend", "ui", "react", "vue"],
            "generate_backend": ["backend", "server", "api"],
        }
    
    def route(self, task):
        """Route task to appropriate skill"""
        task_lower = task.lower()
        
        for skill, keywords in self.skill_map.items():
            for keyword in keywords:
                if keyword in task_lower:
                    return skill
        
        return "general_task"
    
    def get_skill_keywords(self, skill):
        """Get keywords for a specific skill"""
        return self.skill_map.get(skill, [])
    
    def add_skill(self, skill_name, keywords):
        """Add a new skill with keywords"""
        self.skill_map[skill_name] = keywords
    
    def list_skills(self):
        """List all available skills"""
        return list(self.skill_map.keys())
