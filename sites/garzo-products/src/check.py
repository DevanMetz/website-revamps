from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json, re
from data import PREVIEW_SUBSCRIBE_URL, STRIPE_PORTAL_URL
from keep import KEEP_CODE_URL
root=Path('site'); errors=[]
class Check(HTMLParser):
 def __init__(self,file):
  super().__init__(); self.file=file; self.h=0; self.ids=set(); self.fragments=[]; self.labels=set(); self.fields=[]; self.aria_refs=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if len(a)!=len(attrs): errors.append(f'{self.file}: duplicate attribute on {tag}')
  if 'id' in a:
   if a['id'] in self.ids: errors.append(f'{self.file}: duplicate id {a["id"]}')
   self.ids.add(a['id'])
  if tag=='label' and 'for' in a: self.labels.add(a['for'])
  if tag in ('input','textarea') and a.get('type') not in ('checkbox','hidden'): self.fields.append(a.get('id'))
  for attr in ('aria-controls','aria-labelledby','aria-describedby'):
   self.aria_refs.extend(a.get(attr,'').split())
  if tag=='h1': self.h+=1
  if tag=='img' and not all(k in a for k in ('alt','width','height')): errors.append(f'{self.file}: incomplete image')
  for key in ('href','src'):
   v=a.get(key,''); u=urlsplit(v)
   if u.scheme in ('http','https') and tag not in ('meta',) and not (tag=='link' and a.get('rel')=='canonical' and v.startswith('https://garzoproducts.com/')) and v not in (PREVIEW_SUBSCRIBE_URL,KEEP_CODE_URL,STRIPE_PORTAL_URL): errors.append(f'{self.file}: external {v}')
   if v.startswith('/') and not v.startswith('//'):
    p=root/unquote(u.path.lstrip('/')); p=p/'index.html' if u.path.endswith('/') else p
    if not p.is_file(): errors.append(f'{self.file}: missing {v}')
   if tag=='a' and key=='href' and not u.scheme and not u.netloc and u.fragment:
    p=root/unquote(u.path.lstrip('/')) if u.path.startswith('/') else self.file.parent/unquote(u.path) if u.path else self.file
    if p.is_dir(): p=p/'index.html'
    self.fragments.append((p,unquote(u.fragment)))
pages={}
for f in root.rglob('*.html'):
 c=Check(f); c.feed(f.read_text());
 pages[f]=c
 if c.h!=1: errors.append(f'{f}: {c.h} h1s')
for f,c in pages.items():
 for target,fragment in c.fragments:
  if target not in pages or fragment not in pages[target].ids: errors.append(f'{f}: missing anchor {target}#{fragment}')
 for field in c.fields:
  if not field or field not in c.labels: errors.append(f'{f}: unlabeled field {field}')
 for ref in c.labels | set(c.aria_refs):
  if ref not in c.ids: errors.append(f'{f}: missing label/ARIA target {ref}')
 source=f.read_text()
 if '<meta name="robots" content="noindex">' not in source: errors.append(f'{f}: missing preview noindex')
 for structured in re.findall(r'<script type="application/ld\+json">(.*?)</script>',source,re.S):
  try: json.loads(structured)
  except ValueError: errors.append(f'{f}: invalid structured data')
# Every published page is reachable from the home page or the shared footer.
home=(root/'index.html').read_text()
footer=home.split('<footer>',1)[1].split('</footer>',1)[0]
for _page in root.rglob('index.html'):
 _path='/' + str(_page.parent.relative_to(root)).strip('.') + '/'
 if _path == '//': _path='/'
 if _path.startswith('/keep/'): continue
 if f'href="{_path}"' not in home and f'href="{_path}"' not in footer:
  errors.append(f'{_page}: not linked from home or footer')
css=(root/'assets/css/site.css').read_text(); js=(root/'assets/js/site.js').read_text()
if re.search(r'url\(["\']?https?://|@import',css): errors.append('External CSS request')
if len(css.encode())>25600 or len(js.encode())>6144: errors.append('Asset size exceeded')
redirects={}
for line in (root/'_redirects').read_text().splitlines():
 parts=line.split()
 if len(parts)!=3 or parts[2]!='301' or parts[0]==parts[1]: errors.append('Invalid redirect: '+line)
 else: redirects[parts[0]]=parts[1]
for old,destination in redirects.items():
 u=urlsplit(destination); target=root/unquote(u.path.lstrip('/'))
 if target.is_dir(): target=target/'index.html'
 if not target.is_file(): errors.append(f'{old}: missing redirect destination {destination}')
 elif u.fragment and (target not in pages or unquote(u.fragment) not in pages[target].ids): errors.append(f'{old}: missing redirect anchor {destination}')
for line in Path('src/assets/pages.tsv').read_text().splitlines()[1:]:
 p=line.split('\t')[0]
 if p!='/' and p not in redirects: errors.append('Missing redirect: '+p)
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
headers=(root/'_headers').read_text()
if '/assets/*\n' in headers: errors.append('Broad asset cache rule overrides CSS/JS revalidation')
for folder in ('css','js'):
 if f'/assets/{folder}/*\n  Cache-Control: public, max-age=0, must-revalidate' not in headers: errors.append(f'{folder}: missing cache revalidation')
for folder in ('img','fonts'):
 if f'/assets/{folder}/*\n  Cache-Control: public, max-age=31536000, immutable' not in headers: errors.append(f'{folder}: missing immutable cache')
if '  X-Robots-Tag: noindex' not in headers: errors.append('Missing preview noindex header')
if 'User-agent: *\nDisallow: /\n' not in (root/'robots.txt').read_text(): errors.append('Missing preview robots exclusion')
print(f'{len(list(root.rglob("*.html")))} HTML pages; CSS {len(css.encode())} bytes; JS {len(js.encode())} bytes; {len(redirects)} redirects')
print('\n'.join(errors) if errors else 'All static checks passed.')
raise SystemExit(bool(errors))
