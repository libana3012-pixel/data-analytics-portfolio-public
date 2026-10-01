# Input guide | Why these sample files exist

[Case overview](README.md) · [Method](METHOD.md) · [Clean CSV](data/orders_clean.csv) · [Faulty CSV](data/orders_problematic.csv) · [Validator](check_data.py) · [Tests](test_checks.py)

Both files are made-up, one-row-per-order examples. The columns are `order_id` (unique transaction), `customer_id` (must appear in the fictional reference set C01–C03), `quantity` (positive integer) and `unit_price` (valid finite, non-negative decimal).

## Clean input and calculation
| Order | Calculation | Gross line value (CU) |
| --- | --- | ---: |
| O01 | 2 × 50 | 100 |
| O02 | 1 × 80 | 80 |
| O03 | 3 × 20 | 60 |
| O04 | 1 × 120 | 120 |
| **Total** | | **360** |

## Why the problematic file is included
Its duplicated O02 tests the duplicate-ID rule; C99 tests the unknown-customer rule; a negative quantity tests quantity validation; and `not_a_number` tests numerical parsing. The aim is to demonstrate that the checker detects and reports failures, not merely that it can sum valid records.

Run the clean case from the portfolio root: `python3 projects/data-quality/check_data.py`. The following command **should exit with an error**: `python3 projects/data-quality/check_data.py projects/data-quality/data/orders_problematic.csv`.

These rules are appropriate to this small fixture, not universal accounting rules. Real item-level records may repeat an order ID legitimately; refunds and returns require separately defined treatment.
