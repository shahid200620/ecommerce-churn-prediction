\# Data Cleaning Strategy



\## 1. Missing Values Strategy



\### CustomerID

\- Missing Percentage: ~25%

\- Decision: \*\*DROP rows with missing CustomerID\*\*

\- Reasoning: CustomerID is a unique identifier and cannot be imputed.

\- Impact: Approximately 135,000 rows removed.



\### Description

\- Missing Percentage: <1%

\- Decision: \*\*REMOVE rows\*\*

\- Reasoning: Product description is useful for product-level analysis and interpretation.



---



\## 2. Handling Cancellations



\- Issue: Invoice numbers starting with 'C' represent cancelled transactions.

\- Chosen Strategy: \*\*Remove all cancelled invoices\*\*

\- Reasoning: Cancelled orders do not represent successful purchases and can distort churn behavior.



---



\## 3. Negative Quantities



\- Issue: Negative quantities indicate product returns.

\- Strategy: \*\*Remove rows with Quantity ≤ 0\*\*

\- Reasoning: Returns complicate churn definition and revenue calculations.



---



\## 4. Outliers



\### Quantity Outliers

\- Detection Method: \*\*Interquartile Range (IQR)\*\*

\- Threshold: Q1 − 1.5×IQR to Q3 + 1.5×IQR

\- Action: Remove outliers beyond thresholds.



\### Price Outliers

\- Detection Method: \*\*IQR\*\*

\- Action: Remove extreme price values to avoid skewed monetary features.



---



\## 5. Data Type Conversions



\- InvoiceDate: Converted to datetime

\- CustomerID: Converted from float to integer after removing missing values

\- StockCode \& Country: Converted to categorical for memory efficiency



---



\## 6. Duplicate Handling



\- Definition: Duplicate rows with same InvoiceNo, StockCode, CustomerID, Quantity, UnitPrice, InvoiceDate

\- Strategy: \*\*Remove exact duplicates\*\*



