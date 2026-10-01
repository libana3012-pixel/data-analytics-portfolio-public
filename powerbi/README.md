# Power BI — next build
**Status: implementation plan, not a finished Power BI report.**

## The question
Can a manager see sales performance in less than a minute, and drill into why a month changed?

## One-page layout
- Header: reporting period and note that all inputs are synthetic.
- KPI cards: Revenue, Orders, Average Order Value, Active Customers.
- Monthly revenue trend: line chart with month on the horizontal axis.
- Product contribution: sorted bar chart.
- Filters: month, category and market.
- Notes: incomplete months, assumptions, source and refresh date.

## Data model
Import `customers`, `orders`, `order_items` and `products` from the revenue case study. Use one-to-many relationships from customers→orders, orders→order_items and products→order_items. Validate each relationship's cardinality before building measures.

## Measures to implement and validate
```dax
Revenue = SUMX(order_items, order_items[quantity] * order_items[unit_price])
Orders = DISTINCTCOUNT(orders[order_id])
Average Order Value = DIVIDE([Revenue], [Orders])
Active Customers = DISTINCTCOUNT(orders[customer_id])
```
These are draft measures until tested inside the actual Power BI model. In particular, check how date and product filters affect `Orders` and `Active Customers`.

## Acceptance criteria
- All-time Revenue = 2,020 CU and Orders = 12 against the synthetic source.
- Monthly totals match the SQL result table.
- Screenshots show the real report, not an invented mock-up.
- Include the exported `.pbix` file only after it exists and is checked.
