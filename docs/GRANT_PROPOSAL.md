# Grant Proposal

## CogniSync Professional
### A background-first AI system for reducing repetitive professional work while preserving human control

**Applicant:** Andrzej Mikulski  
**Track:** Professional Agents  
**Hackathon:** Agents for Humans Hackathon 2026  
**Repository:** https://github.com/fotografandrzejmikulski-bit/Agents-for-Humans-Hackathon

---

## 1. Executive Summary

CogniSync Professional is an AI agent designed to remove repetitive professional work without forcing professionals to become full-time operators of an AI system.

The system continuously processes project signals — messages, documents, notes, status updates and structured business records — and converts them into evidence-backed summaries, detected blockers, follow-up drafts and decision-ready work packages. It performs low-risk preparation autonomously. When a proposed action would create an external or consequential side effect, CogniSync stops and asks the human to decide.

The core innovation is therefore not simply greater autonomy. It is **bounded autonomy optimized for human attention**.

The project targets creators, independent professionals, consultants, makers and small-business owners whose days are fragmented by repetitive coordination and judgment-heavy administrative work. The Professional Agents track explicitly calls for agents that make professionals dramatically better at work they already do, especially repetitive and judgment-heavy workloads. citeturn437470view0

The prototype in this repository is deliberately judgeable without cloud credentials. It includes a working local orchestration core, a least-privilege action policy, evidence propagation, an approval gate, append-only audit logging, tests and an adapter for a real Strands/Bedrock execution path.

---

## 2. Problem Statement

Knowledge workers lose substantial attention not only to large tasks, but to the accumulation of small coordination tasks:

- collecting status from scattered sources;
- reading and classifying incoming information;
- identifying what changed since the last review;
- drafting routine follow-ups;
- assembling progress reports;
- detecting blockers before they become urgent;
- deciding which items actually require the professional's attention.

Conventional assistant interfaces often shift this coordination burden onto the user. The human must repeatedly open the assistant, supply context, inspect intermediate results and approve many low-value operations.

This creates an **attention inversion**: the technology intended to reduce work becomes another system that must be managed.

CogniSync addresses the inversion by making the agent responsible for background preparation while making the human the final authority over consequential actions.

---

## 3. Target Beneficiaries

The initial target audience is a solo or small-team professional operating in a high-context environment:

- photographers and other creative professionals managing client work;
- consultants and freelancers coordinating deliverables;
- small agencies managing multiple projects;
- independent makers and service businesses handling repeated communication and reporting.

These users often have enough digital tooling to generate data but not enough operational bandwidth to continuously synthesize it.

The product is designed to sit **above** those systems rather than replace them.

---

## 4. Project Objectives

### Objective 1 — Eliminate routine cognitive overhead

Turn raw project signals into concise, evidence-backed work products without requiring repeated manual prompting.

### Objective 2 — Preserve human agency

Keep humans in control of external communication, publication, financial operations, destructive actions and other high-consequence effects.

### Objective 3 — Make agent behavior inspectable

Provide provenance, explicit policy decisions and an append-only audit trail for every meaningful workflow.

### Objective 4 — Build a credible path from prototype to production

Use Strands Agents as the agent orchestration layer and maintain compatibility with Amazon Bedrock AgentCore Runtime, Memory, Gateway/MCP and A2A as the production infrastructure.

### Objective 5 — Measure usefulness and restraint together

Do not optimize only for task completion. Measure the system's ability to know when it should act, when it should wait, and when it must ask.

---

## 5. Technical Innovation

CogniSync is organized around five architectural primitives.

### 5.1 Background Work Loop

The agent repeatedly performs:

**ingest → interpret → synthesize → prepare → gate → surface**

This creates a product experience in which the user interacts with outcomes, not with every internal step.

### 5.2 Consequence-Aware Autonomy

The action policy separates safe information work from externally consequential operations.

The default posture is:

- low-risk internal work: autonomous;
- ambiguous or reversible internal actions: policy-dependent;
- high-impact external actions: approval required;
- unknown or unclassified side effects: fail closed.

This is more defensible than a generic "autonomous agent" design because authorization is represented as a first-class system boundary rather than hidden inside prompting.

### 5.3 Evidence-Carrying Decisions

Every important insight carries source references and confidence. A human decision request therefore contains both the proposed action and the evidence supporting it.

