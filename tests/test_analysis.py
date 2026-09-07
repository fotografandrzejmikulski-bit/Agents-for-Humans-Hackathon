from cognisync.analysis import analyze_items
from cognisync.models import ProjectItem


def test_analysis_extracts_pending_signals_and_evidence() -> None:
    items = [
        ProjectItem("1", "email", "Launch", "Homepage review is pending before launch."),
        ProjectItem("2", "notes", "Accessibility", "Accessibility checks are still pending."),
    ]
    insights, evidence = analyze_items(items)
    assert insights
    assert "pending" in insights[0].summary.lower()
    assert evidence == ["email: Launch", "notes: Accessibility"]
    assert 0.0 <= insights[0].confidence <= 1.0
