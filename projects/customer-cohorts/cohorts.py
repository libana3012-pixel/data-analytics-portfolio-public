"""Customer cohort exercise. Month-one retention = return in next calendar month."""
import csv
from collections import defaultdict
from pathlib import Path

SOURCE = Path(__file__).parent / "data" / "orders.csv"

def next_month(month):
    year, value = map(int, month.split("-"))
    return f"{year + (value == 12):04d}-{(value % 12) + 1:02d}"

def analyse(path=SOURCE, observation_end="2026-06"):
    customer_months = defaultdict(set)
    seen_orders = set()
    with open(path, newline="", encoding="utf-8") as source:
        for row in csv.DictReader(source):
            if row["order_id"] in seen_orders:
                raise ValueError("Duplicate order ID")
            seen_orders.add(row["order_id"])
            if row["order_month"] > observation_end:
                raise ValueError("Order outside observation window")
            customer_months[row["customer_id"]].add(row["order_month"])
    cohorts = defaultdict(list)
    for customer_id, months in customer_months.items():
        cohorts[min(months)].append(months)
    result = []
    for cohort, members in sorted(cohorts.items()):
        followup = next_month(cohort)
        eligible = followup <= observation_end
        returned = sum(followup in months for months in members) if eligible else None
        result.append({"first_month": cohort, "new_customers": len(members),
                       "month_1_returned": returned,
                       "month_1_retention_pct": round(100 * returned / len(members), 2) if eligible else None})
    return result

if __name__ == "__main__":
    for row in analyse():
        print(row)
