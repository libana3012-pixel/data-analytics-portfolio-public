# Data and calculation guide | Customer cohorts

[Case overview](README.md) · [Reasoning](METHOD.md) · [CSV](data/orders.csv) · [Python](cohorts.py) · [Results](RESULTS.md)

The fictional `orders.csv` has three fields: `customer_id` identifies a buyer, `order_id` identifies a purchase, and `order_month` records its month in YYYY-MM format. There are **12 distinct customers and 20 orders**; repeated customer IDs are expected because a buyer can place multiple orders. Duplicate **order IDs** are rejected because each purchase should have its own identifier.

**Step 1:** read rows with Python's `csv.DictReader`; store the set of months per customer. This removes repeated activity in one month when the question is whether somebody returned in that month.

**Step 2:** find the earliest recorded month for each customer, then group customers with the same earliest month. This is the *observed first purchase*, not proof that they never bought before the example dataset begins.

**Step 3:** calculate the next calendar month and check whether it is inside the observation period. For March, the next month is April; the March customers are C01, C02 and C03. C01 and C03 have an April purchase, while C02's subsequent order is in May.

**Step 4:** calculate 2 / 3 × 100 = **66.67% March month-one return**. April and May each have one of three customers returning the following month: **33.33%**. The sample ends in June, so June's next-month return is **not observable**, rather than zero.

**Why this method:** it gives every eligible cohort the same one-calendar-month follow-up question instead of counting all returns before a common cutoff. With three people per group, results are sensitive to individual behaviour and cannot establish a population trend.

Reproduce from the root: `python3 projects/customer-cohorts/cohorts.py`.
