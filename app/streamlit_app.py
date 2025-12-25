# -----------------------------------
# Streamlit App: E-Commerce Churn
# -----------------------------------

import streamlit as st
import pandas as pd
import plotly.express as px
import json
from app.predict import predict, predict_proba, get_feature_names

# -----------------------------------
# Page Configuration
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
        "📈 Model Performance",
        "📘 Documentation"
    ]
)

# -----------------------------------
# HOME
# -----------------------------------
if page == "🏠 Home":
    st.title("📉 E-Commerce Customer Churn Prediction")

    st.markdown("""
    ### 🔍 What is Customer Churn?
    Churn refers to customers who stop purchasing for **90 consecutive days**.

    ### 🎯 Objective
    Predict churn probability using historical transaction behavior
    to help businesses run **targeted retention campaigns**.

    ### 🚀 Features
    - Single customer churn prediction
    - Batch CSV predictions
    - Model performance dashboard
    - Business-ready insights
    """)

    st.success("✅ Application deployed successfully")

# -----------------------------------
# SINGLE PREDICTION
# -----------------------------------
elif page == "🔍 Single Customer Prediction":
    st.header("🔍 Single Customer Churn Prediction")

    feature_names = get_feature_names()
    input_data = {}

    cols = st.columns(2)
    for i, feature in enumerate(feature_names):
        with cols[i % 2]:
            input_data[feature] = st.number_input(
                feature,
                value=0.0
            )

    if st.button("Predict Churn Risk"):
        prob = predict_proba(input_data)[0]
        label = predict(input_data)[0]

        st.subheader("📊 Prediction Result")
        st.metric("Churn Probability", f"{prob:.2%}")

        if label == 1:
            st.error("⚠️ High Risk: Customer likely to churn")
        else:
            st.success("✅ Low Risk: Customer likely to stay")

# -----------------------------------
# BATCH PREDICTION
# -----------------------------------
elif page == "📂 Batch Prediction":
    st.header("📂 Batch Prediction")

    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)

        probs = predict_proba(df)
        preds = predict(df)

        df["Churn_Probability"] = probs
        df["Churn_Prediction"] = preds

        st.success("✅ Predictions generated")
        st.dataframe(df.head())

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            "⬇️ Download Results",
            csv,
            "churn_predictions.csv",
            "text/csv"
        )

# -----------------------------------
# MODEL PERFORMANCE
# -----------------------------------
elif page == "📈 Model Performance":
    st.header("📈 Model Performance")

    try:
        with open("models/model_metrics.json", "r") as f:
            metrics = json.load(f)

        df = pd.DataFrame(metrics).T
        st.dataframe(df)

        fig = px.bar(
            df.reset_index(),
            x="index",
            y="roc_auc",
            title="ROC-AUC Comparison"
        )
        st.plotly_chart(fig)

    except Exception:
        st.warning("Model metrics not available")

# -----------------------------------
# DOCUMENTATION
# -----------------------------------
elif page == "📘 Documentation":
    st.header("📘 Documentation")

    st.markdown("""
    ### 📌 How to Use
    - Use **Single Prediction** for individual customers
    - Use **Batch Prediction** for CSV uploads
    - Interpret churn probabilities for business action

    ### ⚙️ Technical Summary
    - Dataset: E-Commerce Transactions
    - Churn Window: 90 days
    - Features: RFM + Behavioral
    - Final Model: Random Forest

    ### 📈 Business Value
    - Reduce churn
    - Increase retention ROI
    - Focus on high-risk customers

    ---
    **Developer:** Shahid Mohammed  
    **Program:** PATNR GPP
    """)
