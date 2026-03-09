# Repository Status

## What is finished enough for demo use
- CLI execution path
- Provider abstraction
- Memory and workflow persistence skeleton
- Observability summary
- Distributed in-memory queue demo

## What is still prototype-grade
- Provider integrations
- Vector retrieval
- Real distributed backends
- Dashboard UI
- Production deployment

## Boundary decision

New development should happen in `agentforge_core/`.
Root-level duplicated modules are transitional and should be treated as legacy.
