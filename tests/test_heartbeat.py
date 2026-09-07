from cognisync.audit import AuditLog
from cognisync.engine import CogniSyncEngine
from cognisync.heartbeat import BackgroundHeartbeat
from cognisync.store import ProjectStore


def test_heartbeat_tick_runs_background_work(tmp_path) -> None:
    data = tmp_path / "data"
    audit = AuditLog(data / "audit.jsonl")
    engine = CogniSyncEngine(ProjectStore(data), audit)
    heartbeat = BackgroundHeartbeat(engine, audit, interval_seconds=1)
    result = heartbeat.tick()
    assert result.status == "idle"
    assert '"event": "heartbeat.tick"' in (data / "audit.jsonl").read_text(encoding="utf-8")
