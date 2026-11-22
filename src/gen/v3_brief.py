from v3 import *
def brief():
    inp="height:46px;border:1px solid #DADCE0;border-radius:8px;padding:0 12px;font:inherit;font-size:15px;background:#FFFFFF;color:#0A0B0D;width:100%"
    lab="display:grid;gap:7px;font-size:13px;font-weight:500"
    steps=[('We reply within one business day','With a few times that suit you.'),('A 30-minute briefing','We walk through a live map and ask where work gets stuck.'),('A straight answer','If Mission Control is a fit, we scope it. If not, we say so.')]
    sl=''.join(f'<li style="display:flex;gap:18px;padding:18px 0;border-bottom:1px solid #EEEFF1"><span style="flex:none;width:28px;font-size:13px;color:#8A9099;padding-top:2px">0{i+1}</span><div><div style="font-weight:600">{a}</div><div style="margin-top:2px;font-size:15px;color:#5B616B">{b}</div></div></li>' for i,(a,b) in enumerate(steps))
    body = header('') + f"""<main>
<section><div style="max-width:1200px;margin:0 auto;padding:88px 24px 0;display:flex;flex-wrap:wrap;gap:48px 80px;align-items:flex-start">
<div style="flex:1 1 400px;min-width:0">
{eyebrow('Book a briefing')}<h1 class="d" style="{H1}">See your organisation from above.</h1>
<p style="{LEAD};max-width:460px">Tell us a little about your organisation. A member of our team will be in touch to arrange a time.</p>
<ol style="margin:32px 0 0;padding:0;list-style:none;border-top:1px solid #EEEFF1">{sl}</ol>
<div style="margin-top:32px;position:relative;border-radius:14px;overflow:hidden;background:#0A0B0D;aspect-ratio:16/9">{video('call','A business leader smiles on a video call.')}</div>
<p style="margin:18px 0 0;font-size:14px;color:#5B616B">Prefer email? <a href="mailto:hello@missioncntrl.io" style="color:#0A0B0D;font-weight:500;text-decoration:underline;text-underline-offset:3px">hello@missioncntrl.io</a></p>
</div>
<div style="flex:1.1 1 460px;min-width:0;position:sticky;top:96px">
<form onSubmit="{{{{submit}}}}" style="{CARD};padding:32px;display:grid;gap:18px;box-shadow:0 40px 80px -48px rgba(10,11,13,0.3)">
<sc-if value="{{{{sent}}}}" hint-placeholder-val="{{{{false}}}}"><div role="status" class="fade" style="display:flex;gap:10px;align-items:center;border:1px solid #D7F5CC;background:#F4FDF0;border-radius:8px;padding:12px 14px;font-size:14px"><span style="width:8px;height:8px;border-radius:50%;background:#85EC68"></span>Thank you. We will be in touch within one business day.</div></sc-if>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(190px,100%),1fr));gap:16px">
<label style="{lab}">First name<input class="in" type="text" name="first" required="" autocomplete="given-name" style="{inp}"></label>
<label style="{lab}">Last name<input class="in" type="text" name="last" autocomplete="family-name" style="{inp}"></label>
</div>
<input type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-9999px;width:1px;height:1px;opacity:0">
<label style="{lab}">Work email<input class="in" type="email" name="email" required="" autocomplete="email" style="{inp}"></label>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(190px,100%),1fr));gap:16px">
<label style="{lab}">Organisation<input class="in" type="text" name="org" autocomplete="organization" style="{inp}"></label>
<label style="{lab}">Your role<input class="in" type="text" name="role" autocomplete="organization-title" style="{inp}"></label>
</div>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(190px,100%),1fr));gap:16px">
<label style="{lab}">Organisation size<select class="in" name="size" style="{inp}"><option>20 to 50 people</option><option>50 to 200 people</option><option>200 to 1,000 people</option><option>1,000+ people</option></select></label>
<label style="{lab}">Industry<select class="in" name="industry" style="{inp}"><option>Accounting and advisory</option><option>Legal</option><option>Insurance</option><option>Financial services and broking</option><option>Property management</option><option>Recruitment and staffing</option><option>Agency or consultancy</option><option>Healthcare administration</option><option>Manufacturing or logistics (early access)</option><option>Other</option></select></label>
</div>
<label style="{lab}">Where does work get stuck today? <span style="font-weight:400;color:#8A9099">Optional</span><textarea class="in" name="message" rows="4" style="border:1px solid #DADCE0;border-radius:8px;padding:10px 12px;font:inherit;font-size:15px;resize:vertical;width:100%"></textarea></label>
<sc-if value="{{{{failed}}}}" hint-placeholder-val="{{{{false}}}}"><div role="alert" style="border:1px solid #F6D2BD;background:#FFF6F0;border-radius:8px;padding:12px 14px;font-size:14px;color:#8A3A08">Something went wrong sending your request. Please email <a href="mailto:hello@missioncntrl.io" style="text-decoration:underline">hello@missioncntrl.io</a> and we will be in touch.</div></sc-if>
<button type="submit" class="b1" style="display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:48px;border:0;border-radius:8px;background:#0A0B0D;color:#FFFFFF;font:inherit;font-size:15px;font-weight:500;cursor:pointer">{{{{btnLabel}}}} <span class="ar" aria-hidden="true">→</span></button>
<p style="margin:0;font-size:12px;line-height:1.5;color:#8A9099">We use these details only to arrange your briefing.</p>
</form>
</div>
</div></section>

<section><div style="max-width:1200px;margin:0 auto;padding:128px 24px 96px">
<div style="max-width:620px">{eyebrow('Engagement model')}{h2('What working together looks like.')}</div>
<div style="margin-top:40px;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(300px,100%),1fr));border:1px solid #EEEFF1;border-radius:14px;overflow:hidden">
<div style="padding:32px;border-right:1px solid #EEEFF1"><div style="font-size:13px;color:#8A9099">One-off</div><h3 class="d" style="margin:10px 0 0;font-size:22px;font-weight:500">Implementation</h3><p style="margin:10px 0 0;font-size:15px;line-height:1.55;color:#5B616B">Deployment, connections, staff briefing and your first review.</p></div>
<div style="padding:32px;border-right:1px solid #EEEFF1"><div style="font-size:13px;color:#8A9099">Ongoing</div><h3 class="d" style="margin:10px 0 0;font-size:22px;font-weight:500">Platform</h3><p style="margin:10px 0 0;font-size:15px;line-height:1.55;color:#5B616B">Live map, monthly reviews and a named engagement lead.</p></div>
<div style="padding:32px"><div style="font-size:13px;color:#8A9099">Per automation</div><h3 class="d" style="margin:10px 0 0;font-size:22px;font-weight:500">Automations</h3><p style="margin:10px 0 0;font-size:15px;line-height:1.55;color:#5B616B">Priced individually, after you approve the business case.</p></div>
</div>
<a href="HowWeWork-V3.dc.html" style="margin-top:24px;display:inline-flex;align-items:center;gap:8px;font-size:15px;font-weight:500">How an engagement runs <span class="ar" aria-hidden="true">→</span></a>
</div></section>
</main>{FOOTER}"""
    script="""class Component extends DCLogic {
  constructor(props) { super(props); this.state = { status: 'idle' }; }
  renderVals() { var self = this; var st = this.state.status;
    return { sent: st === 'sent', failed: st === 'error', btnLabel: st === 'sending' ? 'Sending...' : 'Request a briefing',
      submit: function (e) { if (e && e.preventDefault) e.preventDefault();
        var form = e && e.target; var data = {};
        if (form && form.elements) { for (var i = 0; i < form.elements.length; i++) { var el = form.elements[i]; if (el.name) data[el.name] = el.value; } }
        self.setState({ status: 'sending' });
        fetch('/api/briefing', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) })
          .then(function (r) { self.setState({ status: r.ok ? 'sent' : 'error' }); if (r.ok && form && form.reset) form.reset(); })
          .catch(function () { self.setState({ status: 'error' }); });
      } }; }
}"""
    return doc('Mission Control | Book a briefing', body, script, 2600)
