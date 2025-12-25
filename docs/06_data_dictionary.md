\# Data Dictionary



\*\*Dataset:\*\* online\_retail.csv  

\*\*Source:\*\* UCI Online Retail Dataset  



| Column Name | Data Type | Description | Example | Missing % | Notes |

|------------|-----------|-------------|---------|-----------|-------|

| InvoiceNo | String | Invoice number (C prefix indicates cancellation) | 536365, C536365 | 0% | Used to identify transactions |

| StockCode | String | Product code | 85123A | 0% | Some non-standard codes exist |

| Description | String | Product name | WHITE HANGING HEART | ~0.3% | Missing values removed |

| Quantity | Integer | Quantity per transaction | 6, -1 | 0% | Negative indicates returns |

| InvoiceDate | DateTime | Date and time of purchase | 2010-12-01 08:26 | 0% | Used for temporal features |

| UnitPrice | Float | Price per unit (£) | 2.55 | 0% | Zero/negative removed |

| CustomerID | Float | Customer identifier | 17850.0 | ~25% | Missing values removed |

| Country | String | Customer country | United Kingdom | 0% | 38 unique values |



---



\## Data Quality Issues Identified

\- High percentage of missing CustomerID

\- Cancelled invoices

\- Negative quantities (returns)

\- Zero or negative prices

\- Outliers in quantity and price



---



\## Data Cleaning Required

\- Remove rows with missing CustomerID

\- Remove cancelled invoices

\- Remove negative quantities and invalid prices

\- Handle outliers using IQR method

\- Convert data types for efficiency



