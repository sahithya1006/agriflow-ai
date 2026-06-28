import streamlit as st
import json
from database.db import save_prediction

st.title("❓ Ask a Question")
st.caption("Type your farming problem in any language")

crop = st.selectbox(
    "Select crop",
    ["Tomato", "Wheat", "Rice", "Cotton", "Maize", "Sugarcane", "Chilli", "Soybean"],
)

symptoms = st.text_area(
    "Describe your problem",
    placeholder="e.g. My tomato leaves have brown spots and are turning yellow",
)

if st.button("🔍 Get advice"):
    if not symptoms:
        st.warning("Please describe your problem first.")
    else:
        with st.spinner("Running offline AI..."):
            # Replace this with Member 1's actual function once ready:
            # from ai.disease_model import predict_disease
            # result = predict_disease(crop=crop, symptoms=symptoms)
            from ai.disease_model import predict_disease
            from ai.text_classifier import classify_query

            category = classify_query(symptoms)["category"]
            result = predict_disease(
                crop=crop, symptom=symptoms, season="Kharif", soil_type="Red Soil"
            )
            result["category"] = category

        st.markdown("### Result")
        col1, col2 = st.columns(2)
        col1.metric("Disease", result["disease"])
        col2.metric("Confidence", f"{result['confidence'] * 100:.0f}%")
        st.error(f"Severity: {result['severity']}")
        st.success(f"Recommendation: {result['recommendation']}")
        st.json(result)

        if st.button("💾 Save to history"):
            save_prediction(
                input_type="text",
                crop=result["crop"],
                disease=result["disease"],
                severity=result["severity"],
                recommendation=result["recommendation"],
                confidence=result["confidence"],
                raw_json=json.dumps(result),
            )
            st.success("Saved.")
