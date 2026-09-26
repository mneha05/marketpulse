from __future__ import annotations
import argparse,json
from pathlib import Path
from .demo import generate
from .analysis import semrush,market
from .export import bi_exports
from .report import render

def main():
    p=argparse.ArgumentParser(prog="marketpulse"); sub=p.add_subparsers(dest="cmd",required=True)
    d=sub.add_parser("demo");d.add_argument("--out",type=Path,default=Path("demo-output"))
    a=sub.add_parser("analyze");a.add_argument("semrush",type=Path);a.add_argument("statista",type=Path);a.add_argument("--out",type=Path,default=Path("market-output"))
    args=p.parse_args()
    if args.cmd=="demo": kw,m=generate(args.out); out=args.out
    else: kw,m,out=args.semrush,args.statista,args.out; out.mkdir(parents=True,exist_ok=True)
    ds=semrush(kw); ms=market(m); bi_exports(out,ds,ms); (out/"analysis.json").write_text(json.dumps({"domains":ds,"markets":ms},indent=2)); (out/"index.html").write_text(render(ds,ms)); print(out/"index.html")
