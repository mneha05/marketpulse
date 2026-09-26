from __future__ import annotations
import html

def render(domains,markets):
    dr="".join(f"<tr><td>{html.escape(k)}</td><td>{v['top10_keywords']}</td><td>{v['estimated_traffic']:,.0f}</td><td>{v['share_of_voice']:.1%}</td></tr>" for k,v in sorted(domains.items(),key=lambda kv:kv[1]['share_of_voice'],reverse=True))
    mr="".join(f"<tr><td>{html.escape(k)}</td><td>${v['start_usd_m']:,.0f}M</td><td>${v['end_usd_m']:,.0f}M</td><td>{v['cagr']:.1%}</td></tr>" for k,v in markets.items())
    return f'''<!doctype html><meta charset="utf-8"><title>MarketPulse</title><style>body{{font:16px system-ui;background:#0a0e18;color:#edf2ff;max-width:1050px;margin:40px auto;padding:0 20px}}table{{width:100%;border-collapse:collapse}}td,th{{padding:11px;border-bottom:1px solid #2c3548;text-align:left}}h1{{font-size:44px}}</style><h1>MarketPulse</h1><p>Competitive search visibility + market growth analysis</p><h2>Competitive visibility</h2><table><tr><th>Domain</th><th>Top-10 keywords</th><th>Traffic</th><th>Share of voice</th></tr>{dr}</table><h2>Market growth</h2><table><tr><th>Segment</th><th>Start</th><th>End</th><th>CAGR</th></tr>{mr}</table>'''
