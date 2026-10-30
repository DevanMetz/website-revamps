from pathlib import Path
from html import escape
from bs4 import BeautifulSoup
from PIL import Image
import re, json
from data import SERVICES
ROOT=Path(__file__).resolve().parent.parent
SITE=ROOT/'site'; IMG=SITE/'assets/img'; IMG.mkdir(parents=True,exist_ok=True)
source=(ROOT/'reference/crawl-page-text.txt').read_text()
sections={}
for chunk in source.split('='*100):
 m=re.search(r'URL: https://bmrebuildersinc.com/([^\n]*)\nTITLE:.*?\n(.*)',chunk,re.S)
 if m: sections[m.group(1).removesuffix('.html')]=m.group(2)

def image(name,alt,cls=''):
 p=ROOT/'reference/img/images'/name
 im=Image.open(p); im.seek(0)
 if im.mode not in ('RGB','L'): im=im.convert('RGB')
 out=Path(name).stem.lower()+('.png' if p.suffix.lower() in ('.gif','.png') else '.jpg'); im.save(IMG/out, 'PNG' if out.endswith('.png') else 'JPEG', **({'optimize': True} if out.endswith('.png') else {'quality':82,'optimize':True}))
 w,h=im.size
 return f'<img class="{cls}" src="/assets/img/{out}" width="{w}" height="{h}" alt="{escape(alt)}" loading="lazy">'
# Preserve the source logo's existing transparency.
logo = Image.open(ROOT/'img-originals/logo/original.gif').convert('RGBA')
logo = logo.resize((300, 177), Image.Resampling.LANCZOS)
logo.save(IMG/'logo.png')

# Captions are transcribed from the corresponding original table cells.
CAPTIONS = {
'001':'1/8 Carlo Salvi Cold Header','002':'National 625-6 Die S3 Cold Former','003':'Waterbury 3/8 SDDS Cold Header','004':'National 5/8 L.S. Boltmaker','005':'Malmedie QPB13 Boltmaker',
'006':'National 1/2 C.N.F.','007':'National 3/4 Boltmaker','008':'National #34 Header','009':'National 5 Die Partial',
'010':'National 5/8 CNF','011':'Rebuild Complete','012':'Cracked Frame','013':'Metal Stitching','014':'Broken Crankshaft','015':'New Crankshaft','016':'Chrome & Grind',
'017':'National 750-5 Die S1','018':'Machine ready for shipment after run off has been completed by the customer to their satisfaction using all the secondary equipment and platforms supplied by them.',
'021':'This National 3/8-4 die boltmaker converted to 4 die cold former.','022':'“Omega” Thermocouplers for bearing / liner temperature controls with bayonet quick disconnects.',
'029':'Safety Light Fault Panel. Mounted above push button station for easy operator awareness.',
'035':'Prutton','036':'Reed','037':'Hartford','038':'Frame Scraping','039':'Vertical','040':'#30 Machining','041':'Nutap','042':'Snow','043':'National',
'047':'#5 Waterbury C.N.F. Pitman arm complete from solid steel forgings with bearings in a 3 week turnaround','048':'#5 Waterbury C.N.F. Pitman arm complete from solid steel forgings with bearings in a 3 week turnaround','049':'New #30 W/F Thread Roller Slide','050':'National 5/8 CNF Crankshaft','051':'National 5/8 CNF Drive Lever Repair','052':'Requalify National 1000 Progressive Slide','053':'Hartford #40-140 Re-Machine','054':'National Die Block Cap','055':'National 750-6 Die Cold Former New Parts: bolsters - bolster wedges Complete transfer.','056':'B/M Die Blocks','057':'#4 Waterbury C.N.F. Die Block','058':'3/4 PKO System','059':'Die Set',
'060':'Custom Made for all diameters','061':'Custom Made for all diameters','063':'National 1000','064':'Ajax','065':'National 700','066':'Waterbury Toolroom Press','067':'National 2000 MaxiPress heading slide and wrist pin assembly.','068':'Ready to deliver to the door','069':'Complete rebuild and a triple kick-out installed',
'070':'Gardner 1 1/2 Surface Grinder','072':'Parker tool & Cutter Grinder','071':'Van Doran Milling Machine','073':'16 spindle double ended boring, spot facing and reamering with indexing fixtures.','074':'16 spindle double ended boring, spot facing and reamering with indexing fixtures.','075':'16 spindle double ended boring, spot facing and reamering with indexing fixtures.','076':'Flutemaster Production Mill upgraded with new table base with hardened roller packs-ball screws, Electrics-PLC.','077':'Flutemaster Production Mill upgraded with new table base with hardened roller packs-ball screws, Electrics-PLC.','078':'Flutemaster Production Mill upgraded with new table base with hardened roller packs-ball screws, Electrics-PLC.',
'083':'Seneca Falls R-O Form Relieving Grinder','084':'Before','085':'After','086':'Bridgeport Milling Machine','091':'14" Cincinnati','092':'15" Cincinnati','093':'17" Colchester','094':'Ground Bedways','095':'12" South Bend','096':'14" Lodge and Shipley',
}
# Longer descriptions in adjacent cells belong to these photographs.
DETAILS = {'006':'Disassembled to Bare Metal','007':'Heading slide requalified','008':'All Cam Rollers Replaced','009':'Complete documented manual','017':'Central location for all pneumatic','019':'Rear of panel shows','021':'This National 3/8-4 die','022':'"Omega" Thermocouplers','044':'A total of 30 Snow','082':'Gearbox,','083':'All machines are requalified','086':'All machines are requalified','093':'All bedways are scraped','095':'Leadscrews can be reground','096':'Leadscrews can be reground'}
def detail_text(olds, prefix):
 for old in olds:
  soup=BeautifulSoup((ROOT/f'reference/html/{old}.html.html').read_text(errors='ignore'),'html.parser')
  for cell in soup.find_all('td'):
   if cell.find('table'): continue
   text=re.sub(r'\s+',' ',' '.join(cell.stripped_strings)).strip()
   if text.startswith(prefix): return text
 return ''
