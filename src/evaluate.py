from sklearn.metrics import r2_score, mean_squared_error
from math import sqrt


def evaluate_model(y_true, y_pred):
    """Return R2, MSE, RMSE."""
    mse = mean_squared_error(y_true, y_pred)
    rmse = sqrt(mse)
    r2 = r2_score(y_true, y_pred)

    return {
        "r2": r2,
        "mse": mse,
        "rmse": rmse
    }
