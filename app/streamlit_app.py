import streamlit as st
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
# Custom CSS (Dark-mode safe)
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
# Session State Navigation
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
    st.markdown("**PATNR GPP – End-to-End Machine Learning Project**")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="card"><h4>🎯 Objective</h4><p>Identify customers likely to churn using behavioral data.</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card"><h4>🧠 ML Pipeline</h4><p>EDA → Feature Engineering → Model Training → Evaluation.</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="card"><h4>🚀 Deployment</h4><p>Streamlit Cloud demo with production-aware constraints.</p></div>', unsafe_allow_html=True)

    st.info(
        "🔒 **Note on Deployment**  \n"
        "Raw data and trained model artifacts are excluded from the public repository "
        "to follow data privacy and repository size best practices."
    )

# -------------------------------------------------
# SINGLE CUSTOMER
# -------------------------------------------------
elif selected == "Single Customer":
    st.markdown("## 👤 Single Customer Churn Prediction")

    st.info(
        "ℹ️ This is a **demo prediction** using rule-based logic.\n\n"
        "In production, this would be powered by a trained ML model."
    )

    col1, col2 = st.columns(2)

    with col1:
        recency = st.number_input("Recency (days since last purchase)", min_value=0, value=30)
        frequency = st.number_input("Frequency (total purchases)", min_value=0, value=5)
        monetary = st.number_input("Monetary Value (total spend)", min_value=0.0, value=500.0)

    with col2:
        avg_order = st.number_input("Average Order Value", min_value=0.0, value=100.0)
        recent_purchases = st.number_input("Purchases in last 90 days", min_value=0, value=2)

    if st.button("Predict Churn Risk"):
        # --- SAFE MOCK LOGIC ---
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
            st.error("⚠️ High Risk: Customer is likely to churn")
        elif churn_prob > 0.3:
            st.warning("🟡 Medium Risk: Customer may churn")
        else:
            st.success("✅ Low Risk: Customer likely to stay")

        st.caption(
            "⚠️ Demo prediction — values are illustrative, not ML-based."
        )


# -------------------------------------------------
# BATCH PREDICTION
# -------------------------------------------------
elif selected == "Batch Prediction":
    st.markdown("## 📂 Batch Customer Churn Prediction")

    st.info(
        "ℹ️ Demo batch prediction using rule-based scoring.\n\n"
        "Upload a CSV with customer features to simulate churn analysis."
    )

    uploaded = st.file_uploader("Upload customer CSV file", type=["csv"])

    if uploaded:
        try:
            df = pd.read_csv(uploaded)

            # --- SAFE MOCK CHURN SCORE ---
            df["Churn_Probability"] = (
                df.iloc[:, 0].rank(pct=True) * 0.4 +
                df.iloc[:, 1].rank(pct=True) * 0.3 +
                df.iloc[:, 2].rank(pct=True) * 0.3
            ).clip(0, 1)

            df["Churn_Risk"] = df["Churn_Probability"].apply(
                lambda x: "High" if x > 0.6 else "Medium" if x > 0.3 else "Low"
            )

            st.success("✅ Batch prediction completed (demo)")
            st.dataframe(df.head())

            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                "⬇️ Download Predictions",
                data=csv,
                file_name="churn_predictions_demo.csv",
                mime="text/csv"
            )

            st.caption("⚠️ Demo-only results for UI and workflow demonstration.")

        except Exception as e:
            st.error(f"Failed to process file: {e}")


# -------------------------------------------------
# EDA VISUALIZATIONS
# -------------------------------------------------
elif selected == "EDA Visualizations":
    st.markdown("## 📊 Exploratory Data Analysis (EDA)")
    st.markdown("Below are key insights generated during exploratory analysis.")

    vis_path = Path("visualizations")

    if vis_path.exists():
        images = list(vis_path.glob("*.png")) + list(vis_path.glob("*.jpg"))

        if images:
            cols = st.columns(2)
            for i, img in enumerate(images):
                with cols[i % 2]:
                    st.image(img, caption=img.name, use_container_width=True)
        else:
            st.info("No visualization images found in the visualizations folder.")
    else:
        st.warning(
            "Visualization folder not found.\n\n"
            "This is expected if images were generated locally and excluded from GitHub."
        )

# -------------------------------------------------
# MODEL OVERVIEW
# -------------------------------------------------
elif selected == "Model Overview":
    st.markdown("## 📊 Model Overview")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="card"><h4>Models Trained</h4><ul><li>Logistic Regression</li><li>Random Forest</li><li>Decision Tree</li></ul></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card"><h4>Evaluation Metrics</h4><ul><li>ROC-AUC</li><li>Precision</li><li>Recall</li><li>F1-Score</li></ul></div>', unsafe_allow_html=True)

# -------------------------------------------------
# DOCUMENTATION
# -------------------------------------------------
elif selected == "Documentation":
    st.markdown("## 📘 Documentation")

    st.markdown("""
    ### Project Summary
    This project demonstrates a complete **machine learning lifecycle**
    for predicting customer churn in an e-commerce environment.

    ### Key Highlights
    - Feature engineering using customer behavior
    - Model comparison and evaluation
    - Streamlit deployment with real-world constraints
    - Clean, professional UI for demonstration

    ### Program
    **PATNR GPP – E-Commerce Churn Prediction**

    **Developer:** Shahid Mohammed
    """)

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.markdown('<div class="footer">© 2025 • PATNR GPP • Streamlit Deployment Demo</div>', unsafe_allow_html=True)
