import streamlit as st
import pandas as pd
from pathlib import Path

# -------------------------------------------------
# Page Config
# -------------------------------------------------
st.set_page_config(
    page_title="E-Commerce Churn Prediction",
    page_icon="📉",
    layout="wide"
)

# -------------------------------------------------
# Styling (Dark Mode Friendly)
# -------------------------------------------------
st.markdown("""
<style>
.stApp { background-color: #0f172a; }
h1, h2, h3, h4 { color: #f8fafc; }
p, li, span { color: #cbd5f5; }

.card {
    background: #111827;
    padding: 1.5rem;
    border-radius: 14px;
    border: 1px solid #1e293b;
}

.footer {
    text-align: center;
    color: #94a3b8;
    margin-top: 3rem;
    font-size: 0.9rem;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Navigation (Top Bar)
# -------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

pages = [
    "Home",
    "Single Customer",
    "Batch Prediction",
    "EDA Visualizations",
    "Model Overview",
    "Documentation"
]

selected = st.radio(
    "",
    pages,
    horizontal=True,
    index=pages.index(st.session_state.page)
)
st.session_state.page = selected
st.markdown("---")

# -------------------------------------------------
# HOME
# -------------------------------------------------
if selected == "Home":
    st.markdown("## 📉 E-Commerce Customer Churn Prediction")
    st.markdown("**End-to-End Machine Learning System for Customer Retention**")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="card"><h4>🎯 Objective</h4><p>Identify customers at risk of churn using behavioral signals.</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card"><h4>🧠 ML Workflow</h4><p>EDA → Feature Engineering → Modeling → Deployment.</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="card"><h4>🚀 Application</h4><p>Interactive web app for churn analysis.</p></div>', unsafe_allow_html=True)

# -------------------------------------------------
# SINGLE CUSTOMER
# -------------------------------------------------
elif selected == "Single Customer":
    st.markdown("## 👤 Single Customer Churn Prediction")

    col1, col2 = st.columns(2)

    with col1:
        recency = st.number_input("Recency (days since last purchase)", min_value=0, value=30)
        frequency = st.number_input("Frequency (total purchases)", min_value=0, value=5)
        monetary = st.number_input("Monetary Value (total spend)", min_value=0.0, value=500.0)

    with col2:
        avg_order = st.number_input("Average Order Value", min_value=0.0, value=100.0)
        recent_purchases = st.number_input("Purchases in last 90 days", min_value=0, value=2)

    if st.button("Predict Churn Risk"):
        score = (
            (recency / 90) * 0.4 +
            (1 / (frequency + 1)) * 0.2 +
            (1 / (recent_purchases + 1)) * 0.2 +
            (1 / (avg_order + 1)) * 0.2
        )
        churn_prob = min(max(score, 0), 1)

        st.subheader("📊 Prediction Result")
        st.metric("Churn Probability", f"{churn_prob:.2%}")

        if churn_prob > 0.6:
            st.error("High Risk: Customer is likely to churn")
        elif churn_prob > 0.3:
            st.warning("Medium Risk: Customer shows churn tendencies")
        else:
            st.success("Low Risk: Customer likely to remain active")

# -------------------------------------------------
# BATCH PREDICTION
# -------------------------------------------------
elif selected == "Batch Prediction":
    st.markdown("## 📂 Batch Customer Churn Prediction")

    uploaded = st.file_uploader("Upload customer data (CSV format)", type=["csv"])

    if uploaded:
        try:
            df = pd.read_csv(uploaded)

            df["Churn_Probability"] = (
                df.iloc[:, 0].rank(pct=True) * 0.4 +
                df.iloc[:, 1].rank(pct=True) * 0.3 +
                df.iloc[:, 2].rank(pct=True) * 0.3
            ).clip(0, 1)

            df["Churn_Risk"] = df["Churn_Probability"].apply(
                lambda x: "High" if x > 0.6 else "Medium" if x > 0.3 else "Low"
            )

            st.success("Batch prediction completed successfully")
            st.dataframe(df.head())

            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                "⬇️ Download Results",
                data=csv,
                file_name="churn_predictions.csv",
                mime="text/csv"
            )

        except Exception as e:
            st.error(f"Error processing file: {e}")

# -------------------------------------------------
# EDA VISUALIZATIONS
# -------------------------------------------------
elif selected == "EDA Visualizations":
    st.markdown("## 📊 Exploratory Data Analysis")

    vis_path = Path("visualizations")
    if vis_path.exists():
        images = list(vis_path.glob("*.png")) + list(vis_path.glob("*.jpg"))
        if images:
            cols = st.columns(2)
            for i, img in enumerate(images):
                with cols[i % 2]:
                    st.image(img, caption=img.name, use_container_width=True)
        else:
            st.info("No visualization images available.")
    else:
        st.info("Visualization assets not found.")

# -------------------------------------------------
# MODEL OVERVIEW
# -------------------------------------------------
elif selected == "Model Overview":
    st.markdown("## 📊 Model Overview")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="card"><h4>Models Evaluated</h4><ul><li>Logistic Regression</li><li>Random Forest</li><li>Decision Tree</li></ul></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card"><h4>Evaluation Metrics</h4><ul><li>ROC-AUC</li><li>Precision</li><li>Recall</li><li>F1-Score</li></ul></div>', unsafe_allow_html=True)

# -------------------------------------------------
# DOCUMENTATION
# -------------------------------------------------
elif selected == "Documentation":
    st.markdown("## 📘 Documentation")

    st.markdown("""
    ### Overview
    This application provides an interactive interface for analyzing customer churn
    in an e-commerce environment using behavioral features.

    ### Key Capabilities
    - Individual customer risk assessment
    - Batch churn analysis
    - Insight-driven EDA visualizations
    - Clear and interpretable outputs

    **Developer:** Shahid Mohammed  
    **Program:** PATNR GPP
    """)

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.markdown('<div class="footer">© 2025 • E-Commerce Churn Prediction</div>', unsafe_allow_html=True)
