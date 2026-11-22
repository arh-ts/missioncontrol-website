from v3 import *
def platform():
    overview = """<div style="display:flex;min-height:460px">
<aside class="side" aria-hidden="true" style="flex:none;width:196px;border-right:1px solid #EEEFF1;padding:16px 10px;font-size:13px;color:#5B616B;display:flex;flex-direction:column;gap:2px">
<div style="display:flex;align-items:center;gap:8px;padding:6px 8px 14px"><img src="%s" alt="" style="width:18px;height:18px"><span style="font-weight:600;color:#0A0B0D">Northwind Group</span></div>
<div style="padding:7px 8px;border-radius:6px;background:#F2F3F5;color:#0A0B0D;font-weight:500">Overview</div><div style="padding:7px 8px">Live map</div><div style="padding:7px 8px">Workflows</div><div style="padding:7px 8px">Bottlenecks</div><div style="padding:7px 8px">Teams</div><div style="padding:7px 8px">Automations</div><div style="padding:7px 8px">Reports</div>
</aside>
<div style="flex:1;min-width:0;padding:20px">
<div style="display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap"><span class="d" style="font-size:18px;font-weight:500">Overview</span><span style="font-size:12px;color:#8A9099;border:1px solid #EEEFF1;border-radius:6px;padding:5px 9px">Last 30 days</span></div>
<div style="margin-top:16px;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(150px,100%%),1fr));gap:10px">
<div style="border:1px solid #EEEFF1;border-radius:10px;padding:14px"><div style="font-size:12px;color:#8A9099">Work in flight</div><div class="d" style="margin-top:6px;font-size:24px;font-weight:500">1,284</div><div style="font-size:12px;color:#157A36">+6%% vs last month</div></div>
<div style="border:1px solid #EEEFF1;border-radius:10px;padding:14px"><div style="font-size:12px;color:#8A9099">Median cycle time</div><div class="d" style="margin-top:6px;font-size:24px;font-weight:500">3.1 days</div><div style="font-size:12px;color:#157A36">−0.4d</div></div>
<div style="border:1px solid #EEEFF1;border-radius:10px;padding:14px"><div style="font-size:12px;color:#8A9099">Active bottlenecks</div><div class="d" style="margin-top:6px;font-size:24px;font-weight:500">3</div><div style="font-size:12px;color:#C2510C">1 high impact</div></div>
<div style="border:1px solid #EEEFF1;border-radius:10px;padding:14px;background:#0A0B0D;color:#FFFFFF"><div style="font-size:12px;color:#A7ADB6">Automatable time</div><div class="d" style="margin-top:6px;font-size:24px;font-weight:500">53 h/wk</div><div style="font-size:12px;color:#85EC68">$152k a year</div></div>
</div>
<div style="margin-top:16px;border:1px solid #EEEFF1;border-radius:10px;overflow:hidden">
<div style="overflow-x:auto"><table style="width:100%%;min-width:560px;border-collapse:collapse;font-size:13px">
<thead><tr style="text-align:left;background:#FAFAFB;color:#8A9099;font-size:12px"><th style="padding:10px 14px;font-weight:500">Workflow</th><th style="padding:10px 14px;font-weight:500">In flight</th><th style="padding:10px 14px;font-weight:500">Median</th><th style="padding:10px 14px;font-weight:500">Trend</th><th style="padding:10px 14px;font-weight:500">Health</th></tr></thead>
<tbody>
<tr style="border-top:1px solid #EEEFF1"><td style="padding:11px 14px;font-weight:500">Client onboarding</td><td style="padding:11px 14px">214</td><td style="padding:11px 14px">3.1d</td><td style="padding:11px 14px"><svg width="80" height="20" aria-hidden="true"><path d="M0 14 L13 12 L26 15 L39 9 L52 11 L65 6 L80 7" fill="none" stroke="#0A0B0D" stroke-width="1.5"></path></svg></td><td style="padding:11px 14px"><span style="display:inline-flex;align-items:center;gap:6px"><span style="width:7px;height:7px;border-radius:50%%;background:#E8590C"></span>Bottleneck</span></td></tr>
<tr style="border-top:1px solid #EEEFF1"><td style="padding:11px 14px;font-weight:500">Monthly close</td><td style="padding:11px 14px">96</td><td style="padding:11px 14px">4.6d</td><td style="padding:11px 14px"><svg width="80" height="20" aria-hidden="true"><path d="M0 8 L13 9 L26 7 L39 10 L52 8 L65 9 L80 8" fill="none" stroke="#0A0B0D" stroke-width="1.5"></path></svg></td><td style="padding:11px 14px"><span style="display:inline-flex;align-items:center;gap:6px"><span style="width:7px;height:7px;border-radius:50%%;background:#85EC68"></span>Healthy</span></td></tr>
<tr style="border-top:1px solid #EEEFF1"><td style="padding:11px 14px;font-weight:500">Change requests</td><td style="padding:11px 14px">341</td><td style="padding:11px 14px">1.2d</td><td style="padding:11px 14px"><svg width="80" height="20" aria-hidden="true"><path d="M0 6 L13 7 L26 9 L39 8 L52 11 L65 12 L80 14" fill="none" stroke="#0A0B0D" stroke-width="1.5"></path></svg></td><td style="padding:11px 14px"><span style="display:inline-flex;align-items:center;gap:6px"><span style="width:7px;height:7px;border-radius:50%%;background:#C4C8CE"></span>Watching</span></td></tr>
<tr style="border-top:1px solid #EEEFF1"><td style="padding:11px 14px;font-weight:500">Billing and collections</td><td style="padding:11px 14px">633</td><td style="padding:11px 14px">6.8d</td><td style="padding:11px 14px"><svg width="80" height="20" aria-hidden="true"><path d="M0 15 L13 13 L26 12 L39 12 L52 9 L65 8 L80 5" fill="none" stroke="#0A0B0D" stroke-width="1.5"></path></svg></td><td style="padding:11px 14px"><span style="display:inline-flex;align-items:center;gap:6px"><span style="width:7px;height:7px;border-radius:50%%;background:#85EC68"></span>Healthy</span></td></tr>
</tbody></table></div></div>
</div></div>""" % MARKDEEP

    def module(idx, anchor, label, title, body, bullets, visual, reverse=False):
        b=''.join(f'<li style="display:flex;gap:12px;padding:12px 0;border-bottom:1px solid #EEEFF1;font-size:15px"><span aria-hidden="true" style="flex:none;width:6px;height:6px;margin-top:8px;border-radius:50%;background:#0A0B0D"></span>{x}</li>' for x in bullets)
        text=f'<div style="flex:1 1 380px;min-width:0"><p style="margin:0;font-size:13px;color:#8A9099">{idx}</p>{eyebrow(label)}{h2(title)}<p style="{LEAD}">{body}</p><ul style="margin:24px 0 0;padding:0;list-style:none;border-top:1px solid #EEEFF1">{b}</ul></div>'
        vis=f'<div aria-hidden="true" style="flex:1.2 1 480px;min-width:0;background:#FAFAFB;border:1px solid #EEEFF1;border-radius:16px;padding:28px">{visual}</div>'
        inner = vis+text if reverse else text+vis
        return f'<section id="{anchor}"><div style="max-width:1200px;margin:0 auto;padding:120px 24px 0;display:flex;flex-wrap:{"wrap-reverse" if reverse else "wrap"};gap:48px 72px;align-items:center">{inner}</div></section>'

    mapvis = """<div style="%s;padding:16px"><div style="display:flex;justify-content:space-between;font-size:12px;color:#8A9099"><span style="display:inline-flex;align-items:center;gap:6px"><span class="live" style="width:7px;height:7px;border-radius:50%%;background:#85EC68"></span>Live · whole organisation</span><span>6 teams · 41 tools</span></div>
<svg viewBox="0 0 520 300" width="100%%" style="margin-top:8px;display:block"><g fill="none" stroke-linecap="round" stroke="#0A0B0D"><path d="M70 60 C150 40 200 50 250 80" stroke-width="3"></path><path d="M250 80 C320 110 380 70 450 70" stroke-width="2.5"></path><path d="M250 80 C260 150 300 190 360 220" stroke-width="2"></path><path d="M360 220 C410 240 440 180 450 70" stroke-width="1.5"></path><path d="M70 60 C60 150 100 220 160 240" stroke-width="1.5" stroke="#B9BDC3"></path><path d="M160 240 C230 250 300 240 360 220" stroke-width="2.5" stroke="#E8590C"></path></g>
<g font-family="Inter, sans-serif" font-size="12" font-weight="500" text-anchor="middle"><circle cx="70" cy="60" r="24" fill="#FFFFFF" stroke="#D4D7DB"></circle><text x="70" y="64" fill="#0A0B0D">Sales</text><circle cx="250" cy="80" r="30" fill="#0A0B0D"></circle><text x="250" y="84" fill="#FFFFFF">Ops</text><circle cx="450" cy="70" r="26" fill="#FFFFFF" stroke="#D4D7DB"></circle><text x="450" y="74" fill="#0A0B0D">Delivery</text><circle cx="160" cy="240" r="24" fill="#FFFFFF" stroke="#D4D7DB"></circle><text x="160" y="244" fill="#0A0B0D">Legal</text><circle cx="360" cy="220" r="28" fill="#FFF3EB" stroke="#E8590C"></circle><text x="360" y="224" fill="#B4450A">Finance</text></g></svg>
<div style="display:flex;gap:16px;font-size:12px;color:#5B616B"><span style="display:inline-flex;align-items:center;gap:6px"><span style="width:14px;height:3px;background:#0A0B0D"></span>Line weight = volume</span><span style="display:inline-flex;align-items:center;gap:6px"><span style="width:14px;height:3px;background:#E8590C"></span>Slowing</span></div></div>""" % CARD
    variants = f"""<div style="{CARD};padding:18px"><div style="font-size:12px;color:#8A9099">Client onboarding · how cases actually travel</div>
<div style="margin-top:14px;display:grid;gap:10px;font-size:13px">
<div><div style="display:flex;justify-content:space-between"><span style="font-weight:500">Route A · the usual path</span><span>71% · 2.6d</span></div><div style="margin-top:6px;height:8px;border-radius:4px;background:#EEEFF1"><div style="width:71%;height:8px;border-radius:4px;background:#0A0B0D"></div></div></div>
<div><div style="display:flex;justify-content:space-between"><span style="font-weight:500">Route B · via compliance review</span><span style="color:#C2510C">22% · 4.1d</span></div><div style="margin-top:6px;height:8px;border-radius:4px;background:#EEEFF1"><div style="width:22%;height:8px;border-radius:4px;background:#E8590C"></div></div></div>
<div><div style="display:flex;justify-content:space-between"><span style="font-weight:500">Route C · sent back for rework</span><span style="color:#C2510C">7% · 6.8d</span></div><div style="margin-top:6px;height:8px;border-radius:4px;background:#EEEFF1"><div style="width:7%;height:8px;border-radius:4px;background:#E8590C"></div></div></div>
</div>
<div style="margin-top:16px;padding-top:14px;border-top:1px solid #EEEFF1;font-size:13px;color:#5B616B">Documented process: Route A only. <span style="color:#0A0B0D;font-weight:500">29% of cases leave it.</span></div></div>"""
    alerts = f"""<div style="{CARD};padding:6px 18px"><div style="display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid #EEEFF1;font-size:12px;color:#8A9099"><span>Alerts</span><span>Today</span></div>
<div style="display:flex;gap:12px;padding:14px 0;border-bottom:1px solid #EEEFF1;font-size:13px"><span style="flex:none;width:8px;height:8px;margin-top:5px;border-radius:50%;background:#E8590C"></span><div><div style="font-weight:500">Compliance review queue is 2.3x normal</div><div style="color:#8A9099;margin-top:2px">18 cases waiting · approver out until Monday</div></div></div>
<div style="display:flex;gap:12px;padding:14px 0;border-bottom:1px solid #EEEFF1;font-size:13px"><span style="flex:none;width:8px;height:8px;margin-top:5px;border-radius:50%;background:#C4C8CE"></span><div><div style="font-weight:500">Change requests trending slower</div><div style="color:#8A9099;margin-top:2px">Median up 0.3d over two weeks</div></div></div>
<div style="display:flex;gap:12px;padding:14px 0;font-size:13px"><span style="flex:none;width:8px;height:8px;margin-top:5px;border-radius:50%;background:#85EC68"></span><div><div style="font-weight:500">Monthly close finished a day early</div><div style="color:#8A9099;margin-top:2px">First time this quarter</div></div></div></div>"""
    teams = f"""<div style="{CARD};padding:18px"><div style="display:flex;justify-content:space-between;font-size:12px;color:#8A9099"><span>Team load · this week</span><span>Teams, not individuals</span></div>
<div style="margin-top:14px;display:grid;gap:12px;font-size:13px">
<div style="display:grid;grid-template-columns:110px 1fr 48px;gap:10px;align-items:center"><span>Onboarding</span><div style="height:8px;border-radius:4px;background:#EEEFF1"><div style="width:92%;height:8px;border-radius:4px;background:#E8590C"></div></div><span style="text-align:right">92%</span></div>
<div style="display:grid;grid-template-columns:110px 1fr 48px;gap:10px;align-items:center"><span>Delivery</span><div style="height:8px;border-radius:4px;background:#EEEFF1"><div style="width:74%;height:8px;border-radius:4px;background:#0A0B0D"></div></div><span style="text-align:right">74%</span></div>
<div style="display:grid;grid-template-columns:110px 1fr 48px;gap:10px;align-items:center"><span>Finance</span><div style="height:8px;border-radius:4px;background:#EEEFF1"><div style="width:61%;height:8px;border-radius:4px;background:#0A0B0D"></div></div><span style="text-align:right">61%</span></div>
<div style="display:grid;grid-template-columns:110px 1fr 48px;gap:10px;align-items:center"><span>Sales</span><div style="height:8px;border-radius:4px;background:#EEEFF1"><div style="width:48%;height:8px;border-radius:4px;background:#0A0B0D"></div></div><span style="text-align:right">48%</span></div>
</div>
<div style="margin-top:16px;padding-top:14px;border-top:1px solid #EEEFF1;font-size:13px;color:#5B616B">Onboarding is carrying work that belongs to two other workflows.</div></div>"""
    report = f"""<div style="{CARD};padding:22px"><div style="display:flex;justify-content:space-between;align-items:center"><img src="{MARKDEEP}" alt="" style="width:20px;height:20px"><span style="font-size:12px;color:#8A9099">October review</span></div>
<div class="d" style="margin-top:14px;font-size:20px;font-weight:500;letter-spacing:-0.01em">Operations review: Northwind Group</div>
<div style="margin-top:14px;display:grid;gap:8px;font-size:13px;color:#5B616B">
<div style="display:flex;gap:10px"><span style="color:#0A0B0D;font-weight:600;width:18px">1</span>Cycle time down 0.4 days, driven by faster intake.</div>
<div style="display:flex;gap:10px"><span style="color:#0A0B0D;font-weight:600;width:18px">2</span>Compliance review remains the biggest delay.</div>
<div style="display:flex;gap:10px"><span style="color:#0A0B0D;font-weight:600;width:18px">3</span>Two automations ready for approval, 37 h/wk combined.</div>
</div>
<div style="margin-top:16px;display:flex;gap:8px"><span style="font-size:12px;border:1px solid #EEEFF1;border-radius:6px;padding:5px 9px">12 pages</span><span style="font-size:12px;border:1px solid #EEEFF1;border-radius:6px;padding:5px 9px">Reviewed with your lead</span></div></div>"""
    def kcard(title, items, dot):
        it=''.join(f'<div style="{CARD};padding:10px;font-size:12px;line-height:1.4">{a}<div style="margin-top:6px;color:#8A9099">{b}</div></div>' for a,b in items)
        return f'<div style="min-width:0"><div style="display:flex;align-items:center;gap:6px;font-size:12px;font-weight:500;margin-bottom:8px"><span style="width:7px;height:7px;border-radius:50%;background:{dot}"></span>{title}</div><div style="display:grid;gap:8px">{it}</div></div>'
    kanban = '<div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px">'+kcard('Found',[('Re-keying invoice data','Finance · sizing'),('Status update emails','Delivery')],'#C4C8CE')+kcard('Sized',[('Weekly client updates','9 h/wk · $25,920')],'#9AA0A8')+kcard('Approved',[('Chasing documents','15 h/wk · $43,200')],'#0A0B0D')+kcard('Live',[('Enquiries into CRM','22 h/wk · saving now')],'#85EC68')+'</div>'

    connect_items=[('Email and calendar','When requests arrive, move and get answered.'),('CRM','Enquiries, deals and client hand-offs.'),('Practice and job management','Matters, jobs, cases and their status changes.'),('Finance and billing','Invoices, approvals and payment timing.'),('Document management','When files are created, shared and signed off, never what they say.'),('Ticketing and help desks','Requests, queues and resolution times.')]
    conn=''.join(f'<div style="padding:22px 22px 22px 0;border-bottom:1px solid #EEEFF1"><div style="font-weight:600;font-size:15px">{a}</div><div style="margin-top:4px;font-size:14px;line-height:1.5;color:#5B616B">{b}</div></div>' for a,b in connect_items)

    body = header('plat') + f"""<main>
<section><div style="max-width:1200px;margin:0 auto;padding:88px 24px 0">
<div style="display:flex;flex-wrap:wrap;align-items:flex-end;justify-content:space-between;gap:32px 48px">
<div style="flex:1 1 620px;min-width:0">{eyebrow('Platform')}<h1 class="d" style="{H1}">Operational intelligence for services organisations.</h1></div>
<div style="flex:0 1 420px;min-width:0"><p style="margin:0;font-size:17px;line-height:1.6;color:#5B616B">One live view of how work moves, where it stalls and what it would be worth to automate. Deployed and run with you by our team.</p>{btns(secondary='How we work', shref='HowWeWork-V3.dc.html')}</div>
</div>
<div style="margin-top:56px">{appframe(overview)}</div>
</div></section>

<section><div style="max-width:1200px;margin:0 auto;padding:40px 24px 0">
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(200px,100%),1fr));border-top:1px solid #EEEFF1;border-bottom:1px solid #EEEFF1">
<a href="#map" class="row" style="padding:20px 16px 20px 0"><div style="font-size:12px;color:#8A9099">01</div><div style="margin-top:6px;font-weight:600">Live map</div></a>
<a href="#workflows" class="row" style="padding:20px 16px"><div style="font-size:12px;color:#8A9099">02</div><div style="margin-top:6px;font-weight:600">Workflows</div></a>
<a href="#bottlenecks" class="row" style="padding:20px 16px"><div style="font-size:12px;color:#8A9099">03</div><div style="margin-top:6px;font-weight:600">Bottlenecks</div></a>
<a href="#teams" class="row" style="padding:20px 16px"><div style="font-size:12px;color:#8A9099">04</div><div style="margin-top:6px;font-weight:600">Teams</div></a>
<a href="#reports" class="row" style="padding:20px 16px"><div style="font-size:12px;color:#8A9099">05</div><div style="margin-top:6px;font-weight:600">Reports</div></a>
<a href="#automations" class="row" style="padding:20px 16px"><div style="font-size:12px;color:#8A9099">06</div><div style="margin-top:6px;font-weight:600">Automations</div></a>
</div></div></section>

{module('01','map','Live map','See the whole organisation at once.','Every team, tool and hand-off, drawn from how work really moves and updated as it happens.',['Line weight shows volume, colour shows speed','Click any team to see what flows in and out','No process documents needed to get started'],mapvis)}
{module('02','workflows','Workflows','The process you wrote down, and the ones people follow.','Mission Control finds every route a piece of work takes, how often, and how long each one costs.',['Every route ranked by volume and time','Spot rework loops and detours','Compare teams running the same workflow'],variants,True)}
{module('03','bottlenecks','Bottlenecks and alerts','Know about a delay before your client does.','Queues that grow beyond normal are flagged early, with the cases behind them.',['Alerts when a step slows beyond its normal range','Open the actual cases, not just averages','See the pattern behind a recurring delay'],alerts)}
{module('04','teams','Teams and capacity','Find where the load really sits.','See which teams carry work that belongs elsewhere, and where capacity is quietly being borrowed.',['Load by team, never by individual','Borrowed capacity between workflows','Early warning before a team burns out'],teams,True)}
{module('05','reports','Reports and reviews','A clear read on the business, every month.','A written review of what changed, what is slowing and what to act on, walked through with you by our team.',['Monthly operations review','Board-ready summaries','Trends you can track quarter to quarter'],report)}
{module('06','automations','Automations','Know what to automate, and what it is worth.','Every repetitive task is found, sized in hours and dollars, and tracked from idea to live saving.',['A business case before anything is built','Built, tested and measured by our team','One-click deployment on the roadmap'],kanban,True)}

<section><div style="max-width:1200px;margin:0 auto;padding:128px 24px 0">
<div style="max-width:680px">{eyebrow('From guesswork to a map')}{h2('What changes on day one.')}</div>
<div style="margin-top:40px;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(440px,100%),1fr));gap:16px">
<figure style="margin:0"><div style="border:1px solid #EEEFF1;border-radius:16px;overflow:hidden;aspect-ratio:16/10;background:#FFFFFF"><img src="{TANGLE}" alt="A tangle of hand-offs crossing in every direction." style="width:100%;height:100%;object-fit:cover;display:block"></div><figcaption style="margin-top:12px;font-size:14px;color:#5B616B"><span style="color:#0A0B0D;font-weight:600">Before.</span> Work moves between people with no shared view of the route.</figcaption></figure>
<figure style="margin:0"><div style="border:1px solid #EEEFF1;border-radius:16px;overflow:hidden;aspect-ratio:16/10;background:#FFFFFF"><img src="{CLEAR}" alt="The same people joined by one clear route." style="width:100%;height:100%;object-fit:cover;display:block"></div><figcaption style="margin-top:12px;font-size:14px;color:#5B616B"><span style="color:#0A0B0D;font-weight:600">After.</span> One map, every hand-off visible, the slow steps named.</figcaption></figure>
</div></div></section>

<section id="connect"><div style="max-width:1200px;margin:0 auto;padding:128px 24px 0;display:flex;flex-wrap:wrap;gap:40px 80px">
<div style="flex:1 1 340px;min-width:0">{eyebrow('Connections')}{h2('Works across the systems you already run.')}<p style="{LEAD}">No rip and replace. We connect to your existing tools and capture how work moves between them.</p><a href="Security-V3.dc.html" style="margin-top:20px;display:inline-flex;align-items:center;gap:8px;font-size:15px;font-weight:500">What we capture, and what we never do <span class="ar" aria-hidden="true">→</span></a></div>
<div style="flex:1.4 1 520px;min-width:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(240px,100%),1fr));column-gap:32px;border-top:1px solid #EEEFF1">{conn}</div>
</div></section>
{cta()}
</main>{FOOTER}"""
    script="""class Component extends DCLogic {
  renderVals() { return {}; }
}"""
    return doc('Mission Control | Platform', body, script, 7600)
