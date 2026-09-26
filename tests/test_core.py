from pathlib import Path
from marketpulse.demo import generate
from marketpulse.analysis import semrush,market
from marketpulse.export import bi_exports

def test_demo(tmp_path:Path):
    k,m=generate(tmp_path); d=semrush(k); g=market(m); assert len(d)==3 and len(g)==3
    assert abs(sum(v["share_of_voice"] for v in d.values())-1)<1e-9
    a,b=bi_exports(tmp_path/"bi",d,g); assert a.exists() and b.exists()
