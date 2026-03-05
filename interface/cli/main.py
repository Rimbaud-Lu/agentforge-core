from control_plane.planner.planner import plan_task
from agents.backend.agent import run_agent

def main():
    task = input("Enter task: ")
    plan = plan_task(task)
    run_agent(plan)

if __name__ == "__main__":
    main()
