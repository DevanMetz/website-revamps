from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
import csv,re
root=Path(__file__).resolve().parent.parent; site=root/'site'; errors=[]
class Check(HTMLParser):
 def __init__(self,p): super().__init__(); self.p=p; self.h1=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='h1': self.h1+=1
  if tag=='img' and not all(k in a for k in ('alt','width','height')): errors.append(f'{self.p}: incomplete image')
  for k in ('href','src'):
   v=a.get(k,''); u=urlsplit(v)
   if u.scheme in ('http','https') and tag not in ('a',): errors.append(f'{self.p}: external request {v}')
   if v.startswith('/') and not v.startswith('//'):
    target=site/u.path.lstrip('/'); target=target/'index.html' if u.path.endswith('/') else target
    if not target.is_file(): errors.append(f'{self.p}: missing {v}')
for p in site.rglob('*.html'):
 html=p.read_text()
 for pattern in (r'\+\s*img\s*\(', r'\{\{', r'[\"\']\s*\+\s*(?:[\"\']|[a-zA-Z_]\w*\s*\()', r'\+\s*[\"\']'):
  if re.search(pattern, html): errors.append(f'{p}: leaked template code ({pattern})')
 c=Check(p); c.feed(html);
 if c.h1!=1: errors.append(f'{p}: {c.h1} h1s')
css=(site/'assets/css/site.css').read_text(); js=(site/'assets/js/site.js').read_text()
if re.search(r'url\(["\']?https?://|@import',css): errors.append('external CSS request')
if len(css.encode())>25000 or len(js.encode())>6000: errors.append('asset size exceeded')
redirects={}
for line in (site/'_redirects').read_text().splitlines():
 parts=line.split()
 if len(parts)!=3 or parts[2]!='301' or parts[0]==parts[1]: errors.append('bad redirect: '+line)
 else: redirects[parts[0]]=parts[1]
with (root/'src/assets/pages.tsv').open() as f:
 for row in csv.DictReader(f,delimiter='\t'):
  if row['old_path']!='/' and row['old_path'] not in redirects: errors.append('missing redirect '+row['old_path'])
print(f'Checked {len(list(site.rglob("*.html")))} HTML pages; CSS {len(css.encode())} bytes; JS {len(js.encode())} bytes.')
print('\n'.join(errors) if errors else 'All static checks passed.')
raise SystemExit(bool(errors))
