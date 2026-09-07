# Release Notes — CogniSync Professional 0.2.0

## Submission hardening

The project has been upgraded from a concept-heavy prototype into a judgeable submission package with explicit separation between autonomous preparation, authorization and execution.

### Added

- consequence-aware decision gate;
- fail-closed risk policy;
- evidence/provenance helpers;
- append-only audit events;
- deterministic local demo;
- heartbeat/background-work abstraction;
- health/readiness helper;
- evaluation matrix and release gates;
- threat model;
- judge-focused review guide;
- professional English grant application;
- CI workflow for lint and tests;
- clean repository submission checklist.

### Correctness posture

The repository does not claim that AWS infrastructure is already provisioned. AgentCore Runtime, Memory, Gateway/MCP and A2A are production integration targets documented against current platform capabilities.

The local prototype intentionally uses synthetic data and never pretends that a simulated approval performed a real-world side effect.

## Release invariant

`prepared != authorized != executed`

Any future connector must preserve this invariant.
