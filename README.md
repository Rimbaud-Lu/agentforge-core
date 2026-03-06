# AgentForge Core

AgentForge Core is an AI Agent Software Factory prototype focused on:
planner -> skill routing -> model routing -> workflow execution.

## Current status

Implemented in repository:
- Core CLI
- Planner
- Skill router
- Model router
- Workflow executor
- Memory / observability / distributed module skeletons
- Docker / Redis / Qdrant scaffolding

Not fully complete yet:
- Real model provider integrations
- Robust workflow persistence
- Full dashboard runtime
- Production distributed execution

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
cp .env.example .env
python -m agentforge_core.cli.cli --doctor
python -m agentforge_core.cli.cli "create fastapi project"
```

## Docker

```bash
docker compose up --build
```

## CLI

```bash
agentforge --doctor
agentforge "create fastapi project"
agentforge --json "generate backend api"
```

## Testing

```bash
pytest -q
```

## Roadmap alignment

- Phase 1: core flow present
- Phase 2: skill structure present
- Phase 3: model routing present
- Phase 4+: partial skeletons present, not production complete

## Repository cleanup goals

- remove generated artifacts from git
- improve tests
- unify package boundaries
- add CI/CD
