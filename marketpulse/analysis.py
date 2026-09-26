from __future__ import annotations
import csv,math
from collections import defaultdict

def semrush(path):
    rows=list(csv.DictReader(open(path,encoding="utf-8"))); by=defaultdict(list)
    for r in rows: by[r["domain"]].append(r)
    out={}
    for d,rs in by.items():
        volume=sum(float(r["volume"]) for r in rs); traffic=sum(float(r["traffic"]) for r in rs)
        vis=sum(float(r["volume"])/(max(float(r["position"]),1)) for r in rs)
        top10=sum(1 for r in rs if float(r["position"])<=10)
        out[d]={"keywords":len(rs),"top10_keywords":top10,"search_volume":volume,"estimated_traffic":traffic,"visibility_score":vis,"avg_cpc":sum(float(r["cpc"]) for r in rs)/len(rs)}
    total=sum(v["visibility_score"] for v in out.values()) or 1
    for v in out.values(): v["share_of_voice"]=v["visibility_score"]/total
    return out

def market(path):
    rows=list(csv.DictReader(open(path,encoding="utf-8"))); by=defaultdict(list)
    for r in rows: by[r["segment"]].append((int(r["year"]),float(r["market_usd_m"])))
    out={}
    for seg,pts in by.items():
        pts=sorted(pts); years=pts[-1][0]-pts[0][0]; cagr=(pts[-1][1]/pts[0][1])**(1/years)-1 if years else 0
        out[seg]={"start_year":pts[0][0],"end_year":pts[-1][0],"start_usd_m":pts[0][1],"end_usd_m":pts[-1][1],"cagr":cagr}
    return out
