# Interactive Drug Safety Explorer

Dashboard upgraded from a demo matrix to **real public openFDA FAERS drug/event counts** for selected common drugs. The repo is careful about interpretation: FAERS counts are spontaneous reports and cannot be read as incidence or causal risk without denominators and pharmacovigilance methods.

## Reproduce

```bash
python scripts/run_pipeline.py
```

## Outputs

- `data/openfda_drug_event_counts.csv`
- `data/openfda_event_matrix.csv`
- `outputs/top_adverse_events.csv`
- `outputs/drug_report_totals.csv`
- `figures/top_events.svg`
- `app.py`

## Analysis Report

Open `reports/analysis_report.html` for the hypothesis, public data provenance, process, outputs, and interpretation.

## Portfolio Note

This repository uses public data sources or clearly labelled synthetic demonstration data only. No employer-owned or confidential data are included.
