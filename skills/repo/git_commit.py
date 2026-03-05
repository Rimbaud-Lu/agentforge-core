import subprocess

def commit_changes(message="AI commit"):
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", message])
    
    return "changes committed"
