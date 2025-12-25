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
# Custom CSS (Dark-mode safe)
# -------------------------------------------------
st.markdown("""
<style>
/* Main background */
.stApp {
    background-color: #0f172a;
}

/* Headings */
h1, h2, h3, h4 {
    color: #f8fafc;
}

/* Paragraph text */
p, li, span {
    color: #cbd5f5;
}

/* Cards */
.card {
    background: #111827;
    padding: 1.5rem;
    border-radius: 14px;
    border: 1px solid #1e293b;
    height: 100%;
}

/* Buttons */
.stButton button {
    background: linear-gradient(90deg, #6366f1, #22d3ee);
    color: black;
    border-radius: 10px;
    font-weight: 600;
}

/* Top nav */
.nav {
    display: flex;
    gap: 1rem;
    margin-bottom: 1.5rem;
}
.nav a {
    text-decoration: none;
    padding: 0.4rem 1rem;
    border-radius: 8px;
    color: #e5e7eb;
    background-color: #1e293b;
}
.nav a:hover {
    background-color: #334155;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Top Navigation
# -------------------------------------------------
pages = {
    "🏠 Home": "home",
    "👤 Single Customer": "single",
    "📂 Batch Prediction": "batch",
    "📊 Model Overview": "model",
    "📘 Documentation": "docs"
}

query_params = st.query_params
current_page = query_params.get("page", "home")

nav_html = '<div class="nav">'
for name, key in pages.items():
    nav_html += f'<a href="?page={key}">{name}</a>'
nav_html += '</div>'

st.markdown(nav_html, unsafe_allow_html=True)

# -------------------------------------------------
# HOME
# -------------------------------------------------
if current_page == "home":
    st.markdown("## 📉 E-Commerce Customer Churn Prediction")
    st.markdown("**PATNR GPP – End-to-End Machine Learning Project**")

    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="card"><h4>🎯 Objective</h4><p>Identify customers likely to churn using behavioral insights.</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card"><h4>🧠 ML Pipeline</h4><p>EDA → Feature Engineering → Model Training → Evaluation.</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="card"><h4>🚀 Deployment</h4><p>Streamlit Cloud demo with production-aware constraints.</p></div>', unsafe_allow_html=True)

    st.markdown("---")
    st.info(
        "🔒 **Note on Deployment**  \n"
        "Raw data and trained models are excluded from the public repository "
        "to follow data privacy and repository size best practices. "
        "This deployment demonstrates **architecture, UI, and ML workflow understanding**."
    )

# -------------------------------------------------
# SINGLE CUSTOMER
# -------------------------------------------------
elif current_page == "single":
    st.markdown("## 👤 Single Customer Churn Prediction")
    st.warning(
        "Prediction is disabled in this public demo.\n\n"
        "This page showcases the **input design and business interpretation**."
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
elif current_page == "batch":
    st.markdown("## 📂 Batch Prediction")
    st.warning(
        "Batch prediction is disabled in this public deployment.\n\n"
        "This section demonstrates how CSV uploads would be handled in production."
    )
    st.file_uploader("Upload customer CSV file", type=["csv"], disabled=True)

# -------------------------------------------------
# MODEL OVERVIEW
# -------------------------------------------------
elif current_page == "model":
    st.markdown("## 📊 Model Overview")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="card"><h4>Models Trained</h4><ul><li>Logistic Regression</li><li>Random Forest</li><li>Decision Tree</li></ul></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card"><h4>Evaluation Metrics</h4><ul><li>ROC-AUC</li><li>Precision</li><li>Recall</li><li>F1-Score</li></ul></div>', unsafe_allow_html=True)

# -------------------------------------------------
# DOCUMENTATION
# -------------------------------------------------
elif current_page == "docs":
    st.markdown("## 📘 Documentation")

    st.markdown("""
    ### Project Summary
    This project demonstrates a complete **machine learning lifecycle** for
    predicting customer churn in an e-commerce setting.

    ### Key Learnings
    - Feature engineering using customer behavior
    - Model comparison & evaluation
    - Deployment constraints in real-world ML systems
    - Building stable, user-friendly ML demos

    ### Program
    **PATNR GPP – E-Commerce Churn Prediction**

    **Developer:** Shahid Mohammed
    """)

st.markdown("<br><p style='text-align:center;color:#94a3b8;'>© 2025 • PATNR GPP • Streamlit Deployment Demo</p>", unsafe_allow_html=True)
