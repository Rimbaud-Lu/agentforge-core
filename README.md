# AgentForge Core

AgentForge Core is an AI agent software factory prototype focused on:
planner -> skill routing -> model routing -> model execution -> memory -> workflow execution.

## Current repository status

Implemented:
- CLI entrypoint
- Planner
- Skill router
- Model router
- Provider abstraction layer
- Memory manager
- Workflow store and task graph
- Resume workflow support
- Docker scaffolding
- Basic CI and tests

Not production-complete:
- Real provider API calls for all vendors
- Redis/Qdrant-backed memory persistence
- Full dashboard runtime
- Production-grade distributed workers

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
cp .env.example .env
python -m agentforge_core.main --doctor
python -m agentforge_core.main --json "create fastapi project"
```

## CLI examples

```bash
agentforge --doctor
agentforge --list-providers
agentforge --json "generate backend api"
agentforge --resume-workflow wf-xxxxxxxxxxxx
```

## Testing

```bash
pytest -q
```

## Next priorities

- redis/qdrant-backed memory
- persistent workflow retry/resume
- metrics and dashboard integration
- distributed worker execution
