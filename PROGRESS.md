# Development process | From marketing measurement to data analytics

[← Portfolio](README.md) · [Project guide](START-HERE.md) · [Tools and calculations](WORKFLOW.md)

The portfolio is organised into two learning chapters: **Marketing Analytics (February–31 March 2026)** and **Data Analytics (April–October 2026)**. The stages below explain the sequence of decisions behind the published case studies. They are a *project-development narrative*, not an invented daily GitHub activity record. Example datasets are synthetic; original GitHub commit dates are not changed.

## Chapter I: Marketing Analytics | February–31 March 2026

[Open the Marketing Analytics portfolio](https://github.com/libana3012-pixel/Marketing-Analytics-Portfolio).

| Development phase | Question or reason for the step | What the completed case contains |
| --- | --- | --- |
| 1. Clarify measurement | Website traffic alone does not prove useful visitor behaviour. What should a business measure? | [Website questions and proposed events](https://github.com/libana3012-pixel/Marketing-Analytics-Portfolio/tree/main/projects/00-marketing-measurement) |
| 2. Define the input | Before interpreting performance, distinguish users, sessions, actions and how the metrics are collected. | Example CSV, event definitions and source caveats |
| 3. Analyse campaigns | More clicks might simply reflect higher spend; compare outcomes and efficiency as well. | [Campaign calculations](https://github.com/libana3012-pixel/Marketing-Analytics-Portfolio/tree/main/projects/01-campaign-performance) |
| 4. Review organic search | Extra clicks could follow greater visibility, a higher CTR or both. | [Search analysis](https://github.com/libana3012-pixel/Marketing-Analytics-Portfolio/tree/main/projects/02-organic-search) |
| 5. Check and explain | A manager needs comprehensible definitions and reproducible numbers, not just figures. | Code, checks, KPI dictionary and management brief |

**Chapter outcome:** A structured, synthetic demonstration of measurement planning, campaign KPIs and SEO-style reporting. These are learning-period headings, not assertions that the current files were publicly committed during February or March.

## Chapter II: Data Analytics | April–October 2026

The following stages show how the published technical projects fit together. Some original SQL practice predates this public compilation; the stage labels describe the learning path, not invented file-creation dates.

### Stage 1 — Formulate the business questions
The [revenue case](https://github.com/libana3012-pixel/Sales-Revenue-Analysis) asks whether a change in sales value is connected to order count or basket value. The [customer case](https://github.com/libana3012-pixel/Customer-Sales-Analysis) asks who ordered once, returned or never ordered. These questions define what the subsequent data model and queries need to answer.

### Stage 2 — Understand and prepare the data
The SQL exercises use four related tables: customers, products, orders and order items. One order may have multiple item rows, so an item count cannot be treated as an order count. Transaction-time price is used when reconstructing sample sales value. The complete fictional SQL inputs and setup instructions are available in the two standalone repositories.

### Stage 3 — Build the first analyses
SQL joins, grouped values, CTEs and date-based comparisons produce the customer segments and monthly revenue results. The [revenue method](https://github.com/libana3012-pixel/Sales-Revenue-Analysis/blob/main/case-study/METHOD.md) and [customer method](https://github.com/libana3012-pixel/Customer-Sales-Analysis/blob/main/case-study/METHOD.md) explain why each operation was selected, with worked calculations.

### Stage 4 — Improve the comparisons
A cumulative repeat-purchase share does not offer all customers equal time to return. The [Python cohort exercise](projects/customer-cohorts/README.md) therefore compares each first-purchase cohort against its immediately following calendar month. Because the example ends in June, July follow-up for June's cohort is recorded as **not observable**, rather than zero. [See the calculation](projects/customer-cohorts/METHOD.md).

### Stage 5 — Add quality checks
Before relying on a reported value, test its underlying inputs. The [data-quality case](projects/data-quality/README.md) checks identifiers, reference values, quantities and prices using a passing fixture and a deliberately incorrect one. [See why each rule exists](projects/data-quality/METHOD.md).

### Stage 6 — Cross-check and present the results
The [Python sales check](python/README.md) independently recalculates illustrative revenue and order figures from embedded example lines. The published work also includes method notes, data dictionaries and [GitHub verification](.github/workflows/verify.yml). The Python script currently keeps a separate copy of its input lines rather than importing the SQL tables directly; that is a documented improvement opportunity.

### Public release — 1 October 2026
The existing work was assembled into four public repositories with detailed navigation, explanations and automated checks. GitHub records the actual commits on this date. This consolidation date is not presented as the date on which every original concept, exercise or skill was first developed.

## Dated records that precede the public release

These are records of relevant learning and analysis activity, **not dates assigned to the current public CSV files or retrospectively created GitHub commits**.

| Date | Recorded work | How it connects to the portfolio |
| --- | --- | --- |
| **13 August 2026** | Defined a recurring practical learning route: SQL first, then Power BI, then portfolio/GitHub projects; Python where needed. | Provides the technical direction behind this chapter. |
| **29–30 August 2026** | Worked through hands-on SQL exercises involving customers and purchases, including `SELECT`, `COUNT`, `JOIN` and fixing join errors. | The published SQL case studies extend these concepts into documented customer and revenue questions; they should not be mistaken for the exact earlier practice files. |
| **21 September 2026** | Worked on organising website analytics and KPI material into an analytical report. | A prior reporting activity relevant to defining metrics and explaining findings; the published Marketing Analytics examples remain independently fictional. |
| **1 October 2026** | Assembled and revised four public repositories, method explanations and automated checks. | Records the **publication and documentation milestone**, rather than claiming the underlying learning began that day. |

Where the exact date of an individual exercise is not established, its place in the earlier development sequence is described in the preceding stages without assigning a false timestamp.

## Remaining part of October | Next actual milestones

| Target period | Next action | What will count as complete | Status |
| --- | --- | --- | --- |
| Early October | Review SQL source and make the purpose of each query and validation rule explicit | Checked query explanations and successful verification | Planned |
| Second week | Extend Python test coverage and improve edge-case handling | Additional passing tests and documented cases | Planned |
| Third week | Build and validate a real Power BI report from the fictional revenue source | A working file or genuine report screenshots with matching SQL totals | Planned |
| Fourth week | Reconcile SQL, Python and Power BI against a common source | Reproducible comparison, including any differences | Planned |

[Power BI](powerbi/README.md) and [Microsoft Fabric](fabric/README.md) are documented as *planned work*, not delivered reports or deployed platforms. Planned milestones are updated only after actual implementation.

## How completed progress will be recorded

New, dated entries are added as work is done and linked to a file, test or actual commit:

```markdown
### YYYY-MM-DD | Specific change
Question: What was the problem?
Tools: What did I use?
Decision: Why did I choose this approach?
Work: What exactly changed? Link the file.
Verification: What result or test supports it?
Next: What still needs attention?
```

This makes the reasoning and gradual technical development visible without manufacturing a historical contribution graph.
