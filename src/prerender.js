const fs = require('fs'); const path = require('path');
const { JSDOM, VirtualConsole } = require('jsdom');
const OUT = process.argv[2];
const runtime = fs.readFileSync(path.join(OUT, 'mc.js'), 'utf8');
for (const f of fs.readdirSync(OUT).filter((x) => x.endsWith('.html'))) {
  const file = path.join(OUT, f);
  const html = fs.readFileSync(file, 'utf8');
  const vc = new VirtualConsole(); vc.on('jsdomError', (e) => { if (!/Not implemented/.test(e.message)) console.error(f, e.message); });
  const dom = new JSDOM(html.split('<script src="/mc.js"></script>').join('<script>' + runtime + '</script>'), { runScripts: 'dangerously', virtualConsole: vc });
  const app = dom.window.document.getElementById('mc-app');
  const rendered = app ? app.innerHTML : '';
  if (rendered.length < 500) { console.error('Render failed for ' + f); process.exit(1); }
  fs.writeFileSync(file, html.replace('<div id="mc-app"></div>', '<div id="mc-app">' + rendered + '</div>'));
  console.log('prerendered', f, rendered.length);
}
