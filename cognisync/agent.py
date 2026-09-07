from __future__ import annotations

from typing import Any

from .config import Settings

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
    """Build the real Strands/Bedrock agent when optional dependencies are installed."""
    if Agent is None or BedrockModel is None:
        raise RuntimeError("Install the project with the 'aws' extra or install strands-agents.")

    settings = Settings.from_env()
    model = BedrockModel(
        model_id=settings.model_id,
        temperature=settings.temperature,
        streaming=True,
    )
    return Agent(model=model, system_prompt=SYSTEM_PROMPT)
