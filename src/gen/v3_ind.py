from v3 import *
def ind():
    body = header('ind') + f"""<main>
<section><div style="max-width:1200px;margin:0 auto;padding:88px 24px 0">
<div style="display:flex;flex-wrap:wrap;align-items:flex-end;justify-content:space-between;gap:32px 48px">
<div style="flex:1 1 620px;min-width:0">{eyebrow('Industries')}<h1 class="d" style="{H1}">Built for organisations where the product is the work.</h1></div>
<div style="flex:0 1 420px;min-width:0"><p style="margin:0;font-size:17px;line-height:1.6;color:#5B616B">If work moves between people, inboxes and systems before it reaches a client, Mission Control can map it. We start with services organisations, where that is the whole business.</p>{btns()}</div>
</div>
<div style="margin-top:56px;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(260px,100%),1fr));border-top:1px solid #EEEFF1;border-bottom:1px solid #EEEFF1">
<div style="padding:26px 24px 26px 0"><div class="d" style="font-size:34px;font-weight:500;letter-spacing:-0.03em">50+</div><div style="margin-top:6px;font-size:15px;color:#5B616B">People doing the work, across several teams.</div></div>
<div style="padding:26px 24px"><div class="d" style="font-size:34px;font-weight:500;letter-spacing:-0.03em">Repeatable</div><div style="margin-top:6px;font-size:15px;color:#5B616B">The same kinds of jobs run again and again: files, claims, cases, orders.</div></div>
<div style="padding:26px 0 26px 24px"><div class="d" style="font-size:34px;font-weight:500;letter-spacing:-0.03em">Hand-offs</div><div style="margin-top:6px;font-size:15px;color:#5B616B">Each job passes several people or systems before it is done.</div></div>
</div>
</div></section>

<section id="explore"><div style="max-width:1200px;margin:0 auto;padding:120px 24px 0">
<div style="display:flex;flex-wrap:wrap;justify-content:space-between;align-items:flex-end;gap:24px"><div style="max-width:640px">{eyebrow('What we map')}{h2('See what Mission Control would show your organisation.')}</div><p style="margin:0;max-width:320px;font-size:15px;line-height:1.55;color:#5B616B">Typical patterns from each industry. Illustrative.</p></div>
<div style="margin-top:40px;display:flex;flex-wrap:wrap;gap:32px 56px">
<div role="tablist" aria-label="Industries" style="flex:0 1 300px;min-width:0;display:flex;flex-direction:column;border-top:1px solid #EEEFF1">
<sc-for list="{{{{tabs}}}}" as="t"><button type="button" role="tab" class="tb" onClick="{{{{t.pick}}}}" aria-selected="{{{{t.on}}}}" style="{{{{t.style}}}}">{{{{t.name}}}}<span class="ar" aria-hidden="true">→</span></button></sc-for>
</div>
<div class="fade" style="flex:1 1 560px;min-width:0">
<div style="{CARD};overflow:hidden;box-shadow:0 40px 80px -48px rgba(10,11,13,0.25)">
<div style="padding:24px 28px;border-bottom:1px solid #EEEFF1;display:flex;justify-content:space-between;align-items:baseline;gap:12px;flex-wrap:wrap"><h3 class="d" style="margin:0;font-size:26px;font-weight:500;letter-spacing:-0.02em">{{{{cur.name}}}}</h3><span style="font-size:13px;color:#8A9099">{{{{cur.unit}}}}</span></div>
<div style="padding:24px 28px">
<div style="font-size:12px;font-weight:600;color:#8A9099;letter-spacing:0.04em">TYPICAL ROUTE</div>
<ol style="list-style:none;margin:14px 0 0;padding:0;display:flex;flex-wrap:wrap;gap:8px;align-items:center">
<sc-for list="{{{{cur.route}}}}" as="r"><li style="{{{{r.style}}}}">{{{{r.step}}}}</li></sc-for>
</ol>
</div>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(240px,100%),1fr));border-top:1px solid #EEEFF1">
<div style="padding:24px 28px;border-right:1px solid #EEEFF1"><div style="font-size:12px;font-weight:600;color:#C2510C;letter-spacing:0.04em">WHERE IT USUALLY SLOWS</div><p style="margin:10px 0 0;font-size:16px;line-height:1.55">{{{{cur.slow}}}}</p></div>
<div style="padding:24px 28px"><div style="font-size:12px;font-weight:600;color:#157A36;letter-spacing:0.04em">WHAT WE OFTEN AUTOMATE</div><ul style="margin:10px 0 0;padding:0;list-style:none;display:grid;gap:8px;font-size:15px"><sc-for list="{{{{cur.auto}}}}" as="a"><li style="display:flex;gap:10px"><span aria-hidden="true" style="flex:none;width:6px;height:6px;margin-top:8px;border-radius:50%;background:#85EC68"></span>{{{{a}}}}</li></sc-for></ul></div>
</div>
<div style="padding:18px 28px;border-top:1px solid #EEEFF1;background:#FAFAFB;font-size:14px;color:#5B616B"><span style="color:#0A0B0D;font-weight:600">Who leads it: </span>{{{{cur.who}}}}</div>
</div>
</div>
</div>
</div></section>

<section id="roadmap"><div style="max-width:1200px;margin:0 auto;padding:128px 24px 0">
<div style="position:relative;border-radius:16px;overflow:hidden;background:#0A0B0D;aspect-ratio:16/7">
{video('factory','A technician checks a tablet beside a robot arm on a factory line.')}
<div aria-hidden="true" style="position:absolute;inset:0;background:linear-gradient(0deg,rgba(10,11,13,0.85) 0%,rgba(10,11,13,0) 60%)"></div>
<div style="position:absolute;left:0;right:0;bottom:0;padding:40px;color:#FFFFFF;max-width:640px"><span style="font-size:12px;font-weight:600;letter-spacing:0.04em;color:#0A0B0D;background:#FFFFFF;border-radius:4px;padding:4px 8px">ON THE ROADMAP</span><h2 class="d" style="margin:16px 0 0;font-weight:500;font-size:clamp(28px,3vw,40px);line-height:1.1;letter-spacing:-0.025em">From the inbox to the factory floor.</h2><p style="margin:12px 0 0;font-size:16px;line-height:1.55;color:#C9CED4">The same map, for work that moves through the physical world.</p></div>
</div>
<div style="margin-top:24px;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(250px,100%),1fr));border:1px solid #EEEFF1;border-radius:14px;overflow:hidden">
<div style="padding:26px;border-right:1px solid #EEEFF1"><div style="font-weight:600">Manufacturing</div><p style="margin:6px 0 0;font-size:14px;line-height:1.55;color:#5B616B">Jobs from order to production line to quality check.</p></div>
<div style="padding:26px;border-right:1px solid #EEEFF1"><div style="font-weight:600">Warehousing</div><p style="margin:6px 0 0;font-size:14px;line-height:1.55;color:#5B616B">Stock from receiving to picking to dispatch.</p></div>
<div style="padding:26px;border-right:1px solid #EEEFF1"><div style="font-weight:600">Logistics</div><p style="margin:6px 0 0;font-size:14px;line-height:1.55;color:#5B616B">Every leg between depot, driver and doorstep.</p></div>
<div style="padding:26px"><div style="font-weight:600">Robotics</div><p style="margin:6px 0 0;font-size:14px;line-height:1.55;color:#5B616B">Hand-offs between people, machines and robots.</p></div>
</div>
<div style="margin-top:20px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px;align-items:center"><p style="margin:0;font-size:15px;color:#5B616B">We are building this now with a small number of early partners.</p><a href="Briefing-V3.dc.html" class="b2" style="display:inline-flex;align-items:center;gap:8px;min-height:44px;padding:0 18px;border-radius:8px;border:1px solid #DADCE0;font-size:14px;font-weight:500">Join early access <span class="ar" aria-hidden="true">→</span></a></div>
</div></section>
{cta('Not sure if you fit? Ask us.','A 30-minute briefing. If Mission Control is not right for your organisation, we will tell you.')}
</main>{FOOTER}"""
    script="""class Component extends DCLogic {
  constructor(props) { super(props); this.state = { tab: 0 }; }
  renderVals() {
    var self = this;
    var list = [
      { name: 'Accounting and advisory', unit: 'Client jobs', route: ['Onboarded', 'Documents requested', 'Waiting on client', 'Prepared', 'Partner review', 'Lodged'], slowAt: 2, slow: 'Waiting on clients for documents, then work queuing for partner review.', auto: ['Document requests and reminders', 'Reconciliation preparation', 'Job status updates to clients'], who: 'Practice managers and partners.' },
      { name: 'Legal', unit: 'Matters', route: ['Enquiry', 'Conflict check', 'Engagement', 'Matter opened', 'In progress', 'Billed'], slowAt: 1, slow: 'Conflict checks and engagement letters waiting on sign-off.', auto: ['Intake and conflict searches', 'Engagement letters', 'Time entry reminders'], who: 'Managing partners and operations leads.' },
      { name: 'Insurance', unit: 'Claims', route: ['Lodged', 'Triage', 'Assessment', 'Approval', 'Payment', 'Closed'], slowAt: 2, slow: 'Claims queuing for assessment, then bouncing back for missing information.', auto: ['Claim triage and routing', 'Missing information requests', 'Customer status updates'], who: 'Claims and operations leaders at brokers and underwriting agencies.' },
      { name: 'Financial services and broking', unit: 'Applications', route: ['Enquiry', 'Fact find', 'Documents', 'Submission', 'Approval', 'Settlement'], slowAt: 2, slow: 'Collecting documents from clients before an application can be lodged.', auto: ['Document checklists and chasers', 'CRM and lender data entry', 'Settlement updates'], who: 'Principals and operations managers.' },
      { name: 'Property management', unit: 'Maintenance jobs', route: ['Request', 'Quote', 'Owner approval', 'Booked', 'Completed', 'Paid'], slowAt: 2, slow: 'Jobs waiting on owners to approve quotes.', auto: ['Quote routing and approvals', 'Tenant updates', 'Invoice matching'], who: 'Heads of property management.' },
      { name: 'Recruitment and staffing', unit: 'Roles', route: ['Brief', 'Sourcing', 'Shortlist', 'Interviews', 'Offer', 'Placed'], slowAt: 3, slow: 'Interview scheduling and waiting on client feedback.', auto: ['Interview scheduling', 'Candidate updates', 'CRM notes and admin'], who: 'Directors and delivery leads.' },
      { name: 'Agencies and consultancies', unit: 'Projects', route: ['Brief', 'Scoped', 'Production', 'Client review', 'Delivered', 'Invoiced'], slowAt: 3, slow: 'Client review rounds, and finished work not yet invoiced.', auto: ['Status reports', 'Review reminders', 'Invoicing from delivery'], who: 'Managing directors and heads of delivery.' },
      { name: 'Healthcare administration', unit: 'Referrals', route: ['Referral', 'Triage', 'Booked', 'Appointment', 'Billing', 'Follow-up'], slowAt: 0, slow: 'Referrals sitting in a shared inbox before anyone triages them.', auto: ['Referral intake', 'Booking reminders', 'Billing and claims preparation'], who: 'Practice and group operations managers. We map the admin, never patient records.' }
    ];
    var cur = this.state.tab;
    var tabs = list.map(function (it, i) { var on = i === cur;
      return { name: it.name, on: on ? 'true' : 'false', pick: function () { self.setState({ tab: i }); },
        style: 'display:flex;justify-content:space-between;align-items:center;gap:12px;width:100%;text-align:left;border:0;border-bottom:1px solid #EEEFF1;background:' + (on ? '#FAFAFB' : 'transparent') + ';padding:16px 12px;min-height:44px;cursor:pointer;font:inherit;font-size:15px;font-weight:500;color:' + (on ? '#0A0B0D' : '#5B616B') }; });
    var c = list[cur];
    var route = c.route.map(function (s, i) { var slow = i === c.slowAt;
      return { step: s, style: 'font-size:14px;font-weight:500;border-radius:8px;padding:8px 12px;border:1px solid ' + (slow ? '#E8590C' : '#E7E8EB') + ';background:' + (slow ? '#FFF3EB' : '#FFFFFF') + ';color:' + (slow ? '#B4450A' : '#0A0B0D') }; });
    return { tabs: tabs, cur: { name: c.name, unit: c.unit, route: route, slow: c.slow, auto: c.auto, who: c.who } };
  }
}"""
    return doc('Mission Control | Industries', body, script, 4400)
