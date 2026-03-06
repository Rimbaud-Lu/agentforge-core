from __future__ import annotations

import argparse
import json
import sys

from agentforge_core.app import AgentForgeApp
from agentforge_core.bootstrap.init_project import init_project
from agentforge_core.config_loader import load_all_configs, validate_environment, get_env_summary
from agentforge_core.logging_utils import setup_logging


def main():
    logger = setup_logging()

    parser = argparse.ArgumentParser(description="AgentForge CLI")
    parser.add_argument("task", nargs="?", help="Task to execute")
    parser.add_argument("--init", action="store_true", help="Initialize a new AgentForge project")
    parser.add_argument("--doctor", action="store_true", help="Validate config and environment")
    parser.add_argument("--model", default=None, help="Override selected model")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    parser.add_argument("--list-providers", action="store_true", help="Show configured provider env readiness")
    args = parser.parse_args()

    if args.init:
        init_project()
        return

    if args.list_providers:
        print(json.dumps(get_env_summary(), ensure_ascii=False, indent=2))
        return

    if args.doctor:
        try:
            configs = load_all_configs()
            problems = validate_environment()
            payload = {
                "ok": len(problems) == 0,
                "problems": problems,
                "config_keys": list(configs.keys()),
                "env_summary": get_env_summary(),
            }
        except Exception as e:
            payload = {"ok": False, "problems": [str(e)]}

        print(json.dumps(payload, ensure_ascii=False, indent=2))
        sys.exit(0 if payload["ok"] else 1)

    if not args.task:
        parser.print_help()
        return

    logger.info("Executing task: %s", args.task)
    app = AgentForgeApp()
    result = app.execute_task(args.task, model_override=args.model)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Task: {result['task']}")
        print(f"Skill: {result['skill']}")
        print(f"Model: {result['model']}")
        print(f"Provider: {result['provider']}")
        print(f"Status: {result['status']}")
        print(f"Output: {result['output'].get('message', '')}")
