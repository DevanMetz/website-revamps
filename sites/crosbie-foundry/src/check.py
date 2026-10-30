from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlsplit, unquote
import re
root=Path(__file__).resolve().parents[1]; site=root/'site'; errors=[]
pages=list(site.rglob('*.html'))
for p in pages:
 s=BeautifulSoup(p.read_text(),'html.parser')
 if len(s.find_all('h1'))!=1: errors.append(f'{p}: h1 count')
 for im in s.find_all('img'):
  if any(not im.has_attr(a) for a in ('alt','width','height')): errors.append(f'{p}: image attributes')
 for tag in s.find_all(['a','img','script','link']):
  value=tag.get('href') or tag.get('src')
  if not value or value.startswith(('#','mailto:','tel:')): continue
  if value.startswith(('http:','https:','//')): errors.append(f'{p}: external resource {value}'); continue
  path=unquote(urlsplit(value).path)
  dest=site/path.lstrip('/') if path.startswith('/') else p.parent/path
  if dest.is_dir(): dest=dest/'index.html'
  if not dest.exists(): errors.append(f'{p}: missing {value}')
css=(site/'assets/css/site.css').read_text()
if re.search(r'url\([\'"]?(?:https?:)?//|@import',css): errors.append('external CSS request')
redirects={}
for line in (site/'_redirects').read_text().splitlines():
 parts=line.split()
 if len(parts)!=3 or parts[2]!='301' or not parts[0].startswith('/') or not parts[1].startswith('/') or parts[0]==parts[1]: errors.append('invalid redirect: '+line)
 else: redirects[parts[0]]=parts[1]
for line in (root/'reference/pages.tsv').read_text().splitlines()[1:]:
 old=line.split('\t')[0]
 if old!='/' and old not in redirects: errors.append('missing redirect '+old)
for dest in redirects.values():
 if not (site/dest.lstrip('/')/'index.html').exists(): errors.append('missing redirect target '+dest)
for file,limit in [('assets/css/site.css',25000),('assets/js/site.js',6000)]:
 size=(site/file).stat().st_size
 print(f'{file}: {size} bytes')
 if size>limit: errors.append(file+' too large')
print(f'{len(pages)} HTML pages checked; {len(redirects)} redirects checked; {len(errors)} errors')
for e in errors: print('ERROR:',e)
raise SystemExit(bool(errors))
