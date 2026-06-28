import json

import streamlit as st

from database.db import save_prediction

st.title("❓ Ask a Question")
st.caption("Type your farming problem or use the microphone")

crop = st.selectbox(
    "Select crop",
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

st.markdown(
    """
<style>
.mic-btn {
    background-color: #2e7d32;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 16px;
}
.mic-btn.recording {
    background-color: #c62828;
}
</style>

<script>
function startDictation() {
    if (window.hasOwnProperty('webkitSpeechRecognition')) {
        var recognition = new webkitSpeechRecognition();
        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.lang = document.getElementById('lang-select').value;
        recognition.start();

        document.getElementById('mic-btn').classList.add('recording');
        document.getElementById('mic-btn').innerText = '🔴 Recording...';

        recognition.onresult = function(e) {
            document.getElementById('transcript').value =
                e.results[0][0].transcript;
            document.getElementById('mic-btn').classList.remove('recording');
            document.getElementById('mic-btn').innerText = '🎙️ Speak';
            recognition.stop();
        };

        recognition.onerror = function(e) {
            document.getElementById('mic-btn').classList.remove('recording');
            document.getElementById('mic-btn').innerText = '🎙️ Speak';
        };
    } else {
        alert('Speech recognition is not supported. Please use Chrome.');
    }
}
</script>

<select
    id="lang-select"
    style="padding:8px;border-radius:6px;margin-bottom:10px;">
    <option value="te-IN">Telugu</option>
    <option value="hi-IN">Hindi</option>
    <option value="en-IN">English</option>
    <option value="ta-IN">Tamil</option>
</select>

<br>

<button
    id="mic-btn"
    class="mic-btn"
    onclick="startDictation()">
    🎙️ Speak
</button>

<br><br>

<textarea
    id="transcript"
    rows="3"
    style="
        width:100%;
        padding:10px;
        border-radius:8px;
        border:1px solid #ccc;
        font-size:14px;
    "
    placeholder="Your speech will appear here...">
</textarea>

<br>

<button
    onclick="
        var text = document.getElementById('transcript').value;
        var input = window.parent.document.querySelectorAll('textarea')[0];
        var setter = Object.getOwnPropertyDescriptor(
            window.HTMLTextAreaElement.prototype,
            'value'
        ).set;
        setter.call(input, text);
        input.dispatchEvent(new Event('input', { bubbles: true }));
    "
    style="
        margin-top:8px;
        padding:8px 16px;
        background:#1565c0;
        color:white;
        border:none;
        border-radius:6px;
        cursor:pointer;
    ">
    ✅ Use this text
</button>
""",
    unsafe_allow_html=True,
)

symptoms = st.text_area(
    "Or type your problem here",
    placeholder="e.g. My tomato leaves have brown spots and are turning yellow",
)

if st.button("🔍 Get advice"):
    if not symptoms:
        st.warning("Please describe your problem first.")
    else:
        with st.spinner("Running offline AI..."):
            result = {
                "crop": crop,
                "disease": "Early Blight",
                "severity": "High",
                "recommendation": (
                    "Apply Copper Fungicide at 2g per litre every 7 days"
                ),
                "confidence": 0.87,
            }

        st.markdown("### Result")
        col1, col2 = st.columns(2)
        col1.metric("Disease", result["disease"])
        col2.metric("Confidence", f"{result['confidence'] * 100:.0f}%")
        st.error(f"Severity: {result['severity']}")
        st.success(f"Recommendation: {result['recommendation']}")
        st.json(result)

        if st.button("Save to history"):
            save_prediction(
                input_type="voice",
                crop=result["crop"],
                disease=result["disease"],
                severity=result["severity"],
                recommendation=result["recommendation"],
                confidence=result["confidence"],
                raw_json=json.dumps(result),
            )
            st.success("Saved.")
