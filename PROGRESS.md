# Development timeline | Marketing to Data Analytics

[← Portfolio home](README.md) · [Reading guide](START-HERE.md) · [Learning path](LEARNING-PATH.md) · [Project workflow](WORKFLOW.md)

The portfolio is arranged by **subject-matter learning periods**. The month ranges explain the structure of the work; they are not altered GitHub timestamps or claims that every included example file was created in the month shown. All published case datasets are synthetic. Specific dated entries will be added when supported by actual work records.

## February–31 March 2026 | Marketing Analytics

This chapter is documented in the separate [Marketing Analytics Portfolio](https://github.com/libana3012-pixel/Marketing-Analytics-Portfolio). It covers the business questions behind website measurement, campaign performance and organic search.

| Topic | What the project demonstrates | Evidence |
| --- | --- | --- |
| Website measurement | Defining useful actions before interpreting traffic and engagement | [Event plan and sample analysis](https://github.com/libana3012-pixel/Marketing-Analytics-Portfolio/tree/main/projects/00-marketing-measurement) |
| Campaign performance | Evaluating spend, click volume, conversions, attributed revenue and limitations together | [Campaign case](https://github.com/libana3012-pixel/Marketing-Analytics-Portfolio/tree/main/projects/01-campaign-performance) |
| Organic search | Separating increased impressions from changes in click-through rate | [Search case](https://github.com/libana3012-pixel/Marketing-Analytics-Portfolio/tree/main/projects/02-organic-search) |

These are the themes of the February–March chapter, not a simulated daily activity history.

## April–September 2026 | Technical Data Analytics chapter

The continuation centres on SQL and Python: relating transaction tables, choosing consistent KPI definitions, grouping customers, checking source quality and explaining results.

| Focus area | Question and approach | Project evidence |
| --- | --- | --- |
| SQL: Revenue | Count distinct orders separately from item lines; reconstruct gross value using transaction-time prices | [Sales Revenue Analysis](https://github.com/libana3012-pixel/Sales-Revenue-Analysis) |
| SQL: Customers | Start from registered customers, using a left join so people with no purchases are not lost | [Customer Sales Analysis](https://github.com/libana3012-pixel/Customer-Sales-Analysis) |
| Python: Cohorts | Use next-calendar-month follow-up; report the final cohort as not observable when follow-up is missing | [Customer cohorts](projects/customer-cohorts/README.md) |
| Python: Data quality | Validate IDs, quantities and prices with both passing and deliberately failing fixtures | [Data quality](projects/data-quality/README.md) |
| Reconciliation | Recalculate illustrative retail figures in a second language and compare expected values | [Sales cross-check](python/README.md) |

The table groups work by technical theme rather than assigning invented completion dates to individual files.

## 1 October 2026 | Public portfolio consolidation

The four existing public repositories were structured for external reading. This Data Analytics collection received its public-safe project files, step-by-step method notes, source-field guides, a [workflow explanation](WORKFLOW.md) and automated [GitHub verification](.github/workflows/verify.yml). The check passed after publication. Original practice and file-creation dates are not inferred from the date of this consolidation.

## October 2026 | Current work and next milestones

| Period | Work to undertake | Evidence required to mark complete | Status |
| --- | --- | --- | --- |
| Early October | Review the SQL cases and annotate the reason for each query and validation decision | Updated query explanation, corresponding tested code | Planned |
| Week 2 | Improve Python edge cases and test coverage | New unit tests and a passing workflow | Planned |
| Week 3 | Build an actual Power BI report from the fictional sales case | Real report or genuine screenshots, validated against SQL | Planned |
| Week 4 | Reconcile SQL, Python and Power BI results against one common source | Reproducible source-to-report comparison | Planned |

[Power BI](powerbi/README.md) and [Fabric](fabric/README.md) remain documented plans until there is working, verified output. An October target is not marked complete simply because it appears on the timeline.

## How future progress will be recorded

Add an entry **after the work takes place**, using its actual date:

```markdown
### YYYY-MM-DD — Specific improvement
Question: What problem did I address?
Tools: Which tools did I use?
Reason: Why was this action needed?
Change: Which file, calculation or test changed? Link to it.
Result: What was verified?
Next: What remains?
```

This timeline describes the learning sequence while GitHub's commit history continues to show the actual publication and change dates.
