import pandas as pd
import numpy as np
from datetime import datetime
import json
import logging
import os

# Setup logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/data_cleaning.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class DataCleaner:
    """
    Comprehensive data cleaning pipeline for Online Retail dataset
    """

    def __init__(self, input_path="data/raw/online_retail.csv"):
        self.input_path = input_path
        self.df = None
        self.cleaning_stats = {
            "original_rows": 0,
            "rows_after_cleaning": 0,
            "rows_removed": 0,
            "retention_rate": 0.0,
            "missing_values_before": {},
            "missing_values_after": {},
            "steps_applied": []
        }

    def load_data(self):
        logging.info("Loading raw dataset")
        self.df = pd.read_csv(
            self.input_path,
            encoding="latin1",
            parse_dates=["InvoiceDate"]
        )

        self.cleaning_stats["original_rows"] = len(self.df)
        self.cleaning_stats["missing_values_before"] = self.df.isnull().sum().to_dict()

        logging.info(f"Loaded {len(self.df)} rows")
        return self

    def remove_missing_customer_ids(self):
        logging.info("Removing missing CustomerID")
        initial_rows = len(self.df)

        self.df = self.df.dropna(subset=["CustomerID"])

        rows_removed = initial_rows - len(self.df)
        self.cleaning_stats["steps_applied"].append({
            "step": "remove_missing_customer_ids",
            "rows_removed": rows_removed
        })
        return self

    def handle_cancelled_invoices(self):
        logging.info("Removing cancelled invoices")
        initial_rows = len(self.df)

        self.df = self.df[~self.df["InvoiceNo"].astype(str).str.startswith("C")]

        rows_removed = initial_rows - len(self.df)
        self.cleaning_stats["steps_applied"].append({
            "step": "handle_cancelled_invoices",
            "rows_removed": rows_removed
        })
        return self

    def handle_negative_quantities(self):
        logging.info("Removing negative or zero quantities")
        initial_rows = len(self.df)

        self.df = self.df[self.df["Quantity"] > 0]

        rows_removed = initial_rows - len(self.df)
        self.cleaning_stats["steps_applied"].append({
            "step": "handle_negative_quantities",
            "rows_removed": rows_removed
        })
        return self

    def handle_zero_prices(self):
        logging.info("Removing zero or negative prices")
        initial_rows = len(self.df)

        self.df = self.df[self.df["UnitPrice"] > 0]

        rows_removed = initial_rows - len(self.df)
        self.cleaning_stats["steps_applied"].append({
            "step": "handle_zero_prices",
            "rows_removed": rows_removed
        })
        return self

    def handle_missing_descriptions(self):
        logging.info("Removing missing descriptions")
        initial_rows = len(self.df)

        self.df = self.df.dropna(subset=["Description"])

        rows_removed = initial_rows - len(self.df)
        self.cleaning_stats["steps_applied"].append({
            "step": "handle_missing_descriptions",
            "rows_removed": rows_removed
        })
        return self

    def remove_outliers(self):
        logging.info("Removing outliers using IQR")

        initial_rows = len(self.df)

        # Quantity IQR
        Q1_qty = self.df["Quantity"].quantile(0.25)
        Q3_qty = self.df["Quantity"].quantile(0.75)
        IQR_qty = Q3_qty - Q1_qty

        lower_qty = Q1_qty - 1.5 * IQR_qty
        upper_qty = Q3_qty + 1.5 * IQR_qty

        self.df = self.df[
            (self.df["Quantity"] >= lower_qty) &
            (self.df["Quantity"] <= upper_qty)
        ]

        # Price IQR
        Q1_price = self.df["UnitPrice"].quantile(0.25)
        Q3_price = self.df["UnitPrice"].quantile(0.75)
        IQR_price = Q3_price - Q1_price

        lower_price = Q1_price - 1.5 * IQR_price
        upper_price = Q3_price + 1.5 * IQR_price

        self.df = self.df[
            (self.df["UnitPrice"] >= lower_price) &
            (self.df["UnitPrice"] <= upper_price)
        ]

        rows_removed = initial_rows - len(self.df)
        self.cleaning_stats["steps_applied"].append({
            "step": "remove_outliers",
            "rows_removed": rows_removed,
            "method": "IQR",
            "threshold": 1.5
        })
        return self

    def remove_duplicates(self):
        logging.info("Removing duplicate rows")
        initial_rows = len(self.df)

        self.df = self.df.drop_duplicates()

        rows_removed = initial_rows - len(self.df)
        self.cleaning_stats["steps_applied"].append({
            "step": "remove_duplicates",
            "rows_removed": rows_removed
        })
        return self

    def add_derived_columns(self):
        logging.info("Adding derived columns")

        self.df["TotalPrice"] = self.df["Quantity"] * self.df["UnitPrice"]
        self.df["Year"] = self.df["InvoiceDate"].dt.year
        self.df["Month"] = self.df["InvoiceDate"].dt.month
        self.df["DayOfWeek"] = self.df["InvoiceDate"].dt.dayofweek
        self.df["Hour"] = self.df["InvoiceDate"].dt.hour

        self.cleaning_stats["steps_applied"].append({
            "step": "add_derived_columns",
            "columns_added": [
                "TotalPrice", "Year", "Month", "DayOfWeek", "Hour"
            ]
        })
        return self

    def convert_data_types(self):
        logging.info("Converting data types")

        self.df["CustomerID"] = self.df["CustomerID"].astype(int)
        self.df["StockCode"] = self.df["StockCode"].astype("category")
        self.df["Country"] = self.df["Country"].astype("category")

        self.cleaning_stats["steps_applied"].append({
            "step": "convert_data_types"
        })
        return self

    def save_cleaned_data(self, output_path="data/processed/cleaned_transactions.csv"):
        os.makedirs("data/processed", exist_ok=True)

        self.df.to_csv(output_path, index=False)

        self.cleaning_stats["rows_after_cleaning"] = len(self.df)
        self.cleaning_stats["rows_removed"] = (
            self.cleaning_stats["original_rows"] - len(self.df)
        )
        self.cleaning_stats["retention_rate"] = round(
            (len(self.df) / self.cleaning_stats["original_rows"]) * 100, 2
        )
        self.cleaning_stats["missing_values_after"] = self.df.isnull().sum().to_dict()

        with open("data/processed/cleaning_statistics.json", "w") as f:
            json.dump(self.cleaning_stats, f, indent=4)

        print("\nDATA CLEANING SUMMARY")
        print("=" * 50)
        print(f"Original rows: {self.cleaning_stats['original_rows']:,}")
        print(f"Cleaned rows: {self.cleaning_stats['rows_after_cleaning']:,}")
        print(f"Rows removed: {self.cleaning_stats['rows_removed']:,}")
        print(f"Retention rate: {self.cleaning_stats['retention_rate']}%")
        print("=" * 50)

        return self

    def run_pipeline(self):
        print("Starting data cleaning pipeline...")

        (
            self.load_data()
            .remove_missing_customer_ids()
            .handle_cancelled_invoices()
            .handle_negative_quantities()
            .handle_zero_prices()
            .handle_missing_descriptions()
            .remove_outliers()
            .remove_duplicates()
            .add_derived_columns()
            .convert_data_types()
            .save_cleaned_data()
        )

        print("Data cleaning pipeline completed successfully!")
        return self.df


if __name__ == "__main__":
    cleaner = DataCleaner("data/raw/online_retail.csv")
    cleaned_df = cleaner.run_pipeline()

    print(f"\nFinal cleaned dataset shape: {cleaned_df.shape}")
