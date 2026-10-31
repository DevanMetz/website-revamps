from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import sys
from data import CATALOG
root=Path('site')
errors=[]
class Page(HTMLParser):
 def __init__(self): super().__init__(); self.ids=set(); self.links=[]; self.noindex=False
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a: self.ids.add(a['id'])
  if tag=='meta' and a.get('name')=='robots' and a.get('content')=='noindex': self.noindex=True
  for key in ('href','src'):
   if a.get(key,'').startswith('/') and not a[key].startswith('//'): self.links.append(a[key])
for file in root.rglob('*.html'):
 page=Page(); page.feed(file.read_text())
 if not page.noindex: errors.append(f'{file}: missing noindex')
 for url in page.links:
  path=unquote(urlsplit(url).path); target=root/path.lstrip('/')
  if target.is_dir(): target=target/'index.html'
  if not target.exists(): errors.append(f'{file}: missing {url}')
for category,slug in [('ECG','ecg'),('TENS','tens'),('Tab','tab'),('Adhesive Strips','adhesive-strips')]:
 page=Page(); page.feed((root/'electrodes'/slug/'index.html').read_text())
 for p in CATALOG:
  if p['category']==category and p['code'] not in page.ids: errors.append(f'{slug}: missing {p["code"]}')
from data import PREVIEW_SUBSCRIBE_URL, STRIPE_PORTAL_URL
from keep import KEEP_CODE_URL as _code
from html import escape as _escape
# Preview subscribe button: one per page while PREVIEW_SUBSCRIBE_URL is set, none once it is ''.
_keep=Path(__file__).resolve().parent.parent/'site'/'keep'/'index.html'
for _f in (Path(__file__).resolve().parent.parent/'site').rglob('*.html'):
 _h=_f.read_text(); _n=_h.count('class="preview-subscribe"')
 if _f==_keep:
  if _n: errors.append(f'{_f}: preview subscribe button on /keep/')
  continue
 if _n!=(1 if PREVIEW_SUBSCRIBE_URL else 0): errors.append(f'{_f}: {_n} preview subscribe buttons')
 elif PREVIEW_SUBSCRIBE_URL and '<a class="preview-subscribe" href="/keep/" aria-label="Upgrade my website: see how to switch to this new site">Upgrade my website</a>' not in _h: errors.append(f'{_f}: preview subscribe link')
# /keep/ funnel: exists with the exact Stripe link while PREVIEW_SUBSCRIBE_URL is set, absent once it is ''.
if PREVIEW_SUBSCRIBE_URL:
 if not _keep.exists(): errors.append('/keep/ missing')
 else:
  _h=_keep.read_text()
  if _h.count('<a class="button" href="'+_escape(PREVIEW_SUBSCRIBE_URL)+'">Continue to checkout · $20/mo</a>')!=2 or _h.count('buy.stripe.com')!=2: errors.append('/keep/: checkout link')
  if _h.count('href="'+_escape(_code)+'"')!=1 or '<a href="'+_escape(_code)+'" target="_blank" rel="noopener" aria-label="Get the code (opens in a new tab)">Get the code</a>' not in _h: errors.append('/keep/: code link must open in a new tab')
  if '<meta name="robots" content="noindex">' not in _h: errors.append('/keep/: noindex')
  if _h.count('class="keep-step"')!=4 or 'Cancel your old hosting' not in _h: errors.append('/keep/: 4 steps')
  if _h.count('href="'+_escape(STRIPE_PORTAL_URL)+'"')!=1 or '<a href="'+_escape(STRIPE_PORTAL_URL)+'" target="_blank" rel="noopener" aria-label="Manage or cancel your subscription (opens in a new tab)">Manage or cancel your subscription here</a>' not in _h: errors.append('/keep/: Stripe portal link missing')
  if _h.count('target="_blank"')!=2: errors.append('/keep/: only the code and portal links may open a new tab')
elif _keep.parent.exists(): errors.append('/keep/ built while PREVIEW_SUBSCRIBE_URL is empty')
_sitemap=_keep.parent.parent/'sitemap.xml'
if _sitemap.exists() and '/keep/' in _sitemap.read_text(): errors.append('/keep/ in sitemap')
print('\n'.join(errors) if errors else 'All internal assets, product anchors and noindex tags pass.')
sys.exit(bool(errors))
