from __future__ import annotations
import csv,random
from pathlib import Path

def generate(out:Path):
    rng=random.Random(11); out.mkdir(parents=True,exist_ok=True)
    kw=out/"semrush_export.csv"; market=out/"statista_export.csv"
    domains=["nova.ai","atlas.dev","vectorlabs.io"]
    keywords=["gpu inference","ai compiler","cuda profiling","llm serving","distributed training","vector database","ai infrastructure","gpu debugging"]
    with kw.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=["domain","keyword","position","volume","cpc","traffic"]);w.writeheader()
        for d in domains:
            for k in keywords:
                w.writerow({"domain":d,"keyword":k,"position":rng.randint(1,80),"volume":rng.randrange(500,12000,100),"cpc":round(rng.uniform(1.2,18),2),"traffic":rng.randint(20,1800)})
    with market.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=["segment","year","market_usd_m"]);w.writeheader()
        for seg,base,g in [("AI infrastructure",42000,.23),("GPU software",18000,.28),("Observability",12000,.16)]:
            v=base
            for y in range(2024,2030): w.writerow({"segment":seg,"year":y,"market_usd_m":round(v,1)}); v*=1+g
    return kw,market
