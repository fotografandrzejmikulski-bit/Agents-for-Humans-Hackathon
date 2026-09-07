# Submission Checklist — Agents for Humans Hackathon 2026

## Repository readiness

- [x] Public GitHub repository
- [x] Strands Agents-based implementation surface
- [x] Professional Agents positioning
- [x] Runnable local prototype without AWS credentials
- [x] README with quick start, architecture and security model
- [x] Mermaid architecture diagram
- [x] MIT license
- [x] Automated tests and CI workflow
- [x] Explicit human decision gate
- [x] Fail-closed unknown-action policy
- [x] Evidence and provenance model
- [x] Append-only audit trail
- [x] Background heartbeat component
- [x] Judgeable five-minute demo scenario
- [x] English grant proposal
- [x] Threat model and evaluation matrix

## Final submission actions

- [ ] Confirm hackathon registration on Devpost
- [ ] Confirm final Devpost submission fields
- [ ] Record final demo video within the published five-minute limit
- [ ] Add the final demo URL to the Devpost submission
- [ ] Confirm AWS promotional-credit request before its published deadline
- [ ] Perform a clean-room clone/install/test from the public repository
- [ ] Run `pytest -q`
- [ ] Run `ruff check .`

## What the demo must prove

1. Background work happens without continuous human supervision.
2. Important outputs retain evidence.
3. Consequential actions cross an explicit policy boundary.
4. Human approval/rejection is auditable.
5. Unknown actions fail closed.
6. No external completion is claimed without real connector confirmation.

## Current honest scope

The repository contains a functional local prototype and production-oriented architecture. A live AWS deployment, real MCP integrations, notification channel and cloud telemetry are environment-specific next steps and must not be represented as already deployed unless provisioned and verified.
