# Continuous Integration

This repository ships with dependency-free validation scripts.

Run locally:

```bash
python -m pip install -e . --no-deps
python -m unittest discover -s tests -v
rmk check . --strict
rmk check examples/toy-research-project
rmk check examples/fictional-paper-project
python scripts/demo_gate.py
python scripts/validate_public_repo.py .
python scripts/init_memory.py minimal /tmp/rmk-minimal --force
python scripts/init_memory.py research-project /tmp/rmk-research --force
python scripts/init_memory.py delivery-project /tmp/rmk-delivery --force
```

The template tests intentionally expect a freshly copied Current State to fail
until its `YYYY-MM-DD` date is initialized.

## This repository's workflow

ResearchMemoryKit validates its package, examples, templates, public files, and
executable demo with:

```text
.github/workflows/validate.yml
```

That workflow is specific to this repository and should not be copied into an
adopting project.

## Minimal workflow for another project

A project that already has `rmk.json` only needs to install the checker and run
one command. Copy
[`docs/github-actions/rmk-check.yml`](github-actions/rmk-check.yml) to
`.github/workflows/rmk-check.yml` in that project.

The reusable workflow is intentionally small:

```yaml
name: ResearchMemoryKit

on:
  push:
  pull_request:

permissions:
  contents: read

jobs:
  rmk-check:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v6

      - name: Set up Python
        uses: actions/setup-python@v6
        with:
          python-version: "3.11"

      - name: Install ResearchMemoryKit
        run: python -m pip install "researchmemorykit @ git+https://github.com/qzSOS/ResearchMemoryKit.git@v0.2.0"

      - name: Check project memory contract
        run: rmk check . --strict
```

The Git reference is pinned to a release tag. Update it deliberately when a
new ResearchMemoryKit release is available.
