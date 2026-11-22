from v3 import *
def sec():
    yes=['When work moves between people, teams and systems','How long each step takes','Status changes and hand-offs','Which system a piece of work moved through']
    no=['The contents of emails or messages','The contents of files and documents','Client or matter details inside your systems','Rankings of individual staff']
    yl=''.join(f'<li style="display:flex;gap:12px;padding:14px 0;border-bottom:1px solid #EEEFF1;font-size:15px"><span aria-hidden="true" style="flex:none;margin-top:2px;width:18px;height:18px;border-radius:50%;background:#85EC68;display:inline-flex;align-items:center;justify-content:center"><svg width="10" height="10" viewBox="0 0 10 10"><path d="M2 5.2l2 2 4-4.4" fill="none" stroke="#0A0B0D" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"></path></svg></span>{x}</li>' for x in yes)
    nl=''.join(f'<li style="display:flex;gap:12px;padding:14px 0;border-bottom:1px solid rgba(255,255,255,0.12);font-size:15px"><span aria-hidden="true" style="flex:none;margin-top:2px;width:18px;height:18px;border-radius:50%;border:1.5px solid #8A9099;display:inline-flex;align-items:center;justify-content:center"><svg width="8" height="8" viewBox="0 0 8 8"><path d="M1.5 1.5l5 5M6.5 1.5l-5 5" stroke="#C9CED4" stroke-width="1.4" stroke-linecap="round"></path></svg></span>{x}</li>' for x in no)
    controls=[('Evidence behind every insight','Every finding links back to the observations it came from, so it can be checked.'),('Logged audit trail','Access and changes are recorded and reviewable.'),('Role-based access','Leaders see what their role needs. Scope is set by you.'),('Scope you control','Choose which teams and systems are included, and change it at any time.'),('Documentation on request','Architecture, data flows and handling details for your IT and legal teams.'),('Attestations as we earn them','Certifications will be published here as they are obtained.')]
    cl=''.join(f'<div style="padding:28px;border-right:1px solid #EEEFF1;border-bottom:1px solid #EEEFF1"><h3 class="d" style="margin:0;font-size:18px;font-weight:500">{a}</h3><p style="margin:8px 0 0;font-size:15px;line-height:1.55;color:#5B616B">{b}</p></div>' for a,b in controls)
    steps=[('Brief leadership','Agree scope, purpose and what will be said to staff.'),('Notify staff in writing','Plain-language notice of what is captured and why, ahead of switch-on, in line with workplace surveillance rules where you operate.'),('Answer questions','A short session for teams, with our team present.'),('Switch on and review','Start with the agreed scope and review it together.')]
    sl=''.join(f'<li style="display:flex;gap:20px;padding:20px 0;border-bottom:1px solid #EEEFF1"><span style="flex:none;width:28px;font-size:13px;color:#8A9099;padding-top:2px">0{i+1}</span><div><div style="font-weight:600">{a}</div><div style="margin-top:4px;font-size:15px;line-height:1.55;color:#5B616B">{b}</div></div></li>' for i,(a,b) in enumerate(steps))
    body = header('sec') + f"""<main>
<section><div style="max-width:1200px;margin:0 auto;padding:88px 24px 0">
<div style="display:flex;flex-wrap:wrap;align-items:flex-end;justify-content:space-between;gap:32px 48px">
<div style="flex:1 1 620px;min-width:0">{eyebrow('Security and privacy')}<h1 class="d" style="{H1}">Designed to pass your security review.</h1></div>
<div style="flex:0 1 420px;min-width:0"><p style="margin:0;font-size:17px;line-height:1.6;color:#5B616B">Mission Control maps how work moves. It is built to capture as little as possible, to be rolled out openly, and to stand up to scrutiny from your IT, legal and people teams.</p>{btns('Request documentation')}</div>
</div></div></section>

<section><div style="max-width:1200px;margin:0 auto;padding:72px 24px 0">
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(460px,100%),1fr));border-radius:16px;overflow:hidden;border:1px solid #EEEFF1">
<div style="padding:40px"><p style="margin:0;font-size:13px;font-weight:600;color:#157A36;letter-spacing:0.04em">WHAT WE CAPTURE</p><h2 class="d" style="margin:12px 0 0;font-size:28px;font-weight:500;letter-spacing:-0.02em">The movement of work.</h2><ul style="margin:24px 0 0;padding:0;list-style:none;border-top:1px solid #EEEFF1">{yl}</ul></div>
<div style="padding:40px;background:#0A0B0D;color:#FFFFFF"><p style="margin:0;font-size:13px;font-weight:600;color:#A7ADB6;letter-spacing:0.04em">WHAT WE NEVER CAPTURE</p><h2 class="d" style="margin:12px 0 0;font-size:28px;font-weight:500;letter-spacing:-0.02em">What the work says.</h2><ul style="margin:24px 0 0;padding:0;list-style:none;border-top:1px solid rgba(255,255,255,0.12)">{nl}</ul></div>
</div></div></section>

<section><div style="max-width:1200px;margin:0 auto;padding:128px 24px 0">
<div style="max-width:640px">{eyebrow('Controls')}{h2('Built for organisations that cannot get this wrong.')}</div>
<div style="margin-top:40px;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(320px,100%),1fr));border-top:1px solid #EEEFF1;border-left:1px solid #EEEFF1;border-radius:0">{cl}</div>
</div></section>

<section><div style="max-width:1200px;margin:0 auto;padding:128px 24px 0;display:flex;flex-wrap:wrap;gap:48px 72px;align-items:center">
<div style="flex:1.1 1 460px;min-width:0;position:relative;border-radius:16px;overflow:hidden;background:#0A0B0D;aspect-ratio:4/3.6">{video('whiteboard','A team discusses a rollout plan at a whiteboard.')}</div>
<div style="flex:1 1 400px;min-width:0">{eyebrow('Rolling out with your people')}{h2('Open by default. No surprises for staff.')}<p style="{LEAD}">Mission Control measures how work moves, not how individuals perform. We help you say that clearly, before anything is switched on.</p><ol style="margin:28px 0 0;padding:0;list-style:none;border-top:1px solid #EEEFF1">{sl}</ol></div>
</div></section>

<section><div style="max-width:1200px;margin:0 auto;padding:128px 24px 0;display:flex;flex-wrap:wrap;gap:40px 80px">
<div style="flex:1 1 300px">{eyebrow('Questions')}{h2('For your IT and legal teams.')}</div>
<div style="flex:2 1 560px;min-width:0">{FAQ_MARKUP}</div>
</div></section>
{cta('Bring your security questions.','Book a briefing with your IT or legal lead in the room. We will walk through exactly what is captured and how.')}
</main>{FOOTER}"""
    faq=[['Do you read emails or documents?','No. Mission Control records when work moves and where it goes. It does not capture what emails, messages or documents say.'],
         ['Is this employee monitoring?','It measures how work flows between teams and systems, not individual performance. We help you notify staff in writing before switch-on.'],
         ['Can we limit what is in scope?','Yes. You choose which teams and systems are included, and can change that at any time.'],
         ['What documentation can you provide?','Architecture, data flow and data handling documentation is available on request for your security review.'],
         ['Do you hold certifications?','We will publish certifications and attestations here as we obtain them. Ask us about current status in your briefing.']]
    script="""class Component extends DCLogic {
  constructor(props) { super(props); this.state = { faq: 0 }; }
  renderVals() { var self = this;
    """ + faq_js(faq) + """
    return { faqs: faqs }; }
}"""
    return doc('Mission Control | Security and privacy', body, script, 4800)
