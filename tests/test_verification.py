from cognisync.models import Insight
from cognisync.verification import verify_insight, verify_insights


def test_valid_insight_passes_verification() -> None:
    insight = Insight(
        title="Launch blocker",
        summary="Accessibility review is still pending.",
        evidence=["brief-1"],
        confidence=0.92,
        recommended_action="Assign the review owner.",
    )
    result = verify_insight(insight)
    assert result.passed is True
    assert result.status == "passed"
    assert not result.failures


def test_missing_evidence_fails_verification() -> None:
    insight = Insight(
        title="Unverified claim",
        summary="Something may be wrong.",
        evidence=[],
        confidence=0.5,
        recommended_action="Investigate.",
    )
    result = verify_insight(insight)
    assert result.passed is False
    assert "missing evidence" in result.failures


def test_collection_requires_evidence_and_insights() -> None:
    result = verify_insights([], [])
    assert result.passed is False
    assert "no insights produced" in result.failures
    assert "no evidence produced" in result.failures
