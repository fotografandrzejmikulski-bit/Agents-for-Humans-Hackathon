# 5-Minute Demo Script

## 0:00–0:35 — The problem

**Narration:**

"Professionals do not need another chatbot to operate. They need repetitive work to disappear. CogniSync runs in the background, reads the signals that normally require manual attention, and surfaces a compact decision packet only when a human decision is actually needed."

Show the repository and the synthetic project input.

## 0:35–1:35 — Run the prototype

```bash
pip install -e '.[dev]'
pytest -q
python -m cognisync.cli --pretty
```

Show:

- a successful autonomous run;
- evidence attached to the insight;
- the audit file.

## 1:35–2:35 — Demonstrate the human gate

```bash
COGNISYNC_SEND=1 python -m cognisync.cli --pretty
```

Point out:

- the action is recognized as externally consequential;
- no external message is sent;
- the run changes to `decision_required`;
- the audit records the gate.

**Key phrase:** "Autonomy stops exactly where consequence begins."

## 2:35–3:35 — Explain the production architecture

Show `docs/ARCHITECTURE.md`.

Explain:

- Strands is the cognition/orchestration layer;
- AgentCore Gateway is the MCP integration boundary;
- AgentCore Memory supplies durable context;
- optional A2A workers handle bounded specialist jobs;
- AgentCore Runtime is the hosted execution boundary.

## 3:35–4:25 — Show scalability

Explain that the same design can connect to email, files, CRM and project systems while keeping authorization outside the model prompt. A2A workers can be added only when decomposition helps throughput, cost or specialization.

## 4:25–5:00 — Why it matters

"The product is not another assistant people must manage. It is an attention-management system. CogniSync takes the work humans repeatedly postpone — collecting signals, summarizing progress, preparing follow-ups, detecting blockers — and does it continuously. It brings the person back only for the decisions that deserve a person."

End on the repository URL and project name: **CogniSync Professional**.
