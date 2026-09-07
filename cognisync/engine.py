from __future__ import annotations

import os
import uuid
from collections import Counter

from .audit import AuditLog
from .models import Insight, ProjectItem, RunResult
from .policy import DEFAULT_POLICY, AutonomyPolicy
from .store import ProjectStore


class CogniSyncEngine:
    """Deterministic prototype core; the LLM layer can supply richer extraction later."""

    def __init__(self, store: ProjectStore, audit: AuditLog, policy: AutonomyPolicy = DEFAULT_POLICY) -> None:
        self.store = store
        self.audit = audit
        self.policy = policy

    def run(self, request: str, items: list[ProjectItem] | None = None) -> RunResult:
        run_id = str(uuid.uuid4())
        self.audit.record("run.started", run_id=run_id, request=request)
        items = items if items is not None else self.store.load_items()

        if not items:
            summary = "No project inputs were available. The agent remained idle rather than fabricating work."
            self.audit.record("run.completed", run_id=run_id, status="idle")
            return RunResult(run_id, "idle", summary, [], audit_events=[])

        keyword_counts = Counter()
        for item in items:
            for token in item.content.lower().split():
                cleaned = "".join(ch for ch in token if ch.isalnum())
                if len(cleaned) >= 5:
                    keyword_counts[cleaned] += 1

        top_terms = [word for word, _ in keyword_counts.most_common(8)]
        evidence = [f"{item.source}: {item.title}" for item in items[:6]]
        insight = Insight(
            title="Project activity signal",
            summary=f"Processed {len(items)} project inputs. Dominant terms: {', '.join(top_terms) or 'none'}.",
            evidence=evidence,
            confidence=min(0.98, 0.55 + 0.05 * len(items)),
            recommended_action="Review the generated brief and approve only external actions that require a business decision.",
        )

        decision_request = None
        if any(os.getenv(flag) == "1" for flag in ("COGNISYNC_SEND", "COGNISYNC_PUBLISH")):
            action = "send_external_message" if os.getenv("COGNISYNC_SEND") == "1" else "publish_document"
            decision_request = self.policy.gate(
                action,
                "An external side effect was requested by configuration.",
                evidence,
                {"run_id": run_id, "request": request},
            )
            self.audit.record(
                "decision.gated",
                run_id=run_id,
                action=action,
                risk=decision_request.risk if decision_request else "low",
            )

        self.audit.record("run.completed", run_id=run_id, status="decision_required" if decision_request else "completed")
        return RunResult(
            run_id=run_id,
            status="decision_required" if decision_request else "completed",
            summary=f"CogniSync processed {len(items)} inputs in background mode.",
            insights=[insight],
            decision_request=decision_request,
        )
