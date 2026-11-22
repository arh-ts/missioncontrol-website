import json
marks = [
 ("A","Route","Recommended","Two points and the route between them. Work leaving one place and arriving at the next. Calm, ownable, and it reads at favicon size.",
  '<path d="M7 25 C7 14, 25 18, 25 7" fill="none" stroke="{ink}" stroke-width="3" stroke-linecap="round"/><circle cx="7" cy="25" r="4.2" fill="{ink}"/><circle cx="25" cy="7" r="4.2" fill="{acc}"/>'),
 ("B","Flow M","","The M drawn as one continuous route through three stops. The green node is the hand-off you are watching.",
  '<path d="M6 26 V8 L16 19 L26 8 V26" fill="none" stroke="{ink}" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="16" cy="19" r="3.6" fill="{acc}"/>'),
 ("C","Waypoint","","A map pin with a live dot inside. Says 'map' instantly, and the dot says 'live'. Most literal of the set.",
  '<path d="M16 29 C16 29 6.5 19.8 6.5 12.6 A9.5 9.5 0 0 1 25.5 12.6 C25.5 19.8 16 29 16 29Z" fill="{ink}"/><circle cx="16" cy="12.6" r="4" fill="{acc}"/>'),
 ("D","Junction","","An evolution of today's mark: four hand-offs meeting at one point. Keeps some equity, loses the busy petals.",
  '<g stroke="{ink}" stroke-width="3" stroke-linecap="round"><path d="M16 3.5 V9.5"/><path d="M28.5 16 H22.5"/><path d="M16 28.5 V22.5"/><path d="M3.5 16 H9.5"/></g><circle cx="16" cy="16" r="4.4" fill="{acc}"/>'),
 ("E","Folded map","","A folded map with a route across it. The most story-led option: the map of your business, unfolded.",
  '<path d="M4 8 L12 5 L20 8 L28 5 V24 L20 27 L12 24 L4 27Z" fill="none" stroke="{ink}" stroke-width="2.4" stroke-linejoin="round"/><path d="M12 5 V24 M20 8 V27" stroke="{ink}" stroke-width="1.6" opacity="0.45"/><path d="M8 20 C11 13 15 21 18.5 14.5 S23.5 10.5 24 11" fill="none" stroke="{acc}" stroke-width="2.4" stroke-linecap="round"/><circle cx="24" cy="11" r="2.4" fill="{acc}"/>'),
 ("F","Orbit","","Mission control in the original sense: a tracking ring with one object in motion. Most 'product' feeling, least literal.",
  '<path d="M16 5 A11 11 0 1 1 5 16" fill="none" stroke="{ink}" stroke-width="3" stroke-linecap="round"/><circle cx="8.3" cy="8.3" r="3.2" fill="{acc}"/><circle cx="16" cy="16" r="3.4" fill="{ink}"/>'),
]
GREEN="#22C55E"; INK="#0E1512"
def svg(m,size,ink,acc,label=False):
    a = 'role="img" aria-label="Mission Control mark, option %s"'%m[0] if label else 'aria-hidden="true"'
    return '<svg width="%d" height="%d" viewBox="0 0 32 32" %s>%s</svg>'%(size,size,a,m[4].format(ink=ink,acc=acc).replace("/>","></path>").replace("<circle","<circle").replace("></path>","/>"))
def fix(s):
    # close elements explicitly for dc format
    import re
    s=re.sub(r'<(path|circle)([^>]*)/>',r'<\1\2></\1>',s)
    return s
