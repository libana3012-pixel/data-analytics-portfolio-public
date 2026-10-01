"""Fail a dataset with duplicate orders, unknown customers, invalid quantities/prices."""
import csv
import sys
from decimal import Decimal, InvalidOperation
from pathlib import Path

ROOT = Path(__file__).parent
VALID_CUSTOMERS = {"C01", "C02", "C03"}

def validate(path):
    errors, seen, revenue = [], set(), Decimal("0")
    with open(path, newline="", encoding="utf-8") as source:
        for line, row in enumerate(csv.DictReader(source), start=2):
            order_id = row["order_id"]
            if not order_id or order_id in seen:
                errors.append(f"row {line}: missing or duplicate order_id")
            seen.add(order_id)
            if row["customer_id"] not in VALID_CUSTOMERS:
                errors.append(f"row {line}: unknown customer")
            try:
                quantity = int(row["quantity"])
                price = Decimal(row["unit_price"])
                if quantity <= 0 or price < 0 or not price.is_finite():
                    errors.append(f"row {line}: invalid quantity or unit price")
                else:
                    revenue += quantity * price
            except (ValueError, InvalidOperation):
                errors.append(f"row {line}: non-numeric quantity or price")
    return errors, revenue

if __name__ == "__main__":
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "data" / "orders_clean.csv"
    errors, revenue = validate(path)
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    print(f"PASSED: no issues detected; total line value = {revenue}")
