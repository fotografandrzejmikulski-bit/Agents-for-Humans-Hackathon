from __future__ import annotations

import uuid
from dataclasses import asdict
from typing import Any

from .analysis import analyze_items
from .audit import AuditLog
from .decision import DecisionGate
from .models import Insight, ProjectItem, RunResult
from .policy import DEFAULT_POLICY, AutonomyPolicy
from .store import ProjectStore
from .verification import VerificationResult, verify_insights


class CogniSyncEngine:
    """Background-first orchestration core with explicit verification and consequence boundaries."""

    def __init__(
        self,
        store: ProjectStore,
        audit: AuditLog,
        policy: AutonomyPolicy = DEFAULT_POLICY,
    ) -> None:
        self.store = store
        self.audit = audit
        self.policy = policy
        self.gate = DecisionGate(policy, audit)

    def run(self, request: str, items: list[ProjectItem] | None = None) -> RunResult:
        run_id = str(uuid.uuid4())
        self.audit.record("run.started", run_id=run_id, request=request)
        sources = items if items is not None else self.store.load_items()

        if not sources:
            summary = "No project inputs were available. The agent remained idle rather than fabricating work."
            self.audit.record("run.completed", run_id=run_id, status="idle")
            return RunResult(run_id, "idle", summary, [], audit_events=[])

        insights, evidence = analyze_items(sources)
        verification: VerificationResult = verify_insights(insights, evidence)
        self.audit.record(
            "analysis.completed",
            run_id=run_id,
            source_count=len(sources),
            insight_count=len(insights),
            evidence_count=len(evidence),
            verification_status=verification.status,
            verification_errors=verification.errors,
        )

        if not verification.passed:
            summary = "The agent produced candidate insights but did not promote them because verification failed."
            self.audit.record("run.completed", run_id=run_id, status="verification_failed")
            return RunResult(run_id, "verification_failed", summary, [], audit_events=[])

        decision_request = None
        requested_action = self._requested_action(request)
        if requested_action:
            decision_request = self.gate.request(
                action=requested_action,
                reason="The requested operation may create an externally consequential side effect.",
                evidence=evidence,
                payload={
                    "run_id": run_id,
                    "request": request,
                    "source_ids": [item.id for item in sources],
                },
            )

        status = "decision_required" if decision_request else "completed"
        summary = self._summary(sources, insights, decision_request)
        self.audit.record("run.completed", run_id=run_id, status=status)
        return RunResult(run_id, status, summary, insights, decision_request)

    @staticmethod
    def _requested_action(request: str) -> str | None:
        text = request.lower()
        if any(token in text for token in ("send", "email", "message", "notify", "contact")):
            return "send_external_message"
        if any(token in text for token in ("publish", "release")):
            return "publish_document"
        if any(token in text for token in ("calendar", "schedule", "reschedule")):
            return "modify_calendar"
        if any(token in text for token in ("crm", "customer record", "client record")):
            return "change_crm_record"
        if any(token in text for token in ("pay", "payment", "transfer")):
            return "make_payment"
        if any(token in text for token in ("delete", "remove permanently", "destroy")):
            return "delete_data"
        return None

    @staticmethod
    def _summary(items: list[ProjectItem], insights: list[Insight], decision_request: Any) -> str:
        base = (
            f"CogniSync processed {len(items)} inputs in background mode and produced "
            f"{len(insights)} verified evidence-backed insight(s)."
        )
        if decision_request:
            return base + f" A human decision is required before {decision_request.action} can proceed."
        return base + " No consequential side effect was authorized or executed."


def result_as_dict(result: RunResult) -> dict[str, Any]:
    return asdict(result)
