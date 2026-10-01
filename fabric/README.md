# Microsoft Fabric — proposed end-to-end build
**Status: architecture and learning plan; no live Fabric deployment claimed.**

## In everyday language
Right now, the SQL project keeps the shop data and asks questions about it. Fabric would let us put the data into one shared system, prepare it reliably and supply it to a reporting dashboard.

| Tool | Everyday explanation | Intended role |
| --- | --- | --- |
| OneLake | A shared storage location | Keep the source data together |
| Data Factory | A scheduled delivery service | Bring source files into the platform |
| Lakehouse | A workspace for organised data | Store and transform raw records |
| SQL endpoint | A way to ask structured questions | Produce reporting-ready tables |
| Power BI | A reporting screen | Show results to a business user |
| GitHub Actions | An automatic checklist | Test data/code before publication |

## Build stages
1. Ingest the synthetic CSV or equivalent SQL tables.
2. Add quality checks for duplicate IDs, missing references, invalid prices and quantities.
3. Transform into an order-level fact table with dimensions for customer, product and date.
4. Calculate the same core KPIs as in the standalone SQL project.
5. Compare all figures against the original SQL case study.
6. Connect a Power BI report; document actual refresh and permissions.

## What must exist before this is called complete
A working Fabric workspace and suitable capacity, pipeline configuration, SQL/lakehouse objects, recorded validation results, and screenshots of the real implementation. Until then, treat this as a proposal, not a portfolio achievement.
