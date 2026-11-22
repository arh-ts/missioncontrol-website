#!/usr/bin/env python3
"""Mission Control site extras.

Run from anywhere after the main pages are built (build.py + prerender.js), or on its own to
publish newsroom changes. It is idempotent: running it twice gives the same output.

It does five things:
  1. SEO/AEO layer on the main pages: titles, Open Graph, Twitter cards, JSON-LD, self-hosted fonts.
  2. Newsroom: /news index, one page per article, header art, RSS feed, Markdown copies.
  3. Legal and utility pages: /privacy, /terms, /404, /.well-known/security.txt.
  4. Crawl files: sitemap.xml, robots.txt, llms.txt, llms-full.txt.
  5. Default social image (media/og.jpg) and per-article social images (news/img/*.png) when skia is available.

Articles live in src/news/articles.json (metadata) and src/news/<slug>.html (body).
"""
import datetime as _dt
import html
import json
import os
import random
import re
import sys

ROOT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SRC = os.path.join(ROOT, 'src')
SITE = 'https://missioncntrl.io'
NAME = 'Mission Control'
EMAIL = 'hello@missioncntrl.io'
TODAY = _dt.date.today().isoformat()
LOGO = SITE + '/media/mission-control-logo.svg'

MAIN = {
    'index.html': ('/', 'Mission Control | See how work really moves through your organisation'),
    'platform.html': ('/platform', 'Platform: a live map of how work moves | Mission Control'),
    'how-we-work.html': ('/how-we-work', 'How we work: deployed and run with you | Mission Control'),
    'industries.html': ('/industries', 'Industries: built for services organisations | Mission Control'),
    'security.html': ('/security', 'Security and privacy | Mission Control'),
    'company.html': ('/company', 'About Mission Control | The team behind it'),
    'briefing.html': ('/briefing', 'Book a briefing | Mission Control'),
}
CRUMB = {'/platform': 'Platform', '/how-we-work': 'How we work', '/industries': 'Industries', '/security': 'Security and privacy', '/company': 'Company', '/briefing': 'Book a briefing'}


def rd(p):
    with open(p, encoding='utf-8') as f:
        return f.read()


def wr(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(s)


def esc(s):
    return html.escape(str(s), quote=True)


def text_of(fragment):
    t = re.sub(r'<(script|style|template)[^>]*>.*?</\1>', ' ', fragment, flags=re.S)
    t = re.sub(r'<br\s*/?>|</(p|li|h[1-6]|div|tr|section|figure)>', '\n', t)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = html.unescape(t)
    lines = [re.sub(r'[ \t]+', ' ', l).strip() for l in t.split('\n')]
    out, prev = [], None
    for l in lines:
        if l and l != prev:
            out.append(l)
        prev = l
    return '\n'.join(out)


def nice_date(iso):
    d = _dt.date.fromisoformat(iso)
    return f'{d.day} {d.strftime("%B %Y")}'


# ---------------------------------------------------------------- fonts
FONT_FILES = [('Inter', w, f'/fonts/inter-latin-{w}-normal.woff2') for w in (400, 500, 600)] + \
             [('Inter Tight', w, f'/fonts/inter-tight-latin-{w}-normal.woff2') for w in (400, 500, 600)]
FONT_BLOCK = ('<link rel="preload" href="/fonts/inter-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>\n'
              '<link rel="preload" href="/fonts/inter-tight-latin-500-normal.woff2" as="font" type="font/woff2" crossorigin>\n'
              '<style>' + ''.join(f"@font-face{{font-family:'{f}';font-style:normal;font-weight:{w};font-display:swap;src:url({u}) format('woff2')}}" for f, w, u in FONT_FILES) + '</style>')
GOOGLE_RE = re.compile(r'<link rel="preconnect" href="https://fonts\.googleapis\.com">\s*<link rel="preconnect" href="https://fonts\.gstatic\.com" crossorigin="">\s*<link href="https://fonts\.googleapis\.com/css2[^"]*" rel="stylesheet">')

# ---------------------------------------------------------------- JSON-LD
ORG = {
    '@type': 'Organization', '@id': SITE + '/#org', 'name': NAME, 'url': SITE, 'logo': LOGO, 'email': EMAIL,
    'description': 'Operational intelligence for services organisations: a live map of how work moves between people and teams, where it stalls, and what is worth automating.',
    'areaServed': ['AU', 'US', 'GB'],
    'founder': [{'@type': 'Person', 'name': 'Abdul'}, {'@type': 'Person', 'name': 'Amresh'}],
    'contactPoint': {'@type': 'ContactPoint', 'contactType': 'sales', 'email': EMAIL, 'url': SITE + '/briefing'},
}
WEBSITE = {'@type': 'WebSite', '@id': SITE + '/#website', 'url': SITE, 'name': NAME, 'publisher': {'@id': SITE + '/#org'}, 'inLanguage': 'en-AU'}
SERVICE = {
    '@type': 'Service', 'name': 'Mission Control', 'provider': {'@id': SITE + '/#org'},
    'serviceType': 'Operational intelligence and process automation',
    'description': 'A deployed platform and team that maps how work moves through a services organisation, shows where it slows down, and sizes and builds the automations worth doing.',
    'areaServed': ['AU', 'US', 'GB'], 'audience': {'@type': 'BusinessAudience', 'audienceType': 'Services organisations'},
}


def ld(graph):
    return '<script type="application/ld+json">' + json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False).replace('</', '<\\/') + '</script>'


