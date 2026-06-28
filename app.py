import runpy

import streamlit as st

from database.db import init_db

init_db()

st.set_page_config(page_title="AgriFlow AI", page_icon="AG", layout="wide")

with st.sidebar:
    st.title("AgriFlow AI")
    st.caption("Offline Farm Assistant")
    st.markdown("---")
    choice = st.radio(
        "Navigate",
        ["Home", "Ask Question", "Upload Image", "Dashboard", "Reports"],
    )
    st.markdown("---")
    st.success("Running offline")
    st.caption("CPU only - No cloud - SQLite")

if choice == "Home":
    runpy.run_path("ui/home.py", run_name="__main__")
elif choice == "Ask Question":
    runpy.run_path("ui/ask.py", run_name="__main__")
elif choice == "Upload Image":
    runpy.run_path("ui/upload.py", run_name="__main__")
elif choice == "Dashboard":
    runpy.run_path("ui/dashboard.py", run_name="__main__")
elif choice == "Reports":
    runpy.run_path("ui/reports.py", run_name="__main__")
