# CogniSync Professional — Five-Minute Demo Scenario

## Story

A professional is preparing a client website launch. Information arrives through email, notes and documents. The professional does not want another dashboard to babysit.

CogniSync runs in the background.

## 0:00–1:00 — Problem

Show the synthetic project input: visual direction approved, one final copy review, accessibility checks pending, launch target approaching, and a request for a concise progress report.

Say:

> The information is available. The scarce resource is attention. CogniSync absorbs the work of collecting, organizing and preparing it.

## 1:00–2:00 — Background work

Run:

```bash
python -m cognisync --pretty
```

Show the evidence-backed insight and source references. Emphasize that no human approval was needed for the read/analyze/prepare path.

## 2:00–3:15 — Consequence boundary

Run:

```bash
python -m cognisync --demo-gate --pretty
```

Show `decision_required`, the high-risk action, reason, evidence and proposed payload.

Say:

> Capability is not authorization. CogniSync can prepare the follow-up, but it cannot silently send it.

## 3:15–4:00 — Human resolution

Run:

```bash
python -m cognisync --demo-gate --approve --pretty
```

Then inspect `data/audit.jsonl` and show the approval event.

Say:

> The prototype proves the authorization transition. It does not fake a real-world send. A production MCP connector would execute only after authorization and report actual completion.

## 4:00–5:00 — Closing

Say:

> Most agent demos focus on what an agent can do. CogniSync also demonstrates what it should not do, when it should wait, and why it interrupts. Our optimization target is useful work per unit of human attention. The agent owns the repetition; the human owns the consequence.

## Integrity rules

- Use synthetic local data unless a real integration is explicitly enabled.
- Never claim an external action without connector confirmation.
- Keep the policy boundary visible.
- Show evidence and audit events, not only generated prose.