def intro(olds):
 paragraphs=[]
 for old in olds:
  soup=BeautifulSoup((ROOT/f'reference/html/{old}.html.html').read_text(errors='ignore'),'html.parser')
  for cell in soup.find_all('td'):
   if cell.find('table') or cell.find('img') or cell.find('h1') or cell.find('a'): continue
   text=' '.join(cell.stripped_strings)
   text=re.sub(r'\s+',' ',text).strip()
   if not text or text in ('| HOME |','| NEXT PAGE | HOME |') or len(text)<45: continue
   if any(text in c or c in text for c in CAPTIONS.values() if len(c)>20) or any(text.startswith(d) for d in DETAILS.values()): continue
   if text not in paragraphs: paragraphs.append(text)
 if 'fastupgrade2' in olds:
  soup=BeautifulSoup((ROOT/'reference/html/fastupgrade2.html.html').read_text(errors='ignore'),'html.parser')
  cell=soup.find('img',src=re.compile('020')).find_parent('td')
  paragraphs.append(re.sub(r'\s+',' ',' '.join(cell.stripped_strings)).replace('| HOME |','').strip())
 return '<div class="intro">'+''.join(f'<h2>{escape(t)}</h2>' if t.startswith('Acme-Gridley 1" RAC') else f'<p>{escape(t)}</p>' for t in paragraphs)+'</div>'
def gallery(olds,title):
 result=[]
 previous_caption=None
 for old in olds:
  soup=BeautifulSoup((ROOT/f'reference/html/{old}.html.html').read_text(errors='ignore'),'html.parser')
  for img in soup.find_all('img'):
   name=Path(img.get('src','')).name
   if not re.match(r'^\d+\.',name) or not (ROOT/'reference/img/images'/name).exists(): continue
   key=Path(name).stem
   caption=CAPTIONS.get(key,'')
   detail=detail_text(olds,DETAILS[key]) if key in DETAILS else ''
   if detail and detail not in caption: caption=(caption+' '+detail).strip()
   rendered=image(name,caption or title)
   show_caption=caption and caption != previous_caption
   w,h=Image.open(ROOT/'reference/img/images'/name).size
   result.append(f'<figure style="--photo-width:{w*1.5:g}px"><div class="gallery-image">{rendered}</div>'+ (f'<figcaption>{escape(caption)}</figcaption>' if show_caption else '')+'</figure>')
   previous_caption=caption
 return '<div class="gallery">'+''.join(result)+'</div>'
