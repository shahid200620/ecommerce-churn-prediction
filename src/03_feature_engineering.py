import pandas as pd
import numpy as np
import json
import os
from datetime import timedelta

class FeatureEngineer:
    """
    Feature engineering and churn labeling for customer-level prediction
    """

    def __init__(self, input_path="data/processed/cleaned_transactions.csv"):
        self.input_path = input_path
        self.df = None
        self.customer_df = None
        self.feature_metadata = {}

    def load_data(self):
        self.df = pd.read_csv(
            self.input_path,
            parse_dates=["InvoiceDate"]
        )
        return self

    def create_reference_date(self):
        self.reference_date = self.df["InvoiceDate"].max()
        return self

    def create_rfm_features(self):
        snapshot_date = self.reference_date + timedelta(days=1)

        rfm = self.df.groupby("CustomerID").agg({
            "InvoiceDate": lambda x: (snapshot_date - x.max()).days,
            "InvoiceNo": "nunique",
            "TotalPrice": "sum"
        })

        rfm.columns = ["Recency", "Frequency", "Monetary"]
        self.customer_df = rfm.reset_index()
        return self

    def create_additional_features(self):
        # Average order value
        order_values = (
            self.df.groupby(["CustomerID", "InvoiceNo"])["TotalPrice"]
            .sum()
            .reset_index()
        )

        aov = order_values.groupby("CustomerID")["TotalPrice"].mean().reset_index()
        aov.columns = ["CustomerID", "AvgOrderValue"]

        # Active months
        active_months = (
            self.df.groupby("CustomerID")["InvoiceDate"]
            .apply(lambda x: x.dt.to_period("M").nunique())
            .reset_index()
        )
        active_months.columns = ["CustomerID", "ActiveMonths"]

        self.customer_df = (
            self.customer_df
            .merge(aov, on="CustomerID")
            .merge(active_months, on="CustomerID")
        )
        return self

    def define_churn(self, churn_threshold_days=90):
        self.customer_df["Churn"] = (
            self.customer_df["Recency"] > churn_threshold_days
        ).astype(int)
        return self

    def finalize_features(self):
        self.customer_df["LogMonetary"] = np.log1p(self.customer_df["Monetary"])
        return self

    def save_outputs(self):
        os.makedirs("data/processed", exist_ok=True)

        output_path = "data/processed/customer_features.csv"
        self.customer_df.to_csv(output_path, index=False)

        churn_rate = round(self.customer_df["Churn"].mean() * 100, 2)

        self.feature_metadata = {
            "total_customers": int(len(self.customer_df)),
            "churn_rate_percentage": churn_rate,
            "features": {
                "Recency": "Days since last purchase",
                "Frequency": "Number of unique invoices",
                "Monetary": "Total spending",
                "LogMonetary": "Log-transformed total spending",
                "AvgOrderValue": "Average order value per invoice",
                "ActiveMonths": "Number of active months",
                "Churn": "Target variable (1 = churned, 0 = active)"
            },
            "churn_definition": "Customer inactive for more than 90 days",
            "reference_date": str(self.reference_date.date())
        }

        with open("data/processed/feature_metadata.json", "w") as f:
            json.dump(self.feature_metadata, f, indent=4)

        print("\nFEATURE ENGINEERING SUMMARY")
        print("=" * 50)
        print(f"Total customers: {len(self.customer_df)}")
        print(f"Churn rate: {churn_rate}%")
        print("=" * 50)

        return self

    def run_pipeline(self):
        (
            self.load_data()
            .create_reference_date()
            .create_rfm_features()
            .create_additional_features()
            .define_churn()
            .finalize_features()
            .save_outputs()
        )

        return self.customer_df


if __name__ == "__main__":
    engineer = FeatureEngineer()
    customer_features = engineer.run_pipeline()

    print("\nFinal feature dataset shape:", customer_features.shape)
