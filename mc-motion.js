/* Mission Control motion and detail layer. Runs after the page renders; every class it adds starts with "mv-" so re-renders keep it. */
(function () {
  'use strict';
  var doc = document.documentElement;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var app = document.getElementById('mc-app');
  if (!app) return;

  function finishLoader() {
    if (!doc.classList.contains('mv-loading')) return;
    setTimeout(function () { doc.classList.add('mv-loaded'); }, reduce ? 0 : 950);
    setTimeout(function () { doc.classList.remove('mv-loading', 'mv-loaded'); }, reduce ? 0 : 1500);
  }

  /* Hero: split the headline into lines that rise, fade the supporting pieces, draw the survey pattern. */
  function hero() {
    var sec = app.querySelector('main > section');
    if (!sec || sec.classList.contains('mv-hero')) return;
    sec.classList.add('mv-hero');
    var h1 = sec.querySelector('h1');
    if (h1 && !reduce && !h1.hasAttribute('data-mv-split')) {
      var words = h1.textContent.trim().split(/\s+/);
      h1.setAttribute('data-mv-split', '1');
      h1.setAttribute('aria-label', h1.textContent.trim());
      h1.textContent = '';
      var probe = [];
      words.forEach(function (w) { var s = document.createElement('span'); s.textContent = w + ' '; s.style.display = 'inline-block'; s.style.whiteSpace = 'pre'; h1.appendChild(s); probe.push(s); });
      var lines = [], top = null;
      probe.forEach(function (s) { var t = s.offsetTop; if (top === null || Math.abs(t - top) > 4) { lines.push([]); top = t; } lines[lines.length - 1].push(s.textContent); });
      h1.textContent = '';
      lines.forEach(function (ws, i) {
        var outer = document.createElement('span'); outer.className = 'mv-h1-line'; outer.setAttribute('aria-hidden', 'true');
        var inner = document.createElement('span'); inner.textContent = ws.join('').trim(); outer.style.setProperty('--l', i);
        outer.appendChild(inner); h1.appendChild(outer);
      });
    }
    var fades = [];
    var eyebrow = h1 && h1.previousElementSibling; if (eyebrow) fades.push(eyebrow);
    sec.querySelectorAll('p, .b1, .b2').forEach(function (el) { if (el !== eyebrow && !h1.contains(el)) fades.push(el); });
    var media = sec.querySelector('video, [style*="aspect-ratio"], [style*="border-radius:14px"]');
    fades.forEach(function (el, i) { el.classList.add('mv-hero-fade'); el.style.setProperty('--d', (360 + i * 70) + 'ms'); });
    if (media) { var box = media.closest('[style*="border-radius"]') || media; box.classList.add('mv-hero-fade'); box.style.setProperty('--d', '620ms'); }
    if (!reduce) sec.classList.add('mv-hero-in');

    var bg = document.createElement('div'); bg.className = 'mv-hero-bg'; bg.setAttribute('aria-hidden', 'true'); bg.setAttribute('data-mv-ins', '1');
    bg.innerHTML = '<svg viewBox="0 0 1440 640" preserveAspectRatio="xMidYMid slice">' +
      '<path class="mv-route" style="--r:0" d="M-20 520 C 180 470 260 300 420 300 S 640 380 760 250 S 980 90 1180 130 S 1400 230 1480 180"/>' +
      '<path class="mv-route mv-route-live" id="mv-live-route" style="--r:1" d="M-20 140 C 160 160 220 260 380 250 S 600 120 760 160 S 1000 330 1200 300 S 1380 260 1480 300"/>' +
      '<path class="mv-route" style="--r:2" d="M260 660 C 300 520 420 470 540 440 S 760 470 860 380"/>' +
      '<circle class="mv-node" style="--r:0" cx="420" cy="300" r="4.5"/><circle class="mv-node mv-node-live" style="--r:1" cx="760" cy="160" r="4.5"/>' +
      '<circle class="mv-node" style="--r:1" cx="1200" cy="300" r="4.5"/><circle class="mv-node" style="--r:2" cx="860" cy="380" r="4.5"/>' +
      '<circle class="mv-traveller" r="3.5" style="offset-path:path(\'M-20 140 C 160 160 220 260 380 250 S 600 120 760 160 S 1000 330 1200 300 S 1380 260 1480 300\')"/>' +
      '</svg>';
    sec.insertBefore(bg, sec.firstChild);
  }

  /* Small structural details that ride on the existing markup. */
  function details() {
    var header = app.querySelector('header');
    if (header) header.classList.add('mv-nav');
    app.querySelectorAll('h2, h1').forEach(function (h) {
      var p = h.previousElementSibling;
      if (p && p.tagName === 'P' && /#157A36|#85EC68/i.test(p.getAttribute('style') || '')) p.classList.add('mv-waypoint');
    });
    app.querySelectorAll('video').forEach(function (v) {
      var box = v.parentElement; if (box) box.classList.add('mv-media');
      if (!v.hasAttribute('data-mv-bound')) {
        v.setAttribute('data-mv-bound', '1');
        if (v.readyState < 3 && !reduce) v.classList.add('mv-wait');
        var show = function () { v.classList.remove('mv-wait'); };
        v.addEventListener('playing', show); v.addEventListener('canplay', show); setTimeout(show, 2500);
        v.muted = true; try { var pr = v.play(); if (pr && pr.catch) pr.catch(function () {}); } catch (e) {}
      }
    });
    app.querySelectorAll('svg path').forEach(function (p) {
      var s = (p.getAttribute('stroke') || '').toUpperCase();
      if (s === '#E8590C' || s === '#F2A16B') p.classList.add('mv-flow');
    });
    app.querySelectorAll('.live, span[style*="background:#85EC68"][style*="border-radius:50%"]').forEach(function (d) {
      var w = parseFloat(d.style.width || '0'); if (w && w <= 10) d.classList.add('mv-live');
    });
  }

  /* Reveals: below-the-fold groups only, revealed once, pieces 80ms apart. */
  var io = null;
  function reveals() {
    if (reduce || !('IntersectionObserver' in window)) return;
    if (!io) io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('mv-in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.12 });
    var fold = window.innerHeight * 0.92;
    var secs = app.querySelectorAll('main > section');
    secs.forEach(function (sec, si) {
      if (si === 0) return;
      var groups = [];
      var h2 = sec.querySelector('h2');
      if (h2 && h2.parentElement) groups.push([].slice.call(h2.parentElement.children));
      sec.querySelectorAll('[style*="display:grid"], ol, tbody').forEach(function (g) {
        if (g.closest('.mv-rv-done')) return;
        var kids = [].slice.call(g.children).filter(function (k) { return k.tagName !== 'TEMPLATE'; });
        if (kids.length > 1 && kids.length < 13) groups.push(kids);
      });
      sec.querySelectorAll('video').forEach(function (v) { var b = v.closest('.mv-media'); if (b) groups.push([b]); });
      groups.forEach(function (els) {
        els.forEach(function (el, i) {
          if (el.classList.contains('mv-rv') || el.querySelector('.mv-rv')) return;
          if (el.getBoundingClientRect().top < fold) return;
          el.classList.add('mv-rv'); el.style.setProperty('--s', Math.min(i, 6)); io.observe(el);
        });
      });
    });
  }


  /* Product screens: survey grid behind, tilt-to-flat on arrival. */
  function frames() {
    app.querySelectorAll('[style*="0 40px 80px -40px"]').forEach(function (f) {
      var sec = f.closest('section'); if (sec && !sec.classList.contains('mv-hero')) sec.classList.add('mv-grid');
      if (reduce || !io || f.classList.contains('mv-tilt')) return;
      if (f.getBoundingClientRect().top < window.innerHeight * 0.92) return;
      f.classList.add('mv-tilt'); io.observe(f);
    });
  }

  /* Numbers count up once, when they come into view. */
  function counts() {
    if (reduce || !('IntersectionObserver' in window)) return;
    var re = /^(\$?)([\d,]+(?:\.\d+)?)(\s?[%a-zA-Z/]*)$/;
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return; cio.unobserve(e.target);
        var el = e.target, m = el.textContent.trim().match(re); if (!m) return;
        var target = parseFloat(m[2].replace(/,/g, '')), dec = (m[2].split('.')[1] || '').length, comma = m[2].indexOf(',') > -1;
        var t0 = null, dur = 1100;
        function fmt(v) { var s = v.toFixed(dec); if (comma) s = Number(s).toLocaleString('en-AU', { minimumFractionDigits: dec, maximumFractionDigits: dec }); return m[1] + s + m[3]; }
        function step(ts) { if (!t0) t0 = ts; var k = Math.min(1, (ts - t0) / dur); var eased = 1 - Math.pow(1 - k, 3); el.textContent = fmt(target * eased); if (k < 1) requestAnimationFrame(step); }
        el.textContent = fmt(0); requestAnimationFrame(step);
      });
    }, { threshold: 0.6 });
    app.querySelectorAll('.d, td').forEach(function (el) {
      if (el.children.length) return;
      var t = el.textContent.trim(); if (!re.test(t) || t.length > 12) return;
      var size = parseFloat(getComputedStyle(el).fontSize);
      if (size >= 22 || el.tagName === 'TD') cio.observe(el);
    });
  }

  /* Scroll state: nav settles, progress line fills. */
  function scrollUI() {
    var bar = document.getElementById('mv-progress');
    if (!bar) { bar = document.createElement('div'); bar.id = 'mv-progress'; bar.setAttribute('aria-hidden', 'true'); document.body.appendChild(bar); }
    var ticking = false;
    function update() {
      ticking = false;
      var y = window.scrollY, h = document.documentElement.scrollHeight - window.innerHeight;
      bar.style.transform = 'scaleX(' + (h > 0 ? Math.min(1, y / h) : 0) + ')';
      var header = app.querySelector('header'); if (header) header.classList.toggle('mv-scrolled', y > 8);
    }
    window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
    update();
  }

  function run() { details(); }
  function init() {
    hero(); details(); reveals(); frames(); counts(); scrollUI(); finishLoader();
    var render = window.MC && window.MC.render;
    if (render) window.MC.render = function () { render(); run(); };
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
  window.addEventListener('load', finishLoader);
})();
