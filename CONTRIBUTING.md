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
python -m pip install -e . --no-deps
python -m unittest discover -s tests -v
rmk check . --strict
rmk check examples/toy-research-project
rmk check examples/fictional-paper-project
python scripts/validate_public_repo.py .
python scripts/init_memory.py minimal /tmp/rmk-minimal --force
python scripts/init_memory.py research-project /tmp/rmk-research --force
python scripts/init_memory.py delivery-project /tmp/rmk-delivery --force
```

Before submitting Python changes, also run:

```bash
ruff check researchmemorykit scripts tests
ruff format --check researchmemorykit scripts tests
```

Ruff is a development tool only; ResearchMemoryKit has no third-party runtime
dependencies.

## Privacy

Do not submit real project names, unpublished metrics, server paths, collaborator names, client information, dataset-private details, credentials, or screenshots that reveal local paths.

Public maintainer attribution belongs only in repository-level pages and
metadata such as `README.md`, `LICENSE`, `CITATION.cff`, and package metadata.
Do not add personal identities to templates, examples, case studies, or
project-memory records.

Use [docs/desensitization.md](docs/desensitization.md) before opening a pull request.
