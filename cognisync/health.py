from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone


@dataclass(frozen=True, slots=True)
class HealthStatus:
    service: str
    status: str
    version: str
    timestamp: str


def health_status(version: str) -> HealthStatus:
    return HealthStatus(
        service="cognisync",
        status="ok",
        version=version,
        timestamp=datetime.now(timezone.utc).isoformat(),
    )
