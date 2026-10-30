from pathlib import Path
from PIL import Image
import html, json, re, shutil
from data import source, products
S=Path('site'); I=S/'assets/img'; I.mkdir(parents=True,exist_ok=True)
used=set()
fonts=S/'assets/fonts'; fonts.mkdir(parents=True, exist_ok=True)
for font in Path('src/fonts').glob('*.woff2'): shutil.copyfile(font, fonts/font.name)
shutil.copyfile('src/assets/logo/garzo.png', I/'garzo-logo.png')
used.add('garzo-logo.png')
shutil.copyfile('src/assets/logo/favicon.png', I/'favicon.png')
used.add('favicon.png')
logo='<img src="/assets/img/garzo-logo.png" alt="Garzo Products" width="900" height="272">'
def img(name, alt=None):
    p=Path('src/assets/img/images')/name
    if not p.exists(): return ''
    out=re.sub(r'[^a-z0-9.-]','-',name.lower()).rsplit('.',1)[0]+'.png' if name.lower().endswith(('.gif','.png')) else re.sub(r'[^a-z0-9.-]','-',name.lower())
    transparent=Path('src/transparent')/(p.stem.lower()+'.png')
    if transparent.exists():
        out=transparent.name; shutil.copyfile(transparent, I/out); im=Image.open(transparent)
    else:
        im=Image.open(p); im.seek(0); im=im.convert('RGB' if out.endswith('.jpg') else 'RGBA'); im.save(I/out, quality=82, optimize=True)
    used.add(out); w,h=im.size
    return f'<img src="/assets/img/{out}" alt="{html.escape(alt or name.rsplit(".",1)[0])}" width="{w}" height="{h}" loading="lazy">'
def cards():
    return '<div class="cards">'+''.join(f'<a class="card" href="{u}"><div class="card-image">{img(n,t)}</div><div class="card-caption"><span>Fig. {i:02}</span><h3>{t}</h3></div></a>' for i,(t,u,n) in enumerate(products,1))+'</div>'
def layout(title, body, path, desc=None):
    nav=[('Products','/products/'),('Product registration','/product-registration/'),('Contact','/contact/')]
    mobile_products = [('Oil level regulator 101', '/products/oil-level-regulators/101/'), ('Oil level regulator 108', '/products/oil-level-regulators/108/'), ('108 installation guide', '/products/oil-level-regulators/108/installation/'), ('Low flow meters', '/products/low-flow-meters/'), ('Lubricator box control 211', '/products/lubricator-box-controls/211/'), ('Lubricator box control 213', '/products/lubricator-box-controls/213/'), ('Linear diaphragm operators', '/products/linear-diaphragm-operators/')]
    mobile_links = '<ul class="mobile-products">' + ''.join('<li><a href="' + u + '"' + (' aria-current="page"' if path == u else '') + '>' + t + '</a>' + ('<ul>' + ' '.join(f'<li><a href="{u}#model-501-{n}">501-{n}</a></li>' for n in (4,6,12,18,25)) + '</ul>' if t == 'Linear diaphragm operators' else '') + '</li>' for t, u in mobile_products) + '</ul>'
    links=' '.join(f'<li><a href="{u}"'+(' aria-current="page"' if path == u else '')+f'>{t}</a>' + (mobile_links if u == '/products/' else '') + '</li>' for t,u in nav)
    description=desc or title+' by Garzo Products, Waller, Texas.'
    ld={'@context':'https://schema.org','@type':'Organization','name':'Garzo Products','url':'https://garzoproducts.com/','telephone':'(713) 466-8679','email':'info@garzoproducts.com','address':{'@type':'PostalAddress','streetAddress':'42146 HWY 290 Business','addressLocality':'Waller','addressRegion':'TX','postalCode':'77484'}}
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>{html.escape(title)} | Garzo Products</title><meta name="description" content="{html.escape(description)}"><meta property="og:title" content="{html.escape(title)} | Garzo Products"><meta property="og:description" content="{html.escape(description)}"><meta property="og:type" content="website"><meta property="og:url" content="https://garzoproducts.com{path}"><link rel="icon" href="/assets/img/favicon.png" type="image/png"><link rel="preload" href="/assets/fonts/dm-serif-display-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin><link rel="stylesheet" href="/assets/css/site.css"><script type="application/ld+json">{json.dumps(ld)}</script><script src="/assets/js/site.js" defer></script></head><body><a class="skip" href="#main">Skip to content</a><header><div class="wrap header"><a class="brand" href="/" aria-label="Garzo Products home">{logo}</a><a class="mobile-call" href="tel:8007298807">Call</a><button class="menu" aria-expanded="false" aria-controls="nav">Menu</button><nav id="nav" aria-label="Main navigation"><ul class="nav-list">{links} <li><a class="nav-cta" href="/catalog-request/" {('aria-current="page"' if path == '/catalog-request/' else '')}>Request a catalog</a></li></ul> <a class="header-phone" href="tel:8007298807">(800) 729-8807</a></nav></div></header><main id="main">{body}</main><footer><div class="wrap footer"><div><a class="brand" href="/" aria-label="Garzo Products home">{logo}</a><p>42146 HWY 290 Business<br>Waller, TX 77484</p></div><div><a href="tel:7134668679">(713) 466-8679</a><br><a href="tel:8007298807">(800) 729-8807</a><br><a href="mailto:info@garzoproducts.com">info@garzoproducts.com</a></div><div><a href="/products/">Products</a><br><a href="/product-registration/">Product registration</a><br><a href="/contact/">Contact</a></div></div></footer></body></html>'''
def write(path,title,body,desc=None):
    f=S/path.strip('/')/'index.html' if path!='/' else S/'index.html'; f.parent.mkdir(parents=True,exist_ok=True); f.write_text(re.sub(r'</a>(?=<(?:a|button)\b)', '</a> ', layout(title,body,path,desc)))
