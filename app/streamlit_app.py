# -----------------------------------
# Streamlit App: E-Commerce Churn
# -----------------------------------

from pathlib import Path
import sys
import os
import json
import joblib
import pandas as pd
import streamlit as st
import plotly.express as px

# -----------------------------------
# Project root (IMPORTANT for Streamlit Cloud)
# -----------------------------------
ROOT_DIR = Path(__file__).resolve().parent.parent

# Fix import path
sys.path.append(str(ROOT_DIR))

from app.predict import predict, predict_proba


# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(
    page_title="E-Commerce Churn Prediction",
    page_icon="📉",
    layout="wide"
)


# -----------------------------------
# Cached Loaders
# -----------------------------------
@st.cache_resource
def load_feature_names():
    feature_path = ROOT_DIR / "data" / "processed" / "feature_names.json"

    if not feature_path.exists():
        st.error("❌ feature_names.json not found. Please check deployment files.")
        return []

    with open(feature_path, "r") as f:
        return json.load(f)


@st.cache_resource
def load_metrics():
    metrics_path = ROOT_DIR / "models" / "model_metrics.json"

    if not metrics_path.exists():
        return {}

    with open(metrics_path, "r") as f:
        return json.load(f)


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
        "📈 Model Performance",
        "📘 Documentation"
    ]
)


# -----------------------------------
# HOME PAGE
# -----------------------------------
if page == "🏠 Home":
    st.title("📉 E-Commerce Customer Churn Prediction")

    st.markdown("""
    ### 🔍 What is Customer Churn?
    Customer churn refers to customers who stop purchasing from the platform
    for a significant period (here, **90 days**).

    ### 🎯 Project Objective
    This application predicts the **probability of customer churn** using
    historical transaction behavior and machine learning models.

    ### 🚀 What this app can do
    - Predict churn risk for **individual customers**
    - Perform **bulk predictions** using CSV uploads
    - Visualize **model performance**
    - Support **business decision-making**

    ### 🧠 Model Highlights
    - Models trained: Logistic Regression, Random Forest  
    - Selected model: **Random Forest**
    - Key metric: **ROC-AUC**

    ---
    👉 Use the **sidebar** to explore the app.
    """)

    st.success("✅ Application is ready for use")


# -----------------------------------
# SINGLE CUSTOMER PREDICTION
# -----------------------------------
elif page == "🔍 Single Customer Prediction":
    st.header("🔍 Single Customer Churn Prediction")

    st.markdown("""
    Enter customer feature values below to predict the **likelihood of churn**.
    """)

    feature_names = load_feature_names()

    # 🔒 Safety check (FIXED INDENTATION)
    if not feature_names:
        st.stop()

    input_data = {}

    cols = st.columns(2)
    for i, feature in enumerate(feature_names):
        with cols[i % 2]:
            input_data[feature] = st.number_input(
                label=feature,
                value=0.0
            )

    if st.button("Predict Churn Risk"):
        try:
            prob = predict_proba(input_data)[0]
            label = predict(input_data)[0]

            st.subheader("📊 Prediction Result")
            st.metric(
                label="Churn Probability",
                value=f"{prob:.2%}"
            )

            if label == 1:
                st.error("⚠️ High Risk: Customer is likely to churn")
            else:
                st.success("✅ Low Risk: Customer is likely to stay")

        except Exception as e:
            st.error(f"Prediction failed: {e}")


# -----------------------------------
# BATCH PREDICTION
# -----------------------------------
elif page == "📂 Batch Prediction":
    st.header("📂 Batch Customer Churn Prediction")

    st.markdown("""
    Upload a CSV file containing customer features.
    The file must follow the **same structure used during training**.
    """)

    uploaded_file = st.file_uploader(
        "Upload CSV file",
        type=["csv"]
    )

    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)

            probs = predict_proba(df)
            preds = predict(df)

            df["Churn_Probability"] = probs
            df["Churn_Prediction"] = preds

            st.success("✅ Predictions generated successfully")
            st.dataframe(df.head())

            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="⬇️ Download Predictions",
                data=csv,
                file_name="churn_predictions.csv",
                mime="text/csv"
            )

        except Exception as e:
            st.error(f"Batch prediction failed: {e}")


# -----------------------------------
# MODEL PERFORMANCE
# -----------------------------------
elif page == "📈 Model Performance":
    st.header("📈 Model Performance Dashboard")

    metrics = load_metrics()

    if metrics:
        metrics_df = pd.DataFrame(metrics).T
        st.subheader("📊 Evaluation Metrics")
        st.dataframe(metrics_df)

        if "roc_auc" in metrics_df.columns:
            fig = px.bar(
                metrics_df.reset_index(),
                x="index",
                y="roc_auc",
                labels={"index": "Model", "roc_auc": "ROC-AUC"},
                title="ROC-AUC Comparison"
            )
            st.plotly_chart(fig)
    else:
        st.warning("Model metrics not available.")


# -----------------------------------
# DOCUMENTATION
# -----------------------------------
elif page == "📘 Documentation":
    st.header("📘 Documentation")

    st.markdown("""
    ### 📌 How to Use This App
    1. Navigate using the sidebar
    2. Choose **Single Prediction** for individual customers
    3. Choose **Batch Prediction** for CSV uploads
    4. Review probabilities and download results

    ### ⚙️ Technical Details
    - Data source: Transaction-level e-commerce data
    - Churn definition: No purchase in last **90 days**
    - Feature engineering: RFM + behavioral metrics
    - Final model: Random Forest

    ### 📈 Business Value
    - Early identification of at-risk customers
    - Targeted retention campaigns
    - Improved customer lifetime value

    ---
    **Developer:** Shahid Mohammed  
    **Program:** PATNR GPP  
    **Project:** E-Commerce Customer Churn Prediction
    """)
