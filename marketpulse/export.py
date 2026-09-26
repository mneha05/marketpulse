from __future__ import annotations
import csv
from pathlib import Path

def bi_exports(out:Path,domains:dict,markets:dict):
    out.mkdir(parents=True,exist_ok=True)
    d=out/"fact_domain_visibility.csv"; m=out/"fact_market_growth.csv"
    with d.open("w",newline="",encoding="utf-8") as f:
        cols=["domain","keywords","top10_keywords","search_volume","estimated_traffic","visibility_score","avg_cpc","share_of_voice"]
        w=csv.DictWriter(f,fieldnames=cols);w.writeheader();
        for name,v in domains.items(): w.writerow({"domain":name,**v})
    with m.open("w",newline="",encoding="utf-8") as f:
        cols=["segment","start_year","end_year","start_usd_m","end_usd_m","cagr"]
        w=csv.DictWriter(f,fieldnames=cols);w.writeheader();
        for name,v in markets.items(): w.writerow({"segment":name,**v})
    return d,m
