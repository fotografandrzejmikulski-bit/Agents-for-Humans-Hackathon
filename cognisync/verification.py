from __future__ import annotations

from dataclasses import dataclass

from .models import Insight


@dataclass(frozen=True, slots=True)
class VerificationResult:
    passed: bool
    checks: tuple[str, ...]
    failures: tuple[str, ...]


def verify_insight(insight: Insight) -> VerificationResult:
    failures: list[str] = []
    if not insight.title.strip():
        failures.append("missing title")
    if not insight.summary.strip():
        failures.append("missing summary")
    if not insight.evidence:
        failures.append("missing evidence")
    if not 0.0 <= insight.confidence <= 1.0:
        failures.append("confidence outside [0,1]")
    if not insight.recommended_action.strip():
        failures.append("missing recommended action")
    return VerificationResult(
        passed=not failures,
        checks=("schema", "evidence", "confidence", "actionability"),
        failures=tuple(failures),
    )
