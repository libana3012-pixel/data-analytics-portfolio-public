# Data quality: stop bad numbers before they reach a dashboard
**Python · Automated checks · Testable code**

## The question
What if a monthly report looks polished but its input includes duplicate orders, a customer ID that does not exist, or an invalid price? The numbers could be wrong without anyone noticing.

## What this project does
A small Python program checks an order file before it is used in analysis. It rejects duplicate order IDs, unknown customer IDs, non-positive quantities and invalid prices. A second file contains deliberate mistakes so the tests can prove that the checks catch them.

## Try it
From the portfolio root:

```bash
python3 projects/data-quality/check_data.py
python3 projects/data-quality/check_data.py projects/data-quality/data/orders_problematic.csv
python3 -m unittest discover -s projects/05-data-quality -p 'test_*.py' -v
```

Expected: the first command passes and reports **360** in total sample line value. The second prints errors and exits with a non-zero status. The test command verifies both behaviours.

## Why a manager should care
A dashboard cannot fix unreliable source data. These checks turn a manual review into repeatable rules and make errors visible early. All data is invented for this exercise. This is a small proof of concept, not a production monitoring system.
