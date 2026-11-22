import json
B = {
 'lockup':'/_blob/5f444ae733218df8443956ffe7496978','lockupDark':'/_blob/2055b7d9e1689710c5225cf1503da78e',
 'mark':'/_blob/80665112aa38d425f1ca23677edbcf66','markDeep':'/_blob/0f7e7d87d6394b84028f82c7a752723a',
 'hero-cobalt':'/_blob/b15edd613000990e50e6de13905e9315','hero-lilac':'/_blob/85a5f77cb732004f9c7e92dcff4ef81a','hero-sun':'/_blob/377a9351e5307526778faa568054abf8',
 'tangle':'/_blob/4252a436427190d8843b53d6fc9a088f','clear':'/_blob/fdaba4287c5f3bd30007dfd3f57a8633','floor':'/_blob/cbb113c29db362cf47fd4484fc75bbc3'}
PAL = {
 'cobalt':dict(name='Cobalt',pop='#2B44F0',popInk='#FFFFFF',popTint='#EEF1FF',popText='#2B44F0',hot='#FF6A3D',hotText='#B5400F',hotTint='#FFF0EA'),
 'lilac':dict(name='Lilac',pop='#6C4CF5',popInk='#FFFFFF',popTint='#F3EFFF',popText='#5B3BE0',hot='#FF7A45',hotText='#B4470F',hotTint='#FFF1EA'),
 'sun':dict(name='Sunshine',pop='#FFD84D',popInk='#0B0F0D',popTint='#FFF6D6',popText='#7A5200',hot='#FF5A36',hotText='#B23314',hotTint='#FFEDE8'),
}
def rootvars(p):
    return ";".join([f"--pop:{p['pop']}",f"--popInk:{p['popInk']}",f"--popTint:{p['popTint']}",f"--popText:{p['popText']}",f"--hot:{p['hot']}",f"--hotText:{p['hotText']}",f"--hotTint:{p['hotTint']}",
      "--lime:#85EC68","--limeTint:#EEFCE8","--green:#1F9D47","--greenText:#157A36","--ink:#0B0F0D","--muted:#4F5753","--line:#E6E8EA","--soft:#F5F6F8"])

HELMET = """<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500..700&amp;family=Figtree:wght@400;500;600&amp;display=swap" rel="stylesheet">
<style>
body{margin:0;background:#FFFFFF}
*{box-sizing:border-box}
a{color:inherit;text-decoration:none}a:hover{color:var(--popText)}
h1,h2,h3{text-wrap:balance}p{text-wrap:pretty}
.hd{font-family:'Bricolage Grotesque',system-ui,sans-serif}
.nav a:hover{color:var(--ink)}
.btn{transition:transform 150ms cubic-bezier(0.32,0.72,0,1),box-shadow .2s ease,filter .2s ease}
.btn:hover{filter:brightness(0.94);box-shadow:0 10px 24px -12px rgba(11,15,13,0.45)}
.btn:active{transform:scale(0.97)}
.ghost{transition:background .2s ease}
.ghost:hover{background:#EEF0F2 !important;color:var(--ink) !important}
.arrow{display:inline-block;transition:transform .2s ease}
a:hover .arrow,button:hover .arrow{transform:translateX(4px)}
.lift{transition:transform .25s cubic-bezier(0.32,0.72,0,1),box-shadow .25s ease}
.lift:hover{transform:translateY(-3px);box-shadow:0 24px 40px -28px rgba(11,15,13,0.4)}
.tab{transition:background .2s ease,border-color .2s ease}
.tab:hover{border-color:var(--ink) !important}
.tab:focus-visible,.seg:focus-visible{outline:2px solid var(--popText);outline-offset:2px}
.mark{background:linear-gradient(transparent 58%,var(--lime) 58%,var(--lime) 92%,transparent 92%)}
@keyframes rise{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
.rise{animation:rise 420ms cubic-bezier(0.32,0.72,0,1) both}
@keyframes floaty{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}
.float{animation:floaty 5s ease-in-out infinite}
.in{transition:border-color .2s ease}
.in:hover{border-color:#9AA19D !important}
.in:focus{outline:2px solid var(--popText);outline-offset:1px}
@media (max-width:980px){.navlinks{display:none !important}}
@media (prefers-reduced-motion:reduce){.rise,.float{animation:none}}
</style>
</helmet>"""

def header(active=''):
    def l(href,label,key):
        cur = ' aria-current="page"' if key==active else ''
        col = 'var(--ink)' if key==active else 'var(--muted)'
        return f'<a href="{href}"{cur} style="padding:6px 0;color:{col}">{label}</a>'
    return f"""<header style="position:sticky;top:0;z-index:20;background:rgba(255,255,255,0.9);backdrop-filter:blur(14px);border-bottom:1px solid var(--line)">
<nav aria-label="Primary" style="max-width:1240px;margin:0 auto;padding:0 28px;height:70px;display:flex;align-items:center;justify-content:space-between;gap:24px">
<a href="Main.dc.html" aria-label="Mission Control home" style="display:inline-flex;align-items:center"><img src="{B['lockup']}" alt="Mission Control" style="height:26px;width:auto;display:block"></a>
<div class="navlinks nav" style="display:flex;gap:32px;font-size:15px;font-weight:500;align-items:center">
{l('Main.dc.html#how','How it works','how')}{l('Industries.dc.html','Industries','ind')}{l('Pricing.dc.html','Pricing','price')}{l('Main.dc.html#privacy','Privacy','priv')}
</div>
<a href="Pricing.dc.html#demo" class="btn" style="background:var(--pop);color:var(--popInk);font-weight:600;font-size:15px;padding:0 18px;height:44px;border-radius:12px;display:inline-flex;align-items:center;gap:8px">Book a demo <span class="arrow" aria-hidden="true">→</span></a>
</nav>
</header>"""

FOOTER = f"""<footer style="background:var(--soft);border-top:1px solid var(--line)">
<div style="max-width:1240px;margin:0 auto;padding:64px 28px 36px">
<div style="display:flex;flex-wrap:wrap;gap:48px;justify-content:space-between">
<div style="flex:1 1 280px;max-width:360px"><img src="{B['lockup']}" alt="Mission Control" style="height:26px;width:auto;display:block"><p style="margin:18px 0 0;font-size:15px;line-height:1.6;color:var(--muted)">A live map of how work moves through your business, and what is worth automating.</p></div>
<div style="flex:2 1 480px;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(140px,100%),1fr));gap:32px;font-size:15px">
<div style="display:flex;flex-direction:column;gap:10px"><span style="font-weight:600">Product</span><a href="Main.dc.html#how" style="color:var(--muted)">How it works</a><a href="Pricing.dc.html" style="color:var(--muted)">Pricing</a><a href="Main.dc.html#privacy" style="color:var(--muted)">Privacy</a></div>
<div style="display:flex;flex-direction:column;gap:10px"><span style="font-weight:600">Industries</span><a href="Industries.dc.html" style="color:var(--muted)">Services businesses</a><a href="Industries.dc.html#soon" style="color:var(--muted)">Coming soon</a></div>
<div style="display:flex;flex-direction:column;gap:10px"><span style="font-weight:600">Company</span><a href="Pricing.dc.html#demo" style="color:var(--muted)">Book a demo</a><a href="mailto:hello@missioncntrl.io" style="color:var(--muted)">hello@missioncntrl.io</a></div>
</div></div>
<div style="margin-top:56px;padding-top:20px;border-top:1px solid var(--line);display:flex;flex-wrap:wrap;justify-content:space-between;gap:12px;font-size:13px;color:var(--muted)"><span>© 2026 Mission Control</span><span style="display:flex;gap:18px"><a href="#" style="color:var(--muted)">Privacy policy</a><a href="#" style="color:var(--muted)">Terms</a></span></div>
</div></footer>"""

def tag(text, dot='var(--lime)', bg='#FFFFFF', border='var(--line)', color='var(--ink)'):
    return f'<span style="display:inline-flex;align-items:center;gap:8px;font-size:13px;font-weight:600;color:{color};background:{bg};border:1px solid {border};border-radius:999px;padding:6px 12px 6px 10px"><span aria-hidden="true" style="width:8px;height:8px;border-radius:50%;background:{dot}"></span>{text}</span>'

