from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
import csv,re
root=Path(__file__).resolve().parent.parent; site=root/'site'; errors=[]
class Check(HTMLParser):
 def __init__(self,p): super().__init__(); self.p=p; self.h1=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='h1': self.h1+=1
  if tag=='img' and not all(k in a for k in ('alt','width','height')): errors.append(f'{self.p}: incomplete image')
  for k in ('href','src'):
   v=a.get(k,''); u=urlsplit(v)
   if u.scheme in ('http','https') and tag not in ('a',): errors.append(f'{self.p}: external request {v}')
   if v.startswith('/') and not v.startswith('//'):
    target=site/u.path.lstrip('/'); target=target/'index.html' if u.path.endswith('/') else target
    if not target.is_file(): errors.append(f'{self.p}: missing {v}')
for p in site.rglob('*.html'):
 html=p.read_text()
 for pattern in (r'\+\s*img\s*\(', r'\{\{', r'[\"\']\s*\+\s*(?:[\"\']|[a-zA-Z_]\w*\s*\()', r'\+\s*[\"\']'):
  if re.search(pattern, html): errors.append(f'{p}: leaked template code ({pattern})')
 c=Check(p); c.feed(html);
 if c.h1!=1: errors.append(f'{p}: {c.h1} h1s')
css=(site/'assets/css/site.css').read_text(); js=(site/'assets/js/site.js').read_text()
if re.search(r'url\(["\']?https?://|@import',css): errors.append('external CSS request')
if len(css.encode())>25000 or len(js.encode())>6000: errors.append('asset size exceeded')
redirects={}
for line in (site/'_redirects').read_text().splitlines():
 parts=line.split()
 if len(parts)!=3 or parts[2]!='301' or parts[0]==parts[1]: errors.append('bad redirect: '+line)
 else: redirects[parts[0]]=parts[1]
with (root/'src/assets/pages.tsv').open() as f:
 for row in csv.DictReader(f,delimiter='\t'):
  if row['old_path']!='/' and row['old_path'] not in redirects: errors.append('missing redirect '+row['old_path'])
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
  if _h.count('href="'+_escape(_code)+'"')!=1: errors.append('/keep/: code link')
  if '<meta name="robots" content="noindex">' not in _h: errors.append('/keep/: noindex')
  if 'target="_blank"' in _h: errors.append('/keep/: new-tab link')
elif _keep.parent.exists(): errors.append('/keep/ built while PREVIEW_SUBSCRIBE_URL is empty')
for _x in ('sitemap.xml',):
 if (_keep.parent.parent/_x).exists() and '/keep/' in (_keep.parent.parent/_x).read_text(): errors.append('/keep/ in sitemap')
print(f'Checked {len(list(site.rglob("*.html")))} HTML pages; CSS {len(css.encode())} bytes; JS {len(js.encode())} bytes.')
print('\n'.join(errors) if errors else 'All static checks passed.')
raise SystemExit(bool(errors))
