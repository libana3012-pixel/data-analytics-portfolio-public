# Method explained | Month-one cohort analysis

[← Case overview](README.md) · [Results](RESULTS.md) · [Source](data/orders.csv) · [Code](cohorts.py)

## Why cohorts instead of one repeat percentage?
A cumulative repeat count answers whether somebody ever returned before the reporting cutoff, but does not give everybody the same follow-up period. A first-purchase cohort groups customers by their entry month and asks a fixed follow-up question.

## Definitions
- **Cohort month:** the earliest recorded order month for a customer.
- **Month-one return:** an order in the *next calendar month*, not merely any later month and not exactly 30 days after purchase.
- **Eligible cohort:** the next calendar month is covered by the dataset.
- **Retention rate for this exercise:** eligible customers with a next-month order divided by the cohort's customer count.

## Follow one customer
Customer C01 first purchased in March and has another order in April. They count in the March cohort and as a month-one returner. C02 first purchased in March but next purchased in May, so they do **not** count as returning in April. C03 purchased first in March and again in April: two of the three March customers returned the following month, giving 2 ÷ 3 × 100 = **66.67%**.

## Why June is blank
The data ends in June. For a customer first seen in June, the next calendar month is July. We did not observe July, so we cannot report 0% retention. `None` in the code means *not observable*, not a calculation failure.

## How the script works
It reads CSV rows, rejects duplicate order IDs, groups observed months by customer, chooses the minimum month as the first, advances to the next calendar month and counts eligible returns. The helper handles December-to-January rollover. The final report keeps cohort size and the follow-up condition visible.

## Limitations and next step
This assumes that the first order in the file is the true first order: older missing history could misclassify a customer. It has only monthly granularity and three customers per cohort; no marketing cost, refunds or acquisition source. In a larger implementation I would inspect data completeness, report multiple follow-up months, and include cohort counts next to every percentage.

[← Back to case](README.md) · [Portfolio home](../../README.md).
