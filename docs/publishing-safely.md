# Publishing a project memory layer safely

This guide is for projects that use ResearchMemoryKit privately and later
publish the repository, a template, or a case study. It is not a rule that
private research records must omit every operational detail.

## Private project use

A working research project may need machine names, storage roots, output
paths, dataset roles, and unpublished results. Preserve the facts needed to
resume and reproduce the work.

Use these boundaries:

- `rmk.json` contract paths are always repository-relative.
- Operational records may contain exact paths when the project is private and
  the path is needed for recovery.
- For shared or portable projects, prefer an environment role such as
  `gpu-server-a` plus a path key such as `experiment_root`. Keep each machine's
  concrete mapping in a gitignored local file.
- Never store passwords, access tokens, private keys, or other credentials in
  project memory. Use environment variables or a secret manager.

Add `*.local.md` to the target project's `.gitignore` before creating files
such as `memory/ENVIRONMENT.local.md`. This repository already uses that
pattern, but initialized templates do not overwrite an existing `.gitignore`.

## Before publishing

Review the current tree, Git history, release tags, generated artifacts, and
screenshots. Remove or generalize:

- non-public project, paper, client, institution, patient, or collaborator
  names;
- unpublished claims, exact metrics, dataset splits, and internal experiment
  identifiers;
- usernames, IP addresses, ports, server aliases, cache roots, and local
  filesystem paths;
- credentials, private mirrors, and signed download links;
- images, logs, or reports that reveal any of the above.

Useful public replacements include:

| Private record | Public replacement |
|---|---|
| Exact server path | named environment role |
| Real project name | fictional project description |
| Exact unpublished metric | synthetic value or qualitative gate result |
| Collaborator identity | reviewer role |
| Dataset-specific sequence | synthetic development or held-out input |

Do not call a heavily generalized description a real case study. Label it as a
fictional example or a design pattern unless readers can inspect enough
evidence to evaluate the claim.

## Author attribution

Publishing a repository under a real name is separate from publishing private
project details. A maintainer may intentionally use a public identity in the
README, license, citation file, and package metadata.

If the repository should be pseudonymous, make that decision before the first
public release. Removing a name from the latest commit does not remove it from
Git history or old release artifacts.

## Release check

Run:

```bash
rmk check . --strict
python scripts/validate_public_repo.py .
```

The scanner catches common path, email, and secret patterns. It cannot decide
whether a project name, result, or image is confidential, so a human review is
still required.
