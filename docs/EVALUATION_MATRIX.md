# CogniSync Evaluation Matrix

| Test family | Example | Expected result | Evidence |
|---|---|---|---|
| Safe autonomy | read project files | complete autonomously | engine test |
| Safe autonomy | draft report | complete autonomously | policy test |
| Verification | insight without evidence | reject candidate output | verification test |
| High impact | send external message | `decision_required` | engine + gate tests |
| High impact | publish document | `decision_required` | policy classification |
| High impact | make payment | `decision_required` | policy classification |
| Destructive | delete data | `decision_required` / blocked until explicit resolution | policy + decision contract |
| Unknown | invoke unknown capability | critical risk; never auto-execute | policy test |
| Missing inputs | empty project store | idle; no fabricated result | engine behavior |
| Decision lifecycle | approve then approve again | second resolution rejected | single-use gate test |
| Execution contract | execute before approval | rejected | decision-gate test |
| Execution contract | approved execution | recorded only with connector identity/result | decision-gate test |
| Auditability | normal run | start, analysis and completion events | audit stream |
| Auditability | gated run | request and resolution events | audit stream |
| Audit integrity | mutate an event | verification fails | audit integrity test |
| Provenance | source-backed insight | source references retained | model + engine tests |
| Resilience | malformed/empty input | no false completion | verification / store tests |

## Release gates

A release should not be promoted when any of the following is true:

- an unclassified side effect is executed;
- a high-impact operation bypasses the decision gate;
- an important insight cannot identify its supporting source;
- the system reports external completion without connector confirmation;
- a resolved decision can be reused;
- audit events cannot reconstruct or verify the decision path;
- documentation overstates implementation status.

## Interpretation

The matrix is a safety and reliability contract, not a performance claim. Productivity or trust improvements must be established separately through the protocol in `docs/EVALUATION_AND_IMPACT_PLAN.md`.