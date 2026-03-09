# AgentForge Core

AgentForge Core is an AI agent software factory prototype focused on:
planner -> skill routing -> model routing -> model execution -> persistence -> workflow -> observability.

## Current repository status

Implemented:
- CLI entrypoint
- Planner
- Skill router
- Model router
- Provider abstraction layer with fallback
- Memory manager with backend selection
- Workflow store, retry and resume support
- Execution history and dashboard summary API
- Docker scaffolding for Redis/Qdrant
- Basic CI and tests

Not production-complete:
- Real provider API calls for all vendors
- Real Qdrant embedding/search pipeline
- Full web dashboard UI
- Production-grade distributed workers

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
cp .env.example .env
python -m agentforge_core.main --doctor
python -m agentforge_core.main --json "create fastapi project"
python -m agentforge_core.main --dashboard
```

## CLI examples

```bash
agentforge --doctor
agentforge --list-providers
agentforge --json "generate backend api"
agentforge --resume-workflow wf-xxxxxxxxxxxx
agentforge --retry-workflow wf-xxxxxxxxxxxx
agentforge --dashboard
```

## Testing

```bash
pytest -q
```

## Next priorities

- real qdrant embedding and retrieval
- persistent workflow replay
- web dashboard UI
- distributed worker execution
