# Portfolio Plan

ResearchMemoryKit is best presented as a research-engineering portfolio project.

## Positioning

Short version:

> A gated memory layer for trustworthy AI-assisted research workflows.

Resume version:

> Designed and open-sourced ResearchMemoryKit, a dependency-free gated memory layer for AI-assisted research workflows, with explicit project contracts, Current State snapshots, append-only research records, completion gates, and a CI-ready `rmk check` validator.

## What It Demonstrates

- long-horizon research engineering;
- ability to turn repeated workflow failures into system design;
- disciplined provenance and evidence-boundary thinking;
- practical AI-agent collaboration;
- dependency-free Python CLI and contract validation;
- template design, documentation, and public-facing abstraction;
- awareness of privacy and publication boundaries.

## Suggested GitHub Presentation

Pin the repository with a concise description:

> A gated memory layer for trustworthy AI-assisted research workflows.

Topics:

```text
ai-agents
research-tools
markdown
workflow
experiment-management
knowledge-management
research-engineering
```

## Blog Post Ideas

1. **Why AI Research Agents Need a Current State File**
   - Problem: chat history is not project memory.
   - Core pattern: short overwriteable state plus append-only records.

2. **Append-Only Is Not Enough**
   - Problem: permanent records and evolving presentation have different needs.
   - Pattern: conclusions append-only, presentation reformattable.

3. **The Completion Gate That Made Agents Remember**
   - Problem: templates are ignored unless maintenance is part of done.
   - Pattern: task is not complete until memory is updated.

4. **How to Publish a Private Research Workflow Without Leaking the Research**
   - Problem: portfolio value versus unpublished work.
   - Pattern: publish structure, not sensitive content.

## Interview Talking Points

- "I found that agent memory was less about storing everything and more about maintaining a credible current state."
- "The main failure mode was not forgetting; it was drift between multiple copies of the same fact."
- "I use append-only records for provenance, but an overwriteable current snapshot for fast recovery."
- "The system is intentionally not a database. It is a low-friction layer that works before a project deserves heavier infrastructure."

## Future Work

- add registry lifecycle and experiment reference checks;
- add git-aware append-only deletion detection;
- add claim evidence and human-review status;
- add conservative router truth-duplication checks;
- add optional indexes for large append-only files.
