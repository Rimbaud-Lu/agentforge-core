# AgentForge Core

AgentForge Core is an AI agent software factory prototype focused on:
planner -> skill routing -> model routing -> workflow execution.

## Current repository status

Implemented:
- CLI entrypoint
- Planner
- Skill router
- Model router
- Workflow executor
- Memory / observability / distributed skeletons
- Docker scaffolding
- Basic CI and tests

Not production-complete:
- Real provider-backed model execution
- Production workflow persistence
- Full dashboard runtime
- Production-grade distributed workers

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
cp .env.example .env
python -m agentforge_core.main --doctor
python -m agentforge_core.main "create fastapi project"
```

## CLI examples

```bash
agentforge --doctor
agentforge "generate backend api"
agentforge --json "create agent workflow"
```

## Docker

```bash
docker compose up --build
```

## Testing

```bash
pytest -q
```

## Next priorities

- unify package boundaries
- connect real model providers
- improve workflow persistence
- expand observability metrics
