# Customer cohorts: are people coming back?
**Python · Customer analysis · Honest reporting**

## The question
We know who bought once. But what share of new customers returned in the *next calendar month*? That gives us a fairer view than dividing all repeat purchasers by all customers, because newer customers have had less time to return.

## How this works
A *cohort* is a group whose first purchase happened in the same month. The script finds each person's first month and checks if they purchased again in the following month.

## Read it in this order
1. `data/orders.csv` — twelve fictional customers and twenty orders.
2. `cohorts.py` — the logic that groups customers.
3. `RESULTS.md` — the findings and why June is intentionally left blank.

Run from the portfolio root: `python3 projects/customer-cohorts/cohorts.py`. No packages required.

## Important distinction
June has no full July observation. Reporting its month-one retention as 0% would be wrong; the code returns `None` (not yet observable) instead. This project is an exercise with synthetic data, not a claim about real customer behaviour.
