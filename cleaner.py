import pandas as pd


def load_data(filepath: str) -> pd.DataFrame:
    """Load CSV data into a Pandas DataFrame."""
    return pd.read_csv(filepath)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and aggregate revenue by region."""
    df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")
    df = df.dropna()

    summary = (
        df.groupby("region")["revenue"]
        .sum()
        .reset_index()
        .sort_values(by="revenue", ascending=False)
    )

    return summary
