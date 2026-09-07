# End-to-End Prototype Scenario

## Scenario: Client launch readiness

A professional is preparing a client website launch. During the day, project signals arrive from different sources. The user does not want to open an assistant repeatedly.

### Background phase

CogniSync ingests the project inputs and identifies:

- the visual direction is approved;
- homepage copy needs a final review;
- accessibility checks are pending;
- launch timing is approaching;
- a concise status report is useful.

The system autonomously prepares a brief with evidence and recommended next action.

### Decision phase

Suppose the workflow also requests sending a client confirmation. `send_external_message` is classified as high risk.

CogniSync does **not** send the message. It produces a decision packet:

```json
{
  "status": "decision_required",
  "action": "send_external_message",
  "risk": "high",
  "reason": "An external side effect was requested by configuration.",
  "evidence": ["email: Launch"],
  "proposed_payload": {"run_id": "...", "request": "send follow-up"}
}
```

This is the central product moment: the agent has done the preparation, but the person retains control of the consequence.

## Why this scenario is strong for judging

It demonstrates the complete loop in under five minutes:

**real-ish professional problem → autonomous background work → evidence → risk classification → human gate → auditable outcome**

It also makes the product thesis visible instead of relying on an architecture diagram alone.
