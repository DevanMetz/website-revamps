from pathlib import Path
from urllib.parse import urlparse,unquote
from bs4 import BeautifulSoup
import csv,re
root=Path(__file__).resolve().parent.parent; site=root/'site'; errors=[]; pages=list(site.rglob('*.html'))
for p in pages:
 html=p.read_text()
 if re.search(r'</a><(?:a|button)\b', html): errors.append(f'{p}: adjacent actions lack whitespace')
 s=BeautifulSoup(html,'html.parser')
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
with (root/'src/assets/pages.tsv').open() as f:
 for row in csv.DictReader(f,delimiter='\t'):
  if row['old_path']!='/' and row['old_path'] not in redirects: errors.append('missing redirect '+row['old_path'])
css=(site/'assets/css/site.css').read_text();js=(site/'assets/js/site.js').read_text()
if re.search(r'url\(["\']?(?:https?:)?//|@import',css): errors.append('external CSS request')
if len(css.encode())>25000 or len(js.encode())>6000: errors.append('asset size limit')
# Preview subscribe button: one per page while PREVIEW_SUBSCRIBE_URL is set, none once it is ''.
from data import PREVIEW_SUBSCRIBE_URL, STRIPE_PORTAL_URL
from keep import KEEP_CODE_URL
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
  if _h.count('href="'+_escape(STRIPE_PORTAL_URL)+'"')!=1 or '<a href="'+_escape(STRIPE_PORTAL_URL)+'" target="_blank" rel="noopener" aria-label="Manage or cancel your subscription (opens in a new tab)">Manage or cancel your subscription here</a>' not in _h: errors.append('/keep/: Stripe portal link missing')
  if _h.count('target="_blank"')!=2: errors.append('/keep/: only the code and portal links may open a new tab')
elif _keep.parent.exists(): errors.append('/keep/ built while PREVIEW_SUBSCRIBE_URL is empty')
for _x in ('sitemap.xml',):
 if (_keep.parent.parent/_x).exists() and '/keep/' in (_keep.parent.parent/_x).read_text(): errors.append('/keep/ in sitemap')
print(f'{len(pages)} HTML pages checked; {len(redirects)} redirects; CSS {len(css.encode())} bytes; JS {len(js.encode())} bytes.')
print('\n'.join(errors) if errors else 'All static checks passed.')
raise SystemExit(bool(errors))
