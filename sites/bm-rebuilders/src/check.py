from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlsplit
import re
from data import PREVIEW_SUBSCRIBE_URL
root=Path(__file__).resolve().parent.parent; site=root/'site'; errors=[]
pages=list(site.rglob('*.html'))
for p in pages:
 s=BeautifulSoup(p.read_text(),'html.parser')
 if len(s.find_all('h1'))!=1: errors.append(f'{p}: h1 count')
 for img in s.find_all('img'):
  if any(not img.has_attr(x) for x in ('alt','width','height')): errors.append(f'{p}: image attributes')
 for tag in s.find_all(['a','link','script','img']):
  u=tag.get('href') or tag.get('src') or ''
  if u.startswith(('http:','https:','//')) and u!=PREVIEW_SUBSCRIBE_URL: errors.append(f'{p}: external URL {u}')
  if u.startswith('/') and not u.startswith('//'):
   path=urlsplit(u).path; target=site/path.lstrip('/')
   if target.is_dir(): target=target/'index.html'
   if not target.exists(): errors.append(f'{p}: missing {u}')
redirects=(site/'_redirects').read_text().splitlines(); mapping={}
for line in redirects:
 parts=line.split()
 if len(parts)!=3 or parts[2]!='301' or parts[0]==parts[1]: errors.append(f'bad redirect: {line}')
 else: mapping[parts[0]]=parts[1]
for line in (root/'src/assets/pages.tsv').read_text().splitlines()[1:]:
 old=line.split('\t')[0]
 if old!='/' and old not in mapping: errors.append(f'missing redirect: {old}')
for f,limit in [('assets/css/site.css',25000),('assets/js/site.js',6000)]:
 p=site/f
 if p.stat().st_size>limit: errors.append(f'{f}: too large')
 if re.search(r'https?://|//[^/]',p.read_text()): errors.append(f'{f}: external reference')
# Preview subscribe button: one per page while PREVIEW_SUBSCRIBE_URL is set, none once it is ''.
from html import escape as _escape
for _f in (Path(__file__).resolve().parent.parent/'site').rglob('*.html'):
 _h=_f.read_text(); _n=_h.count('class="preview-subscribe"')
 if _n!=(1 if PREVIEW_SUBSCRIBE_URL else 0): errors.append(f'{_f}: {_n} preview subscribe buttons')
 elif PREVIEW_SUBSCRIBE_URL and f'href="{_escape(PREVIEW_SUBSCRIBE_URL)}" target="_blank" rel="noopener"' not in _h: errors.append(f'{_f}: preview subscribe link')
print(f'{len(pages)} HTML pages checked; {len(redirects)} redirects checked; CSS { (site/"assets/css/site.css").stat().st_size} bytes; JS {(site/"assets/js/site.js").stat().st_size} bytes.')
print('\n'.join(errors) if errors else 'All checks passed.')
raise SystemExit(bool(errors))
