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
# Preview subscribe button: one per page while PREVIEW_SUBSCRIBE_URL is set, none once it is ''.
from data import PREVIEW_SUBSCRIBE_URL
from html import escape as _escape
for _f in (Path(__file__).resolve().parent.parent/'site').rglob('*.html'):
 _h=_f.read_text(); _n=_h.count('class="preview-subscribe"')
 if _n!=(1 if PREVIEW_SUBSCRIBE_URL else 0): errors.append(f'{_f}: {_n} preview subscribe buttons')
 elif PREVIEW_SUBSCRIBE_URL and f'href="{_escape(PREVIEW_SUBSCRIBE_URL)}" target="_blank" rel="noopener"' not in _h: errors.append(f'{_f}: preview subscribe link')
print('\n'.join(errors) if errors else 'All internal assets, product anchors and noindex tags pass.')
sys.exit(bool(errors))
