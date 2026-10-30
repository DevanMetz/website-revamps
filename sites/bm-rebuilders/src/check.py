from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlsplit
import re
from data import PREVIEW_SUBSCRIBE_URL
from keep import KEEP_CODE_URL
root=Path(__file__).resolve().parent.parent; site=root/'site'; errors=[]
pages=list(site.rglob('*.html'))
for p in pages:
 s=BeautifulSoup(p.read_text(),'html.parser')
 if len(s.find_all('h1'))!=1: errors.append(f'{p}: h1 count')
 for img in s.find_all('img'):
  if any(not img.has_attr(x) for x in ('alt','width','height')): errors.append(f'{p}: image attributes')
 for tag in s.find_all(['a','link','script','img']):
  u=tag.get('href') or tag.get('src') or ''
  if u.startswith(('http:','https:','//')) and u not in (PREVIEW_SUBSCRIBE_URL,KEEP_CODE_URL): errors.append(f'{p}: external URL {u}')
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
# /keep/ funnel: exists with the exact Stripe link while PREVIEW_SUBSCRIBE_URL is set, absent once it is ''.
from keep import KEEP_CODE_URL as _code
_keep=Path(__file__).resolve().parent.parent/'site'/'keep'/'index.html'
for _f in (Path(__file__).resolve().parent.parent/'site').rglob('*.html'):
 _h=_f.read_text(); _n=_h.count('class="preview-subscribe"')
 if _f==_keep:
  if _n: errors.append(f'{_f}: preview subscribe button on /keep/')
  continue
 if _n!=(1 if PREVIEW_SUBSCRIBE_URL else 0): errors.append(f'{_f}: {_n} preview subscribe buttons')
 elif PREVIEW_SUBSCRIBE_URL and '<a class="preview-subscribe" href="/keep/" aria-label="Upgrade my website: see how to switch to this new site">Upgrade my website</a>' not in _h: errors.append(f'{_f}: preview subscribe link')
if PREVIEW_SUBSCRIBE_URL:
 if not _keep.exists(): errors.append('/keep/ missing')
 else:
  _h=_keep.read_text()
  if _h.count('<a class="button" href="'+_escape(PREVIEW_SUBSCRIBE_URL)+'">Continue to checkout · $20/mo</a>')!=1 or _h.count('buy.stripe.com')!=1: errors.append('/keep/: checkout link')
  if _h.count('href="'+_escape(_code)+'"')!=1 or '<a href="'+_escape(_code)+'" target="_blank" rel="noopener" aria-label="Get the code (opens in a new tab)">Get the code</a>' not in _h: errors.append('/keep/: code link must open in a new tab')
  if '<meta name="robots" content="noindex">' not in _h: errors.append('/keep/: noindex')
  if _h.count('class="keep-step"')!=4 or 'Cancel your old hosting' not in _h: errors.append('/keep/: 4 steps')
  if _h.count('target="_blank"')!=1: errors.append('/keep/: only the code link may open a new tab')
elif _keep.parent.exists(): errors.append('/keep/ built while PREVIEW_SUBSCRIBE_URL is empty')
for _x in ('sitemap.xml',):
 if (_keep.parent.parent/_x).exists() and '/keep/' in (_keep.parent.parent/_x).read_text(): errors.append('/keep/ in sitemap')
print(f'{len(pages)} HTML pages checked; {len(redirects)} redirects checked; CSS { (site/"assets/css/site.css").stat().st_size} bytes; JS {(site/"assets/js/site.js").stat().st_size} bytes.')
print('\n'.join(errors) if errors else 'All checks passed.')
raise SystemExit(bool(errors))
