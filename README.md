# CogniSync Professional + Sovereign AI Project Portfolio

> **A background-first agent system and applied AI portfolio that turns project noise into decision-ready work — while keeping the human in control of consequences.**

This repository began as a minimal/near-empty hackathon scaffold and has been expanded into a coherent engineering portfolio. fileciteturn2file0L1-L2

## Flagship project — CogniSync Professional

CogniSync is a Strands Agents–based professional agent for background coordination work.

**observe → interpret → prepare → evaluate consequence → act or wait → surface → audit**

The local prototype demonstrates autonomous background analysis, source-backed insights, a model-independent consequence policy, human decision gates, fail-closed handling of unknown operations, append-only audit events, a Strands/Bedrock adapter, automated tests and CI, plus a documented path to AgentCore Runtime, Memory, Gateway/MCP and A2A.

The key system boundary is explicit: **model capability is not authorization**.

## Portfolio derived from the supplied research corpus

The uploaded materials contain several strong technical and product directions. They are now organized as buildable projects rather than remaining disconnected notes:

| Project | Role | State |
|---|---|---|
| **01 — CogniSync Professional** | Background professional agent | Prototype |
| **02 — Sovereign Edge Agent** | Local AI execution substrate | Architecture + benchmark plan |
| **03 — Open Creator Layer** | Buildbox-class creation UX over Unity/Unreal | MVP design |
| **04 — Influence Literacy Lab** | Defensive analysis of persuasive systems | Research product |
| **05 — AI Content Product Studio** | Productized content-production workflows | Product design |

See [`projects/00-portfolio/PROJECT_PORTFOLIO.md`](projects/00-portfolio/PROJECT_PORTFOLIO.md).

## Project 02 — Sovereign Edge Agent

The supplied local-AI material describes Gemma 3 27B on RTX 3070-class hardware, GGUF Q4_K_M, CPU/GPU offloading, local Deep Search, Rclone-backed Google Drive, MCP and a neuro-symbolic verification loop. The source recommends starting points such as 18–20 GPU layers and 16k–32k context on 32 GB RAM; those figures are intentionally treated as **benchmark hypotheses**, not guarantees. fileciteturn69file6L258-L289

The supplied documents also propose syntax/lint/sandbox verification plus bounded self-correction for generated code. fileciteturn68file12L534-L555

The project strengthens these ideas with:

`model → typed tools → policy → verification → human gate → audit`

## Project 03 — Open Creator Layer

The Buildbox analysis proposes an **Engine-on-Engine** strategy: retain Unity/Unreal as the underlying rendering/runtime platform while providing a much simpler creator UX. It identifies Mind Map navigation, visual scripting, Smart Assets, build automation and monetization abstraction as core experience pillars. fileciteturn66file1L50-L69

The project therefore centers on a typed graph, engine-independent project model, native engine adapters, compiler/validator and AI-assisted authoring.

## Project 04 — Influence Literacy & Ethical Communication Lab

The influence corpus covers reciprocity, social proof, attention capture, gaze cueing, habit loops, visual rhetoric and the proposed VNLC framework. fileciteturn66file2L87-L140

Some source material describes covert subliminal-control techniques. Those are not turned into an operational manipulation engine. Instead, the project uses the same analytical vocabulary defensively: detect persuasive mechanisms, surface hidden pressure, recommend disclosure and generate transparent alternatives. The source itself identifies media literacy, deliberate decision slowing and metadata analysis as countermeasures. fileciteturn68file3L152-L160

## Project 05 — AI Content Product Studio

The supplied visual material contains reusable patterns for blog writing, ideal-customer targeting, hooks, social proof, calls to action, and pre-written email/newsletter templates. It identifies niches such as Etsy sellers, coaches, digital-product creators and service providers. fileciteturn64file6L1-L10

The product architecture is:

`research → audience model → offer → content system → generation → QA → packaging → human approval → publishing`

## Shared platform architecture

```text
                 ┌──────────────────────────────┐
                 │      Model / Reasoning       │
                 │ local or cloud, provider-agn.│
                 └──────────────┬───────────────┘
                                │
                 ┌──────────────▼───────────────┐
                 │      Tool / MCP boundary     │
                 │ files • web • cloud • engines│
                 └──────────────┬───────────────┘
                                │
                 ┌──────────────▼───────────────┐
                 │ Evidence + Memory + Context │
                 └──────────────┬───────────────┘
                                │
                 ┌──────────────▼───────────────┐
                 │ Policy / Consequence Engine │
                 └──────────────┬───────────────┘
                                │
                 ┌──────────────▼───────────────┐
                 │ Verification / Evaluation   │
                 └──────────────┬───────────────┘
                                │
                 ┌──────────────▼───────────────┐
                 │ Human Decision Boundary     │
                 └──────────────┬───────────────┘
                                │
                 ┌──────────────▼───────────────┐
                 │ Action / Artifact / Audit   │
                 └──────────────────────────────┘
```

This shared control plane is the portfolio's central architectural insight: model intelligence is one component; durable value comes from the evidence, tools, policies, verification and human-control layers around it.

## Judge / reviewer quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
pytest -q
python -m cognisync --pretty
python -m cognisync --demo-gate --pretty
python -m scripts.demo
```

The local demo proves the authorization transition but does **not** pretend to send a real external message.

## Documentation

- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) — technical architecture and deployment progression.
- [`docs/GRANT_PROPOSAL.md`](docs/GRANT_PROPOSAL.md) — professional English application.
- [`docs/DEMO_SCENARIO_V2.md`](docs/DEMO_SCENARIO_V2.md) — five-minute demonstration narrative.
- [`docs/EVALUATION_MATRIX.md`](docs/EVALUATION_MATRIX.md) — evaluation and release gates.
- [`docs/THREAT_MODEL.md`](docs/THREAT_MODEL.md) — threat model and security invariants.
- [`docs/BUILD_NOTES.md`](docs/BUILD_NOTES.md) — source-to-implementation decisions.
- [`projects/`](projects/) — expanded project portfolio.

## Evidence policy

Every important technical statement is classified as one of:

**source-derived claim → engineering hypothesis → verified behavior → future roadmap**

This is particularly important for hardware performance, third-party integrations, ecosystem capabilities and market claims. The supplied documents remain the knowledge source for their concepts; implementation and validation status must be stated separately.

## Safety principle

For all agentic projects in this portfolio:

**prepared ≠ authorized ≠ executed**

The objective is not to maximize autonomous activity. It is to maximize useful work while minimizing unnecessary human supervision.

## License

MIT.
