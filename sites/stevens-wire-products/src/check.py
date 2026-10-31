from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import csv,re
from data import PREVIEW_SUBSCRIBE_URL, STRIPE_PORTAL_URL
from keep import KEEP_CODE_URL
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
   if tag=='link' and a.get('rel')=='canonical':
    expected='https://stevenswire.com'+('/' if self.path==site/'index.html' else '/'+str(self.path.relative_to(site)).removesuffix('index.html'))
    if v!=expected: errors.append(f'{self.path}: incorrect canonical {v}')
    continue
   if v in (PREVIEW_SUBSCRIBE_URL,KEEP_CODE_URL,STRIPE_PORTAL_URL): continue
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
with (root/'src/assets/pages.tsv').open() as f:
 for row in csv.DictReader(f,delimiter='\t'):
  if row['old_path']!='/' and row['old_path'] not in redirects: errors.append('missing redirect '+row['old_path'])
for p,limit in [('assets/css/site.css',25600),('assets/js/site.js',6144)]:
 size=(site/p).stat().st_size
 if size>limit: errors.append(f'{p} too large: {size}')
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
  if _h.count('href="'+_escape(STRIPE_PORTAL_URL)+'"')!=1 or '<a href="'+_escape(STRIPE_PORTAL_URL)+'" target="_blank" rel="noopener" aria-label="Manage or cancel your subscription (opens in a new tab)">Manage or cancel your subscription here</a>' not in _h: errors.append('/keep/: Stripe portal link missing')
  if _h.count('target="_blank"')!=2: errors.append('/keep/: only the code and portal links may open a new tab')
elif _keep.parent.exists(): errors.append('/keep/ built while PREVIEW_SUBSCRIBE_URL is empty')
for _x in ('sitemap.xml',):
 if (_keep.parent.parent/_x).exists() and '/keep/' in (_keep.parent.parent/_x).read_text(): errors.append('/keep/ in sitemap')
print(f'{len(pages)} HTML pages checked; {len(redirects)} redirects; CSS {(site/"assets/css/site.css").stat().st_size} bytes; JS {(site/"assets/js/site.js").stat().st_size} bytes')
print('\n'.join(errors) if errors else 'All static checks passed.')
raise SystemExit(bool(errors))
