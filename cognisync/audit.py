from __future__ import annotations

import hashlib
import json
import uuid
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


class AuditLog:
    """Append-only, hash-chained JSONL audit trail."""

    def __init__(self, path: str | Path = "data/audit.jsonl") -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._previous_hash = self._load_previous_hash()

    def record(self, event: str, **fields: Any) -> dict[str, Any]:
        payload = {
            "event_id": str(uuid.uuid4()),
            "timestamp": datetime.now(UTC).isoformat(),
            "event": event,
            "prev_hash": self._previous_hash,
            **fields,
        }
        canonical = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        event_hash = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
        payload["event_hash"] = event_hash
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(payload, ensure_ascii=False) + "\n")
        self._previous_hash = event_hash
        return payload

    def verify_integrity(self) -> tuple[bool, int, str | None]:
        previous = ""
        checked = 0
        if not self.path.exists():
            return True, 0, None
        for line_no, line in enumerate(self.path.read_text(encoding="utf-8").splitlines(), start=1):
            record = json.loads(line)
            expected_previous = record.get("prev_hash", "")
            if expected_previous != previous:
                return False, checked, f"line {line_no}: prev_hash mismatch"
            supplied_hash = record.pop("event_hash", None)
            canonical = json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
            expected_hash = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
            if supplied_hash != expected_hash:
                return False, checked, f"line {line_no}: event_hash mismatch"
            previous = supplied_hash
            checked += 1
        return True, checked, None

    def _load_previous_hash(self) -> str:
        if not self.path.exists():
            return ""
        lines = self.path.read_text(encoding="utf-8").splitlines()
        if not lines:
            return ""
        return json.loads(lines[-1]).get("event_hash", "")
