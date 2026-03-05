"""
AgentForge CLI Entry Point
"""

import argparse
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="AgentForge CLI - AI Agent Software Factory"
    )
    
    parser.add_argument("task", nargs="?", help="Task to execute")
    parser.add_argument("--init", action="store_true", help="Initialize a new AgentForge project")
    parser.add_argument("--config", default="config/runtime.yaml", help="Path to config file")
    parser.add_argument("--model", default="claude", help="Model to use")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    
    args = parser.parse_args()
    
    if args.init:
        from agentforge_core.bootstrap.init_project import init_project
        init_project()
    elif args.task:
        print(f"Executing task: {args.task}")
        print(f"Using model: {args.model}")
        # Import and run workflow
        try:
            from workflow.workflow_engine import WorkflowEngine
            from workflow.workflow_executor import WorkflowExecutor
            
            we = WorkflowEngine()
            executor = WorkflowExecutor()
            
            print(f"Task '{args.task}' would be executed here")
            print("(Full execution requires configured models)")
        except Exception as e:
            print(f"Error: {e}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
