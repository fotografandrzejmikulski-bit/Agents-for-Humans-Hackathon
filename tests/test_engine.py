import json

from cognisync.audit import AuditLog
from cognisync.engine import CogniSyncEngine
from cognisync.models import ProjectItem
from cognisync.store import ProjectStore


def test_engine_creates_evidence_backed_result(tmp_path) -> None:
    store = ProjectStore(tmp_path / "data")
    audit = AuditLog(tmp_path / "data" / "audit.jsonl")
    items = [
        ProjectItem("1", "email", "Launch", "Homepage review is pending before launch."),
        ProjectItem("2", "notes", "Accessibility", "Accessibility checks are still pending."),
    ]
    result = CogniSyncEngine(store, audit).run("prepare brief", items)
    assert result.status == "completed"
    assert result.insights
    assert result.insights[0].evidence == ["email: Launch", "notes: Accessibility"]
    assert (tmp_path / "data" / "audit.jsonl").exists()


def test_engine_emits_gate_for_external_action(tmp_path, monkeypatch) -> None:
    data = tmp_path / "data"
    store = ProjectStore(data)
    audit = AuditLog(data / "audit.jsonl")
    monkeypatch.setenv("COGNISYNC_SEND", "1")
    result = CogniSyncEngine(store, audit).run(
        "send follow-up",
        [ProjectItem("1", "email", "Client", "Approval needed.")],
    )
    assert result.status == "decision_required"
    assert result.decision_request is not None
    events = [json.loads(line) for line in (data / "audit.jsonl").read_text().splitlines()]
    assert any(event["event"] == "decision.gated" for event in events)
