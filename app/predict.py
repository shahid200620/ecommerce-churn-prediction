# -----------------------------------
# Prediction API for Churn Model
# -----------------------------------

import joblib
import pandas as pd
from pathlib import Path

# Root directory
ROOT_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = ROOT_DIR / "models" / "best_model.pkl"
SCALER_PATH = ROOT_DIR / "models" / "scaler.pkl"


def load_model():
    """Load trained ML model"""
    if not MODEL_PATH.exists():
        raise FileNotFoundError("Model file not found")
    return joblib.load(MODEL_PATH)


def load_scaler():
    """Load feature scaler"""
    if not SCALER_PATH.exists():
        raise FileNotFoundError("Scaler file not found")
    return joblib.load(SCALER_PATH)


def get_feature_names():
    """
    Extract feature names directly from the trained model
    This avoids dependency on data folder
    """
    model = load_model()

    if hasattr(model, "feature_names_in_"):
        return list(model.feature_names_in_)
    else:
        raise RuntimeError("Model does not expose feature names")


def preprocess_input(input_data):
    """
    Prepare input data for prediction
    Supports single dict or batch DataFrame
    """
    feature_names = get_feature_names()

    # Single customer (dict)
    if isinstance(input_data, dict):
        df = pd.DataFrame([input_data])

    # Batch (DataFrame)
    elif isinstance(input_data, pd.DataFrame):
        df = input_data.copy()

    else:
        raise ValueError("Input must be dict or DataFrame")

    # Ensure correct feature order
    df = df.reindex(columns=feature_names, fill_value=0)

    scaler = load_scaler()
    df_scaled = scaler.transform(df)

    return df_scaled


def predict(input_data):
    """Return churn class (0 or 1)"""
    model = load_model()
    X = preprocess_input(input_data)
    return model.predict(X)


def predict_proba(input_data):
    """Return churn probability"""
    model = load_model()
    X = preprocess_input(input_data)
    return model.predict_proba(X)[:, 1]
