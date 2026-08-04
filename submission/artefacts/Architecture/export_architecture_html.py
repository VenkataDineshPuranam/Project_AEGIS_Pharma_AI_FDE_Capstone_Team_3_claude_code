#!/usr/bin/env python
"""Embed AEGIS_ARCHITECTURE_MAP.json into a self-contained interactive HTML diagram."""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
JSON_PATH = HERE / "AEGIS_ARCHITECTURE_MAP.json"
HTML_PATH = HERE / "AEGIS_ARCHITECTURE_INTERACTIVE.html"

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>AEGIS-PHARMA Architecture Map</title>
<style>
  :root {
    --bg: #0f1419;
    --panel: #171d25;
    --panel-2: #1e2630;
    --border: #2c3642;
    --text: #e8eef4;
    --muted: #9aa8b5;
    --accent: #3d9cf0;
    --accent-2: #5ec4a2;
    --warn: #e0a35c;
    --danger: #e06c75;
    --node: #243040;
    --node-stroke: #4a5d73;
    --highlight: #f0c14a;
    --highlight-edge: #ffd666;
    --shadow: 0 10px 40px rgba(0,0,0,.35);
    --radius: 12px;
    --font: "Segoe UI", "IBM Plex Sans", system-ui, sans-serif;
    --mono: "Cascadia Code", "Consolas", ui-monospace, monospace;
  }
  * { box-sizing: border-box; }
  html, body { margin: 0; height: 100%; background: var(--bg); color: var(--text); font-family: var(--font); }
  body {
    display: grid;
    grid-template-rows: auto 1fr;
    min-height: 100vh;
    background:
      radial-gradient(1200px 600px at 10% -10%, rgba(61,156,240,.18), transparent 55%),
      radial-gradient(900px 500px at 90% 0%, rgba(94,196,162,.12), transparent 50%),
      var(--bg);
  }
  header {
    display: flex; flex-wrap: wrap; gap: 12px 20px; align-items: center; justify-content: space-between;
    padding: 14px 20px; border-bottom: 1px solid var(--border); background: rgba(15,20,25,.85); backdrop-filter: blur(8px);
    position: sticky; top: 0; z-index: 5;
  }
  header h1 { margin: 0; font-size: 1.15rem; font-weight: 650; letter-spacing: .02em; }
  header p { margin: 0; color: var(--muted); font-size: .85rem; max-width: 52ch; }
  .badges { display: flex; flex-wrap: wrap; gap: 8px; }
  .badge {
    font-size: .72rem; padding: 4px 9px; border-radius: 999px; border: 1px solid var(--border);
    background: var(--panel-2); color: var(--muted); font-family: var(--mono);
  }
  .badge.ok { color: var(--accent-2); border-color: rgba(94,196,162,.4); }
  .badge.warn { color: var(--warn); border-color: rgba(224,163,92,.4); }
  main {
    display: grid;
    grid-template-columns: 1fr minmax(280px, 360px);
    min-height: 0;
  }
  @media (max-width: 960px) {
    main { grid-template-columns: 1fr; grid-template-rows: minmax(420px, 55vh) 1fr; }
  }
  .canvas-wrap {
    position: relative; min-height: 0; overflow: hidden; border-right: 1px solid var(--border);
  }
  svg#graph {
    width: 100%; height: 100%; min-height: 520px; display: block; cursor: grab;
    background:
      linear-gradient(transparent 23px, rgba(255,255,255,.03) 24px),
      linear-gradient(90deg, transparent 23px, rgba(255,255,255,.03) 24px);
    background-size: 24px 24px;
  }
  svg#graph:active { cursor: grabbing; }
  .edge { fill: none; stroke: #4a5a6a; stroke-width: 1.6; opacity: .75; transition: stroke .2s, opacity .2s, stroke-width .2s; }
  .edge.dim { opacity: .12; }
  .edge.hot { stroke: var(--highlight-edge); stroke-width: 3.2; opacity: 1; filter: drop-shadow(0 0 4px rgba(240,193,74,.45)); }
  .edge-label { fill: var(--muted); font-size: 10px; opacity: 0; pointer-events: none; }
  .edge-label.show { opacity: .9; }
  .node rect {
    fill: var(--node); stroke: var(--node-stroke); stroke-width: 1.5; rx: 10; ry: 10;
    transition: fill .2s, stroke .2s, filter .2s;
    filter: drop-shadow(0 2px 6px rgba(0,0,0,.25));
  }
  .node.dim rect { opacity: .22; }
  .node.hot rect {
    stroke: var(--highlight); stroke-width: 2.6;
    fill: #2f3d28;
    filter: drop-shadow(0 0 10px rgba(240,193,74,.35));
  }
  .node.selected rect { stroke: var(--accent); }
  .node text { fill: var(--text); font-size: 11.5px; pointer-events: none; font-weight: 600; }
  .node .sub { fill: var(--muted); font-size: 9.5px; font-weight: 400; font-family: var(--mono); }
  .node.dim text, .node.dim .sub { opacity: .25; }
  .layer-band { fill: rgba(255,255,255,.02); stroke: none; }
  .layer-title { fill: var(--muted); font-size: 11px; font-weight: 700; letter-spacing: .08em; text-transform: uppercase; }
  aside {
    display: flex; flex-direction: column; min-height: 0; background: var(--panel);
  }
  .aside-head {
    padding: 14px 16px 10px; border-bottom: 1px solid var(--border);
  }
  .aside-head h2 { margin: 0 0 4px; font-size: 1rem; }
  .aside-head p { margin: 0; color: var(--muted); font-size: .8rem; }
  .controls { display: flex; gap: 8px; margin-top: 10px; flex-wrap: wrap; }
  button, .btn {
    appearance: none; border: 1px solid var(--border); background: var(--panel-2); color: var(--text);
    border-radius: 8px; padding: 7px 10px; font-size: .78rem; cursor: pointer;
  }
  button:hover { border-color: var(--accent); color: #fff; }
  button.active { background: rgba(61,156,240,.2); border-color: var(--accent); }
  .flows {
    overflow: auto; padding: 10px 12px 16px; display: flex; flex-direction: column; gap: 8px; flex: 1;
  }
  .flow-card {
    border: 1px solid var(--border); background: var(--panel-2); border-radius: var(--radius);
    padding: 10px 12px; cursor: pointer; transition: border-color .15s, transform .15s, background .15s;
  }
  .flow-card:hover { border-color: var(--accent); transform: translateY(-1px); }
  .flow-card.active {
    border-color: var(--highlight); background: rgba(240,193,74,.08);
    box-shadow: inset 0 0 0 1px rgba(240,193,74,.25);
  }
  .flow-card h3 { margin: 0 0 4px; font-size: .88rem; }
  .flow-card p { margin: 0; color: var(--muted); font-size: .75rem; line-height: 1.35; }
  .flow-meta { margin-top: 6px; font-family: var(--mono); font-size: .68rem; color: var(--accent-2); }
  .detail {
    border-top: 1px solid var(--border); padding: 12px 16px; background: #121820; max-height: 38%;
    overflow: auto;
  }
  .detail h3 { margin: 0 0 6px; font-size: .92rem; }
  .detail .path { font-family: var(--mono); font-size: .72rem; color: var(--accent); margin-bottom: 8px; word-break: break-all; }
  .detail p { margin: 0; color: var(--muted); font-size: .8rem; line-height: 1.45; }
  .tags { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 8px; }
  .tag { font-size: .68rem; padding: 2px 7px; border-radius: 6px; background: #243041; color: var(--muted); border: 1px solid var(--border); }
  #tooltip {
    position: fixed; z-index: 20; pointer-events: none; max-width: 320px;
    background: #101820; color: var(--text); border: 1px solid var(--accent);
    border-radius: 10px; padding: 10px 12px; box-shadow: var(--shadow);
    opacity: 0; transform: translateY(4px); transition: opacity .12s;
    font-size: .78rem; line-height: 1.4;
  }
  #tooltip.visible { opacity: 1; transform: none; }
  #tooltip strong { display: block; margin-bottom: 4px; }
  #tooltip .tt-path { color: var(--accent-2); font-family: var(--mono); font-size: .7rem; margin-bottom: 4px; }
  .legend {
    position: absolute; left: 12px; bottom: 12px; z-index: 3;
    background: rgba(23,29,37,.92); border: 1px solid var(--border); border-radius: 10px;
    padding: 8px 10px; font-size: .7rem; color: var(--muted); display: flex; gap: 12px; flex-wrap: wrap;
  }
  .legend span::before {
    content: ""; display: inline-block; width: 10px; height: 10px; border-radius: 3px; margin-right: 5px; vertical-align: -1px;
  }
  .legend .l-actor::before { background: #3b4f6b; }
  .legend .l-challenge::before { background: #4a3d2e; }
  .legend .l-runtime::before { background: #2a4a3a; }
  .legend .l-eval::before { background: #3a2f4f; }
  .hint { position: absolute; top: 12px; left: 12px; z-index: 3; color: var(--muted); font-size: .72rem;
    background: rgba(23,29,37,.85); border: 1px solid var(--border); border-radius: 8px; padding: 6px 9px; }
</style>
</head>
<body>
<header>
  <div>
    <h1>Project AEGIS-PHARMA — Interactive Architecture</h1>
    <p>Challenge package + planned submission runtime. Select a flow to highlight the complete path. Nodes show tooltips.</p>
  </div>
  <div class="badges">
    <span class="badge ok">writable: submission/</span>
    <span class="badge warn">challenge evidence immutable</span>
    <span class="badge" id="counts"></span>
  </div>
</header>
<main>
  <section class="canvas-wrap" aria-label="Architecture diagram">
    <div class="hint">Drag to pan · Scroll to zoom · Click node or flow</div>
    <svg id="graph" role="img" aria-label="AEGIS architecture graph"></svg>
    <div class="legend">
      <span class="l-actor">Actors / tooling</span>
      <span class="l-challenge">Challenge evidence</span>
      <span class="l-runtime">Runtime / workflows</span>
      <span class="l-eval">Eval / ops</span>
    </div>
  </section>
  <aside>
    <div class="aside-head">
      <h2>Flows</h2>
      <p>Select a flow to highlight nodes and edges on the path.</p>
      <div class="controls">
        <button type="button" id="btnClear">Clear highlight</button>
        <button type="button" id="btnFit">Fit view</button>
      </div>
    </div>
    <div class="flows" id="flowList"></div>
    <div class="detail" id="detail">
      <h3>Component detail</h3>
      <p class="path">Select a node or flow</p>
      <p>Tooltips appear on hover. Flow selection dims unrelated components.</p>
    </div>
  </aside>
</main>
<div id="tooltip" role="tooltip"></div>
<script id="arch-data" type="application/json">__ARCH_JSON__</script>
<script>
(function () {
  const ARCH = JSON.parse(document.getElementById('arch-data').textContent);
  const svg = document.getElementById('graph');
  const flowList = document.getElementById('flowList');
  const detail = document.getElementById('detail');
  const tooltip = document.getElementById('tooltip');
  const counts = document.getElementById('counts');
  counts.textContent = ARCH.nodes.length + ' nodes · ' + ARCH.edges.length + ' edges · ' + ARCH.flows.length + ' flows';

  const LAYER_ORDER = ARCH.layers.slice().sort((a,b) => a.order - b.order).map(l => l.id);
  const LAYER_COLORS = {
    actors: '#243447',
    challenge: '#3a3228',
    tooling: '#243447',
    brownfield: '#3a3228',
    runtime: '#243a32',
    workflows: '#243a32',
    eval: '#322844',
    ops: '#322844'
  };

  // Layout: columns by layer, stack nodes vertically
  const COL_W = 210;
  const NODE_W = 168;
  const NODE_H = 46;
  const ROW_GAP = 14;
  const COL_GAP = 48;
  const PAD_X = 40;
  const PAD_Y = 56;

  const nodesByLayer = {};
  LAYER_ORDER.forEach(l => { nodesByLayer[l] = []; });
  ARCH.nodes.forEach(n => {
    (nodesByLayer[n.layer] || (nodesByLayer[n.layer] = [])).push(n);
  });

  const pos = {};
  let maxH = 0;
  LAYER_ORDER.forEach((layer, li) => {
    const list = nodesByLayer[layer] || [];
    list.forEach((n, ni) => {
      const x = PAD_X + li * (COL_W + COL_GAP);
      const y = PAD_Y + ni * (NODE_H + ROW_GAP);
      pos[n.id] = { x, y, w: NODE_W, h: NODE_H, layer };
      maxH = Math.max(maxH, y + NODE_H + 40);
    });
  });
  const width = PAD_X + LAYER_ORDER.length * (COL_W + COL_GAP);
  const height = Math.max(maxH, 640);

  const NS = 'http://www.w3.org/2000/svg';
  function el(name, attrs, parent) {
    const e = document.createElementNS(NS, name);
    if (attrs) Object.entries(attrs).forEach(([k,v]) => e.setAttribute(k, v));
    if (parent) parent.appendChild(e);
    return e;
  }

  // Viewport transform
  let view = { x: 0, y: 0, k: 0.92 };
  const root = el('g', { id: 'viewport' }, svg);
  const bands = el('g', { id: 'bands' }, root);
  const edgesG = el('g', { id: 'edges' }, root);
  const nodesG = el('g', { id: 'nodes' }, root);

  LAYER_ORDER.forEach((layer, li) => {
    const x = PAD_X + li * (COL_W + COL_GAP) - 16;
    el('rect', {
      class: 'layer-band', x: x, y: 28, width: COL_W + 8, height: height - 40, rx: 12
    }, bands);
    const title = ARCH.layers.find(l => l.id === layer);
    el('text', {
      class: 'layer-title', x: x + 8, y: 48
    }, bands).textContent = title ? title.label : layer;
  });

  function edgePath(a, b) {
    const x1 = a.x + a.w;
    const y1 = a.y + a.h / 2;
    const x2 = b.x;
    const y2 = b.y + b.h / 2;
    const mx = (x1 + x2) / 2;
    return `M ${x1} ${y1} C ${mx} ${y1}, ${mx} ${y2}, ${x2} ${y2}`;
  }

  const edgeEls = {};
  ARCH.edges.forEach(e => {
    const a = pos[e.from], b = pos[e.to];
    if (!a || !b) return;
    const path = el('path', {
      class: 'edge', id: 'edge-' + e.id, d: edgePath(a, b),
      'data-from': e.from, 'data-to': e.to
    }, edgesG);
    edgeEls[e.id] = path;
  });

  const nodeEls = {};
  ARCH.nodes.forEach(n => {
    const p = pos[n.id];
    const g = el('g', {
      class: 'node', id: 'node-' + n.id, transform: `translate(${p.x},${p.y})`,
      'data-id': n.id
    }, nodesG);
    const fill = LAYER_COLORS[n.layer] || '#243040';
    el('rect', { width: p.w, height: p.h, fill: fill, stroke: '#5a6d82' }, g);
    const label = n.label.length > 28 ? n.label.slice(0, 26) + '…' : n.label;
    el('text', { x: 10, y: 20 }, g).textContent = label;
    el('text', { class: 'sub', x: 10, y: 36 }, g).textContent = n.type + (n.path ? ' · ' + n.path.split('/').filter(Boolean).slice(-1)[0] : '');
    nodeEls[n.id] = g;

    g.addEventListener('mouseenter', (ev) => showTip(n, ev));
    g.addEventListener('mousemove', (ev) => moveTip(ev));
    g.addEventListener('mouseleave', hideTip);
    g.addEventListener('click', () => selectNode(n.id));
  });

  function applyView() {
    root.setAttribute('transform', `translate(${view.x},${view.y}) scale(${view.k})`);
  }
  function fit() {
    const rect = svg.getBoundingClientRect();
    const sx = rect.width / width;
    const sy = rect.height / height;
    view.k = Math.min(sx, sy) * 0.95;
    view.x = (rect.width - width * view.k) / 2;
    view.y = 20;
    applyView();
  }

  // Pan / zoom
  let dragging = false, last = null;
  svg.addEventListener('mousedown', e => { dragging = true; last = { x: e.clientX, y: e.clientY }; });
  window.addEventListener('mouseup', () => { dragging = false; });
  window.addEventListener('mousemove', e => {
    if (!dragging) return;
    view.x += e.clientX - last.x;
    view.y += e.clientY - last.y;
    last = { x: e.clientX, y: e.clientY };
    applyView();
  });
  svg.addEventListener('wheel', e => {
    e.preventDefault();
    const rect = svg.getBoundingClientRect();
    const mx = e.clientX - rect.left;
    const my = e.clientY - rect.top;
    const prev = view.k;
    const next = Math.min(2.2, Math.max(0.35, view.k * (e.deltaY < 0 ? 1.08 : 0.92)));
    view.x = mx - (mx - view.x) * (next / prev);
    view.y = my - (my - view.y) * (next / prev);
    view.k = next;
    applyView();
  }, { passive: false });

  let activeFlow = null;
  let selectedNode = null;

  function clearHighlight() {
    activeFlow = null;
    document.querySelectorAll('.flow-card').forEach(c => c.classList.remove('active'));
    Object.values(nodeEls).forEach(g => g.classList.remove('hot', 'dim', 'selected'));
    Object.values(edgeEls).forEach(p => p.classList.remove('hot', 'dim'));
    if (selectedNode) nodeEls[selectedNode]?.classList.add('selected');
  }

  function highlightFlow(flow) {
    activeFlow = flow.id;
    const stepSet = new Set(flow.steps);
    // edges between consecutive steps OR any edge connecting two steps in the set
    const hotEdges = new Set();
    for (let i = 0; i < flow.steps.length - 1; i++) {
      const a = flow.steps[i], b = flow.steps[i + 1];
      ARCH.edges.forEach(e => {
        if ((e.from === a && e.to === b) || (e.from === b && e.to === a)) hotEdges.add(e.id);
      });
    }
    ARCH.edges.forEach(e => {
      if (stepSet.has(e.from) && stepSet.has(e.to)) hotEdges.add(e.id);
    });

    Object.values(nodeEls).forEach(g => {
      g.classList.remove('hot', 'dim', 'selected');
      const id = g.getAttribute('data-id');
      if (stepSet.has(id)) g.classList.add('hot');
      else g.classList.add('dim');
    });
    Object.entries(edgeEls).forEach(([id, p]) => {
      p.classList.remove('hot', 'dim');
      if (hotEdges.has(id)) p.classList.add('hot');
      else p.classList.add('dim');
    });

    detail.innerHTML = '<h3>' + escapeHtml(flow.name) + '</h3>' +
      '<p class="path">' + escapeHtml(flow.id) + ' · ' + flow.steps.length + ' steps</p>' +
      '<p>' + escapeHtml(flow.description) + '</p>' +
      '<div class="tags">' + flow.steps.map(s => '<span class="tag">' + escapeHtml(s) + '</span>').join('') + '</div>';
  }

  function selectNode(id) {
    selectedNode = id;
    const n = ARCH.nodes.find(x => x.id === id);
    if (!n) return;
    if (!activeFlow) {
      Object.values(nodeEls).forEach(g => g.classList.remove('selected'));
      nodeEls[id]?.classList.add('selected');
      // soft neighborhood highlight
      const neigh = new Set([id]);
      const hotE = new Set();
      ARCH.edges.forEach(e => {
        if (e.from === id || e.to === id) { neigh.add(e.from); neigh.add(e.to); hotE.add(e.id); }
      });
      Object.values(nodeEls).forEach(g => {
        g.classList.remove('hot', 'dim');
        const gid = g.getAttribute('data-id');
        if (neigh.has(gid)) g.classList.add('hot'); else g.classList.add('dim');
      });
      Object.entries(edgeEls).forEach(([eid, p]) => {
        p.classList.remove('hot', 'dim');
        if (hotE.has(eid)) p.classList.add('hot'); else p.classList.add('dim');
      });
      nodeEls[id]?.classList.add('selected');
    }
    detail.innerHTML = '<h3>' + escapeHtml(n.label) + '</h3>' +
      '<p class="path">' + escapeHtml(n.path || '') + '</p>' +
      '<p>' + escapeHtml(n.tooltip || '') + '</p>' +
      '<div class="tags"><span class="tag">' + escapeHtml(n.layer) + '</span><span class="tag">' +
      escapeHtml(n.type) + '</span>' + (n.tags || []).map(t => '<span class="tag">' + escapeHtml(t) + '</span>').join('') +
      '</div>';
  }

  function escapeHtml(s) {
    return String(s ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  }

  function showTip(n, ev) {
    tooltip.innerHTML = '<strong>' + escapeHtml(n.label) + '</strong>' +
      '<div class="tt-path">' + escapeHtml(n.path || n.id) + '</div>' +
      escapeHtml(n.tooltip || '');
    tooltip.classList.add('visible');
    moveTip(ev);
  }
  function moveTip(ev) {
    const pad = 14;
    let x = ev.clientX + pad, y = ev.clientY + pad;
    const r = tooltip.getBoundingClientRect();
    if (x + r.width > window.innerWidth - 8) x = ev.clientX - r.width - pad;
    if (y + r.height > window.innerHeight - 8) y = ev.clientY - r.height - pad;
    tooltip.style.left = x + 'px';
    tooltip.style.top = y + 'px';
  }
  function hideTip() { tooltip.classList.remove('visible'); }

  ARCH.flows.forEach(flow => {
    const card = document.createElement('article');
    card.className = 'flow-card';
    card.innerHTML = '<h3></h3><p></p><div class="flow-meta"></div>';
    card.querySelector('h3').textContent = flow.name;
    card.querySelector('p').textContent = flow.description;
    card.querySelector('.flow-meta').textContent = flow.steps.length + ' steps · ' + (flow.audience || []).join(', ');
    card.addEventListener('click', () => {
      document.querySelectorAll('.flow-card').forEach(c => c.classList.remove('active'));
      card.classList.add('active');
      highlightFlow(flow);
    });
    flowList.appendChild(card);
  });

  document.getElementById('btnClear').addEventListener('click', () => {
    clearHighlight();
    detail.innerHTML = '<h3>Component detail</h3><p class="path">Select a node or flow</p><p>Highlight cleared.</p>';
  });
  document.getElementById('btnFit').addEventListener('click', fit);

  window.addEventListener('resize', fit);
  fit();
})();
</script>
</body>
</html>
"""


def main() -> None:
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    # Compact embed (still valid JSON)
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    # Prevent accidental </script> breakout
    payload = payload.replace("</", "<\\/")
    html = HTML_TEMPLATE.replace("__ARCH_JSON__", payload)
    HTML_PATH.write_text(html, encoding="utf-8")
    print(f"Wrote {HTML_PATH} ({len(data['nodes'])} nodes, {len(data['edges'])} edges, {len(data['flows'])} flows)")


if __name__ == "__main__":
    main()
