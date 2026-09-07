# Project 03 — Open Creator Layer

## Vision

Build a Buildbox-class authoring experience without building a new renderer or physics engine. The source corpus proposes an **Engine-on-Engine** abstraction layer over Unity and Unreal, preserving native engine power while replacing complexity with an intuitive creator workflow. fileciteturn66file1L50-L69

## Product primitives

### 1. Mind Map

The game project is represented as a directed graph of worlds/scenes and transitions. The source identifies this as a central part of the Buildbox experience. fileciteturn66file7L310-L330

### 2. Typed Visual Logic

Nodes expose typed ports. Invalid connections are prevented at authoring time. Blackboard-style global variables are persisted as project data. Runtime execution is event-driven rather than driven by per-frame polling. fileciteturn66file11L480-L492

### 3. Smart Assets

Importing an asset triggers heuristics: texture type, sprite processing, collider creation, prefab generation and atlas inclusion. The source specifically proposes `AssetPostprocessor` automation and platform-aware compression. fileciteturn66file11L493-L513

### 4. One-click monetization

Advertising and related monetization should appear as explicit graph nodes rather than forcing developers to hand-edit manifests and Gradle configuration. fileciteturn66file5L227-L234

## Stronger architecture

```text
Creator Intent
     ↓
Visual Project Model
     ↓
Typed Graph + Blackboard
     ↓
Compiler / Validator
     ↓
Unity or Unreal Native Representation
     ↓
Build / Test / Package
```

The key architectural decision is to keep the **source of truth engine-independent** while providing native adapters for Unity and Unreal. This protects against lock-in and allows the same project model to target different execution environments.

## AI-native layer

An optional local/remote coding agent can operate above the authoring model. It should never edit the project blindly. Its lifecycle is:

`request → plan → graph/code patch → static validation → engine validation → preview → user approval → commit`

The source corpus proposes a neuro-symbolic verification loop using syntax parsing, linting and forbidden-operation checks before generated code is accepted. fileciteturn68file8L358-L375

## MVP roadmap

**Phase 1:** Unity EditorWindow + UX shell and Unreal Editor Utility Widget shell.

**Phase 2:** typed visual graph, serialization, compiler/runtime runner.

**Phase 3:** Smart Assets and project-wide import automation.

**Phase 4:** AI-assisted authoring, validation and packaging.

**Phase 5:** monetization, templates and creator marketplace.

The source roadmap proposes a similar progression, beginning with UI foundations, then visual scripting, Smart Assets and finally monetization/build automation. fileciteturn65file9L437-L459

## Business model hypothesis

The supplied corpus proposes a lower-friction alternative to subscription-heavy creator tooling, including perpetual licensing and freemium/template-based models. This remains a market hypothesis and should be validated with actual willingness-to-pay research before commercialization. fileciteturn66file5L235-L255

## Success metrics

- time from empty project to playable prototype;
- number of manual setup operations eliminated;
- invalid graph connection rate;
- asset-import automation success rate;
- compile/validation pass rate;
- native-engine compatibility rate;
- creator retention and project completion rate.
