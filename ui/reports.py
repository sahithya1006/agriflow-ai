# ruff: noqa: E501
import pandas as pd
import streamlit as st

from database.db import get_all_predictions

st.title("📄 Reports & Export")
st.caption("Download your farm data — all stored locally")

rows = get_all_predictions()

if not rows:
    st.info(
        "No data to export yet. Go to Ask a Question or Upload Image to generate predictions first."
    )
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

    st.markdown("### 📊 Season Summary")
    col1, col2, col3 = st.columns(3)
    col1.metric("📋 Total Predictions", len(df))
    col2.metric("🌿 Crops Analyzed", df["Crop"].nunique())
    col3.metric("📊 Avg Confidence", f"{df['Confidence'].mean() * 100:.0f}%")

    col4, col5, col6 = st.columns(3)
    col4.metric("🦠 Most Common Disease", df["Disease"].mode()[0])
    col5.metric("🔬 Most Analyzed Crop", df["Crop"].mode()[0])
    col6.metric("📅 Latest Prediction", df["Created At"].iloc[0][:10])

    st.markdown("---")
    st.markdown("### ⬇️ Download Reports")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("**📊 CSV Report**")
        st.caption("Open in Excel or Google Sheets")
        csv = df.drop(columns=["JSON"]).to_csv(index=False)
        st.download_button(
            label="⬇️ Download CSV",
            data=csv,
            file_name="agriflow_report.csv",
            mime="text/csv",
            use_container_width=True,
        )

    with col2:
        st.markdown("**📋 JSON Report**")
        st.caption("Full structured data with raw AI output")
        json_data = df.to_json(orient="records", indent=2)
        st.download_button(
            label="⬇️ Download JSON",
            data=json_data,
            file_name="agriflow_report.json",
            mime="application/json",
            use_container_width=True,
        )

    with col3:
        st.markdown("**📝 Summary TXT**")
        st.caption("Simple text summary easy to read and share")
        summary_lines = []
        summary_lines.append("AGRIFLOW AI - FARM REPORT")
        summary_lines.append("=" * 40)
        summary_lines.append(f"Total Predictions: {len(df)}")
        summary_lines.append(f"Crops Analyzed: {df['Crop'].nunique()}")
        summary_lines.append(f"Most Common Disease: {df['Disease'].mode()[0]}")
        summary_lines.append("=" * 40)
        for _, row in df.iterrows():
            summary_lines.append(f"Date: {row['Created At']}")
            summary_lines.append(f"Crop: {row['Crop']}")
            summary_lines.append(f"Disease: {row['Disease']}")
            summary_lines.append(f"Severity: {row['Severity']}")
            summary_lines.append(f"Recommendation: {row['Recommendation']}")
            summary_lines.append(f"Confidence: {row['Confidence'] * 100:.0f}%")
            summary_lines.append("-" * 40)
        st.download_button(
            label="⬇️ Download TXT",
            data="\n".join(summary_lines),
            file_name="agriflow_summary.txt",
            mime="text/plain",
            use_container_width=True,
        )

    st.markdown("---")
    st.markdown("### 🦠 Disease Breakdown")
    col1, col2 = st.columns(2)
    with col1:
        st.bar_chart(df["Disease"].value_counts())
    with col2:
        st.bar_chart(df["Severity"].value_counts())

    st.markdown("---")
    st.markdown("### 📋 Full Prediction History")
    display_df = df[
        [
            "Created At",
            "Input Type",
            "Crop",
            "Disease",
            "Severity",
            "Recommendation",
            "Confidence",
        ]
    ].copy()
    display_df["Confidence"] = display_df["Confidence"].apply(
        lambda x: f"{x * 100:.0f}%"
    )
    st.dataframe(display_df, use_container_width=True, hide_index=True)

    st.markdown("---")
    st.success("🔒 All data stored locally in SQLite. Nothing sent to cloud.")
