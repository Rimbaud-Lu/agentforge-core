import os


class RepoIndexer:
    """Repository Indexer for indexing project files into memory"""
    
    def __init__(self, project_memory):
        self.project_memory = project_memory
    
    def index_repo(self, repo_path):
        """Index all files in a repository"""
        indexed_files = []
        
        for root, dirs, files in os.walk(repo_path):
            # Skip hidden directories and common ignore patterns
            dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
            
            for file in files:
                # Skip hidden files and binary files
                if file.startswith('.'):
                    continue
                
                path = os.path.join(root, file)
                
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read()
                        self.project_memory.add_file(path, content)
                        indexed_files.append(path)
                except:
                    pass
        
        return indexed_files
    
    def get_file_content(self, path):
        """Get content of indexed file"""
        return self.project_memory.get_file(path)
