# ruff: noqa: E501
import json

import streamlit as st

from database.db import save_prediction

try:
    import speech_recognition as sr

    MIC_AVAILABLE = True
except ImportError:
    MIC_AVAILABLE = False

st.markdown(
    """
<style>
.ask-hero {
    background: linear-gradient(135deg, #e65100, #f57c00);
    padding: 30px;
    border-radius: 16px;
    color: white;
    margin-bottom: 24px;
    text-align: center;
}
.ask-hero h2 { margin: 0; font-size: 32px; }
.ask-hero p { margin-top: 8px; opacity: 0.9; font-size: 15px; }
</style>
<div class="ask-hero">
    <div style="font-size:48px;">❓</div>
    <h2>Ask a Question</h2>
    <p>Describe your farming problem and get instant AI advice — 100% offline</p>
</div>
""",
    unsafe_allow_html=True,
)

col_left, col_right = st.columns([2, 1])

with col_left:
    crop = st.selectbox(
        "🌿 Select your crop",
        [
            "Tomato",
            "Wheat",
            "Rice",
            "Cotton",
            "Maize",
            "Sugarcane",
            "Chilli",
            "Soybean",
        ],
    )

    language = st.selectbox(
        "🌐 Select language for voice input",
        [
            ("English", "en-IN"),
            ("Telugu (తెలుగు)", "te-IN"),
            ("Hindi (हिंदी)", "hi-IN"),
            ("Tamil (தமிழ்)", "ta-IN"),
            ("Kannada (ಕನ್ನಡ)", "kn-IN"),
        ],
        format_func=lambda x: x[0],
    )
    lang_code = language[1]

    symptoms = st.text_area(
        "📝 Describe your problem",
        placeholder="e.g. My tomato leaves have brown spots and are turning yellow",
        key="symptoms_input",
        height=120,
    )

    mic_col, btn_col = st.columns([1, 3])
    with mic_col:
        mic_clicked = st.button(
            "🎤 Speak", use_container_width=True, help=f"Speak in {language[0]}"
        )
    with btn_col:
        get_advice = st.button(
            "🔍 Get Advice", use_container_width=True, type="primary"
        )

    if mic_clicked:
        if not MIC_AVAILABLE:
            st.error(
                "SpeechRecognition not installed. Run: pip install SpeechRecognition pyaudio"
            )
        else:
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                with st.spinner(f"🎙️ Listening in {language[0]}... Speak now!"):
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    try:
                        audio = recognizer.listen(source, timeout=6)
                        text = recognizer.recognize_google(audio, language=lang_code)
                        st.session_state["symptoms_input"] = text
                        st.success(f"✅ Heard: {text}")
                        st.rerun()
                    except sr.WaitTimeoutError:
                        st.warning("⏱️ No speech detected. Try again.")
                    except sr.UnknownValueError:
                        st.warning("❓ Could not understand. Speak clearly.")
                    except Exception as e:
                        st.error(f"Mic error: {e}")

with col_right:
    st.markdown("#### 💡 Example Questions")
    examples = [
        "My tomato leaves have yellow spots",
        "Rice has brown patches on leaves",
        "Cotton plant has white insects",
        "Which fertilizer for wheat?",
        "When to water sugarcane?",
    ]
    for ex in examples:
        if st.button(ex, use_container_width=True, key=ex):
            st.session_state["symptoms_input"] = ex
            st.rerun()

if get_advice and st.session_state.get("symptoms_input"):
    symptoms = st.session_state["symptoms_input"]
    with st.spinner("🤖 Running offline AI..."):
        from ai.disease_model import predict_disease
        from ai.text_classifier import classify_query

        category = classify_query(symptoms)["category"]
        result = predict_disease(
            crop=crop, symptom=symptoms, season="Kharif", soil_type="Red Soil"
        )
        result["category"] = category

    st.session_state["last_result"] = result

if "last_result" in st.session_state:
    result = st.session_state["last_result"]
    st.markdown("---")
    st.markdown("### 🧪 Analysis Result")

    col1, col2, col3 = st.columns(3)
    col1.metric("🦠 Disease", result["disease"])
    col2.metric("📊 Confidence", f"{result['confidence']*100:.0f}%")
    col3.metric("🏷️ Category", result.get("category", "Disease"))

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
            input_type="text",
            crop=crop,
            disease=result["disease"],
            severity=result["severity"],
            recommendation=result["recommendation"],
            confidence=result["confidence"],
            raw_json=json.dumps(result),
        )
        st.success("✅ Saved to history!")
        del st.session_state["last_result"]
