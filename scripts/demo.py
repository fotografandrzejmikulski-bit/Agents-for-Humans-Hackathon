from __future__ import annotations

import json
from pathlib import Path

from cognisync.audit import AuditLog
from cognisync.engine import CogniSyncEngine
from cognisync.store import ProjectStore


def main() -> None:
    data_dir = Path("data")
    audit_path = data_dir / "demo-audit.jsonl"
    if audit_path.exists():
        audit_path.unlink()

    engine = CogniSyncEngine(ProjectStore(data_dir), AuditLog(audit_path))

    print("\nCOGNISYNC PROFESSIONAL — LOCAL DEMO\n")
    result = engine.run("prepare today's project brief and identify decision points")
    print("[1/3] BACKGROUND INTELLIGENCE")
    print(json.dumps({"status": result.status, "summary": result.summary}, indent=2))
    for insight in result.insights:
        print(json.dumps({"title": insight.title, "summary": insight.summary, "evidence": insight.evidence, "confidence": insight.confidence}, indent=2))

    gated = engine.run("prepare and send the client follow-up")
    print("\n[2/3] CONSEQUENCE BOUNDARY")
    print(json.dumps({"status": gated.status, "decision": str(gated.decision_request)}, indent=2))

    print("\n[3/3] HUMAN RESOLUTION — SIMULATED")
    if gated.decision_request:
        resolution = engine.gate.resolve(gated.decision_request, approved=True)
        print(json.dumps(resolution, indent=2))
    print(f"\nAudit trail: {audit_path}")


if __name__ == "__main__":
    main()
