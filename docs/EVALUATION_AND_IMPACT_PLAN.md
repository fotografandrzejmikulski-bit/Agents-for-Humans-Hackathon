# CogniSync — Evaluation & Impact Plan

## Purpose

The project is evaluated as a socio-technical system, not only as a model benchmark. The primary question is whether CogniSync can remove repetitive coordination work **without increasing unauthorized action risk, notification burden, or decision ambiguity**.

## Primary hypothesis

> A background-first agent with evidence-backed preparation and consequence-aware escalation can reduce repetitive coordination effort while preserving or improving human control.

## Baselines

The evaluation compares at least three conditions:

1. **Manual baseline** — user performs the coordination workflow without an agent.
2. **Interactive assistant baseline** — user actively prompts and supervises an assistant.
3. **CogniSync** — background preparation plus exception-based human decision gates.

## Primary metrics

| Metric | Definition | Direction |
|---|---|---|
| Coordination time | Minutes spent collecting, synthesizing and drafting routine project information | lower |
| Human interventions | Number of human interactions required per completed workflow | lower, subject to quality floor |
| Attention load | Interruptions or decision prompts per unit of useful work | lower |
| Evidence coverage | Fraction of material claims carrying traceable evidence | higher |
| Escalation precision | Fraction of escalations that correctly require human authority | higher |
| Unauthorized side effects | External actions without valid authorization | zero |
| Completion integrity | External actions reported as complete only when connector-confirmed | 100% |
| Recovery rate | Workflows recovered safely after tool/model faults | higher |
| User trust | Human-rated clarity and appropriateness of decision packets | higher |

## Quality floors

Productivity gains are invalid if they are obtained by weakening safety or factuality. A candidate release must therefore satisfy minimum floors for evidence coverage, action authorization, and completion integrity.

A release is blocked when:

- an unknown capability is automatically executed;
- a consequential action bypasses the human decision boundary;
- an external effect is claimed without connector confirmation;
- evidence is missing from a high-impact recommendation when evidence was available;
- a fault causes the agent to continue in an unverifiable state.

## Experimental design

### Phase A — deterministic regression

Use synthetic fixtures to verify policy, provenance, audit integrity, idempotency and empty-input behavior.

### Phase B — replay evaluation

Replay representative professional workflows with fixed inputs and compare the three baselines.

### Phase C — adversarial evaluation

Inject prompt manipulation, malicious tool output, ambiguous requests, authority redefinition, duplicate events, stale evidence and tool failures.

### Phase D — pilot

Run with real users in a constrained environment. Record time saved, interaction frequency, escalation quality and qualitative trust. No experimental deployment receives unrestricted destructive permissions.

## Falsification criteria

The hypothesis is considered unsupported if CogniSync repeatedly produces no material reduction in coordination effort, materially increases user burden, or cannot maintain the required safety floors under adversarial and fault-injection conditions.

## Reporting

Every experiment should record:

- configuration and model identifier;
- tool/capability set;
- scenario identifier;
- input fixture version;
- run identifier;
- measured metrics;
- failures and interventions;
- evaluator notes;
- decision whether the evidence supports or weakens the hypothesis.

This creates a reproducible evidence chain rather than a qualitative product demo alone.
