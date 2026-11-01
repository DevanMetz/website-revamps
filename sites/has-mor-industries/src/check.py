from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import re, sys
root=Path(__file__).resolve().parents[1]; site=root/'site'; errors=[]
void_tags={'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
documents={}; fragments=[]
class Check(HTMLParser):
 def __init__(self,path):
  super().__init__(); self.path=path; self.h=0; self.ids=set(); self.stack=[]; self.labels=[]; self.controls=set(); self.noindex=False
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag not in void_tags: self.stack.append(tag)
  if 'id' in a:
   if a['id'] in self.ids: errors.append(f'{self.path}: duplicate id {a["id"]}')
   self.ids.add(a['id'])
  if tag=='label' and 'for' in a: self.labels.append(a['for'])
  if tag in ('input','select','textarea'): self.controls.add(a.get('id'))
  if tag=='meta' and a.get('name')=='robots' and 'noindex' in a.get('content',''): self.noindex=True
  if tag=='h1': self.h+=1
  if tag=='img' and not all(k in a for k in ('alt','width','height')): errors.append(f'{self.path}: incomplete image')
  for key in ('href','src'):
   v=a.get(key,''); p=urlsplit(v)
   if key=='src' and p.scheme in ('http','https'): errors.append(f'{self.path}: external request {v}')
   if (v.startswith('/') and not v.startswith('//')) or v.startswith('#'):
    target=site/unquote(p.path).lstrip('/') if p.path else self.path
    if target.is_dir(): target=target/'index.html'
    if not target.exists(): errors.append(f'{self.path}: missing {v}')
    elif p.fragment and target.suffix=='.html': fragments.append((self.path,target,unquote(p.fragment)))
 def handle_startendtag(self,tag,attrs):
  self.handle_starttag(tag,attrs)
  if tag not in void_tags: self.handle_endtag(tag)
 def handle_endtag(self,tag):
  if not self.stack or self.stack[-1]!=tag: errors.append(f'{self.path}: misnested closing {tag}')
  if tag in self.stack:
   while self.stack.pop()!=tag: pass
for file in site.rglob('*.html'):
 c=Check(file); c.feed(file.read_text()); c.close(); documents[file]=c
 if c.h!=1: errors.append(f'{file}: {c.h} h1s')
 if c.stack: errors.append(f'{file}: unclosed tags {c.stack}')
 if not c.noindex: errors.append(f'{file}: missing preview noindex')
 for control in c.controls:
  if not control or control not in c.labels: errors.append(f'{file}: unlabelled form control {control}')
 for label in c.labels:
  if label not in c.controls: errors.append(f'{file}: label without a control {label}')
for source,target,fragment in fragments:
 if fragment not in documents[target].ids: errors.append(f'{source}: missing anchor {target}#{fragment}')
css=(site/'assets/css/site.css').read_text(); js=(site/'assets/js/site.js').read_text()
for asset in re.findall(r'url\(["\']?(/[^)"\']+)',css):
 if not (site/asset.lstrip('/')).is_file(): errors.append(f'CSS asset missing: {asset}')
for source in (root/'src/static').rglob('*'):
 if source.is_file():
  target=site/source.relative_to(root/'src/static')
  if not target.is_file() or source.read_bytes()!=target.read_bytes(): errors.append(f'static asset not copied: {source}')
if 'X-Robots-Tag: noindex' not in (site/'_headers').read_text(): errors.append('missing preview X-Robots-Tag')
if not re.search(r'^Disallow: /$',(site/'robots.txt').read_text(),re.M): errors.append('missing preview robots exclusion')
from xml.etree import ElementTree
for location in ElementTree.parse(site/'sitemap.xml').iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc'):
 if not location.text.startswith('https://has-mor.com/'): errors.append(f'wrong sitemap domain: {location.text}')
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
print(f'{len(list(site.rglob("*.html")))} pages checked; CSS {len(css.encode())} bytes; JS {len(js.encode())} bytes; {len(redirects)} redirects checked.')
print('\n'.join(errors) if errors else 'All static checks passed.')
sys.exit(bool(errors))
