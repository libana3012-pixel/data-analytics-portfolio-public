# Development log | Data Analytics

[← Portfolio home](README.md) · [How the projects work](WORKFLOW.md) · [Learning path](LEARNING-PATH.md)

This log records **actual repository milestones and future work separately**. Dates below refer to documented GitHub activity or intended work, not reconstructed contribution dates. GitHub commit history remains unchanged. The datasets are synthetic exercises.

## Recorded milestone — 1 October 2026

The public-safe Data Analytics portfolio was set up with the following work, brought together from existing practice material and documented in its current form:

- [Customer cohort analysis](projects/customer-cohorts/README.md): Python example with defined next-calendar-month follow-up and missing June follow-up correctly identified as not observable.
- [Data-quality exercise](projects/data-quality/README.md): clean and intentionally faulty CSV fixtures, a validator and automated unit tests.
- [Sales cross-check](python/README.md): a Python standard-library calculation of the illustrative order and revenue figures.
- [Workflow explanation](WORKFLOW.md), source-field guides and an organised reading route.
- A [GitHub Actions workflow](.github/workflows/verify.yml) that runs the published checks. The workflow reported success when the public portfolio was assembled.

The separately published [Revenue](https://github.com/libana3012-pixel/Sales-Revenue-Analysis), [Customer Sales](https://github.com/libana3012-pixel/Customer-Sales-Analysis) and [Marketing Analytics](https://github.com/libana3012-pixel/Marketing-Analytics-Portfolio) projects are linked rather than duplicated here. Their synthetic case studies and automated checks were also documented and verified. This is a summary of the work visible now, **not a claim that each component was originally created on this day**.

## Planned work | Update as it is completed

| Target window | Task | Completion evidence | Status |
| --- | --- | --- | --- |
| Early October | Review SQL queries line by line; explain joins, calculation grain and validation decisions | Source comments or a clear worked example linked from each SQL case | Planned |
| October, week 2 | Improve Python exercises: edge cases, input validation and unit tests | New tests and a successful GitHub workflow | Planned |
| October, week 3 | Build a real Power BI report from the synthetic sales case | Actual report file or genuine screenshots and reconciled figures | Planned |
| October, week 4 | Compare source, SQL, Python and Power BI figures; document differences | One consistent source-to-report reconciliation | Planned |
| November | Extend a case with a new business question and publish a dated findings note | Reproducible code, explanatory write-up and documented limitations | Planned |

These windows are **targets**, not commitments or claims of already completed work. If a task takes longer, update the plan rather than marking it complete early.

## Format for future entries

When real work has been carried out, add a new entry in this format:

```markdown
### YYYY-MM-DD — Short, specific milestone
**Question:** What was I trying to understand or improve?
**Tools:** Which tools were actually used?
**Action:** Which file, query, calculation or test changed, and why?
**Result:** What did I observe? Link the relevant file or commit.
**Issue or limitation:** What was difficult, uncertain or still missing?
**Next:** The smallest useful next step.
```

The aim is to make learning visible through verifiable changes and explanations, not to produce activity solely to fill the contribution calendar.
