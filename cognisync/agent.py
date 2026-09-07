from __future__ import annotations

import os
from typing import Any

try:
    from strands import Agent
    from strands.models import BedrockModel
except ImportError:  # pragma: no cover - optional at import time for local core tests
    Agent = None  # type: ignore[assignment,misc]
    BedrockModel = None  # type: ignore[assignment,misc]


SYSTEM_PROMPT = """You are CogniSync Professional, a background work agent.
Your job is to reduce repetitive professional work without creating notification noise.
Read and analyze supplied project inputs, identify decisions, dependencies and follow-ups,
and produce a decision-ready brief. Never claim an external action was completed unless a
real tool confirms it. Treat external side effects as gated operations requiring approval.
Prefer concise evidence-backed outputs and preserve provenance for important claims.
"""


def build_strands_agent() -> Any:
    """Build the real Strands agent when the runtime dependencies are installed."""
    if Agent is None or BedrockModel is None:
        raise RuntimeError("Install the project with the 'aws' extra or install strands-agents.")

    model_id = os.getenv("COGNISYNC_MODEL_ID", "amazon.nova-pro-v1:0")
    model = BedrockModel(
        model_id=model_id,
        temperature=float(os.getenv("COGNISYNC_TEMPERATURE", "0.2")),
        streaming=True,
    )
    return Agent(model=model, system_prompt=SYSTEM_PROMPT)
