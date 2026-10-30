from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import re, sys
root=Path(__file__).resolve().parents[1]; site=root/'site'; errors=[]
class Check(HTMLParser):
 def __init__(self,path): super().__init__(); self.path=path; self.h=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='h1': self.h+=1
  if tag=='img' and not all(k in a for k in ('alt','width','height')): errors.append(f'{self.path}: incomplete image')
  for key in ('href','src'):
   v=a.get(key,''); p=urlsplit(v)
   if key=='src' and p.scheme in ('http','https'): errors.append(f'{self.path}: external request {v}')
   if v.startswith('/') and not v.startswith('//'):
    target=site/unquote(p.path).lstrip('/')
    if target.is_dir(): target=target/'index.html'
    if not target.exists(): errors.append(f'{self.path}: missing {v}')
for file in site.rglob('*.html'):
 c=Check(file); c.feed(file.read_text());
 if c.h!=1: errors.append(f'{file}: {c.h} h1s')
css=(site/'assets/css/site.css').read_text(); js=(site/'assets/js/site.js').read_text()
if re.search(r'url\(["\']?https?://|@import',css): errors.append('external CSS request')
if len(css.encode())>25000 or len(js.encode())>6000: errors.append('asset size limit')
redirects={}
for line in (site/'_redirects').read_text().splitlines():
 parts=line.split()
 if len(parts)!=3 or parts[2]!='301' or parts[0]==parts[1]: errors.append(f'bad redirect: {line}')
 else: redirects[parts[0]]=parts[1]
for line in (root/'src/assets/pages.tsv').read_text().splitlines()[1:]:
 old=line.split('\t')[0]
 if old!='/' and old not in redirects: errors.append(f'missing redirect {old}')
# Preview subscribe button: one per page while PREVIEW_SUBSCRIBE_URL is set, none once it is ''.
from data import PREVIEW_SUBSCRIBE_URL
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
  if _h.count('target="_blank"')!=1: errors.append('/keep/: only the code link may open a new tab')
elif _keep.parent.exists(): errors.append('/keep/ built while PREVIEW_SUBSCRIBE_URL is empty')
for _x in ('sitemap.xml',):
 if (_keep.parent.parent/_x).exists() and '/keep/' in (_keep.parent.parent/_x).read_text(): errors.append('/keep/ in sitemap')
print(f'{len(list(site.rglob("*.html")))} pages checked; CSS {len(css.encode())} bytes; JS {len(js.encode())} bytes; {len(redirects)} redirects checked.')
print('\n'.join(errors) if errors else 'All static checks passed.')
sys.exit(bool(errors))
