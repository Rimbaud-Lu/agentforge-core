from pathlib import Path


def init_project(project_name="my-agent-project"):
    for folder in ["agents", "skills", "config", "tests"]:
        Path(folder).mkdir(parents=True, exist_ok=True)

    Path("agentforge.yaml").write_text(
        f"""project: {project_name}

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
""",
        encoding="utf-8",
    )

    Path("agents/sample_agent.py").write_text(
        "class SampleAgent:\n    name = 'sample_agent'\n",
        encoding="utf-8",
    )
    Path("skills/sample_skill.py").write_text(
        "def run(task: str):\n    return f\"handled: {task}\"\n",
        encoding="utf-8",
    )
    print(f"Initialized AgentForge project: {project_name}")
