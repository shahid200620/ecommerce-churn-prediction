# -----------------------------------
# Safe Prediction Stubs for Deployment
# -----------------------------------

def is_model_available():
    # Models are not shipped in public repo
    return False


def predict(input_data):
    raise RuntimeError("Model not available in public deployment")


def predict_proba(input_data):
    raise RuntimeError("Model not available in public deployment")