def banner(title, intro='', back=True, back_url='/products/', back_label='Products'):
    return f'<section class="pagehead"><div class="wrap">'+(f'<a class="back" href="{back_url}">{back_label}</a>' if back else '')+f'<h1>{title}</h1>'+ (f'<p>{intro}</p>' if intro else '')+'</div></section>'
def paras(lines):
    return ''.join('<p>'+html.escape(x)+'</p>' for x in lines)
def checklist(lines, heading='Features'):
    return '<h2>'+heading+'</h2><ul class="checklist">'+''.join('<li>'+html.escape(x)+'</li>' for x in lines)+'</ul>'
def ordering(name, alt):
    picture=img(name,alt)
    target=(Path('src/transparent')/(Path(name).stem.lower()+'.png')).name if (Path('src/transparent')/(Path(name).stem.lower()+'.png')).exists() else name
    width=Image.open(Path('src/assets/img/images')/name).width
    return f'<figure class="ordering" style="max-width:{width:g}px"><figcaption><a href="/assets/img/{target}">Open full size</a><span>Scroll chart →</span></figcaption><div class="chart-scroll" tabindex="0" role="region" aria-label="{html.escape(alt)}">{picture}</div></figure>'
def siblings(current):
    entries=[('101','/products/oil-level-regulators/101/'),('108','/products/oil-level-regulators/108/'),('211','/products/lubricator-box-controls/211/'),('213','/products/lubricator-box-controls/213/'),('Low flow meters','/products/low-flow-meters/'),('Linear diaphragm operators','/products/linear-diaphragm-operators/')]
    return '<nav class="siblings" aria-label="Products"><ul>'+''.join(f'<li><a href="{url}"'+(' aria-current="page"' if current == url else '')+f'>{label}</a></li>' for label,url in entries)+'</ul></nav>'
def product_content(lines, model, photo, title):
    if model == '108':
        lines[1] = lines[1].replace('This feature will allow the controller to operate with adequate oil supply pressures. ', '') + ' ' + lines[2].split(' The gauge glass',1)[0]
        lines[2] = 'The gauge glass' + lines[2].split(' The gauge glass',1)[1]
        headings={1:'Oil supply',2:'Gauge glass',3:'Level alarms',4:'Mounting',5:'Oil level',6:'Valve and seat',7:'Oil filter',8:'Construction',9:'Installation kits'}
        features=lines[10:]; lines=lines[:10]
    elif model == '101':
        headings={1:'Level switch',2:'Oil filter',3:'Gauge glass',4:'Vent connection',5:'Maintenance',6:'Construction',7:'Installation kits'}; features=[]
    elif model == '300B':
        headings={1:'Meter operation',2:'Oil filter',3:'Mounting'}; features=lines[5:9]; specs=lines[10:]; lines=lines[:4]
    else:
        headings={1:'Float valve',2:'Model 211-08-1',3:'Model 211-070-1',4:'Model 211A-08-1',5:'Model 211A-070-1',6:'Model 211-PNEU',7:'Model 211-EX',8:'Model 211C-04-EX'}; features=[]
    result='' 
    if features: result+=checklist(features)
    for i,line in enumerate(lines[1:],1): result+='<h2 id="'+re.sub(r'[^a-z0-9]+','-',headings[i].lower()).strip('-')+'">'+headings[i]+'</h2>'+paras([line])
    if model == '300B': result+=checklist(specs,'Specifications')
    return result
