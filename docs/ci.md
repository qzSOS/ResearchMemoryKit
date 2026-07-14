# Continuous Integration

This repository ships with dependency-free validation scripts.

Run locally:

```bash
python scripts/validate_public_repo.py .
python scripts/init_memory.py minimal /tmp/rmk-minimal --force
python scripts/init_memory.py research-project /tmp/rmk-research --force
python scripts/init_memory.py delivery-project /tmp/rmk-delivery --force
```

## Optional GitHub Actions Workflow

The workflow template lives at:

```text
docs/github-actions/validate.yml
```

GitHub requires the `workflow` token scope to push files under `.github/workflows/`. If your token does not have that scope, keep the template in `docs/github-actions/` until you refresh auth.

To enable Actions locally:

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
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Validate public repo
        run: python scripts/validate_public_repo.py .

      - name: Smoke-test template initialization
        run: |
          mkdir -p /tmp/rmk-minimal /tmp/rmk-research /tmp/rmk-delivery
          python scripts/init_memory.py minimal /tmp/rmk-minimal
          python scripts/init_memory.py research-project /tmp/rmk-research
          python scripts/init_memory.py delivery-project /tmp/rmk-delivery
```