H2 = "margin:16px 0 0;font-family:'Bricolage Grotesque',system-ui,sans-serif;font-weight:600;font-size:clamp(30px,3.4vw,46px);line-height:1.08;letter-spacing:-0.025em"
CHK = '<svg width="18" height="18" viewBox="0 0 18 18" aria-hidden="true"><circle cx="9" cy="9" r="9" fill="var(--lime)"></circle><path d="M5.2 9.3l2.4 2.4 5-5.2" fill="none" stroke="#0B0F0D" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"></path></svg>'

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
{body}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1440,"height":{h}}}}}'>
{script}
</script>
</body>
</html>
"""

def home(pk):
    p = PAL[pk]
    hero = B['hero-'+pk]
    body = f"""<div style="{rootvars(p)};font-family:'Figtree',system-ui,sans-serif;color:var(--ink);background:#FFFFFF;-webkit-font-smoothing:antialiased">
{header()}
<main>
<!-- HERO -->
<section>
<div style="max-width:1240px;margin:0 auto;padding:72px 28px 88px;display:flex;flex-wrap:wrap;gap:48px 56px;align-items:center">
<div style="flex:1 1 420px;min-width:0">
{tag('Now onboarding services businesses')}
<h1 class="hd" style="margin:24px 0 0;font-weight:650;font-size:clamp(40px,4.6vw,64px);line-height:1.02;letter-spacing:-0.035em">See how work <span class="mark">really moves</span> through your business.</h1>
<p style="margin:22px 0 0;max-width:500px;font-size:19px;line-height:1.55;color:var(--muted)">Mission Control maps how work flows between your people and teams. See where it moves well, where it gets stuck, and exactly what is worth automating.</p>
<div style="margin-top:32px;display:flex;flex-wrap:wrap;gap:12px">
<a href="Pricing.dc.html#demo" class="btn" style="display:inline-flex;align-items:center;gap:10px;min-height:52px;padding:0 24px;border-radius:12px;background:var(--pop);color:var(--popInk);font-size:16px;font-weight:600">Book a demo <span class="arrow" aria-hidden="true">→</span></a>
<a href="#how" class="ghost" style="display:inline-flex;align-items:center;min-height:52px;padding:0 22px;border-radius:12px;background:var(--soft);color:var(--ink);font-size:16px;font-weight:600">How it works</a>
</div>
<ul style="margin:32px 0 0;padding:0;list-style:none;display:flex;flex-wrap:wrap;gap:10px 22px;font-size:14px;color:var(--muted)">
<li style="display:flex;align-items:center;gap:8px">{CHK}We set it up for you</li>
<li style="display:flex;align-items:center;gap:8px">{CHK}Works with your existing tools</li>
<li style="display:flex;align-items:center;gap:8px">{CHK}No new software for staff</li>
</ul>
</div>
<div style="flex:1.3 1 520px;min-width:0;position:relative">
<div style="position:relative;border-radius:28px;overflow:hidden;aspect-ratio:16/11;background:var(--popTint)">
<img src="{hero}" alt="A rendered map of work moving between teams. Most routes flow in green; one detour through an approvals step glows orange." style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover">
</div>
<div class="float" style="position:absolute;left:-18px;top:28px;background:#FFFFFF;border-radius:14px;padding:12px 16px;box-shadow:0 18px 40px -18px rgba(11,15,13,0.35);display:flex;align-items:center;gap:10px;font-size:14px;font-weight:600"><span style="width:10px;height:10px;border-radius:50%;background:var(--green)"></span>Live map · 6 teams</div>
<div class="float" style="position:absolute;left:24px;bottom:-22px;background:#FFFFFF;border-radius:16px;padding:16px 18px;box-shadow:0 22px 44px -20px rgba(11,15,13,0.4);min-width:220px;animation-delay:1.2s">
<div style="font-size:12px;font-weight:600;color:var(--hotText);text-transform:uppercase;letter-spacing:0.05em">Slowing down</div>
<div class="hd" style="margin-top:6px;font-size:20px;font-weight:600;letter-spacing:-0.01em">Approvals</div>
<div style="margin-top:2px;font-size:14px;color:var(--muted)">Work waits 2.4 days on average</div>
</div>
<div class="float" style="position:absolute;right:-14px;bottom:56px;background:var(--lime);border-radius:16px;padding:16px 18px;box-shadow:0 22px 44px -20px rgba(11,15,13,0.4);animation-delay:2.4s">
<div style="font-size:12px;font-weight:600;text-transform:uppercase;letter-spacing:0.05em">Worth automating</div>
<div class="hd" style="margin-top:4px;font-size:30px;font-weight:650;letter-spacing:-0.02em">46 hrs</div>
<div style="font-size:14px">a week, across 4 tasks</div>
</div>
<p style="margin:34px 0 0;text-align:right;font-size:12px;color:var(--muted)">Illustrative figures</p>
</div>
</div>
</section>

<!-- PROBLEM with before / after -->
<section style="background:var(--soft)">
<div style="max-width:1240px;margin:0 auto;padding:96px 28px;display:flex;flex-wrap:wrap;gap:48px 64px;align-items:center">
<div style="flex:1 1 380px;min-width:0">
{tag('The problem', dot='var(--hot)')}
<h2 style="{H2}">Your org chart shows who reports to whom. It doesn't show how work gets done.</h2>
<div style="margin-top:32px;display:grid;gap:18px">
<div style="display:flex;gap:14px"><span class="hd" style="flex:none;width:32px;height:32px;border-radius:10px;background:var(--hotTint);color:var(--hotText);display:inline-flex;align-items:center;justify-content:center;font-weight:700">1</span><div><div style="font-weight:600;font-size:17px">Hand-offs are invisible</div><p style="margin:4px 0 0;font-size:16px;line-height:1.55;color:var(--muted)">Work passes between people, inboxes and systems all day. Nobody sees the whole route.</p></div></div>
<div style="display:flex;gap:14px"><span class="hd" style="flex:none;width:32px;height:32px;border-radius:10px;background:var(--hotTint);color:var(--hotText);display:inline-flex;align-items:center;justify-content:center;font-weight:700">2</span><div><div style="font-weight:600;font-size:17px">Delays hide in the gaps</div><p style="margin:4px 0 0;font-size:16px;line-height:1.55;color:var(--muted)">A job sits in a queue for two days. No one notices until a customer does.</p></div></div>
<div style="display:flex;gap:14px"><span class="hd" style="flex:none;width:32px;height:32px;border-radius:10px;background:var(--hotTint);color:var(--hotText);display:inline-flex;align-items:center;justify-content:center;font-weight:700">3</span><div><div style="font-weight:600;font-size:17px">Automation is a guess</div><p style="margin:4px 0 0;font-size:16px;line-height:1.55;color:var(--muted)">You know some work is repetitive. Not which, how much, or what fixing it is worth.</p></div></div>
</div>
</div>
<div style="flex:1.2 1 500px;min-width:0">
<div role="group" aria-label="Compare" style="display:inline-flex;background:#FFFFFF;border:1px solid var(--line);border-radius:12px;padding:4px;gap:4px">
<button type="button" class="seg" onClick="{{{{showBefore}}}}" aria-pressed="{{{{beforeOn}}}}" style="{{{{beforeBtn}}}}">Without Mission Control</button>
<button type="button" class="seg" onClick="{{{{showAfter}}}}" aria-pressed="{{{{afterOn}}}}" style="{{{{afterBtn}}}}">With Mission Control</button>
</div>
<div style="margin-top:16px;position:relative;border-radius:24px;overflow:hidden;background:#FFFFFF;border:1px solid var(--line);aspect-ratio:16/10">
<sc-if value="{{{{isBefore}}}}" hint-placeholder-val="{{{{true}}}}"><img class="rise" src="{B['tangle']}" alt="A tangle of hand-offs between thirteen people, crossing in every direction." style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover"></sc-if>
<sc-if value="{{{{isAfter}}}}" hint-placeholder-val="{{{{false}}}}"><img class="rise" src="{B['clear']}" alt="The same thirteen people joined by one clear, bundled route." style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover"></sc-if>
<span style="{{{{capStyle}}}}">{{{{caption}}}}</span>
</div>
</div>
</div>
</section>

<!-- WHAT YOU SEE: bento -->
<section>
<div style="max-width:1240px;margin:0 auto;padding:104px 28px">
<div style="max-width:720px">{tag('What you see')}<h2 style="{H2}">Four things you have never been able to see.</h2></div>
<div style="margin-top:48px;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(500px,100%),1fr));gap:20px">

<article class="lift" style="border:1px solid var(--line);border-radius:24px;padding:32px;background:#FFFFFF">
<h3 class="hd" style="margin:0;font-weight:600;font-size:26px;letter-spacing:-0.02em">Where work slows down</h3>
<p style="margin:10px 0 0;font-size:16px;line-height:1.55;color:var(--muted)">Every step ranked by how long work waits there.</p>
<div aria-hidden="true" style="margin-top:24px;background:var(--soft);border-radius:16px;padding:20px;display:grid;gap:14px;font-size:14px">
<div><div style="display:flex;justify-content:space-between;font-weight:500"><span>Approvals</span><span style="color:var(--hotText)">2.4 days</span></div><div style="margin-top:6px;height:10px;border-radius:5px;background:#FFFFFF"><div style="width:92%;height:10px;border-radius:5px;background:var(--hot)"></div></div></div>
<div><div style="display:flex;justify-content:space-between;font-weight:500"><span>Waiting on client</span><span style="color:var(--hotText)">1.6 days</span></div><div style="margin-top:6px;height:10px;border-radius:5px;background:#FFFFFF"><div style="width:62%;height:10px;border-radius:5px;background:var(--hot);opacity:0.6"></div></div></div>
<div><div style="display:flex;justify-content:space-between;font-weight:500"><span>Onboarding</span><span style="color:var(--muted)">0.4 days</span></div><div style="margin-top:6px;height:10px;border-radius:5px;background:#FFFFFF"><div style="width:18%;height:10px;border-radius:5px;background:#C9CFCB"></div></div></div>
</div>
</article>

