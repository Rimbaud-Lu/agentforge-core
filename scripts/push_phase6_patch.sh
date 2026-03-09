#!/usr/bin/env bash
set -e

git add .
git commit -m "feat: add persistence backends and workflow retry support"
git push origin main
