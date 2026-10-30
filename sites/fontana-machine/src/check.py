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
print(f'Checked {len(files)} HTML pages, internal links, images, external resources, redirects and asset sizes.')
if errors:
 print('\n'.join(errors)); raise SystemExit(1)
print('All checks passed.')
