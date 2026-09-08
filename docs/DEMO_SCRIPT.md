# 5-Minute Demo Script

## 0:00–0:35 — The problem

**Narration:**

"Professionals do not need another chatbot to operate. They need repetitive coordination work to disappear. CogniSync runs in the background, reads project signals, verifies what it can support, and surfaces a compact decision packet only when human authority is required."

Show the repository and the synthetic project input.

## 0:35–1:35 — Run the verified local prototype

```bash
pip install -e '.[dev]'
pytest -q
python -m cognisync --pretty
```

Show:

- a successful autonomous run;
- evidence attached to the insight;
- the audit stream created locally.

Explain that the prototype is deterministic and does not require cloud credentials.

## 1:35–2:35 — Demonstrate the consequence boundary

```bash
python -m cognisync --demo-gate --pretty
```

Point out:

- the external capability is classified as high risk;
- the run becomes `decision_required`;
- evidence and proposed payload remain visible;
- no external message is sent.

**Key phrase:** "Capability is not authorization."

## 2:35–3:15 — Resolve the local decision

```bash
python -m cognisync --demo-gate --approve --pretty
```

Then inspect:

```text
data/audit.jsonl
```

Point out the `decision.requested` and `decision.approved` events and the hash-chain fields.

State explicitly: this is a local approval-state demonstration. It is not a real-world send.

## 3:15–4:20 — Explain the production architecture

Show `docs/ARCHITECTURE.md` and `docs/THREAT_MODEL.md`.

Explain:

- Strands is the cognition/orchestration layer;
- a governed MCP/connector plane exposes narrow capabilities;
- durable memory is contextual, not an authorization mechanism;
- bounded A2A workers are optional and must prove measurable value;
- consequential effects pass through policy, human authorization and trusted connector confirmation.

## 4:20–5:00 — Why it matters

"Most agent demos optimize for what the model can do. CogniSync optimizes for useful work per unit of human supervisory attention. It collects signals, prepares work and checks evidence in the background, then interrupts only when a consequence requires a human decision. The agent owns the repetition; the human owns the consequence."

End on **CogniSync Professional** and the repository URL.

## Demo integrity rules

Never substitute a local approval event for external execution. Never claim an effect without connector confirmation. Keep the evidence, policy decision and audit trail visible during the demonstration.
