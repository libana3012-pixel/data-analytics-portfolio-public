# How the data-analysis projects were carried out

[Portfolio home](README.md) | [Reading guide](START-HERE.md) | [Skills and evidence](SKILLS.md)

The studies use fictional data so that the inputs, transformation steps, calculations and outcomes can be reviewed openly. The following distinguishes demonstrated work from future reporting plans.

## 1. Understand the underlying customer and order tables

**Tools actually used:** SQL / SQLite, with Python's built-in `sqlite3` used for independent checks in the two standalone cases.

**Why start here:** One order can have multiple items and one customer can have multiple orders. If those are joined without considering the row level, counting rows can inflate the order count. A reliable KPI begins with a clear definition of what one record represents.

**How:** The [revenue case](https://github.com/libana3012-pixel/Sales-Revenue-Analysis/blob/main/case-study/METHOD.md) calculates each order from quantity multiplied by transaction-time unit price, then aggregates orders. The [customer case](https://github.com/libana3012-pixel/Customer-Sales-Analysis/blob/main/case-study/METHOD.md) starts from the customer table with a LEFT JOIN so people who never purchased remain visible.

**Outcome:** The synthetic example has 12 distinct orders, 19 order lines and a gross line value of 2,020 CU. Eight customers are registered, seven have an observed order and one has none. See the linked analyses for detailed checks and limitations.

## 2. Compare customer behaviour over a fair period

**Tool actually used:** Python 3 (`csv`, `pathlib`, `collections`) with the [source orders](projects/customer-cohorts/data/orders.csv).

**Why:** A single repeat-purchase count gives March's customers more time to return than June's customers. Grouping people by first observed purchase month and testing their immediately following calendar month makes the question more consistent.

**How:** The [cohort script](projects/customer-cohorts/cohorts.py) groups each person's observed order months, finds their first month and checks the next calendar month. Duplicate order IDs are rejected.

**Recreate an answer:** Two of three March customers purchased again in April: 2 / 3 × 100 = **66.67%**. June is marked *not observable*, rather than 0%, because the file has no July data. [Method and worked example](projects/customer-cohorts/METHOD.md) | [Results](projects/customer-cohorts/RESULTS.md).

## 3. Check inputs before reporting

**Tools actually used:** Python 3's `csv`, `Decimal` and `unittest`.

**Why:** Duplicate IDs, an unknown customer reference and invalid quantities or prices can make a calculated total unreliable. Validating the inputs helps identify a problem close to its source instead of trying to guess why a dashboard looks wrong.

**How:** The [validator](projects/data-quality/check_data.py) reads the [clean file](projects/data-quality/data/orders_clean.csv) and the deliberately [faulty file](projects/data-quality/data/orders_problematic.csv), reports specific problems and returns a non-zero exit code on invalid input. The [unit tests](projects/data-quality/test_checks.py) cover passing and failing cases.

**Recreate an answer:** The valid fictional lines are 2×50 + 1×80 + 3×20 + 1×120 = **360 CU**. The flawed input should fail; that failure is expected. [Detailed explanation](projects/data-quality/METHOD.md).

## 4. Check a key sales figure independently

**Tool actually used:** Python 3 standard library.

**Why:** A single polished SQL result is not enough if its underlying aggregation has an unnoticed mistake. The [cross-check script](python/verify_sales.py) calculates a second set of totals from included fictional line-item values and asserts the expected figures.

**Outcome:** Twelve orders, 19 lines, 28 units and 2,020 CU; average order value = 2,020 / 12 = **168.33 CU**. At present, the Python script maintains a separate included copy of the fictional line values; loading from the same source tables directly is the next improvement. [Script explanation](python/README.md).

## 5. Reporting tools: planned, not yet implemented

The [Power BI plan](powerbi/README.md) outlines a dashboard layout, data model and draft DAX. The [Fabric plan](fabric/README.md) explains a possible ingestion-to-reporting architecture. Neither is represented here as a completed deployed report.

## Reproduce and verify
From the root with Python 3:
```bash
python3 projects/customer-cohorts/cohorts.py
python3 projects/data-quality/check_data.py
python3 -m unittest discover -s projects/data-quality -p 'test_*.py' -v
python3 python/verify_sales.py
```
The [GitHub Actions workflow](.github/workflows/verify.yml) runs the scripts and unit tests. It also checks that the deliberately faulty fixture is rejected.
