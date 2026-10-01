"""Independent, simple check of synthetic sales figures. Python standard library."""
from collections import defaultdict

# Each entry is (order_id, item_quantity, transaction_unit_price).
LINES = [
 ("O001",1,120),("O001",2,35),("O002",1,85),("O003",1,160),("O003",1,25),
 ("O004",2,120),("O005",1,60),("O005",1,35),("O006",2,85),("O007",1,160),
 ("O008",1,120),("O008",2,25),("O009",2,60),("O010",3,35),("O010",1,85),
 ("O011",1,160),("O011",1,60),("O012",3,25),("O012",1,120),
]

def calculate(lines):
    """Return simple shop KPIs. An order may have several item rows."""
    revenue_by_order = defaultdict(int)
    unit_count = 0
    for order_id, quantity, price in lines:
        if quantity <= 0 or price < 0:
            raise ValueError("Invalid quantity or price")
        revenue_by_order[order_id] += quantity * price
        unit_count += quantity
    if not revenue_by_order:
        raise ValueError("Cannot calculate average on an empty dataset")
    total = sum(revenue_by_order.values())
    return {
        "orders": len(revenue_by_order),
        "order_lines": len(lines),
        "units": unit_count,
        "revenue_cu": total,
        "average_order_value_cu": round(total / len(revenue_by_order), 2),
    }

if __name__ == "__main__":
    actual = calculate(LINES)
    expected = {"orders":12,"order_lines":19,"units":28,"revenue_cu":2020,"average_order_value_cu":168.33}
    assert actual == expected, f"Mismatch: {actual} != {expected}"
    for name, value in actual.items():
        print(f"{name}: {value}")
    print("Checks passed.")
