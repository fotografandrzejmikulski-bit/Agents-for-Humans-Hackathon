from __future__ import annotations

import time
from collections.abc import Callable

from .audit import AuditLog
from .engine import CogniSyncEngine


class BackgroundHeartbeat:
    """Small local scheduler proving the background-first operating model."""

    def __init__(self, engine: CogniSyncEngine, audit: AuditLog, interval_seconds: float = 30.0) -> None:
        if interval_seconds <= 0:
            raise ValueError("interval_seconds must be positive")
        self.engine = engine
        self.audit = audit
        self.interval_seconds = interval_seconds

    def tick(self, request: str = "Prepare the latest project brief and identify decision points."):
        self.audit.record("heartbeat.tick", request=request)
        return self.engine.run(request)

    def run_forever(self, request: str, *, sleep: Callable[[float], None] = time.sleep) -> None:
        while True:
            self.tick(request)
            sleep(self.interval_seconds)
