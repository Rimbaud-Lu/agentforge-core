#!/usr/bin/env bash
set -e

python scripts/audit_root_imports.py || true
git status
git add .
git commit -m "chore: clean tracked artifacts and prepare structure migration"
