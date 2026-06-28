# AGENTS.md

## Project Guidance

This repository contains a small offline Python and Streamlit application. Keep changes focused, readable, and compatible with local CPU-only execution.

## Development Commands

```bash
python -m pip install -r requirements.txt
python -m ruff check .
python -m ruff format .
python -m mypy ai database ui --ignore-missing-imports
python -m bandit -r ai database ui app.py -ll
python -m pytest
```

## Coding Standards

- Prefer simple Python modules over framework-heavy abstractions.
- Keep runtime behavior offline-first.
- Do not commit generated local databases, secrets, virtual environments, caches, or large private datasets.
- Add or update tests when behavior changes.
- Keep user-facing documentation current when workflows change.

## CI Expectations

Merge requests should pass linting, formatting, type checking, security scanning, dependency audit, and tests with coverage reporting.
