import streamlit as st
import pandas as pd

# -----------------------------------
# Page Config
# -----------------------------------
st.set_page_config(
    page_title="E-Commerce Churn Prediction",
    page_icon="📉",
    layout="wide"
)

# -----------------------------------
# Sidebar
# -----------------------------------
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

    st.markdown("""
    ### Project Overview
    This project demonstrates an **end-to-end machine learning pipeline**
    for predicting customer churn in an e-commerce platform.

    ### Note on Deployment
    - Raw data and trained models are **excluded from the public repository**
    - This deployment focuses on **pipeline design, UI, and reproducibility**
    """)

    st.success("Application deployed successfully")

# -----------------------------------
# SINGLE PREDICTION (UI DEMO)
# -----------------------------------
elif page == "🔍 Single Customer Prediction":
    st.header("🔍 Single Customer Churn Prediction")

    st.info(
        "ℹ️ Prediction is disabled in this public deployment.\n\n"
        "This page demonstrates the **input schema and UI design**."
    )

    # Static demo features (SAFE)
    demo_features = [
        "Recency",
        "Frequency",
        "Monetary",
        "Avg_Order_Value",
        "Purchase_Count"
    ]

    input_data = {}
    cols = st.columns(2)
    for i, f in enumerate(demo_features):
        with cols[i % 2]:
            input_data[f] = st.number_input(f, value=0.0)

    st.button("Predict Churn Risk", disabled=True)

# -----------------------------------
# BATCH PREDICTION (UI DEMO)
# -----------------------------------
elif page == "📂 Batch Prediction":
    st.header("📂 Batch Prediction")

    st.info(
        "ℹ️ Batch prediction is disabled in public deployment.\n\n"
        "This section demonstrates how CSV uploads would be handled."
    )

    st.file_uploader("Upload CSV", type=["csv"], disabled=True)

# -----------------------------------
# DOCUMENTATION
# -----------------------------------
elif page == "📘 Documentation":
    st.header("📘 Documentation")

    st.markdown("""
    ### What This Project Demonstrates
    - Data preprocessing and feature engineering
    - Model training and evaluation
    - Streamlit-based deployment
    - Production constraints handling

    ### Why Models Are Not Included
    - Data privacy
    - Repository size limits
    - Security best practices

    ### Program
    **PATNR GPP – E-Commerce Churn Prediction**
    """)
