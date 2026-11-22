from v3 import *
def co():
    principles=[('Operators, not observers','We run services businesses ourselves. We build for the person accountable on Monday morning.'),('Evidence over opinion','Every insight traces back to what actually happened. No black boxes.'),('About the work, not the people','We measure how work moves, never how individuals perform.'),('Value before spend','Nothing gets built until the business case is clear.')]
    pl=''.join(f'<div style="padding:28px;border-right:1px solid #EEEFF1"><div style="font-size:13px;color:#8A9099">0{i+1}</div><h3 class="d" style="margin:28px 0 0;font-size:19px;font-weight:500">{a}</h3><p style="margin:8px 0 0;font-size:15px;line-height:1.55;color:#5B616B">{b}</p></div>' for i,(a,b) in enumerate(principles))
    def person(init,name,role,bio):
        return f'<div style="{CARD};padding:28px;display:flex;gap:20px;align-items:flex-start"><div aria-hidden="true" class="d" style="flex:none;width:64px;height:64px;border-radius:14px;background:#0A0B0D;color:#FFFFFF;display:flex;align-items:center;justify-content:center;font-size:20px;font-weight:500">{init}</div><div><h3 class="d" style="margin:0;font-size:20px;font-weight:500">{name}</h3><div style="margin-top:2px;font-size:14px;color:#8A9099">{role}</div><p style="margin:12px 0 0;font-size:15px;line-height:1.6;color:#5B616B">{bio}</p></div></div>'
    body = header('co') + f"""<main>
<section><div style="max-width:1200px;margin:0 auto;padding:88px 24px 0">
<div style="max-width:860px">{eyebrow('Company')}<h1 class="d" style="{H1}">We built Mission Control because we needed it.</h1><p style="{LEAD};max-width:640px">We run a services business. Like every operator, we could see the outcomes but not the work that produced them. So we built the map we wanted, and ran it on ourselves first.</p></div>
<div style="margin-top:56px;position:relative;border-radius:16px;overflow:hidden;background:#0A0B0D;aspect-ratio:16/7">{video('overhead','Overhead view of an office with glowing trails tracing how work moves.')}</div>
</div></section>

<section><div style="max-width:1200px;margin:0 auto;padding:128px 24px 0;display:flex;flex-wrap:wrap;gap:40px 80px">
<div style="flex:1 1 360px;min-width:0">{eyebrow('Proof, on ourselves')}{h2('We ran Mission Control on our own business first.')}<p style="{LEAD}">We followed one workflow end to end: staff offboarding. The documented process had one path. Reality had several.</p></div>
<div style="flex:1.2 1 480px;min-width:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(180px,100%),1fr));border-top:1px solid #EEEFF1">
<div style="padding:28px 20px 28px 0;border-bottom:1px solid #EEEFF1"><div class="d" style="font-size:48px;font-weight:500;letter-spacing:-0.04em">184</div><div style="margin-top:6px;font-size:14px;color:#5B616B">Cases traced end to end</div></div>
<div style="padding:28px 20px;border-bottom:1px solid #EEEFF1"><div class="d" style="font-size:48px;font-weight:500;letter-spacing:-0.04em">40%</div><div style="margin-top:6px;font-size:14px;color:#5B616B">Took a path no procedure described</div></div>
<div style="padding:28px 0 28px 20px;border-bottom:1px solid #EEEFF1"><div class="d" style="font-size:48px;font-weight:500;letter-spacing:-0.04em">21h</div><div style="margin-top:6px;font-size:14px;color:#5B616B">Longest wait, traced to one person carrying two workflows</div></div>
</div>
</div></section>

<section><div style="max-width:1200px;margin:0 auto;padding:128px 24px 0">
<div style="max-width:640px">{eyebrow('What we believe')}{h2('How we build, and how we work with you.')}</div>
<div style="margin-top:40px;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(260px,100%),1fr));border:1px solid #EEEFF1;border-radius:14px;overflow:hidden">{pl}</div>
</div></section>

<section><div style="max-width:1200px;margin:0 auto;padding:128px 24px 0">
<div style="max-width:640px">{eyebrow('Leadership')}{h2('The team you will work with.')}</div>
<div style="margin-top:40px;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(440px,100%),1fr));gap:16px">
{person('AH','Abdurrahman Haroon','Co-founder','Has spent his career building and running services businesses, and the operational foundations behind them.')}
{person('AS','Amresh Selvaskandan','Co-founder','Works across operations and delivery strategy, and stays hands-on with every implementation.')}
{person('IS','Isuru','Head of Operations','Runs delivery on every engagement, from deployment through to the automations clients approve.')}
</div>
</div></section>

<section><div style="max-width:1200px;margin:0 auto;padding:128px 24px 0;display:flex;flex-wrap:wrap;gap:48px 72px;align-items:center">
<div style="flex:1 1 400px;min-width:0">{eyebrow('Work with us')}{h2('We are building the team.')}<p style="{LEAD}">We are looking for operators, analysts and engineers who want to see how organisations really work, and make them better.</p><a href="mailto:hello@missioncntrl.io" style="margin-top:22px;display:inline-flex;align-items:center;gap:8px;font-size:15px;font-weight:500">hello@missioncntrl.io <span class="ar" aria-hidden="true">→</span></a></div>
<div style="flex:1.1 1 460px;min-width:0;position:relative;border-radius:16px;overflow:hidden;background:#0A0B0D;aspect-ratio:4/3.4">{video('whiteboard','A team works through a problem at a whiteboard.')}</div>
</div></section>
{cta()}
</main>{FOOTER}"""
    script="""class Component extends DCLogic {
  renderVals() { return {}; }
}"""
    return doc('Mission Control | Company', body, script, 4600)
