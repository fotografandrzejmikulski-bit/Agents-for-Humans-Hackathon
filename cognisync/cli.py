from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any

from .audit import AuditLog
from .decision import DecisionGate
from .engine import CogniSyncEngine
from .policy import DEFAULT_POLICY
from .store import ProjectStore


def _serialize(result: Any) -> dict[str, Any]:
    payload: dict[str, Any] = {
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
        "decision_request": None,
    }
    if result.decision_request:
        payload["decision_request"] = {
            "action": result.decision_request.action,
            "risk": str(result.decision_request.risk),
            "reason": result.decision_request.reason,
            "evidence": result.decision_request.evidence,
            "proposed_payload": result.decision_request.proposed_payload,
        }
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description="CogniSync background professional agent")
    parser.add_argument("--request", default="Prepare today's project brief and identify decision points.")
    parser.add_argument("--data-dir", default="data")
    parser.add_argument("--pretty", action="store_true")
    parser.add_argument("--demo-gate", action="store_true", help="Request an external action to demonstrate HITL gating")
    parser.add_argument("--approve", action="store_true", help="Resolve a demo decision as approved; never executes a real side effect")
    args = parser.parse_args()

    request = args.request
    if args.demo_gate:
        request = "Prepare the brief and send the external follow-up."

    store = ProjectStore(args.data_dir)
    audit = AuditLog(Path(args.data_dir) / "audit.jsonl")
    result = CogniSyncEngine(store, audit).run(request)

    if result.decision_request and args.approve:
        resolution = DecisionGate(DEFAULT_POLICY, audit).resolve(result.decision_request, approved=True)
        result.summary += f" {resolution.message}"

    print(json.dumps(_serialize(result), ensure_ascii=False, indent=2 if args.pretty else None))
    if result.status == "decision_required" and not args.approve:
        print("\nHuman decision required: rerun with --approve only for the local demo resolution path.", file=os.sys.stderr)
