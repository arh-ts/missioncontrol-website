// Adds a "Request an AI summary" strip to every page footer.
// Each button opens an AI assistant with a prefilled prompt about this site.
// Usage: node ai-summary.js <site: lexops|missioncontrol> <dir> [<dir> ...]
// Idempotent: footers that already carry the strip are left alone.
const fs = require('fs');
const path = require('path');

const SITES = {
  lexops: {
    name: 'LexOps',
    prompt: 'Summarise what LexOps (https://lex-ops.io) does, who it works with and how its partnership model works. Use https://lex-ops.io and https://lex-ops.io/llms.txt as your sources.',
    label: '#1A2029', muted: '#5B6573', line: '#E3E7EC', hover: '#F3F5F7', top: '56px'
  },
  missioncontrol: {
    name: 'Mission Control',
    prompt: 'Summarise what Mission Control (https://missioncntrl.io) does, who it is for and how engagements work. Use https://missioncntrl.io and https://missioncntrl.io/llms.txt as your sources.',
    label: '#0A0B0D', muted: '#5B616B', line: '#E7E8EB', hover: '#F2F3F5', top: '40px'
  }
};

function block(s) {
  const q = encodeURIComponent(s.prompt);
  const ais = [
    ['ChatGPT', 'https://chatgpt.com/?q=' + q],
    ['Claude', 'https://claude.ai/new?q=' + q],
    ['Google AI', 'https://www.google.com/search?udm=50&q=' + q],
    ['Perplexity', 'https://www.perplexity.ai/search/new?q=' + q],
    ['Grok', 'https://grok.com/?q=' + q]
  ];
  const links = ais.map(([n, u]) =>
    `<a class="ais-b" href="${u}" target="_blank" rel="noopener noreferrer" aria-label="Ask ${n} for a summary of ${s.name} (opens in a new tab)">${n}</a>`).join('');
  return `<div class="ais" data-ai-summary style="margin-top:${s.top};display:flex;flex-wrap:wrap;align-items:center;gap:12px 20px">` +
    `<style>.ais-b{display:inline-flex;align-items:center;min-height:36px;padding:0 14px;border:1px solid ${s.line};border-radius:999px;font-size:13px;font-weight:500;color:${s.muted};background:transparent;text-decoration:none;transition:background .15s,color .15s,border-color .15s}.ais-b:hover,.ais-b:focus-visible{background:${s.hover};color:${s.label};border-color:${s.label}}</style>` +
    `<span style="font-size:13px;font-weight:600;color:${s.label}">Request an AI summary of ${s.name}</span>` +
    `<span role="list" style="display:flex;flex-wrap:wrap;gap:8px">${links.replace(/<a /g, '<a role="listitem" ')}</span></div>`;
}

function inject(html, b) {
  return html.replace(/<footer\b[\s\S]*?<\/footer>/g, (f) => {
    if (f.includes('data-ai-summary')) return f;
    const i = f.lastIndexOf('<div style="margin-top:');
    if (i < 0) return f.replace(/<\/footer>$/, b + '</footer>');
    return f.slice(0, i) + b + '\n' + f.slice(i);
  });
}

function walk(d, out) {
  for (const e of fs.readdirSync(d, { withFileTypes: true })) {
    if (e.name === 'node_modules' || e.name.startsWith('.')) continue;
    const p = path.join(d, e.name);
    if (e.isDirectory()) walk(p, out); else if (e.name.endsWith('.html')) out.push(p);
  }
  return out;
}

const [site, ...dirs] = process.argv.slice(2);
const s = SITES[site];
if (!s || !dirs.length) { console.error('usage: node ai-summary.js <lexops|missioncontrol> <dir>...'); process.exit(1); }
const b = block(s);
let n = 0;
for (const d of dirs) for (const f of walk(d, [])) {
  const h = fs.readFileSync(f, 'utf8'); const o = inject(h, b);
  if (o !== h) { fs.writeFileSync(f, o); n++; }
}
console.log(`ai-summary: added strip to ${n} file(s)`);
