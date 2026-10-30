from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import re, csv
root = Path(__file__).resolve().parent.parent
site = root/'site'
errors=[]
class Check(HTMLParser):
 def __init__(self, file): super().__init__(); self.file=file; self.h1=0
 def handle_starttag(self, tag, attrs):
  a=dict(attrs)
  if tag=='h1': self.h1+=1
  if tag=='img':
   for key in ('alt','width','height'):
    if key not in a: errors.append(f'{self.file}: img missing {key}')
  for key in ('href','src'):
   value=a.get(key,'')
   if not value or value.startswith(('#','mailto:','tel:')): continue
   if value.startswith(('https://','http://')):
    if tag in ('img','script','link'): errors.append(f'{self.file}: external resource {value}')
    continue
   path=unquote(urlsplit(value).path)
   target=(site/path.lstrip('/')) if path.startswith('/') else (self.file.parent/path)
   if target.is_dir(): target=target/'index.html'
   if not target.exists(): errors.append(f'{self.file}: missing {value}')
files=list(site.rglob('*.html'))
for f in files:
 p=Check(f); p.feed(f.read_text());
 if p.h1!=1: errors.append(f'{f}: {p.h1} h1s')
css=(site/'assets/css/site.css').read_text()
if re.search(r'url\([\'"]?https?://|@import',css): errors.append('external CSS resource')
redirects={}
for line in (site/'_redirects').read_text().splitlines():
 parts=line.split()
 if len(parts)!=3 or parts[2]!='301' or parts[0]==parts[1]: errors.append(f'bad redirect: {line}')
 else: redirects[parts[0]]=parts[1]
with (root/'src/assets/pages.tsv').open() as f:
 for row in csv.DictReader(f,delimiter='\t'):
  if row['old_path']!='/' and row['old_path'] not in redirects: errors.append('missing redirect '+row['old_path'])
for path,limit in [('assets/css/site.css',25000),('assets/js/site.js',6000)]:
 size=(site/path).stat().st_size
 if size>limit: errors.append(f'{path} too large: {size}')
 print(f'{path}: {size} bytes')
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
  if _h.count('class="keep-step"')!=4 or 'Cancel your old hosting' not in _h: errors.append('/keep/: 4 steps')
  if _h.count('target="_blank"')!=1: errors.append('/keep/: only the code link may open a new tab')
elif _keep.parent.exists(): errors.append('/keep/ built while PREVIEW_SUBSCRIBE_URL is empty')
for _x in ('sitemap.xml',):
 if (_keep.parent.parent/_x).exists() and '/keep/' in (_keep.parent.parent/_x).read_text(): errors.append('/keep/ in sitemap')
print(f'Checked {len(files)} HTML pages, internal links, images, external resources, redirects and asset sizes.')
if errors:
 print('\n'.join(errors)); raise SystemExit(1)
print('All checks passed.')
