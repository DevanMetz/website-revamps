from pathlib import Path
from html import escape
from data import CATALOG
import json
S=Path('site'); A='/assets/img/'
from PIL import Image
import shutil
import hashlib
CSS_V=hashlib.sha256(Path('site/assets/css/site.css').read_bytes()).hexdigest()[:10]  # cache-bust: /assets/* is cached for a year

def img(path,alt,cls='',eager=False):
 p=S/'assets/img'/path
 cutout=Path('src/transparent')/Path(path).with_suffix('.webp')
 transparent=p.with_name(p.stem+'-transparent.png')
 if cutout.exists():
  path=str(Path(path).with_suffix('.webp')); p=S/'assets/img'/path; shutil.copyfile(cutout,p)
 elif transparent.exists():
  p=transparent; path=str(p.relative_to(S/'assets/img'))
 with Image.open(p) as im: w,h=im.size
 return f'<img class="{cls}" src="{A+path}" alt="{escape(alt)}" width="{w}" height="{h}" '+('loading="eager" fetchpriority="high"' if eager else 'loading="lazy" decoding="async"')+'>'
def link(url,label,cls=''): return f'<a class="{cls}" href="{url}">{label}</a>'
def button(url,label): return link(url,label,'button')
def link_list(items): return '<ul>'+''.join('<li>'+link(u,n)+'</li>' for n,u in items)+'</ul>'
categories=[('ECG Electrodes','/electrodes/ecg/','ecg/2000ZT_Disposable_ECG_Electrode.jpg'),('TENS Electrodes','/electrodes/tens/','tens/971904152-TENS_Electrode.jpg'),('Tab Electrodes','/electrodes/tab/','misc/tab.jpg'),('Adhesive Strips','/electrodes/adhesive-strips/','strip/5FS-single_Adhesive_Strips.jpg'),('Custom Electrodes','/electrodes/custom/','misc/custom_electrodes.jpg')]
features=['Low impedance Solid Gel providing excellent performance and easy clean up','Silver/Silver Chloride (Ag/AgCl) coated sensors','Stainless Steel industry standard snaps','Latex Free, Hypoallergenic medical grade foam','Private label packaging']
options=['Latex Free, Hypoallergenic Cloth Material available on most shapes','Logo Tape to help market your product','Custom shapes and sizes','Packaging configuration flexibility to help maximize costs']
def bullets(items): return '<ul class="checklist">'+''.join('<li>'+x+'</li>' for x in items)+'</ul>'
def cards(): return '<div class="category-grid">'+''.join(f'<a class="category-card" href="{u}"><div class="category-image">{img(p,n)}</div><span>{n}</span></a>' for n,u,p in categories)+'</div>'
def video(): return f'<div class="video" id="video"><button type="button" class="video-load" aria-label="Play video: ECG Electrode Production Machine">{img("machines/video-thumb.jpg","", "", False)}<span class="play" aria-hidden="true">▶</span></button></div>'
def section(title,body,extra=''): return f'<section class="section {extra}"><div class="wrap">{f'<h2>{title}</h2>' if title else ''}{body}</div></section>'
def pagehead(title,intro=''): return f'<div class="page-head"><div class="wrap"><h1>{title}</h1>{f"<p>{intro}</p>" if intro else ""}</div></div>'
def machine_cards(): return '<div class="machine-grid">'+''.join(f'<a class="machine-card" href="{u}">{img(p,n)}<div><h3>{n}</h3><span aria-hidden="true">↗</span></div></a>' for n,u,p in [('ECG Electrode Production Machine','/production-machines/ecg-electrode-machine/','machines/ECGMachine-Front1.jpg'),('Packaging Systems','/production-machines/packaging-systems/','machines/Packager.jpg')])+'</div>'
intro='Taylor Industries Inc. is your contract manufacturing resource for ECG, TENS and Tab electrodes. Our electrodes are available in a wide variety of shapes and sizes to accommodate many different monitoring applications.'
home=f'''<section class="hero"><div class="wrap hero-grid"><div><h1>ECG, TENS &amp; Tab electrodes</h1><p>Our latex free, hypoallergenic electrodes are manufactured here in the United States in a wide variety of shapes, sizes and materials.</p><div class="actions">{button('/electrodes/','Electrodes')}{link('/production-machines/','Production machines','button-quiet')}</div></div><div class="hero-tray">{img('brand/electrodes-collage.webp','A range of Taylor Industries electrodes','hero-image',True)}</div></div></section><div class="wrap ecg-line" aria-hidden="true"><svg viewBox="0 -12 1240 64" preserveAspectRatio="none"><path d="M0 20 H485 l12 -8 10 16 12 -35 14 55 12 -28 H1240"/></svg></div>{section('Electrodes','<p>We can also help develop and manufacture custom electrodes exclusive to your company.</p>'+cards())}<section class="section"><div class="wrap"><div class="section-heading"><div><h2>Production machines</h2><p>Bring production in-house with a custom-built electrode production machine from Taylor Industries. We can provide an easy-to-operate machine that is designed and built to address your specific needs.</p></div></div>{machine_cards()}</div></section><section class="contact-band"><div class="wrap band-inner"><h2>Contact Taylor Industries</h2><div class="band-contact"><a href="tel:+15738935412">573-893-5412</a><a href="mailto:sales@taylor-ind.com">sales@taylor-ind.com</a></div>{button('/contact/','Contact us')}</div></section>'''
pages={'/':('Electrodes & Production Machines',intro,home)}
ecgintro='Let Taylor Industries be your contract manufacturing resource for disposable ECG / EKG electrodes manufactured in the United States. All ECG electrodes are Latex Free, Hypoallergenic and exceed AAMI specifications.'
from urllib.parse import quote

