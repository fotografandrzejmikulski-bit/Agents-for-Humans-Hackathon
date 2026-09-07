from __future__ import annotations

from dataclasses import dataclass
from typing import Final

from .models import DecisionRequest, RiskLevel


@dataclass(frozen=True, slots=True)
class AutonomyPolicy:
    """Determines whether an operation can execute without human approval."""

    safe_actions: frozenset[str]
    approval_actions: frozenset[str]

    def classify(self, action: str) -> RiskLevel:
        normalized = action.strip().lower()
        if normalized in self.safe_actions:
            return RiskLevel.LOW
        if normalized in self.approval_actions:
            return RiskLevel.HIGH
        return RiskLevel.CRITICAL

    def requires_approval(self, action: str) -> bool:
        return self.classify(action) in {RiskLevel.HIGH, RiskLevel.CRITICAL}

    def gate(self, action: str, reason: str, evidence: list[str], payload: dict) -> DecisionRequest | None:
        if not self.requires_approval(action):
            return None
        return DecisionRequest(
            action=action,
            reason=reason,
            risk=self.classify(action),
            evidence=evidence,
            proposed_payload=payload,
        )


SAFE_ACTIONS: Final = frozenset(
    {
        "read_project_data",
        "summarize",
        "classify",
        "draft_followup",
        "draft_report",
        "search_knowledge",
    }
)

APPROVAL_ACTIONS: Final = frozenset(
    {
        "send_external_message",
        "publish_document",
        "modify_calendar",
        "change_crm_record",
        "make_payment",
        "delete_data",
    }
)

DEFAULT_POLICY = AutonomyPolicy(SAFE_ACTIONS, APPROVAL_ACTIONS)
