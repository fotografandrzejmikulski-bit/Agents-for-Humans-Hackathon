# Judge Guide — CogniSync Professional

This guide is designed for a reviewer who has 3–5 minutes to understand and verify the submission.

## 1. What to notice first

CogniSync is not a chatbot demo. It demonstrates a **background-first operating model**:

`observe → analyze → prepare → evaluate consequence → act or wait → audit`

The defining boundary is:

> The model may recommend an action. Authorization is a separate system decision.

## 2. Fastest verification path

### A. Safe autonomous work

```bash
python -m cognisync --pretty
```

Expected:

- `status: completed`
- evidence-backed insight(s)
- source references retained
- no human gate
- no claim of external execution

### B. Consequential action

```bash
python -m cognisync --demo-gate --pretty
```

Expected:

- `status: decision_required`
- explicit action classification
- high-risk decision request
- evidence attached
- proposed payload attached

### C. Human resolution

```bash
python -m cognisync --demo-gate --approve --pretty
```

Expected:

- approval event is written to the audit trail
- the local prototype still performs **no real external send**

This distinction is intentional. A production connector would execute only after policy authorization and would return tool-confirmed completion.

## 3. Code paths worth inspecting

| Concern | File | Why it matters |
|---|---|---|
| Background orchestration | `cognisync/engine.py` | separates observation/analysis from side effects |
| Risk taxonomy | `cognisync/policy.py` | fail-closed action classification |
| Human gate | `cognisync/decision.py` | explicit approval boundary |
| Evidence | `cognisync/analysis.py`, `cognisync/evidence.py` | provenance is carried into results |
| Auditability | `cognisync/audit.py` | append-only state-transition record |
| Real model adapter | `cognisync/agent.py` | Strands/Bedrock integration point |
| Tests | `tests/` | demonstrates normal and adversarial boundary behavior |

## 4. What is prototype vs production

The local core is executable without AWS credentials.

The AWS/AgentCore components are an explicit production integration path, not a false claim that cloud resources have already been provisioned.

This makes the submission reproducible and keeps architecture claims auditable.

## 5. The design thesis

Most agent systems optimize for **more autonomous activity**.

CogniSync optimizes for:

**useful work per unit of human attention**.

The human is removed from repetitive coordination, but remains the authority over meaningful consequences.

## 6. Expected judging evidence

A strong evaluation should be able to verify that:

1. safe work is completed without approval;
2. consequential work is gated;
3. unknown actions fail closed;
4. evidence is preserved;
5. audit records reconstruct the decision path;
6. the cloud design is credible without overstating deployment status.
