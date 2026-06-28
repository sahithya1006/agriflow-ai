# Tasks: [Feature Name]

## Setup

- [ ] Review the accepted feature specification.
- [ ] Confirm local datasets, models, and database behavior needed for the feature.

## Implementation

- [ ] Update application code.
- [ ] Update local data or schema code if required.
- [ ] Update user-facing documentation if workflows change.

## Verification

- [ ] Run `python -m ruff check .`
- [ ] Run `python -m ruff format --check .`
- [ ] Run `python -m mypy ai database ui --ignore-missing-imports`
- [ ] Run `python -m bandit -r ai database ui app.py -ll`
- [ ] Run `python -m pytest --cov=ai --cov=database`