This reduces the cost of supervision: the user does not need to reconstruct why the system reached a conclusion.

### 5.4 Context and Long-Term Personalization

A production deployment can use AgentCore Memory for session continuity and long-term user preferences, semantic facts and session summaries. AWS documents these strategies as built-in AgentCore Memory capabilities. citeturn493810search3turn493810search4

### 5.5 Bounded Multi-Agent Delegation

A supervisor can delegate narrowly defined specialist work through A2A when it provides value. Strands supports A2A and an `A2AAgent` abstraction; AgentCore Runtime supports hosted A2A servers with standard discovery and JSON-RPC interactions. citeturn493810search0turn888617search0

The design explicitly avoids uncontrolled agent swarms. Delegation is a capacity and specialization mechanism, not an aesthetic choice.

---

## 6. AWS and Strands Integration

The project is built around the Strands Agents SDK, which is the required framework for the hackathon. Strands is a library that runs in the application's own process and supports model-provider flexibility; Strands 1.0 introduced production-oriented multi-agent primitives and A2A support. citeturn493810search8turn888617search5

For production hosting, Amazon Bedrock AgentCore Runtime is the target execution environment. AWS describes it as a secure, serverless, purpose-built environment that is framework-agnostic and supports MCP and A2A communication. citeturn888617search8

For tool access, AgentCore Gateway provides a managed MCP boundary and handles authentication and target invocation. citeturn493810search2turn493810search11

For durable context, AgentCore Memory provides built-in strategies for user preferences, semantic memory and summaries. citeturn493810search3turn493810search4

For evaluation, the Strands Evals ecosystem supports output/trajectory analysis, tool-use evaluation, trace-based evaluation, failure diagnosis, chaos testing and red-team evaluation. citeturn493810search9turn493810search6

---

## 7. Prototype and Current State

The repository now contains:

1. a deterministic local orchestration engine;
2. a Strands/Bedrock adapter;
3. a project input store;
4. a risk-aware autonomy policy;
5. a human decision gate;
6. append-only JSONL audit logging;
7. a CLI for local demonstration;
8. unit tests covering normal operation and safety gating;
9. an architecture specification;
10. a five-minute demonstration script;
11. this grant proposal.

This structure is intentionally stronger than a code-only proof of concept. A judge can run the system locally, inspect its decision logic, and understand the production architecture without being asked to trust claims that cannot be reproduced.

---

## 8. Expected Impact

CogniSync aims to create measurable improvements in the daily operating environment of professionals.

### Primary impact

Reduce the amount of human time spent collecting, sorting and preparing routine professional information.

### Secondary impact

Improve consistency and timeliness of follow-ups and project reporting while preserving human review for consequential decisions.

### Systemic impact

Demonstrate a practical design pattern for human-centered autonomy in which the optimization target is not maximum agent activity but maximum **useful work per unit of human attention**.

---

## 9. Measurement Framework

The project will be evaluated using a balanced scorecard.

| Dimension | Measure | Desired direction |
|---|---|---|
| Productivity | Minutes of repetitive work removed | Up |
| Responsiveness | Input-to-decision-ready-brief latency | Down |
| Attention | Human interventions per completed workflow | Down, without lowering quality |
| Quality | Task success / acceptance rate | Up |
| Grounding | Evidence coverage of important insights | Up |
| Safety | Unsafe external actions executed | Zero |
| Precision | Correct escalation rate | Up |
| Efficiency | Cost per completed workflow | Down |
| Resilience | Recovery after simulated tool failures | Up |

---

## 10. Evaluation and Red-Team Plan

The project will be evaluated against three classes of failure.

### A. Over-automation

Examples: sending a message, publishing a document or changing a record without explicit authority.

Success criterion: consequential actions are consistently intercepted by the policy gate.

### B. Under-automation

Examples: asking for approval for every low-risk read or drafting operation.

Success criterion: safe repetitive work completes autonomously without notification spam.

### C. Model / Tool Failure

Examples: malformed tool result, timeout, duplicated input, partial context or adversarial instruction.

Success criterion: the system fails safely, preserves auditability and does not silently invent completion.

Strands Evals provides the appropriate foundation for trajectory, tool-use, trace, chaos and adversarial evaluation. citeturn493810search9turn493810search6

---

## 11. Security and Responsible AI

CogniSync follows a least-privilege architecture.

