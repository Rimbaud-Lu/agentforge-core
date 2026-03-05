from memory.session.session_memory import SessionMemory
from memory.project.project_memory import ProjectMemory
from memory.vector.vector_memory import VectorMemory
from memory.cache.cache_memory import CacheMemory
from memory.knowledge.knowledge_memory import KnowledgeMemory


class MemoryManager:
    """Central Memory Manager for all memory systems"""
    
    def __init__(self):
        self.session = SessionMemory()
        self.project = ProjectMemory()
        self.vector = VectorMemory()
        self.cache = CacheMemory()
        self.knowledge = KnowledgeMemory()
    
    # Session Memory methods
    def add_session(self, item):
        """Add item to session memory"""
        self.session.add(item)
    
    def get_session_context(self):
        """Get session context"""
        return self.session.get_context()
    
    def clear_session(self):
        """Clear session memory"""
        self.session.clear()
    
    # Project Memory methods
    def add_project_file(self, path, content):
        """Add file to project memory"""
        self.project.add_file(path, content)
    
    def get_project_file(self, path):
        """Get file from project memory"""
        return self.project.get_file(path)
    
    def set_architecture(self, architecture):
        """Store architecture"""
        self.project.set_architecture(architecture)
    
    def get_architecture(self):
        """Get architecture"""
        return self.project.get_architecture()
    
    # Vector Memory methods
    def add_vector(self, id, vector, payload):
        """Add vector to memory"""
        self.vector.add_vector(id, vector, payload)
    
    def search_vectors(self, vector, limit=5):
        """Search vectors"""
        return self.vector.search(vector, limit)
    
    # Cache Memory methods
    def cache_set(self, key, value):
        """Set cache"""
        self.cache.set(key, value)
    
    def cache_get(self, key):
        """Get cache"""
        return self.cache.get(key)
    
    # Knowledge Memory methods
    def add_knowledge(self, data):
        """Add knowledge"""
        self.knowledge.add(data)
    
    def search_knowledge(self, query):
        """Search knowledge"""
        return self.knowledge.search(query)
