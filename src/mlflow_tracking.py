import mlflow
import mlflow.sklearn


def log_model(model, model_name, metrics, X_example):
    mlflow.log_param("model", model_name)

    for key, value in metrics.items():
        mlflow.log_metric(key, value)

    mlflow.sklearn.log_model(
        model,
        model_name,
        input_example=X_example
    )
