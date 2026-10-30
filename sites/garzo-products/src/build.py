from pathlib import Path
from PIL import Image
import html, json, re, shutil
from data import source, products
S=Path('site'); I=S/'assets/img'; I.mkdir(parents=True,exist_ok=True)
used=set()
def img(name, alt=None):
    p=Path('reference/img/images')/name
    if not p.exists(): return ''
    out=re.sub(r'[^a-z0-9.-]','-',name.lower()).rsplit('.',1)[0]+'.png' if name.lower().endswith(('.gif','.png')) else re.sub(r'[^a-z0-9.-]','-',name.lower())
    im=Image.open(p); im.seek(0); im=im.convert('RGB' if out.endswith('.jpg') else 'RGBA'); im.save(I/out, quality=82, optimize=True)
    used.add(out); w,h=im.size
    return f'<img src="/assets/img/{out}" alt="{html.escape(alt or name.rsplit(".",1)[0])}" width="{w}" height="{h}" loading="lazy">'
def cards():
    return '<div class="cards">'+''.join(f'<a class="card" href="{u}"><div class="card-image">{img(n,t)}</div><h3>{t}</h3><span aria-hidden="true">→</span></a>' for t,u,n in products)+'</div>'
def layout(title, body, path, desc=None):
    nav=[('Products','/products/'),('Product registration','/product-registration/'),('Contact','/contact/')]
    links=''.join(f'<a href="{u}"'+(' aria-current="page"' if path.startswith(u) else '')+f'>{t}</a>' for t,u in nav)
    description=desc or title+' by Garzo Products, Waller, Texas.'
    ld={'@context':'https://schema.org','@type':'Organization','name':'Garzo Products','url':'https://garzoproducts.com/','telephone':'(713) 466-8679','email':'info@garzoproducts.com','address':{'@type':'PostalAddress','streetAddress':'42146 HWY 290 Business','addressLocality':'Waller','addressRegion':'TX','postalCode':'77484'}}
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>{html.escape(title)} | Garzo Products</title><meta name="description" content="{html.escape(description)}"><meta property="og:title" content="{html.escape(title)} | Garzo Products"><meta property="og:description" content="{html.escape(description)}"><meta property="og:type" content="website"><meta property="og:url" content="https://garzoproducts.com{path}"><link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/assets/css/site.css"><script type="application/ld+json">{json.dumps(ld)}</script><script src="/assets/js/site.js" defer></script></head><body><a class="skip" href="#main">Skip to content</a><header><div class="wrap header"><a class="brand" href="/" aria-label="Garzo Products home">GARZO<span>PRODUCTS</span></a><button class="menu" aria-expanded="false" aria-controls="nav">Menu</button><nav id="nav" aria-label="Main navigation">{links}<a class="header-phone" href="tel:8007298807">(800) 729-8807</a><a class="nav-cta" href="/catalog-request/">Request a catalog</a></nav></div></header><main id="main">{body}</main><footer><div class="wrap footer"><div><a class="brand light" href="/">GARZO<span>PRODUCTS</span></a><p>42146 HWY 290 Business<br>Waller, TX 77484</p></div><div><a href="tel:7134668679">(713) 466-8679</a><br><a href="tel:8007298807">(800) 729-8807</a><br><a href="mailto:info@garzoproducts.com">info@garzoproducts.com</a></div><div><a href="/products/">Products</a><br><a href="/product-registration/">Product registration</a><br><a href="/contact/">Contact</a></div></div></footer></body></html>'''
def write(path,title,body,desc=None):
    f=S/path.strip('/')/'index.html' if path!='/' else S/'index.html'; f.parent.mkdir(parents=True,exist_ok=True); f.write_text(layout(title,body,path,desc))
def banner(title, intro='', back=True):
    return f'<section class="pagehead"><div class="wrap">'+('<a class="back" href="/products/">← Products</a>' if back else '')+f'<h1>{title}</h1>'+ (f'<p>{intro}</p>' if intro else '')+'</div></section>'
