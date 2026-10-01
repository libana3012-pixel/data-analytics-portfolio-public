# How the Python sales cross-check works

[Portfolio](../README.md) · [Python overview](README.md) · [Script](verify_sales.py) · [SQL source case](https://github.com/libana3012-pixel/Sales-Revenue-Analysis)

**Tool:** Python 3 standard library, using `collections.defaultdict`. No Pandas, Power BI or external integration is claimed for this small verification script.

**Reason:** It is easy to accidentally count 19 order-item rows as 19 purchases. By grouping individual fictional line values using their order ID, a second calculation shows why the twelve actual orders and item-line count are different quantities.

**Method:** Each embedded tuple contains order ID, item quantity and transaction unit price. The script rejects a nonpositive quantity and a negative price, multiplies quantity by price and adds line values under the matching order ID. It separately sums quantity to measure units sold.

**Worked example:** order O001 has (1 × 120) + (2 × 35) = **190 CU**, even though it is represented by two item rows. All 19 sample lines represent **28 units**, grouped into **12 orders**. Total gross line value = **2,020 CU**; average order value = 2,020 / 12 = **168.33 CU**.

**How to run:** `python3 python/verify_sales.py` from the portfolio root. The script asserts expected example values; a mismatch raises an error rather than silently publishing a new figure.

**Important design limitation:** this file currently embeds a separate copy of the fictional order-line values. It does not fetch SQL data automatically. A stronger next version should read the SQL source tables directly and reconcile totals row-by-row, removing the risk of two maintained copies drifting apart.
