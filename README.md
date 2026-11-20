# Mission Control website

Static marketing site for Mission Control, deployed on Vercel.

- Pages: `index.html`, `platform.html`, `how-we-work.html`, `industries.html`, `security.html`, `company.html`, `briefing.html` (clean URLs).
- `mc.js`: small runtime that keeps tabs, FAQs and the briefing form interactive. Pages are prerendered, so content is in the HTML.
- `api/briefing.js`: emails briefing requests through Resend. Set `RESEND_API_KEY`, `BRIEFING_TO` and optionally `BRIEFING_FROM` in Vercel.
- `src/design/`: the Claude Design source pages. `src/build.py` + `src/prerender.js` regenerate the site from them.
- Live at https://missioncntrl.io.