def paras(lines):
    return ''.join('<p>'+html.escape(x)+'</p>' for x in lines)
def checklist(lines, heading='Features'):
    return '<h2>'+heading+'</h2><ul class="checklist">'+''.join('<li>'+html.escape(x)+'</li>' for x in lines)+'</ul>'
def ordering(name, alt):
    picture=img(name,alt)
    width=Image.open(Path('reference/img/images')/name).width
    return f'<figure class="ordering" style="max-width:{width*1.25:g}px"><a href="/assets/img/{name}">{picture}</a><figcaption><a href="/assets/img/{name}">Open full size</a></figcaption></figure>'
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
    result=paras(lines[:1])+'<aside class="product-image">'+img(photo,title)+'</aside>'
    if features: result+=checklist(features)
    for i,line in enumerate(lines[1:],1): result+='<h2>'+headings[i]+'</h2>'+paras([line])
    if model == '300B': result+=checklist(specs,'Specifications')
    return result
write('/','Oil level regulators and compressor accessories','<section class="hero"><div class="wrap"><h1>Oil level regulators and compressor accessories</h1><p>Since 1939, GARZO has been providing quality lubrication regulating systems to the stationary equipment and natural gas compression industries.</p><div class="actions"><a class="button" href="/products/">Explore products</a><a class="textlink" href="/contact/">Contact us <span>→</span></a></div></div></section><section class="section wrap"><div class="section-title"><h2>Products</h2><a href="/products/">View all products →</a></div>'+cards()+'</section><section class="band"><div class="wrap band-inner"><div><h2>Request a catalog</h2><p>Garzo catalogs are sent out by bulk mail. Please allow 1-4 weeks for delivery.</p></div><a class="button" href="/catalog-request/">Request a catalog</a></div></section>')
write('/products/','Products',banner('Products','Oil level regulators, shut down devices, low flow meters, lubricator box controls, oil reservoirs and linear diaphragm operators.',False)+'<section class="section wrap">'+cards()+'<div class="additional"><h2>Shut-down devices &amp; oil reservoirs</h2><p>Contact Garzo Products for information about shut-down devices and oil reservoirs.</p><a class="button dark" href="/contact/">Contact us</a></div></section>')
items=[('101','oil-level-regulators/101','101.html','101b.jpg'),('108','oil-level-regulators/108','108.html','108b.jpg'),('300B','low-flow-meters','meter.html','300b.jpg'),('211','lubricator-box-controls/211','211.html','211-08.jpg')]
for model,path,old,photo in items:
    lines=source(old); lines=lines[1:]
    title={'101':'Oil level regulator 101B','108':'Oil level regulator 108B','300B':'Low flow meter 300B','211':'Lubricator box control 211'}[model]
    extra=''
    if model=='101': extra='<h2>How to order</h2>'+ordering('order.jpg','Model 101 ordering information')
    if model=='108': extra='<p><a href="/products/oil-level-regulators/108/installation/">108B installation guide →</a></p><h2>How to order</h2>'+ordering('order108.jpg','Model 108 ordering information')
    if model=='300B': extra='<h2>Diagram</h2>'+ordering('300bdia.jpg','300B low flow meter diagram')
    if model=='211': extra='<p><a href="/products/lubricator-box-controls/213/">Model 213 →</a></p>'
    body=banner(title)+f'<section class="section wrap product"><div class="product-copy">{product_content(lines,model,photo,title)}{extra}<p><a class="button dark" href="/contact/">Contact us</a></p></div></section>'
    write('/products/'+path+'/',title,body)
write('/products/lubricator-box-controls/213/','Lubricator box control 213',banner('Lubricator box control 213')+'<section class="section wrap"><p>Contact Garzo Products for information on Model 213.</p><a class="button dark" href="/contact/">Contact us</a></section>')
lines=source('install.html')[1:]
steps=[]
for i, line in enumerate(lines[1:], 1):
    content=html.escape(re.sub(r'^\d+\.\s*', '', line))
    if i == 4: content+='<div class="figures">'+''.join(img(f'fig{n}.jpg',f'Installation figure {n}') for n in (1,2,3))+'</div>'
    steps.append('<li>'+content+'</li>')