write('/','Oil level regulators and compressor accessories','<section class="hero wrap"><div class="cover"><p class="since">Since 1939</p><h1>Oil level regulators and compressor accessories</h1><div class="actions"><a class="button" href="/products/">Explore products</a><a class="textlink" href="/contact/">Contact us</a></div><div class="hero-image">'+img('501gp.jpg','Garzo linear diaphragm operators')+'</div></div></section><section class="section wrap"><div class="section-title"><h2>Products</h2><a href="/products/">View all products</a></div>'+cards()+'</section><section class="band"><div class="wrap band-inner"><div><h2>Request a catalog</h2><p>Garzo catalogs are sent out by bulk mail. Please allow 1-4 weeks for delivery.</p></div><a class="button" href="/catalog-request/">Request a catalog</a></div></section>')
write('/products/','Products',banner('Products','Oil level regulators, shut down devices, low flow meters, lubricator box controls, oil reservoirs and linear diaphragm operators.',False)+'<section class="section wrap">'+cards()+'<p class="model-link"><a href="/products/lubricator-box-controls/213/">Lubricator box control 213</a></p><div class="additional"><h2>Shut-down devices &amp; oil reservoirs</h2><p>Contact Garzo Products for information about shut-down devices and oil reservoirs.</p><a class="button dark" href="/contact/">Contact us</a></div></section>')
items=[('101','oil-level-regulators/101','101.html','101b.jpg'),('108','oil-level-regulators/108','108.html','108b.jpg'),('300B','low-flow-meters','meter.html','300b.jpg'),('211','lubricator-box-controls/211','211.html','211-08.jpg')]
for model,path,old,photo in items:
    lines=source(old); lines=lines[1:]
    title={'101':'Oil level regulator 101B','108':'Oil level regulator 108B','300B':'Low flow meter 300B','211':'Lubricator box control 211'}[model]
    extra=''
    if model=='101': extra='<h2 id="ordering">How to order</h2>'+ordering('order.jpg','Model 101 ordering information')
    if model=='108': extra='<h2 id="ordering">How to order</h2>'+ordering('order108.jpg','Model 108 ordering information')
    if model=='300B': extra='<h2 id="diagram">Diagram</h2>'+ordering('300bdia.jpg','300B low flow meter diagram')
    if model=='211': extra='<p><a href="/products/lubricator-box-controls/213/">Model 213</a></p>'
    actions=('<a href="/products/oil-level-regulators/108/installation/">Installation guide</a>' if model=='108' else '') + ' ' + ('<a href="#ordering">How to order</a>' if model in ('101','108') else '<a href="#diagram">Diagram</a>' if model=='300B' else '') + ' <a href="/contact/">Contact</a>'
    content=product_content(lines,model,photo,title)
    body=banner(title)+siblings('/products/'+path+'/')+f'<section class="section wrap product-detail {"detail-108" if model == "108" else ""}"><div class="detail-intro"><aside class="detail-photo">{img(photo,title)}</aside><div><div class="detail-actions">{actions}</div>{paras(lines[:1])}</div></div><div class="detail-body"><div class="product-copy">{content}</div><div class="detail-extra">{extra}</div></div></section>'
    write('/products/'+path+'/',title,body)
write('/products/lubricator-box-controls/213/','Lubricator box control 213',banner('Lubricator box control 213')+siblings('/products/lubricator-box-controls/213/')+'<section class="section wrap"><p>Contact Garzo Products for information on Model 213.</p><a class="button dark" href="/contact/">Contact us</a></section>')
lines=source('install.html')[1:]
steps=[]
for i, line in enumerate(lines[1:], 1):
    content=html.escape(re.sub(r'^\d+\.\s*', '', line))
    if i == 4: content+='<div class="figures">'+''.join(img(f'fig{n}.jpg',f'Installation figure {n}') for n in (1,2,3))+'</div>'
    steps.append('<li>'+content+'</li>')
