import pandas as pd

def ingest(filepath):
    df = pd.read_csv(filepath)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    print(f"** Loaded {len(df)} log entries.\n** Log filepath:{filepath}")
    print()
    return df


