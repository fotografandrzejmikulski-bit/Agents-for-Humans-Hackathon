## Change summary

Describe the user-visible or engineering change in one paragraph.

## Evidence

- [ ] Tests added or updated
- [ ] `pytest -q` passes
- [ ] `ruff check .` passes
- [ ] `python scripts/repo_quality_check.py` passes
- [ ] Documentation claim state is consistent with `docs/CLAIM_LEDGER.md`

## Safety / consequence boundary

- [ ] No new consequential capability bypasses `AutonomyPolicy`
- [ ] Unknown capabilities remain fail-closed
- [ ] External execution is never inferred from intent or model output
- [ ] Audit coverage is preserved for important state transitions

## Scope

- [ ] Local prototype only
- [ ] Production adapter / roadmap only
- [ ] External integration tested with a real connector

## Notes for reviewer

Call out limitations, assumptions, migration concerns, or intentionally deferred work.