write('/products/oil-level-regulators/108/installation/','108B installation guide',banner('108B installation guide', back_url='/products/oil-level-regulators/108/', back_label='Oil level regulator 108B')+'<section class="section wrap narrow product-detail"><h2>Basic installation</h2><ol class="installation-steps">'+''.join(steps)+'</ol></section>')
lines=source('diap.html')[1:]
body=banner('Linear diaphragm operators')+siblings('/products/linear-diaphragm-operators/')+'<section class="section wrap product-detail"><div class="modelnav">'+' '.join(f'<a href="#model-501-{n}">501-{n}</a>' for n in (4,6,12,18,25))+'</div><div class="detail-intro"><aside class="detail-photo">'+img('501gp.jpg','Linear diaphragm operators')+'</aside><div><div class="detail-actions"><a href="/contact/">Contact</a> <a href="#ordering">How to order</a></div>'+paras(lines[:1])+'</div></div><div class="product"><div class="product-copy">'+checklist(lines[4:12])+'<h2>Construction</h2>'+paras(lines[1:2])+'<h2>Spring rates</h2>'+paras(lines[2:3])+checklist(lines[13:],'Specifications')+'</div></div>'
for n in (4,6,12,18,25):
    body+=f'<section class="model" id="model-501-{n}"><h2>Model 501-{n}</h2><div class="model-images">'+img(f'501{n}.jpg',f'Model 501-{n}')
    for name in {4:['0932.jpg'],6:['0114.jpg','mount5016.jpg'],12:['0115.jpg','mount5012.jpg'],18:[],25:['0116.jpg']}[n]: body+=img(name,f'Model 501-{n} diagram')
    body+='</div>'+ordering(f'501{n}chart.jpg',f'Model 501-{n} specifications chart')+'</section>'
body+='<h2>Spring chart</h2>'+ordering('springchart.jpg','Spring chart')+'<h2 id="ordering">How to order</h2>'+ordering('order501.jpg','501 ordering information')+'<p><a class="button dark" href="/contact/">Contact us</a></p></section>'
write('/products/linear-diaphragm-operators/','Linear diaphragm operators',body)
def form(fields,subject,checks=[]):
    s='<form data-subject="'+subject+'"><!-- Replace the mailto handler with a production form endpoint here. --><div class="form-grid">'
    for label,typ,req,auto in fields:
        id=re.sub('[^a-z0-9]+','-',label.lower()).strip('-'); wide=typ=='textarea'
        s+=f'<div class="field {"wide" if wide else ""}"><label for="{id}">{label}</label>'
        if wide: s+=f'<textarea id="{id}" name="{label}" rows="5"'+(' required' if req else '')+'></textarea>'
        else: s+=f'<input id="{id}" name="{label}" type="{typ}"'+(' required' if req else '')+(f' autocomplete="{auto}"' if auto else '')+'>'
        s+='</div>'
    s+='</div>'
    if checks: s+='<fieldset><legend>Select any of the following options that apply</legend>'+''.join(f'<label class="check"><input type="checkbox" name="Installation" value="{x}"> {x}</label>' for x in checks)+'</fieldset>'
    return s+'<button class="button dark" type="submit">Prepare email</button><p class="status" role="status"></p></form>'
F=lambda x,t='text',r=False,a='':(x,t,r,a)
address=[F('Company Name',a='organization'),F('Address 1',a='address-line1'),F('Address 2',a='address-line2'),F('City',a='address-level2'),F('State/Province',a='address-level1'),F('Zip/Postal Code',a='postal-code'),F('Country',a='country-name')]
cat=[F('Name',a='name'),F('Company',a='organization'),F('Address',a='street-address'),F('City',a='address-level2'),F('State',a='address-level1'),F('Zip',a='postal-code'),F('Country',a='country-name'),F('Phone','tel',a='tel'),F('Email','email',True,'email'),F('Where did you hear about us?'),F('Description of your work / products of interest','textarea')]
write('/catalog-request/','Catalog request',banner('Catalog request','Garzo catalogs are sent out by bulk mail. Please allow 1-4 weeks for delivery.',False)+'<section class="section wrap narrow">'+form(cat,'Catalog request')+'</section>')
reg=[F('Full name',a='name')]+address+[F('Work Phone','tel',a='tel'),F('Fax','tel'),F('E-mail','email',True,'email'),F('Company Web Site','url',a='url'),F('Model Number'),F('Serial Number')]
write('/product-registration/','Product registration',banner('Product registration','All information obtained is for GARZO’s use only. No information will be given or sold to any other organization.',False)+'<section class="section wrap narrow">'+form(reg,'Product registration',['New Installation','Rebuild of Old Installation','Replacing Existing GARZO Product','Replacing Existing Competitors Product'])+'</section>')
write('/contact/','Contact',banner('Contact','',False)+'<section class="section wrap contact-grid"><div><h2>Garzo Products</h2><p>42146 HWY 290 Business<br>Waller, TX 77484</p><p><a href="tel:7134668679">(713) 466-8679</a><br><a href="tel:8007298807">(800) 729-8807</a><br><a href="mailto:info@garzoproducts.com">info@garzoproducts.com</a></p></div><div><h2>Send an inquiry</h2>'+form([F('Name',r=True,a='name'),F('Email','email',True,'email'),F('Phone','tel',a='tel'),F('Message','textarea',True)],'Product inquiry')+'</div></section>')
(S/'404.html').write_text(re.sub(r'</a>(?=<(?:a|button)\b)', '</a> ', layout('Page not found',banner('Page not found','',False)+'<section class="section wrap"><a href="/">Return home</a></section>','/404.html')))

