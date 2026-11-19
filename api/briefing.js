// Briefing request handler. Emails the request through Resend when RESEND_API_KEY and BRIEFING_TO are set.
const EMAIL_RE = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;
const esc = (s) => String(s || '').slice(0, 5000).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

module.exports = async (req, res) => {
  if (req.method !== 'POST') { res.setHeader('Allow', 'POST'); return res.status(405).json({ ok: false }); }
  let b = req.body || {};
  if (typeof b === 'string') { try { b = JSON.parse(b); } catch (e) { b = {}; } }
  if (b.website) return res.status(200).json({ ok: true });
  const email = String(b.email || '').trim();
  const name = [b.first, b.last].filter(Boolean).join(' ').trim();
  if (!name || !EMAIL_RE.test(email)) return res.status(400).json({ ok: false, error: 'invalid' });

  const key = process.env.RESEND_API_KEY;
  const to = process.env.BRIEFING_TO;
  const from = process.env.BRIEFING_FROM || 'Mission Control website <website@missioncntrl.io>';
  if (!key || !to) {
    console.warn('Briefing request received but email delivery is not configured (RESEND_API_KEY / BRIEFING_TO).', JSON.stringify({ name, email, org: b.org }));
    return res.status(503).json({ ok: false, error: 'not_configured' });
  }
  const rows = [['Name', name], ['Email', email], ['Organisation', b.org], ['Role', b.role], ['Size', b.size], ['Industry', b.industry], ['Where work gets stuck', b.message]]
    .map(([k, v]) => `<tr><td style="padding:6px 12px 6px 0;color:#5B616B;vertical-align:top">${k}</td><td style="padding:6px 0;white-space:pre-wrap">${esc(v)}</td></tr>`).join('');
  const r = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: { Authorization: `Bearer ${key}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({ from, to: to.split(',').map((x) => x.trim()), reply_to: email, subject: `Briefing request: ${name}${b.org ? ' (' + String(b.org).slice(0, 80) + ')' : ''}`, html: `<table style="font-family:Arial,sans-serif;font-size:14px">${rows}</table>` }),
  });
  if (!r.ok) { console.error('Resend error', r.status, await r.text()); return res.status(502).json({ ok: false }); }
  return res.status(200).json({ ok: true });
};