def esc(v): return escape(str(v or ''), quote=True)
def anchor(p): return p['code']
def product_url(p): return '/electrodes/'+{'ECG':'ecg','TENS':'tens','Tab':'tab','Adhesive Strips':'adhesive-strips'}[p['category']]+'/#'+quote(anchor(p))
def size_in(p):
 return p["size_in"] + ((" " + p["shape"]) if p["category"] == "TENS" else ("" if '"' in p["size_in"] or not p["size_in"] else '"'))
def size_text(p):
 return size_in(p) + (f' ({p["size_mm"]})' if p["size_mm"] else "")
def photo(p): return img(p['image'],p['code']+' electrode','catalog-photo') if p['image'] else ''
def product(p):
 pack=' / '.join(f'{p[k]} per {k}' for k in ('card','pouch','box','case') if p.get(k))
 if p['category']=='ECG' and p['pouch']==30 and p['case']==1200: pack=''
 if p['category']=='TENS' and pack=='4 per pouch': pack=''
 material='' if p['category']=='ECG' else f'<p>{esc(p["material"])}'+(f' / {esc(p["laminate"])}' if p.get('laminate') else '')+'</p>'
 available=p['available']
 if available: available=available.replace(' (', ': ').rstrip(')') if ' (' in available else 'Available: '+available
 extra=(f'<p>{esc(available)}</p>' if available else '')+(f'<p>{esc(p["note"])}</p>' if p['note'] and p['note'] != 'Listed in the Electrode Reference Guide' else '')
 pack_html=f'<p>{esc(pack)}'+('*' if p['category']=='ECG' else '')+'</p>' if pack else ''
 wire=img('ecg/TL225_Disposable_ECG_Electrode_with_wire.jpg','TL225 electrode with lead wire','catalog-detail-photo') if p['code']=='TL225' else ''
 image_html=f'<div class="catalog-image">{photo(p)}{wire}</div>' if p['image'] else ''
 size_html=esc(size_in(p)) + (f' <span class="metric-size">({esc(p["size_mm"])})</span>' if p['size_mm'] else '')
 return f'<article id="{esc(anchor(p))}" class="product">{image_html}<div class="product-copy"><h3>{esc(p["code"])}</h3><dl><dt>Size</dt><dd>{size_html}</dd></dl>{material}{pack_html}{extra}</div></article>'
