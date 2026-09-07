from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .audit import AuditLog
from .models import DecisionRequest
from .policy import AutonomyPolicy


@dataclass(frozen=True, slots=True)
class DecisionResolution:
    status: str
    message: str
    request: DecisionRequest


class DecisionGate:
    """Central consequence boundary: policy decides, a human resolves high-impact effects."""

    def __init__(self, policy: AutonomyPolicy, audit: AuditLog) -> None:
        self.policy = policy
        self.audit = audit

    def request(
        self,
        *,
        action: str,
        reason: str,
        evidence: list[str],
        payload: dict[str, Any],
    ) -> DecisionRequest | None:
        decision = self.policy.gate(action, reason, evidence, payload)
        if decision is None:
            return None
        self.audit.record(
            "decision.requested",
            action=action,
            risk=str(decision.risk),
            evidence_count=len(evidence),
        )
        return decision

    def resolve(
        self,
        decision: DecisionRequest,
        approved: bool,
        actor: str = "human",
    ) -> DecisionResolution:
        status = "approved" if approved else "rejected"
        event = "decision.approved" if approved else "decision.rejected"
        self.audit.record(event, action=decision.action, risk=str(decision.risk), actor=actor)
        message = (
            f"Human approval recorded for {decision.action}. External execution may proceed."
            if approved
            else f"Human rejection recorded for {decision.action}. No external effect is authorized."
        )
        return DecisionResolution(status, message, decision)