<article class="lift" style="border:1px solid var(--line);border-radius:24px;padding:32px;background:#FFFFFF">
<h3 class="hd" style="margin:0;font-weight:600;font-size:26px;letter-spacing:-0.02em">The moments it happened</h3>
<p style="margin:10px 0 0;font-size:16px;line-height:1.55;color:var(--muted)">Not just averages. Open any slowdown and see the real cases behind it.</p>
<div aria-hidden="true" style="margin-top:24px;background:var(--soft);border-radius:16px;padding:8px 20px;font-size:14px">
<div style="display:flex;gap:14px;padding:12px 0;border-bottom:1px solid #E2E5E8"><span style="flex:none;width:78px;color:var(--muted)">Tue 9:12</span><span>Job #4821 reached Approvals</span></div>
<div style="display:flex;gap:14px;padding:12px 0;border-bottom:1px solid #E2E5E8"><span style="flex:none;width:78px;color:var(--muted)">Wed 4:40</span><span>Reassigned, approver on leave</span></div>
<div style="display:flex;gap:14px;padding:12px 0"><span style="flex:none;width:78px;color:var(--hotText);font-weight:600">Fri 11:05</span><span>Approved. <strong style="font-weight:600">Waited 3 days 2 hours</strong></span></div>
</div>
</article>

<article class="lift" style="border-radius:24px;padding:32px;background:var(--limeTint)">
<h3 class="hd" style="margin:0;font-weight:600;font-size:26px;letter-spacing:-0.02em">What is working well</h3>
<p style="margin:10px 0 0;font-size:16px;line-height:1.55;color:var(--muted)">See the fastest route and the teams that move work cleanly, so you can copy them.</p>
<div aria-hidden="true" style="margin-top:24px;background:#FFFFFF;border-radius:16px;padding:22px">
<svg viewBox="0 0 440 84" width="100%" height="84"><path d="M20 44 H420" stroke="#E6E8EA" stroke-width="4" stroke-linecap="round"></path><path d="M20 44 H300" stroke="#1F9D47" stroke-width="4" stroke-linecap="round"></path><circle cx="20" cy="44" r="9" fill="#0B0F0D"></circle><circle cx="160" cy="44" r="9" fill="#1F9D47"></circle><circle cx="300" cy="44" r="9" fill="#1F9D47"></circle><circle cx="420" cy="44" r="9" fill="#FFFFFF" stroke="#C9CFCB" stroke-width="3"></circle><text x="6" y="78" font-family="Figtree" font-size="13" fill="#4F5753">Enquiry</text><text x="142" y="78" font-family="Figtree" font-size="13" fill="#4F5753">Quote</text><text x="280" y="78" font-family="Figtree" font-size="13" fill="#4F5753">Signed</text><text x="150" y="20" font-family="Figtree" font-size="13" font-weight="600" fill="#157A36">Team B: 1.2 days end to end</text></svg>
</div>
</article>

<article class="lift" style="border-radius:24px;padding:32px;background:var(--pop);color:var(--popInk)">
<div style="display:flex;justify-content:space-between;align-items:center;gap:12px"><h3 class="hd" style="margin:0;font-weight:600;font-size:26px;letter-spacing:-0.02em">What is worth automating</h3><span style="flex:none;font-size:12px;font-weight:700;background:var(--lime);color:#0B0F0D;border-radius:999px;padding:5px 10px">THE BIG ONE</span></div>
<p style="margin:10px 0 0;font-size:16px;line-height:1.55;opacity:0.85">Repetitive work, found and sized in hours, before anything is built.</p>
<div aria-hidden="true" style="margin-top:24px;background:#FFFFFF;color:#0B0F0D;border-radius:16px;padding:8px 20px;font-size:14px">
<div style="display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid #EEF0F2"><span>Copying enquiries into the CRM</span><strong style="font-weight:700">22 hrs/wk</strong></div>
<div style="display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid #EEF0F2"><span>Chasing missing documents</span><strong style="font-weight:700">15 hrs/wk</strong></div>
<div style="display:flex;justify-content:space-between;padding:12px 0"><span>Weekly status updates</span><strong style="font-weight:700">9 hrs/wk</strong></div>
</div>
</article>
</div>
</div>
</section>

<!-- THE UNLOCK -->
<section style="padding:0 28px">
<div style="max-width:1240px;margin:0 auto;background:var(--popTint);border-radius:32px;padding:72px 56px;display:flex;flex-wrap:wrap;gap:40px 56px;align-items:center">
<div style="flex:1 1 340px;min-width:0">
{tag('The unlock', dot='var(--pop)')}
<h2 style="{H2}">Automate what matters. Skip what doesn't.</h2>
<p style="margin:18px 0 0;max-width:440px;font-size:18px;line-height:1.6;color:var(--muted)">Most businesses automate the wrong things first. Mission Control ranks every opportunity by the time it gives back, so you start with the biggest win.</p>
</div>
<div style="flex:1.5 1 520px;min-width:0;background:#FFFFFF;border-radius:20px;box-shadow:0 30px 60px -40px rgba(11,15,13,0.45);overflow:hidden">
<div style="display:flex;justify-content:space-between;align-items:center;padding:18px 22px;border-bottom:1px solid var(--line)"><span class="hd" style="font-weight:600;font-size:18px">Automation shortlist</span><span style="font-size:12px;color:var(--muted)">Illustrative</span></div>
<div style="overflow-x:auto"><table style="width:100%;min-width:560px;border-collapse:collapse;font-size:15px">
<thead><tr style="text-align:left;font-size:13px;color:var(--muted)"><th style="padding:14px 22px;font-weight:500">Task</th><th style="padding:14px 22px;font-weight:500">Team</th><th style="padding:14px 22px;font-weight:500">Hrs a week</th><th style="padding:14px 22px;font-weight:500">Hrs back a year</th><th style="padding:14px 22px;font-weight:500">Status</th></tr></thead>
<tbody><sc-for list="{{{{autos}}}}" as="a"><tr style="border-top:1px solid var(--line)"><td style="padding:16px 22px;font-weight:500">{{{{a.task}}}}</td><td style="padding:16px 22px;color:var(--muted)">{{{{a.team}}}}</td><td style="padding:16px 22px">{{{{a.hrs}}}}</td><td style="padding:16px 22px;font-weight:700">{{{{a.year}}}}</td><td style="padding:16px 22px"><span style="{{{{a.chip}}}}">{{{{a.status}}}}</span></td></tr></sc-for></tbody>
</table></div>
<p style="margin:0;padding:12px 22px 18px;font-size:13px;color:var(--muted)">Hours back a year assumes 48 working weeks.</p>
</div>
</div>
</section>

