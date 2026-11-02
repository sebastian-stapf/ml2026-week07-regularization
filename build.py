#!/usr/bin/env python3
"""Build index.html: inline the shared CSS/JS into the page so the site is one self-contained HTML file.

Usage:
  python3 build.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"

# Links to the week's own site and the companion lab, which lives in its own repository
W06_URL = "https://sebastian-stapf.github.io/ml2026-week06-deep-learning/"
W07_URL = "./"
HOME_URL = "./"

css = (SRC / "lab.css").read_text()
js = (SRC / "lab.js").read_text()
page = (SRC / "page.src.html").read_text()
page = page.replace("<!-- @inline lab.css -->", f"<style>\n{css}\n</style>")
page = page.replace("<!-- @inline lab.js -->", f"<script>\n{js}\n</script>")
page = page.replace("{{W06_URL}}", W06_URL).replace("{{W07_URL}}", W07_URL).replace("{{HOME_URL}}", HOME_URL)
(ROOT / "index.html").write_text(page)
print(f"wrote index.html ({len(page) // 1024} KB)")
