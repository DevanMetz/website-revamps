from pathlib import Path
from urllib.parse import urlparse,unquote
from bs4 import BeautifulSoup
import csv,re
root=Path(__file__).resolve().parent.parent; site=root/'site'; errors=[]; pages=list(site.rglob('*.html'))
for p in pages:
 s=BeautifulSoup(p.read_text(),'html.parser')
 if len(s.find_all('h1'))!=1: errors.append(f'{p}: h1 count')
 for im in s.find_all('img'):
  if any(not im.has_attr(x) for x in ['alt','width','height']): errors.append(f'{p}: image attributes')
 for el in s.select('[href], [src]'):
  u=el.get('href') or el.get('src'); parsed=urlparse(u)
  if parsed.scheme or u.startswith('#'): continue
  target=site/unquote(parsed.path).lstrip('/') if u.startswith('/') else p.parent/unquote(parsed.path)
  if target.is_dir(): target=target/'index.html'
  if not target.exists(): errors.append(f'{p}: missing {u}')
 for el in s.select('script[src], link[rel="stylesheet"], img[src]'):
  if (el.get('src') or el.get('href','')).startswith(('http:','https:','//')): errors.append(f'{p}: external request')
redirects={}
for line in (site/'_redirects').read_text().splitlines():
 bits=line.split()
 if len(bits)!=3 or bits[2]!='301' or bits[0]==bits[1]: errors.append('bad redirect: '+line)
 else: redirects[bits[0]]=bits[1]
with (root/'reference/pages.tsv').open() as f:
 for row in csv.DictReader(f,delimiter='\t'):
  if row['old_path']!='/' and row['old_path'] not in redirects: errors.append('missing redirect '+row['old_path'])
css=(site/'assets/css/site.css').read_text();js=(site/'assets/js/site.js').read_text()
if re.search(r'url\(["\']?(?:https?:)?//|@import',css): errors.append('external CSS request')
if len(css.encode())>25000 or len(js.encode())>6000: errors.append('asset size limit')
print(f'{len(pages)} HTML pages checked; {len(redirects)} redirects; CSS {len(css.encode())} bytes; JS {len(js.encode())} bytes.')
print('\n'.join(errors) if errors else 'All static checks passed.')
raise SystemExit(bool(errors))
