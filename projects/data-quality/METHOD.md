# Method explained | Data quality

[← Case overview](README.md) · [Input files](data/orders_clean.csv) · [Validator](check_data.py) · [Tests](test_checks.py)

## Why validate before reporting?
A monthly KPI is an aggregate. It can look plausible even if underlying records are duplicated, invalid or missing a reference. Checking only the final total would not explain *why* a number is wrong. I therefore test individual source rows first and make invalid input stop the workflow.

## Read the implementation from top to bottom
1. **Define the allowed customer references.** `VALID_CUSTOMERS` acts as a tiny reference table. This is suitable for a transparent exercise; in production the IDs should come from a maintained customer source.
2. **Read rows with `csv.DictReader`.** Named columns are easier to understand than relying on the position of each field. Starting the row counter at 2 accounts for the header and makes error messages useful.
3. **Remember prior order IDs.** A `set` allows the script to flag a duplicate in this *one-row-per-order* fixture. Real item-level datasets must use a different uniqueness rule.
4. **Check the customer reference.** An unknown ID could indicate a mistyped transaction or missing master data.
5. **Convert quantity to an integer and unit price to `Decimal`.** Decimal is appropriate for money-like example values. The script rejects invalid, negative and non-finite prices.
6. **Collect errors rather than hiding them.** The command returns a non-zero status when errors exist, so a reporting pipeline can stop instead of using questionable totals.
7. **Test success and failure.** The clean file should produce 360 CU; the damaged fixture should identify multiple problems.

## One calculation
For `O01`, quantity 2 × unit price 50 = 100 CU. The four valid rows contribute 100 + 80 + 60 + 120 = **360 CU**. It is a gross example line value, not profit.

## What this does not test
It does not prove a complete upstream data pipeline is reliable. It does not currently enforce an external schema, verify currency conversions, distinguish refunds or handle millions of rows. These are future engineering and business-definition tasks.

**Try next:** alter a quantity in the clean file and rerun validation and unit tests. Then restore the original to see why fixed expected outputs are useful for catching accidental changes.

[← Back to data-quality case](README.md) · [Portfolio home](../../README.md).
