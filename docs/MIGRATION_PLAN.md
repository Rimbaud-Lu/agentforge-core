# Migration Plan

## Goal
Consolidate active implementation under `agentforge_core/` and phase out duplicated
root-level modules.

## Rules
1. New code goes into `agentforge_core/`
2. Tests should import package modules first
3. Root-level duplicates should be removed only after imports are updated

## Candidate legacy roots to phase out
- `memory/`
- `model_execution/`
- `observability/`
- `workflow/`
- `distributed/`
- `dashboard/`