Sensitive credentials should remain at the integration boundary rather than inside prompts. AgentCore Gateway is positioned as the managed MCP access layer. External side effects are classified explicitly. Unknown operations default to a critical-risk state.

For shell execution, Strands Shell can provide a default-deny mediation layer for files and network access, but it should not be described as a hardened OS sandbox. Production deployment should rely on appropriate hosted isolation and IAM controls in the target environment. citeturn916868search1turn916868search6

The project also avoids synthetic certainty: the prototype distinguishes successful local computation from external real-world completion.

---

## 12. Implementation Roadmap

### Phase 1 — Hackathon prototype

Completed in the current repository:

- local background workflow;
- policy engine;
- evidence model;
- audit log;
- tests;
- Strands integration adapter;
- competition documentation.

### Phase 2 — Cloud deployment

- deploy supervisor on AgentCore Runtime;
- connect AgentCore Memory;
- configure Gateway/MCP targets;
- establish IAM boundaries;
- add telemetry and trace correlation.

### Phase 3 — Workflow expansion

Initial professional workflows:

- daily project brief;
- client follow-up preparation;
- progress reporting;
- blocker detection;
- meeting-to-action extraction;
- deliverable readiness checks.

### Phase 4 — Specialist A2A workers

Introduce specialized agents only where they create measurable gains in latency, quality or cost.

### Phase 5 — Continuous evaluation

Run regression, fault-injection and red-team suites against each release and maintain an auditable baseline of safety and usefulness metrics.

---

## 13. Sustainability and Scalability

The system is intentionally modular. The same cognitive core can process different professional workflows by changing the input adapters, domain policies and tool catalog rather than rebuilding the agent from scratch.

The architecture also preserves model flexibility. Strands is designed to work across supported model providers, while AgentCore Runtime is documented as model-flexible and framework-agnostic. citeturn493810search8turn888617search8

This enables a cost-aware routing model in which high-value reasoning can be handled by stronger models while repetitive bounded workloads can use less expensive alternatives, subject to evaluation gates.

---

## 14. Competitive Differentiation

CogniSync is differentiated by its operating philosophy rather than by a larger collection of integrations.

### Existing assistant paradigm

Human opens system → provides context → supervises execution → receives result.

### CogniSync paradigm

System gathers context → performs safe background work → prepares evidence → waits at the consequence boundary → surfaces only the decision.

The product therefore treats **human attention as the scarce resource**.

---

## 15. Why This Project Fits the Hackathon

The hackathon asks for a new Strands-based AI agent that performs real work for people, especially repetitive work, and highlights background operation with human interaction only when meaningful decisions arise. CogniSync is designed specifically around that behavior and targets the Professional Agents track. citeturn437470view0

The project also addresses the published evaluation criteria directly:

- **Technical Implementation:** real executable prototype, Strands integration, safety policy, tests and a clear AgentCore production path;
- **Design:** background-first user experience rather than a chatbot that requires constant operation;
- **Potential Impact:** explicit target users, workflows and measurable outcomes;
- **Creativity & Originality:** consequence-aware autonomy and attention optimization as the core design principle;
- **Presentation:** a reproducible five-minute end-to-end demo narrative.

---

## 16. Requested Support / Grant Use

Grant support would accelerate the transition from the current reproducible prototype to a real-world professional pilot.

Priority investment areas:

1. **Cloud execution and evaluation** — AgentCore Runtime, memory, integration testing and telemetry.
2. **Professional connectors** — carefully scoped MCP integrations for real workflows.
3. **Safety and reliability engineering** — adversarial tests, chaos testing, policy refinement and evaluation infrastructure.
4. **Pilot validation** — measuring time saved, intervention rates and user trust with professional users.
5. **Open-source delivery** — documentation, reference integrations and reusable architecture patterns for other builders.

The goal is not merely to demonstrate an agent that can act. The goal is to demonstrate a system that knows **what it can do autonomously, what it must ask, and why**.

---

## 17. Final Statement

CogniSync Professional proposes a different contract between people and agents.

The agent should not demand more attention than the work it replaces.

It should absorb repetitive coordination, preserve evidence, learn stable working preferences, collaborate with specialist agents when useful, operate securely through controlled tool boundaries, and stop exactly where a human decision becomes meaningful.

That is the practical path toward human-centered autonomy: not removing humans from the loop, but removing humans from the parts of the loop that never needed them.
