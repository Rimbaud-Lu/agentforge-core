"""
AgentForge Project Bootstrap
"""

import os


def init_project(project_name="my-agent-project"):
    """Initialize a new AgentForge project"""
    
    # Create project directories
    os.makedirs("agents", exist_ok=True)
    os.makedirs("skills", exist_ok=True)
    os.makedirs("config", exist_ok=True)
    os.makedirs("tests", exist_ok=True)
    
    # Create agentforge.yaml config
    config = f"""project: {project_name}

agents:
  - backend_agent
  - frontend_agent
  - qa_agent

skills:
  - generate_api
  - generate_tests
  - deploy_service

models:
  default: claude
  
runtime:
  max_agents: 10
  parallel_execution: true
"""
    
    with open("agentforge.yaml", "w") as f:
        f.write(config)
    
    print(f"AgentForge project '{project_name}' initialized successfully!")
    print("\nProject structure created:")
    print("  - agents/")
    print("  - skills/")
    print("  - config/")
    print("  - tests/")
    print("  - agentforge.yaml")
    print("\nNext steps:")
    print("  1. Copy .env.example to .env and add your API keys")
    print("  2. Run: python -m agentforge_core.cli.cli 'your task'")


if __name__ == "__main__":
    init_project()
