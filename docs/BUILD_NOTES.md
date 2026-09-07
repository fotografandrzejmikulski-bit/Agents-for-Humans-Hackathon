# Build Notes

## Source baseline

The starting material described CogniSync as a background multi-agent system using Strands Agents, Amazon Bedrock AgentCore Runtime, AgentCore Memory, MCP/Gateway, A2A and Human-in-the-Loop. It also proposed a Python prototype with memory/session management and a CLI-oriented deployment path. The concept is retained, but the implementation is made more conservative and reproducible.

## Improvements made

### 1. Replaced speculative claims with explicit architecture boundaries

The repository does not claim that an AWS resource exists merely because code is prepared for it. Cloud deployment remains an explicit next step.

### 2. Made autonomy a first-class policy

The policy engine is independent from the model. Low-risk work is autonomous; high-risk and unknown actions fail closed.

### 3. Added a deterministic local mode

Judges can execute the core without AWS credentials. This lowers the barrier to verification and makes safety behavior testable.

### 4. Added evidence and auditability

Insights carry source references and confidence. Runs and decision gates are logged in JSONL.

### 5. Added explicit threat model

Prompt injection, privilege, credential exposure, hallucinated completion, context poisoning and runaway execution are treated as system design concerns rather than prompt-only concerns.

### 6. Updated security framing

Current Strands Shell documentation distinguishes an in-process mediation layer from hardened OS isolation. Production isolation should therefore be attributed to the appropriate runtime boundary rather than overstated. citeturn916868search1turn916868search6

### 7. Updated AWS architecture references

Current AWS documentation supports AgentCore Runtime as a framework-agnostic execution environment, AgentCore Gateway as an MCP integration boundary, AgentCore Memory built-in strategies, and A2A server deployment with Agent Cards and JSON-RPC. citeturn888617search8turn493810search2turn493810search4turn888617search0

## Important implementation note

The exact production APIs and CLI parameters should be pinned and validated in the deployment environment before a cloud rollout. The repository intentionally avoids encoding unverified legacy snippets as if they were guaranteed current interfaces.
