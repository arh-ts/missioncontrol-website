# Shared V3 system
LOCKUP='/_blob/5f444ae733218df8443956ffe7496978'; MARKDEEP='/_blob/0f7e7d87d6394b84028f82c7a752723a'
V={'overhead':('a60c2c0bd7da2d874191da3a46feb609','4cee990f4f6e40fa8c1ed5e661a22ed9'),
   'leader':('2adfa15d353451be6038078795e3103f','22525d641ae94f0fc2df366f127f4188'),
   'whiteboard':('7d530c71ddd6c65481543937e9c81a26','b4f5dcc33ea1ea6cbc0fd817b8451ab5'),
   'factory':('36d1c3a4445feeeff6e1c607ba4462d3','7c381692a494be53b7a0c56a74d7aecf'),
   'call':('452f36bd032df4a4e252718e08a0b13f','3bb593c211c6ef064d73709b54adcb6a')}
TANGLE='/_blob/4252a436427190d8843b53d6fc9a088f'; CLEAR='/_blob/fdaba4287c5f3bd30007dfd3f57a8633'

def video(k,label,style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover"):
    m,p=V[k]
    return f'<video src="/_blob/{m}" poster="/_blob/{p}" autoplay="" muted="" loop="" playsinline="" aria-label="{label}" style="{style}"></video>'

HELMET = """<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600&amp;family=Inter:wght@400;500;600&amp;display=swap" rel="stylesheet">
<style>
body{margin:0;background:#FFFFFF}
*{box-sizing:border-box}
a{color:inherit;text-decoration:none}
h1,h2,h3{text-wrap:balance}p{text-wrap:pretty}
.d{font-family:'Inter Tight',system-ui,sans-serif}
.nl{transition:color .2s ease}.nl:hover{color:#0A0B0D !important}
.b1{transition:background .2s ease,transform 150ms cubic-bezier(0.32,0.72,0,1)}
.b1:hover{background:#2A2D33 !important}
.b1:active,.b2:active{transform:scale(0.98)}
.b2{transition:border-color .2s ease}
.b2:hover{border-color:#0A0B0D !important}
.bw{transition:background .2s ease}.bw:hover{background:#E9EBEE !important}
.ar{display:inline-block;transition:transform .2s ease}
a:hover .ar,button:hover .ar{transform:translateX(3px)}
.row{transition:background .2s ease}.row:hover{background:#F7F7F8}
.tb{transition:color .2s ease,border-color .2s ease,background .2s ease}
.tb:hover{color:#0A0B0D !important}
.tb:focus-visible,.fq:focus-visible{outline:2px solid #0A0B0D;outline-offset:2px}
.fq{transition:background .2s ease}.fq:hover{background:#FAFAFB}
.in{transition:border-color .2s ease}.in:hover{border-color:#9AA0A8 !important}
.in:focus{outline:2px solid #0A0B0D;outline-offset:1px;border-color:#0A0B0D !important}
@keyframes fade{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
.fade{animation:fade 360ms cubic-bezier(0.32,0.72,0,1) both}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.35}}
.live{animation:pulse 2s ease-in-out infinite}
.mnav{display:none;position:relative}.mnav>summary{list-style:none;cursor:pointer;display:inline-flex;align-items:center;height:38px;padding:0 12px;border:1px solid #DADCE0;border-radius:8px;font-size:14px;font-weight:500;color:#0A0B0D}.mnav>summary::-webkit-details-marker{display:none}.mnav[open]>summary{border-color:#0A0B0D}.mnav-p{position:absolute;right:0;top:46px;min-width:220px;background:#FFFFFF;border:1px solid #EEEFF1;border-radius:12px;box-shadow:0 24px 48px -24px rgba(10,11,13,0.25);padding:8px;display:flex;flex-direction:column}.mnav-p a{padding:10px 12px;border-radius:8px;font-size:15px;color:#0A0B0D}.mnav-p a:hover{background:#F5F6F7}.mnav summary:focus-visible{outline:2px solid #0A0B0D;outline-offset:2px}@media (max-width:980px){.mnav{display:block}}
@media (max-width:980px){.navlinks{display:none !important}.signin{display:none !important}.side{display:none !important}}
@media (prefers-reduced-motion:reduce){.fade,.live{animation:none}}
</style>
</helmet>"""

PAGES=[('Platform-V3.dc.html','Platform','plat'),('HowWeWork-V3.dc.html','How we work','how'),('Industries-V3.dc.html','Industries','ind'),('Security-V3.dc.html','Security','sec'),('Company-V3.dc.html','Company','co'),('/news','Newsroom','news')]
def header(active=''):
    links=''.join(f'<a class="nl" href="{h}"{" aria-current=\"page\"" if k==active else ""} style="color:{"#0A0B0D" if k==active else "#5B616B"}">{l}</a>' for h,l,k in PAGES)
    return f"""<header style="position:sticky;top:0;z-index:30;background:rgba(255,255,255,0.86);backdrop-filter:saturate(180%) blur(16px);border-bottom:1px solid #EEEFF1">
<nav aria-label="Primary" style="max-width:1200px;margin:0 auto;padding:0 24px;height:64px;display:flex;align-items:center;justify-content:space-between;gap:24px">
<a href="Home-V3.dc.html" aria-label="Mission Control home" style="display:inline-flex;align-items:center"><img src="{LOCKUP}" alt="Mission Control" style="height:22px;width:auto;display:block"></a>
<div class="navlinks" style="display:flex;gap:30px;font-size:14px;font-weight:500;align-items:center">{links}</div>
<div style="display:flex;align-items:center;gap:10px">
<details class="mnav"><summary aria-label="Open menu">Menu</summary><div class="mnav-p"><a href="Platform-V3.dc.html">Platform</a><a href="HowWeWork-V3.dc.html">How we work</a><a href="Industries-V3.dc.html">Industries</a><a href="Security-V3.dc.html">Security</a><a href="Company-V3.dc.html">Company</a><a href="/news">Newsroom</a></div></details>
<a href="Briefing-V3.dc.html" class="b1" style="display:inline-flex;align-items:center;height:38px;padding:0 16px;border-radius:8px;background:#0A0B0D;color:#FFFFFF;font-size:14px;font-weight:500">Book a briefing</a>
</div>
</nav>
</header>"""

FOOTER=f"""<footer style="border-top:1px solid #EEEFF1">
<div style="max-width:1200px;margin:0 auto;padding:56px 24px 32px">
<div style="display:flex;flex-wrap:wrap;gap:40px;justify-content:space-between">
<div style="flex:1 1 260px;max-width:320px"><img src="{LOCKUP}" alt="Mission Control" style="height:22px;width:auto;display:block"><p style="margin:16px 0 0;font-size:14px;line-height:1.6;color:#5B616B">Operational intelligence for services organisations.</p></div>
<div style="flex:2 1 480px;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(140px,100%),1fr));gap:28px;font-size:14px">
<div style="display:flex;flex-direction:column;gap:10px"><span style="font-weight:600">Platform</span><a class="nl" href="Platform-V3.dc.html" style="color:#5B616B">Overview</a><a class="nl" href="Platform-V3.dc.html#map" style="color:#5B616B">Live map</a><a class="nl" href="Platform-V3.dc.html#automations" style="color:#5B616B">Automations</a><a class="nl" href="Platform-V3.dc.html#connect" style="color:#5B616B">Connections</a></div>
<div style="display:flex;flex-direction:column;gap:10px"><span style="font-weight:600">Solutions</span><a class="nl" href="Industries-V3.dc.html" style="color:#5B616B">Industries</a><a class="nl" href="HowWeWork-V3.dc.html" style="color:#5B616B">How we work</a><a class="nl" href="Industries-V3.dc.html#roadmap" style="color:#5B616B">Roadmap</a></div>
<div style="display:flex;flex-direction:column;gap:10px"><span style="font-weight:600">Company</span><a class="nl" href="Company-V3.dc.html" style="color:#5B616B">About</a><a class="nl" href="Security-V3.dc.html" style="color:#5B616B">Security</a><a class="nl" href="/news" style="color:#5B616B">Newsroom</a><a class="nl" href="Briefing-V3.dc.html" style="color:#5B616B">Book a briefing</a><a class="nl" href="mailto:hello@missioncntrl.io" style="color:#5B616B">hello@missioncntrl.io</a></div>
</div></div>
<div style="margin-top:48px;padding-top:20px;border-top:1px solid #EEEFF1;display:flex;flex-wrap:wrap;justify-content:space-between;gap:12px;font-size:12px;color:#8A9099"><span>© 2026 Mission Control. All rights reserved.</span><span style="display:flex;gap:18px"><a class="nl" href="/privacy">Privacy</a><a class="nl" href="/terms">Terms</a><a class="nl" href="/news/feed.xml">RSS</a></span></div>
</div></footer>"""

def cta(title='See your organisation from above.', body='A 30-minute briefing with our team. We walk through a live map and tell you plainly whether Mission Control is a fit.', vid='call'):
    return f"""<section style="padding:128px 24px 96px">
<div style="max-width:1200px;margin:0 auto;position:relative;border-radius:16px;overflow:hidden;background:#0A0B0D;min-height:440px;display:flex;align-items:center">
{video(vid,'A business leader on a video call.')}
<div aria-hidden="true" style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(10,11,13,0) 25%,rgba(10,11,13,0.86) 62%)"></div>
<div style="position:relative;margin-left:auto;max-width:480px;padding:56px 48px;color:#FFFFFF">
<h2 class="d" style="margin:0;font-weight:500;font-size:clamp(30px,3.2vw,44px);line-height:1.06;letter-spacing:-0.03em">{title}</h2>
<p style="margin:16px 0 0;font-size:16px;line-height:1.6;color:#C9CED4">{body}</p>
<div style="margin-top:28px;display:flex;flex-wrap:wrap;gap:10px"><a href="Briefing-V3.dc.html" class="bw" style="display:inline-flex;align-items:center;gap:8px;min-height:46px;padding:0 20px;border-radius:8px;background:#FFFFFF;color:#0A0B0D;font-size:15px;font-weight:500">Book a briefing <span class="ar" aria-hidden="true">→</span></a></div>
</div></div></section>"""

def eyebrow(t, color='#157A36'): return f'<p style="margin:0;font-size:14px;font-weight:500;color:{color}">{t}</p>'
H2="margin:14px 0 0;font-weight:500;font-size:clamp(30px,3.2vw,42px);line-height:1.1;letter-spacing:-0.03em"
H1="margin:24px 0 0;font-weight:500;font-size:clamp(40px,4.8vw,60px);line-height:1.04;letter-spacing:-0.035em"
LEAD="margin:20px 0 0;font-size:17px;line-height:1.6;color:#5B616B"
CARD="border:1px solid #EEEFF1;border-radius:12px;background:#FFFFFF"
def h2(t, extra=''): return f'<h2 class="d" style="{H2}{extra}">{t}</h2>'
def btns(primary='Book a briefing', href='Briefing-V3.dc.html', secondary=None, shref='#'):
    s=f'<a href="{href}" class="b1" style="display:inline-flex;align-items:center;gap:8px;min-height:46px;padding:0 20px;border-radius:8px;background:#0A0B0D;color:#FFFFFF;font-size:15px;font-weight:500">{primary} <span class="ar" aria-hidden="true">→</span></a>'
    if secondary: s+=f'<a href="{shref}" class="b2" style="display:inline-flex;align-items:center;min-height:46px;padding:0 20px;border-radius:8px;border:1px solid #DADCE0;color:#0A0B0D;font-size:15px;font-weight:500">{secondary}</a>'
    return f'<div style="margin-top:28px;display:flex;flex-wrap:wrap;gap:10px">{s}</div>'

def appframe(inner, title='Mission Control · Illustrative data', minh=420):
    return f"""<div style="border:1px solid #E7E8EB;border-radius:14px;overflow:hidden;background:#FFFFFF;box-shadow:0 1px 2px rgba(10,11,13,0.04),0 40px 80px -40px rgba(10,11,13,0.22)">
<div style="height:40px;display:flex;align-items:center;gap:14px;padding:0 14px;border-bottom:1px solid #EEEFF1;background:#FAFAFB"><span aria-hidden="true" style="display:flex;gap:6px"><span style="width:10px;height:10px;border-radius:50%;background:#E2E4E7"></span><span style="width:10px;height:10px;border-radius:50%;background:#E2E4E7"></span><span style="width:10px;height:10px;border-radius:50%;background:#E2E4E7"></span></span><span style="font-size:12px;color:#8A9099">{title}</span></div>
<div style="min-height:{minh}px">{inner}</div></div>"""

def faq_script_items(items):
    import json
    return json.dumps(items)

def doc(title, body, script, h):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
{HELMET}
<div style="font-family:'Inter',system-ui,sans-serif;color:#0A0B0D;background:#FFFFFF;-webkit-font-smoothing:antialiased;font-feature-settings:'ss01','cv11'">
{body}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1440,"height":{h}}}}}'>
{script}
</script>
</body>
</html>
"""

FAQ_MARKUP = """<div style="border-top:1px solid #EEEFF1">
<sc-for list="{{faqs}}" as="f"><div style="border-bottom:1px solid #EEEFF1"><button type="button" class="fq" onClick="{{f.toggle}}" aria-expanded="{{f.open}}" style="width:100%;display:flex;justify-content:space-between;align-items:center;gap:20px;text-align:left;border:0;background:transparent;padding:20px 4px;min-height:44px;cursor:pointer;font:inherit;font-size:17px;font-weight:500;color:#0A0B0D">{{f.q}}<span aria-hidden="true" style="flex:none;font-size:20px;color:#8A9099">{{f.sign}}</span></button><sc-if value="{{f.isOpen}}" hint-placeholder-val="{{false}}"><p class="fade" style="margin:0;padding:0 4px 22px;max-width:680px;font-size:15px;line-height:1.65;color:#5B616B">{{f.a}}</p></sc-if></div></sc-for>
</div>"""
def faq_js(items):
    import json
    return """var faqItems = %s;
    var faqs = faqItems.map(function (f, i) { var open = self.state.faq === i; return { q: f[0], a: f[1], isOpen: open, open: open ? 'true' : 'false', sign: open ? '−' : '+', toggle: function () { self.setState({ faq: open ? -1 : i }); } }; });""" % json.dumps(items)