def related(current): return ''
def category_nav(current):
 names=['ECG','TENS','Tab','Adhesive strips','Custom']
 return '<nav class="category-nav wrap" aria-label="Electrode categories"><a href="/electrodes/">Electrodes</a><ul>'+''.join(f'<li><a href="{u}"'+(' aria-current="page"' if u==current else '')+f'>{n}</a></li>' for n,(_,u,_) in zip(names,categories))+'</ul></nav>'
def catalog_section(category):
 items=[p for p in CATALOG if p['category']==category]
 foot='<p class="footnote">*Standard pouch size of 8-1/4&quot; x 8-1/4&quot; with black monochromatic print. Standard shipping case 17&quot; long x 10&quot; wide x 9&quot; high. Pouches shipped bulk with no inside boxes. Other pouch sizes and quantities per pouch are available.</p>' if category=='ECG' else ''
 return '<section class="section pale catalog"><div class="wrap"><div class="catalog-toolbar">'+button('/contact/?product='+quote(category+' electrodes'),'Request a quote or samples')+link('/assets/Electrode_Reference_Guide.pdf','Reference guide (PDF)','text-link')+'</div>'+('<p class="catalog-note">Solid Gel - Foam Monitoring Electrodes. Cloth is available on most shapes. Unless noted: 30 per pouch / 1200 per case.*</p>' if category=='ECG' else ('<p class="catalog-note">Unless noted: 4 per pouch.</p>' if category=='TENS' else ''))+'<div class="product-grid catalog-grid">'+''.join(product(p) for p in items)+'</div>'+foot+'</div></section>'


index_cards=cards()
pages['/electrodes/']=('Electrodes',intro,'<div class="page-head"><div class="wrap"><h1>Electrodes</h1><p>'+intro+' We can also work with you to create your own custom electrodes unique to your company.</p></div></div>'+section('',index_cards+'<div class="reference-row">'+link('/assets/Electrode_Reference_Guide.pdf','Download electrode reference guide (PDF)','text-link')+'</div>'))
ecg_features=section('Features & options',f'<div class="feature-columns"><div><h3>Features</h3>{bullets(features)}</div><div><h3>Options</h3>{bullets(options)}</div></div>')
pages['/electrodes/ecg/']=('ECG Electrodes',ecgintro,pagehead('ECG Electrodes',ecgintro)+catalog_section('ECG')+ecg_features+related('/electrodes/ecg/'))
tensintro='Prewired TENS electrodes available with a Black Carbon Film or a Tin conductive element.'
pages['/electrodes/tens/']=('TENS Electrodes',tensintro,pagehead('TENS Electrodes',tensintro)+catalog_section('TENS')+related('/electrodes/tens/'))
pages['/electrodes/tab/']=('Tab Electrodes','Tab electrodes and grounding pads.',pagehead('Tab Electrodes')+catalog_section('Tab')+related('/electrodes/tab/'))
stripintro='These 3" x .5" adhesive strips are ideal for securing lead wires to a patient and are made using the same medical grade, Latex Free, Hypoallergenic materials used in our ECG electrodes.'
pages['/electrodes/adhesive-strips/']=('Adhesive Strips','Adhesive strips for securing lead wires.',pagehead('Adhesive Strips',stripintro)+catalog_section('Adhesive Strips')+related('/electrodes/adhesive-strips/'))
custom=pagehead('Custom Electrodes','Do you need a specific proprietary electrode to work with your device? Do you see a unique need in the market that could be filled by an innovative electrode design?')+section('',f'<div class="split"><div><p>Taylor Industries can work with you to develop a product unique to your company.</p><div class="actions">{button("/contact/?product=Custom%20electrode","Request a custom electrode quote")}</div>{link("/assets/Electrode_Reference_Guide.pdf","Download reference guide (PDF)","text-link")}</div>{img("misc/custom_electrodes.jpg","Custom electrodes","detail-image")}</div>')+related('/electrodes/custom/')
pages['/electrodes/custom/']=('Custom Electrodes','Taylor Industries can work with you to develop a product unique to your company.',custom)

