import json
import os
import tempfile
from pathlib import Path

import streamlit as st

from database.db import save_prediction

st.markdown(
    """
<style>
.upload-hero {
    background: linear-gradient(135deg, #1b5e20, #2e7d32);
    padding: 30px;
    border-radius: 16px;
    color: white;
    margin-bottom: 24px;
    text-align: center;
}
.upload-hero h2 { margin: 0; font-size: 32px; }
.upload-hero p { margin-top: 8px; opacity: 0.9; font-size: 15px; }
.tip-card {
    background: #e8f5e9;
    border-left: 4px solid #2e7d32;
    border-radius: 8px;
    padding: 12px 16px;
    margin-bottom: 12px;
    font-size: 14px;
    color: #1b5e20;
}
.result-card {
    background: white;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    margin-top: 16px;
}
</style>

<div class="upload-hero">
    <div style="font-size:48px;">📷</div>
    <h2>Upload Crop Image</h2>
    <p>Upload a crop photo or fertilizer bill for instant AI analysis</p>
</div>
""",
    unsafe_allow_html=True,
)

col1, col2 = st.columns([2, 1])

with col2:
    st.markdown("#### 💡 Tips")
    st.markdown(
        '<div class="tip-card">📸 Use clear, well-lit photos</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="tip-card">🌿 Focus on affected leaves</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="tip-card">📄 Bills: ensure text is readable</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="tip-card">🖼️ Supported: JPG, PNG, PDF</div>', unsafe_allow_html=True
    )

with col1:
    uploaded = st.file_uploader(
        "Choose a file",
        type=["jpg", "jpeg", "png", "pdf"],
        help="Upload a crop image or fertilizer bill",
    )

    if uploaded:
        if uploaded.type.startswith("image"):
            st.image(uploaded, caption="Uploaded Image", use_container_width=True)

        with st.spinner("🔍 Running OCR and disease detection..."):
            from ai.disease_model import predict_disease
            from ai.ocr import extract_text

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

        st.session_state["upload_result"] = result

if "upload_result" in st.session_state:
    result = st.session_state["upload_result"]

    st.markdown("---")
    st.markdown("### 🧪 Analysis Result")

    col1, col2, col3 = st.columns(3)
    col1.metric("🌿 Crop", result["crop"])
    col2.metric("🦠 Disease", result["disease"])
    col3.metric("📊 Confidence", f"{result['confidence'] * 100:.0f}%")

    if result.get("severity") == "High":
        st.error(f"⚠️ Severity: {result['severity']}")
    elif result.get("severity") == "Medium":
        st.warning(f"⚠️ Severity: {result['severity']}")
    else:
        st.info(f"✅ Severity: {result.get('severity', 'Low')}")

    st.success(f"💊 Recommendation: {result['recommendation']}")

    with st.expander("📋 View full JSON output"):
        st.json(result)

    if st.button("💾 Save to history", use_container_width=True):
        save_prediction(
            input_type="image",
            crop=result["crop"],
            disease=result["disease"],
            severity=result["severity"],
            recommendation=result["recommendation"],
            confidence=result["confidence"],
            raw_json=json.dumps(result),
        )
        st.success("✅ Saved to history!")
        del st.session_state["upload_result"]
