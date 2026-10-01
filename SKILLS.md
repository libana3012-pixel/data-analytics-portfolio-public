# Skills and evidence

The goal is to show what each tool contributes to an analysis, rather than presenting a long list of logos.

| Tool or concept | Evidence | Status |
| --- | --- | --- |
| SQL, SQLite | [Revenue analysis](https://github.com/libana3012-pixel/Sales-Revenue-Analysis), [Customer analysis](https://github.com/libana3012-pixel/Customer-Sales-Analysis) | Public case-study queries and source checks |
| Python, CSV | [Cohort script](projects/customer-cohorts/cohorts.py), [sales cross-check](python/verify_sales.py) | Working sample code with fictional inputs |
| Data validation | [Validation script](projects/data-quality/check_data.py) and [unit tests](projects/data-quality/test_checks.py) | Tests provided; CI workflow verifies them |
| Reporting and KPI definitions | [Marketing portfolio](https://github.com/libana3012-pixel/Marketing-Analytics-Portfolio) | Prior, separate marketing chapter |
| Power BI, Power Query, DAX | [Design plan](powerbi/README.md) | In development; no validated PBIX available |
| Microsoft Fabric | [Architecture plan](fabric/README.md) | Proposed study; no deployed environment claimed |

## Working principles
- Define the business question and data grain first.
- Reconcile key totals before reporting them.
- Keep missing observations distinct from observed zero values.
- Separate measured associations from causal conclusions.
- Only describe delivered implementations and credentials as complete after verification.
