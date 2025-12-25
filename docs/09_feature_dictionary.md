\# Feature Dictionary



\## Target Variable



| Feature | Type | Description | Example | Business Meaning |

|-------|------|-------------|---------|------------------|

| Churn | Binary | 1 = Customer did not purchase in next 3 months, 0 = Active | 1 | Identifies customers at risk of leaving |

\# Feature Dictionary



\## Target Variable



| Feature | Type | Description | Example | Business Meaning |

|-------|------|-------------|---------|------------------|

| Churn | Binary | 1 = Customer did not purchase in next 3 months, 0 = Active | 1 | Identifies customers at risk of leaving |



---



\## RFM Features



| Feature | Type | Description | Range | Business Meaning |

|------|------|-------------|-------|------------------|

| Recency | Integer | Days since last purchase (from cutoff date) | 0–600 | Lower = more recently active |

| Frequency | Integer | Total number of purchases | 1–200+ | Higher = more loyal |

| TotalSpent | Float | Total revenue from customer (£) | 0–50,000+ | Customer lifetime value |

| AvgOrderValue | Float | Avg spend per transaction (£) | 0–500+ | Spending behavior |

| UniqueProducts | Integer | Distinct products purchased | 1–300+ | Product diversity |

| TotalItems | Integer | Total quantity purchased | 1–5000+ | Purchase volume |



---



\## Behavioral Features



| Feature | Type | Description | Business Meaning |

|------|------|-------------|------------------|

| AvgDaysBetweenPurchases | Float | Avg gap between purchases | Purchase consistency |

| AvgBasketSize | Float | Avg items per order | Basket behavior |

| StdBasketSize | Float | Variability in basket size | Shopping stability |

| MaxBasketSize | Integer | Largest basket | Bulk buying |

| PreferredDay | Integer (0–6) | Most common shopping weekday | Engagement timing |

| PreferredHour | Integer (0–23) | Most common purchase hour | Time preference |

| CountryDiversity | Integer | Number of countries purchased from | Cross-border behavior |



---



\## Temporal Features



| Feature | Type | Description | Business Meaning |

|------|------|-------------|------------------|

| CustomerLifetimeDays | Integer | Days between first and last purchase | Customer longevity |

| PurchaseVelocity | Float | Purchases per day | Engagement intensity |

| Purchases\_Last30Days | Integer | Purchases in last 30 days | Recent activity |

| Purchases\_Last60Days | Integer | Purchases in last 60 days | Medium-term activity |

| Purchases\_Last90Days | Integer | Purchases in last 90 days | Churn signal |



---



\## Product Affinity Features



| Feature | Type | Description | Business Meaning |

|------|------|-------------|------------------|

| ProductDiversityScore | Float | Ratio of unique products to total purchases | Variety preference |

| AvgPricePreference | Float | Avg unit price purchased | Price sensitivity |

| StdPricePreference | Float | Price variability | Discount sensitivity |

| MinPrice | Float | Cheapest product purchased | Budget floor |

| MaxPrice | Float | Most expensive product purchased | Premium affinity |

| AvgQuantityPerOrder | Float | Avg quantity per order | Bulk vs retail buyer |



---



\## RFM Segmentation Features



| Feature | Type | Description | Business Meaning |

|------|------|-------------|------------------|

| RecencyScore | Integer (1–4) | Quartile score (lower recency = higher score) | Recent engagement |

| FrequencyScore | Integer (1–4) | Quartile score | Loyalty level |

| MonetaryScore | Integer (1–4) | Quartile score | Revenue value |

| RFM\_Score | Integer | Combined RFM score | Overall customer value |

| CustomerSegment | Categorical | Champions, Loyal, Potential, At Risk, Lost | Marketing targeting |



---



\## Feature Engineering Decisions



\- RFM features capture \*\*value, loyalty, and engagement\*\*

\- Temporal features detect \*\*early churn signals\*\*

\- Behavioral features capture \*\*purchase patterns\*\*

\- Product features represent \*\*shopping preferences\*\*

