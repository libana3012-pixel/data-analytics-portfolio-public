# Case study | Keeping unreliable records out of a report

[← Portfolio home](../../README.md) · [Detailed method](METHOD.md)

**Python · CSV validation · Unit tests · Synthetic input**

[← Data Analytics portfolio](../../README.md) · [Read the approach in detail](METHOD.md) · [Input fields and worked calculations](DATA-GUIDE.md) · [Source code](check_data.py) · [Automated tests](test_checks.py)

## 1. The business situation
Imagine a manager receiving a monthly sales dashboard. A duplicate order inflates revenue; an unknown customer reference misstates customer activity; an invalid price may produce misleading values. A good-looking chart cannot correct incorrect input. I built a validation step **before** the reporting stage.

## 2. The question
Can a short, repeatable program distinguish a valid file from deliberately damaged data, explain the error clearly, and prevent subsequent calculations from treating bad input as trusted?

## 3. Why these checks?
| Check | Reason | Bad example |
| --- | --- | --- |
| Missing or repeated order ID | Avoid counting a one-row-per-order transaction twice | `O02` twice |
| Unknown customer | Flag an ID outside the fictional reference list | `C99` |
| Quantity must be positive | A negative or zero quantity needs an explicit business treatment | `-2` |
| Valid non-negative finite price | Avoid invalid numeric calculations | `not_a_number` |

**Scope of the model:** This fictional file has one row per order. In a real order-line dataset an order ID may legitimately repeat; the unique key should then be a line ID or an appropriate composite key.

## 4. The process
Read the CSV using Python's standard library; track seen IDs; compare customers against a tiny reference set; parse prices with `Decimal`; collect row-numbered errors. The valid four-row sample totals **360 fictional currency units (CU)**. A deliberately flawed fixture proves the script can reject problems rather than merely print a success message.

[Follow the method step by step](METHOD.md) to see why each operation was selected and what would need to change in production.

## 5. Read and run
| Link | Why open it |
| --- | --- |
| [Valid sample](data/orders_clean.csv) | Shows the expected input format |
| [Problematic sample](data/orders_problematic.csv) | See the precise mistakes the rules should catch |
| [Validation code](check_data.py) | Implements the rules |
| [Unit tests](test_checks.py) | Tests a clean file and a bad one |
| [Workflow](../../.github/workflows/verify.yml) | Runs checks automatically on GitHub |

From the public portfolio root:
```bash
python3 projects/data-quality/check_data.py
python3 -m unittest discover -s projects/data-quality -p 'test_*.py' -v
```
The first command should print **360 CU**. Now deliberately run the problematic file:
```bash
python3 projects/data-quality/check_data.py projects/data-quality/data/orders_problematic.csv
```
**A non-zero exit code is the expected result of the last command**, not a failed portfolio.

## 6. Business interpretation and next steps
A report is only as reliable as its inputs. These checks demonstrate a starting point, not a production monitoring system. A realistic next build would obtain the customer reference from a database, validate required columns and dates, distinguish refunds from invalid negative values, define a source-data contract and log failures to a review queue.

**Data provenance:** All values and IDs in this exercise are fictional. [Return to the project overview](../../README.md).
