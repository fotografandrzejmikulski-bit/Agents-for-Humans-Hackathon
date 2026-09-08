# Milestone Acceptance Criteria

The grant plan is considered successful only when each milestone has observable acceptance evidence. Architecture diagrams or narrative claims alone are insufficient.

| Milestone | Acceptance criterion | Evidence |
|---|---|---|
| M1 — Reproducible prototype | A clean environment can install the project and run the deterministic demo successfully. | Clean-room installation log; `pytest -q`; CLI output |
| M2 — Evidence discipline | Candidate insights without required evidence are rejected before promotion. | Verification tests and failure-path output |
| M3 — Consequence control | Safe preparation completes autonomously; consequential capability produces a pending decision request; unknown capability is critical and gated. | Policy + decision-gate tests; demo transcript |
| M4 — Audit integrity | Audit chain detects modification, deletion/reordering, or broken predecessor linkage in covered records. | Integrity test suite and tampering fixture |
| M5 — Production integration path | Strands/Bedrock adapter is validated against the chosen runtime configuration without weakening the local safety contract. | Integration test report; configuration record |
| M6 — Evaluation pilot | Manual, interactive-assistant and CogniSync conditions can be compared on predefined metrics. | Dataset, protocol, raw measurements and analysis |
| M7 — Deployment hardening | Connector failures, timeouts and ambiguous outcomes do not silently become successful external actions. | Failure-injection tests and connector contract tests |

## Release gates

A release is blocked when any of the following is true:

1. `pytest` fails.
2. Static checks fail.
3. The public demo claims an external action without a connector-confirmed execution record.
4. An unknown capability can bypass the policy gate.
5. A verification failure still promotes candidate output as verified work.
6. Audit integrity checks fail on an otherwise valid audit chain.
7. A documentation claim is stronger than the evidence recorded in `docs/CLAIM_LEDGER.md`.

## Measurement principle

The project optimizes for **useful work per unit of human supervisory attention**, not raw agent activity. Any claimed improvement must be measured against a declared baseline and reported with sample size, task definition, intervention count and failure rate.