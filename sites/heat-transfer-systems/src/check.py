from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote,urlsplit
import re
root=Path(__file__).resolve().parents[1]; site=root/'site'; errors=[]
class Check(HTMLParser):
 def __init__(self,p): super().__init__(); self.p=p; self.h1=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='h1': self.h1+=1
  if tag=='img' and any(k not in a for k in ('alt','width','height')): errors.append(f'{self.p}: incomplete image')
  for k in ('href','src'):
   v=a.get(k,''); u=urlsplit(v)
   if tag in ('script','img','link') and u.scheme in ('http','https'): errors.append(f'{self.p}: external resource {v}')
   if v.startswith('/') and not v.startswith('//'):
    path=site/unquote(u.path).lstrip('/'); path=path/'index.html' if u.path.endswith('/') else path
    if not path.is_file(): errors.append(f'{self.p}: missing {v}')
for p in site.rglob('*.html'):
 c=Check(p); c.feed(p.read_text());
 if c.h1!=1: errors.append(f'{p}: {c.h1} h1s')
css=(site/'assets/css/site.css').read_text(); js=(site/'assets/js/site.js').read_text()
if re.search(r'url\(["\']?https?://|@import',css): errors.append('external CSS resource')
redirects=(site/'_redirects').read_text().splitlines(); mapping={}
for line in redirects:
 parts=line.split()
 if len(parts)!=3 or parts[2]!='301' or not parts[0].startswith('/') or not parts[1].startswith('/') or parts[0]==parts[1]: errors.append('bad redirect: '+line)
 else: mapping[parts[0]]=parts[1]
for line in (root/'src/assets/pages.tsv').read_text().splitlines()[1:]:
 path=line.split('\t')[0]
 if path!='/' and path not in mapping: errors.append('missing redirect '+path)
for name,content,limit in [('CSS',css,25000),('JS',js,6000)]:
 if len(content.encode())>limit: errors.append(name+' exceeds size limit')
print(f'{len(list(site.rglob("*.html")))} HTML pages checked; CSS {len(css.encode())} bytes; JS {len(js.encode())} bytes')
print('\n'.join(errors) if errors else 'All static checks passed.')
raise SystemExit(bool(errors))
