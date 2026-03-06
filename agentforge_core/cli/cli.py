import argparse
import json
import sys

from agentforge_core.app import AgentForgeApp
from agentforge_core.bootstrap.init_project import init_project
from agentforge_core.config_loader import load_all_configs, validate_environment


def main():
    parser = argparse.ArgumentParser(description="AgentForge CLI")
    parser.add_argument("task", nargs="?", help="Task to execute")
    parser.add_argument("--init", action="store_true", help="Initialize a new AgentForge project")
    parser.add_argument("--doctor", action="store_true", help="Validate config and environment")
    parser.add_argument("--model", default=None, help="Override selected model")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    if args.init:
        init_project()
        return

    if args.doctor:
        try:
            load_all_configs()
            problems = validate_environment()
            payload = {"ok": len(problems) == 0, "problems": problems}
        except Exception as e:
            payload = {"ok": False, "problems": [str(e)]}

        print(json.dumps(payload, ensure_ascii=False, indent=2))
        sys.exit(0 if payload["ok"] else 1)

    if not args.task:
        parser.print_help()
        return

    app = AgentForgeApp()
    result = app.execute_task(args.task, model_override=args.model)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Task: {result['task']}")
        print(f"Skill: {result['skill']}")
        print(f"Model: {result['model']}")
        print(f"Status: {result['result']['status']}")
        print(f"Message: {result['result'].get('message', '')}")


if __name__ == "__main__":
    main()
