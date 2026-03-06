import subprocess
import sys


def test_main_help():
    result = subprocess.run(
        [sys.executable, "-m", "agentforge_core.main", "--help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
