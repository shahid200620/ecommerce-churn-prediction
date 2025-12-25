import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
import json
import joblib
import plotly.express as px

from app.predict import predict, predict_proba


# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="E-Commerce Churn Prediction",
    page_icon="📉",
    layout="wide"
)


# -----------------------------
# Sidebar Navigation
# -----------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    [
        "Home",
        "Single Prediction",
        "Batch Prediction",
        "Model Dashboard",
        "Documentation"
    ]
)


# -----------------------------
# Cached Loaders
# -----------------------------
@st.cache_resource
def load_model():
    return joblib.load("models/best_model.pkl")


@st.cache_resource
def load_feature_names():
    with open("data/processed/feature_names.json", "r") as f:
        return json.load(f)


# -----------------------------
# HOME
# -----------------------------
if page == "Home":
    st.title("📉 E-Commerce Customer Churn Prediction")

    st.markdown("""
    ### Project Overview
    This application predicts whether an e-commerce customer is likely to **churn**
    (stop purchasing in the next 3 months).

    ### What this app provides:
    - 🔹 Single customer churn prediction
    - 🔹 Batch churn prediction using CSV upload
    - 🔹 Model performance dashboard
    - 🔹 Business-ready insights

    **Model used:** Gradient Boosting (XGBoost / equivalent)  
    **Primary metric:** ROC-AUC  
    """)

    st.success("Use the sidebar to navigate through the application.")


# -----------------------------
# SINGLE PREDICTION
# -----------------------------
elif page == "Single Prediction":
    st.header("🔍 Single Customer Churn Prediction")

    feature_names = load_feature_names()

    input_data = {}
    cols = st.columns(2)

    for i, feature in enumerate(feature_names):
        with cols[i % 2]:
            input_data[feature] = st.number_input(
                feature,
                value=0.0
            )

    if st.button("Predict Churn Risk"):
        try:
            prob = predict_proba(input_data)[0]
            label = predict(input_data)[0]

            st.subheader("Prediction Result")
            st.write(f"**Churn Probability:** {prob:.2%}")

            if label == 1:
                st.error("⚠️ High Risk: Customer is likely to churn")
            else:
                st.success("✅ Low Risk: Customer is likely to stay")

        except Exception as e:
            st.error(f"Prediction failed: {e}")


# -----------------------------
# BATCH PREDICTION
# -----------------------------
elif page == "Batch Prediction":
    st.header("📂 Batch Churn Prediction")

    uploaded_file = st.file_uploader(
        "Upload CSV file with customer features",
        type=["csv"]
    )

    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)

            probs = predict_proba(df)
            preds = predict(df)

            df["Churn_Probability"] = probs
            df["Churn_Prediction"] = preds

            st.success("Predictions generated successfully")
            st.dataframe(df.head())

            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                "Download Predictions",
                csv,
                "churn_predictions.csv",
                "text/csv"
            )

        except Exception as e:
            st.error(f"Batch prediction failed: {e}")


# -----------------------------
# MODEL DASHBOARD
# -----------------------------
elif page == "Model Dashboard":
    st.header("📊 Model Performance Dashboard")

    metrics = {
        "ROC-AUC": 0.78,
        "Precision": 0.75,
        "Recall": 0.68,
        "F1-Score": 0.71
    }

    st.subheader("Model Metrics")
    st.json(metrics)

    fig = px.bar(
        x=list(metrics.keys()),
        y=list(metrics.values()),
        labels={"x": "Metric", "y": "Score"},
        title="Model Performance Metrics"
    )
    st.plotly_chart(fig)


# -----------------------------
# DOCUMENTATION
# -----------------------------
elif page == "Documentation":
    st.header("📘 Documentation")

    st.markdown("""
    ### How to use this app
    1. Navigate using the sidebar
    2. Enter customer features for single prediction
    3. Upload CSV for batch prediction
    4. Review results and download predictions

    ### Notes
    - Predictions are based on historical transaction behavior
    - Probabilities closer to 1 indicate higher churn risk

    ### Contact
    **Developer:** Shahid Mohammed  
    **Project:** PATNR GPP – E-Commerce Churn Prediction
    """)