rows=[]
for m in marks:
    badge = '<span style="font-size:12px;color:#14532D;background:#DCF5E4;border-radius:999px;padding:4px 10px">Recommended</span>' if m[2] else ''
    wm_w = 500 if m[0]!="F" else 400
    rows.append(f'''
<section style="display:grid;grid-template-columns:300px 1fr 1fr 220px;gap:20px;align-items:stretch">
<div style="padding:8px 8px 8px 0">
<div style="display:flex;align-items:center;gap:10px"><span style="font-family:'Geist Mono',monospace;font-size:13px;color:#56605A">{m[0]}</span>{badge}</div>
<h2 style="margin:12px 0 0;font-weight:400;font-size:34px;letter-spacing:-0.03em">{m[1]}</h2>
<p style="margin:12px 0 0;font-size:15px;line-height:1.6;color:#56605A">{m[3]}</p>
<div style="margin-top:20px;display:flex;align-items:center;gap:14px">{fix(svg(m,16,INK,GREEN))}{fix(svg(m,24,INK,GREEN))}{fix(svg(m,40,INK,GREEN,True))}</div>
</div>
<div style="background:#F7F8F5;border:1px solid #E2E6E1;border-radius:16px;display:flex;align-items:center;justify-content:center;gap:14px;min-height:220px">{fix(svg(m,46,INK,"{{accentDeep}}"))}<span style="font-size:38px;font-weight:{wm_w};letter-spacing:-0.03em;color:#0E1512">Mission Control</span></div>
<div style="background:#0B110E;border-radius:16px;display:flex;align-items:center;justify-content:center;gap:14px;min-height:220px">{fix(svg(m,46,"#FFFFFF","{{accent}}"))}<span style="font-size:38px;font-weight:{wm_w};letter-spacing:-0.03em;color:#FFFFFF">Mission Control</span></div>
<div style="background:#FFFFFF;border:1px solid #E2E6E1;border-radius:16px;display:flex;align-items:center;justify-content:center;min-height:220px"><div style="width:120px;height:120px;border-radius:28px;background:#0E1512;display:flex;align-items:center;justify-content:center;box-shadow:0 20px 40px -20px rgba(14,21,18,0.5)">{fix(svg(m,68,"#FFFFFF","{{accent}}"))}</div></div>
</section>''')
html=f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Mission Control logo options</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600&amp;family=Geist+Mono:wght@400;500&amp;display=swap" rel="stylesheet">
<style>
body{{margin:0}}
</style>
</helmet>
<div style="width:1440px;box-sizing:border-box;padding:80px;background:#FFFFFF;font-family:'Geist',system-ui,sans-serif;color:#0E1512;-webkit-font-smoothing:antialiased">
<p style="margin:0;font-family:'Geist Mono',monospace;font-size:13px;letter-spacing:0.06em;text-transform:uppercase;color:#15803D">Mission Control · Logo exploration · V1</p>
<h1 style="margin:20px 0 0;font-weight:300;font-size:84px;line-height:0.95;letter-spacing:-0.05em">Six directions for the mark.</h1>
<p style="margin:24px 0 0;max-width:760px;font-size:19px;line-height:1.6;color:#3B4540">Every option is built on the same idea: a live map of how work moves. Each is shown at small sizes, on light, on dark and as an app icon. Wordmark is Geist. Swap the accent colour in the panel on the right.</p>
<div style="margin-top:28px;display:grid;grid-template-columns:300px 1fr 1fr 220px;gap:20px;font-family:'Geist Mono',monospace;font-size:12px;color:#56605A;text-transform:uppercase;letter-spacing:0.04em"><span>Idea and small sizes</span><span>On light</span><span>On dark</span><span>App icon</span></div>
<div style="margin-top:14px;display:grid;gap:28px">{"".join(rows)}
</div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"accent":{{"editor":"color","default":"#22C55E","options":["#22C55E","#3DDC84","#14B8A6","#4F7CFF","#FF7A45"]}},"$preview":{{"width":1440,"height":2400}}}}'>
class Component extends DCLogic {{
  renderVals() {{
    var accent = this.props.accent ?? '#22C55E';
    var deep = {{'#22C55E':'#16A34A','#3DDC84':'#16A34A','#14B8A6':'#0D9488','#4F7CFF':'#2F5BEA','#FF7A45':'#E35A22'}}[accent] || accent;
    return {{ accent: accent, accentDeep: deep }};
  }}
}}
</script>
</body>
</html>
'''
open('/home/claude/logo/project/Main.dc.html','w').write(html)
json.dump({"v":3,"createdOnFiles":{"v":1,"at":"2026-11-19T06:33:00Z"},"title":"Mission Control logo options","launch":{"view":"canvas"},"pages":[],"boards":{"Main.dc.html":{"x":0,"y":0,"w":1440,"h":2400,"title":"Logo options V1"}},"order":["Main.dc.html"],"notes":{},"designSystems":[]},open('/home/claude/logo/project/canvas.json','w'))
print(len(html))
