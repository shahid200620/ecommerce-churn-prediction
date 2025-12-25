import streamlit as st

# -------------------------------------------------
# Page Config
# -------------------------------------------------
st.set_page_config(
    page_title="E-Commerce Churn Prediction",
    page_icon="📉",
    layout="wide"
)

# -------------------------------------------------
# Custom CSS (SAFE – no JS, no hacks)
# -------------------------------------------------
st.markdown("""
<style>
.big-title {
    font-size: 2.4rem;
    font-weight: 700;
    color: #1f2937;
}
.subtle {
    color: #6b7280;
    font-size: 1rem;
}
.card {
    padding: 1.2rem;
    border-radius: 12px;
    background-color: #f9fafb;
    border: 1px solid #e5e7eb;
}
.metric {
    font-size: 1.8rem;
    font-weight: 600;
}
.footer {
    color: #6b7280;
    font-size: 0.9rem;
    margin-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Sidebar
# -------------------------------------------------
st.sidebar.title("📊 Churn Prediction")
st.sidebar.markdown("Navigate through the app")

page = st.sidebar.radio(
    "",
    [
        "🏠 Home",
        "🔍 Single Customer",
        "📂 Batch Prediction",
        "📘 Documentation"
    ]
)

# -------------------------------------------------
# HOME
# -------------------------------------------------
if page == "🏠 Home":
    st.markdown('<div class="big-title">📉 E-Commerce Customer Churn Prediction</div>', unsafe_allow_html=True)
    st.markdown('<p class="subtle">PATNR GPP – End-to-End Machine Learning Project</p>', unsafe_allow_html=True)

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="card"><b>🎯 Objective</b><br>Predict customers likely to stop purchasing using behavioral data.</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card"><b🧠> ML Pipeline</b><br>EDA → Feature Engineering → Model Training → Deployment.</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card"><b>🚀 Deployment</b><br>Streamlit Cloud demo with production constraints.</div>', unsafe_allow_html=True)

    st.markdown("---")

    st.info(
        "ℹ️ **Note on Deployment**\n\n"
        "To follow best practices for data privacy and repository size limits, "
        "raw data and trained model artifacts are excluded from the public repository. "
        "This deployment focuses on **pipeline design, UI, and reproducibility**."
    )

# -------------------------------------------------
# SINGLE CUSTOMER (UI DEMO)
# -------------------------------------------------
elif page == "🔍 Single Customer":
    st.markdown('<div class="big-title">🔍 Single Customer Churn Prediction</div>', unsafe_allow_html=True)
    st.markdown('<p class="subtle">Demo interface for individual customer analysis</p>', unsafe_allow_html=True)

    st.warning(
        "⚠️ **Prediction Disabled (Public Deployment)**\n\n"
        "This section demonstrates the **input schema and UI design**. "
        "Live predictions require private model artifacts which are intentionally excluded."
    )

    demo_features = {
        "Recency (days since last purchase)": 0,
        "Frequency (total purchases)": 0,
        "Monetary Value (total spend)": 0.0,
        "Average Order Value": 0.0,
        "Purchase Count (last 90 days)": 0
    }

    col1, col2 = st.columns(2)
    for i, (feature, default) in enumerate(demo_features.items()):
        with (col1 if i % 2 == 0 else col2):
            st.number_input(feature, value=default)

    st.button("Predict Churn Risk", disabled=True)

# -------------------------------------------------
# BATCH PREDICTION (UI DEMO)
# -------------------------------------------------
elif page == "📂 Batch Prediction":
    st.markdown('<div class="big-title">📂 Batch Prediction</div>', unsafe_allow_html=True)
    st.markdown('<p class="subtle">Upload-based churn analysis (demo)</p>', unsafe_allow_html=True)

    st.warning(
        "⚠️ Batch prediction is disabled in this public deployment.\n\n"
        "This section demonstrates how CSV uploads would be handled in production."
    )

    st.file_uploader("Upload customer CSV file", type=["csv"], disabled=True)

# -------------------------------------------------
# DOCUMENTATION
# -------------------------------------------------
elif page == "📘 Documentation":
    st.markdown('<div class="big-title">📘 Documentation</div>', unsafe_allow_html=True)

    st.markdown("""
    ### 📌 Project Overview
    This project implements a complete **machine learning workflow**
    to predict customer churn in an e-commerce environment.

    ### 🔧 Key Components
    - Data Cleaning & Feature Engineering
    - Exploratory Data Analysis (EDA)
    - Model Training & Evaluation
    - Streamlit Deployment

    ### 🔒 Why Data & Models Are Excluded
    - Data privacy considerations  
    - Repository size constraints  
    - Security best practices  

    ### 🎓 Program
    **PATNR GPP – E-Commerce Churn Prediction**

    ---
    **Developer:** Shahid Mohammed
    """)

# -------------------------------------------------
# Footer
# -------------------------------------------------
st.markdown(
    '<div class="footer">© 2025 • PATNR GPP • Streamlit Deployment Demo</div>',
    unsafe_allow_html=True
)
