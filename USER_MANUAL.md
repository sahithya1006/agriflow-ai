# User Manual

## Overview

agriflow-ai is an offline Streamlit application for crop disease support, fertilizer guidance, OCR-assisted bill reading, and local prediction history.

## Start the application

1. Install the project dependencies from `requirements.txt`.
2. Run `streamlit run app.py`.
3. Open the local Streamlit URL shown in the terminal.

## Navigate the app

Use the sidebar to move between pages:

- Home: view the app overview and available modules.
- Ask Question: classify farming questions and route them to the right topic.
- Upload Image: upload an image for OCR or crop-related analysis.
- Dashboard: review locally saved prediction history.
- Reports: export prediction records as JSON or CSV.

## Make a disease prediction

1. Open the disease or question workflow from the sidebar.
2. Enter the crop, visible symptom, season, and soil type when prompted.
3. Review the predicted disease, severity, confidence, and recommendation.
4. Save or export the result if needed.

## Work offline

The app is designed to run without internet after dependencies are installed. Prediction history is stored in `agriflow.db` on the same machine.

## Data privacy

Uploaded images, generated predictions, and exported reports remain on the local machine unless the user manually shares them. Do not enter private credentials or personal secrets into the app.

## Troubleshooting

- If Streamlit does not start, confirm Python and dependencies are installed.
- If OCR does not work, confirm Tesseract OCR is installed and available on the system path.
- If predictions fail, delete only local generated model artifacts after backing up any needed data, then restart the app so models can be rebuilt.
