import json
import subprocess
import sys
import re


def test_cli_json_flow():
    result = subprocess.run(
        [sys.executable, "-m", "agentforge_core.main", "--json", "create fastapi project"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    # Extract JSON from output (skip logging lines)
    json_match = re.search(r'\{[\s\S]*\}', result.stdout)
    assert json_match is not None
    payload = json.loads(json_match.group())
    assert payload["status"] == "success"
    assert "provider" in payload
    assert "output" in payload
