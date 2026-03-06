from __future__ import annotations

from pathlib import Path
import os
import yaml
from dotenv import load_dotenv


ROOT = Path(__file__).resolve().parent.parent


class ConfigError(Exception):
    pass


def _read_yaml(path: Path) -> dict:
    if not path.exists():
        raise ConfigError(f"Missing config file: {path}")
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def load_all_configs(runtime_path: str = "config/runtime.yaml", models_path: str = "config/models.yaml") -> dict:
    load_dotenv()
    runtime = _read_yaml(ROOT / runtime_path)
    models = _read_yaml(ROOT / models_path)
    return {"runtime": runtime, "models": models}


def get_env_summary() -> dict:
    required = [
        "OPENAI_API_KEY",
        "ANTHROPIC_API_KEY",
        "DEEPSEEK_API_KEY",
        "QWEN_API_KEY",
        "REDIS_URL",
        "QDRANT_URL",
    ]
    return {key: bool(os.getenv(key)) for key in required}


def validate_environment() -> list[str]:
    problems = []
    envs = get_env_summary()

    if not any(envs.get(k) for k in ["OPENAI_API_KEY", "ANTHROPIC_API_KEY", "DEEPSEEK_API_KEY", "QWEN_API_KEY"]):
        problems.append("No model API key configured in environment.")

    if not envs.get("REDIS_URL"):
        problems.append("REDIS_URL is not configured.")
    if not envs.get("QDRANT_URL"):
        problems.append("QDRANT_URL is not configured.")

    return problems
