# Start here | A reading guide

This is a public-safe selection from Liban Yusuf's Data Analytics learning work, organised under the **April–October 2026** technical chapter. All example data is synthetic; the stated chapter is not a backdated commit history.

## If you have two minutes
Start with the [homepage](README.md). For two complete and independently readable SQL studies, open [Revenue](https://github.com/libana3012-pixel/Sales-Revenue-Analysis) and [Customer Sales](https://github.com/libana3012-pixel/Customer-Sales-Analysis).

## Choose an area
| Question | Study | What you will see |
| --- | --- | --- |
| How do we measure customer return fairly? | [Cohorts](projects/customer-cohorts/README.md) · [Results](projects/customer-cohorts/RESULTS.md) | First-purchase groups and incomplete follow-up |
| How can errors be caught before a dashboard? | [Data quality](projects/data-quality/README.md) | Valid and intentionally invalid CSVs, checks and unit tests |
| Do Python and SQL figures agree? | [Sales verification](python/README.md) | Independent sample check |
| What is planned for reporting? | [Power BI](powerbi/README.md) | Design and draft DAX, not a finished report |
| What could an end-to-end platform look like? | [Fabric](fabric/README.md) | Architecture plan, not a deployed pipeline |

## Reproduce
```bash
python3 projects/customer-cohorts/cohorts.py
python3 projects/data-quality/check_data.py
python3 -m unittest discover -s projects/data-quality -p 'test_*.py' -v
python3 python/verify_sales.py
```

The check of the deliberately flawed input is expected to exit with an error:
```bash
python3 projects/data-quality/check_data.py projects/data-quality/data/orders_problematic.csv
```

For a complete technical overview, see [Skills and evidence](SKILLS.md) and [the learning route](LEARNING-PATH.md).

## Public versus private
The projects use fictional source data and are intended to be reproducible without access to employer systems.
