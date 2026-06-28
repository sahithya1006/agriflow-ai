import json

import streamlit as st
import streamlit.components.v1 as components
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

st.markdown("#### 🎙️ Voice Input")
st.caption("Click the button, speak, then copy the text into the box below")

components.html(
    f"""
<!DOCTYPE html>
<html>
<body style="margin:0;padding:0;font-family:sans-serif;">

<button id="micBtn" onclick="startSpeech()"
    style="background:#2e7d32;color:white;border:none;padding:12px 24px;
    border-radius:8px;cursor:pointer;font-size:16px;width:100%;margin-bottom:8px;">
    🎙️ Click to Speak
</button>

<div id="status"
    style="color:#555;font-size:13px;margin-bottom:8px;min-height:20px;">
    Press the button and speak
</div>

<div id="result-box"
    style="background:#f1f8e9;border:2px solid #2e7d32;border-radius:8px;
    padding:12px;font-size:15px;min-height:50px;margin-bottom:8px;
    color:#1b5e20;font-weight:500;word-wrap:break-word;">
    Your speech will appear here
</div>

<div style="font-size:12px;color:#777;margin-bottom:4px;">
    👆 Copy the text above and paste it in the box below in Streamlit
</div>

<script>
function startSpeech() {{
    if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {{
        document.getElementById('status').innerText = '❌ Use Chrome browser for voice.';
        document.getElementById('status').style.color = 'red';
        return;
    }}

    var recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = '{lang[1]}';
    recognition.continuous = false;
    recognition.interimResults = true;

    document.getElementById('micBtn').innerText = '🔴 Listening... Speak now';
    document.getElementById('micBtn').style.background = '#c62828';
    document.getElementById('status').innerText = '🎤 Listening... speak clearly';
    document.getElementById('status').style.color = '#c62828';
    document.getElementById('result-box').innerText = '...';

    recognition.start();

    recognition.onresult = function(event) {{
        var interim = '';
        var final = '';
        for (var i = event.resultIndex; i < event.results.length; i++) {{
            if (event.results[i].isFinal) {{
                final += event.results[i][0].transcript;
            }} else {{
                interim += event.results[i][0].transcript;
            }}
        }}
        document.getElementById('result-box').innerText = final || interim;
    }};

    recognition.onend = function() {{
        document.getElementById('micBtn').innerText = '🎙️ Click to Speak again';
        document.getElementById('micBtn').style.background = '#2e7d32';
        document.getElementById('status').innerText = '✅ Done! Copy the text above into the box below';
        document.getElementById('status').style.color = '#2e7d32';
    }};

    recognition.onerror = function(event) {{
        document.getElementById('micBtn').innerText = '🎙️ Click to Speak';
        document.getElementById('micBtn').style.background = '#2e7d32';
        document.getElementById('status').innerText = '❌ Error: ' + event.error + '. Try again.';
        document.getElementById('status').style.color = 'red';
    }};
}}
</script>
</body>
</html>
""",
    height=220,
)

symptoms = st.text_area(
    "Type or paste your problem here",
    placeholder="Speak using the mic above, then paste the text here",
)

if st.button("🔍 Get advice"):
    if not symptoms:
        st.warning("Please describe your problem first.")
    else:
        with st.spinner("Running AI..."):
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
