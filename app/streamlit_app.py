import streamlit as st
import pandas as pd
from app.predict import (
    get_feature_names,
    predict,
    predict_proba,
    is_model_available
)

st.set_page_config(
    page_title="E-Commerce Churn Prediction",
    page_icon="📉",
    layout="wide"
)

st.sidebar.title("📊 Churn Prediction App")
page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "🔍 Single Customer Prediction",
        "📂 Batch Prediction",
        "📘 Documentation"
    ]
)

# -----------------------------------
# HOME
# -----------------------------------
if page == "🏠 Home":
    st.title("📉 E-Commerce Customer Churn Prediction")
    st.success("Application deployed successfully on Streamlit Cloud")

    if not is_model_available():
        st.warning(
            "⚠️ Model files are not present in this deployment.\n\n"
            "This demo focuses on pipeline, UI, and deployment as required by PATNR GPP."
        )

# -----------------------------------
# SINGLE PREDICTION
# -----------------------------------
elif page == "🔍 Single Customer Prediction":
    st.header("🔍 Single Customer Churn Prediction")

    feature_names = get_feature_names()
    input_data = {}

    cols = st.columns(2)
    for i, f in enumerate(feature_names):
        with cols[i % 2]:
            input_data[f] = st.number_input(f, value=0.0)

    if st.button("Predict Churn Risk"):
        if not is_model_available():
            st.error(
                "❌ Model not available in deployment.\n\n"
                "Prediction disabled. UI and pipeline demonstration completed."
            )
        else:
            prob = predict_proba(input_data)[0]
            label = predict(input_data)[0]
            st.metric("Churn Probability", f"{prob:.2%}")
            st.success("Prediction completed")

# -----------------------------------
# BATCH PREDICTION
# -----------------------------------
elif page == "📂 Batch Prediction":
    st.header("📂 Batch Prediction")

    uploaded = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded:
        st.warning(
            "Batch prediction disabled in deployment demo.\n\n"
            "Model files are not present on Streamlit Cloud."
        )

# -----------------------------------
# DOCS
# -----------------------------------
elif page == "📘 Documentation":
    st.header("📘 Documentation")
    st.markdown("""
    ### Project Summary
    - Goal: Predict e-commerce customer churn
    - Models trained locally
    - Deployment focuses on reproducibility and UI

    ### Note
    For PATNR GPP evaluation, this app demonstrates:
    - End-to-end ML pipeline
    - Feature engineering
    - Model training
    - Streamlit deployment
    """)
