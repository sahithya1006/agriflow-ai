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
