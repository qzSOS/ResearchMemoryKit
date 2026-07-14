# Case Study: Creative Pipeline Project

This anonymized case study describes a creative AI production pipeline involving prompts, generated assets, model training, and a playable prototype.

No private story, character, asset, server, model-output, or unpublished production detail is included.

## Starting Problem

The project had to preserve context across:

- prompt iterations;
- character asset definitions;
- model-training preparation;
- local preview and remote rendering;
- generated asset metadata;
- prototype assembly.

The main risk was not a single failed experiment. It was asset and prompt drift.

## Memory Design

The project started with:

- a router file;
- an overwriteable Current State;
- an append-only activity log;
- a theory/principles file;
- conventions for naming and metadata;
- environment records for local/remote roles.

## What Worked

The Day-0 memory layer helped the project reach an early closed loop: prompt design, asset generation, model training, asset cleanup, and prototype integration could be recovered from files instead of chat history.

## What Degraded

Later migration and infrastructure work was not fully reflected back into the main state/log chain. The project also had weak git hygiene: many important files existed locally but were not tracked.

## Transferable Lesson

Creative pipelines need memory just as much as scientific experiments. But asset-heavy projects require an explicit output and git boundary from the start.

Recommended addition:

> Every generated asset should be classified as accepted, diagnostic, archived, or external before the session ends.
