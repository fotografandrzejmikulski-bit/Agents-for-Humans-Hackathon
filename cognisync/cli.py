from __future__ import annotations

import argparse
import json
from pathlib import Path

from .audit import AuditLog
from .engine import CogniSyncEngine
from .models import ProjectItem
from .store import ProjectStore


def main() -> None:
    parser = argparse.ArgumentParser(description="CogniSync Professional background agent prototype")
    parser.add_argument("--request", default="Prepare today's project brief and identify decision points.")
    parser.add_argument("--data-dir", default="data")
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()

    store = ProjectStore(args.data_dir)
    audit = AuditLog(Path(args.data_dir) / "audit.jsonl")
    result = CogniSyncEngine(store, audit).run(args.request)
    payload = {
        "run_id": result.run_id,
        "status": result.status,
        "summary": result.summary,
        "insights": [
            {
                "title": insight.title,
                "summary": insight.summary,
                "evidence": insight.evidence,
                "confidence": insight.confidence,
                "recommended_action": insight.recommended_action,
            }
            for insight in result.insights
        ],
        "decision_request": (
            {
                "action": result.decision_request.action,
                "risk": result.decision_request.risk,
                "reason": result.decision_request.reason,
                "evidence": result.decision_request.evidence,
                "proposed_payload": result.decision_request.proposed_payload,
            }
            if result.decision_request
            else None
        ),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2 if args.pretty else None))
