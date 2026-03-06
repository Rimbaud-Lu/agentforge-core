import subprocess
import sys


def test_cli_help():
    result = subprocess.run(
        [sys.executable, "-m", "agentforge_core.cli.cli", "--help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "AgentForge CLI" in result.stdout
