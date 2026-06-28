import streamlit as st

st.title("🌾 agriflow-ai")
st.subheader("Offline AI assistant for farmers")

st.info("This app runs 100% offline on your CPU. No internet needed.")

col1, col2, col3 = st.columns(3)
col1.metric("Models", "4", "CPU only")
col2.metric("Languages", "3", "Hindi, Telugu, English")
col3.metric("Crops", "15+", "All major crops")

st.markdown("---")
st.markdown("### What can agriflow-ai do?")
st.markdown("""
- 🔬 Detect crop diseases from symptoms
- 💊 Recommend fertilizers based on crop and soil
- 🧾 Read fertilizer bills using OCR
- ❓ Answer farming questions
- 📊 Track all predictions locally
""")
