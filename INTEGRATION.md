# AgriFlow AI — ML Integration Guide

## Member 1 (ML) → Member 2 (UI) Connection

### Functions Connected

| Function | File | Connected In |
|---|---|---|
| predict_disease() | ai/disease_model.py | ui/ask.py, ui/upload.py |
| classify_query() | ai/text_classifier.py | ui/ask.py |
| extract_text() | ai/ocr.py | ui/upload.py |

### ui/ask.py
`python
from ai.disease_model import predict_disease
from ai.text_classifier import classify_query
category = classify_query(symptoms)["category"]
result = predict_disease(crop=crop, symptom=symptoms, season="Kharif", soil_type="Red Soil")
`

### ui/upload.py
`python
from ai.ocr import extract_text
from ai.disease_model import predict_disease
ocr_text = extract_text(tmp_path)
result = predict_disease(crop="Tomato", symptom=ocr_text, season="Kharif", soil_type="Red Soil")
`

## Offline Checklist
- [x] ML models connected to UI
- [x] Database saving predictions
- [x] App runs with streamlit run app.py
- [x] No internet required
