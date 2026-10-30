from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import re
root=Path(__file__).resolve().parent.parent; site=root/'site'; errors=[]
class Check(HTMLParser):
 def __init__(self,path): super().__init__(); self.path=path; self.h1=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='h1': self.h1+=1
  if tag=='img' and any(k not in a for k in ('alt','width','height')): errors.append(f'{self.path}: incomplete image')
  for k in ('href','src'):
   v=a.get(k,''); u=urlsplit(v)
   if u.scheme in ('http','https') and tag not in ('a',): errors.append(f'{self.path}: external resource {v}')
   if v.startswith('/') and not v.startswith('//'):
    p=site/unquote(u.path).lstrip('/'); p=p/'index.html' if u.path.endswith('/') else p
    if not p.is_file(): errors.append(f'{self.path}: missing {v}')
for p in site.rglob('*.html'):
 c=Check(p); c.feed(p.read_text());
 if c.h1!=1: errors.append(f'{p}: {c.h1} h1s')
redirects={}
for line in (site/'_redirects').read_text().splitlines():
 parts=line.split()
 if len(parts)!=3 or parts[2]!='301' or not parts[0].startswith('/') or not parts[1].startswith('/') or parts[0]==parts[1]: errors.append('Bad redirect: '+line)
 else: redirects[parts[0]]=parts[1]
for line in (root/'src/assets/pages.tsv').read_text().splitlines()[1:]:
 p=line.split('\t')[0]
 if p!='/' and p not in redirects: errors.append('Missing redirect '+p)
if '/docs/catalog.pdf' not in redirects: errors.append('Missing PDF redirect')
css=(site/'assets/css/site.css').read_text(); js=(site/'assets/js/site.js').read_text()
if re.search(r'url\(["\']?https?://|@import',css): errors.append('External CSS resource')
if len(css.encode())>25000 or len(js.encode())>6000: errors.append('Asset too large')
print(f'{len(list(site.rglob("*.html")))} HTML pages checked; CSS {len(css.encode())} bytes; JS {len(js.encode())} bytes; {len(redirects)} redirects checked.')
print('\n'.join(errors) if errors else 'All static checks passed.')
raise SystemExit(bool(errors))
