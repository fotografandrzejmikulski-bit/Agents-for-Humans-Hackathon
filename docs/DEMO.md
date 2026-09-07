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
3. A consequential action crosses an explicit policy boundary.
4. The human resolves the boundary rather than supervising every read/draft operation.
5. Audit events make the path inspectable.

## Cloud evolution

The local core is deliberately independent of credentials. The production path is Strands + Amazon Bedrock AgentCore Runtime, with AgentCore Memory for durable context, AgentCore Gateway for authenticated MCP access and A2A for bounded specialist delegation. AWS currently documents `agentcore create`/`agentcore deploy` workflows and A2A hosting through `StrandsA2AExecutor` and `serve_a2a`.
