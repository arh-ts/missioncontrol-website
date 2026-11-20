#!/usr/bin/env python3
"""Compile the Mission Control V3 design pages into a static site in OUT."""
import re, sys, shutil, os, json
SRC = '/home/claude/mc2/project'
OUT = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/missioncontrol-website'

PAGES = {
    'Home-V3.dc.html': ('index.html', '/', 'Mission Control maps how work flows between your people and teams, shows where it stalls, and tells you exactly what to automate, with the business case attached.'),
    'Platform-V3.dc.html': ('platform.html', '/platform', 'Operational intelligence for services organisations: a live map of how work moves, where it stalls and what it would be worth to automate.'),
    'HowWeWork-V3.dc.html': ('how-we-work.html', '/how-we-work', 'Mission Control is deployed and run with you by our team, from first briefing to automations that pay for themselves.'),
    'Industries-V3.dc.html': ('industries.html', '/industries', 'Built for organisations where the product is the work: accounting, legal, insurance, financial services, property, recruitment, agencies and healthcare administration.'),
    'Security-V3.dc.html': ('security.html', '/security', 'Mission Control maps how work moves, not what it says. Designed to pass your security review and to be rolled out openly with your people.'),
    'Company-V3.dc.html': ('company.html', '/company', 'We built Mission Control because we needed it. Meet the team behind it.'),
    'Briefing-V3.dc.html': ('briefing.html', '/briefing', 'Book a 30-minute briefing with the Mission Control team.'),
}
MEDIA = {
    '5f444ae733218df8443956ffe7496978': ('/home/claude/brand/lockup-light.svg', 'mission-control-logo.svg'),
    '0f7e7d87d6394b84028f82c7a752723a': ('/home/claude/brand/mark-deep.svg', 'mark.svg'),
    '4252a436427190d8843b53d6fc9a088f': ('/home/claude/img/tangle.jpg', 'before.jpg'),
    'fdaba4287c5f3bd30007dfd3f57a8633': ('/home/claude/img/clear.jpg', 'after.jpg'),
    'a60c2c0bd7da2d874191da3a46feb609': ('/home/claude/vid/overhead.mp4', 'overhead.mp4'),
    '4cee990f4f6e40fa8c1ed5e661a22ed9': ('/home/claude/vid/overhead-poster.jpg', 'overhead.jpg'),
    '2adfa15d353451be6038078795e3103f': ('/home/claude/vid/leader.mp4', 'leader.mp4'),
    '22525d641ae94f0fc2df366f127f4188': ('/home/claude/vid/leader-poster.jpg', 'leader.jpg'),
    '7d530c71ddd6c65481543937e9c81a26': ('/home/claude/vid/whiteboard.mp4', 'whiteboard.mp4'),
    'b4f5dcc33ea1ea6cbc0fd817b8451ab5': ('/home/claude/vid/whiteboard-poster.jpg', 'whiteboard.jpg'),
    '36d1c3a4445feeeff6e1c607ba4462d3': ('/home/claude/vid/factory.mp4', 'factory.mp4'),
    '7c381692a494be53b7a0c56a74d7aecf': ('/home/claude/vid/factory-poster.jpg', 'factory.jpg'),
    '452f36bd032df4a4e252718e08a0b13f': ('/home/claude/vid/call.mp4', 'call.mp4'),
    '3bb593c211c6ef064d73709b54adcb6a': ('/home/claude/vid/call-poster.jpg', 'call.jpg'),
}

def between(s, a, b):
    i = s.index(a) + len(a); j = s.index(b, i); return s[i:j]

os.makedirs(OUT + '/media', exist_ok=True)
for bid, (path, name) in MEDIA.items():
    shutil.copyfile(path, f'{OUT}/media/{name}')
for f in ('mc.js','mc-motion.js','mc-motion.css'):
    shutil.copyfile(f'/home/claude/site/{f}', f'{OUT}/{f}')
LOADER = open('/home/claude/site/loader.html').read()

def rewrite(s):
    for bid, (_, name) in MEDIA.items():
        s = s.replace(f'/_blob/{bid}', f'/media/{name}')
    def link(m):
        page, frag = m.group(1), m.group(2) or ''
        url = PAGES[page][1]
        return f'href="{url}{frag}"'
    s = re.sub(r'href="([A-Za-z0-9-]+\.dc\.html)(#[A-Za-z0-9_-]+)?"', link, s)
    return s

for src, (out, url, desc) in PAGES.items():
    s = open(f'{SRC}/{src}').read()
    title = between(s, '<title>', '</title>')
    xdc = between(s, '<x-dc>', '</x-dc>')
    helmet = between(xdc, '<helmet>', '</helmet>')
    body = xdc.split('</helmet>', 1)[1]
    script = between(s, 'data-dc-script', '</script>')
    script = script[script.index('>') + 1:]
    # dc markup to plain templates
    body = re.sub(r'<sc-for list="([^"]*)" as="([^"]*)">', r'<template data-for="\1" data-as="\2">', body)
    body = body.replace('</sc-for>', '</template>')
    body = re.sub(r'<sc-if value="([^"]*)"[^>]*>', r'<template data-if="\1">', body)
    body = body.replace('</sc-if>', '</template>')
    body = body.replace('onClick="', 'data-on-click="').replace('onSubmit="', 'data-on-submit="')
    body, helmet = rewrite(body), rewrite(helmet)
    canon = 'https://missioncntrl.io' + ('' if url == '/' else url)
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="/media/overhead.jpg">
<meta property="og:type" content="website">
<link rel="icon" type="image/svg+xml" href="/media/mark.svg">
<meta name="theme-color" content="#FFFFFF">
<script>try{{if(!sessionStorage.getItem("mv-seen")&&!matchMedia("(prefers-reduced-motion: reduce)").matches){{document.documentElement.classList.add("mv-loading");sessionStorage.setItem("mv-seen","1")}}}}catch(e){{}}</script>
{helmet}
<link rel="stylesheet" href="/mc-motion.css">
</head>
<body>
{LOADER}
<template id="mc-root">{body}</template>
<div id="mc-app"></div>
<script src="/mc.js"></script>
<script>
{script}
MC.mount(Component);
</script>
<script src="/mc-motion.js"></script>
</body>
</html>
"""
    open(f'{OUT}/{out}', 'w').write(html)
    print('built', out)
