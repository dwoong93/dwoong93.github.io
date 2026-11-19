#!/usr/bin/env python3
"""Build the GitHub Pages version of the portfolio from the Claude artifact export.

Usage:  python3 tools/build.py <artifact-export.html>

What it does (and why):
  1. Pulls every embedded image (data: URIs) out into images/ and links to the files instead.
     LinkedIn refuses to read pages over 3 MB; the artifact export is ~4.5 MB because images are inlined.
  2. Wraps the page in a full HTML document with title, description and link-preview (Open Graph) tags,
     plus the base styles the Claude artifact host normally adds.
  3. Appends the GoatCounter visitor-stats script (GitHub version only).
Each step prints what it did, so problems are easy to trace.
"""
import base64, hashlib, os, re, sys

src = sys.argv[1]
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
img_dir = os.path.join(root, 'images')
os.makedirs(img_dir, exist_ok=True)
s = open(src, encoding='utf-8').read()
print(f'[build] read {src}: {len(s)/1e6:.2f} MB')

ext = {'jpeg': 'jpg', 'jpg': 'jpg', 'png': 'png', 'gif': 'gif', 'webp': 'webp'}
seen = {}
def save(m):
    kind, data = m.group(1), m.group(2)
    raw = base64.b64decode(data)
    name = hashlib.sha1(raw).hexdigest()[:12] + '.' + ext.get(kind, kind)
    if name not in seen:
        open(os.path.join(img_dir, name), 'wb').write(raw)
        seen[name] = len(raw)
    return 'images/' + name
s = re.sub(r'data:image/([a-z]+);base64,([A-Za-z0-9+/=]+)', save, s)
print(f'[build] extracted {len(seen)} images ({sum(seen.values())/1e6:.2f} MB) into images/')
# keep removed files tidy: delete images no longer referenced
for f in os.listdir(img_dir):
    if f not in seen:
        os.remove(os.path.join(img_dir, f)); print(f'[build] removed unused images/{f}')
# lazy-load images that don't already say how to load
s = re.sub(r'<img (?![^>]*loading=)', '<img loading="lazy" ', s)

head = open(os.path.join(root, 'tools', 'head.html'), encoding='utf-8').read()
tail = open(os.path.join(root, 'tools', 'tail.html'), encoding='utf-8').read()
out = head + s.rstrip() + '\n' + tail
open(os.path.join(root, 'index.html'), 'w', encoding='utf-8').write(out)
print(f'[build] wrote index.html: {len(out)/1e6:.2f} MB (LinkedIn limit 3.15 MB)')