def page(title,body,description,active=''):
 service_links=''.join(f'<li><a href="/services/{slug}/"'+(' aria-current="page"' if title==label else '')+f'>{label}</a></li>\n' for slug,label,_ in SERVICES)
 nav=(f'<ul><li><a href="/"'+(' aria-current="page"' if active=='home' else '')+'>Home</a></li>\n'
      f'<li><a href="/#services"'+(' class="section-current"' if active=='services' else '')+'>Services</a><ul class="service-nav">'+service_links+'</ul></li>\n'
      +''.join(f'<li><a href="/{key}/"'+(' aria-current="page"' if active==key else '')+f'>{label}</a></li>\n' for key,label in [('shop','Shop'),('contact','Contact')])+'</ul>')
 schema={'@context':'https://schema.org','@type':'Organization','name':'B.M. Rebuilders, Inc.','url':'https://bmrebuildersinc.com/','address':{'@type':'PostalAddress','addressLocality':'Elyria','addressRegion':'Ohio'},'telephone':'440-365-2300','faxNumber':'440-366-9868','email':'bmrebuild@aol.com'}
 return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>{escape(title)} | B.M. Rebuilders, Inc.</title><meta name="description" content="{escape(description)}"><meta property="og:title" content="{escape(title)} | B.M. Rebuilders, Inc."><meta property="og:description" content="{escape(description)}"><meta property="og:type" content="website"><link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml"><link rel="preload" href="/assets/fonts/archivo-narrow-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin><link rel="stylesheet" href="/assets/css/site.css?v=5"><script type="application/ld+json">{json.dumps(schema)}</script><script src="/assets/js/site.js?v=4" defer></script></head><body><a class="skip" href="#main">Skip to content</a><header class="header"><div class="wrap head"><a class="brand" href="/"><img src="/assets/img/logo.png" width="100" height="59" alt="B.M. Rebuilders, Inc."></a> <button class="menu" aria-expanded="false" aria-controls="nav">Menu</button><nav id="nav" aria-label="Main navigation">{nav}</nav><div class="rail-contact"><a href="tel:8886866237">888-686-6237</a> <a href="mailto:bmrebuild@aol.com">bmrebuild@aol.com</a></div></div></header><main id="main">{body}</main><footer><div class="wrap footer"><div><a class="brand" href="/"><img src="/assets/img/logo.png" width="100" height="59" alt="B.M. Rebuilders, Inc."></a><p>Elyria, Ohio</p></div><div><a href="tel:8886866237">888-686-6237</a><br><a href="tel:4403652300">440-365-2300</a><br><a href="mailto:bmrebuild@aol.com">bmrebuild@aol.com</a></div><div><a href="/shop/">Shop</a><br><a href="/contact/">Contact</a></div></div></footer></body></html>'''
def write(path,html):
 p=SITE/path/'index.html' if path else SITE/'index.html'; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(html)
cards=''
for slug,title,olds in SERVICES:
 soup=BeautifulSoup((ROOT/f'reference/html/{olds[0]}.html.html').read_text(errors='ignore'),'html.parser')
 names=[Path(i.get('src','')).name for i in soup.find_all('img') if re.match(r'^\d+\.', Path(i.get('src','')).name) and (ROOT/'reference/img/images'/Path(i.get('src','')).name).exists()]
 name=next((n for n in names if Image.open(ROOT/'reference/img/images'/n).width / Image.open(ROOT/'reference/img/images'/n).height > 1.25), names[0])
 cards+=f'<a class="card" href="/services/{slug}/"><div class="card-image">{image(name,title)}</div><div class="card-title"><h3>{title}</h3></div></a> '
mosaic=''.join(f'<div class="mosaic-photo mosaic-photo-{i}">{image(name, alt)}</div>' for i,(name,alt) in enumerate([('001.jpg','Carlo Salvi cold header'),('006.jpg','National cold former during rebuilding'),('014.jpg','Broken crankshaft'),('038.jpg','Frame scraping')],1))
home=f'''<section class="hero"><div class="hero-copy"><h1>Cold forming and wire drawing machinery rebuilding</h1><div class="actions"><a class="button" href="/contact/">Contact us about a machine</a> <a class="hero-link" href="/#services">Services</a></div></div>{mosaic}</section><section class="section wrap" id="services"><div class="section-heading"><h2>Services</h2></div><div class="cards">{cards}</div></section><section class="shop-band"><div class="wrap"><div class="shop-copy"><h2>Shop</h2><p>Our 20,000 square foot facility under crane has a fully equipped machine shop with horizontal boring mills up to 5" spindle, and lathes up to 30" diameter by 120" long.</p><p>We also have four stake bed trucks, each equipped with its own toolbox, fully loaded to handle the smallest repair to a mini or full rebuild on your floor.</p><a class="text-link" href="/shop/">Shop</a></div></div></section>''' 
write('',page('Machinery rebuilding',home,'Rebuilding and repairing machinery used in the cold forming and wire drawing industry.','home'))
for slug,title,olds in SERVICES:
 parts=intro(olds)+gallery(olds,title)+'<div class="service-cta"><a href="tel:8886866237">888-686-6237</a> <a class="button dark" href="/contact/">Contact us</a></div>'
 body=f'<section class="page-hero"><div class="wrap"><a class="back" href="/#services">All services</a><h1>{title}</h1><a class="button service-contact" href="/contact/">Contact us</a></div></section><div class="wrap service-content">{parts}</div>'
 write('services/'+slug,page(title,body,title+' from B.M. Rebuilders, Inc.','services'))