mintro='Taylor Industries can design and build machines to fit your company’s specific requirements. Our machines are easy to operate and can be run by one operator.'
prod=pagehead('Production Machines',mintro)+section('','<p>Solid gel, wet gel, one size of electrode or the flexibility to produce several sizes of electrodes on one machine. Using our packaging system, the same operator can produce, inspect and package the product.</p>'+machine_cards()+button('/machine-inquiry/','Machine inquiry'))
pages['/production-machines/']=('Production Machines',mintro,prod)
machine=pagehead('ECG Electrode Production Machine','Bring production of electrodes in-house or expand your production capabilities.')+f'''<section class="section"><div class="wrap"><div class="split machine-intro"><div><p>Taylor Industries custom builds each manufacturing system according to the specific needs of each customer. Different sizes of electrodes can be produced on a single machine.</p><p>When coupled with our <a href="/production-machines/packaging-systems/">packaging system</a>, the same operator can inspect the product, package and place finished pouches in shipping cases.</p>{button("/machine-inquiry/","Machine inquiry")}</div>{img("machines/ECGMachine-Front1.jpg","ECG electrode production machine","detail-image")}</div><div class="spec-row"><div><strong>4.46875&quot;</strong><span>Standard foam &amp; cloth width</span></div><div><strong>2&quot;</strong><span>Maximum electrode width (standard machine)</span></div><div><strong>1</strong><span>Operator</span></div></div><p>If you need a larger size, we can design a machine to fit your needs.</p><div class="video-container">{video()}</div></div></section>'''
pages['/production-machines/ecg-electrode-machine/']=('ECG Electrode Production Machine','Custom built ECG electrode production machines.',machine)
pack=pagehead('Packaging Systems')+f'''<section class="section"><div class="wrap"><div class="split machine-intro"><div><p>With a typical foot print of 12 feet x 5 feet, our simple to operate packaging system can be placed at the end of our production machine allowing the operator to inspect and package product while running the machine.</p><p>Our standard packager runs a poly/foil material 8.25&quot; wide and can produce pouches up to 11&quot; long. With the optional dual pouch configuration, two smaller pouches can be made side-by-side giving you added packaging flexibility.</p>{button("/machine-inquiry/","Machine inquiry")}</div>{img("machines/Packager.jpg","Packaging system","detail-image")}</div><div class="spec-row"><div><strong>12 ft x 5 ft</strong><span>Typical footprint</span></div><div><strong>8.25&quot;</strong><span>Poly/foil material width</span></div><div><strong>11&quot;</strong><span>Maximum pouch length</span></div></div><h3 class="pack-options">Options</h3><ul class="checklist"><li>Dual pouch configuration for two smaller pouches side-by-side</li><li>Custom modified in-line monochromatic thermal transfer printer</li></ul><div class="media-row"><figure class="pouches">{img("machines/pouches.jpg","Pouches produced on the packaging system","detail-image")}<figcaption>Samples of pouches produced on the same packaging system.</figcaption></figure>{video()}</div></div></section>'''

pages['/production-machines/packaging-systems/']=('Packaging Systems','Packaging systems for electrode production.',pack)
def field(label,name,required=False,typ='text',auto='',area=False,placeholder=''):
 req=' required' if required else ''; ph=f' placeholder="{escape(placeholder,quote=True)}"' if placeholder else ''; ac=f' autocomplete="{auto}"' if auto else ''; control=f'<textarea id="{name}" name="{label}" rows="4"{req}></textarea>' if area else f'<input id="{name}" name="{label}" type="{typ}"{req}{ac}{ph}>'
 return f'<div class="field"><label for="{name}">{label}{" *" if required else ""}</label>{control}</div>'
