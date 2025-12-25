import pandas as pd
import numpy as np
import json
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

# ======================
# Load data
# ======================
df = pd.read_csv("data/processed/customer_features.csv")

X = df.drop(columns=["Churn"])
y = df["Churn"]

if "CustomerID" in X.columns:
    X = X.drop(columns=["CustomerID"])

X = X.select_dtypes(include=[np.number])

# ======================
# Train-test split
# ======================
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# ======================
# Scaling
# ======================
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

os.makedirs("models", exist_ok=True)

# ======================
# Logistic Regression
# ======================
lr = LogisticRegression(max_iter=1000, random_state=42)
lr.fit(X_train_scaled, y_train)

lr_preds = lr.predict(X_test_scaled)
lr_probs = lr.predict_proba(X_test_scaled)[:, 1]

# ======================
# Random Forest
# ======================
rf = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    n_jobs=-1
)
rf.fit(X_train, y_train)

rf_preds = rf.predict(X_test)
rf_probs = rf.predict_proba(X_test)[:, 1]

# ======================
# Metrics (NO nested dict issues)
# ======================
metrics = {}

metrics["logistic_regression"] = {
    "accuracy": float(accuracy_score(y_test, lr_preds)),
    "precision": float(precision_score(y_test, lr_preds)),
    "recall": float(recall_score(y_test, lr_preds)),
    "f1_score": float(f1_score(y_test, lr_preds)),
    "roc_auc": float(roc_auc_score(y_test, lr_probs))
}

metrics["random_forest"] = {
    "accuracy": float(accuracy_score(y_test, rf_preds)),
    "precision": float(precision_score(y_test, rf_preds)),
    "recall": float(recall_score(y_test, rf_preds)),
    "f1_score": float(f1_score(y_test, rf_preds)),
    "roc_auc": float(roc_auc_score(y_test, rf_probs))
}

# ======================
# Save outputs
# ======================
joblib.dump(lr, "models/logistic_regression.pkl")
joblib.dump(rf, "models/random_forest.pkl")
joblib.dump(scaler, "models/scaler.pkl")

with open("models/model_metrics.json", "w") as f:
    json.dump(metrics, f, indent=4)

print("\nMODEL TRAINING COMPLETE")
print(json.dumps(metrics, indent=4))
