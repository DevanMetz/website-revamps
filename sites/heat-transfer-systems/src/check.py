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
   if (tag in ('script','img') or (tag=='link' and a.get('rel')!='canonical')) and u.scheme in ('http','https'): errors.append(f'{self.p}: external resource {v}')
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
print(f'{len(list(site.rglob("*.html")))} HTML pages checked; CSS {len(css.encode())} bytes; JS {len(js.encode())} bytes')
print('\n'.join(errors) if errors else 'All static checks passed.')
raise SystemExit(bool(errors))
