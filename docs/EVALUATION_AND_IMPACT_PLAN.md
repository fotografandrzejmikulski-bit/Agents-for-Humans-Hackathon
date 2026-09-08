# CogniSync — Evaluation & Impact Plan

## Purpose

CogniSync is evaluated as a socio-technical system, not only as a model benchmark. The primary question is whether it removes repetitive coordination work **without increasing unauthorized-action risk, notification burden, factual ambiguity, or recovery failures**.

## Primary hypothesis

> A background-first agent with evidence-backed preparation and consequence-aware escalation can reduce repetitive coordination effort while preserving or improving human control.

## Evaluation unit

The basic unit is a **workflow** with a fixed scenario, input fixture, capability set, and completion criterion. Results should be reported per workflow and aggregated across a declared sample size.

## Baselines

The evaluation compares at least three conditions:

1. **Manual baseline** — the professional performs the workflow without an agent.
2. **Interactive assistant baseline** — the professional actively prompts and supervises an assistant.
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

## Secondary diagnostics

Record false escalations, missed escalation opportunities, stale-evidence use, duplicate action attempts, timeout outcomes, operator overrides, and notification count. These diagnostics help explain why a headline metric changed.

## Quality floors

Productivity gains are invalid if they are obtained by weakening safety or factuality. A candidate release must therefore satisfy minimum floors for evidence coverage, authorization correctness, completion integrity, and safe fault handling.

A release is blocked when:

- an unknown capability is automatically executed;
- a consequential action bypasses the human decision boundary;
- an external effect is claimed without connector confirmation;
- evidence is missing from a high-impact recommendation when evidence was available;
- a fault causes the agent to continue in an unverifiable state;
- a resolved decision can be replayed against a different payload.

## Experimental design

### Phase A — deterministic regression

Use synthetic fixtures to verify policy, provenance, audit integrity, single-use decisions and empty-input behavior.

### Phase B — replay evaluation

Replay representative professional workflows with fixed inputs and compare the three baselines. Keep the scenario and completion criteria fixed across conditions.

### Phase C — adversarial evaluation

Inject prompt manipulation, malicious tool output, ambiguous requests, authority redefinition, duplicate events, stale evidence, timeout/failure responses and malformed connector results.

### Phase D — constrained pilot

Run with real users in a restricted environment. Record time saved, interaction frequency, escalation quality, recovery behavior and qualitative trust. No experimental deployment receives unrestricted destructive permissions.

## Falsification criteria

The hypothesis is considered unsupported if CogniSync repeatedly produces no material reduction in coordination effort, materially increases user burden, or cannot maintain the required safety floors under adversarial and fault-injection conditions.

## Reporting standard

Every experiment should record:

- configuration and model identifier;
- tool/capability set;
- scenario identifier;
- input fixture version;
- run identifier;
- sample size;
- measured metrics and units;
- failures, interventions and escalations;
- evaluator notes;
- evidence supporting or weakening each hypothesis.

Report aggregate statistics together with scenario-level failures. Do not replace missing measurements with estimated performance percentages.

This creates a reproducible evidence chain rather than a qualitative product demo alone.
