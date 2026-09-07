# Project 02 — Sovereign Edge Agent

## Purpose

A local-first engineering agent for constrained consumer hardware. The source corpus describes a Gemma 3 27B setup around an RTX 3070 8 GB GPU, 32 GB RAM, GGUF quantization, CPU/GPU offloading, local research, Rclone-mounted cloud data, MCP tools, and a neuro-symbolic verification loop.

## Source-derived baseline

The corpus proposes:

- Gemma 3 27B in GGUF Q4_K_M form;
- roughly 18–20 GPU layers as an initial RTX 3070 target;
- 16k–32k context as a practical range for 32 GB RAM;
- Open WebUI + SearXNG for local research;
- Rclone/WinFsp for multi-drive Google Drive access;
- MCP for filesystem and engine control;
- Unity and Unreal integrations;
- NSVIF-style generation → verification → feedback loops.

These figures are treated as **starting hypotheses**. Actual memory use and tokens/sec must be measured on the target machine because quantization, KV-cache settings, context length, backend version and thermals materially affect results. The source itself gives a 3–6 token/s expectation, but this repository does not present that figure as a guarantee. fileciteturn69file6L258-L289

## Architecture

```text
                    ┌─────────────────────────┐
                    │    Local Supervisor     │
                    │  planning + policy      │
                    └───────────┬─────────────┘
                                │
              ┌─────────────────┼─────────────────┐
              │                 │                 │
        ┌─────▼─────┐     ┌─────▼─────┐     ┌────▼─────┐
        │ Gemma /   │     │ MCP Tool  │     │ Research │
        │ llama.cpp │     │ Boundary  │     │ SearXNG  │
        └─────┬─────┘     └─────┬─────┘     └────┬─────┘
              │                 │                 │
        ┌─────▼─────┐     ┌─────▼─────┐     ┌────▼─────┐
        │ GPU + RAM │     │ Files /   │     │ Direct   │
        │ offload   │     │ Drive     │     │ Context  │
        └───────────┘     └───────────┘     └──────────┘
                                │
                         ┌──────▼──────┐
                         │ Verification│
                         │ syntax/lint │
                         │ policy      │
                         └─────────────┘
```

## Core design improvement

The most important upgrade over the source material is separating **model capability** from **authorization**. Even a local model with broad tool access must never be the sole authority for destructive operations.

The local agent therefore uses:

1. typed tool capabilities;
2. allow/deny policies outside the prompt;
3. static verification for generated code;
4. bounded retries;
5. human approval for consequential actions;
6. complete local audit logs.

The supplied material already identifies the need for an NSVIF-style verification loop because generated code can contain syntax and operational errors. fileciteturn68file12L534-L555

## Research stack

The source corpus proposes Open WebUI + SearXNG, with JSON search responses and local Docker/WSL2 deployment. fileciteturn69file13L559-L590

The stronger architecture uses a three-stage evidence pipeline:

`search → retrieve/clean → cite/retain provenance → reason`

This prevents "fast context injection" from becoming untraceable context pollution.

## Google Drive

The source proposes Rclone-mounted drives with conservative VFS buffers. A 32 MB buffer is explicitly recommended to avoid multiplying memory consumption when many files are open. fileciteturn69file11L478-L496

The project standardizes this as a profile rather than a hard-coded universal value:

- `low-memory`: 16–32 MB;
- `balanced`: 32–64 MB;
- `high-memory`: 64–128 MB.

The correct profile must be benchmarked against the number and size of concurrently opened files.

## Unity / Unreal

The corpus describes Unity MCP and Unreal Python-based MCP integrations for editing scenes, creating objects, importing assets and executing automation. fileciteturn68file4L172-L205

The production design wraps those capabilities with a project-state layer and verification stage:

`intent → plan → tool calls → project diff → compile/static validation → optional preview → commit`

This is substantially safer than giving the model an unconstrained shell.

## Benchmark plan

The benchmark matrix should record:

- prompt length;
- context length;
- GPU layer count;
- KV-cache quantization;
- RAM usage;
- VRAM peak;
- tokens/sec;
- first-token latency;
- tool-call latency;
- verification failure rate;
- successful task completion rate.

Every benchmark should be repeatable and stored as a machine-readable artifact.
