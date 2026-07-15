# Continuous Integration

This repository ships with dependency-free validation scripts.

Run locally:

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

The template tests intentionally expect a freshly copied Current State to fail
until its `YYYY-MM-DD` date is initialized.

## GitHub Actions Workflow

The active workflow lives at:

```text
.github/workflows/validate.yml
```

A synchronized copy is kept at `docs/github-actions/validate.yml` for projects
that want to adopt the workflow.

GitHub requires the `workflow` token scope to push files under
`.github/workflows/`. To install the synchronized copy in another checkout:

```bash
gh auth refresh -s workflow
python scripts/enable_github_actions.py
git add .github/workflows/validate.yml
git commit -m "Enable validation workflow"
git push
```

The template content is:

```yaml
name: Validate

on:
  push:
  pull_request:

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v6

      - name: Set up Python
        uses: actions/setup-python@v6
        with:
          python-version: "3.11"

      - name: Install ResearchMemoryKit
        run: python -m pip install -e . --no-deps

      - name: Run unit tests
        run: python -m unittest discover -s tests -v

      - name: Validate self-hosted contract
        run: rmk check . --strict

      - name: Validate bundled examples
        run: |
          rmk check examples/toy-research-project
          rmk check examples/fictional-paper-project

      - name: Validate public repo
        run: python scripts/validate_public_repo.py .

      - name: Smoke-test template initialization
        run: |
          mkdir -p /tmp/rmk-minimal /tmp/rmk-research /tmp/rmk-delivery
          python scripts/init_memory.py minimal /tmp/rmk-minimal
          python scripts/init_memory.py research-project /tmp/rmk-research
          python scripts/init_memory.py delivery-project /tmp/rmk-delivery
```
