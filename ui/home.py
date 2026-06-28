# ruff: noqa: E501
import streamlit as st

st.markdown("""
<style>
.hero {
    background: linear-gradient(135deg, #1b5e20 0%, #2e7d32 50%, #388e3c 100%);
    padding: 40px;
    border-radius: 16px;
    color: white;
    text-align: center;
    margin-bottom: 24px;
}
.hero h1 { font-size: 48px; margin: 0; }
.hero p { font-size: 18px; opacity: 0.9; margin-top: 8px; }
.feature-card {
    background: white;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    height: 100%;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}
.feature-icon { font-size: 36px; margin-bottom: 10px; }
.feature-title { font-size: 16px; font-weight: 600; color: #1b5e20; margin-bottom: 6px; }
.feature-desc { font-size: 13px; color: #666; }
.stat-box {
    background: linear-gradient(135deg, #e8f5e9, #f1f8e9);
    border: 1px solid #c8e6c9;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
}
.stat-num { font-size: 36px; font-weight: 700; color: #1b5e20; }
.stat-label { font-size: 13px; color: #555; margin-top: 4px; }
.offline-badge {
    display: inline-block;
    background: rgba(255,255,255,0.15);
    border: 1px solid rgba(255,255,255,0.4);
    color: white;
    padding: 6px 16px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 600;
    margin-top: 12px;
}
.lang-pill {
    display: inline-block;
    background: #e8f5e9;
    border: 1px solid #4caf50;
    color: #1b5e20;
    padding: 8px 20px;
    border-radius: 20px;
    font-size: 14px;
    font-weight: 600;
    margin: 4px;
}
.step-card {
    background: white;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    padding: 16px;
    text-align: center;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}
.step-num {
    background: #2e7d32;
    color: white;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    margin: 0 auto 8px;
    font-size: 16px;
}
</style>

<div class="hero">
    <div style="font-size:72px;">🌽</div>
    <h1>🌾 AgriFlow AI</h1>
    <p>Your offline AI assistant for smarter farming decisions</p>
    <div class="offline-badge">✅ 100% Offline &nbsp;·&nbsp; CPU Only &nbsp;·&nbsp; No Internet Needed</div>
</div>
""", unsafe_allow_html=True)

st.markdown("### 📊 At a Glance")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-num">🤖 4</div>
        <div class="stat-label">AI Models Running on CPU</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-num">🌐 4</div>
        <div class="stat-label">Languages Supported</div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-num">🌱 15+</div>
        <div class="stat-label">Crops Covered</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### 🚀 What can AgriFlow AI do?")

col1, col2, col3, col4 = st.columns(4)
features = [
    ("🔬", "Disease Detection", "Identify crop diseases instantly from symptoms"),
    ("💊", "Fertilizer Advice", "Get the right fertilizer for your crop and soil"),
    ("🧾", "Bill Scanner", "Scan fertilizer bills using OCR technology"),
    ("📊", "Farm Dashboard", "Track all predictions and history locally"),
]
for col, (icon, title, desc) in zip([col1, col2, col3, col4], features):
    with col:
        st.markdown(f"""
        <div class="feature-card">
            <div class="feature-icon">{icon}</div>
            <div class="feature-title">{title}</div>
            <div class="feature-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### 🌍 Supported Languages")
st.markdown("""
<div>
    <span class="lang-pill">🇮🇳 Telugu</span>
    <span class="lang-pill">🇮🇳 Hindi</span>
    <span class="lang-pill">🇮🇳 Tamil</span>
    <span class="lang-pill">🌐 English</span>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### 📋 How to Use")

col1, col2, col3, col4 = st.columns(4)
steps = [
    ("1", "❓ Ask Question", "Type or speak your crop problem"),
    ("2", "📷 Upload Image", "Upload a crop photo or bill"),
    ("3", "🔍 Get AI Advice", "Instant diagnosis and recommendation"),
    ("4", "💾 Save History", "All data saved locally to SQLite"),
]
for col, (num, title, desc) in zip([col1, col2, col3, col4], steps):
    with col:
        st.markdown(f"""
        <div class="step-card">
            <div class="step-num">{num}</div>
            <div style="font-size:24px;margin-bottom:6px;">{title.split()[0]}</div>
            <div style="font-size:14px;font-weight:600;color:#1b5e20;">{" ".join(title.split()[1:])}</div>
            <div style="font-size:12px;color:#666;margin-top:4px;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.success("🔒 **Privacy First** — All your farm data stays on your device. Nothing is sent to the cloud.")
st.info("💡 **Tip** — Use Chrome browser for the best voice input experience in the Ask Question page.")