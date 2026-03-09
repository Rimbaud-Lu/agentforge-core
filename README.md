# AgentForge Core

AgentForge Core is an AI agent software factory prototype that now includes:
planner -> skill routing -> model routing -> model execution -> memory ->
workflow persistence -> observability -> distributed execution.

## Current status

This repository is no longer a simple Phase 1 project.

Implemented in the current repository:
- CLI entrypoint and app orchestrator
- Planner, skill router, model router
- Provider abstraction layer and model executor
- Memory manager and persistence backend selection
- Workflow store, resume and retry support
- Execution history and dashboard summary API
- Lightweight distributed queue, dispatcher, worker runtime
- Multi-agent demo execution path
- Docker scaffolding and test suite

Still prototype / not production-complete:
- Real provider API calls for all supported vendors
- Real Kafka / Redis queue workers
- Real vector embedding + retrieval pipeline
- Full web dashboard UI
- Production-grade orchestration and deployment

## Repository layout

Primary package code lives in `agentforge_core/`.

Legacy root-level modules may still exist for backward compatibility during migration,
but new development should target the package modules under `agentforge_core/`.

Key package areas:
- `agentforge_core/cli`
- `agentforge_core/memory`
- `agentforge_core/model_execution`
- `agentforge_core/workflow`
- `agentforge_core/observability`
- `agentforge_core/dashboard`
- `agentforge_core/distributed`

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
cp .env.example .env
python -m agentforge_core.main --doctor
python -m agentforge_core.main --json "create fastapi project"
python -m agentforge_core.main --dashboard
python -m agentforge_core.main --multi-agent-demo
```

## CLI examples

```bash
agentforge --doctor
agentforge --list-providers
agentforge --json "generate backend api"
agentforge --resume-workflow wf-xxxxxxxxxxxx
agentforge --retry-workflow wf-xxxxxxxxxxxx
agentforge --dispatch-task "generate backend api"
agentforge --process-next
agentforge --queue-size
agentforge --multi-agent-demo
```

## Testing

```bash
pytest -q
```

## Migration note

This repository is in a package-boundary cleanup phase.
The long-term target is to keep implementation under `agentforge_core/`
and remove duplicated legacy root-level modules.

## Release target

Recommended next release tag:
- `v0.9.0`
