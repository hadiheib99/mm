import mlflow


def fetch_model_from_registry(model_name, stage=None):
    """Fetch the latest validated model from MLflow registry."""
    print(f"Fetching model '{model_name}' from MLflow registry...")

    client = mlflow.tracking.MlflowClient()

    # If no stage is provided, fetch the latest version
    if not stage:
        versions = client.get_latest_versions(model_name)
        if not versions:
            print(f"❌ No registered versions found for model '{model_name}'")
            return None
        stage = versions[0].current_stage  # Use latest stage

    print(f"Using stage: {stage}")
    model_uri = f"models:/{model_name}/{stage}"

    try:
        model = mlflow.pyfunc.load_model(model_uri)
        print(f"✅ Model '{model_name}' (Stage: {stage}) loaded successfully.")
        return model
    except Exception as e:
        print(f"❌ Failed to load model '{model_name}': {e}")
        return None
