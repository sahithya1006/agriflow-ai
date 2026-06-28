import os
import tempfile
import json
from pathlib import Path

import streamlit as st
from database.db import save_prediction

st.title("📷 Upload Image")
st.caption("Upload a crop photo or fertilizer bill")

uploaded = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png", "pdf"])

if uploaded:
    if uploaded.type.startswith("image"):
        st.image(uploaded, caption="Uploaded image", use_container_width=True)

    with st.spinner("Running OCR and disease detection..."):
        from ai.ocr import extract_text
        from ai.disease_model import predict_disease

        # Save uploaded file to temp path so OCR can read it
        suffix = Path(uploaded.name).suffix
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(uploaded.read())
            tmp_path = tmp.name

        try:
            ocr_text = extract_text(tmp_path)
        except Exception:
            ocr_text = "spots"
        finally:
            os.unlink(tmp_path)

        result = predict_disease(
            crop="Tomato",
            symptom=ocr_text if ocr_text else "spots",
            season="Kharif",
            soil_type="Red Soil",
        )

    st.markdown("### Result")
    col1, col2 = st.columns(2)
    col1.metric("Disease", result["disease"])
    col2.metric("Confidence", f"{result['confidence'] * 100:.0f}%")
    st.error(f"Severity: {result['severity']}")
    st.success(f"Recommendation: {result['recommendation']}")
    st.json(result)

    if st.button("💾 Save to history"):
        save_prediction(
            input_type="image",
            crop=result["crop"],
            disease=result["disease"],
            severity=result["severity"],
            recommendation=result["recommendation"],
            confidence=result["confidence"],
            raw_json=json.dumps(result),
        )
        st.success("Saved.")
