from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(".")
PACKAGE = ROOT / "agentforge_core"

patterns = [
    r"from\s+control_plane\.",
    r"from\s+router\.",
    r"from\s+workflow\.",
    r"from\s+observability\.",
    r"from\s+memory\.",
    r"from\s+model_execution\.",
    r"from\s+distributed\.",
    r"from\s+dashboard\.",
    r"import\s+control_plane\.",
    r"import\s+router\.",
    r"import\s+workflow\.",
    r"import\s+observability\.",
    r"import\s+memory\.",
    r"import\s+model_execution\.",
    r"import\s+distributed\.",
    r"import\s+dashboard\.",
]

compiled = [re.compile(p) for p in patterns]

for pyfile in PACKAGE.rglob("*.py"):
    text = pyfile.read_text(encoding="utf-8")
    for line_no, line in enumerate(text.splitlines(), start=1):
        if any(p.search(line) for p in compiled):
            print(f"{pyfile}:{line_no}: {line}")
