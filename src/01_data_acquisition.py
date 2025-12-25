import pandas as pd
import os
from datetime import datetime

RAW_DATA_PATH = "data/raw/online_retail.csv"

def load_raw_data():
    """
    Load raw dataset from data/raw directory
    """
    if not os.path.exists(RAW_DATA_PATH):
        raise FileNotFoundError(
            "Dataset not found! Please place online_retail.csv inside data/raw/"
        )

    df = pd.read_csv(
        RAW_DATA_PATH,
        encoding="latin1",
        parse_dates=["InvoiceDate"]
    )

    print(f"Dataset loaded successfully")
    print(f"Shape: {df.shape}")
    return df


def generate_data_profile(df):
    """
    Generate basic data profile
    """
    os.makedirs("data/raw", exist_ok=True)

    profile_path = "data/raw/data_profile.txt"
    with open(profile_path, "w") as f:
        f.write(f"Generated on: {datetime.now()}\n\n")
        f.write(f"Rows: {df.shape[0]}\n")
        f.write(f"Columns: {df.shape[1]}\n\n")
        f.write("Column Types:\n")
        f.write(str(df.dtypes))
        f.write("\n\nPreview:\n")
        f.write(str(df.head()))

    print(f"Data profile saved to {profile_path}")


if __name__ == "__main__":
    df = load_raw_data()
    generate_data_profile(df)
