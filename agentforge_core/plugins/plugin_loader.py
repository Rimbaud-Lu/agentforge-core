"""
Plugin Loader for AgentForge
"""

import importlib
import os
import sys


class PluginLoader:
    """Loader for AgentForge plugins"""
    
    def __init__(self, plugin_path="plugins"):
        self.plugin_path = plugin_path
        self.loaded_plugins = {}
    
    def load_plugins(self):
        """Load all plugins from the plugins directory"""
        if not os.path.exists(self.plugin_path):
            print(f"Plugin directory '{self.plugin_path}' does not exist")
            return {}
        
        for file in os.listdir(self.plugin_path):
            if file.endswith(".py") and not file.startswith("_"):
                module_name = file[:-3]
                self.load_plugin(module_name)
        
        return self.loaded_plugins
    
    def load_plugin(self, module_name):
        """Load a single plugin"""
        try:
            full_module_name = f"{self.plugin_path}.{module_name}"
            module = importlib.import_module(full_module_name)
            self.loaded_plugins[module_name] = module
            print(f"Loaded plugin: {module_name}")
            return module
        except Exception as e:
            print(f"Failed to load plugin {module_name}: {e}")
            return None
    
    def get_plugin(self, name):
        """Get a loaded plugin by name"""
        return self.loaded_plugins.get(name)
    
    def list_plugins(self):
        """List all loaded plugins"""
        return list(self.loaded_plugins.keys())
    
    def reload_plugin(self, module_name):
        """Reload a plugin"""
        if module_name in self.loaded_plugins:
            del self.loaded_plugins[module_name]
        
        full_module_name = f"{self.plugin_path}.{module_name}"
        if full_module_name in sys.modules:
            del sys.modules[full_module_name]
        
        return self.load_plugin(module_name)
