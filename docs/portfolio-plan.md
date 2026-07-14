# Portfolio Plan

ResearchMemoryKit is best presented as a research-engineering portfolio project.

## Positioning

Short version:

> A Markdown-based memory continuity kit for long-running AI-assisted research projects.

Resume version:

> Designed and open-sourced ResearchMemoryKit, a lightweight file-based memory system for AI-assisted research workflows, with Current State snapshots, append-only decision logs, failed-attempt records, pitfall catalogs, and completion gates to preserve experiment continuity across sessions.

## What It Demonstrates

- long-horizon research engineering;
- ability to turn repeated workflow failures into system design;
- disciplined provenance and evidence-boundary thinking;
- practical AI-agent collaboration;
- template design, documentation, and public-facing abstraction;
- awareness of privacy and publication boundaries.

## Suggested GitHub Presentation

Pin the repository with a concise description:

> Markdown memory templates for long-running AI-assisted research projects.

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

- add a small CLI to initialize templates;
- add a linter for router truth duplication;
- add a stale-state checker;
- add a privacy scanner for public release;
- add optional indexes for large append-only files.