<!-- HOW IT WORKS -->
<section id="how">
<div style="max-width:1240px;margin:0 auto;padding:104px 28px">
<div style="max-width:720px">{tag('How it works')}<h2 style="{H2}">Four steps. We do the heavy lifting.</h2></div>
<div role="group" aria-label="Steps" style="margin-top:40px;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(220px,100%),1fr));gap:12px">
<sc-for list="{{{{steps}}}}" as="s"><button type="button" class="tab" onClick="{{{{s.pick}}}}" aria-pressed="{{{{s.on}}}}" style="{{{{s.btn}}}}"><span style="{{{{s.num}}}}">{{{{s.n}}}}</span><span style="display:block;text-align:left"><span class="hd" style="display:block;font-size:20px;font-weight:600">{{{{s.title}}}}</span><span style="display:block;margin-top:2px;font-size:14px;color:var(--muted)">{{{{s.short}}}}</span></span></button></sc-for>
</div>
<div class="rise" style="margin-top:20px;background:var(--soft);border-radius:28px;padding:40px;display:flex;flex-wrap:wrap;gap:32px 48px;align-items:center">
<div style="flex:1 1 320px;min-width:0">
<div style="font-size:14px;font-weight:600;color:var(--popText)">Step {{{{cur.n}}}} of 4</div>
<h3 class="hd" style="margin:10px 0 0;font-weight:650;font-size:40px;letter-spacing:-0.03em">{{{{cur.title}}}}</h3>
<p style="margin:14px 0 0;max-width:420px;font-size:17px;line-height:1.6;color:var(--muted)">{{{{cur.body}}}}</p>
<div style="margin-top:22px;display:flex;flex-wrap:wrap;gap:8px"><sc-for list="{{{{cur.outputs}}}}" as="o"><span style="display:inline-flex;align-items:center;gap:8px;font-size:14px;font-weight:500;background:#FFFFFF;border-radius:999px;padding:8px 14px">{CHK}{{{{o}}}}</span></sc-for></div>
</div>
<div aria-hidden="true" style="flex:1.2 1 420px;min-width:0;background:#FFFFFF;border-radius:20px;padding:24px;box-shadow:0 24px 50px -36px rgba(11,15,13,0.4);min-height:280px">
<sc-if value="{{{{s1}}}}" hint-placeholder-val="{{{{true}}}}"><div style="display:grid;gap:10px;font-size:15px"><div class="hd" style="font-weight:600;font-size:17px;margin-bottom:6px">Connecting your tools</div><sc-for list="{{{{tools}}}}" as="t"><div style="display:flex;justify-content:space-between;align-items:center;padding:12px 14px;border:1px solid var(--line);border-radius:12px"><span>{{{{t.name}}}}</span><span style="{{{{t.chip}}}}">{{{{t.state}}}}</span></div></sc-for></div></sc-if>
<sc-if value="{{{{s2}}}}" hint-placeholder-val="{{{{false}}}}"><div><div class="hd" style="font-weight:600;font-size:17px">Live map</div><svg viewBox="0 0 460 230" width="100%" style="margin-top:10px"><g fill="none" stroke-linecap="round" stroke-width="3"><path d="M50 60 C120 30 170 40 220 60" stroke="#1F9D47"></path><path d="M220 60 C280 80 320 120 400 110" stroke="#1F9D47"></path><path d="M220 60 C200 120 160 160 120 180" stroke="{p['hot']}" stroke-dasharray="6 6"></path><path d="M120 180 C220 200 330 170 400 110" stroke="{p['hot']}" stroke-dasharray="6 6"></path></g><g font-family="Figtree" font-size="13" font-weight="600" text-anchor="middle"><rect x="10" y="44" width="84" height="32" rx="16" fill="#0B0F0D"></rect><text x="52" y="65" fill="#FFFFFF">Sales</text><rect x="172" y="44" width="100" height="32" rx="16" fill="#FFFFFF" stroke="#C9CFCB"></rect><text x="222" y="65" fill="#0B0F0D">Onboarding</text><rect x="352" y="94" width="96" height="32" rx="16" fill="#FFFFFF" stroke="#C9CFCB"></rect><text x="400" y="115" fill="#0B0F0D">Delivery</text><rect x="64" y="164" width="112" height="32" rx="16" fill="{p['hotTint']}" stroke="{p['hot']}"></rect><text x="120" y="185" fill="{p['hotText']}">Approvals</text></g></svg></div></sc-if>
<sc-if value="{{{{s3}}}}" hint-placeholder-val="{{{{false}}}}"><div><div style="display:flex;justify-content:space-between"><span class="hd" style="font-weight:600;font-size:17px">Monthly report</span><span style="font-size:13px;color:var(--muted)">October</span></div><div style="margin-top:16px;display:grid;grid-template-columns:repeat(3,1fr);gap:10px"><div style="background:var(--limeTint);border-radius:12px;padding:14px"><div style="font-size:12px;color:var(--muted)">Moving well</div><div class="hd" style="font-size:26px;font-weight:650">82%</div></div><div style="background:var(--hotTint);border-radius:12px;padding:14px"><div style="font-size:12px;color:var(--muted)">Slow spots</div><div class="hd" style="font-size:26px;font-weight:650">3</div></div><div style="background:var(--popTint);border-radius:12px;padding:14px"><div style="font-size:12px;color:var(--muted)">Hand-offs</div><div class="hd" style="font-size:26px;font-weight:650">12.4k</div></div></div><svg viewBox="0 0 420 90" width="100%" style="margin-top:14px"><g fill="#E6E8EA"><rect x="0" y="40" width="40" height="50" rx="6"></rect><rect x="60" y="30" width="40" height="60" rx="6"></rect><rect x="120" y="20" width="40" height="70" rx="6"></rect><rect x="180" y="34" width="40" height="56" rx="6"></rect><rect x="240" y="14" width="40" height="76" rx="6"></rect><rect x="300" y="10" width="40" height="80" rx="6"></rect></g><rect x="360" y="4" width="40" height="86" rx="6" fill="#1F9D47"></rect></svg><div style="font-size:13px;color:var(--muted)">Work moving on the fastest route, by month</div></div></sc-if>
<sc-if value="{{{{s4}}}}" hint-placeholder-val="{{{{false}}}}"><div style="display:grid;gap:10px;font-size:15px"><div class="hd" style="font-weight:600;font-size:17px;margin-bottom:6px">Ready to build</div><div style="display:flex;justify-content:space-between;align-items:center;padding:14px;border:1px solid var(--line);border-radius:12px"><span>Enquiries into the CRM<br><span style="font-size:13px;color:var(--muted)">22 hrs a week back</span></span><span style="font-size:13px;font-weight:600;background:var(--lime);border-radius:8px;padding:8px 12px">Live</span></div><div style="display:flex;justify-content:space-between;align-items:center;padding:14px;border:1px solid var(--line);border-radius:12px"><span>Chasing missing documents<br><span style="font-size:13px;color:var(--muted)">15 hrs a week back</span></span><span style="font-size:13px;font-weight:600;background:var(--pop);color:var(--popInk);border-radius:8px;padding:8px 12px">Building</span></div><div style="display:flex;justify-content:space-between;align-items:center;padding:14px;border:1px dashed #C9CFCB;border-radius:12px;color:var(--muted)"><span>One-click deploy</span><span style="font-size:13px">Coming soon</span></div></div></sc-if>
</div>
</div>
</div>
</section>

<!-- INDUSTRIES -->
<section style="background:var(--soft)">
<div style="max-width:1240px;margin:0 auto;padding:104px 28px">
<div style="display:flex;flex-wrap:wrap;justify-content:space-between;align-items:flex-end;gap:20px">
<div style="max-width:760px">{tag('Who it is for')}<h2 style="{H2}">Built for businesses where work moves through people and software.</h2></div>
<a href="Industries.dc.html" style="display:inline-flex;align-items:center;gap:8px;min-height:44px;font-size:15px;font-weight:600">All industries <span class="arrow" aria-hidden="true">→</span></a>
</div>
<div style="margin-top:44px;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(260px,100%),1fr));gap:14px">
<sc-for list="{{{{industries}}}}" as="i"><a href="Industries.dc.html" class="lift" style="display:block;background:#FFFFFF;border-radius:20px;padding:24px;min-height:150px"><span style="{{{{i.dot}}}}"></span><span class="hd" style="display:block;margin-top:18px;font-size:21px;font-weight:600;letter-spacing:-0.01em">{{{{i.name}}}}</span><span style="display:block;margin-top:6px;font-size:14px;line-height:1.5;color:var(--muted)">{{{{i.flow}}}}</span></a></sc-for>
<a href="Pricing.dc.html#demo" class="lift" style="display:flex;flex-direction:column;justify-content:space-between;background:var(--ink);color:#FFFFFF;border-radius:20px;padding:24px;min-height:150px"><span class="hd" style="font-size:21px;font-weight:600">Not on the list?</span><span style="display:inline-flex;align-items:center;gap:8px;font-size:15px;font-weight:600;color:var(--lime)">Ask us anyway <span class="arrow" aria-hidden="true">→</span></span></a>
</div>
</div>
</section>

<!-- COMING SOON -->
<section>
<div style="max-width:1240px;margin:0 auto;padding:104px 28px;display:flex;flex-wrap:wrap;gap:48px 64px;align-items:center">
<div style="flex:1.2 1 480px;min-width:0;position:relative">
<div style="border-radius:28px;overflow:hidden;background:#F2F4F1;aspect-ratio:16/11.5"><img src="{B['floor']}" alt="An isometric factory floor. Machines sit in a grid while work moves along dashed routes through the aisles." style="width:100%;height:100%;object-fit:cover;display:block"></div>
<span style="position:absolute;top:20px;left:20px;font-size:13px;font-weight:700;background:var(--hot);color:#FFFFFF;border-radius:999px;padding:7px 14px">COMING SOON</span>
</div>
<div style="flex:1 1 360px;min-width:0">
{tag('On the roadmap', dot='var(--hot)')}
<h2 style="{H2}">Next stop: the factory floor.</h2>
<p style="margin:18px 0 0;max-width:460px;font-size:18px;line-height:1.6;color:var(--muted)">Today we map work that moves through software. Next, work that moves through the real world: production lines, warehouses and robotics.</p>
<div style="margin-top:24px;display:flex;flex-wrap:wrap;gap:8px"><span style="font-size:14px;font-weight:500;background:var(--soft);border-radius:999px;padding:8px 14px">Manufacturing</span><span style="font-size:14px;font-weight:500;background:var(--soft);border-radius:999px;padding:8px 14px">Warehousing</span><span style="font-size:14px;font-weight:500;background:var(--soft);border-radius:999px;padding:8px 14px">Logistics</span><span style="font-size:14px;font-weight:500;background:var(--soft);border-radius:999px;padding:8px 14px">Robotics</span></div>
<a href="Pricing.dc.html#demo" style="margin-top:28px;display:inline-flex;align-items:center;gap:8px;min-height:44px;font-size:15px;font-weight:600">Join early access <span class="arrow" aria-hidden="true">→</span></a>
</div>
</div>
</section>

