# Contributing

## Development setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

## Before opening a PR

```bash
pytest -q
python -m agentforge_core.main --doctor
```

## Branch naming

- feat/*
- fix/*
- docs/*
- chore/*
