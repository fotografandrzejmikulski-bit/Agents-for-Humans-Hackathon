from __future__ import annotations

import re
from collections import Counter

from .models import Insight, ProjectItem

_STOPWORDS = {
    "about", "after", "again", "before", "could", "from", "have", "into", "needs", "only",
    "that", "their", "there", "these", "this", "what", "when", "with", "would", "your",
    "still", "next", "final", "asked", "client", "project", "progress", "remaining",
}


def _tokens(text: str) -> list[str]:
    return [token for token in re.findall(r"[a-zA-Z][a-zA-Z0-9_-]{3,}", text.lower()) if token not in _STOPWORDS]


def analyze_items(items: list[ProjectItem]) -> tuple[list[Insight], list[str]]:
    evidence = [f"{item.source}: {item.title}" for item in items]
    corpus = Counter(token for item in items for token in _tokens(item.content))
    top_terms = [term for term, _ in corpus.most_common(8)]
    pending = [item.title for item in items if any(word in item.content.lower() for word in ("pending", "needs", "remaining", "review"))]
    summary = (
        f"Processed {len(items)} source items. Key signals: {', '.join(top_terms) or 'no dominant terms'}; "
        f"potentially pending work: {', '.join(pending) or 'none detected'}."
    )
    confidence = min(0.95, 0.60 + 0.06 * len(items))
    insight = Insight(
        title="Decision-ready project signal",
        summary=summary,
        evidence=evidence,
        confidence=confidence,
        recommended_action="Review the evidence-backed brief; approve only consequential external actions.",
    )
    return [insight], evidence
