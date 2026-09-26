# MarketPulse

**Market-intelligence analysis for SEMrush- and Statista-style exports with Tableau/Power BI-ready outputs.**

```text
SEMrush CSV export ─► keyword/domain normalization ─► visibility / traffic / share of voice
Statista CSV export ─► market time series ──────────► CAGR / segment growth
                                                   └► clean fact tables for Tableau / Power BI
```

## Run immediately

```bash
pip install -e .
marketpulse demo --out demo-output
```

Open `demo-output/index.html`.

The demo is deterministic synthetic data. For real analysis, replace the two demo CSVs with your exported SEMrush and Statista files using the same normalized columns.

## Competitive search metrics

For each domain the project computes:
- keyword count
- top-10 keyword count
- total search volume
- estimated traffic
- average CPC
- weighted visibility score
- competitive share of voice

## Market sizing

For each market segment it computes:
- first and final market size
- start/end years
- compound annual growth rate (CAGR)

## BI exports

`marketpulse analyze ...` produces flat fact tables designed to import directly into Tableau or Power BI:

```text
fact_domain_visibility.csv
fact_market_growth.csv
```

## Tooling boundary

This repo supports **exports from** named market-intelligence tools; it does not claim access to paid SEMrush or Statista accounts. The analysis code is fully runnable with the included demo generator.
