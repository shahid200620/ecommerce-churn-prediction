import pandas as pd
import os
from datetime import datetime

def download_dataset():
    """
    Dataset is downloaded manually (Kaggle fallback).
    This function validates presence of the dataset.
    """
    os.makedirs("data/raw", exist_ok=True)

    dataset_path = "data/raw/online_retail.csv"

    if not os.path.exists(dataset_path):
        raise FileNotFoundError(
            "Dataset not found. Please place 'online_retail.csv' inside data/raw/"
        )

    print("Dataset found successfully.")
    print(f"Path: {dataset_path}")
    print(f"Timestamp: {datetime.now()}")

    return True


def load_raw_data():
    """
    Load the raw dataset and return DataFrame.
    Handles encoding issues.
    """
    df = pd.read_csv(
        "data/raw/online_retail.csv",
        encoding="latin1",
        parse_dates=["InvoiceDate"]
    )
    return df


def generate_data_profile(df):
    """
    Generate basic data profile and save to text file.
    """
    profile_path = "data/raw/data_profile.txt"

    with open(profile_path, "w", encoding="utf-8") as f:
        f.write("ONLINE RETAIL DATA PROFILE\n")
        f.write("=" * 40 + "\n\n")

        f.write(f"Rows: {df.shape[0]}\n")
        f.write(f"Columns: {df.shape[1]}\n\n")

        f.write("Column Names and Data Types:\n")
        f.write(str(df.dtypes) + "\n\n")

        f.write("Memory Usage:\n")
        f.write(str(df.memory_usage(deep=True)) + "\n\n")

        f.write("Preview (First 5 Rows):\n")
        f.write(str(df.head()) + "\n")

    print("Data profile saved to data/raw/data_profile.txt")


if __name__ == "__main__":
    download_dataset()
    df = load_raw_data()
    generate_data_profile(df)

    print("\nDATA ACQUISITION SUMMARY")
    print("=" * 40)
    print(f"Dataset Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
