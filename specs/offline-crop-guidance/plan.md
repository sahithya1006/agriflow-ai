# Implementation Plan: Offline Crop Guidance

## Summary

Keep inference, history storage, and reporting local so installed users can run the Streamlit app without network access.

## Files Expected to Change

- `ai/`
- `database/`
- `ui/`
- `tests/`
- `README.md`
- `USER_MANUAL.md`

## Test Plan

- Run `python -m pytest`.
- Run `python -m pytest --cov=ai --cov=database`.
- Manually start the Streamlit app and verify prediction and report workflows with Wi-Fi disabled.

## Rollback Plan

Revert the feature changes and restore the prior local database schema if a migration was introduced.
