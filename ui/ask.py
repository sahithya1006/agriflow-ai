import json
import speech_recognition as sr
import streamlit as st

from database.db import save_prediction

st.title("❓ Ask a Question")
st.caption("Type your farming problem or use the microphone")

crop = st.selectbox(
    "Select crop",
    ["Tomato", "Wheat", "Rice", "Cotton", "Maize", "Sugarcane", "Chilli", "Soybean"],
)

# ── Voice input ──────────────────────────────────────────────
col_text, col_mic = st.columns([9, 1])

with col_text:
    symptoms = st.text_area(
        "Describe your problem",
        placeholder="e.g. My tomato leaves have brown spots and are turning yellow",
        key="symptoms_input",
        height=100,
    )

with col_mic:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🎤", help="Click to speak your problem"):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            with st.spinner("🎙️ Listening..."):
                recognizer.adjust_for_ambient_noise(source, duration=1)
                try:
                    audio = recognizer.listen(source, timeout=5)
                    text = recognizer.recognize_google(audio)
                    st.session_state["symptoms_input"] = text
                    st.success(f"Heard: {text}")
                    st.rerun()
                except sr.WaitTimeoutError:
                    st.warning("No speech detected. Try again.")
                except sr.UnknownValueError:
                    st.warning("Could not understand. Speak clearly.")
                except Exception as e:
                    st.error(f"Mic error: {e}")

# ── Get advice ───────────────────────────────────────────────
if st.button("🔍 Get advice"):
    if not symptoms:
        st.warning("Please describe your problem first.")
    else:
        with st.spinner("Running offline AI..."):
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

        if st.button("Save to history"):
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
