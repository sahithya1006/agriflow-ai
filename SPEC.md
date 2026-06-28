# agriflow-ai — Technical Specification

## 1. Project Overview

**Project Name:** agriflow-ai
**Theme:** CPU-First Hackathon — Build AI that runs anywhere
**License:** GNU General Public License v3.0

AgriFlow AI is an offline-first, CPU-only AI web application that helps
farmers identify crop diseases, get fertilizer recommendations, and manage
farm records — all without any internet connection.

---

## 2. Problem Statement

Farmers in rural India face three critical problems:

1. They cannot identify crop diseases quickly enough to save their crops
2. They have no access to agronomists or farming experts nearby
3. They have no reliable internet to search for solutions online

By the time a farmer gets expert advice, the disease has already spread
and the crop is lost. This causes massive financial loss for small farmers
who cannot afford it.

---

## 3. Solution

agriflow-ai runs completely offline on a basic laptop or computer.
The farmer opens the app in a browser, types their symptoms or uploads
a photo, and gets an instant AI-powered diagnosis with treatment advice.

No internet. No cloud. No GPU. Just a CPU and the app.

---

## 4. Core Features

| Feature | Description |
|---|---|
| Disease Prediction | Predicts crop disease from symptoms using Random Forest |
| Fertilizer Recommendation | Recommends fertilizer based on crop, soil, and symptoms |
| Question Classifier | Routes farmer questions to the right AI model |
| OCR Bill Scanner | Extracts text from fertilizer bill photos |
| Structured JSON Output | All results returned as validated Pydantic JSON |
| Local History | All predictions saved to SQLite database |
| Report Export | Download predictions as JSON or CSV |
| Fully Offline | Works with Wi-Fi completely turned off |

---

## 5. Input Types

| Input | How | Example |
|---|---|---|
| Text | Farmer types symptoms or question | My tomato leaves have brown spots |
| Image | Farmer uploads crop photo or bill | JPG or PNG of infected leaf |
| PDF | Farmer uploads a document | Fertilizer bill or soil report |

---

## 6. Output Format

Every prediction returns a structured JSON validated by Pydantic:

```json
{
  "crop": "Tomato",
  "disease": "Early Blight",
  "severity": "High",
  "recommendation": "Apply Copper Fungicide at 2g per litre every 7 days",
  "confidence": 0.87,
  "input_type": "text",
  "timestamp": "2026-06-28T09:00:00"
}
```

---

## 7. AI Models

| Model | Algorithm | Library | Input | Output |
|---|---|---|---|---|
| Disease Predictor | Random Forest | scikit-learn | crop + symptoms | disease name + confidence |
| Fertilizer Recommender | Random Forest | scikit-learn | crop + soil + disease | fertilizer + dosage |
| Text Classifier | Random Forest | scikit-learn | question text | category label |
| OCR Engine | Tesseract 5 | pytesseract | image file | extracted text |

### Why Random Forest?
- Runs entirely on CPU — no GPU needed
- Fast inference — results in under 1 second
- Works well with small agricultural datasets
- Models saved as .pkl files using joblib — fully offline
- No internet required at any point

### Text Classifier Categories
- disease — question about a crop disease
- fertilizer — question about fertilizers or nutrients
- irrigation — question about watering schedule
- pest — question about insects or pests
- government_scheme — question about subsidies or schemes

---

## 8. Tech Stack

| Layer | Technology | Version |
|---|---|---|
| Language | Python | 3.11 |
| UI | Streamlit | Latest |
| ML Models | scikit-learn | Latest |
| Model Storage | joblib | Latest |
| OCR | Tesseract + pytesseract | 5.x |
| Data Validation | Pydantic | v2 |
| Database | SQLite | Built-in |
| Data Processing | pandas | Latest |
| Image Handling | Pillow | Latest |

---

## 9. System Architecture


---

## 10. Data Flow


---

## 11. Pages

| Page | File | Description |
|---|---|---|
| Home | ui/home.py | Overview, instructions, quick stats |
| Ask a Question | ui/ask.py | Type symptoms, get diagnosis |
| Upload Image | ui/upload.py | Upload crop photo or bill for OCR |
| Dashboard | ui/dashboard.py | View all past predictions and charts |
| Reports | ui/reports.py | Download data as JSON or CSV |

---

## 12. Database Schema

### Table: predictions
| Column | Type | Description |
|---|---|---|
| id | INTEGER | Primary key, auto increment |
| input_type | TEXT | text or image |
| crop | TEXT | Crop name |
| disease | TEXT | Predicted disease |
| severity | TEXT | Low, Medium, High |
| recommendation | TEXT | Treatment advice |
| confidence | REAL | Model confidence 0 to 1 |
| raw_json | TEXT | Full JSON output |
| created_at | TIMESTAMP | Auto timestamp |

### Table: farmers
| Column | Type | Description |
|---|---|---|
| id | INTEGER | Primary key |
| name | TEXT | Farmer name |
| village | TEXT | Village or district |
| crop | TEXT | Primary crop |
| created_at | TIMESTAMP | Auto timestamp |

### Table: history
| Column | Type | Description |
|---|---|---|
| id | INTEGER | Primary key |
| action | TEXT | What the user did |
| details | TEXT | Extra details |
| created_at | TIMESTAMP | Auto timestamp |

### Table: reports
| Column | Type | Description |
|---|---|---|
| id | INTEGER | Primary key |
| prediction_id | INTEGER | Links to predictions table |
| report_type | TEXT | json or csv |
| created_at | TIMESTAMP | Auto timestamp |

---

## 13. Folder Structure

---

## 14. Offline Requirement

- All ML models saved as .pkl files using joblib
- No API calls at any point in the code
- No external URLs or cloud services used
- SQLite used for all data storage
- Tesseract OCR runs locally on CPU
- App runs on localhost:8501 via Streamlit
- Demo will be shown with Wi-Fi turned OFF

---

## 15. CPU Requirement

- No GPU or CUDA used anywhere
- scikit-learn Random Forest runs on CPU by default
- Tesseract OCR runs on CPU
- Models are lightweight — inference under 1 second on any laptop
- No deep learning frameworks used — no PyTorch, no TensorFlow

---

## 16. Datasets

| Model | Dataset | Source |
|---|---|---|
| Disease Predictor | Crop Disease Dataset | Kaggle |
| Fertilizer Recommender | Fertilizer Prediction Dataset | Kaggle |
| Text Classifier | Custom labeled questions | Created by team |

---

## 17. Example Predictions

### Disease prediction from text

### Fertilizer recommendation

### OCR from bill image

### OCR from bill image

---

## 18. Evaluation Criteria Mapping

| Criterion | How AgriFlow AI satisfies it |
|---|---|
| CPU-first | Random Forest + Tesseract — no GPU anywhere |
| Offline-first | Works with Wi-Fi off — demo will prove this |
| Unstructured to structured | Text and image input to validated Pydantic JSON |
| Open source | GPL-3.0 license in repo |
| Working demo | Streamlit app running on localhost |
| Real problem | Crop disease kills farmer income across India |