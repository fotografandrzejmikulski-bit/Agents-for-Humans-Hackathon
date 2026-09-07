from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256

from .models import ProjectItem


@dataclass(frozen=True, slots=True)
class EvidenceRecord:
    source_id: str
    source: str
    title: str
    content_hash: str

    @classmethod
    def from_item(cls, item: ProjectItem) -> EvidenceRecord:
        digest = sha256(item.content.encode("utf-8")).hexdigest()
        return cls(item.id, item.source, item.title, digest)


def build_evidence(items: list[ProjectItem]) -> list[EvidenceRecord]:
    return [EvidenceRecord.from_item(item) for item in items]
