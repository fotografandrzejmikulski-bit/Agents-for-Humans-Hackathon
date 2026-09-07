from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path
from typing import Iterable

from .models import ProjectItem


class ProjectStore:
    """Small local store used by the prototype; replaceable by S3/DB in production."""

    def __init__(self, root: str | Path = "data") -> None:
        self.root = Path(root)

    def load_items(self) -> list[ProjectItem]:
        self.root.mkdir(parents=True, exist_ok=True)
        records: list[ProjectItem] = []
        for path in sorted(self.root.glob("*.json")):
            payload = json.loads(path.read_text(encoding="utf-8"))
            if "id" not in payload:
                continue
            records.append(ProjectItem(**payload))
        return records

    def save_item(self, item: ProjectItem) -> Path:
        self.root.mkdir(parents=True, exist_ok=True)
        target = self.root / f"{item.id}.json"
        target.write_text(
            json.dumps(asdict(item), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        return target

    def seed(self, items: Iterable[ProjectItem]) -> None:
        for item in items:
            if not (self.root / f"{item.id}.json").exists():
                self.save_item(item)
