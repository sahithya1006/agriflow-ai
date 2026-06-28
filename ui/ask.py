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

    recognition.start();

    recognition.onresult = function(event) {{
        var interim = '';
        var final_transcript = '';
        for (var i = event.resultIndex; i < event.results.length; i++) {{
            if (event.results[i].isFinal) {{
                final_transcript += event.results[i][0].transcript;
            }} else {{
                interim += event.results[i][0].transcript;
            }}
        }}

        var text = final_transcript || interim;
        document.getElementById('status').innerText = '📝 ' + text;

        if (final_transcript) {{
            // directly paste into streamlit text area
            var allTextAreas = window.parent.document.querySelectorAll('textarea');
            for (var i = 0; i < allTextAreas.length; i++) {{
                if (allTextAreas[i].getAttribute('aria-label') === 'Type or paste your problem here') {{
                    var nativeInputValueSetter = Object.getOwnPropertyDescriptor(
                        window.HTMLTextAreaElement.prototype, 'value'
                    ).set;
                    nativeInputValueSetter.call(allTextAreas[i], final_transcript);
                    allTextAreas[i].dispatchEvent(new Event('input', {{ bubbles: true }}));
                    break;
                }}
            }}
        }}
    }};

    recognition.onend = function() {{
        document.getElementById('micBtn').innerText = '🎙️ Click to Speak again';
        document.getElementById('micBtn').style.background = '#2e7d32';
        document.getElementById('status').style.color = '#2e7d32';
        document.getElementById('status').innerText = '✅ Done! Click Get advice below';
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
    height=120,
)

symptoms = st.text_area(
    "Type or paste your problem here",
    placeholder="Speak using the mic above — text will appear here automatically",
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
