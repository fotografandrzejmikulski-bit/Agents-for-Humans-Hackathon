from __future__ import annotations

from dataclasses import dataclass

from .models import RunResult


@dataclass(frozen=True, slots=True)
class AttentionMetrics:
    """Simple outcome metrics for the product's human-attention objective."""

    human_interventions: int
    evidence_coverage: float
    consequence_gates: int
    autonomous_insights: int


def measure(result: RunResult) -> AttentionMetrics:
    total = len(result.insights)
    evidenced = sum(1 for insight in result.insights if insight.evidence)
    return AttentionMetrics(
        human_interventions=1 if result.decision_request else 0,
        evidence_coverage=(evidenced / total) if total else 1.0,
        consequence_gates=1 if result.decision_request else 0,
        autonomous_insights=total,
    )
