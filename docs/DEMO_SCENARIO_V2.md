# CogniSync Professional — Canonical Five-Minute Demo Scenario

## Story

A professional is preparing a client website launch. Information arrives through email, notes and documents. The professional does not want another dashboard to babysit.

CogniSync runs in the background.

## 0:00–0:45 — Problem

Show the synthetic project input: visual direction approved, one final copy review, accessibility checks pending, launch target approaching, and a request for a concise progress report.

Say:

> The information is available. The scarce resource is attention. CogniSync absorbs the work of collecting, organizing and preparing it.

## 0:45–1:45 — Background work

Run:

```bash
python -m cognisync --pretty
```

Show the evidence-backed insight and source references. Emphasize that no human approval is needed for the safe read/analyze/prepare path.

## 1:45–2:45 — Consequence boundary

Run:

```bash
python -m cognisync --demo-gate --pretty
```

Show:

- `decision_required`;
- the requested capability;
- risk level;
- evidence;
- proposed payload;
- explicit statement that no external execution occurred.

Say:

> Capability is not authorization. CogniSync can prepare the follow-up, but it cannot silently send it.

## 2:45–3:30 — Human resolution

Run:

```bash
python -m cognisync --demo-gate --approve --pretty
```

Show the transition from `pending` to `approved`.

Say:

> Approval changes authorization state. It does not invent proof that an external system executed the action.

## 3:30–4:15 — Audit integrity

Run the canonical Python demo if desired:

```bash
python scripts/demo.py
```

Show the final `AUDIT INTEGRITY` result and explain that the local audit chain can detect tampering.

## 4:15–5:00 — Closing

Say:

> Most agent demos focus on what an agent can do. CogniSync also demonstrates what it should not do, when it should wait, and why it interrupts. Our optimization target is useful work per unit of human attention. The agent owns the repetition; the human owns the consequence.

## Integrity rules

- Use synthetic local data in the public demo.
- Never claim a real external effect without trusted connector confirmation.
- Never treat local approval as external execution.
- Keep evidence and policy state visible.
- Use the claim ledger to distinguish implementation from roadmap.