<!-- PRIVACY -->
<section id="privacy" style="background:var(--soft)">
<div style="max-width:1240px;margin:0 auto;padding:96px 28px">
<div style="max-width:760px">{tag('Privacy', dot='var(--green)')}<h2 style="{H2}">We map how work moves. Not what is inside it.</h2></div>
<div style="margin-top:44px;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(280px,100%),1fr));gap:16px">
<div style="background:#FFFFFF;border-radius:20px;padding:28px"><svg width="44" height="44" viewBox="0 0 44 44" aria-hidden="true"><rect width="44" height="44" rx="12" fill="var(--limeTint)"></rect><path d="M12 28 C16 18 22 30 32 16" fill="none" stroke="#1F9D47" stroke-width="2.4" stroke-linecap="round"></path><circle cx="12" cy="28" r="3" fill="#0B0F0D"></circle><circle cx="32" cy="16" r="3" fill="#1F9D47"></circle></svg><h3 class="hd" style="margin:18px 0 0;font-size:21px;font-weight:600">Movement, not content</h3><p style="margin:8px 0 0;font-size:16px;line-height:1.55;color:var(--muted)">We look at when work moves and where it goes. Not what is written in emails or documents.</p></div>
<div style="background:#FFFFFF;border-radius:20px;padding:28px"><svg width="44" height="44" viewBox="0 0 44 44" aria-hidden="true"><rect width="44" height="44" rx="12" fill="var(--popTint)"></rect><circle cx="17" cy="18" r="4" fill="none" stroke="var(--popText)" stroke-width="2.2"></circle><circle cx="27" cy="18" r="4" fill="none" stroke="var(--popText)" stroke-width="2.2"></circle><path d="M10 31c1.5-4 4-6 7-6s5.5 2 7 6M20 31c1.5-4 4-6 7-6s5.5 2 7 6" fill="none" stroke="var(--popText)" stroke-width="2.2" stroke-linecap="round"></path></svg><h3 class="hd" style="margin:18px 0 0;font-size:21px;font-weight:600">Your team is in the loop</h3><p style="margin:8px 0 0;font-size:16px;line-height:1.55;color:var(--muted)">We help you roll it out openly, with clear notice to staff. It is about the work, not the people.</p></div>
<div style="background:#FFFFFF;border-radius:20px;padding:28px"><svg width="44" height="44" viewBox="0 0 44 44" aria-hidden="true"><rect width="44" height="44" rx="12" fill="var(--hotTint)"></rect><rect x="12" y="13" width="20" height="18" rx="4" fill="none" stroke="var(--hotText)" stroke-width="2.2"></rect><path d="M17 22l3.5 3.5L27 19" fill="none" stroke="var(--hotText)" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"></path></svg><h3 class="hd" style="margin:18px 0 0;font-size:21px;font-weight:600">You choose the scope</h3><p style="margin:8px 0 0;font-size:16px;line-height:1.55;color:var(--muted)">Pick which teams and tools are included. Change it any time.</p></div>
</div>
</div>
</section>

<!-- PRICING TEASER -->
<section>
<div style="max-width:1240px;margin:0 auto;padding:104px 28px">
<div style="display:flex;flex-wrap:wrap;justify-content:space-between;align-items:flex-end;gap:20px">
<div style="max-width:720px">{tag('Pricing')}<h2 style="{H2}">Simple pricing, in three parts.</h2></div>
<a href="Pricing.dc.html" style="display:inline-flex;align-items:center;gap:8px;min-height:44px;font-size:15px;font-weight:600">See pricing <span class="arrow" aria-hidden="true">→</span></a>
</div>
<div style="margin-top:44px;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(280px,100%),1fr));gap:16px">
<div style="border:1px solid var(--line);border-radius:22px;padding:28px"><div style="font-size:13px;font-weight:600;color:var(--muted)">ONCE</div><div class="hd" style="margin-top:10px;font-size:28px;font-weight:600">Setup</div><p style="margin:8px 0 0;font-size:16px;line-height:1.55;color:var(--muted)">We install it, connect your tools and draw your first map.</p></div>
<div style="border-radius:22px;padding:28px;background:var(--pop);color:var(--popInk)"><div style="font-size:13px;font-weight:600;opacity:0.85">MONTHLY</div><div class="hd" style="margin-top:10px;font-size:28px;font-weight:600">Platform</div><p style="margin:8px 0 0;font-size:16px;line-height:1.55;opacity:0.85">Your live map, dashboard and regular reports.</p></div>
<div style="border-radius:22px;padding:28px;background:var(--limeTint)"><div style="font-size:13px;font-weight:600;color:var(--greenText)">AS YOU GO</div><div class="hd" style="margin-top:10px;font-size:28px;font-weight:600">Automations</div><p style="margin:8px 0 0;font-size:16px;line-height:1.55;color:var(--muted)">Priced one by one, only when the payoff is clear.</p></div>
</div>
</div>
</section>

<!-- CTA -->
<section style="padding:0 28px 96px">
<div style="max-width:1240px;margin:0 auto;position:relative;overflow:hidden;background:var(--lime);border-radius:32px;padding:80px 56px">
<img src="{B['markDeep']}" alt="" aria-hidden="true" style="position:absolute;right:-90px;top:50%;width:460px;height:460px;transform:translateY(-50%);opacity:0.22">
<div style="position:relative;max-width:640px">
<h2 class="hd" style="margin:0;font-weight:650;font-size:clamp(34px,4.4vw,58px);line-height:1.02;letter-spacing:-0.035em">See your business from above.</h2>
<p style="margin:18px 0 0;max-width:460px;font-size:18px;line-height:1.55">30 minutes. We show you a live map and answer every question.</p>
<a href="Pricing.dc.html#demo" class="btn" style="margin-top:30px;display:inline-flex;align-items:center;gap:10px;min-height:54px;padding:0 26px;border-radius:12px;background:#0B0F0D;color:#FFFFFF;font-size:16px;font-weight:600">Book a demo <span class="arrow" aria-hidden="true">→</span></a>
</div>
</div>
</section>
</main>
{FOOTER}
</div>"""
    script = """class Component extends DCLogic {
  constructor(props) { super(props); this.state = { after: false, step: 0 }; }
  renderVals() {
    var self = this;
    var after = !!this.state.after;
    var segBase = 'min-height:44px;padding:0 16px;border:0;border-radius:9px;font:inherit;font-size:14px;font-weight:600;cursor:pointer;';
    var chipBase = 'font-size:12px;font-weight:600;border-radius:999px;padding:5px 10px;';
    var autos = [
      { task: 'Copying enquiries into the CRM', team: 'Sales', hrs: '22', year: '1,056', status: 'Ready to build', go: true },
      { task: 'Chasing missing documents', team: 'Onboarding', hrs: '15', year: '720', status: 'Ready to build', go: true },
      { task: 'Weekly client status updates', team: 'Delivery', hrs: '9', year: '432', status: 'Sizing', go: false },
      { task: 'Matching payments to invoices', team: 'Finance', hrs: '7', year: '336', status: 'Sizing', go: false }
    ].map(function (a) { a.chip = chipBase + (a.go ? 'background:#85EC68;color:#0B0F0D' : 'background:#F5F6F8;color:#4F5753'); return a; });
    var data = [
      { title: 'Set up', short: 'We install and connect it', body: 'We set Mission Control up for you and connect it to the tools your team already uses. No new software for your people to learn.', outputs: ['Tools connected', 'Teams mapped', 'Staff briefed'] },
      { title: 'See', short: 'A live map of your business', body: 'Your dashboard draws a live map of how work moves between people and teams. It updates as the work happens.', outputs: ['Live map', 'Team views', 'Every hand-off'] },
      { title: 'Understand', short: 'Reports on fast and slow', body: 'Regular reports show what is moving well, what is slowing down, and the moments it happened.', outputs: ['Monthly report', 'Slowdown alerts', 'Trends over time'] },
      { title: 'Automate', short: 'We build what is worth it', body: 'We size every opportunity in hours, then build the ones worth building with you. One-click automation is on the way.', outputs: ['Ranked shortlist', 'Built and tested', 'Results measured'] }
    ];
    var cur = this.state.step;
    var steps = data.map(function (d, i) {
      var on = i === cur;
      return { n: String(i + 1), title: d.title, short: d.short, on: on ? 'true' : 'false',
        pick: function () { self.setState({ step: i }); },
        btn: 'display:flex;gap:14px;align-items:center;width:100%;min-height:84px;padding:16px 18px;border-radius:18px;cursor:pointer;font:inherit;color:#0B0F0D;background:' + (on ? '#FFFFFF' : '#FFFFFF') + ';border:2px solid ' + (on ? '#0B0F0D' : '#E6E8EA'),
        num: 'flex:none;width:38px;height:38px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-family:Bricolage Grotesque,sans-serif;font-weight:700;font-size:17px;background:' + (on ? '#85EC68' : '#F5F6F8') };
    });
    var d = data[cur];
    var tools = [['Email', 'Connected'], ['Calendar', 'Connected'], ['CRM', 'Connected'], ['Practice software', 'Connecting'], ['Shared drives', 'Queued']].map(function (t) {
      return { name: t[0], state: t[1], chip: chipBase + (t[1] === 'Connected' ? 'background:#85EC68;color:#0B0F0D' : t[1] === 'Connecting' ? 'background:var(--popTint);color:var(--popText)' : 'background:#F5F6F8;color:#4F5753') };
    });
    var dots = ['#85EC68', 'var(--pop)', 'var(--hot)', '#0B0F0D'];
    var inds = [
      ['Accounting and bookkeeping', 'Onboarding, month-end and lodgement'], ['Legal', 'Intake, matters and billing'], ['Insurance', 'Claims, assessment and approvals'],
      ['Finance and mortgage broking', 'Applications, documents and settlement'], ['Property management', 'Maintenance, approvals and leasing'],
      ['Recruitment', 'Briefs, interviews and placements'], ['Agencies and consultancies', 'Briefs, reviews, delivery and invoicing']
    ].map(function (x, i) { return { name: x[0], flow: x[1], dot: 'display:block;width:14px;height:14px;border-radius:5px;background:' + dots[i % 4] }; });
    return {
      isBefore: !after, isAfter: after,
      beforeOn: after ? 'false' : 'true', afterOn: after ? 'true' : 'false',
      showBefore: function () { self.setState({ after: false }); },
      showAfter: function () { self.setState({ after: true }); },
      beforeBtn: segBase + (after ? 'background:transparent;color:#4F5753' : 'background:#0B0F0D;color:#FFFFFF'),
      afterBtn: segBase + (after ? 'background:#85EC68;color:#0B0F0D' : 'background:transparent;color:#4F5753'),
      caption: after ? 'One clear route. Every hand-off visible.' : 'How work moves today: nobody can see it.',
      capStyle: 'position:absolute;left:16px;bottom:16px;font-size:14px;font-weight:600;border-radius:10px;padding:8px 12px;box-shadow:0 10px 24px -14px rgba(11,15,13,0.4);' + (after ? 'background:#85EC68;color:#0B0F0D' : 'background:#FFFFFF;color:#0B0F0D'),
      autos: autos, steps: steps,
      cur: { n: cur + 1, title: d.title, body: d.body, outputs: d.outputs },
      s1: cur === 0, s2: cur === 1, s3: cur === 2, s4: cur === 3,
      tools: tools, industries: inds
    };
  }
}"""
    return doc('Mission Control | See how work really moves', body, script, 7600)

if __name__ == '__main__':
    import sys
    out='/home/claude/mc2/project/'
    open(out+'Main.dc.html','w').write(home('cobalt'))
    open(out+'Home-Lilac.dc.html','w').write(home('lilac'))
    open(out+'Home-Sunshine.dc.html','w').write(home('sun'))
    print('ok')

def industries(pk='cobalt'):
    p=PAL[pk]
    body=f"""<div style="{rootvars(p)};font-family:'Figtree',system-ui,sans-serif;color:var(--ink);background:#FFFFFF;-webkit-font-smoothing:antialiased">
{header('ind')}
<main>
<section>
<div style="max-width:1240px;margin:0 auto;padding:72px 28px 64px;display:flex;flex-wrap:wrap;gap:40px 56px;align-items:center">
<div style="flex:1 1 440px;min-width:0">
{tag('Industries')}
<h1 class="hd" style="margin:24px 0 0;font-weight:650;font-size:clamp(38px,4.4vw,60px);line-height:1.03;letter-spacing:-0.035em">If work moves through people and software, <span class="mark">we can map it.</span></h1>
<p style="margin:22px 0 0;max-width:520px;font-size:19px;line-height:1.55;color:var(--muted)">We start with services businesses, where the product is the work itself. That is where Mission Control sees the most, and where automation pays back fastest.</p>
</div>
<div style="flex:1 1 420px;min-width:0;display:grid;gap:12px">
<div style="background:var(--limeTint);border-radius:20px;padding:22px 24px;display:flex;gap:18px;align-items:center"><span class="hd" style="flex:none;font-size:34px;font-weight:700;letter-spacing:-0.03em;min-width:96px">20+</span><span style="font-size:16px;line-height:1.5">People doing the work, across a few teams</span></div>
<div style="background:var(--popTint);border-radius:20px;padding:22px 24px;display:flex;gap:18px;align-items:center"><span class="hd" style="flex:none;font-size:34px;font-weight:700;letter-spacing:-0.03em;min-width:96px;color:var(--popText)">Repeat</span><span style="font-size:16px;line-height:1.5">The same kinds of jobs, again and again: files, claims, cases, orders</span></div>
<div style="background:var(--hotTint);border-radius:20px;padding:22px 24px;display:flex;gap:18px;align-items:center"><span class="hd" style="flex:none;font-size:34px;font-weight:700;letter-spacing:-0.03em;min-width:96px;color:var(--hotText)">Hand-offs</span><span style="font-size:16px;line-height:1.5">Each job passes several people or systems before it is done</span></div>
<p style="margin:4px 0 0;font-size:14px;color:var(--muted)">Tick all three and Mission Control will pay for itself.</p>
</div>
</div>
</section>

