# Data Governance

CogniSync processes professional project signals, so data handling is part of the product architecture rather than a documentation afterthought.

## Data classes

| Class | Examples | Default handling |
|---|---|---|
| Public | public project metadata, non-sensitive documents | may be processed normally |
| Internal | project notes, schedules, client drafts | least-privilege access; scoped to the task |
| Confidential | private client information, business records | explicit connector policy; minimize exposure |
| Secrets | API keys, tokens, credentials | never placed in model context or repository |

## Core principles

1. **Data minimization** — only task-relevant fields should cross a connector boundary.
2. **Purpose limitation** — information collected for one workflow should not silently become permanent memory.
3. **Provenance** — important outputs retain references to their source records.
4. **Scoped memory** — long-term memory is not an authorization mechanism.
5. **Least privilege** — connectors receive only the capabilities required for the workflow.
6. **Auditability** — important authorization and execution transitions are observable.
7. **Retention control** — production deployments must define retention and deletion policies for source data, derived state and audit records.

## Production requirements

Before processing real client data, the deployment should define:

- identity and access model;
- encryption at rest and in transit;
- secret management;
- data residency requirements where applicable;
- retention and deletion schedules;
- tenant/session isolation;
- incident response and access review;
- logging redaction rules.

The local hackathon prototype uses synthetic data and does not claim production-grade compliance certification.