shop='''<section class="page-hero"><div class="wrap"><a class="back" href="/">Home</a><h1>Shop</h1></div></section><section class="section wrap shop-layout"><div><h2>Machine shop</h2><p>Our 20,000 square foot facility under crane has a fully equipped machine shop with horizontal boring mills up to 5" spindle, and lathes up to 30" diameter by 120" long.</p></div><div><h2>Field service</h2><p>We have four stake bed trucks, each equipped with its own toolbox, to handle repairs and mini or full rebuilds on your floor.</p><a class="text-link" href="/contact/">Contact us</a></div></section>'''
write('shop',page('Our shop',shop,'Our fully equipped machine shop and field service trucks.','shop'))
fields=[('name','Name','text','name',True),('company','Company','text','organization',False),('phone','Phone','tel','tel',False),('email','Email','email','email',True),('machine','Machine make/model','text','off',False),('service','Service needed','text','off',False)]
inputs=''.join(f'<label for="{i}">{label}<input id="{i}" name="{label}" type="{typ}" autocomplete="{auto}"'+(' required' if req else '')+'></label>' for i,label,typ,auto,req in fields)
contact=f'''<section class="page-hero"><div class="wrap"><a class="back" href="/">Home</a><h1>Contact</h1></div></section><section class="section wrap contact-layout"><div class="contact-details"><h2>Get in touch</h2><p>Toll free<br><a href="tel:8886866237">888-686-6237</a></p><p>Phone<br><a href="tel:4403652300">440-365-2300</a></p><p>Fax<br>440-366-9868</p><p>Email<br><a href="mailto:bmrebuild@aol.com">bmrebuild@aol.com</a></p></div><div><h2>Send an inquiry</h2><!-- Replace the mailto handler with a production form endpoint here. --><form id="inquiry"><div class="form-grid">{inputs}</div><label for="message">Message<textarea id="message" name="Message" rows="6" required></textarea></label><button class="button dark" type="submit">Send inquiry</button><p id="status" role="status"></p></form></div></section>'''
write('contact',page('Contact',contact,'Contact B.M. Rebuilders, Inc. in Elyria, Ohio.','contact'))
(SITE/'404.html').write_text(page('Page not found','<section class="page-hero"><div class="wrap"><a class="back" href="/">Home</a><h1>Page not found</h1><p><a href="/">Return home</a></p></div></section>','Page not found.'))
(SITE/'assets/img/favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" fill="#2b2d2f"/><text x="32" y="42" text-anchor="middle" font-family="sans-serif" font-size="25" font-weight="bold" fill="#ed5556">BM</text></svg>')
redirects=['/index.html / 301']
for slug,title,olds in SERVICES:
 for old in olds: redirects.append(f'/{old}.html /services/{slug}/ 301')
(SITE/'_redirects').write_text('\n'.join(redirects)+'\n')
(SITE/'_headers').write_text('/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  X-Frame-Options: DENY\n  X-Robots-Tag: noindex\n\n/assets/*\n  Cache-Control: public, max-age=31536000, immutable\n')
(SITE/'robots.txt').write_text('User-agent: *\nDisallow: /\nSitemap: https://bmrebuildersinc.com/sitemap.xml\n')
urls=['/','/shop/','/contact/']+[f'/services/{s[0]}/' for s in SERVICES]
(SITE/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>https://bmrebuildersinc.com{u}</loc></url>' for u in urls)+'</urlset>')
