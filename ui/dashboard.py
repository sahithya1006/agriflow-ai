# ruff: noqa: E501
import pandas as pd
import streamlit as st

from database.db import get_all_predictions

st.markdown(
    """
<style>
.dash-hero {
    background: linear-gradient(135deg, #1565c0, #1976d2);
    padding: 30px;
    border-radius: 16px;
    color: white;
    margin-bottom: 24px;
    text-align: center;
}
.dash-hero h2 { margin: 0; font-size: 32px; }
.dash-hero p { margin-top: 8px; opacity: 0.9; font-size: 15px; }
.stat-card {
    background: white;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}
.stat-num { font-size: 36px; font-weight: 700; }
.stat-label { font-size: 13px; color: #666; margin-top: 4px; }
.empty-box {
    background: #f5f5f5;
    border: 2px dashed #ccc;
    border-radius: 12px;
    padding: 40px;
    text-align: center;
    color: #999;
}
</style>

<div class="dash-hero">
    <div style="font-size:48px;">📊</div>
    <h2>Farm Dashboard</h2>
    <p>All your predictions and history saved locally on your device</p>
</div>
""",
    unsafe_allow_html=True,
)

rows = get_all_predictions()

if not rows:
    st.markdown(
        """
    <div class="empty-box">
        <div style="font-size:48px;">🌱</div>
        <div style="font-size:18px;font-weight:600;margin-top:12px;">No predictions yet</div>
        <div style="font-size:14px;margin-top:8px;">Go to Ask a Question or Upload Image to get started</div>
    </div>
    """,
        unsafe_allow_html=True,
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

    # Stats row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(
            f"""
        <div class="stat-card">
            <div class="stat-num" style="color:#1b5e20;">🔬 {len(df)}</div>
            <div class="stat-label">Total Predictions</div>
        </div>
        """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            f"""
        <div class="stat-card">
            <div class="stat-num" style="color:#e65100;">🌿 {df["Crop"].nunique()}</div>
            <div class="stat-label">Unique Crops</div>
        </div>
        """,
            unsafe_allow_html=True,
        )
    with col3:
        most_common = df["Disease"].mode()[0] if not df.empty else "None"
        st.markdown(
            f"""
        <div class="stat-card">
            <div class="stat-num" style="color:#b71c1c;font-size:20px;">🦠 {most_common}</div>
            <div class="stat-label">Most Common Disease</div>
        </div>
        """,
            unsafe_allow_html=True,
        )
    with col4:
        avg_conf = df["Confidence"].mean() * 100 if not df.empty else 0
        st.markdown(
            f"""
        <div class="stat-card">
            <div class="stat-num" style="color:#1565c0;">📊 {avg_conf:.0f}%</div>
            <div class="stat-label">Average Confidence</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # Charts
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 🦠 Disease Breakdown")
        st.bar_chart(df["Disease"].value_counts())
    with col2:
        st.markdown("#### 🌿 Crop Breakdown")
        st.bar_chart(df["Crop"].value_counts())

    st.markdown("---")
    st.markdown("#### 📋 Recent Predictions")

    # Severity color coding
    def color_severity(val):
        if val == "High":
            return "background-color: #ffebee; color: #b71c1c; font-weight: bold;"
        elif val == "Medium":
            return "background-color: #fff8e1; color: #e65100; font-weight: bold;"
        return "background-color: #e8f5e9; color: #1b5e20; font-weight: bold;"

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

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True,
    )

    st.markdown("---")
    st.markdown("#### 💾 Local Database Info")
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"📁 Total records stored: **{len(df)}**")
    with col2:
        st.info("🔒 All data saved locally — never sent to cloud")