<section style="background:var(--soft)">
<div style="max-width:1240px;margin:0 auto;padding:96px 28px">
<div style="max-width:760px">{tag('What we map')}<h2 style="{H2}">Pick an industry. See what Mission Control would show you.</h2></div>
<div role="group" aria-label="Industries" style="margin-top:36px;display:flex;flex-wrap:wrap;gap:8px">
<sc-for list="{{{{tabs}}}}" as="t"><button type="button" class="tab" onClick="{{{{t.pick}}}}" aria-pressed="{{{{t.on}}}}" style="{{{{t.style}}}}">{{{{t.name}}}}</button></sc-for>
</div>
<div class="rise" style="margin-top:24px;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(460px,100%),1fr));gap:16px">
<div style="background:#FFFFFF;border-radius:24px;padding:32px;min-width:0">
<div style="display:flex;justify-content:space-between;gap:12px;align-items:center"><span style="font-size:13px;font-weight:600;color:var(--muted)">TYPICAL ROUTE</span><span style="font-size:12px;color:var(--muted)">Illustrative</span></div>
<div class="hd" style="margin-top:14px;font-weight:650;font-size:34px;letter-spacing:-0.03em;line-height:1.05">{{{{cur.name}}}}</div>
<ol style="list-style:none;margin:26px 0 0;padding:0;display:grid;gap:8px">
<sc-for list="{{{{cur.route}}}}" as="r"><li style="{{{{r.style}}}}"><span style="{{{{r.dot}}}}">{{{{r.k}}}}</span><span style="flex:1">{{{{r.step}}}}</span><span style="{{{{r.tagStyle}}}}">{{{{r.tag}}}}</span></li></sc-for>
</ol>
</div>
<div style="display:grid;gap:16px;min-width:0">
<div style="background:var(--hotTint);border-radius:24px;padding:28px"><div style="font-size:13px;font-weight:700;color:var(--hotText)">WHERE IT USUALLY SLOWS</div><p class="hd" style="margin:12px 0 0;font-size:22px;font-weight:600;line-height:1.3;letter-spacing:-0.01em">{{{{cur.slow}}}}</p></div>
<div style="background:var(--pop);color:var(--popInk);border-radius:24px;padding:28px"><div style="font-size:13px;font-weight:700;opacity:0.85">WHAT WE OFTEN AUTOMATE</div><ul style="margin:14px 0 0;padding:0;list-style:none;display:grid;gap:10px;font-size:17px;font-weight:500"><sc-for list="{{{{cur.auto}}}}" as="a"><li style="display:flex;gap:10px;align-items:center"><span aria-hidden="true" style="width:8px;height:8px;border-radius:50%;background:var(--lime)"></span>{{{{a}}}}</li></sc-for></ul></div>
<div style="background:#FFFFFF;border-radius:24px;padding:28px"><div style="font-size:13px;font-weight:700;color:var(--muted)">WHO USES IT</div><p style="margin:12px 0 0;font-size:17px;line-height:1.55">{{{{cur.who}}}}</p></div>
</div>
</div>
</div>
</section>

<section id="soon">
<div style="max-width:1240px;margin:0 auto;padding:96px 28px">
<div style="display:flex;flex-wrap:wrap;gap:40px 56px;align-items:center">
<div style="flex:1 1 360px;min-width:0">{tag('Coming soon', dot='var(--hot)')}<h2 style="{H2}">From the inbox to the factory floor.</h2><p style="margin:18px 0 0;max-width:460px;font-size:18px;line-height:1.6;color:var(--muted)">The same map, for work that moves through the physical world. We are building it now with early partners.</p></div>
<div style="flex:1.2 1 480px;min-width:0;border-radius:28px;overflow:hidden;background:#F2F4F1;aspect-ratio:16/10"><img src="{B['floor']}" alt="An isometric factory floor with work moving along dashed routes between machines." style="width:100%;height:100%;object-fit:cover;display:block"></div>
</div>
<div style="margin-top:40px;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(250px,100%),1fr));gap:14px">
<sc-for list="{{{{soon}}}}" as="s"><div style="border:1px solid var(--line);border-radius:20px;padding:24px"><span style="font-size:12px;font-weight:700;color:var(--hotText);background:var(--hotTint);border-radius:999px;padding:5px 10px">SOON</span><h3 class="hd" style="margin:16px 0 0;font-size:21px;font-weight:600">{{{{s.name}}}}</h3><p style="margin:8px 0 0;font-size:15px;line-height:1.55;color:var(--muted)">{{{{s.body}}}}</p></div></sc-for>
</div>
<a href="Pricing.dc.html#demo" class="btn" style="margin-top:36px;display:inline-flex;align-items:center;gap:10px;min-height:52px;padding:0 24px;border-radius:12px;background:var(--ink);color:#FFFFFF;font-size:16px;font-weight:600">Join early access <span class="arrow" aria-hidden="true">→</span></a>
</div>
</section>

