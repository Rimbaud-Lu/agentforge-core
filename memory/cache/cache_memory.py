import redis
import json

class CacheMemory:
    """Redis Cache Memory for short-term data storage"""
    
    def __init__(self):
        self.client = redis.Redis(host="localhost", port=6379, decode_responses=True)
    
    def set(self, key, value):
        """Set a value in cache"""
        self.client.set(key, json.dumps(value))
    
    def get(self, key):
        """Get a value from cache"""
        value = self.client.get(key)
        if value:
            return json.loads(value)
        return None
    
    def delete(self, key):
        """Delete a key from cache"""
        self.client.delete(key)
    
    def exists(self, key):
        """Check if key exists"""
        return self.client.exists(key)
