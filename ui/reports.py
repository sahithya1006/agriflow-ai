import streamlit as st
import pandas as pd
from database.db import get_all_predictions

st.title("📄 Reports")

rows = get_all_predictions()

if not rows:
    st.info("No data to export yet.")
else:
    df = pd.DataFrame(rows, columns=[
        "ID", "Input Type", "Crop", "Disease",
        "Severity", "Recommendation", "Confidence", "JSON", "Created At"
    ])

    col1, col2 = st.columns(2)

    with col1:
        csv = df.to_csv(index=False)
        st.download_button(
            "⬇️ Download CSV",
            csv,
            "agriflow_report.csv",
            "text/csv"
        )

    with col2:
        json_data = df.to_json(orient="records", indent=2)
        st.download_button(
            "⬇️ Download JSON",
            json_data,
            "agriflow_report.json",
            "application/json"
        )

    st.dataframe(
        df[["Created At", "Crop", "Disease", "Severity", "Recommendation"]],
        use_container_width=True
    )