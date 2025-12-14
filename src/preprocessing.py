import pandas as pd


def encode_features(df: pd.DataFrame) -> pd.DataFrame:
    """Encode categorical variables."""
    df = df.copy()

    df["sex"] = df["sex"].map({"male": 1, "female": 0})
    df["smoker"] = df["smoker"].map({"yes": 1, "no": 0})

    df = pd.get_dummies(df, columns=["region"], drop_first=True)

    return df
