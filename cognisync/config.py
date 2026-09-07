from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Settings:
    region: str = "us-east-1"
    model_id: str = "amazon.nova-pro-v1:0"
    temperature: float = 0.2

    @classmethod
    def from_env(cls) -> Settings:
        return cls(
            region=os.getenv("AWS_DEFAULT_REGION", "us-east-1"),
            model_id=os.getenv("COGNISYNC_MODEL_ID", "amazon.nova-pro-v1:0"),
            temperature=float(os.getenv("COGNISYNC_TEMPERATURE", "0.2")),
        )