def crumbs(items):
    return {'@type': 'BreadcrumbList', 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': SITE + u} for i, (n, u) in enumerate(items)]}


def faq_ld(pairs):
    return {'@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in pairs]}


def social(title, desc, url, image, kind='website', extra=''):
    return '\n'.join([
        f'<meta property="og:site_name" content="{NAME}">', '<meta property="og:locale" content="en_AU">',
        f'<meta property="og:type" content="{kind}">', f'<meta property="og:title" content="{esc(title)}">',
        f'<meta property="og:description" content="{esc(desc)}">', f'<meta property="og:url" content="{SITE}{url}">',
        f'<meta property="og:image" content="{image}">', '<meta property="og:image:width" content="1200">', '<meta property="og:image:height" content="630">',
        '<meta name="twitter:card" content="summary_large_image">', f'<meta name="twitter:title" content="{esc(title)}">',
        f'<meta name="twitter:description" content="{esc(desc)}">', f'<meta name="twitter:image" content="{image}">',
        '<meta name="robots" content="index,follow,max-image-preview:large">',
        f'<link rel="alternate" type="application/rss+xml" title="{NAME} Newsroom" href="{SITE}/news/feed.xml">',
    ]) + extra


# ---------------------------------------------------------------- 1. main pages
def process_main():
    for fn, (url, title) in MAIN.items():
        p = os.path.join(ROOT, fn)
        if not os.path.exists(p):
            continue
        s = rd(p)
        s = s.replace('<html lang="en">', '<html lang="en-AU">')
        s = GOOGLE_RE.sub(FONT_BLOCK, s)
        s = re.sub(r'<title>.*?</title>', f'<title>{esc(title)}</title>', s, count=1)
        s = re.sub(r'\n?<meta property="og:[^"]*" content="[^"]*">', '', s)
        s = re.sub(r'\n?<!--mc-seo-->.*?<!--/mc-seo-->', '', s, flags=re.S)
        desc = html.unescape(re.search(r'<meta name="description" content="([^"]*)"', s).group(1))
        graph = [ORG, WEBSITE, {'@type': 'WebPage', '@id': SITE + url + '#page', 'url': SITE + url, 'name': title, 'description': desc, 'isPartOf': {'@id': SITE + '/#website'}, 'inLanguage': 'en-AU'}]
        if url != '/':
            graph.append(crumbs([('Home', '/'), (CRUMB[url], url)]))
        if url in ('/', '/platform', '/how-we-work'):
            graph.append(SERVICE)
        m = re.search(r'var faqItems = (\[.*?\]);', s, flags=re.S)
        if m:
            try:
                graph.append(faq_ld([(q, a) for q, a in json.loads(m.group(1))]))
            except Exception:
                pass
        block = '<!--mc-seo-->\n' + social(title, desc, url, SITE + '/media/og.jpg') + '\n' + ld(graph) + '\n<!--/mc-seo-->'
        s = s.replace('<link rel="icon"', block + '\n<link rel="icon"', 1)
        wr(p, s)
        print('seo', fn)


# ---------------------------------------------------------------- shared chrome for static pages
def chrome():
    s = rd(os.path.join(ROOT, 'index.html'))
    app = s[s.index('<div id="mc-app">'):]
    header = re.search(r'<header.*?</header>', app, flags=re.S).group(0)
    footer = re.search(r'<footer.*?</footer>', app, flags=re.S).group(0).replace(' id="company"', '')
    style = re.search(r'<style>\s*body\{.*?</style>', s, flags=re.S).group(0)
    loader = re.search(r'<div id="mv-loader".*?</div>\s*</div>', s, flags=re.S)
    return header, footer, style


def header_active(header, href):
    return header.replace(f'<a class="nl" href="{href}">', f'<a class="nl" href="{href}" aria-current="page" style="color:#0A0B0D">', 1)


PAGE_CSS = """
.wrap{max-width:1200px;margin:0 auto;padding:0 24px}
.crumb{font-size:14px;color:#5B616B;display:flex;gap:8px;flex-wrap:wrap}.crumb a:hover{color:#0A0B0D}
.eyb{margin:0;font-size:14px;font-weight:500;color:#157A36}
.h1{margin:20px 0 0;font-weight:500;font-size:clamp(34px,4.2vw,54px);line-height:1.06;letter-spacing:-0.033em;max-width:900px}
.lead{margin:20px 0 0;font-size:19px;line-height:1.55;color:#5B616B;max-width:720px}
.meta{margin-top:24px;display:flex;flex-wrap:wrap;gap:6px 18px;font-size:14px;color:#8A9099}
.art{max-width:700px;margin:0 auto;padding:56px 24px 0;font-size:18px;line-height:1.72;color:#24272C}
.art p{margin:0 0 22px}
.art h2{font-family:'Inter Tight',system-ui,sans-serif;font-weight:500;font-size:28px;line-height:1.2;letter-spacing:-0.02em;color:#0A0B0D;margin:52px 0 16px}
.art h3{font-family:'Inter Tight',system-ui,sans-serif;font-weight:500;font-size:20px;line-height:1.3;color:#0A0B0D;margin:32px 0 10px}
.art ul,.art ol{margin:0 0 22px;padding-left:22px}.art li{margin:0 0 10px;padding-left:4px}
.art a{color:#0A0B0D;text-decoration:underline;text-decoration-color:#85EC68;text-decoration-thickness:2px;text-underline-offset:3px;transition:text-decoration-color .2s ease}
.art a:hover{text-decoration-color:#0A0B0D}
.art strong{font-weight:600;color:#0A0B0D}
.tldr{border:1px solid #EEEFF1;background:#FAFAFB;border-radius:14px;padding:24px 28px 8px;margin:0 0 40px;font-size:16px;line-height:1.6}
.tldr h2{margin:0 0 12px !important;font-size:15px !important;font-family:Inter,system-ui,sans-serif !important;font-weight:600 !important;letter-spacing:0 !important;color:#157A36 !important}
.callout{margin:28px 0;padding:22px 26px;border-left:3px solid #85EC68;background:#F7FBF5;border-radius:0 12px 12px 0;font-size:16px;line-height:1.6}
.callout p{margin:0 0 10px}.callout p:last-child{margin:0}
.faq{margin-top:56px;padding-top:8px;border-top:1px solid #EEEFF1}
.sources{margin-top:48px;padding-top:8px;border-top:1px solid #EEEFF1;font-size:15px;line-height:1.55;color:#5B616B}
.sources h2{font-size:20px !important}.sources li{margin-bottom:8px}
.hero-art{margin-top:48px;border-radius:16px;overflow:hidden;border:1px solid #EEEFF1;background:#FAFAFB}
.hero-art img{display:block;width:100%;height:auto;aspect-ratio:2/1;object-fit:cover}
.chip{display:inline-flex;align-items:center;height:34px;padding:0 14px;border:1px solid #E7E8EB;border-radius:999px;font-size:14px;font-weight:500;color:#5B616B;background:#FFFFFF;cursor:pointer;font-family:inherit;transition:border-color .2s ease,color .2s ease,background .2s ease}
.chip:hover{color:#0A0B0D;border-color:#9AA0A8}.chip[aria-pressed="true"]{background:#0A0B0D;border-color:#0A0B0D;color:#FFFFFF}
.chip:focus-visible,.card:focus-visible{outline:2px solid #0A0B0D;outline-offset:2px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(340px,100%),1fr));gap:28px}
.card{display:flex;flex-direction:column;border:1px solid #EEEFF1;border-radius:14px;overflow:hidden;background:#FFFFFF;transition:border-color .2s ease,box-shadow .25s ease,transform .25s cubic-bezier(0.32,0.72,0,1)}
.card:hover{border-color:#DADCE0;box-shadow:0 24px 48px -32px rgba(10,11,13,0.28);transform:translateY(-2px)}
.card img{display:block;width:100%;height:auto;aspect-ratio:16/9;object-fit:cover;background:#FAFAFB;border-bottom:1px solid #EEEFF1}
.card .ci{padding:22px 22px 24px;display:flex;flex-direction:column;gap:10px;flex:1}
.card .ct{font-family:'Inter Tight',system-ui,sans-serif;font-size:21px;line-height:1.25;font-weight:500;letter-spacing:-0.015em;color:#0A0B0D}
.card .cd{font-size:15px;line-height:1.55;color:#5B616B}
.card .cm{margin-top:auto;padding-top:8px;font-size:13px;color:#8A9099;display:flex;gap:14px}
.feat{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,1fr);border:1px solid #EEEFF1;border-radius:16px;overflow:hidden;transition:border-color .2s ease,box-shadow .25s ease}
.feat:hover{border-color:#DADCE0;box-shadow:0 30px 60px -40px rgba(10,11,13,0.3)}
.feat img{display:block;width:100%;height:100%;object-fit:cover;background:#FAFAFB}
.feat .fi{padding:40px;display:flex;flex-direction:column;justify-content:center;gap:14px}
.feat .ft{font-family:'Inter Tight',system-ui,sans-serif;font-size:clamp(26px,2.6vw,34px);line-height:1.15;font-weight:500;letter-spacing:-0.025em}
@media (max-width:820px){.feat{grid-template-columns:1fr}.feat .fi{padding:28px}}
.legal{max-width:760px;margin:0 auto;padding:48px 24px 0;font-size:16px;line-height:1.7;color:#24272C}
.legal h2{font-family:'Inter Tight',system-ui,sans-serif;font-weight:500;font-size:24px;letter-spacing:-0.015em;color:#0A0B0D;margin:44px 0 12px}
.legal h3{font-size:17px;font-weight:600;color:#0A0B0D;margin:24px 0 8px}
.legal p{margin:0 0 16px}.legal ul{margin:0 0 16px;padding-left:22px}.legal li{margin-bottom:8px}
.legal a{text-decoration:underline;text-decoration-color:#85EC68;text-decoration-thickness:2px;text-underline-offset:3px}
.cta{margin:120px auto 96px;max-width:1152px;border-radius:16px;background:#0A0B0D;color:#FFFFFF;padding:56px 48px;display:flex;flex-wrap:wrap;gap:24px 48px;align-items:center;justify-content:space-between;position:relative;overflow:hidden}
.cta h2{margin:0;font-family:'Inter Tight',system-ui,sans-serif;font-weight:500;font-size:clamp(26px,2.8vw,38px);line-height:1.1;letter-spacing:-0.025em;max-width:560px}
.cta p{margin:12px 0 0;color:#C9CED4;font-size:16px;line-height:1.6;max-width:560px}
@media (max-width:640px){.cta{margin:80px 24px 64px;padding:40px 28px}}
"""


def page(title, desc, url, body, header, footer, style, kind='website', image=None, graph=None, extra_head=''):
    image = image or SITE + '/media/og.jpg'
    g = [ORG, WEBSITE] + (graph or [])
    return f"""<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{SITE}{url}">
{social(title, desc, url, image, kind)}
{ld(g)}
<link rel="icon" type="image/svg+xml" href="/media/mark.svg">
<meta name="theme-color" content="#FFFFFF">
{FONT_BLOCK}
{style}
<style>{PAGE_CSS}</style>
<link rel="stylesheet" href="/mc-motion.css">{extra_head}
</head>
<body style="margin:0;font-family:'Inter',system-ui,sans-serif;color:#0A0B0D;-webkit-font-smoothing:antialiased">
<div id="mc-app"><div>
{header}
<main>
{body}
</main>
{footer}
</div></div>
<script src="/mc-motion.js" defer></script>
</body>
</html>
"""


def cta_block():
    return f"""<section class="cta" aria-label="Book a briefing"><div><h2>See how work really moves through your organisation.</h2><p>A 30-minute briefing with our team. We walk through a live map and tell you plainly whether Mission Control is a fit.</p></div>
<a href="/briefing" class="bw" style="display:inline-flex;align-items:center;gap:8px;min-height:46px;padding:0 20px;border-radius:8px;background:#FFFFFF;color:#0A0B0D;font-size:15px;font-weight:500">Book a briefing <span class="ar" aria-hidden="true">→</span></a></section>"""


# ---------------------------------------------------------------- header art
INK, LINE, SOFT, LIME, GREEN, ORANGE, ORANGE_T = '#0A0B0D', '#DADCE0', '#FAFAFB', '#85EC68', '#26A44C', '#E8590C', '#F2A16B'


def art_svg(slug, motif, W=1600, H=900):
    rnd = random.Random(sum(ord(c) * (i + 1) for i, c in enumerate(slug)))
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
           f'<rect width="{W}" height="{H}" fill="{SOFT}"/>',
           '<defs><pattern id="d" width="32" height="32" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.6" fill="#D5D8DC"/></pattern>'
           f'<radialGradient id="g" cx="0.5" cy="0.5" r="0.6"><stop offset="0" stop-color="{LIME}" stop-opacity="0.18"/><stop offset="1" stop-color="{LIME}" stop-opacity="0"/></radialGradient></defs>',
           f'<rect width="{W}" height="{H}" fill="url(#d)"/>', f'<rect width="{W}" height="{H}" fill="url(#g)"/>']

    def node(x, y, r=14, fill='#FFFFFF', stroke=INK, sw=2):
        out.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

    def path(d, color=INK, w=2, dash=None, op=1):
        da = f' stroke-dasharray="{dash}"' if dash else ''
        out.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" opacity="{op}"{da}/>')

    def card(x, y, w, h, label_w=None, accent=None):
        out.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{w}" height="{h}" rx="12" fill="#FFFFFF" stroke="{LINE}" stroke-width="2"/>')
        lw = label_w or w * 0.55
        out.append(f'<rect x="{x+18:.0f}" y="{y+18:.0f}" width="{lw:.0f}" height="10" rx="5" fill="#C9CDD2"/>')
        out.append(f'<rect x="{x+18:.0f}" y="{y+38:.0f}" width="{lw*0.6:.0f}" height="8" rx="4" fill="#E2E4E7"/>')
        if accent:
            out.append(f'<circle cx="{x+w-22:.0f}" cy="{y+23:.0f}" r="6" fill="{accent}"/>')

    if motif == 'handoff':
        xs = [220, 520, 820, 1120, 1380]
        ys = [470, 360, 520, 380, 460]
        for i in range(len(xs) - 1):
            x1, y1, x2, y2 = xs[i], ys[i], xs[i + 1], ys[i + 1]
            mx = (x1 + x2) / 2
            slow = i in (1, 3)
            path(f'M{x1} {y1} C{mx} {y1} {mx} {y2} {x2} {y2}', ORANGE if slow else INK, 3 if slow else 2.5, '2 12' if slow else None)
            if slow:
                out.append(f'<rect x="{mx-46:.0f}" y="{(y1+y2)/2-20:.0f}" width="92" height="40" rx="20" fill="#FFFFFF" stroke="{ORANGE_T}" stroke-width="2"/>')
                out.append(f'<rect x="{mx-26:.0f}" y="{(y1+y2)/2-4:.0f}" width="52" height="8" rx="4" fill="{ORANGE_T}"/>')
        for x, y in zip(xs, ys):
            out.append(f'<circle cx="{x}" cy="{y}" r="46" fill="#FFFFFF" stroke="{LINE}" stroke-width="2"/>')
            node(x, y, 16, INK, INK)
        path(f'M{xs[0]} {ys[0]+120} L{xs[-1]} {ys[-1]+120}', LIME, 4, None, 0.9)
    elif motif == 'queue':
        cx, cy = 980, 450
        for i in range(9):
            card(170 + i * 70, 300 + (i % 2) * 18 + i * 8, 150, 92, 70, ORANGE_T if i > 5 else None)
        out.append(f'<circle cx="{cx}" cy="{cy}" r="70" fill="#FFFFFF" stroke="{INK}" stroke-width="3"/>')
        node(cx, cy, 20, INK, INK)
        path(f'M{cx+70} {cy} C{cx+200} {cy} {cx+220} {cy-120} {cx+380} {cy-120}', LIME, 5)
        path(f'M{cx+70} {cy} C{cx+200} {cy} {cx+220} {cy+120} {cx+380} {cy+120}', INK, 2.5)
        node(cx + 380, cy - 120, 12, LIME, GREEN)
        node(cx + 380, cy + 120, 12)
    elif motif == 'bottleneck':
        cx, cy = 980, 450
        for i in range(9):
            y0 = 140 + i * 78
            path(f'M140 {y0} C520 {y0} 620 {cy} {cx-40} {cy}', ORANGE if i in (3, 4, 5) else INK, 2.2, None, 0.55 if i not in (3, 4, 5) else 0.9)
            node(140, y0, 9)
        out.append(f'<rect x="{cx-40}" y="{cy-34}" width="80" height="68" rx="16" fill="#FFFFFF" stroke="{ORANGE}" stroke-width="3"/>')
        out.append(f'<rect x="{cx-18}" y="{cy-4}" width="36" height="8" rx="4" fill="{ORANGE_T}"/>')
        path(f'M{cx+40} {cy} L1460 {cy}', LIME, 6)
        node(1460, cy, 16, LIME, GREEN, 3)
    elif motif == 'case':
        base = 700
        vals = [0.22, 0.3, 0.27, 0.42, 0.5, 0.48, 0.63, 0.72, 0.8]
        for i, v in enumerate(vals):
            x = 220 + i * 130
            h = v * 460
            out.append(f'<rect x="{x}" y="{base-h:.0f}" width="72" height="{h:.0f}" rx="10" fill="{"#FFFFFF" if i < 6 else "#EAF8E4"}" stroke="{LINE if i < 6 else GREEN}" stroke-width="2"/>')
        pts = ' '.join(f'{256+i*130},{base-v*460-40:.0f}' for i, v in enumerate(vals))
        out.append(f'<polyline points="{pts}" fill="none" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>')
        path(f'M180 {base} L1420 {base}', INK, 2)
        card(1180, 150, 260, 110, 150, LIME)
    elif motif == 'privacy':
        out.append(f'<rect x="300" y="170" width="1000" height="560" rx="36" fill="none" stroke="{INK}" stroke-width="2.5" stroke-dasharray="4 14"/>')
        pts = []
        for r in range(4):
            for c in range(7):
                x, y = 400 + c * 133, 260 + r * 125
                pts.append((x, y))
        for (x, y) in pts:
            out.append(f'<rect x="{x-26}" y="{y-26}" width="52" height="52" rx="14" fill="#FFFFFF" stroke="{LINE}" stroke-width="2"/>')
        route = [pts[0], pts[8], pts[9], pts[17], pts[18], pts[26], pts[27]]
        path('M' + ' L'.join(f'{x} {y}' for x, y in route), LIME, 6)
        for x, y in route:
            node(x, y, 9, INK, INK)
    else:
        nodes = [(rnd.randint(200, 1400), rnd.randint(160, 740)) for _ in range(12)]
        for i in range(len(nodes) - 1):
            (x1, y1), (x2, y2) = nodes[i], nodes[i + 1]
            path(f'M{x1} {y1} Q{(x1+x2)/2} {min(y1,y2)-80} {x2} {y2}', LIME if i % 4 == 0 else INK, 3 if i % 4 == 0 else 2, None, 0.8)
        for x, y in nodes:
            node(x, y, 12)
    out.append('</svg>')
    return ''.join(out)


def svg_to_png(svg, out_png, size=(1200, 630)):
    try:
        import skia
        W, H = 1600, 900
        dom = skia.SVGDOM.MakeFromStream(skia.MemoryStream(svg.encode()))
        surf = skia.Surface(size[0], size[1])
        c = surf.getCanvas()
        scale = max(size[0] / W, size[1] / H)
        c.translate((size[0] - W * scale) / 2, (size[1] - H * scale) / 2)
        c.scale(scale, scale)
        dom.setContainerSize(skia.Size(W, H))
        dom.render(c)
        surf.makeImageSnapshot().save(out_png, skia.kPNG)
        return True
    except Exception as e:
        print('png skipped:', e)
        return False


def og_default():
    out = os.path.join(ROOT, 'media', 'og.jpg')
    src = os.path.join(ROOT, 'media', 'overhead.jpg')
    if os.path.exists(out) or not os.path.exists(src):
        return
    try:
        import skia
        img = skia.Image.open(src)
        W, H = 1200, 630
        surf = skia.Surface(W, H)
        c = surf.getCanvas()
        s = max(W / img.width(), H / img.height())
        c.drawImageRect(img, skia.Rect.MakeXYWH((W - img.width() * s) / 2, (H - img.height() * s) / 2, img.width() * s, img.height() * s), skia.SamplingOptions(skia.FilterMode.kLinear))
        surf.makeImageSnapshot().save(out, skia.kJPEG, 86)
        print('og.jpg written')
    except Exception as e:
        import shutil
        shutil.copyfile(src, out)
        print('og.jpg copied (no skia):', e)


# ---------------------------------------------------------------- 2. newsroom
def load_articles():
    A = json.loads(rd(os.path.join(SRC, 'news', 'articles.json')))
    for a in A:
        a['body'] = rd(os.path.join(SRC, 'news', a['slug'] + '.html'))
        words = len(text_of(a['body']).split())
        a['mins'] = max(3, round(words / 230))
        a['url'] = '/news/' + a['slug']
        a['img'] = '/news/img/' + a['slug'] + '.svg'
        a.setdefault('motif', 'network')
        a.setdefault('updated', a['date'])
    A.sort(key=lambda a: (a['date'], a.get('order', 0)), reverse=True)
    return A


def external_links(body):
    def fix(m):
        tag = m.group(0)
        if 'href="http' in tag and 'missioncntrl.io' not in tag and 'target=' not in tag:
            tag = tag[:-1] + ' target="_blank" rel="noopener">'
        return tag
    return re.sub(r'<a [^>]*>', fix, body)


def faq_pairs(body):
    m = re.search(r'<section class="faq">(.*?)</section>', body, flags=re.S)
    if not m:
        return []
    return [(text_of(q), text_of(a)) for q, a in re.findall(r'<h3>(.*?)</h3>\s*<p>(.*?)</p>', m.group(1), flags=re.S)]


def card_html(a):
    return f"""<a class="card mv-card" href="{a['url']}" data-cat="{esc(a['cat'])}"><img src="{a['img']}" alt="" loading="lazy" width="1600" height="900"><div class="ci"><span class="eyb">{esc(a['cat'])}</span><span class="ct">{esc(a['title'])}</span><span class="cd">{esc(a['dek'])}</span><span class="cm"><time datetime="{a['date']}">{nice_date(a['date'])}</time><span>{a['mins']} min read</span></span></div></a>"""


def build_news(header, footer, style):
    A = load_articles()
    hdr = header_active(header, '/news')
    os.makedirs(os.path.join(ROOT, 'news', 'img'), exist_ok=True)
    for a in A:
        svg = art_svg(a['slug'], a['motif'])
        wr(os.path.join(ROOT, 'news', 'img', a['slug'] + '.svg'), svg)
        png = os.path.join(ROOT, 'news', 'img', a['slug'] + '.png')
        a['og'] = SITE + '/news/img/' + a['slug'] + '.png' if (os.path.exists(png) or svg_to_png(svg, png)) else SITE + '/media/og.jpg'

    # index
    cats = []
    for a in A:
        if a['cat'] not in cats:
            cats.append(a['cat'])
    chips = '<button type="button" class="chip" aria-pressed="true" data-filter="All">All</button>' + ''.join(f'<button type="button" class="chip" aria-pressed="false" data-filter="{esc(c)}">{esc(c)}</button>' for c in cats)
    f0 = A[0]
    feat = f"""<a class="feat mv-card" href="{f0['url']}" data-cat="{esc(f0['cat'])}"><img src="{f0['img']}" alt="" width="1600" height="900"><div class="fi"><span class="eyb">Latest</span><span class="ft">{esc(f0['title'])}</span><span style="font-size:16px;line-height:1.6;color:#5B616B">{esc(f0['dek'])}</span><span style="font-size:13px;color:#8A9099;display:flex;gap:14px"><time datetime="{f0['date']}">{nice_date(f0['date'])}</time><span>{f0['mins']} min read</span></span></div></a>"""
    body = f"""<section><div class="wrap" style="padding-top:88px">
<p class="eyb">Newsroom</p>
<h1 class="d h1">Thinking on how work really moves.</h1>
<p class="lead">Research and opinion on operations, automation and the hand-offs that slow services organisations down. Every piece is sourced, so you can check our working.</p>
</div></section>
<section><div class="wrap" style="padding-top:48px">{feat}</div></section>
<section aria-label="All articles"><div class="wrap" style="padding-top:64px">
<div role="group" aria-label="Filter by topic" style="display:flex;flex-wrap:wrap;gap:8px;margin-bottom:28px">{chips}</div>
<div class="grid" id="news-grid">{''.join(card_html(a) for a in A[1:])}</div>
<p id="news-empty" hidden style="color:#5B616B">No articles in this topic yet.</p>
</div></section>
{cta_block()}
<script>(function(){{var b=document.querySelectorAll('[data-filter]'),c=document.querySelectorAll('#news-grid .card'),e=document.getElementById('news-empty');b.forEach(function(x){{x.addEventListener('click',function(){{var f=x.getAttribute('data-filter'),n=0;b.forEach(function(y){{y.setAttribute('aria-pressed',y===x?'true':'false')}});c.forEach(function(k){{var s=f==='All'||k.getAttribute('data-cat')===f;k.hidden=!s;if(s)n++}});e.hidden=n>0}})}})}})();</script>"""
    graph = [{'@type': 'CollectionPage', '@id': SITE + '/news#page', 'url': SITE + '/news', 'name': 'Mission Control Newsroom', 'isPartOf': {'@id': SITE + '/#website'}},
             crumbs([('Home', '/'), ('Newsroom', '/news')]),
             {'@type': 'ItemList', 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'url': SITE + a['url'], 'name': a['title']} for i, a in enumerate(A)]}]
    wr(os.path.join(ROOT, 'news', 'index.html'), page('Newsroom: research on how work moves | Mission Control', 'Research and opinion on operations, automation and the hand-offs that slow services organisations down. Sourced, practical and written by the Mission Control team.', '/news', body, hdr, footer, style, graph=graph))
    print('news index', len(A))

    # articles
    for i, a in enumerate(A):
        related = [x for x in A if x['slug'] != a['slug'] and x['cat'] == a['cat']] + [x for x in A if x['slug'] != a['slug'] and x['cat'] != a['cat']]
        related = related[:3]
        body_html = external_links(a['body'])
        body = f"""<section><div class="wrap" style="padding-top:72px">
<nav class="crumb" aria-label="Breadcrumb"><a href="/news">Newsroom</a><span aria-hidden="true">/</span><span>{esc(a['cat'])}</span></nav>
<h1 class="d h1">{esc(a['title'])}</h1>
<p class="lead">{esc(a['dek'])}</p>
<div class="meta"><span>By the Mission Control team</span><time datetime="{a['date']}">{nice_date(a['date'])}</time><span>{a['mins']} min read</span></div>
<div class="hero-art"><img src="{a['img']}" alt="" width="1600" height="900"></div>
</div></section>
<article class="art">
{body_html}
<p style="margin-top:40px;font-size:14px;color:#8A9099">Published {nice_date(a['date'])}{'' if a['updated'] == a['date'] else ', updated ' + nice_date(a['updated'])}. This article is general information, not legal, financial or professional advice.</p>
</article>
<section aria-label="Related reading"><div class="wrap" style="padding-top:96px"><h2 class="d" style="margin:0 0 28px;font-weight:500;font-size:28px;letter-spacing:-0.02em">Keep reading</h2><div class="grid">{''.join(card_html(r) for r in related)}</div></div></section>
{cta_block()}"""
        graph = [{'@type': 'Article', '@id': SITE + a['url'] + '#article', 'headline': a['title'], 'description': a['description'], 'image': [a['og']],
                  'datePublished': a['date'], 'dateModified': a['updated'], 'inLanguage': 'en-AU', 'articleSection': a['cat'],
                  'author': {'@id': SITE + '/#org'}, 'publisher': {'@id': SITE + '/#org'}, 'mainEntityOfPage': SITE + a['url'],
                  'wordCount': len(text_of(a['body']).split())},
                 crumbs([('Home', '/'), ('Newsroom', '/news'), (a['title'], a['url'])])]
        fp = faq_pairs(a['body'])
        if fp:
            graph.append(faq_ld(fp))
        extra = f'\n<meta property="article:published_time" content="{a["date"]}">\n<meta property="article:modified_time" content="{a["updated"]}">\n<meta property="article:section" content="{esc(a["cat"])}">'
        wr(os.path.join(ROOT, 'news', a['slug'] + '.html'), page(f"{a['title']} | Mission Control", a['description'], a['url'], body, hdr, footer, style, kind='article', image=a['og'], graph=graph, extra_head=extra))
        wr(os.path.join(ROOT, 'news', a['slug'] + '.md'), to_markdown(a))
    # RSS
    items = ''.join(f"""<item><title>{esc(a['title'])}</title><link>{SITE}{a['url']}</link><guid isPermaLink="true">{SITE}{a['url']}</guid><pubDate>{_dt.datetime.fromisoformat(a['date']).strftime('%a, %d %b %Y 09:00:00 +1100')}</pubDate><category>{esc(a['cat'])}</category><description>{esc(a['description'])}</description></item>""" for a in A)
    wr(os.path.join(ROOT, 'news', 'feed.xml'), f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel><title>Mission Control Newsroom</title><link>{SITE}/news</link><description>Research and opinion on how work moves through services organisations.</description><language>en-au</language><atom:link href="{SITE}/news/feed.xml" rel="self" type="application/rss+xml"/>{items}</channel></rss>
""")
    return A


def to_markdown(a):
    b = a['body']
    b = re.sub(r'<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>', lambda m: f'[{text_of(m.group(2))}]({m.group(1) if m.group(1).startswith("http") else SITE + m.group(1)})', b, flags=re.S)
    b = re.sub(r'<h2>(.*?)</h2>', r'\n## \1\n', b)
    b = re.sub(r'<h3>(.*?)</h3>', r'\n### \1\n', b)
    b = re.sub(r'<li>(.*?)</li>', r'- \1\n', b, flags=re.S)
    b = re.sub(r'</?(strong|b)>', '**', b)
    b = re.sub(r'</?em>', '_', b)
    b = re.sub(r'</p>|</figure>', '\n\n', b)
    b = re.sub(r'<[^>]+>', '', b)
    b = html.unescape(b)
    b = re.sub(r'\n{3,}', '\n\n', b).strip()
    return f"# {a['title']}\n\n> {a['dek']}\n\nPublished {nice_date(a['date'])} by the Mission Control team. Canonical: {SITE}{a['url']}\n\n{b}\n"


# ---------------------------------------------------------------- 3. legal and utility pages
PRIVACY = """
<h2>About this notice</h2>
<p>This notice explains how Mission Control ("we", "us") handles personal information when you visit missioncntrl.io, contact us or book a briefing. It also explains, at a high level, how personal information is handled when we deploy Mission Control for a client organisation. We aim to handle personal information in line with the Australian Privacy Principles in the <em>Privacy Act 1988</em> (Cth). Where they apply, we also follow the UK GDPR and the privacy laws of US states such as California.</p>

<h2>What we collect through this website</h2>
<h3>Information you give us</h3>
<p>When you book a briefing or email us we collect what you choose to provide: your name, work email, organisation, role, organisation size, industry and any message you write.</p>
<h3>Information collected automatically</h3>
<p>Like most websites, our hosting provider records standard server logs when pages are requested, including IP address, browser type, the page requested and the time. We use these logs to keep the site secure and working.</p>
<h3>Cookies and tracking</h3>
<p>This website does not use advertising cookies, analytics cookies or third-party tracking pixels. Fonts, images and videos are served from our own domain, so loading a page does not send your details to font or video providers. We store one small value in your browser's session storage so the opening animation plays only once per visit. It contains no personal information and is cleared when you close the tab.</p>

<h2>How we use it</h2>
<ul>
<li>To respond to your enquiry and arrange and prepare for a briefing.</li>
<li>To follow up about Mission Control if you have asked us to, or where it is reasonable to expect we will. You can ask us to stop at any time.</li>
<li>To operate, secure and improve this website.</li>
<li>To meet legal obligations.</li>
</ul>
<p>For visitors in the UK, our lawful bases are our legitimate interests in responding to business enquiries and running our website, and taking steps at your request before entering into a contract.</p>

<h2>When we deploy Mission Control for a client</h2>
<p>When an organisation engages us, Mission Control processes information about how work moves through that organisation's systems: when work moves between people, teams and systems, how long steps take, and status changes and hand-offs. By design it does not capture the contents of emails, messages, files or documents, client or matter details inside those systems, or rankings of individual staff.</p>
<p>In a client deployment the client organisation decides the scope and purpose of processing, and we act on its instructions under our agreement with it. The client is responsible for notifying its people and for meeting workplace surveillance and privacy obligations where it operates, and we support it to do so. If you work for one of our clients and have a question about how your information is handled, please contact your employer first. You can also contact us.</p>

<h2>Who we share it with</h2>
<p>We do not sell personal information, and we do not share it for cross-context behavioural advertising. We share it only with service providers that help us run our business, such as website hosting, email delivery and email hosting providers, and only for that purpose. We may also disclose information where the law requires it.</p>

<h2>Overseas disclosure</h2>
<p>Some of our service providers store or process information outside Australia, including in the United States. Where we disclose personal information overseas we take reasonable steps to ensure it is protected in a way that is consistent with the Australian Privacy Principles.</p>

<h2>How long we keep it</h2>
<p>We keep enquiry information for as long as we need it to deal with your enquiry and any resulting relationship, and then delete or de-identify it unless we must keep it longer by law. Server logs are kept for a short period by our hosting provider.</p>

<h2>Security</h2>
<p>We take reasonable steps to protect personal information from misuse, interference, loss and unauthorised access, modification or disclosure. Access to enquiry information is limited to the people who need it.</p>

<h2>Your choices and rights</h2>
<p>You can ask to access or correct the personal information we hold about you. Depending on where you live, you may also have rights to ask us to delete it, to restrict or object to how we use it, or to receive a copy in a portable form. Contact us at <a href="mailto:hello@missioncntrl.io">hello@missioncntrl.io</a>. We will respond within a reasonable time, and within any period required by law. We will not discriminate against you for exercising your rights.</p>

<h2>Complaints</h2>
<p>If you are concerned about how we have handled your personal information, please contact us first so we can try to resolve it. If you are not satisfied, you can contact the <a href="https://www.oaic.gov.au/privacy/privacy-complaints" target="_blank" rel="noopener">Office of the Australian Information Commissioner</a>. In the UK you can contact the <a href="https://ico.org.uk/make-a-complaint/" target="_blank" rel="noopener">Information Commissioner's Office</a>.</p>

<h2>Children</h2>
<p>This website is for businesses and is not directed at children.</p>

<h2>Changes</h2>
<p>We may update this notice. The date at the top shows when it was last changed.</p>

<h2>Contact</h2>
<p>Email <a href="mailto:hello@missioncntrl.io">hello@missioncntrl.io</a> with "Privacy" in the subject line.</p>
"""

TERMS = """
<h2>About these terms</h2>
<p>These terms apply to your use of missioncntrl.io (the "website"), operated by Mission Control ("we", "us"). By using the website you agree to them. They do not govern use of the Mission Control platform or services, which are provided under a separate written agreement with each client.</p>

<h2>Information on the website</h2>
<p>The website gives general information about Mission Control and the topics we write about. It is not legal, financial, privacy or other professional advice, and you should take advice for your own circumstances. Figures, dashboards and product screens shown on the website are illustrative unless we say otherwise, and do not describe any particular client.</p>
<p>We work to keep the website accurate and up to date, but we do not promise that it is complete, current or free of errors, and we may change it at any time.</p>

<h2>Acceptable use</h2>
<p>Please do not misuse the website. That includes attempting to gain unauthorised access to it or to our systems, interfering with its operation, introducing malicious code, or using automated means to submit forms.</p>

<h2>Intellectual property</h2>
<p>The website and its content, including text, design, graphics, video and the Mission Control name and logo, are owned by us or our licensors. You may view and share pages for your own non-commercial purposes and quote short extracts of our articles with attribution and a link. Any other use needs our written permission.</p>

<h2>Links to other websites</h2>
<p>Our articles link to third-party sources so you can check our working. We do not control those websites and are not responsible for their content or privacy practices.</p>

<h2>Liability</h2>
<p>Nothing in these terms excludes, restricts or modifies any right or remedy you have under the Australian Consumer Law or any other law that cannot be excluded. Subject to that, we are not liable for any loss arising from your use of, or reliance on, the website. Where our liability cannot be excluded but can be limited, it is limited, at our option, to supplying the relevant information again.</p>

<h2>Privacy</h2>
<p>Our <a href="/privacy">privacy notice</a> explains how we handle personal information.</p>

<h2>Governing law</h2>
<p>These terms are governed by the laws of Victoria, Australia. You and we submit to the non-exclusive jurisdiction of the courts of Victoria.</p>

<h2>Changes</h2>
<p>We may update these terms. The date at the top shows when they were last changed.</p>

<h2>Contact</h2>
<p><a href="mailto:hello@missioncntrl.io">hello@missioncntrl.io</a></p>
"""

LEGAL_UPDATED = '2026-11-22'


def build_legal(header, footer, style):
    for slug, title, h1, lead, content in [
        ('privacy', 'Privacy notice | Mission Control', 'Privacy notice', 'How we handle personal information on this website and in client deployments.', PRIVACY),
        ('terms', 'Website terms of use | Mission Control', 'Website terms of use', 'The terms that apply when you use missioncntrl.io.', TERMS),
    ]:
        body = f"""<section><div class="wrap" style="padding-top:88px"><p class="eyb">Legal</p><h1 class="d h1">{h1}</h1><p class="lead">{lead}</p><div class="meta"><span>Last updated {nice_date(LEGAL_UPDATED)}</span></div></div></section>
<div class="legal">{content}</div>
<div style="height:96px"></div>"""
        wr(os.path.join(ROOT, slug + '.html'), page(title, lead, '/' + slug, body, header, footer, style, graph=[crumbs([('Home', '/'), (h1, '/' + slug)])]))
        print('legal', slug)
    body = """<section><div class="wrap" style="padding:120px 24px 40px"><p class="eyb">404</p><h1 class="d h1">This page has moved, or never existed.</h1><p class="lead">The link may be out of date. Try one of these instead.</p>
<div style="margin-top:32px;display:flex;flex-wrap:wrap;gap:10px"><a href="/" class="b1" style="display:inline-flex;align-items:center;gap:8px;min-height:46px;padding:0 20px;border-radius:8px;background:#0A0B0D;color:#FFFFFF;font-size:15px;font-weight:500">Go to the homepage <span class="ar" aria-hidden="true">→</span></a><a href="/news" class="b2" style="display:inline-flex;align-items:center;min-height:46px;padding:0 20px;border-radius:8px;border:1px solid #DADCE0;font-size:15px;font-weight:500">Read the newsroom</a><a href="/briefing" class="b2" style="display:inline-flex;align-items:center;min-height:46px;padding:0 20px;border-radius:8px;border:1px solid #DADCE0;font-size:15px;font-weight:500">Book a briefing</a></div></div></section><div style="height:80px"></div>"""
    s = page('Page not found | Mission Control', 'The page you were looking for could not be found.', '/404', body, header, footer, style)
    s = s.replace('<meta name="robots" content="index,follow,max-image-preview:large">', '<meta name="robots" content="noindex">')
    wr(os.path.join(ROOT, '404.html'), s)
    exp = (_dt.date.today() + _dt.timedelta(days=365)).isoformat()
    wr(os.path.join(ROOT, '.well-known', 'security.txt'), f'Contact: mailto:{EMAIL}\nExpires: {exp}T00:00:00.000Z\nPreferred-Languages: en\nCanonical: {SITE}/.well-known/security.txt\n')


# ---------------------------------------------------------------- 4. crawl files
def build_crawl(A):
    urls = [(SITE + u, TODAY, '1.0' if u == '/' else '0.8') for u, _ in MAIN.values()]
    urls += [(SITE + '/news', A[0]['date'] if A else TODAY, '0.8')]
    urls += [(SITE + a['url'], a['updated'], '0.7') for a in A]
    urls += [(SITE + '/privacy', LEGAL_UPDATED, '0.3'), (SITE + '/terms', LEGAL_UPDATED, '0.3')]
    wr(os.path.join(ROOT, 'sitemap.xml'), '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
       ''.join(f'  <url><loc>{u}</loc><lastmod>{d}</lastmod><priority>{p}</priority></url>\n' for u, d, p in urls) + '</urlset>\n')
    bots = ['GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'ClaudeBot', 'Claude-SearchBot', 'Claude-User', 'PerplexityBot', 'Google-Extended', 'Applebot-Extended', 'Bingbot', 'Googlebot']
    wr(os.path.join(ROOT, 'robots.txt'), '# Mission Control welcomes search engines and AI assistants.\n' + ''.join(f'User-agent: {b}\nAllow: /\n\n' for b in bots) +
       f'User-agent: *\nAllow: /\nDisallow: /api/\n\nSitemap: {SITE}/sitemap.xml\n')

    pages_desc = {
        '/': 'What Mission Control is: a live map of how work moves through a services organisation, where it stalls, and what is worth automating.',
        '/platform': 'The platform: live map, bottlenecks and moments, and automations ranked by what they return.',
        '/how-we-work': 'How engagements run: implementation fee, monthly platform fee, automations billed separately; deployed and run by our team.',
        '/industries': 'Who it is for: services organisations where the product is the work. Physical operations are on the roadmap.',
        '/security': 'What is captured (the movement of work) and never captured (contents of emails, files, or staff rankings), plus rollout with staff.',
        '/company': 'The team behind Mission Control and why it was built.',
        '/briefing': 'Book a 30-minute briefing.',
    }
    llms = [f'# {NAME}', '', '> Mission Control is operational intelligence for services organisations. It maps how work flows between people and teams, shows where it stalls, and tells you what to automate, with the business case attached. It is deployed and run with clients by the Mission Control team, and serves organisations in Australia, the United States and the United Kingdom.', '',
            'Key facts:', '- Category: operational intelligence and process automation for services businesses (accounting, legal, insurance, financial services, property, recruitment, agencies, healthcare administration).',
            '- Delivery: our team sets it up, provides a dashboard and reports, and builds the automations worth doing.',
            '- Pricing structure: implementation fee, monthly platform fee, automations billed separately. Quoted upfront after scoping.',
            '- Privacy: measures how work moves, not what it says. No email, message or document contents; no rankings of individual staff.',
            f'- Contact: {EMAIL}; book a briefing at {SITE}/briefing', '', '## Pages']
    llms += [f'- [{CRUMB.get(u, "Home")}]({SITE}{u}): {pages_desc[u]}' for u, _ in MAIN.values()]
    llms += ['', '## Newsroom', f'- [Newsroom]({SITE}/news): research and opinion on operations, automation and hand-offs.']
    llms += [f'- [{a["title"]}]({SITE}{a["url"]}): {a["dek"]} Markdown: {SITE}{a["url"]}.md' for a in A]
    llms += ['', '## Legal', f'- [Privacy notice]({SITE}/privacy)', f'- [Website terms]({SITE}/terms)', '', '## Optional', f'- [Full text for language models]({SITE}/llms-full.txt)', f'- [RSS feed]({SITE}/news/feed.xml)']
    wr(os.path.join(ROOT, 'llms.txt'), '\n'.join(llms) + '\n')

    full = [f'# {NAME}: full site text', f'Generated {TODAY}. Canonical site: {SITE}', '']
    for fn, (u, title) in MAIN.items():
        p = os.path.join(ROOT, fn)
        if not os.path.exists(p):
            continue
        s = rd(p)
        app = s[s.index('<div id="mc-app">'):]
        app = re.sub(r'<header.*?</header>|<footer.*?</footer>', '', app, flags=re.S)
        full += [f'## {title}', f'URL: {SITE}{u}', '', text_of(app), '']
        m = re.search(r'var faqItems = (\[.*?\]);', s, flags=re.S)
        if m:
            try:
                full += ['Frequently asked questions:'] + [f'Q: {q}\nA: {a}' for q, a in json.loads(m.group(1))] + ['']
            except Exception:
                pass
    for a in A:
        full += [f'## {a["title"]}', f'URL: {SITE}{a["url"]}', f'Published: {a["date"]}', '', text_of(a['body']), '']
    wr(os.path.join(ROOT, 'llms-full.txt'), '\n'.join(full) + '\n')
    print('crawl files written')


def main():
    og_default()
    process_main()
    header, footer, style = chrome()
    A = build_news(header, footer, style)
    build_legal(header, footer, style)
    build_crawl(A)


if __name__ == '__main__':
    main()