<section style="padding:0 28px 96px">
<div style="max-width:1240px;margin:0 auto;background:var(--lime);border-radius:32px;padding:56px;display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:24px">
<h2 class="hd" style="margin:0;font-weight:650;font-size:clamp(30px,3.6vw,46px);letter-spacing:-0.03em">Not on the list? Ask us anyway.</h2>
<a href="Pricing.dc.html#demo" class="btn" style="display:inline-flex;align-items:center;gap:10px;min-height:54px;padding:0 26px;border-radius:12px;background:#0B0F0D;color:#FFFFFF;font-size:16px;font-weight:600">Book a demo <span class="arrow" aria-hidden="true">→</span></a>
</div>
</section>
</main>
{FOOTER}
</div>"""
    script="""class Component extends DCLogic {
  constructor(props) { super(props); this.state = { tab: 0 }; }
  renderVals() {
    var self = this;
    var list = [
      { name: 'Accounting and bookkeeping', route: ['New client onboarded', 'Documents requested', 'Waiting on client', 'Work prepared', 'Partner review', 'Lodged and invoiced'], slowAt: 2, slow: 'Waiting on clients for documents, then work queuing for partner review.', auto: ['Document requests and reminders', 'Reconciliation prep', 'Job status updates to clients'], who: 'Practice managers and partners who want to grow without adding headcount.' },
      { name: 'Legal', route: ['Enquiry received', 'Conflict check', 'Engagement signed', 'Matter opened', 'Work in progress', 'Billed'], slowAt: 1, slow: 'Conflict checks and engagement letters waiting on sign-off.', auto: ['Intake and conflict searches', 'Engagement letters', 'Time entry reminders'], who: 'Firm owners and operations leads who want matters to open faster.' },
      { name: 'Insurance', route: ['Claim lodged', 'Triage', 'Assessment', 'Approval', 'Payment', 'Closed'], slowAt: 2, slow: 'Claims queuing for assessment, then bouncing back for missing information.', auto: ['Claim triage and routing', 'Missing information requests', 'Customer status updates'], who: 'Brokers, underwriting agencies and claims teams handling high volumes.' },
      { name: 'Finance and mortgage broking', route: ['Enquiry', 'Fact find', 'Document collection', 'Lender submission', 'Approval', 'Settlement'], slowAt: 2, slow: 'Collecting documents from clients before an application can be lodged.', auto: ['Document checklists and chasers', 'CRM and lender data entry', 'Settlement countdown updates'], who: 'Broker businesses and aggregator teams processing many applications.' },
      { name: 'Property management', route: ['Request logged', 'Trade quoted', 'Owner approval', 'Job booked', 'Job completed', 'Invoice paid'], slowAt: 2, slow: 'Maintenance jobs waiting for owners to approve quotes.', auto: ['Quote routing and owner approvals', 'Tenant updates', 'Invoice matching'], who: 'Agencies managing large rent rolls with lean property teams.' },
      { name: 'Recruitment', route: ['Brief taken', 'Sourcing', 'Shortlist sent', 'Interviews', 'Offer', 'Placed'], slowAt: 3, slow: 'Interview scheduling and waiting on client feedback.', auto: ['Interview scheduling', 'Candidate updates', 'CRM notes and admin'], who: 'Agencies and in-house talent teams running many roles at once.' },
      { name: 'Agencies and consultancies', route: ['Brief received', 'Scoped', 'In production', 'Client review', 'Delivered', 'Invoiced'], slowAt: 3, slow: 'Client review rounds, and work finished but not yet invoiced.', auto: ['Status reports', 'Review reminders', 'Invoicing from delivery'], who: 'Studios and consultancies that sell time and want more of it back.' },
      { name: 'Healthcare admin', route: ['Referral received', 'Triage', 'Booked', 'Appointment', 'Notes and billing', 'Follow-up'], slowAt: 0, slow: 'Referrals sitting in a shared inbox before anyone triages them.', auto: ['Referral intake', 'Booking reminders', 'Billing and claims prep'], who: 'Clinic groups and allied health practices with busy front desks. We map the admin, never patient records.' }
    ];
    var cur = this.state.tab;
    var tabs = list.map(function (it, i) {
      var on = i === cur;
      return { name: it.name, on: on ? 'true' : 'false', pick: function () { self.setState({ tab: i }); },
        style: 'min-height:44px;padding:0 16px;border-radius:12px;font:inherit;font-size:15px;font-weight:600;cursor:pointer;border:2px solid ' + (on ? '#0B0F0D' : 'transparent') + ';background:' + (on ? '#85EC68' : '#FFFFFF') + ';color:#0B0F0D' };
    });
    var c = list[cur];
    var route = c.route.map(function (s, i) {
      var slow = i === c.slowAt, last = i === c.route.length - 1;
      return { k: String(i + 1), step: s, tag: slow ? 'Slow' : (last ? 'Done' : ''),
        tagStyle: 'font-size:12px;font-weight:700;' + (slow ? 'color:var(--hotText)' : 'color:#157A36'),
        style: 'display:flex;align-items:center;gap:14px;padding:12px 14px;border-radius:14px;font-size:16px;font-weight:500;background:' + (slow ? 'var(--hotTint)' : '#F5F6F8'),
        dot: 'flex:none;width:28px;height:28px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;background:' + (slow ? 'var(--hot)' : '#85EC68') + ';color:' + (slow ? '#FFFFFF' : '#0B0F0D') };
    });
    return {
      tabs: tabs,
      cur: { name: c.name, route: route, slow: c.slow, auto: c.auto, who: c.who },
      soon: [
        { name: 'Manufacturing', body: 'Follow jobs from order to production line to quality check.' },
        { name: 'Warehousing', body: 'See how stock moves from receiving to picking to dispatch.' },
        { name: 'Logistics', body: 'Map every leg between depot, driver and doorstep.' },
        { name: 'Robotics', body: 'Track the hand-offs between people, machines and robots.' }
      ]
    };
  }
}"""
    return doc('Mission Control | Industries', body, script, 4400)

def pricing(pk='cobalt'):
    p=PAL[pk]
    li = lambda t: f'<li style="display:flex;gap:10px;align-items:center">{CHK}{t}</li>'
    inp = "height:50px;border:1.5px solid #D9DDE0;border-radius:12px;padding:0 14px;font:inherit;font-size:16px;background:#FFFFFF;color:#0B0F0D"
    body=f"""<div style="{rootvars(p)};font-family:'Figtree',system-ui,sans-serif;color:var(--ink);background:#FFFFFF;-webkit-font-smoothing:antialiased">
{header('price')}
<main>
<section>
<div style="max-width:1240px;margin:0 auto;padding:72px 28px 48px;text-align:center">
{tag('Pricing')}
<h1 class="hd" style="margin:24px auto 0;max-width:820px;font-weight:650;font-size:clamp(38px,4.4vw,60px);line-height:1.03;letter-spacing:-0.035em">Three parts. <span class="mark">No surprises.</span></h1>
<p style="margin:20px auto 0;max-width:580px;font-size:19px;line-height:1.55;color:var(--muted)">A one-off setup, a monthly platform fee, and automations priced one at a time. You see the payoff before you pay for an automation.</p>
</div>
</section>
<section>
<div style="max-width:1240px;margin:0 auto;padding:24px 28px 96px;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(330px,100%),1fr));gap:16px;align-items:stretch">
<article style="border:1px solid var(--line);border-radius:26px;padding:34px">
<span style="font-size:13px;font-weight:700;color:var(--muted)">01 · ONCE</span>
<h2 class="hd" style="margin:16px 0 0;font-weight:650;font-size:38px;letter-spacing:-0.03em">Setup</h2>
<p style="margin:8px 0 0;font-size:16px;color:var(--muted)">We do the work to get you live.</p>
<div style="margin-top:22px;padding:14px 16px;border-radius:12px;background:var(--soft);font-size:15px;font-weight:600">One-off fee, quoted upfront</div>
<ul style="margin:22px 0 0;padding:0;list-style:none;display:grid;gap:12px;font-size:16px">{li('Install and connect your tools')}{li('Map your teams and their work')}{li('Brief your staff and leaders')}{li('Your first map, walked through with you')}</ul>
</article>
<article style="border-radius:26px;padding:34px;background:var(--pop);color:var(--popInk);box-shadow:0 30px 60px -36px rgba(11,15,13,0.55)">
<div style="display:flex;justify-content:space-between;align-items:center"><span style="font-size:13px;font-weight:700;opacity:0.85">02 · MONTHLY</span><span style="font-size:12px;font-weight:700;background:var(--lime);color:#0B0F0D;border-radius:999px;padding:5px 10px">CORE</span></div>
<h2 class="hd" style="margin:16px 0 0;font-weight:650;font-size:38px;letter-spacing:-0.03em">Platform</h2>
<p style="margin:8px 0 0;font-size:16px;opacity:0.85">Your business, live, every day.</p>
<div style="margin-top:22px;padding:14px 16px;border-radius:12px;background:rgba(255,255,255,0.16);font-size:15px;font-weight:600">Monthly fee, based on team size</div>
<ul style="margin:22px 0 0;padding:0;list-style:none;display:grid;gap:12px;font-size:16px">{li('Live map and dashboard')}{li('Reports on what is fast and slow')}{li('Automation opportunities, sized')}{li('A named contact on our team')}</ul>
</article>
<article style="border-radius:26px;padding:34px;background:var(--limeTint)">
<span style="font-size:13px;font-weight:700;color:var(--greenText)">03 · AS YOU GO</span>
<h2 class="hd" style="margin:16px 0 0;font-weight:650;font-size:38px;letter-spacing:-0.03em">Automations</h2>
<p style="margin:8px 0 0;font-size:16px;color:var(--muted)">Built only when the numbers say yes.</p>
<div style="margin-top:22px;padding:14px 16px;border-radius:12px;background:#FFFFFF;font-size:15px;font-weight:600">Priced per automation, billed separately</div>
<ul style="margin:22px 0 0;padding:0;list-style:none;display:grid;gap:12px;font-size:16px">{li('Hours saved shown before you commit')}{li('Built and tested by our team')}{li('Results tracked on your map')}{li('One-click deploy, coming soon')}</ul>
</article>
</div>
</section>

