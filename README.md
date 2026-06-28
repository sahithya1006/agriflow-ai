# agriflow-ai

Offline-first AI assistant for farmers. The app runs locally on CPU, stores data in SQLite, and avoids cloud dependencies so it can be used in low-connectivity field settings.

## Project status

- License: AGPL-3.0-or-later
- Stack: Python, Streamlit, SQLite, scikit-learn
- Runtime: CPU only
- Primary users: farmers, field volunteers, and agricultural support teams

## Problem

Farmers in rural areas often do not have reliable internet access or immediate access to agronomists. Crop disease symptoms, fertilizer choices, and local record keeping can be difficult to manage without a lightweight offline tool.

## Solution

agriflow-ai lets users enter crop symptoms, upload crop or bill images, receive disease and fertilizer guidance, and keep a local history of predictions. The project is intentionally small so it can run on ordinary laptops used by field teams.

## Features

- Crop disease prediction from crop, symptom, season, and soil type
- Fertilizer recommendation based on crop and soil inputs
- OCR support for reading fertilizer bills
- Farming question classification
- Local history dashboard backed by SQLite
- JSON and CSV report export

## Repository layout

```text
ai/          Machine-learning and OCR helpers
database/    SQLite initialization and query helpers
datasets/    Small local CSV datasets used by the models
models/      Serialized local model artifacts
tests/       Pytest test suite
ui/          Streamlit page modules
app.py       Streamlit application entry point
```

## Requirements

- Python 3.11 or newer
- Tesseract OCR installed locally if OCR features are used
- No GPU is required

## Setup

```bash
git clone https://code.swecha.org/jashwitha_210/agriflow-ai.git
cd agriflow-ai
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Run the app

```bash
streamlit run app.py
```

The app creates `agriflow.db` in the project root when it starts. This database is local runtime state and should not be committed.

## Quality checks

```bash
python -m ruff check .
python -m ruff format --check .
python -m mypy ai database ui --ignore-missing-imports
python -m bandit -r ai database ui app.py -ll
python -m pytest --cov=ai --cov=database --cov-report=term-missing --cov-fail-under=40
```

## Security

Do not commit secrets, private datasets, credentials, or production databases. Report vulnerabilities using the process in `SECURITY.md`.

## License

This project is licensed under the GNU Affero General Public License v3.0 or later. See `LICENSE` for details.
