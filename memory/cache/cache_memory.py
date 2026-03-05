import json

class CacheMemory:
    """Cache Memory with in-memory fallback (requires Redis for production)"""
    
    def __init__(self):
        self._cache = {}
        self._redis_client = None
        
        # Try to connect to Redis, fallback to in-memory
        try:
            import redis
            self.client = redis.Redis(host="localhost", port=6379, decode_responses=True)
            # Test connection
            self.client.ping()
            self._use_redis = True
        except:
            # Fallback to in-memory cache
            self.client = None
            self._use_redis = False
    
    def set(self, key, value):
        """Set a value in cache"""
        if self._use_redis:
            self.client.set(key, json.dumps(value))
        else:
            self._cache[key] = value
    
    def get(self, key):
        """Get a value from cache"""
        if self._use_redis:
            value = self.client.get(key)
            if value:
                return json.loads(value)
            return None
        else:
            return self._cache.get(key)
    
    def delete(self, key):
        """Delete a key from cache"""
        if self._use_redis:
            self.client.delete(key)
        else:
            self._cache.pop(key, None)
    
    def exists(self, key):
        """Check if key exists"""
        if self._use_redis:
            return self.client.exists(key)
        else:
            return key in self._cache
