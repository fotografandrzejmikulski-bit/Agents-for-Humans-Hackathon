# CogniSync Professional — Threat Model

## Security objective

Prevent the agent from turning a correct inference into an unauthorized real-world action.

## Threats and controls

| Threat | Example | Control |
|---|---|---|
| Prompt injection | A document asks the agent to reveal secrets or bypass policy | Treat external content as untrusted; policy engine remains outside content |
| Over-permission | Agent can call destructive tools | Narrow tool catalog + explicit action classification |
| Credential exposure | API key appears in prompt or shell output | Credentials stay at integration boundary; never place secrets in repo |
| Silent side effect | Agent sends/publishes without consent | High/critical actions are gated |
| Hallucinated completion | Agent claims it sent a message | Require tool-confirmed execution status |
| Context poisoning | Low-quality memory changes future behavior | Evidence/provenance + evaluation of memory writes |
| Runaway execution | Repeated tool loops | Invocation/time/output limits and cancellation |
| Tool failure | Timeout or malformed result | Fail closed, audit error, retry only where policy allows |
| Data leakage | Cross-user context appears in response | Per-session/per-actor state partitioning and least privilege |

## Trust boundaries

1. **Untrusted input boundary** — documents, messages, web content and external records.
2. **Model boundary** — LLM output is advisory and is not itself authorization.
3. **Tool boundary** — tool calls are typed capabilities subject to policy.
4. **Human boundary** — final authority for consequential actions.
5. **Infrastructure boundary** — runtime isolation, IAM and service authentication.

## Security invariants

- The model never receives raw long-lived credentials.
- Unknown side effects default to critical risk.
- Audit records are produced for important state transitions.
- The agent never reports an external effect as complete without confirmation.
- Synthetic local demo data contains no production secrets.

## Residual risk

No framework or prompt can replace infrastructure security. Production operation requires correctly scoped IAM, network boundaries, secret management, observability, rate limits, data retention controls and continuous adversarial testing.
