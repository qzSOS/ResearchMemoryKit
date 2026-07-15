# Comparison

ResearchMemoryKit sits between informal notes and heavier infrastructure.

## Compared With Agent Memory Databases

Agent memory databases focus on retrieval: storing memories, searching them, and injecting them into future prompts.

ResearchMemoryKit focuses on project continuity:

- What is the current state?
- Why did we choose this route?
- Which failures should not be repeated?
- What evidence supports the current claim?
- What must be updated before a task is done?

It is intentionally file-based and git-native. There is no server, database, vector store, or hidden memory layer.

The explicit `rmk.json` contract and `rmk check` validate project structure,
router reachability, declared gate headings, and Current State health without
adding retrieval infrastructure. P0 does not judge evidence quality or claim
truth.

## Compared With Experiment Trackers

Experiment trackers are strong when a project needs dashboards, metrics, artifact storage, and run comparison.

ResearchMemoryKit does not replace them. It captures information that trackers often miss:

- direction decisions;
- failed-route rationale;
- environment pitfalls;
- evidence boundaries;
- current-state recovery;
- human-agent handoff notes.

The registry template stores metadata only. Large artifacts stay outside git or in a dedicated artifact system.

## Compared With Project Management Tools

Project management tools track tasks. Research projects often need something different: a way to preserve uncertainty, negative evidence, and changing interpretations.

ResearchMemoryKit treats failed attempts and stop conditions as first-class records.

## Compared With Notes Apps

Notes apps are flexible, but flexibility creates drift when agents and humans return weeks later.

ResearchMemoryKit adds lifecycle semantics:

- overwriteable current state;
- append-only decisions;
- append-only failures;
- conclusion-preserving experiment logs;
- completion gates.

## When To Combine Tools

Use ResearchMemoryKit with:

- MLflow, Weights & Biases, TensorBoard, or custom registries for numeric run tracking;
- GitHub Issues for public task tracking;
- Zotero or bibliography managers for citation libraries;
- cloud storage for large outputs.

ResearchMemoryKit should remain the small, readable continuity layer that explains how these pieces fit together.
