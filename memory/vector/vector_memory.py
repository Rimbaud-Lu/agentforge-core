from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

class VectorMemory:
    """Vector Memory using Qdrant for storing and searching embeddings"""
    
    def __init__(self, collection="agent_memory"):
        self.client = QdrantClient(":memory:")
        self.collection = collection
        
        self.client.recreate_collection(
            collection_name=self.collection,
            vectors_config=VectorParams(size=1536, distance=Distance.COSINE)
        )
    
    def add_vector(self, id, vector, payload):
        """Add a vector to the memory"""
        self.client.upsert(
            collection_name=self.collection,
            points=[
                {
                    "id": id,
                    "vector": vector,
                    "payload": payload
                }
            ]
        )
    
    def search(self, vector, limit=5):
        """Search for similar vectors"""
        return self.client.search(
            collection_name=self.collection,
            query_vector=vector,
            limit=limit
        )
