/* Mission Control site runtime: renders the page template with live state, keeps the DOM stable between updates. */
(function () {
  'use strict';
  function DCLogic(props) { this.props = props || {}; this.state = {}; }
  DCLogic.prototype.setState = function (patch) {
    for (var k in patch) this.state[k] = patch[k];
    if (window.MC && window.MC.render) window.MC.render();
  };
  window.DCLogic = DCLogic;

  var WHOLE = /^\{\{\s*([^}]+?)\s*\}\}$/;
  var HOLE = /\{\{\s*([^}]+?)\s*\}\}/g;
  function get(path, scope) {
    path = path.trim();
    if (path === 'true') return true;
    if (path === 'false') return false;
    var parts = path.split('.'), v = scope;
    for (var i = 0; i < parts.length; i++) { if (v == null) return undefined; v = v[parts[i]]; }
    return v;
  }
  function interp(str, scope) {
    var m = str.match(WHOLE);
    if (m) return get(m[1], scope);
    return str.replace(HOLE, function (_, p) { var v = get(p, scope); return v == null ? '' : String(v); });
  }

  function proc(node, scope, out) {
    if (node.nodeType === 3) {
      var t = node.nodeValue;
      if (t.indexOf('{{') > -1) { var v = interp(t, scope); t = v == null ? '' : String(v); }
      out.appendChild(document.createTextNode(t));
      return;
    }
    if (node.nodeType !== 1) return;
    if (node.localName === 'template' && node.hasAttribute('data-for')) {
      var list = interp(node.getAttribute('data-for'), scope) || [];
      var as = node.getAttribute('data-as');
      for (var i = 0; i < list.length; i++) {
        var s = Object.create(scope); s[as] = list[i];
        var kids = node.content.childNodes;
        for (var j = 0; j < kids.length; j++) proc(kids[j], s, out);
      }
      return;
    }
    if (node.localName === 'template' && node.hasAttribute('data-if')) {
      if (interp(node.getAttribute('data-if'), scope)) {
        var ck = node.content.childNodes;
        for (var c = 0; c < ck.length; c++) proc(ck[c], scope, out);
      }
      return;
    }
    var el = document.importNode(node, false);
    var attrs = Array.prototype.slice.call(el.attributes);
    for (var a = 0; a < attrs.length; a++) {
      var name = attrs[a].name, val = attrs[a].value;
      if (name.indexOf('data-on-') === 0) {
        el.__mc = el.__mc || {};
        el.__mc[name.slice(8)] = interp(val, scope);
        el.removeAttribute(name);
      } else if (val.indexOf('{{') > -1) {
        var r = interp(val, scope);
        el.setAttribute(name, r == null ? '' : String(r));
      }
    }
    var src = node.localName === 'template' ? node.content.childNodes : node.childNodes;
    for (var k = 0; k < src.length; k++) proc(src[k], scope, el);
    out.appendChild(el);
  }

  function morph(a, b, root) {
    if (a.nodeType === 1 && !root) {
      var keep = (a.getAttribute('class') || '').split(/\s+/).filter(function (c) { return c.indexOf('mv-') === 0; });
      var aa = Array.prototype.slice.call(a.attributes);
      for (var i = 0; i < aa.length; i++) {
        var nm = aa[i].name;
        if (nm.indexOf('data-mv') === 0 || nm === 'aria-label' && a.hasAttribute('data-mv-split')) continue;
        if (!b.hasAttribute(nm) && !(nm === 'class' && keep.length)) a.removeAttribute(nm);
      }
      for (var j = 0; j < b.attributes.length; j++) {
        var at = b.attributes[j], v = at.value;
        if (at.name === 'class' && keep.length) v = (v + ' ' + keep.join(' ')).trim();
        if (at.name === 'style' && a.hasAttribute('data-mv-ins')) continue;
        if (a.getAttribute(at.name) !== v) a.setAttribute(at.name, v);
      }
      if (keep.length && !b.hasAttribute('class')) a.setAttribute('class', keep.join(' '));
      a.__mc = b.__mc;
      if (a.localName === 'video' || a.hasAttribute('data-mv-split')) return;
    }
    var ac = Array.prototype.slice.call(a.childNodes).filter(function (n) { return !(n.nodeType === 1 && n.hasAttribute('data-mv-ins')); }), bc = Array.prototype.slice.call(b.childNodes);
    for (var n = 0; n < bc.length; n++) {
      var x = ac[n], y = bc[n];
      if (!x) { a.appendChild(y); continue; }
      if (x.nodeType !== y.nodeType || (x.nodeType === 1 && (x.localName !== y.localName || x.namespaceURI !== y.namespaceURI))) { a.replaceChild(y, x); continue; }
      if (x.nodeType !== 1) { if (x.nodeValue !== y.nodeValue) x.nodeValue = y.nodeValue; continue; }
      morph(x, y);
    }
    for (var r = bc.length; r < ac.length; r++) a.removeChild(ac[r]);
  }

  function delegate(type) {
    document.addEventListener(type, function (e) {
      var n = e.target;
      while (n && n !== document) {
        if (n.__mc && typeof n.__mc[type] === 'function') { n.__mc[type](e); return; }
        n = n.parentNode;
      }
    });
  }

  window.MC = {
    mount: function (C) {
      var tpl = document.getElementById('mc-root');
      var app = document.getElementById('mc-app');
      var comp = new C({});
      window.MC.render = function () {
        var vals = comp.renderVals() || {};
        var frag = document.createElement('div');
        var kids = tpl.content.childNodes;
        for (var i = 0; i < kids.length; i++) proc(kids[i], vals, frag);
        morph(app, frag, true);
      };
      window.MC.render();
      delegate('click'); delegate('submit');
      var vids = document.querySelectorAll('video');
      for (var v = 0; v < vids.length; v++) { try { vids[v].muted = true; var p = vids[v].play(); if (p && p.catch) p.catch(function () {}); } catch (err) {} }
    }
  };
})();
