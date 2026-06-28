import json
import streamlit as st
import streamlit.components.v1 as components
from database.db import save_prediction

st.title("❓ Ask a Question")
st.caption("Type your farming problem or use the microphone")

crop = st.selectbox(
    "Select crop",
    ["Tomato", "Wheat", "Rice", "Cotton", "Maize", "Sugarcane", "Chilli", "Soybean"],
)

lang = st.selectbox(
    "Select language for voice",
    [
        ("Telugu", "te-IN"),
        ("Hindi", "hi-IN"),
        ("English", "en-IN"),
        ("Tamil", "ta-IN"),
    ],
    format_func=lambda x: x[0],
)

components.html(
    f"""
<!DOCTYPE html>
<html>
<body style="background:transparent;margin:0;padding:0;">

<button id="micBtn" onclick="startSpeech()"
    style="background:#2e7d32;color:white;border:none;padding:12px 24px;
    border-radius:8px;cursor:pointer;font-size:16px;width:100%;">
    🎙️ Click here to Speak
</button>

<p id="status" style="color:gray;font-size:13px;margin-top:8px;"></p>

<textarea id="result" rows="3"
    style="width:100%;margin-top:8px;padding:10px;border-radius:8px;
    border:1px solid #ccc;font-size:14px;"
    placeholder="Your speech will appear here...">
</textarea>

<button onclick="sendText()"
    style="margin-top:8px;background:#1565c0;color:white;border:none;
    padding:10px 20px;border-radius:8px;cursor:pointer;font-size:14px;width:100%;">
    ✅ Use this text
</button>

<script>
var recognition;

function startSpeech() {{
    if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {{
        document.getElementById('status').innerText = 'Please use Chrome browser for voice input.';
        return;
    }}

    recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = '{lang[1]}';
    recognition.continuous = false;
    recognition.interimResults = false;

    document.getElementById('micBtn').innerText = '🔴 Recording... Speak now';
    document.getElementById('micBtn').style.background = '#c62828';
    document.getElementById('status').innerText = 'Listening...';

    recognition.start();

    recognition.onresult = function(event) {{
        var transcript = event.results[0][0].transcript;
        document.getElementById('result').value = transcript;
        document.getElementById('micBtn').innerText = '🎙️ Click here to Speak';
        document.getElementById('micBtn').style.background = '#2e7d32';
        document.getElementById('status').innerText = 'Done! Click Use this text.';
    }};

    recognition.onerror = function(event) {{
        document.getElementById('micBtn').innerText = '🎙️ Click here to Speak';
        document.getElementById('micBtn').style.background = '#2e7d32';
        document.getElementById('status').innerText = 'Error: ' + event.error + '. Try again.';
    }};

    recognition.onend = function() {{
        document.getElementById('micBtn').innerText = '🎙️ Click here to Speak';
        document.getElementById('micBtn').style.background = '#2e7d32';
    }};
}}

function sendText() {{
    var text = document.getElementById('result').value;
    if (text) {{
        window.parent.postMessage({{type: 'streamlit:setComponentValue', value: text}}, '*');
    }}
}}
</script>
</body>
</html>
""",
    height=280,
)

symptoms = st.text_area(
    "Or type your problem here", placeholder="Spoken text or type manually here"
)

if st.button("🔍 Get advice"):
    if not symptoms:
        st.warning("Please describe your problem or speak first.")
    else:
        with st.spinner("Running AI..."):
            result = {
                "crop": crop,
                "disease": "Early Blight",
                "severity": "High",
                "recommendation": "Apply Copper Fungicide at 2g per litre every 7 days",
                "confidence": 0.87,
            }

        st.markdown("### Result")
        col1, col2 = st.columns(2)
        col1.metric("Disease", result["disease"])
        col2.metric("Confidence", f"{result['confidence']*100:.0f}%")
        st.error(f"Severity: {result['severity']}")
        st.success(f"Recommendation: {result['recommendation']}")
        st.json(result)

        if st.button("💾 Save to history"):
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
