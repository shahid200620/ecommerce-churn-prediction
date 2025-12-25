# -----------------------------------
# Prediction API (Safe for Deployment)
# -----------------------------------

import joblib
import pandas as pd
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = ROOT_DIR / "models"


def _find_model_path():
    candidates = [
        "best_model.pkl",
        "random_forest.pkl",
        "logistic_regression.pkl",
        "decision_tree.pkl",
    ]
    for name in candidates:
        path = MODELS_DIR / name
        if path.exists():
            return path
    return None


def _find_scaler_path():
    path = MODELS_DIR / "scaler.pkl"
    return path if path.exists() else None


def is_model_available():
    return _find_model_path() is not None and _find_scaler_path() is not None


def get_feature_names():
    """
    Return dummy feature names if model is unavailable.
    This prevents Streamlit from crashing.
    """
    model_path = _find_model_path()
    if model_path is None:
        # Safe fallback (UI only)
        return ["Feature_1", "Feature_2", "Feature_3"]

    model = joblib.load(model_path)
    if hasattr(model, "feature_names_in_"):
        return list(model.feature_names_in_)

    return ["Feature_1", "Feature_2", "Feature_3"]


def predict(input_data):
    if not is_model_available():
        raise RuntimeError("Model not available in deployment")

    model = joblib.load(_find_model_path())
    scaler = joblib.load(_find_scaler_path())

    df = pd.DataFrame([input_data]) if isinstance(input_data, dict) else input_data
    df_scaled = scaler.transform(df)
    return model.predict(df_scaled)


def predict_proba(input_data):
    if not is_model_available():
        raise RuntimeError("Model not available in deployment")

    model = joblib.load(_find_model_path())
    scaler = joblib.load(_find_scaler_path())

    df = pd.DataFrame([input_data]) if isinstance(input_data, dict) else input_data
    df_scaled = scaler.transform(df)
    return model.predict_proba(df_scaled)[:, 1]
