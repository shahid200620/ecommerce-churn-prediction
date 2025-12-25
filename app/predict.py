"""
Prediction API for E-Commerce Customer Churn Model
"""

import joblib
import pandas as pd
import json
import os


# -----------------------------
# Paths (RELATIVE – Docker safe)
# -----------------------------
MODEL_PATH = "models/best_model.pkl"
SCALER_PATH = "models/scaler.pkl"
FEATURES_PATH = "data/processed/feature_names.json"


# -----------------------------
# Loaders
# -----------------------------
def load_model():
    """
    Load trained churn prediction model
    """
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("Model file not found")

    return joblib.load(MODEL_PATH)


def load_scaler():
    """
    Load feature scaler
    """
    if not os.path.exists(SCALER_PATH):
        raise FileNotFoundError("Scaler file not found")

    return joblib.load(SCALER_PATH)


def load_feature_names():
    """
    Load feature names in correct order
    """
    if not os.path.exists(FEATURES_PATH):
        raise FileNotFoundError("Feature names file not found")

    with open(FEATURES_PATH, "r") as f:
        return json.load(f)


# -----------------------------
# Preprocessing
# -----------------------------
def preprocess_input(input_data):
    """
    Preprocess single or batch input data

    Args:
        input_data (dict or pd.DataFrame)

    Returns:
        pd.DataFrame: processed input
    """
    feature_names = load_feature_names()

    if isinstance(input_data, dict):
        df = pd.DataFrame([input_data])
    elif isinstance(input_data, pd.DataFrame):
        df = input_data.copy()
    else:
        raise ValueError("Input must be dict or DataFrame")

    # Ensure all required features exist
    for col in feature_names:
        if col not in df.columns:
            df[col] = 0

    # Reorder columns
    df = df[feature_names]

    # Scale numerical features
    scaler = load_scaler()
    df_scaled = pd.DataFrame(
        scaler.transform(df),
        columns=feature_names
    )

    return df_scaled


# -----------------------------
# Prediction
# -----------------------------
def predict(input_data):
    """
    Predict churn label (0 or 1)
    """
    model = load_model()
    processed = preprocess_input(input_data)
    return model.predict(processed)


def predict_proba(input_data):
    """
    Predict churn probability
    """
    model = load_model()
    processed = preprocess_input(input_data)
    return model.predict_proba(processed)[:, 1]
