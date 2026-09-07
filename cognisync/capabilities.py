from __future__ import annotations

from dataclasses import dataclass
from typing import Final

from .models import RiskLevel


@dataclass(frozen=True, slots=True)
class Capability:
    """Typed description of one tool/action boundary."""

    name: str
    description: str
    risk: RiskLevel
    requires_human: bool
    external_side_effect: bool


CAPABILITIES: Final[dict[str, Capability]] = {
    "read_project_data": Capability(
        "read_project_data", "Read project signals", RiskLevel.LOW, False, False
    ),
    "summarize": Capability(
        "summarize", "Summarize project signals", RiskLevel.LOW, False, False
    ),
    "classify": Capability(
        "classify", "Classify project signals", RiskLevel.LOW, False, False
    ),
    "draft_followup": Capability(
        "draft_followup", "Draft a follow-up message", RiskLevel.LOW, False, False
    ),
    "draft_report": Capability(
        "draft_report", "Draft a project report", RiskLevel.LOW, False, False
    ),
    "search_knowledge": Capability(
        "search_knowledge", "Search the connected knowledge surface", RiskLevel.LOW, False, False
    ),
    "send_external_message": Capability(
        "send_external_message", "Send an external message", RiskLevel.HIGH, True, True
    ),
    "publish_document": Capability(
        "publish_document", "Publish an external document", RiskLevel.HIGH, True, True
    ),
    "modify_calendar": Capability(
        "modify_calendar", "Create, change or cancel a calendar event", RiskLevel.HIGH, True, True
    ),
    "change_crm_record": Capability(
        "change_crm_record", "Modify a customer/business record", RiskLevel.HIGH, True, True
    ),
    "make_payment": Capability(
        "make_payment", "Initiate a payment", RiskLevel.HIGH, True, True
    ),
    "delete_data": Capability(
        "delete_data", "Delete information", RiskLevel.HIGH, True, True
    ),
}


def lookup_capability(action: str) -> Capability | None:
    return CAPABILITIES.get(action.strip().lower())


def classify_capability(action: str) -> RiskLevel:
    capability = lookup_capability(action)
    return capability.risk if capability else RiskLevel.CRITICAL
