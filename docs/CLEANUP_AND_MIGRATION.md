# Cleanup and Migration

## Why legacy modules still exist

Root-level modules still exist because some active package code may still import them.
Deleting them immediately could break the current runnable system.

## Safe migration sequence

1. Search imports inside `agentforge_core/`
2. Replace root-level imports with package-local imports where possible
3. Run tests
4. Remove the migrated root-level module
5. Run tests again
6. Commit after each module migration

## Root-level modules to phase out

- `memory/`
- `model_execution/`
- `observability/`
- `workflow/`
- `distributed/`
- `dashboard/`
- `router/`
- `control_plane/`

## Immediate cleanup done by this patch

- remove generated artifacts from git index
- remove caches from git index
- keep legacy modules in place until imports are migrated
