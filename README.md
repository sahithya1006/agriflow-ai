<<<<<<< HEAD
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
=======
# 🌾 AgriFlow AI

> Offline-first AI assistant for farmers. Runs entirely on CPU. No internet required.

## 🔗 Live Demo
**https://agriflow-ai-mw4aed7fvjjfh2qppkoymm.streamlit.app**

> For voice input — open in **Chrome browser**

---

## 🌱 Problem Statement

Farmers in rural India face three critical problems:

1. They cannot identify crop diseases quickly enough to save their crops
2. They have no access to agronomists or farming experts nearby
3. They have no reliable internet to search for solutions online

By the time a farmer gets expert advice, the disease has already spread
and the crop is lost. This causes massive financial loss for small farmers
who cannot afford it.

---

## 💡 Solution

AgriFlow AI lets farmers type or speak their symptoms and get instant
AI-powered disease diagnosis and fertilizer recommendations.

- No internet needed
- No GPU needed
- Runs on any basic laptop or computer
- Supports Telugu, Hindi, Tamil, English

---

## ✨ Features

- 🔬 Crop disease prediction using Random Forest
- 💊 Fertilizer recommendation based on crop and soil
- 🧾 OCR to read fertilizer bills
- ❓ Question classifier (disease / fertilizer / irrigation / pest / scheme)
- 🎙️ Voice input in Telugu, Hindi, Tamil, English
- 📊 Local history dashboard
- 📄 Export reports as JSON and CSV
- 💾 All data saved locally in SQLite

---

## 🤖 AI Models

| Model | Algorithm | Runtime | Purpose |
|---|---|---|---|
| Disease Predictor | Random Forest | scikit-learn CPU | Predict disease from symptoms |
| Fertilizer Recommender | Random Forest | scikit-learn CPU | Recommend fertilizer |
| Text Classifier | Random Forest | scikit-learn CPU | Route question to right model |
| OCR Engine | Tesseract 5 | pytesseract | Extract text from bill images |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11 |
| UI | Streamlit |
| ML Models | scikit-learn |
| Model Storage | joblib |
| OCR | Tesseract + pytesseract |
| Data Validation | Pydantic |
| Database | SQLite |
| Data Processing | pandas |
| Image Handling | Pillow |

---

## 🚀 How to Run Locally (Fully Offline)

```bash
# Clone the repo
git clone https://code.swecha.org/jashwitha_210/agriflow-ai.git
cd agriflow-ai

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

Open in browser:

---

## 📋 Pages

| Page | Description |
|---|---|
| 🏠 Home | Overview and instructions |
| ❓ Ask a Question | Type or speak symptoms, get diagnosis |
| 📷 Upload Image | Upload crop photo or bill for OCR |
| 📊 Dashboard | View all past predictions and charts |
| 📄 Reports | Download data as JSON or CSV |

---

## 🔒 Offline Demo

This app works with WiFi completely turned off:

- All ML models run on CPU using scikit-learn
- No API calls at any point
- SQLite used for all local data storage
- Tesseract OCR runs locally
- Voice input uses browser built-in speech recognition

---

## 👩‍💻 Team — Campus Connect

| Member | Role |
|---|---|
| Jashwitha | AI and ML models, OCR, JSON generator, tests |
| Sahithya | Streamlit UI, SQLite database, CI/CD, deployment |

---

## 📜 License

This project is licensed under the **GNU General Public License v3.0**

See the [LICENSE](LICENSE) file for details.
>>>>>>> origin/main
