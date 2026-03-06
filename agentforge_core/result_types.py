from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any


@dataclass
class TaskResult:
    status: str
    task: str
    skill: str
    model: str
    output: Any
    error: str | None = None

    def to_dict(self) -> dict:
        return asdict(self)
