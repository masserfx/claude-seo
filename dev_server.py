#!/usr/bin/env python3
"""
Claude SEO - Local Development Server

Provides a web API and UI for testing SEO analysis scripts locally.

Usage:
    python dev_server.py
    python dev_server.py --api-port 8420 --ui-port 8421
"""

import argparse
import json
import sys
import threading
import time
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import parse_qs, urlparse

# Add scripts directory to path
SCRIPTS_DIR = Path(__file__).parent / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import uvicorn

from fetch_page import fetch_page
from parse_html import parse_html

app = FastAPI(
    title="Claude SEO Dev Server",
    description="Local development API for Claude SEO analysis tools",
    version="1.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "name": "Claude SEO Dev Server",
        "version": "1.1.0",
        "endpoints": {
            "/api/fetch": "Fetch a web page",
            "/api/analyze": "Fetch and analyze a page for SEO",
            "/api/parse": "Parse raw HTML for SEO elements",
            "/health": "Health check",
        },
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/api/fetch")
def api_fetch(url: str = Query(..., description="URL to fetch")):
    result = fetch_page(url)
    if result["error"]:
        raise HTTPException(status_code=502, detail=result["error"])
    result.pop("content", None)
    return result


@app.get("/api/analyze")
def api_analyze(url: str = Query(..., description="URL to analyze")):
    fetched = fetch_page(url)
    if fetched["error"]:
        raise HTTPException(status_code=502, detail=fetched["error"])

    seo_data = parse_html(fetched["content"], fetched["url"])

    return {
        "url": fetched["url"],
        "status_code": fetched["status_code"],
        "redirect_chain": fetched["redirect_chain"],
        "seo": seo_data,
    }


@app.post("/api/parse")
def api_parse(body: dict):
    html = body.get("html", "")
    base_url = body.get("base_url")
    if not html:
        raise HTTPException(status_code=400, detail="html field is required")
    return parse_html(html, base_url)


UI_HTML = """<!DOCTYPE html>
<html lang="cs">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Claude SEO - Dev Server</title>
  <style>
    :root {
      --bg: #0f1117;
      --surface: #1a1d27;
      --border: #2a2d3a;
      --text: #e4e4e7;
      --muted: #8b8d98;
      --accent: #c084fc;
      --accent2: #818cf8;
      --green: #4ade80;
      --red: #f87171;
      --yellow: #facc15;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'SF Mono', 'Cascadia Code', 'Fira Code', monospace;
      background: var(--bg);
      color: var(--text);
      min-height: 100vh;
    }
    .container { max-width: 960px; margin: 0 auto; padding: 2rem 1.5rem; }
    h1 {
      font-size: 1.5rem;
      font-weight: 600;
      margin-bottom: 0.25rem;
      background: linear-gradient(135deg, var(--accent), var(--accent2));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .subtitle { color: var(--muted); font-size: 0.85rem; margin-bottom: 2rem; }
    .input-row {
      display: flex;
      gap: 0.5rem;
      margin-bottom: 1.5rem;
    }
    input[type="url"] {
      flex: 1;
      padding: 0.75rem 1rem;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 8px;
      color: var(--text);
      font-family: inherit;
      font-size: 0.9rem;
      outline: none;
      transition: border-color 0.2s;
    }
    input[type="url"]:focus { border-color: var(--accent); }
    button {
      padding: 0.75rem 1.5rem;
      background: linear-gradient(135deg, var(--accent), var(--accent2));
      border: none;
      border-radius: 8px;
      color: #fff;
      font-family: inherit;
      font-size: 0.9rem;
      font-weight: 600;
      cursor: pointer;
      transition: opacity 0.2s;
    }
    button:hover { opacity: 0.85; }
    button:disabled { opacity: 0.4; cursor: not-allowed; }
    .status {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.3rem 0.7rem;
      border-radius: 999px;
      font-size: 0.75rem;
      font-weight: 600;
    }
    .status.ok { background: rgba(74,222,128,0.15); color: var(--green); }
    .status.err { background: rgba(248,113,113,0.15); color: var(--red); }
    .status.warn { background: rgba(250,204,21,0.15); color: var(--yellow); }
    .card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1.25rem;
      margin-bottom: 1rem;
    }
    .card h2 {
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--accent);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.75rem;
    }
    .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }
    @media (max-width: 640px) { .grid { grid-template-columns: 1fr; } }
    .field { margin-bottom: 0.6rem; }
    .field .label { font-size: 0.75rem; color: var(--muted); margin-bottom: 0.15rem; }
    .field .value { font-size: 0.85rem; word-break: break-all; }
    .field .value.missing { color: var(--red); font-style: italic; }
    .tag {
      display: inline-block;
      padding: 0.15rem 0.5rem;
      background: rgba(192,132,252,0.12);
      border-radius: 4px;
      font-size: 0.75rem;
      margin: 0.15rem 0.15rem 0 0;
    }
    .heading-list { list-style: none; padding: 0; }
    .heading-list li {
      padding: 0.3rem 0;
      border-bottom: 1px solid var(--border);
      font-size: 0.85rem;
    }
    .heading-list li:last-child { border: none; }
    .heading-list .htag {
      display: inline-block;
      width: 2rem;
      color: var(--accent);
      font-weight: 600;
    }
    .loader {
      display: none;
      width: 1.2rem;
      height: 1.2rem;
      border: 2px solid var(--border);
      border-top-color: var(--accent);
      border-radius: 50%;
      animation: spin 0.6s linear infinite;
      margin-left: 0.5rem;
    }
    .loader.active { display: inline-block; }
    @keyframes spin { to { transform: rotate(360deg); } }
    #results { display: none; }
    #error-msg {
      display: none;
      padding: 1rem;
      background: rgba(248,113,113,0.1);
      border: 1px solid rgba(248,113,113,0.3);
      border-radius: 8px;
      color: var(--red);
      margin-bottom: 1rem;
    }
    .img-table { width: 100%; font-size: 0.8rem; border-collapse: collapse; }
    .img-table th {
      text-align: left;
      padding: 0.4rem;
      border-bottom: 1px solid var(--border);
      color: var(--muted);
      font-weight: 500;
    }
    .img-table td {
      padding: 0.4rem;
      border-bottom: 1px solid var(--border);
      max-width: 300px;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }
    .schema-block {
      background: var(--bg);
      border-radius: 6px;
      padding: 0.75rem;
      font-size: 0.8rem;
      overflow-x: auto;
      margin-bottom: 0.5rem;
      white-space: pre-wrap;
      word-break: break-all;
    }
    .score-bar {
      height: 6px;
      border-radius: 3px;
      background: var(--border);
      margin-top: 0.3rem;
    }
    .score-bar .fill {
      height: 100%;
      border-radius: 3px;
      transition: width 0.6s ease;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Claude SEO</h1>
    <p class="subtitle">Local Dev Server &mdash; SEO Analysis API</p>

    <div class="input-row">
      <input type="url" id="url-input" placeholder="https://example.com" autofocus>
      <button id="analyze-btn" onclick="analyze()">Analyze <span class="loader" id="loader"></span></button>
    </div>

    <div id="error-msg"></div>

    <div id="results">
      <div class="grid">
        <div class="card">
          <h2>Page Info</h2>
          <div class="field"><div class="label">Title</div><div class="value" id="r-title"></div></div>
          <div class="field"><div class="label">Meta Description</div><div class="value" id="r-desc"></div></div>
          <div class="field"><div class="label">Canonical</div><div class="value" id="r-canonical"></div></div>
          <div class="field"><div class="label">Robots</div><div class="value" id="r-robots"></div></div>
          <div class="field"><div class="label">Word Count</div><div class="value" id="r-words"></div></div>
        </div>
        <div class="card">
          <h2>Technical</h2>
          <div class="field"><div class="label">Status Code</div><div class="value" id="r-status"></div></div>
          <div class="field"><div class="label">Final URL</div><div class="value" id="r-url"></div></div>
          <div class="field"><div class="label">Redirects</div><div class="value" id="r-redirects"></div></div>
          <div class="field"><div class="label">Internal Links</div><div class="value" id="r-internal"></div></div>
          <div class="field"><div class="label">External Links</div><div class="value" id="r-external"></div></div>
        </div>
      </div>

      <div class="card">
        <h2>SEO Quick Score</h2>
        <div class="grid">
          <div>
            <div class="field"><div class="label">Title Length</div><div class="value" id="r-title-len"></div><div class="score-bar"><div class="fill" id="bar-title"></div></div></div>
            <div class="field"><div class="label">Description Length</div><div class="value" id="r-desc-len"></div><div class="score-bar"><div class="fill" id="bar-desc"></div></div></div>
          </div>
          <div>
            <div class="field"><div class="label">H1 Tags</div><div class="value" id="r-h1-count"></div></div>
            <div class="field"><div class="label">Images w/o Alt</div><div class="value" id="r-noalt"></div></div>
          </div>
        </div>
      </div>

      <div class="card">
        <h2>Headings</h2>
        <ul class="heading-list" id="r-headings"></ul>
      </div>

      <div class="grid">
        <div class="card">
          <h2>Open Graph</h2>
          <div id="r-og"></div>
        </div>
        <div class="card">
          <h2>Twitter Card</h2>
          <div id="r-twitter"></div>
        </div>
      </div>

      <div class="card" id="schema-card" style="display:none">
        <h2>Schema Markup (JSON-LD)</h2>
        <div id="r-schema"></div>
      </div>

      <div class="card" id="hreflang-card" style="display:none">
        <h2>Hreflang</h2>
        <div id="r-hreflang"></div>
      </div>

      <div class="card" id="images-card" style="display:none">
        <h2>Images</h2>
        <div style="overflow-x:auto"><table class="img-table" id="r-images"></table></div>
      </div>
    </div>
  </div>

  <script>
    const API = 'API_PORT_PLACEHOLDER';
    const input = document.getElementById('url-input');
    input.addEventListener('keydown', e => { if (e.key === 'Enter') analyze(); });

    async function analyze() {
      const url = input.value.trim();
      if (!url) return;

      const btn = document.getElementById('analyze-btn');
      const loader = document.getElementById('loader');
      const errEl = document.getElementById('error-msg');
      const results = document.getElementById('results');

      btn.disabled = true;
      loader.classList.add('active');
      errEl.style.display = 'none';
      results.style.display = 'none';

      try {
        const res = await fetch(`http://127.0.0.1:${API}/api/analyze?url=${encodeURIComponent(url)}`);
        if (!res.ok) {
          const err = await res.json();
          throw new Error(err.detail || res.statusText);
        }
        const data = await res.json();
        render(data);
        results.style.display = 'block';
      } catch (e) {
        errEl.textContent = e.message;
        errEl.style.display = 'block';
      } finally {
        btn.disabled = false;
        loader.classList.remove('active');
      }
    }

    function setVal(id, val, cls) {
      const el = document.getElementById(id);
      if (val === null || val === undefined || val === '') {
        el.textContent = 'missing';
        el.className = 'value missing';
      } else {
        el.textContent = val;
        el.className = 'value' + (cls ? ' ' + cls : '');
      }
    }

    function scoreBar(id, val, min, max) {
      const el = document.getElementById(id);
      const pct = Math.max(0, Math.min(100, ((val - min) / (max - min)) * 100));
      el.style.width = pct + '%';
      el.style.background = pct > 70 ? 'var(--green)' : pct > 40 ? 'var(--yellow)' : 'var(--red)';
    }

    function render(data) {
      const s = data.seo;
      setVal('r-title', s.title);
      setVal('r-desc', s.meta_description);
      setVal('r-canonical', s.canonical);
      setVal('r-robots', s.meta_robots || 'not set');
      setVal('r-words', s.word_count);
      setVal('r-status', data.status_code);
      setVal('r-url', data.url);
      setVal('r-redirects', data.redirect_chain.length ? data.redirect_chain.join(' → ') : 'none');
      setVal('r-internal', s.links.internal.length);
      setVal('r-external', s.links.external.length);

      const tLen = (s.title || '').length;
      setVal('r-title-len', `${tLen} chars ${tLen >= 50 && tLen <= 60 ? '✓' : tLen < 50 ? '(too short)' : '(too long)'}`);
      scoreBar('bar-title', tLen, 0, 70);

      const dLen = (s.meta_description || '').length;
      setVal('r-desc-len', `${dLen} chars ${dLen >= 150 && dLen <= 160 ? '✓' : dLen < 150 ? '(too short)' : '(too long)'}`);
      scoreBar('bar-desc', dLen, 0, 170);

      setVal('r-h1-count', s.h1.length === 1 ? '1 ✓' : `${s.h1.length} ${s.h1.length === 0 ? '(missing!)' : '(multiple!)'}`);
      const noAlt = s.images.filter(i => !i.alt).length;
      setVal('r-noalt', `${noAlt} / ${s.images.length}${noAlt > 0 ? ' ⚠' : ' ✓'}`);

      // Headings
      const hList = document.getElementById('r-headings');
      hList.innerHTML = '';
      for (const tag of ['h1', 'h2', 'h3']) {
        for (const text of s[tag]) {
          hList.innerHTML += `<li><span class="htag">${tag}</span> ${esc(text)}</li>`;
        }
      }
      if (!hList.innerHTML) hList.innerHTML = '<li style="color:var(--muted)">No headings found</li>';

      // OG
      const ogEl = document.getElementById('r-og');
      ogEl.innerHTML = '';
      for (const [k, v] of Object.entries(s.open_graph)) {
        ogEl.innerHTML += `<div class="field"><div class="label">${esc(k)}</div><div class="value">${esc(v)}</div></div>`;
      }
      if (!ogEl.innerHTML) ogEl.innerHTML = '<div class="value missing">No Open Graph tags</div>';

      // Twitter
      const twEl = document.getElementById('r-twitter');
      twEl.innerHTML = '';
      for (const [k, v] of Object.entries(s.twitter_card)) {
        twEl.innerHTML += `<div class="field"><div class="label">${esc(k)}</div><div class="value">${esc(v)}</div></div>`;
      }
      if (!twEl.innerHTML) twEl.innerHTML = '<div class="value missing">No Twitter Card tags</div>';

      // Schema
      const schemaCard = document.getElementById('schema-card');
      const schemaEl = document.getElementById('r-schema');
      if (s.schema.length) {
        schemaCard.style.display = 'block';
        schemaEl.innerHTML = s.schema.map(sc => `<div class="schema-block">${esc(JSON.stringify(sc, null, 2))}</div>`).join('');
      } else {
        schemaCard.style.display = 'none';
      }

      // Hreflang
      const hlCard = document.getElementById('hreflang-card');
      const hlEl = document.getElementById('r-hreflang');
      if (s.hreflang.length) {
        hlCard.style.display = 'block';
        hlEl.innerHTML = s.hreflang.map(h => `<span class="tag">${esc(h.lang)}: ${esc(h.href)}</span>`).join('');
      } else {
        hlCard.style.display = 'none';
      }

      // Images
      const imgCard = document.getElementById('images-card');
      const imgEl = document.getElementById('r-images');
      if (s.images.length) {
        imgCard.style.display = 'block';
        let html = '<tr><th>Src</th><th>Alt</th><th>Size</th><th>Loading</th></tr>';
        for (const img of s.images.slice(0, 30)) {
          const alt = img.alt ? esc(img.alt) : '<span style="color:var(--red)">missing</span>';
          const size = img.width && img.height ? `${img.width}×${img.height}` : '-';
          html += `<tr><td>${esc(img.src || '-')}</td><td>${alt}</td><td>${size}</td><td>${img.loading || '-'}</td></tr>`;
        }
        if (s.images.length > 30) html += `<tr><td colspan="4" style="color:var(--muted)">... and ${s.images.length - 30} more</td></tr>`;
        imgEl.innerHTML = html;
      } else {
        imgCard.style.display = 'none';
      }
    }

    function esc(s) {
      const d = document.createElement('div');
      d.textContent = s;
      return d.innerHTML;
    }
  </script>
</body>
</html>"""


def get_ui_html(api_port: int) -> str:
    return UI_HTML.replace("API_PORT_PLACEHOLDER", str(api_port))


def run_ui_server(port: int, api_port: int):
    """Simple HTTP server that serves the UI HTML."""

    class UIHandler(SimpleHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(get_ui_html(api_port).encode("utf-8"))

        def log_message(self, format, *args):
            pass  # Suppress logs

    server = HTTPServer(("127.0.0.1", port), UIHandler)
    server.serve_forever()


def main():
    parser = argparse.ArgumentParser(description="Claude SEO Dev Server")
    parser.add_argument("--api-port", type=int, default=8420, help="API port (default: 8420)")
    parser.add_argument("--ui-port", type=int, default=8421, help="UI port (default: 8421)")
    args = parser.parse_args()

    # Start UI server in background thread
    ui_thread = threading.Thread(
        target=run_ui_server,
        args=(args.ui_port, args.api_port),
        daemon=True,
    )
    ui_thread.start()

    print(f"\n  Claude SEO Dev Server v1.1.0")
    print(f"  ────────────────────────────")
    print(f"  API:  http://127.0.0.1:{args.api_port}")
    print(f"  UI:   http://127.0.0.1:{args.ui_port}")
    print(f"  Docs: http://127.0.0.1:{args.api_port}/docs")
    print(f"\n  Press Ctrl+C to stop\n")

    uvicorn.run(app, host="127.0.0.1", port=args.api_port, log_level="info")


if __name__ == "__main__":
    main()
