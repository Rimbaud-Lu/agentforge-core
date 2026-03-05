class VectorMemory:
    """Vector Memory using simple in-memory storage (placeholder for Qdrant)"""
    
    def __init__(self, collection="agent_memory"):
        self.collection = collection
        self.vectors = []
        self.payloads = {}
    
    def add_vector(self, id, vector, payload):
        """Add a vector to the memory"""
        self.vectors.append(vector)
        self.payloads[id] = payload
    
    def search(self, vector, limit=5):
        """Search for similar vectors (simple cosine similarity)"""
        results = []
        
        # Simple similarity search
        for i, stored_vec in enumerate(self.vectors):
            if len(vector) == len(stored_vec):
                # Calculate dot product as similarity
                similarity = sum(a * b for a, b in zip(vector, stored_vec))
                results.append({
                    "id": i,
                    "score": similarity,
                    "payload": self.payloads.get(i, {})
                })
        
        # Sort by score and return top results
        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:limit]
    
    def clear(self):
        """Clear all vectors"""
        self.vectors = []
        self.payloads = {}
