"""
Claude Planner for task planning
"""


class ClaudePlanner:
    """Planner using Claude for task decomposition"""
    
    def __init__(self, model=None):
        self.model = model
    
    def create_plan(self, task):
        """Create a plan for the given task"""
        prompt = f"""
        Break down the following task into steps.
        
        Task:
        {task}
        
        Return a list of steps.
        """
        
        if self.model:
            response = self.model.generate(prompt)
        else:
            # Default response when no model is provided
            response = self._default_plan(task)
        
        return self.parse_steps(response)
    
    def parse_steps(self, response):
        """Parse the response into steps"""
        steps = []
        
        for line in response.split("\n"):
            line = line.strip()
            if line:
                # Remove common prefixes like "1.", "-", "*"
                for prefix in ["1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.", "- ", "* "]:
                    if line.startswith(prefix):
                        line = line[len(prefix):].strip()
                        break
                steps.append(line)
        
        return steps
    
    def _default_plan(self, task):
        """Default plan when no model is available"""
        return f"""
        1. Analyze task: {task}
        2. Generate code using appropriate model
        3. Write generated code to files
        4. Return result
        """
    
    def create_detailed_plan(self, task, context=None):
        """Create a detailed plan with context"""
        context_str = ""
        if context:
            context_str = f"\nContext:\n{context}"
        
        prompt = f"""
        Break down the following task into detailed steps.
        
        Task:
        {task}
        {context_str}
        
        For each step, provide:
        - Step number
        - Description
        - Estimated complexity (low/medium/high)
        
        Return a structured plan.
        """
        
        if self.model:
            response = self.model.generate(prompt)
        else:
            response = self._default_plan(task)
        
        return self.parse_steps(response)
