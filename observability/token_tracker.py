"""
Token Tracker for monitoring token usage
"""


class TokenTracker:
    """Tracker for monitoring token usage across models"""
    
    def __init__(self):
        self.usage = {}
        self.cost = {}
        self.total_tokens = 0
        self.total_cost = 0.0
        
        # Token pricing (per 1M tokens)
        self.pricing = {
            "gpt4": 30.0,      # $30 per 1M tokens
            "gpt35": 0.5,      # $0.5 per 1M tokens
            "claude": 15.0,    # $15 per 1M tokens
            "codex": 10.0,     # $10 per 1M tokens
            "deepseek": 1.0,   # $1 per 1M tokens
            "default": 10.0,   # default pricing
        }
    
    def record(self, model, tokens, prompt_tokens=None, completion_tokens=None):
        """Record token usage for a model"""
        if model not in self.usage:
            self.usage[model] = {
                "total": 0,
                "prompt": 0,
                "completion": 0,
                "requests": 0
            }
        
        self.usage[model]["total"] += tokens
        self.usage[model]["requests"] += 1
        
        if prompt_tokens:
            self.usage[model]["prompt"] += prompt_tokens
        if completion_tokens:
            self.usage[model]["completion"] += completion_tokens
        
        # Calculate cost
        price = self.pricing.get(model, self.pricing["default"])
        cost = (tokens / 1_000_000) * price
        
        if model not in self.cost:
            self.cost[model] = 0.0
        self.cost[model] += cost
        
        self.total_tokens += tokens
        self.total_cost += cost
    
    def report(self):
        """Get usage report"""
        return {
            "usage": dict(self.usage),
            "cost": dict(self.cost),
            "total_tokens": self.total_tokens,
            "total_cost": self.total_cost
        }
    
    def get_model_usage(self, model):
        """Get usage for a specific model"""
        return self.usage.get(model, {})
    
    def get_model_cost(self, model):
        """Get cost for a specific model"""
        return self.cost.get(model, 0.0)
    
    def reset(self):
        """Reset all tracking"""
        self.usage.clear()
        self.cost.clear()
        self.total_tokens = 0
        self.total_cost = 0.0
    
    def set_pricing(self, model, price_per_million):
        """Set custom pricing for a model"""
        self.pricing[model] = price_per_million
