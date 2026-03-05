class SessionMemory:
    """Session Memory for storing conversation context"""
    
    def __init__(self):
        self.memory = []
    
    def add(self, item):
        """Add an item to session memory"""
        self.memory.append(item)
    
    def get_context(self):
        """Get last 10 items from session"""
        return self.memory[-10:]
    
    def clear(self):
        """Clear session memory"""
        self.memory = []
    
    def get_all(self):
        """Get all session data"""
        return self.memory
