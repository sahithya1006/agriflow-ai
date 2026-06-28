# AgriFlow AI Constitution

## Principles

### Offline-first operation

The application must continue to provide core user workflows without internet access after installation.

### Local data ownership

Prediction history, uploaded files, and generated reports should remain local by default.

### Small, testable changes

Feature changes should include focused tests and documentation updates when user workflows change.

### Accessible field use

Interfaces should be understandable for non-specialist users and usable on ordinary field laptops.

## Quality Gates

- Linting and formatting must pass.
- Tests must pass.
- Coverage reporting must run with an enforced threshold.
- Security and dependency scans should run in CI.

## Governance

Changes to this constitution require maintainers to update relevant templates and document the reason in `CHANGELOG.md`.