\- Segmentation enables \*\*targeted retention strategies\*\*



---



\## Expected Important Features (Hypothesis)



1\. Recency (strongest predictor)

2\. Purchases\_Last30Days

3\. Frequency

4\. TotalSpent

5\. PurchaseVelocity



These align with standard e-commerce churn behavior.



---



\## RFM Features



| Feature | Type | Description | Range | Business Meaning |

|------|------|-------------|-------|------------------|

| Recency | Integer | Days since last purchase (from cutoff date) | 0–600 | Lower = more recently active |

| Frequency | Integer | Total number of purchases | 1–200+ | Higher = more loyal |

| TotalSpent | Float | Total revenue from customer (£) | 0–50,000+ | Customer lifetime value |

| AvgOrderValue | Float | Avg spend per transaction (£) | 0–500+ | Spending behavior |

| UniqueProducts | Integer | Distinct products purchased | 1–300+ | Product diversity |

| TotalItems | Integer | Total quantity purchased | 1–5000+ | Purchase volume |



---



\## Behavioral Features



| Feature | Type | Description | Business Meaning |

|------|------|-------------|------------------|

| AvgDaysBetweenPurchases | Float | Avg gap between purchases | Purchase consistency |

| AvgBasketSize | Float | Avg items per order | Basket behavior |

| StdBasketSize | Float | Variability in basket size | Shopping stability |

| MaxBasketSize | Integer | Largest basket | Bulk buying |

| PreferredDay | Integer (0–6) | Most common shopping weekday | Engagement timing |

| PreferredHour | Integer (0–23) | Most common purchase hour | Time preference |

| CountryDiversity | Integer | Number of countries purchased from | Cross-border behavior |



---



\## Temporal Features



| Feature | Type | Description | Business Meaning |

|------|------|-------------|------------------|

| CustomerLifetimeDays | Integer | Days between first and last purchase | Customer longevity |

| PurchaseVelocity | Float | Purchases per day | Engagement intensity |

| Purchases\_Last30Days | Integer | Purchases in last 30 days | Recent activity |

| Purchases\_Last60Days | Integer | Purchases in last 60 days | Medium-term activity |

| Purchases\_Last90Days | Integer | Purchases in last 90 days | Churn signal |



---



\## Product Affinity Features



| Feature | Type | Description | Business Meaning |

|------|------|-------------|------------------|

| ProductDiversityScore | Float | Ratio of unique products to total purchases | Variety preference |

| AvgPricePreference | Float | Avg unit price purchased | Price sensitivity |

| StdPricePreference | Float | Price variability | Discount sensitivity |

| MinPrice | Float | Cheapest product purchased | Budget floor |

| MaxPrice | Float | Most expensive product purchased | Premium affinity |

| AvgQuantityPerOrder | Float | Avg quantity per order | Bulk vs retail buyer |



---



\## RFM Segmentation Features



| Feature | Type | Description | Business Meaning |

|------|------|-------------|------------------|

| RecencyScore | Integer (1–4) | Quartile score (lower recency = higher score) | Recent engagement |

| FrequencyScore | Integer (1–4) | Quartile score | Loyalty level |

| MonetaryScore | Integer (1–4) | Quartile score | Revenue value |

| RFM\_Score | Integer | Combined RFM score | Overall customer value |

| CustomerSegment | Categorical | Champions, Loyal, Potential, At Risk, Lost | Marketing targeting |



---



\## Feature Engineering Decisions



\- RFM features capture \*\*value, loyalty, and engagement\*\*

\- Temporal features detect \*\*early churn signals\*\*

\- Behavioral features capture \*\*purchase patterns\*\*

\- Product features represent \*\*shopping preferences\*\*

\- Segmentation enables \*\*targeted retention strategies\*\*



---



\## Expected Important Features (Hypothesis)



1\. Recency (strongest predictor)

2\. Purchases\_Last30Days

3\. Frequency

4\. TotalSpent

5\. PurchaseVelocity



These align with standard e-commerce churn behavior.



