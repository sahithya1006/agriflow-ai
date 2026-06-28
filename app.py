import streamlit as st
from database.db import init_db

init_db()

st.set_page_config(
    page_title="agriflow-ai",
    page_icon="🌾",
    layout="wide"
)

with st.sidebar:
    st.title("🌾 agriflow-ai")
    st.caption("Offline Farm Assistant")
    st.markdown("---")
    choice = st.radio("Navigate", [
        "🏠 Home",
        "❓ Ask Question",
        "📷 Upload Image",
        "📊 Dashboard",
        "📄 Reports"
    ])
    st.markdown("---")
    st.success("● Running offline")
    st.caption("CPU only · No cloud · SQLite")

if choice == "🏠 Home":
    exec(open("ui/home.py").read())
elif choice == "❓ Ask Question":
    exec(open("ui/ask.py").read())
elif choice == "📷 Upload Image":
    exec(open("ui/upload.py").read())
elif choice == "📊 Dashboard":
    exec(open("ui/dashboard.py").read())
elif choice == "📄 Reports":
    exec(open("ui/reports.py").read())