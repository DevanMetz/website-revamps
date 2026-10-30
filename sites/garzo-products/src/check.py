from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import re
root=Path('site'); errors=[]
class Check(HTMLParser):
 def __init__(self,file): super().__init__(); self.file=file; self.h=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='h1': self.h+=1
  if tag=='img' and not all(k in a for k in ('alt','width','height')): errors.append(f'{self.file}: incomplete image')
  for key in ('href','src'):
   v=a.get(key,''); u=urlsplit(v)
   if u.scheme in ('http','https') and tag not in ('meta',): errors.append(f'{self.file}: external {v}')
   if v.startswith('/') and not v.startswith('//'):
    p=root/unquote(u.path.lstrip('/')); p=p/'index.html' if u.path.endswith('/') else p
    if not p.is_file(): errors.append(f'{self.file}: missing {v}')
for f in root.rglob('*.html'):
 c=Check(f); c.feed(f.read_text());
 if c.h!=1: errors.append(f'{f}: {c.h} h1s')
css=(root/'assets/css/site.css').read_text(); js=(root/'assets/js/site.js').read_text()
if re.search(r'url\(["\']?https?://|@import',css): errors.append('External CSS request')
if len(css.encode())>25600 or len(js.encode())>6144: errors.append('Asset size exceeded')
redirects={}
for line in (root/'_redirects').read_text().splitlines():
 parts=line.split()
 if len(parts)!=3 or parts[2]!='301' or parts[0]==parts[1]: errors.append('Invalid redirect: '+line)
 else: redirects[parts[0]]=parts[1]
for line in Path('src/assets/pages.tsv').read_text().splitlines()[1:]:
 p=line.split('\t')[0]
 if p!='/' and p not in redirects: errors.append('Missing redirect: '+p)
print(f'{len(list(root.rglob("*.html")))} HTML pages; CSS {len(css.encode())} bytes; JS {len(js.encode())} bytes; {len(redirects)} redirects')
print('\n'.join(errors) if errors else 'All static checks passed.')
raise SystemExit(bool(errors))
