# -----------------------------------
# Prediction API for Churn Model
# -----------------------------------

import joblib
import pandas as pd
from pathlib import Path

# Project root
ROOT_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = ROOT_DIR / "models"


def load_model():
    """
    Load the best available trained model.
    Priority:
    1. best_model.pkl
    2. random_forest.pkl
    3. logistic_regression.pkl
    """

    candidates = [
        "best_model.pkl",
        "random_forest.pkl",
        "logistic_regression.pkl",
        "decision_tree.pkl"
    ]

    for name in candidates:
        path = MODELS_DIR / name
        if path.exists():
            return joblib.load(path)

    raise FileNotFoundError(
        "No trained model found in models/. "
        "Expected one of: best_model.pkl, random_forest.pkl, logistic_regression.pkl"
    )


def load_scaler():
    scaler_path = MODELS_DIR / "scaler.pkl"
    if not scaler_path.exists():
        raise FileNotFoundError("Scaler file not found in models/")
    return joblib.load(scaler_path)


def get_feature_names():
    """
    Extract feature names from the trained model
    """
    model = load_model()

    if hasattr(model, "feature_names_in_"):
        return list(model.feature_names_in_)

    raise RuntimeError("Model does not expose feature names")


def preprocess_input(input_data):
    """
    Prepare input data for prediction
    """
    feature_names = get_feature_names()

    if isinstance(input_data, dict):
        df = pd.DataFrame([input_data])
    elif isinstance(input_data, pd.DataFrame):
        df = input_data.copy()
    else:
        raise ValueError("Input must be dict or DataFrame")

    # Align columns
    df = df.reindex(columns=feature_names, fill_value=0)

    scaler = load_scaler()
    return scaler.transform(df)


def predict(input_data):
    model = load_model()
    X = preprocess_input(input_data)
    return model.predict(X)


def predict_proba(input_data):
    model = load_model()
    X = preprocess_input(input_data)
    return model.predict_proba(X)[:, 1]
