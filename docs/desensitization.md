# Public-Release Desensitization Checklist

Use this checklist before publishing a memory layer, case study, or example derived from a real project.

## Remove

- real project names before publication;
- collaborator, advisor, lab, client, patient, or hospital identifiers;
- private server names, usernames, IP addresses, ports, and paths;
- unpublished paper titles, claims, exact numbers, and internal experiment IDs;
- dataset splits or institution-specific dataset details that are not already public;
- credentials, tokens, API keys, model cache paths, and private mirrors;
- generated outputs that include private content;
- screenshots that reveal local paths, usernames, or private file names.

## Generalize

| Private detail | Public replacement |
|---|---|
| Real project name | Project A, Project B, research-paper project |
| Real server path | remote GPU server |
| Real collaborator | human reviewer, domain expert |
| Exact unpublished metric | improved / failed / passed gate |
| Client deliverable | engineering delivery artifact |
| Dataset-specific sequence | development sequence, held-out sequence |

## Keep

- file structure patterns;
- update rules;
- failure mode names;
- abstract evidence type;
- public-safe lessons;
- fictional or toy examples.

## Author Attribution

Desensitizing a source project is different from anonymizing the public
repository author.

For a personal open-source project, an intentionally public author identity
may appear in `README.md`, `LICENSE`, `CITATION.cff`, package metadata, and the
GitHub profile. Do not copy that identity into fictional examples, templates,
case studies, or project-memory records unless it is required for attribution.

If the maintainer wants a pseudonymous repository, replace author identity in
all metadata before the first public release and verify the Git history and
release artifacts as well as the current tree.

## Final Checks

- Search the repository for local drive letters, usernames, server aliases, emails, phone numbers, and private names.
- Search for exact unpublished metrics copied from private reports.
- Review author identity in license, citation, and package metadata as an explicit publication decision.
- Read every case study as if it were shown to a reviewer, employer, collaborator, and client.
- If a detail only adds drama but not reusable value, remove it.
