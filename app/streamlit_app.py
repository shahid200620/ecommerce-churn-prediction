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

    st.warning(
        "Prediction is disabled in this public deployment.\n\n"
        "This page demonstrates the **input schema and UI design**."
    )

    col1, col2 = st.columns(2)
    with col1:
        st.number_input("Recency (days since last purchase)", 0)
        st.number_input("Frequency (total purchases)", 0)
        st.number_input("Monetary Value (total spend)", 0.0)
    with col2:
        st.number_input("Average Order Value", 0.0)
        st.number_input("Purchases in last 90 days", 0)

    st.button("Predict Churn Risk", disabled=True)

# -------------------------------------------------
# BATCH PREDICTION
# -------------------------------------------------
elif selected == "Batch Prediction":
    st.markdown("## 📂 Batch Prediction")

    st.warning(
        "Batch prediction is disabled in this public deployment.\n\n"
        "This section demonstrates how CSV uploads would be handled in production."
    )

    st.file_uploader("Upload customer CSV file", type=["csv"], disabled=True)

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