def choice(label,name,vals,typ='radio'): return f'<fieldset class="choice"><legend>{label}</legend>'+''.join(f'<label><input type="{typ}" name="{label}" value="{v}"> {v}</label>' for v in vals)+'</fieldset>'
common=field('Name','name',True,auto='name')+field('Company Name','company',True,auto='organization')+field('E-Mail','email',True,'email','email')+field('Phone','phone',False,'tel','tel')
def form(body,subject): return f'<!-- Replace the mailto handler with a form endpoint when available. --><form data-subject="{subject}"><p>* Required</p>{body}<button class="button" type="submit">Send inquiry</button><p class="form-status" role="status"></p></form>'
contact=pagehead('Contact Us')+f'''<section class="section"><div class="wrap form-layout"><div>{form('<div class="form-grid">'+common+'</div>'+field('Questions & Comments','comments',True,area=True)+field('How did you find out about Taylor Industries?','source'), 'Contact inquiry')}</div><aside class="contact-details"><h2>Taylor Industries Inc.</h2><p>2704 Industrial Drive<br>Jefferson City, MO 65109</p><p><a href="tel:+15738935412">573-893-5412</a><br>Fax 573-893-3647<br><a href="mailto:sales@taylor-ind.com">sales@taylor-ind.com</a></p><p>{link("/machine-inquiry/","Machine inquiry →","text-link")}</p></aside></div></section>'''
pages['/contact/']=('Contact Us','Contact Taylor Industries in Jefferson City, Missouri.',contact)
questions=['What type of ECG electrode(s) do you need to make on your machine?','What is the largest size electrode you will produce?','What is the smallest size electrode you will produce?','What is the quantity of electrodes you will need to produce on monthly basis?','What types of raw materials will you be running on the machine?','What will be the thickness of the material(s)?','Will you want to place a pre-printed logo tape on the top of the electrode underneath the snap?','Will you need a packaging system?','What is the largest size pouch you will produce?','What is the smallest size pouch you will produce?','What type of packaging material will you be using?']
examples={1:'e.g. 30mm x 25mm',2:'e.g. 22mm x 25mm',4:'e.g. foam, cloth or a special material',8:'e.g. 8 inches x 8 inches',9:'e.g. 6 inches x 4 inches',10:'e.g. poly paper...'}
q=''.join(field(x,'q'+str(i)) for i,x in enumerate(questions[:1]))+choice('Will the electrodes have a Wet Gel or Solid Gel?','gel',['Solid Gel','Wet Gel','Both Wet and Solid'],'checkbox')+''.join(field(x,'q'+str(i),placeholder=examples.get(i,'')) for i,x in enumerate(questions[1:],1))
q+=choice('Will you use pre-printed pouch material?','preprint',['Yes','No'])+choice('Will you need to print on the pouch material?','print',['Yes','No'])+choice('Do you require black and white print or color?','color',['Black and White','Color','Both'])+field('Along with the answers to the above questions, please let us know any added functions you would like your machine to perform, or any other special requests or questions you may have.','special',area=True)+field('How did you find out about Taylor Industries?','source')
inquiry=pagehead('Machine Information Request')+f'''<section class="section"><div class="wrap form-layout"><div>{form('<fieldset><legend>Contact information</legend><div class="form-grid">'+common+'</div></fieldset><fieldset><legend>Machine and packaging requirements</legend>'+q+'</fieldset>','Machine information request')}</div><aside class="contact-details"><p>These questions are very important and help us determine what type of system will best fit your needs.</p><hr><p>Taylor Industries Inc.<br>2704 Industrial Drive<br>Jefferson City, MO 65109</p><p><a href="tel:+15738935412">573-893-5412</a><br>Fax 573-893-3647<br><a href="mailto:sales@taylor-ind.com">sales@taylor-ind.com</a></p></aside></div></section>'''
pages['/machine-inquiry/']=('Machine Information Request','Request information about production machines and packaging systems.',inquiry)
pages['/links/']=('Links','Links to Select Engineering and R&D Medical.',pagehead('Links')+section('','<ul class="links-list"><li><a href="http://www.selectengineering.com">Select Engineering ↗</a></li><li><a href="http://www.rdmedicalproducts.com">R&amp;D Medical ↗</a></li></ul>'))
pages['/404.html']=('Page not found','Page not found.',pagehead('Page not found')+section('','<p>The page could not be found.</p>'+button('/','Return home')))
nav=[('Electrodes','/electrodes/'),('Production Machines','/production-machines/'),('Contact','/contact/')]
footerlinks=[('Home','/')]+[(n,u) for n,u,p in categories]+[('Electrodes','/electrodes/'),('Production Machines','/production-machines/'),('ECG Electrode Production Machine','/production-machines/ecg-electrode-machine/'),('Packaging Systems','/production-machines/packaging-systems/'),('Machine Inquiry','/machine-inquiry/'),('Contact','/contact/'),('Links','/links/'),('Electrode Reference Guide','/assets/Electrode_Reference_Guide.pdf')]
org={'@context':'https://schema.org','@type':'Organization','name':'Taylor Industries Inc.','address':{'@type':'PostalAddress','streetAddress':'2704 Industrial Drive','addressLocality':'Jefferson City','addressRegion':'MO','postalCode':'65109'},'telephone':'573-893-5412','faxNumber':'573-893-3647','email':'sales@taylor-ind.com'}
for path,(title,desc,body) in pages.items():
 children={
  '/electrodes/': [(n,item[1]) for n,item in zip(['ECG','TENS','Tab','Adhesive strips','Custom'],categories)],
  '/production-machines/': [('ECG Electrode Production Machine','/production-machines/ecg-electrode-machine/'),('Packaging Systems','/production-machines/packaging-systems/')],
 }
 def nav_item(name,url):
  current=' aria-current="page"' if path==url else ''
  sub=children.get(url,[])
  nested='<ul>'+''.join(f'<li><a href="{u}"'+(' aria-current="page"' if path==u else '')+f'>{n}</a></li>' for n,u in sub)+'</ul>' if sub else ''
  return f'<li><a href="{url}"{current}>{name}</a>{nested}</li>'
 navhtml='<ul>'+''.join(nav_item(n,u) for n,u in nav)+'</ul>' 
 if path in [u for _,u,_ in categories]: body=category_nav(path)+body
 if path in ['/production-machines/ecg-electrode-machine/','/production-machines/packaging-systems/']: body='<nav class="detail-back wrap" aria-label="Production machines"><a href="/production-machines/">Production machines</a></nav>'+body
 html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>{escape(title)} | Taylor Industries Inc.</title><meta name="description" content="{escape(desc,quote=True)}"><meta property="og:title" content="{escape(title)} | Taylor Industries Inc."><meta property="og:description" content="{escape(desc,quote=True)}"><meta property="og:type" content="website">{'<link rel="preload" as="image" href="/assets/img/brand/electrodes-collage.webp" fetchpriority="high">' if path == "/" else ""}<link rel="preload" href="/assets/fonts/instrument-serif-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin><link rel="icon" href="/favicon.ico"><link rel="stylesheet" href="/assets/css/site.css?v={CSS_V}"><script type="application/ld+json">{json.dumps(org)}</script><script defer src="/assets/js/site.js"></script></head><body><a class="skip" href="#main">Skip to content</a><header class="header"><div class="wrap header-inner"><a href="/" class="logo" aria-label="Taylor Industries home">{img('brand/logo-tagline.png','Taylor Industries Inc.',eager=True)}</a><button class="menu-toggle" aria-expanded="false" aria-controls="nav"><span class="menu-label">Menu</span></button><nav id="nav" class="nav" aria-label="Main navigation">{navhtml}</nav><div class="header-actions"><div class="header-contact"><a class="header-phone" href="tel:+15738935412" aria-label="Call 573-893-5412">573-893-5412</a><a class="header-email" href="mailto:sales@taylor-ind.com" aria-label="Email sales@taylor-ind.com">sales@taylor-ind.com</a></div><a class="button header-quote" href="/contact/">Request a quote</a></div></div></header><main id="main">{body}</main><footer class="footer"><div class="wrap footer-grid"><div><h2>Taylor Industries Inc.</h2><p>2704 Industrial Drive<br>Jefferson City, MO 65109</p><p><a href="tel:+15738935412">573-893-5412</a><br>Fax 573-893-3647<br><a href="mailto:sales@taylor-ind.com">sales@taylor-ind.com</a></p></div><div class="footer-links"><div><h2>Electrodes</h2>{link_list([('Overview','/electrodes/')]+[(n,u) for n,u,p in categories]+[('Reference guide','/assets/Electrode_Reference_Guide.pdf')])}</div><div><h2>Production machines</h2>{link_list([('Overview','/production-machines/'),('ECG Electrode Production Machine','/production-machines/ecg-electrode-machine/'),('Packaging Systems','/production-machines/packaging-systems/'),('Machine Inquiry','/machine-inquiry/')])}</div><div><h2>Company</h2>{link_list([('Home','/'),('Contact','/contact/'),('Links','/links/')])}</div></div></div><div class="wrap footer-bottom">© Taylor Industries Inc.</div></footer></body></html>'''
 html=html.replace('</a><a', '</a>\n<a').replace('</a><button', '</a>\n<button').replace('</button><a', '</button>\n<a')
 target=S/('index.html' if path=='/' else path.strip('/')+('' if path.endswith('.html') else '/index.html')); target.parent.mkdir(parents=True,exist_ok=True); target.write_text(html)


