from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import csv,re
root=Path(__file__).resolve().parent.parent; site=root/'site'; errors=[]
class Check(HTMLParser):
 def __init__(self,path): super().__init__(); self.path=path; self.h1=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='h1': self.h1+=1
  if tag=='img':
   for k in ('alt','width','height'):
    if k not in a: errors.append(f'{self.path}: image missing {k}')
  for k in ('href','src'):
   v=a.get(k,'')
   if not v or v.startswith(('#','mailto:','tel:','data:')): continue
   if v.startswith(('http:','https:','//')): errors.append(f'{self.path}: external {k} {v}'); continue
   p=unquote(urlsplit(v).path)
   target=site/p.lstrip('/') if p.startswith('/') else self.path.parent/p
   if target.is_dir(): target=target/'index.html'
   if not target.is_file(): errors.append(f'{self.path}: missing {v}')
pages=list(site.rglob('*.html'))
for p in pages:
 c=Check(p); c.feed(p.read_text());
 if c.h1!=1: errors.append(f'{p}: {c.h1} h1 elements')
css=(site/'assets/css/site.css').read_text()
if re.search(r'url\(["\']?(?:https?:)?//',css): errors.append('external CSS request')
redirects={}
for line in (site/'_redirects').read_text().splitlines():
 parts=line.split()
 if len(parts)!=3 or parts[2]!='301' or not parts[0].startswith('/') or not parts[1].startswith('/') or parts[0]==parts[1]: errors.append('bad redirect: '+line)
 else: redirects[parts[0]]=parts[1]
with (root/'reference/pages.tsv').open() as f:
 for row in csv.DictReader(f,delimiter='\t'):
  if row['old_path']!='/' and row['old_path'] not in redirects: errors.append('missing redirect '+row['old_path'])
for p,limit in [('assets/css/site.css',25600),('assets/js/site.js',6144)]:
 size=(site/p).stat().st_size
 if size>limit: errors.append(f'{p} too large: {size}')
print(f'{len(pages)} HTML pages checked; {len(redirects)} redirects; CSS {(site/"assets/css/site.css").stat().st_size} bytes; JS {(site/"assets/js/site.js").stat().st_size} bytes')
print('\n'.join(errors) if errors else 'All static checks passed.')
raise SystemExit(bool(errors))
