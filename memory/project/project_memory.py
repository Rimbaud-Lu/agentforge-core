class ProjectMemory:
    """Project Memory for storing project-specific data"""
    
    def __init__(self):
        self.files = {}
        self.architecture = None
        self.api_design = None
        self.task_graph = None
    
    def add_file(self, path, content):
        """Add a file to project memory"""
        self.files[path] = content
    
    def get_file(self, path):
        """Get a file from project memory"""
        return self.files.get(path)
    
    def set_architecture(self, architecture):
        """Store architecture design"""
        self.architecture = architecture
    
    def get_architecture(self):
        """Get architecture design"""
        return self.architecture
    
    def set_api_design(self, api_design):
        """Store API design"""
        self.api_design = api_design
    
    def get_api_design(self):
        """Get API design"""
        return self.api_design
    
    def set_task_graph(self, task_graph):
        """Store task graph"""
        self.task_graph = task_graph
    
    def get_task_graph(self):
        """Get task graph"""
        return self.task_graph
    
    def get_all_files(self):
        """Get all files"""
        return self.files
