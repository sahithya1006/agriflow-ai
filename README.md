# agriflow-ai🌾

An offline-first AI assistant for farmers. Runs entirely on CPU. No internet required.

## Problem
Farmers in rural areas have no access to agronomists or reliable internet.
They lose crops to diseases they cannot identify in time.

## Solution
agriflow-ai AI lets farmers type their symptoms or upload a photo.
The app predicts the disease, recommends fertilizer, and saves everything locally.

## Features
- 🔬 Crop disease prediction using Random Forest
- 💊 Fertilizer recommendation based on crop and soil
- 🧾 OCR to read fertilizer bills
- ❓ Question classifier (disease / fertilizer / irrigation / pest / scheme)
- 📊 Local history dashboard
- 📄 Export reports as JSON and CSV

## Tech Stack
- ML: scikit-learn (Random Forest), Tesseract OCR
- UI: Streamlit
- Database: SQLite
- Runtime: CPU only — no GPU, no cloud
- Offline: works with Wi-Fi completely off

## How to run
```bash
git clone <https://code.swecha.org/jashwitha_210/agriflow-ai.git>
cd agriflow-ai
pip install -r requirements.txt
streamlit run app.py
```

## Team
- Member 1 — AI & ML models
- Member 2 — UI, database, CI/CD