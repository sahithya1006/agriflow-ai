# AgriFlow-AI Specification

## Problem Statement
Farmers need offline support for crop disease detection, fertilizer recommendation, irrigation guidance, and agricultural document understanding.

## Goal
Convert unstructured agricultural input into structured JSON using CPU-only machine learning.

## Inputs
- Text
- Crop Image
- Voice Text
- PDF / Fertilizer Bill

## ML Algorithms
- Random Forest for disease prediction
- Decision Tree for fertilizer recommendation
- TF-IDF + Logistic Regression for text classification
- Tesseract OCR for document text extraction

## Output JSON
{
  "crop": "Tomato",
  "issue_type": "Disease",
  "prediction": "Early Blight",
  "severity": "High",
  "confidence": 0.94,
  "recommendation": "Apply Copper Fungicide"
}

## Offline-First
All processing works without internet.

## CPU-First
All ML models run on CPU using scikit-learn and Tesseract.