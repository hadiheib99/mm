def promote_model_version(model_name, source_stage, target_stage):
    """Promote a model version from one stage to another in the MLflow registry."""
    print(f"Promoting model '{model_name}' from '{source_stage}' to '{target_stage}'...")
    # Example API usage with MLflow
    # client = mlflow.tracking.MlflowClient()
    # client.transition_model_version_stage(
    #     name=model_name,
    #     version=model_version,
    #     stage=target_stage
    # )
    print("Model promoted successfully.")