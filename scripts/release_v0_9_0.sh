#!/usr/bin/env bash
set -e

git add .
git commit -m "chore: harden repository and prepare v0.9.0 release"
git tag v0.9.0
git push origin main
git push origin v0.9.0
