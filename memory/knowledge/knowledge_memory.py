class KnowledgeMemory:
    """Knowledge Memory for storing general knowledge and documentation"""
    
    def __init__(self):
        self.knowledge = []
    
    def add(self, data):
        """Add knowledge data"""
        self.knowledge.append(data)
    
    def search(self, query):
        """Search knowledge base"""
        results = []
        for item in self.knowledge:
            if query in str(item):
                results.append(item)
        return results
    
    def get_all(self):
        """Get all knowledge"""
        return self.knowledge
    
    def clear(self):
        """Clear knowledge base"""
        self.knowledge = []
