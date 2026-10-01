# Customer cohorts | Who returns the following month?

**Python · Customer behaviour · Observation windows · Synthetic data**

[← Portfolio home](../../README.md) · [Detailed method](METHOD.md) · [Results](RESULTS.md) · [Source data](data/orders.csv) · [Python code](cohorts.py)

## The business problem
A simple repeat-customer percentage can be unfair. A customer who first bought in March has more opportunities to return before June than someone whose first purchase was in June. If both are measured over the same calendar end date, the newer customer appears worse merely because there is less observation time.

## The question
For each first-purchase month, how many people bought again in the **immediately following calendar month**? I chose that narrow definition so readers can follow it and compare periods with equal eligibility.

## Data and method
The fictional file has 12 customers and 20 orders. Each row contains a customer ID, order ID and order month. The script groups all observed months by customer, finds each earliest purchase month, calculates its next month and tests whether another order occurred then. Duplicate order IDs are rejected.

Read [why this method was chosen](METHOD.md) for a worked example and an explanation of missing follow-up periods.

## Headline findings
| First purchase | New customers | Return next month | Rate |
| --- | ---: | ---: | ---: |
| March | 3 | 2 | 66.67% |
| April | 3 | 1 | 33.33% |
| May | 3 | 1 | 33.33% |
| June | 3 | Not observable | Not observable |

The June value is intentionally missing: the file ends in June, so July behaviour is unknown. A missing observation is not a measured 0%.

## Reproduce
From the root of this repository:
```bash
python3 projects/customer-cohorts/cohorts.py
```
No third-party packages required. Compare output to [the interpreted results](RESULTS.md). The GitHub [verification workflow](../../.github/workflows/verify.yml) also runs the script.

## What the exercise demonstrates
Defining a fair comparison window, reading structured files, de-duplicating order IDs and refusing to fill an unknown outcome with a misleading number. With only three people per group, this is a code-and-reasoning demonstration rather than a basis for customer strategy.

[← Back to portfolio](../../README.md).