<section style="background:var(--soft)">
<div style="max-width:1240px;margin:0 auto;padding:96px 28px">
<div style="max-width:720px">{tag('After you say yes')}<h2 style="{H2}">From first call to first automation.</h2></div>
<ol style="margin:44px 0 0;padding:0;list-style:none;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(240px,100%),1fr));gap:14px">
<li style="background:#FFFFFF;border-radius:20px;padding:26px"><span class="hd" style="width:38px;height:38px;border-radius:50%;background:var(--lime);display:inline-flex;align-items:center;justify-content:center;font-weight:700">1</span><div class="hd" style="margin-top:16px;font-size:21px;font-weight:600">Demo and scope</div><p style="margin:6px 0 0;font-size:15px;line-height:1.55;color:var(--muted)">We show you a live map and agree which teams to start with.</p></li>
<li style="background:#FFFFFF;border-radius:20px;padding:26px"><span class="hd" style="width:38px;height:38px;border-radius:50%;background:var(--lime);display:inline-flex;align-items:center;justify-content:center;font-weight:700">2</span><div class="hd" style="margin-top:16px;font-size:21px;font-weight:600">We get you live</div><p style="margin:6px 0 0;font-size:15px;line-height:1.55;color:var(--muted)">Tools connected, staff briefed, data starts flowing.</p></li>
<li style="background:#FFFFFF;border-radius:20px;padding:26px"><span class="hd" style="width:38px;height:38px;border-radius:50%;background:var(--lime);display:inline-flex;align-items:center;justify-content:center;font-weight:700">3</span><div class="hd" style="margin-top:16px;font-size:21px;font-weight:600">Your map fills in</div><p style="margin:6px 0 0;font-size:15px;line-height:1.55;color:var(--muted)">Patterns appear. We walk you through your first report.</p></li>
<li style="background:var(--pop);color:var(--popInk);border-radius:20px;padding:26px"><span class="hd" style="width:38px;height:38px;border-radius:50%;background:var(--lime);color:#0B0F0D;display:inline-flex;align-items:center;justify-content:center;font-weight:700">4</span><div class="hd" style="margin-top:16px;font-size:21px;font-weight:600">Automate the big wins</div><p style="margin:6px 0 0;font-size:15px;line-height:1.55;opacity:0.85">You pick from a ranked shortlist. We build it.</p></li>
</ol>
</div>
</section>

<section>
<div style="max-width:1240px;margin:0 auto;padding:96px 28px;display:flex;flex-wrap:wrap;gap:40px 72px">
<div style="flex:1 1 300px">{tag('Plain answers')}<h2 style="{H2}">Questions people ask first.</h2></div>
<div style="flex:2 1 560px;min-width:0;display:grid;gap:10px">
<sc-for list="{{{{faqs}}}}" as="f"><div style="{{{{f.box}}}}"><button type="button" class="seg" onClick="{{{{f.toggle}}}}" aria-expanded="{{{{f.open}}}}" style="width:100%;display:flex;justify-content:space-between;align-items:center;gap:20px;text-align:left;border:0;background:transparent;padding:20px 22px;min-height:44px;cursor:pointer;font:inherit;font-size:18px;font-weight:600;color:#0B0F0D">{{{{f.q}}}}<span aria-hidden="true" style="{{{{f.signStyle}}}}">{{{{f.sign}}}}</span></button><sc-if value="{{{{f.isOpen}}}}" hint-placeholder-val="{{{{false}}}}"><p style="margin:0;padding:0 22px 22px;max-width:640px;font-size:16px;line-height:1.6;color:var(--muted)">{{{{f.a}}}}</p></sc-if></div></sc-for>
</div>
</div>
</section>

<section id="demo" style="padding:0 28px 96px">
<div style="max-width:1240px;margin:0 auto;background:var(--popTint);border-radius:32px;padding:56px;display:flex;flex-wrap:wrap;gap:40px 64px;align-items:flex-start">
<div style="flex:1 1 340px;min-width:0">
{tag('Book a demo', dot='var(--pop)')}
<h2 style="{H2}">See your business from above.</h2>
<p style="margin:18px 0 0;max-width:420px;font-size:18px;line-height:1.6;color:var(--muted)">30 minutes. We show you a live map, talk through your team, and tell you honestly whether it is a fit.</p>
<ul style="margin:26px 0 0;padding:0;list-style:none;display:grid;gap:12px;font-size:16px">{li('We reply within one business day')}{li('No prep needed on your side')}<li style="display:flex;gap:10px;align-items:center">{CHK}<span>Or email <a href="mailto:hello@missioncntrl.io" style="text-decoration:underline">hello@missioncntrl.io</a></span></li></ul>
</div>
<form onSubmit="{{{{submit}}}}" style="flex:1.2 1 460px;min-width:0;background:#FFFFFF;border-radius:24px;padding:32px;display:grid;gap:18px;box-shadow:0 30px 60px -40px rgba(11,15,13,0.45)">
<sc-if value="{{{{sent}}}}" hint-placeholder-val="{{{{false}}}}"><div role="status" style="background:var(--limeTint);border-radius:12px;padding:14px 16px;font-size:15px;font-weight:500">Thanks. We will be in touch within one business day.</div></sc-if>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(200px,100%),1fr));gap:18px">
<label style="display:grid;gap:8px;font-size:14px;font-weight:600">Your name<input class="in" type="text" name="name" autocomplete="name" style="{inp}"></label>
<label style="display:grid;gap:8px;font-size:14px;font-weight:600">Work email<input class="in" type="email" name="email" autocomplete="email" style="{inp}"></label>
</div>
<label style="display:grid;gap:8px;font-size:14px;font-weight:600">Company<input class="in" type="text" name="company" autocomplete="organization" style="{inp}"></label>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(200px,100%),1fr));gap:18px">
<label style="display:grid;gap:8px;font-size:14px;font-weight:600">Team size<select class="in" name="size" style="{inp}"><option>Under 20</option><option>20 to 50</option><option>50 to 200</option><option>200+</option></select></label>
<label style="display:grid;gap:8px;font-size:14px;font-weight:600">Industry<select class="in" name="industry" style="{inp}"><option>Accounting and bookkeeping</option><option>Legal</option><option>Insurance</option><option>Finance and mortgage broking</option><option>Property management</option><option>Recruitment</option><option>Agency or consultancy</option><option>Healthcare admin</option><option>Manufacturing or logistics (early access)</option><option>Something else</option></select></label>
</div>
<label style="display:grid;gap:8px;font-size:14px;font-weight:600">What would you most like to see? <span style="font-weight:400;color:var(--muted)">Optional</span><textarea class="in" name="message" rows="3" style="border:1.5px solid #D9DDE0;border-radius:12px;padding:12px 14px;font:inherit;font-size:16px;resize:vertical"></textarea></label>
<button type="submit" class="btn" style="justify-self:start;display:inline-flex;align-items:center;gap:10px;min-height:54px;padding:0 26px;border:0;border-radius:12px;background:var(--pop);color:var(--popInk);font:inherit;font-size:16px;font-weight:600;cursor:pointer">Book my demo <span class="arrow" aria-hidden="true">→</span></button>
</form>
</div>
</section>
</main>
{FOOTER}
</div>"""
    script="""class Component extends DCLogic {
  constructor(props) { super(props); this.state = { open: 0, sent: false }; }
  renderVals() {
    var self = this;
    var items = [
      { q: 'What does Mission Control actually do?', a: 'It draws a live map of how work moves between the people and teams in your business. From that map you can see what is moving well, what is slowing down, and which repetitive tasks are worth automating.' },
      { q: 'Do my staff need to learn new software?', a: 'No. Mission Control works alongside the tools your team already uses. Leaders get a dashboard; everyone else keeps working as normal.' },
      { q: 'Is this monitoring my staff?', a: 'It maps how work moves, not what people write. We help you roll it out openly with clear notice to your team, and you choose which teams and tools are included.' },
      { q: 'How quickly will I see something useful?', a: 'Your map starts filling in once setup is done. Most of the value shows up in the first few weeks, as patterns become clear.' },
      { q: 'How is pricing worked out?', a: 'A one-off setup fee, a monthly platform fee based on team size, and automations priced one by one. We quote everything upfront.' },
      { q: 'Who builds the automations?', a: 'Our team does, today. We size each one first, so you only pay for automations that clearly earn their keep. One-click automation is on the way.' },
      { q: 'Do you work with manufacturing or warehouses?', a: 'Not yet. Mapping physical work is on our roadmap and we are talking to early partners now. Book a demo and choose early access.' }
    ];
    var faqs = items.map(function (f, i) {
      var open = self.state.open === i;
      return { q: f.q, a: f.a, isOpen: open, open: open ? 'true' : 'false', sign: open ? '−' : '+',
        box: 'border-radius:18px;background:' + (open ? '#EEFCE8' : '#F5F6F8'),
        signStyle: 'flex:none;width:32px;height:32px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:20px;background:' + (open ? '#85EC68' : '#FFFFFF'),
        toggle: function () { self.setState({ open: open ? -1 : i }); } };
    });
    return { faqs: faqs, sent: !!this.state.sent, submit: function (e) { if (e && e.preventDefault) e.preventDefault(); self.setState({ sent: true }); } };
  }
}"""
    return doc('Mission Control | Pricing and demo', body, script, 4600)

if __name__ == '__main__':
    out='/home/claude/mc2/project/'
    open(out+'Industries.dc.html','w').write(industries())
    open(out+'Pricing.dc.html','w').write(pricing())
    print('ok2')