for p in I.iterdir():
    if p.name not in used: p.unlink()
paths=['/','/products/','/products/oil-level-regulators/101/','/products/oil-level-regulators/108/','/products/oil-level-regulators/108/installation/','/products/low-flow-meters/','/products/lubricator-box-controls/211/','/products/lubricator-box-controls/213/','/products/linear-diaphragm-operators/','/catalog-request/','/product-registration/','/contact/']
(S/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>https://garzoproducts.com'+p+'</loc></url>' for p in paths)+'</urlset>')
(S/'robots.txt').write_text('User-agent: *\nDisallow: /\nSitemap: https://garzoproducts.com/sitemap.xml\n')
redirect={'index.html':'/','sitemap.html':'/products/','products.html':'/products/','register.html':'/product-registration/','contact.html':'/contact/','108.html':'/products/oil-level-regulators/108/','101.html':'/products/oil-level-regulators/101/','install.html':'/products/oil-level-regulators/108/installation/','meter.html':'/products/low-flow-meters/','211.html':'/products/lubricator-box-controls/211/','213.html':'/products/lubricator-box-controls/213/','other.html':'/products/','main.html':'/'}
for old,n in [('diap',4),('5014',4),('5016',6),('50112',12),('50118',18),('50125',25)]: redirect[old+'.html']=f'/products/linear-diaphragm-operators/#model-501-{n}'
(S/'_redirects').write_text(''.join(f'/{a} {b} 301\n' for a,b in redirect.items()))
(S/'_headers').write_text('/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  X-Frame-Options: DENY\n  X-Robots-Tag: noindex\n\n/assets/*\n  Cache-Control: public, max-age=31536000, immutable\n')


# Preview-only "Keep this site" subscribe button, added to every page after the build.
# Set PREVIEW_SUBSCRIBE_URL = '' in src/data.py and rebuild to remove it.
from data import PREVIEW_SUBSCRIBE_URL
def add_preview_subscribe():
 import re
 from html import escape as esc
 site_dir=Path(__file__).resolve().parent.parent/'site'
 css=("a.preview-subscribe{position:fixed;right:max(20px,calc(env(safe-area-inset-right) + 12px));bottom:max(20px,calc(env(safe-area-inset-bottom) + 12px));z-index:19;display:inline-flex;align-items:center;min-height:66px;padding:0 27px;border-radius:999px;background:#a80000;color:#fff;font:700 22.5px/1.1 'DM Sans',sans-serif;letter-spacing:.01em;text-transform:none;text-decoration:none;white-space:nowrap;box-shadow:0 9px 27px rgba(0,0,0,.22);transition:background-color .15s,opacity .2s,visibility .2s}"
  "a.preview-subscribe:hover{background:#780000;color:#fff;text-decoration:none}"
  "a.preview-subscribe:focus-visible{background:#a80000;color:#fff;outline:3px solid #a80000;outline-offset:3px;box-shadow:0 0 0 3px #fff,0 6px 18px rgba(0,0,0,.22)}"
  "a.preview-subscribe.is-tucked,body:has(header [aria-expanded=\"true\"]) a.preview-subscribe{opacity:0;visibility:hidden}"
  "@media (max-width:760px){a.preview-subscribe{right:max(12px,calc(env(safe-area-inset-right) + 8px));bottom:max(12px,calc(env(safe-area-inset-bottom) + 8px));min-height:60px;padding:0 21px;font-size:21px}}"
  "@media (prefers-reduced-motion:reduce){a.preview-subscribe{transition:none}}")
 js=("(()=>{const b=document.querySelector('a.preview-subscribe');if(!b)return;const k=[...document.querySelectorAll('footer,main .button,main button,main form,main input,main textarea,main select')];let q=0;"
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
