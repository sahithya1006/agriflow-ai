import streamlit as st
import pandas as pd
from database.db import get_all_predictions

st.title("📊 Dashboard")

rows = get_all_predictions()

if not rows:
    st.info("No predictions yet. Ask a question or upload an image to get started.")
else:
    df = pd.DataFrame(
        rows,
        columns=[
            "ID",
            "Input Type",
            "Crop",
            "Disease",
            "Severity",
            "Recommendation",
            "Confidence",
            "JSON",
            "Created At",
        ],
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Total predictions", len(df))
    col2.metric("Unique crops", df["Crop"].nunique())
    col3.metric("Most common disease", df["Disease"].mode()[0])

    st.markdown("---")
    st.subheader("Recent predictions")
    st.dataframe(
        df[
            [
                "Created At",
                "Crop",
                "Disease",
                "Severity",
                "Recommendation",
                "Confidence",
            ]
        ],
        use_container_width=True,
    )

    st.subheader("Disease breakdown")
    st.bar_chart(df["Disease"].value_counts())
