# CogniSync — Judgeable Demo

## 90-second local proof

```bash
python -m pip install -e '.[dev]'
pytest -q
python -m cognisync --pretty
```

Expected: CogniSync loads the synthetic project signal, produces an evidence-backed insight and exits without creating an external side effect.

## Safety boundary proof

```bash
python -m cognisync --demo-gate --pretty
```

Expected: the workflow reaches `decision_required`; the output contains the proposed action, risk and evidence. Nothing is sent or published.

## Human decision proof

```bash
python -m cognisync --demo-gate --approve --pretty
```

Expected: the local decision is recorded as approved. The prototype still performs no real external action; it proves the policy-to-HITL transition only.

## What judges should watch

1. Background work happens without conversational micromanagement.
2. Evidence remains attached to the insight.
3. A consequential capability crosses an explicit policy boundary.
4. The human resolves the boundary rather than supervising every read/draft operation.
5. Audit events make the path inspectable and tamper-evident.

## Production evolution

The local core is deliberately independent of credentials. The production architecture is designed to integrate a Strands-based agent with hosted runtime, durable memory, governed MCP connectors and bounded specialist delegation. Exact deployment commands, SDK versions, IAM configuration and service capabilities must be validated against the target environment before rollout.