# Preview-only "Keep this site" subscribe button, added to every page after the build.
# Set PREVIEW_SUBSCRIBE_URL = '' in src/data.py and rebuild to remove it.
from data import PREVIEW_SUBSCRIBE_URL
def add_preview_subscribe():
 import re
 from html import escape as esc
 site_dir=Path(__file__).resolve().parent.parent/'site'
 css=("a.preview-subscribe{position:fixed;right:max(20px,calc(env(safe-area-inset-right) + 12px));bottom:max(20px,calc(env(safe-area-inset-bottom) + 12px));z-index:19;display:inline-flex;align-items:center;min-height:66px;padding:0 27px;border-radius:999px;background:#000098;color:#fff;font:600 22.5px/1.1 'Instrument Sans',sans-serif;letter-spacing:.01em;text-transform:none;text-decoration:none;white-space:nowrap;box-shadow:0 9px 27px rgba(0,0,0,.22);transition:background-color .15s,opacity .2s,visibility .2s}"
  "a.preview-subscribe:hover{background:#00006e;color:#fff;text-decoration:none}"
  "a.preview-subscribe:focus-visible{background:#000098;color:#fff;outline:3px solid #000098;outline-offset:3px;box-shadow:0 0 0 3px #fff,0 6px 18px rgba(0,0,0,.22)}"
  "a.preview-subscribe.is-tucked,body:has(header [aria-expanded=\"true\"]) a.preview-subscribe{opacity:0;visibility:hidden}"
  "@media (max-width:760px){a.preview-subscribe{right:max(12px,calc(env(safe-area-inset-right) + 8px));bottom:max(12px,calc(env(safe-area-inset-bottom) + 8px));min-height:60px;padding:0 21px;font-size:21px}}"
  "@media (prefers-reduced-motion:reduce){a.preview-subscribe{transition:none}}")
 js=("(()=>{const b=document.querySelector('a.preview-subscribe');if(!b)return;const k=[...document.querySelectorAll('footer,main .button,main button,main form,main input,main textarea,main select,main .category-card,main .machine-card,main .text-link,main .band-contact a')];let q=0;"
  "const u=()=>{q=0;const r=b.getBoundingClientRect();b.classList.toggle('is-tucked',k.some(e=>{const g=e.getBoundingClientRect();return g.width&&g.top<r.bottom+8&&g.bottom>r.top-8&&g.left<r.right+8&&g.right>r.left-8}))};"
  "const s=()=>{if(!q)q=requestAnimationFrame(u)};addEventListener('scroll',s,{passive:true});addEventListener('resize',s);u()})();")
 from keep import build_keep
 build_keep(site_dir,PREVIEW_SUBSCRIBE_URL)
 for page in site_dir.rglob('*.html'):
  if page==site_dir/'keep'/'index.html': continue
  html=re.sub(r'<!-- preview-subscribe -->.*?<!-- /preview-subscribe -->','',page.read_text(),flags=re.S)
  if PREVIEW_SUBSCRIBE_URL:
   html=html.replace('</head>','<!-- preview-subscribe --><style>'+css+'</style><!-- /preview-subscribe --></head>',1)
   html=html.replace('</body>','<!-- preview-subscribe --><a class="preview-subscribe" href="/keep/" aria-label="Upgrade my website: see how to switch to this new site">Upgrade my website</a><script>'+js+'</script><!-- /preview-subscribe --></body>',1)
  page.write_text(html)
add_preview_subscribe()
