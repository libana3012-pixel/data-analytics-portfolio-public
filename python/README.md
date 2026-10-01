# Python cross-check: do the sales numbers agree?
**Status: starter implementation.** This script rebuilds the totals from the same synthetic order lines as the SQL case study using Python's standard library. It deliberately does not claim a Pandas notebook is already complete.

## Run
From the portfolio root: `python3 python/verify_sales.py`. Python 3.8+; no packages required.

Expected: 12 orders, 19 order lines, 28 units, 2020 CU, average order value 168.33 CU. It raises an error if any expected check fails. The input rows are made-up exercise data.

## Why this matters
Two different ways of calculating the same figure help catch mistakes. A useful analyst does not just create a chart: they can explain and check the number behind it.

**Next:** use Pandas to load the SQL dataset directly, then compare results row by row rather than maintain a separate copy of sample data.
