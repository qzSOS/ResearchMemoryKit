# Development Workflow

## Gate 1: Design

The design phase closes only when:

- [x] the public design document defines goals and non-goals;
- [x] the manifest contract is explicit;
- [x] P0 checks and severity behavior are frozen;
- [x] the repository memory layer records the decision and current state;
- [x] existing public validation still passes.

## Gate 2: Implementation

Implementation closes only when:

- [x] the dependency-free checker and CLI are implemented;
- [x] automated tests cover valid and invalid contracts;
- [x] text and JSON output are tested;
- [x] no implementation work depends on private projects or unpublished data;
- [x] the implementation commit updates project memory.

## Gate 3: Adoption

Adoption closes only when:

- [x] every bundled template includes a manifest;
- [x] examples pass `rmk check`;
- [x] this repository passes `rmk check --strict`;
- [x] README, adoption docs, and CI show the real command;
- [x] the adoption commit updates project memory.

## Gate 4: Release

Release closes only when:

- [x] unit tests and public-release validation pass;
- [x] sensitive-pattern and diff audits pass;
- [x] GitHub Actions passes on the release commit;
- [x] release metadata and documentation agree;
- [x] Current State records the released result and next route.

## Gate 5: Reader-facing demo

This phase closes only when:

- [x] README language separates private project use from public release rules;
- [x] current checker behavior is distinguished from future semantic checks;
- [x] an executable fictional demo fails on real P0 findings and then passes;
- [x] the README animation is generated from the executable demo transcript;
- [x] unverifiable anonymized case-study claims are removed or reframed;
- [x] tests, public validation, and package checks pass locally;
- [ ] GitHub Actions passes on the published changes;
- [ ] the repository memory records the closed gate and next route.
