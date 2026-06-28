# Feature Specification: Offline Crop Guidance

## User Need

Field users need crop disease and fertilizer guidance without relying on network connectivity.

## Scope

### In Scope

- Enter crop context such as crop, symptom, season, and soil type.
- Return a local prediction and recommendation.
- Store prediction history in SQLite.

### Out of Scope

- Cloud synchronization.
- Remote model inference.

## Functional Requirements

- [x] The app starts locally through Streamlit.
- [x] The disease model can train from local CSV data if the serialized model is missing.
- [x] Predictions can be saved to the local database.
- [x] Reports can be exported from local history.

## Acceptance Criteria

- [x] `python -m pytest` passes.
- [x] The app can run with Wi-Fi disabled after dependencies are installed.

## Data and Privacy

User-entered crop context and prediction results are stored in `agriflow.db` on the local machine.

## Risks

Model quality depends on the size and representativeness of local datasets.
