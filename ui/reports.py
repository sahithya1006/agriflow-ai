# ruff: noqa: E501
import json

import pandas as pd
import streamlit as st

from database.db import get_all_predictions

st.markdown("""
<style>
.report-hero {
    background: linear-gradient(135deg, #4a148c, #6a1b9a);
    padding: 30px;
    border-radius: 16px;
    color: white;
    margin-bottom: 24px;
    text-align: center;
}
.report-hero h2 { margin: 0; font-size: 32px; }
.report-hero p { margin-top: 8px; opacity: 0.9; font-size: 15px; }
.report-card {
    background: white;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    margin-bottom: 16px;
}
.report-card h4 { margin: 0 0 6px; color: #4a148c; font-size: 16px; }
.report-card p { margin: 0; font-size: 13px; color: #666; }
.summary-box {
    background: linear-gradient(135deg, #e8f5e9, #f1f8e9);
    border: 1px solid #c8e6c9;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 16px;
}
.empty-box {
    background: #f5f5f5;
    border: 2px dashed #ccc;
    border-radius: 12px;
    padding: 40px;
    text-align: center;
    color: #999;
}
.stat-row {
    display: flex;
    justify-content: space-between;
    padding: 10px 0;
    border-bottom: 1px solid #e0e0e0;
    font-size: 14px;
}
.stat-row:last-child { border-bottom: none; }
</style>

<div class="report-hero">
    <div style="font-size:48px;">📄</div>
    <h2>Reports & Export</h2>
    <p>Download your farm data as CSV or JSON — all stored locally</p>
</div>
""", unsafe_allow_html=True)

rows = get_all_predictions()

if not rows:
    st.markdown("""
    <div class="empty-box">
        <div style="font-size:48px;">📭</div>
        <div style="font-size:18px;font-weight:600;margin-top:12px;">No data to export yet</div>
        <div style="font-size:14px;margin-top:8px;">Go to Ask a Question or Upload Image to generate predictions first</div>
    </div>
    """, unsafe_allow_html=True)

else:
    df = pd.DataFrame(rows, columns=[
        "ID", "Input Type", "Crop", "Disease",
        "Severity", "Recommendation", "Confidence", "JSON", "Created At"
    ])

    # Summary section
    st.markdown("### 📊 Season Summary")
    st.markdown(f"""
    <div class="summary-box">
        <div class="stat-row"><span>📋 Total predictions</span><strong>{len(df)}</strong></div>
        <div class="stat-row"><span>🌿 Crops analyzed</span><strong>{df['Crop'].nunique()}</strong></div>
        <div class="stat-row"><span>🦠 Most common disease</span><strong>{df['Disease'].mode()[0]}</strong></div>
        <div class="stat-row"><span>🔬 Most analyzed crop</span><strong>{df['Crop'].mode()[0]}</strong></div>
        <div class="stat-row"><span>📊 Average confidence</span><strong>{df['Confidence'].mean()*100:.0f}%</strong></div>
        <div class="stat-row"><span>📅 First prediction</span><strong>{df['Created At'].iloc[-1]}</strong></div>
        <div class="stat-row"><span>📅 Latest prediction</span><strong>{df['Created At'].iloc[0]}</strong></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Export section
    st.markdown("### ⬇️ Download Reports")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="report-card">
            <h4>📊 CSV Report</h4>
            <p>All predictions in spreadsheet format. Open in Excel or Google Sheets.</p>
        </div>
        """, unsafe_allow_html=True)
        csv = df.drop(columns=["JSON"]).to_csv(index=False)
        st.download_button(
            label="⬇️ Download CSV",
            data=csv,
            file_name="agriflow_report.csv",
            mime="text/csv",
            use_container_width=True,
        )

    with col2:
        st.markdown("""
        <div class="report-card">
            <h4>📋 JSON Report</h4>
            <p>Full structured data including raw AI output. Good for technical use.</p>
        </div>
        """, unsafe_allow_html=True)
        json_data = df.to_json(orient="records", indent=2)
        st.download_button(
            label="⬇️ Download JSON",
            data=json_data,
            file_name="agriflow_report.json",
            mime="application/json",
            use_container_width=True,
        )

    with col3:
        st.markdown("""
        <div class="report-card">
            <h4>📝 Summary TXT</h4>
            <p>Simple text summary of all predictions. Easy to read and share.</p>
        </div>
        """, unsafe_allow_html=True)
        summary_lines = []
        summary_lines.append("AGRIFLOW AI — FARM REPORT")
        summary_lines.append("=" * 40)
        summary_lines.append(f"Total Predictions: {len(df)}")
        summary_lines.append(f"Crops Analyzed: {df['Crop'].nunique()}")
        summary_lines.append(f"Most Common Disease: {df['Disease'].mode()[0]}")
        summary_lines.append("=" * 40)
        summary_lines.append("")
        for _, row in df.iterrows():
            summary_lines.append(f"Date: {row['Created At']}")
            summary_lines.append(f"Crop: {row['Crop']}")
            summary_lines.append(f"Disease: {row['Disease']}")
            summary_lines.append(f"Severity: {row['Severity']}")
            summary_lines.append(f"Recommendation: {row['Recommendation']}")
            summary_lines.append(f"Confidence: {row['Confidence']*100:.0f}%")
            summary_lines.append("-" * 40)
        summary_text = "\n".join(summary_lines)
        st.download_button(
            label="⬇️ Download TXT",
            data=summary_text,
            file_name="agriflow_summary.txt",
            mime="text/plain",
            use_container_width=True,
        )

    st.markdown("---")

    # Disease breakdown
    st.markdown("### 🦠 Disease Breakdown")
    col1, col2 = st.columns(2)
    with col1:
        st.bar_chart(df["Disease"].value_counts())
    with col2:
        st.bar_chart(df["Severity"].value_counts())

    st.markdown("---")

    # Full data table
    st.markdown("### 📋 Full Prediction History")
    display_df = df[["Created At", "Input Type", "Crop", "Disease", "Severity", "Recommendation", "Confidence"]].copy()
    display_df["Confidence"] = display_df["Confidence"].apply(lambda x: f"{x*100:.0f}%")
    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True,
    )

    st.markdown("---")
    st.success("🔒 All data is stored locally on your device in SQLite. Nothing is sent to the cloud.")