write('/products/oil-level-regulators/108/installation/','108B installation guide',banner('108B installation guide')+'<section class="section wrap narrow product-detail"><h2>Basic installation</h2><ol class="installation-steps">'+''.join(steps)+'</ol></section>')
lines=source('diap.html')[1:]
body=banner('Linear diaphragm operators')+'<section class="section wrap product-detail"><div class="product"><div class="product-copy">'+paras(lines[:1])+'<aside class="product-image">'+img('501gp.jpg','Linear diaphragm operators')+'</aside>'+checklist(lines[4:12])+'<h2>Construction</h2>'+paras(lines[1:2])+'<h2>Spring rates</h2>'+paras(lines[2:3])+checklist(lines[13:],'Specifications')+'</div></div><div class="modelnav">'+''.join(f'<a href="#model-501-{n}">501-{n}</a>' for n in (4,6,12,18,25))+'</div>'
for n in (4,6,12,18,25):
    body+=f'<section class="model" id="model-501-{n}"><h2>Model 501-{n}</h2><div class="figure-grid">'+img(f'501{n}.jpg',f'Model 501-{n}')+ordering(f'501{n}chart.jpg',f'Model 501-{n} specifications chart')+'</div>'
    for name in {4:['0932.jpg'],6:['0114.jpg','mount5016.jpg'],12:['0115.jpg','mount5012.jpg'],18:[],25:['0116.jpg']}[n]: body+=ordering(name,f'Model 501-{n} diagram')
    body+='</section>'
body+='<h2>Spring chart</h2>'+ordering('springchart.jpg','Spring chart')+'<h2>How to order</h2>'+ordering('order501.jpg','501 ordering information')+'<p><a class="button dark" href="/contact/">Contact us</a></p></section>'
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
(S/'404.html').write_text(layout('Page not found',banner('Page not found','',False)+'<section class="section wrap"><a href="/">Return home →</a></section>','/404.html'))
(S/'assets/img/favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" fill="#15232d"/><text x="32" y="46" text-anchor="middle" font-family="Arial" font-weight="bold" font-size="43" fill="#f2c94c">G</text></svg>')
for p in I.iterdir():
    if p.name not in used and p.name!='favicon.svg': p.unlink()
paths=['/','/products/','/products/oil-level-regulators/101/','/products/oil-level-regulators/108/','/products/oil-level-regulators/108/installation/','/products/low-flow-meters/','/products/lubricator-box-controls/211/','/products/lubricator-box-controls/213/','/products/linear-diaphragm-operators/','/catalog-request/','/product-registration/','/contact/']
(S/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>https://garzoproducts.com'+p+'</loc></url>' for p in paths)+'</urlset>')
(S/'robots.txt').write_text('User-agent: *\nDisallow: /\nSitemap: https://garzoproducts.com/sitemap.xml\n')
redirect={'index.html':'/','sitemap.html':'/products/','products.html':'/products/','register.html':'/product-registration/','contact.html':'/contact/','108.html':'/products/oil-level-regulators/108/','101.html':'/products/oil-level-regulators/101/','install.html':'/products/oil-level-regulators/108/installation/','meter.html':'/products/low-flow-meters/','211.html':'/products/lubricator-box-controls/211/','213.html':'/products/lubricator-box-controls/213/','other.html':'/products/','main.html':'/'}
for old,n in [('diap',4),('5014',4),('5016',6),('50112',12),('50118',18),('50125',25)]: redirect[old+'.html']=f'/products/linear-diaphragm-operators/#model-501-{n}'
(S/'_redirects').write_text(''.join(f'/{a} {b} 301\n' for a,b in redirect.items()))
(S/'_headers').write_text('/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  X-Frame-Options: DENY\n  X-Robots-Tag: noindex\n\n/assets/*\n  Cache-Control: public, max-age=31536000, immutable\n')
