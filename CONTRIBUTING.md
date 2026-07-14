# Contributing

Thanks for considering a contribution.

ResearchMemoryKit is intentionally small. Contributions should preserve that constraint.

## Good Contributions

- clearer templates;
- stronger completion gates;
- better privacy checks;
- sanitized examples;
- documentation improvements;
- small dependency-free scripts.

## Avoid

- database services;
- agent runtimes;
- dashboards;
- heavy dependencies;
- private or non-anonymized case studies;
- templates that require a specific commercial tool.

## Development Checks

Run:

```bash
python scripts/validate_public_repo.py .
python scripts/init_memory.py minimal /tmp/rmk-minimal --force
python scripts/init_memory.py research-project /tmp/rmk-research --force
python scripts/init_memory.py delivery-project /tmp/rmk-delivery --force
```

## Privacy

Do not submit real project names, unpublished metrics, server paths, collaborator names, client information, dataset-private details, credentials, or screenshots that reveal local paths.

Use [docs/desensitization.md](docs/desensitization.md) before opening a pull request.
