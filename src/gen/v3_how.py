from v3 import *
def how():
    roles=[('Engagement lead','Owns the relationship, the plan and every review. Your one point of contact.'),('Implementation engineer','Deploys the platform and connects your systems.'),('Operations analyst','Reads the map, finds the patterns and writes your reviews.'),('Automation engineer','Builds, tests and measures each automation you approve.')]
    rl=''.join(f'<div style="padding:28px;border-right:1px solid #EEEFF1"><div style="width:40px;height:40px;border-radius:10px;background:#F2F3F5;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:600">{"".join(w[0] for w in a.split()[:2])}</div><h3 class="d" style="margin:24px 0 0;font-size:19px;font-weight:500">{a}</h3><p style="margin:8px 0 0;font-size:15px;line-height:1.55;color:#5B616B">{b}</p></div>' for a,b in roles)
    need=[('An executive sponsor','Someone who owns the outcome and joins the reviews.'),('An IT contact','To approve access to the systems in scope.'),('Team leads, briefly','Short walkthroughs so we understand how their work runs.'),('Open communication with staff','We help you brief your people before anything is switched on.')]
    nd=''.join(f'<li style="display:flex;gap:16px;padding:18px 0;border-bottom:1px solid #EEEFF1"><span aria-hidden="true" style="flex:none;margin-top:3px;width:18px;height:18px;border-radius:50%;border:1.5px solid #0A0B0D;display:inline-flex;align-items:center;justify-content:center"><svg width="10" height="10" viewBox="0 0 10 10"><path d="M2 5.2l2 2 4-4.4" fill="none" stroke="#0A0B0D" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"></path></svg></span><div><div style="font-weight:600">{a}</div><div style="margin-top:2px;font-size:15px;color:#5B616B">{b}</div></div></li>' for a,b in need)
    body = header('how') + f"""<main>
<section><div style="max-width:1200px;margin:0 auto;padding:88px 24px 0">
<div style="display:flex;flex-wrap:wrap;align-items:flex-end;justify-content:space-between;gap:32px 48px">
<div style="flex:1 1 620px;min-width:0">{eyebrow('How we work')}<h1 class="d" style="{H1}">Software, delivered by people who run operations.</h1></div>
<div style="flex:0 1 420px;min-width:0"><p style="margin:0;font-size:17px;line-height:1.6;color:#5B616B">Mission Control is not a tool you are left to figure out. Our team deploys it, reads it with you and builds what it recommends.</p>{btns()}</div>
</div>
<div style="margin-top:56px;position:relative;border-radius:16px;overflow:hidden;background:#0A0B0D;aspect-ratio:16/7">{video('whiteboard','A team maps a workflow on a whiteboard.')}</div>
</div></section>

<section><div style="max-width:1200px;margin:0 auto;padding:128px 24px 0">
<div style="display:flex;flex-wrap:wrap;justify-content:space-between;align-items:flex-end;gap:24px"><div style="max-width:640px">{eyebrow('The engagement')}{h2('From first briefing to automations that pay for themselves.')}</div><p style="margin:0;max-width:340px;font-size:15px;line-height:1.55;color:#5B616B">Select a stage to see what happens and what you receive.</p></div>
<div style="margin-top:40px;display:flex;flex-wrap:wrap;gap:40px 64px">
<ol style="flex:1 1 340px;min-width:0;list-style:none;margin:0;padding:0;border-top:1px solid #EEEFF1">
<sc-for list="{{{{phases}}}}" as="p"><li style="border-bottom:1px solid #EEEFF1"><button type="button" class="tb" onClick="{{{{p.pick}}}}" aria-pressed="{{{{p.on}}}}" style="{{{{p.btn}}}}"><span style="{{{{p.num}}}}">{{{{p.n}}}}</span><span style="flex:1;text-align:left">{{{{p.title}}}}</span><span style="font-size:13px;color:#8A9099">{{{{p.when}}}}</span></button></li></sc-for>
</ol>
<div class="fade" style="flex:1.3 1 480px;min-width:0;background:#FAFAFB;border:1px solid #EEEFF1;border-radius:16px;padding:36px">
<div style="font-size:13px;color:#8A9099">Stage {{{{cur.n}}}} · {{{{cur.when}}}}</div>
<h3 class="d" style="margin:10px 0 0;font-size:32px;font-weight:500;letter-spacing:-0.025em">{{{{cur.title}}}}</h3>
<p style="margin:14px 0 0;font-size:16px;line-height:1.65;color:#5B616B">{{{{cur.body}}}}</p>
<div style="margin-top:28px;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(200px,100%),1fr));gap:20px">
<div><div style="font-size:12px;font-weight:600;color:#8A9099;letter-spacing:0.04em">YOU RECEIVE</div><ul style="margin:10px 0 0;padding:0;list-style:none;display:grid;gap:8px;font-size:15px"><sc-for list="{{{{cur.gets}}}}" as="g"><li style="display:flex;gap:10px"><span aria-hidden="true" style="flex:none;width:6px;height:6px;margin-top:8px;border-radius:50%;background:#85EC68"></span>{{{{g}}}}</li></sc-for></ul></div>
<div><div style="font-size:12px;font-weight:600;color:#8A9099;letter-spacing:0.04em">WHO IS INVOLVED</div><p style="margin:10px 0 0;font-size:15px;line-height:1.55">{{{{cur.who}}}}</p></div>
</div>
</div>
</div>
</div></section>

<section><div style="max-width:1200px;margin:0 auto;padding:128px 24px 0">
<div style="max-width:640px">{eyebrow('Your team')}{h2('A dedicated team on every engagement.')}</div>
<div style="margin-top:40px;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(260px,100%),1fr));border:1px solid #EEEFF1;border-radius:14px;overflow:hidden">{rl}</div>
</div></section>

<section><div style="max-width:1200px;margin:0 auto;padding:128px 24px 0;display:flex;flex-wrap:wrap;gap:48px 72px;align-items:center">
<div style="flex:1 1 400px;min-width:0">{eyebrow('What we need from you')}{h2('Light on your time. Clear on ownership.')}<ul style="margin:28px 0 0;padding:0;list-style:none;border-top:1px solid #EEEFF1">{nd}</ul></div>
<div style="flex:1.1 1 460px;min-width:0;position:relative;border-radius:16px;overflow:hidden;background:#0A0B0D;aspect-ratio:4/4.4">{video('leader','An operations leader reviews her screen.')}</div>
</div></section>

<section id="model"><div style="max-width:1200px;margin:0 auto;padding:128px 24px 0">
<div style="display:flex;flex-wrap:wrap;justify-content:space-between;align-items:flex-end;gap:24px"><div style="max-width:620px">{eyebrow('Engagement model')}{h2('Three parts. Scoped and quoted upfront.')}</div><a href="Briefing-V3.dc.html" style="display:inline-flex;align-items:center;gap:8px;font-size:15px;font-weight:500">Discuss your scope <span class="ar" aria-hidden="true">→</span></a></div>
<div style="margin-top:40px;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(300px,100%),1fr));border:1px solid #EEEFF1;border-radius:14px;overflow:hidden">
<div style="padding:32px;border-right:1px solid #EEEFF1"><div style="font-size:13px;color:#8A9099">One-off</div><h3 class="d" style="margin:10px 0 0;font-size:24px;font-weight:500;letter-spacing:-0.02em">Implementation</h3><ul style="margin:18px 0 0;padding:0;list-style:none;display:grid;gap:10px;font-size:15px;color:#5B616B"><li>Deployment and system connections</li><li>Staff briefing plan and materials</li><li>Your first map and diagnostic review</li></ul></div>
<div style="padding:32px;border-right:1px solid #EEEFF1;background:#0A0B0D;color:#FFFFFF"><div style="font-size:13px;color:#A7ADB6">Ongoing</div><h3 class="d" style="margin:10px 0 0;font-size:24px;font-weight:500;letter-spacing:-0.02em">Platform</h3><ul style="margin:18px 0 0;padding:0;list-style:none;display:grid;gap:10px;font-size:15px;color:#C9CED4"><li>Live map, workflows and alerts</li><li>Monthly operations review</li><li>A named engagement lead</li></ul></div>
<div style="padding:32px"><div style="font-size:13px;color:#8A9099">Per automation</div><h3 class="d" style="margin:10px 0 0;font-size:24px;font-weight:500;letter-spacing:-0.02em">Automations</h3><ul style="margin:18px 0 0;padding:0;list-style:none;display:grid;gap:10px;font-size:15px;color:#5B616B"><li>Business case before any build</li><li>Built, tested and measured</li><li>Priced individually once approved</li></ul></div>
</div></div></section>

<section><div style="max-width:1200px;margin:0 auto;padding:128px 24px 0;display:flex;flex-wrap:wrap;gap:40px 80px">
<div style="flex:1 1 300px">{eyebrow('Questions')}{h2('Before you book.')}</div>
<div style="flex:2 1 560px;min-width:0">{FAQ_MARKUP}</div>
</div></section>
{cta()}
</main>{FOOTER}"""
    faq=[['Is this consulting or software?','Both, by design. You get a platform that maps your organisation continuously, and a team that interprets it with you and builds the automations.'],
         ['Do we need to change our systems?','No. Mission Control connects to the tools you already use. Nothing is replaced.'],
         ['Can we start with one team or workflow?','Yes. Many organisations start with one area where the pain is clearest, then expand once the map proves its value.'],
         ['How are automations priced?','Each one is scoped and priced on its own, after you have seen and approved its business case.'],
         ['How do we explain this to our staff?','We give you a briefing plan and materials. Mission Control measures how work moves, not individual performance, and we recommend saying so plainly.']]
    script="""class Component extends DCLogic {
  constructor(props) { super(props); this.state = { phase: 0, faq: 0 }; }
  renderVals() {
    var self = this;
    var data = [
      { title: 'Briefing', when: 'Week 0', body: 'A working session with your leadership. We walk through a live map, hear where the pain is and agree whether there is a fit.', gets: ['A clear read on fit', 'Areas to start with'], who: 'Your leadership and our engagement lead.' },
      { title: 'Scope and proposal', when: 'Week 0', body: 'We define the teams, workflows and systems in scope and quote every part upfront.', gets: ['Written scope', 'Fixed implementation quote', 'Rollout and staff briefing plan'], who: 'Your sponsor, IT contact and our engagement lead.' },
      { title: 'Deploy', when: 'Weeks 1 to 2', body: 'We install Mission Control, connect your systems and brief your staff openly before anything is switched on.', gets: ['Systems connected', 'Staff briefed', 'Access set up for your leaders'], who: 'Your IT contact and our implementation engineer.' },
      { title: 'Map', when: 'Weeks 2 to 6', body: 'Your map fills in as work moves. We check it against how your teams describe their work.', gets: ['Live map', 'Workflow routes', 'First bottleneck list'], who: 'Team leads, briefly, and our operations analyst.' },
      { title: 'Diagnose', when: 'Monthly', body: 'A written operations review: what is fast, what is slow, why, and what to change.', gets: ['Monthly review', 'Ranked automation shortlist', 'Business cases'], who: 'Your sponsor and our engagement lead.' },
      { title: 'Automate', when: 'Ongoing', body: 'You approve the business cases you want. We build, test and measure each automation on your map.', gets: ['Live automations', 'Measured time saved', 'Next opportunities'], who: 'Your process owners and our automation engineer.' }
    ];
    var cur = this.state.phase;
    var phases = data.map(function (d, i) { var on = i === cur;
      return { n: '0' + (i + 1), title: d.title, when: d.when, on: on ? 'true' : 'false', pick: function () { self.setState({ phase: i }); },
        btn: 'width:100%;display:flex;align-items:center;gap:18px;border:0;background:' + (on ? '#FAFAFB' : 'transparent') + ';padding:20px 12px;min-height:44px;cursor:pointer;font:inherit;font-size:17px;font-weight:500;color:' + (on ? '#0A0B0D' : '#5B616B'),
        num: 'flex:none;width:28px;font-size:13px;color:' + (on ? '#157A36' : '#8A9099') }; });
    var d = data[cur];
    """ + faq_js(faq) + """
    return { phases: phases, cur: { n: cur + 1, title: d.title, when: d.when, body: d.body, gets: d.gets, who: d.who }, faqs: faqs };
  }
}"""
    return doc('Mission Control | How we work', body, script, 6200)
