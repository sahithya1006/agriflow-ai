# Contributing

## Setup
```bash
git clone <repo-url>
cd agriflow-ai
pip install -r requirements.txt
pre-commit install
```

## Commit style
Use semantic commits:
- feat: new feature
- fix: bug fix
- docs: documentation
- test: adding tests
- chore: cleanup

## Branches
- main — stable only
- feature/your-feature — all development

## Before pushing
- Run ruff check .
- Run pytest tests/
- All CI checks must pass