"""
Agent Registry for managing multiple agents
"""


class AgentRegistry:
    """Registry for managing and discovering agents"""
    
    def __init__(self):
        self.agents = {}
        self.metadata = {}
    
    def register(self, name, agent, metadata=None):
        """Register an agent"""
        self.agents[name] = agent
        self.metadata[name] = metadata or {}
    
    def unregister(self, name):
        """Unregister an agent"""
        if name in self.agents:
            del self.agents[name]
            del self.metadata[name]
    
    def get(self, name):
        """Get an agent by name"""
        return self.agents.get(name)
    
    def list_agents(self):
        """List all registered agent names"""
        return list(self.agents.keys())
    
    def get_metadata(self, name):
        """Get metadata for an agent"""
        return self.metadata.get(name, {})
    
    def update_metadata(self, name, metadata):
        """Update metadata for an agent"""
        if name in self.metadata:
            self.metadata[name].update(metadata)
        else:
            self.metadata[name] = metadata
    
    def find_agents_by_capability(self, capability):
        """Find agents with a specific capability"""
        matching = []
        for name, metadata in self.metadata.items():
            capabilities = metadata.get("capabilities", [])
            if capability in capabilities:
                matching.append(name)
        return matching
    
    def get_all_metadata(self):
        """Get all agent metadata"""
        return dict(self.metadata)
    
    def clear(self):
        """Clear all registered agents"""
        self.agents.clear()
        self.metadata.clear()
