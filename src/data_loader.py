import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """Load medical insurance dataset."""
    df = pd.read_csv(path)
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    return df
