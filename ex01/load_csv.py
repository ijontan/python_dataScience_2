import pandas as pd


def load(path: str) -> pd.DataFrame:
    """load a csv file from path"""
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None
