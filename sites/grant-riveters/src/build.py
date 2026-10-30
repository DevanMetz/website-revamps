from pathlib import Path
from html import escape
from urllib.parse import quote, unquote
from bs4 import BeautifulSoup
from PIL import Image
import re, json, shutil, csv
from data import PAGES, IMAGES, PRODUCT_IMAGES, LITERATURE
from content.products import ORBITAL_INTRO, PNEUMATIC, HYDRAULIC, SERVO, PRODUCTS
ROOT=Path(__file__).resolve().parent.parent; SITE=ROOT/'site'; REF=ROOT/'reference'
for key,path in IMAGES.items():
 im=Image.open(REF/'img'/path); im.seek(0); im=im.convert('RGB' if im.format=='JPEG' else 'RGBA'); out=SITE/'assets/img'/f'{key}.png'; im.save(out,optimize=True)
 if key=='orbitfeed':
  # Trim the baked-in white mat and drop shadow around the source photo.
  import numpy as _np; _a=_np.asarray(im.convert('RGB')).astype(int); _m=(_a.max(2)-_a.min(2))>60
  _r=_np.where(_m.mean(1)>0.5)[0]; _c=_np.where(_m.mean(0)>0.5)[0]
  im.crop((_c.min()+1,_r.min()+1,int(_c.min()+(_c.max()-_c.min())*.62),_r.max())).save(out,optimize=True)
logo = Image.open(REF/'img/image/2007 logo.gif').convert('RGBA')
# Remove only border-connected white, preserving enclosed details.
import numpy as np
from scipy import ndimage
pixels = np.array(logo)
white = np.all(pixels[:, :, :3] >= 240, axis=2)
seed = np.zeros(white.shape, dtype=bool)
seed[0, :] = seed[-1, :] = True
seed[:, 0] = seed[:, -1] = True
background = ndimage.binary_propagation(seed & white, mask=white)
pixels[background, 3] = 0
edge = ndimage.binary_dilation(background) & ~background
pixels[edge, 3] = np.minimum(pixels[edge, 3], 192)
logo = Image.fromarray(pixels)
# Keep the complete wordmark with a small transparent margin on every side.
logo.crop((22, 14, 315, 60)).save(SITE/'assets/img/wordmark.png', optimize=True)
def img(key,alt):
 name=f'{key}-transparent.png' if key in {'bench','impact','inspector','kit','power','press','servo'} else f'{key}.png'; im=Image.open(SITE/'assets/img'/name); return f'<img src="/assets/img/{name}" alt="{escape(alt)}" width="{im.width}" height="{im.height}" loading="lazy">'
def tile_img(key,alt):
 name=f'{key}-transparent.png' if key in {'bench','impact','inspector','kit','power','press','servo'} else f'{key}.png'
 im=Image.open(SITE/'assets/img'/name)
 return img(key,alt).replace('<img ', f'<img class="photo-{key}" style="width:{im.width * 1.25:g}px" ')
def link(label,url): return f'<a href="{url}">{escape(label)} <span aria-hidden="true">→</span></a>'
def cards(items): return '<div class="cards">'+''.join(f'<a class="card" href="{u}"><span>{escape(t)}</span><b aria-hidden="true">→</b></a>' for t,u in items)+'</div>'
nav=[('Riveters','/riveters/'),('Presses','/presses/'),('Riveting kits','/riveting-kits/'),('Automation','/automation/'),('Services','/services/'),('Literature','/literature/')]
def layout(title,desc,body,path):
 links='\n'.join(f'<a href="{u}"'+(' aria-current="page"' if path==u.strip('/') or (u=='/riveters/' and path.startswith('riveters/')) else '')+f'>{t}</a>' for t,u in nav)
 data={'@context':'https://schema.org','@type':'Organization','name':'Grant Riveters','url':'https://www.grantriveters.com/','telephone':['800-227-2150','203-366-4557'],'faxNumber':'203-366-0370','email':'sales@grantriveters.com','address':{'@type':'PostalAddress','streetAddress':'90 Silliman Avenue, P.O. Box 3350','addressLocality':'Bridgeport','addressRegion':'Connecticut','postalCode':'06605','addressCountry':'USA'}}
 return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex"><title>{escape(title)} | Grant Riveters</title><meta name="description" content="{escape(desc,quote=True)}"><meta property="og:title" content="{escape(title)} | Grant Riveters"><meta property="og:description" content="{escape(desc,quote=True)}"><meta property="og:type" content="website"><meta property="og:url" content="https://www.grantriveters.com/{path}/"><link rel="icon" href="/assets/img/favicon.svg"><link rel="preload" href="/assets/fonts/barlow-semi-800-italic.woff2" as="font" type="font/woff2" crossorigin><link rel="stylesheet" href="/assets/css/site.css"><script type="application/ld+json">{json.dumps(data)}</script><script src="/assets/js/site.js" defer></script></head><body><a class="skip" href="#main">Skip to content</a><header><div class="masthead wrap"><a class="brand" href="/" aria-label="Grant Riveters home"><img src="/assets/img/wordmark.png" alt="Grant Riveters" width="293" height="46"></a><a class="header-phone" href="tel:8002272150">800-227-2150</a><a class="button header-quote" href="/request-a-quote/">Request a quote</a><button class="menu" aria-expanded="false" aria-controls="navigation">Menu</button></div><div class="nav-row"><nav class="wrap" id="navigation" aria-label="Main navigation">{links}<a class="nav-quote" href="/request-a-quote/">Request a quote</a></nav></div></header><main id="main">{body}</main><footer><div class="wrap footer-grid"><div><a class="brand footer-brand" href="/"><img src="/assets/img/wordmark.png" alt="Grant Riveters" width="293" height="46"></a><p>A Woman Owned Company</p><p>90 Silliman Avenue<br>P.O. Box 3350<br>Bridgeport, Connecticut 06605, USA</p></div><div><h2>Contact</h2><p><a href="tel:8002272150">800-227-2150</a> · Sales ext. 101<br><a href="tel:2033664557">203-366-4557</a><br>Fax 203-366-0370<br><a href="mailto:sales@grantriveters.com">sales@grantriveters.com</a></p></div><div><h2>Explore</h2><a href="/riveting-methods/">Riveting methods</a><a href="/process-inspector/">Process Inspector</a><a href="/history/">History</a><a href="/sales-representatives/">Sales representatives</a><a href="/contact/">Contact</a></div></div></footer></body></html>'''
def hero(title,desc): return f'<section class="page-hero"><div class="wrap"><h1>{escape(title)}</h1></div></section>'
def source_content(files):
 parts=[]; seen=set()
 bad=['copyright','last modified','2012','2010','2007','price','call today','call us','sales@','800-227','click on','http:','other guys','competitor','world today','celebrat','information request','send product literature','require a quotation','salesperson contact','your banner','thank you for helping']
 def clean(text):
  text=' '.join(text.split()).replace('!', '.')
  text=re.split(r'Information Request Form|Select the items that apply', text, flags=re.I)[0]
  sentences=re.split(r'(?<=[.!?])\s+',text)
  return ' '.join(x for x in sentences if not any(y in x.lower() for y in bad))
 for f in files:
  p=REF/'html'/(f+'.html')
  if not p.exists(): continue
  soup=BeautifulSoup(p.read_text(errors='replace'),'html.parser')
  for el in soup.find_all(['p','li','table']):
   if el.name in ('p','li'):
    if el.find_parent('li') or any(len(t.find_all('tr'))>3 and not t.find_all('table') for t in el.find_parents('table')): continue
    text=clean(el.get_text(' ',strip=True))
    if len(text)<25 or text in seen: continue
    seen.add(text)
    if el.name=='li': parts.append('<ul><li>'+escape(text)+'</li></ul>')
    else:
     chunks=[]; chunk=''
     for sentence in re.split(r'(?<=[.!?])\s+',text):
      if len(chunk)+len(sentence)>800 and chunk: chunks.append(chunk); chunk=''
      chunk=(chunk+' '+sentence).strip()
     if chunk: chunks.append(chunk)
     parts.extend('<p>'+escape(c)+'</p>' for c in chunks)
   else:
    if el.find('table') and len(el.find_all('tr'))>20: continue
    rows=[]
    for tr in el.find_all('tr'):
     cells=[' '.join(c.get_text(' ',strip=True).split()).replace('!','.') for c in tr.find_all(['td','th'],recursive=False)]
     if len(cells)>1 and any(cells): rows.append(cells)
    raw=' '.join(' '.join(r) for r in rows).lower()
    if len(rows)<3 or any(x in raw for x in ['price','$','information request','e-mail','sales@','copyright','home |','call today']): continue
    if max(map(len,rows))>10 or max(len(' '.join(r)) for r in rows)>600: continue
    # Old dimension tables split the row label across two cells.
    width=max(map(len,rows))
    for row in rows:
     if len(row)==width and len(row)>2 and 'overall dimensions' in row[0].lower():
      row[:2]=['Overall '+row[1].lower()]
     elif row[0].lower() in ['width','height']:
      row[0]='Overall '+row[0].lower()
    width=max(map(len,rows)); rows=[r+['']*(width-len(r)) for r in rows]
    key=str(rows)
    if key in seen: continue
    seen.add(key)
    parts.append('<div class="table-wrap" tabindex="0" role="region" aria-label="Specifications, scroll horizontally to see all models"><table><tbody>'+''.join('<tr>'+''.join((('<th scope="col">' if j==0 else '<th scope="row">') if i==0 or j==0 else '<td>')+escape(c)+('</th>' if i==0 or j==0 else '</td>') for i,c in enumerate(row))+'</tr>' for j,row in enumerate(rows))+'</tbody></table></div>')
 return ''.join(parts)
def fields(quoteform=False):
 c=('<fieldset><legend>Request</legend>'+''.join(f'<label class="check"><input type="checkbox" name="{x}"> {x}</label>' for x in ['Send product literature','Require a quotation','Have a salesperson contact me'])+'</fieldset>' if not quoteform else '')+'<div class="form-grid">'
 for label,typ,auto,req in [('Name','text','name',True),('Title','text','organization-title',False),('Company','text','organization',False),('E-mail','email','email',True),('Phone','tel','tel',False),('Fax','tel','off',False)]:
  c+=f'<label>{label}<input name="{label}" type="{typ}" autocomplete="{auto}"'+(' required' if req else '')+'></label>'
 c+='</div><label>Address<textarea name="Address" autocomplete="street-address"></textarea></label>'
 if quoteform:
  opts={'Rivet material':['Mild steel','Hard steel','Stainless steel','Non-ferrous','Other material'],'Rivet type':['Solid','Semi-tubular','Tubular','Other shape'],'Rivet style':['Shoulder','Straight shank'],'Rivet tightness':['Tight assembly','Loose assembly','Special requirements'],'Process type':['Orbital','Impact','Twin Spin','Spin Press','Multi-Spin','Pressing application'],'Machine type':['Riveting kit','Bench unit w/o bench','Bench unit w/ bench','Power head w/o electrics & pneumatics','Power head w/ electrics & pneumatics','Automatic feed','Floor riveter','Floor unit'],'System type':['Riveting kit','Stand alone work cell','Rotary system','Automated system','Other system'],'Actuation type':['Pneumatic','Air over oil','Air over oil 100% real-time inspection','Hydraulic','Servo electric','Lowest price','Pneumatic real-time inspection','Hydraulic real-time inspection','Servo real-time inspection'],'Do you have multi-process requirements?':['No','Yes',"Don’t know"]}
  c+='<div class="form-grid">'+''.join(f'<label>{k}<select name="{k}"><option value="">Select one</option>'+''.join(f'<option>{escape(o)}</option>' for o in v)+'</select></label>' for k,v in opts.items())+'<label>Rivet diameter<input name="Rivet diameter"></label></div><label>Rivet length under the head or length protruding above the assembly, and other information<textarea name="Rivet length and other information"></textarea></label>'
 else:c+='<label>Comments<textarea name="Comments"></textarea></label>'
 return '<!-- Replace the mailto fallback with a production form endpoint here. --><form data-mail-form>'+c+'<button class="button" type="submit">Send request</button><p class="status" role="status"></p></form>'
DOC_LABELS = {
 'AP_SERIES.zip':'AP series', 'AX_SERIES.zip':'AX series', 'DrillPress.pdf':'Drill press',
 'HyPower Catalog.pdf':'Hy-Power catalog', 'Model 16 left 3802.pdf':'Model 16 left',
 'Model 16 right 3805.pdf':'Model 16 right', 'Pneumatic_Press_2010_sm.pdf':'Pneumatic presses',
 'Pneumatic_Riveters_2010_sm.pdf':'Pneumatic riveters', 'Process_Inspector_2010_sm.pdf':'Process Inspector',
 'Riveting_Kit_2010_sm.pdf':'Riveting kits', 'XYZ _2010_sm.pdf':'XYZ riveting systems',
 'alfapc0699-c.pdf':'Hydro-pneumatic cylinders', 'servo-riveters.pdf':'Servo riveters'}
def doc_label(name):
 p=SITE/'assets/docs'/name
 return f"{DOC_LABELS[name]} ({p.suffix[1:].upper()}, {p.stat().st_size/1024/1024:.1f} MB)"
def cell(text):
 text=escape(text)
 # Keep each number and its printed unit together, and separate paired measurements.
 text=re.sub(r'(?<=\d) (?=(?:mm|inch|lbs|Lbs|Kg|Kg/Cm²|psi|PSI|Hp|Kw|Ton|seconds|bar|nl|kg|mm/sec)\b)', '&nbsp;', text)
 text=re.sub(r' \(([^()]*(?:mm|Kg/Cm²)[^()]*)\)', r'<br>(\1)', text)
 text=re.sub(r'(?<=inch) (?=\d)|(?<=&quot;) (?=\d)', '<br>', text)
 text=re.sub(r'(?<=psi) (?=\d)', '<br>', text, flags=re.I)
 text=re.sub(r'(?<=Hp) (?=\d)', '<br>', text)
 return text
def source_rows(filename, marker):
 soup=BeautifulSoup((REF/'html'/(filename+'.htm.html')).read_text(errors='replace'),'html.parser')
 for tr in soup.find_all('tr'):
  cells=[' '.join(c.get_text(' ',strip=True).split()) for c in tr.find_all(['td','th'],recursive=False)]
  if cells and cells[0].strip().lower()==marker.lower():
   table=tr.find_parent('table'); rows=[]
   for row in table.find_all('tr'):
    if row.find_parent('table') is not table: continue
    values=[' '.join(c.get_text(' ',strip=True).split()) for c in row.find_all(['td','th'],recursive=False)]
    if values: rows.append(values)
   return rows
 return []
def orbital_table(filename):
 rows=source_rows(filename,'MODEL'); start=next(i for i,r in enumerate(rows) if r[0].lower()=='model'); rows=rows[start:]
 models=rows[0][1:]; specs=[]
 for row in rows[1:]:
  if row[0].lower()=='standard features': break
  if row[0].lower()=='overall dimensions': row=['Overall '+row[1]]+row[2:]
  elif row[0].lower() in ('width','height'): row=['Overall '+row[0]]+row[1:]
  if len(row)==len(models)+1: specs.append((row[0],row[1:]))
 return table(models,specs)
def press_table():
 rows=source_rows('pneumaticpress','Technical Data'); rows=rows[next(i for i,r in enumerate(rows) if r[0]=='Technical Data'):]; models=rows[0][1:]; specs=[]
 for row in rows[1:]:
  if row[0]=='Standard Features': break
  if len(row)==len(models) and specs:
   label,values=specs[-1]; specs[-1]=(label,[a+'\n'+b for a,b in zip(values,row)]); continue
  if row[0]=='Overall Dimensions': row=['Overall '+row[1]]+row[2:]
  elif row[0] in ('Width','Height'): row=['Overall '+row[0]]+row[1:]
  elif row[0]=='Force Output at': row=['Force Output at '+row[1]]+row[2:]
  elif row[0]=='': row=['Force Output at '+row[1]]+row[2:]
  if len(row)==len(models)+1: specs.append((row[0],row[1:]))
 return table(models,specs)
def mop_table():
 rows=source_rows('prod05','VALID FOR ALL VERSIONS'); specs=[('Power fluid',['filtered air max 6 bar']*4)]
 for row in rows[3:]:
  if len(row)>=3:
   values=row[2:]; values=(values*4)[:4] if len(values)==1 else values
   specs.append((row[0]+(' ('+row[1]+')' if row[1] else ''),values))
 return table(['07','15','30','50'],specs)
def table(models, rows):
 return '<div class="table-wrap" tabindex="0" role="region" aria-label="Specifications, scroll horizontally to see all models"><table><thead><tr><th scope="col">Model</th>'+''.join('<th scope="col">'+escape(x)+'</th>' for x in models)+'</tr></thead><tbody>'+''.join('<tr><th scope="row">'+escape(label)+'</th>'+''.join('<td>'+cell(x).replace('\n','<br>')+'</td>' for x in values)+'</tr>' for label,values in rows)+'</tbody></table></div>'
def product_body(path):
 out=''
 if path.startswith('riveters/orbital/'):
  bench=path.endswith('bench-top')
  out+='<nav class="anchors" aria-label="Riveter variants"><a href="#pneumatic">Pneumatic</a><a href="#hydraulic">Hydraulic</a><a href="#servo-electric">Servo-electric</a></nav>'
  out+='<div class="product-intro">'
  if bench: out+='<p>'+' '.join(escape(p) for p in ORBITAL_INTRO)+' We offer a standard two-year factory warranty.</p>'
  else: out+='<p>Power-head riveters offer Orbital, Twin-Spin, Multi-Spin and Spin-Press forming techniques. Typical cycle time is 0.5 to 1.5 seconds for most applications.</p>'
  out+='<p>The riveters have a modular design and support Orbital, Twin-Spin, Multi-Spin and Spin-Press forming. Pneumatic and hydraulic models are available with adjustable stroke and multi-process tooling.</p>'
  out+='</div>'
  intro=out[out.index('<div class="product-intro">'):]
  out=out[:out.index('<div class="product-intro">')]
  for label,anchor,key,data in [('Pneumatic','pneumatic','bench' if bench else 'power',PNEUMATIC),('Hydraulic','hydraulic','hydraulic',HYDRAULIC),('Servo-electric','servo-electric','servo',SERVO)]:
   models=data['models'] if bench or anchor!='pneumatic' else ['G003','G005','G008','G012','G016']
   caps=list(data['capacity'])
   if bench and anchor=='hydraulic': caps[-1]='1.250" DIA. (38 mm)'
   benefits=[]
   if anchor=='pneumatic': benefits+=['Precision micrometer stroke adjustment','Festo pneumatics, Siemens electrical components and SKF bearings']
   elif anchor=='hydraulic': benefits+=['Precision micrometer stroke adjustment','Bearings lubricated for life','Tempo-Sonic III and servo or proportional valve upgrades available']
   else: benefits+=['Programmable stroke and profile','Real-time inspection','Emerson servo components']
   out+='<section id="'+anchor+'"><h2>'+label+'</h2><div class="variant-layout"><div class="product-photo">'+img(key,label+' riveter')+'</div><div>'+('<p>The servo-electric riveter is programmable in spindle stroke velocity, profile, forming pressure and depth.</p>' if anchor=='servo-electric' else '')+'<h3>Features</h3><ul>'+''.join('<li>'+escape(b)+'</li>' for b in benefits)+'</ul>'
   out+='</div></div>'+(intro if anchor=='pneumatic' else '')+orbital_table(anchor.replace('-electric','')+('bt' if bench else 'ph'))
   out+='<p>'+('These riveters are backed with a two-year warranty and are 100% guaranteed.' if anchor=='pneumatic' else 'These riveters are backed with a three-year warranty and are 100% guaranteed.')+'</p></section>'
  return out
 for label,key,paragraphs,benefits,models,values in PRODUCTS[path]:
  out+='<section><h2>'+escape(label)+'</h2><div class="product-photo">'+img(key,label)+'</div>'+''.join('<p>'+escape(p)+'</p>' for p in paragraphs)
  if benefits: out+='<h3>Key benefits</h3><ul>'+''.join('<li>'+escape(x)+'</li>' for x in benefits)+'</ul>'
  if path=='presses': out+=press_table() if label=='Pneumatic presses' else mop_table()
  elif models:
   rows=[('Capacity' if path!='riveting-kits' else 'Process',values)] if values else []
   if path=='riveting-kits': rows.append(('Anvil',['No','Yes','No','Yes','No','No','No','Yes','Yes']))
   out+=table(models,rows)
  if path=='riveters/impact': out+='<p>Grant Riveters are 100% guaranteed and placed into service with a Two-Year Warranty.</p>'
  if path=='presses' and label=='Pneumatic presses': out+='<p>Standard 5-Year Limited Warranty.</p>'
  out+='</section>'
 return out
family=[('Bench-top orbital riveters','/riveters/orbital/bench-top/','bench'),('Power-head orbital riveters','/riveters/orbital/power-head/','power'),('Orbitfeed','/riveters/orbitfeed/','orbitfeed'),('Double-ended riveters','/riveters/double-ended/','double'),('Impact riveters','/riveters/impact/','impact'),('Hydraulic squeeze riveters','/riveters/squeeze/','squeeze'),('Pneumatic presses & cylinders','/presses/','press'),('Riveting kits','/riveting-kits/','kit'),('Automation','/automation/','automation'),('Process Inspector','/process-inspector/','inspector')]
lineup=[('Bench-top','bench','/riveters/orbital/bench-top/'),('Impact','impact','/riveters/impact/'),('Power-head','power','/riveters/orbital/power-head/'),('Presses','press','/presses/'),('Process Inspector','inspector','/process-inspector/'),('Riveting kits','kit','/riveting-kits/')]
home='<section class="hero"><div class="wrap hero-inner"><h1>Orbital, impact and squeeze riveting machines</h1><div class="actions"><a class="button" href="#machines">Explore machines</a><a class="text-action" href="/request-a-quote/">Request a quote →</a></div><div class="lineup">'+''.join(f'<a href="{url}" class="lineup-item"><div>{img(key,label)}</div><span>{label}</span></a>' for label,key,url in lineup)+'</div></div></section><section class="section wrap" id="machines"><div class="section-head"><h2>Riveting machines</h2></div><div class="product-grid">'+''.join(f'<a class="product" href="{u}"><div class="image-well image-{k}">{tile_img(k,t)}</div><h3>{t}</h3></a>' for t,u,k in family)+'</div></section><section class="section wrap home-services"><div><h2>Contract riveting services</h2><p>Grant Riveters offers contract riveting, prototyping and consulting for product design, rivets and riveting process selection.</p>'+link('Our services','/services/')+'</div><div class="home-links">'+link('Riveting methods','/riveting-methods/')+link('Company history','/history/')+'</div></section>'

def separate_actions(html):
 # Preserve a textual boundary between adjacent interactive elements.
 return re.sub(r'</a>(?=<(?:a|button)\b)', '</a>\n', html)
def write(path,title,desc,body):
 out=SITE/path/'index.html' if path else SITE/'index.html';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(separate_actions(layout(title,desc,body,path)))
write('','Riveting machines and assembly systems','Orbital, spin, impact and squeeze riveting machines, presses and automated systems.',home)
for path,(title,desc,files,items) in PAGES.items():
 body=hero(title,desc)+'<section class="section wrap content">'
 if items and path=='riveters': body+='<div class="product-grid family-grid">'+''.join(f'<a class="product" href="{u}"><div class="image-well image-{k}">{tile_img(k,t)}</div><h3>{t}</h3></a>' for t,u,k in family[:6])+'</div>'
 elif items: body+=cards(items)
 if path=='process-inspector': body+='<div class="feature">'+img('inspector','Process Inspector screen')+'<div><h2>Force and distance control</h2><p>Grant Riveters has implemented the Process Inspector™ controller in its riveter product line. The controller provides real-time force and distance data and alerts the operator to non-conforming parts.</p><p>The PLC/HMI features a color touch-screen control with a digital readout for setting force and distance triggers. Programs are generated from high and low distance and force data and saved under a preferred name.</p></div></div>'
 if path=='process-inspector': body+='<h2>Specifications</h2><p>The Process Inspector V570 combines a PLC and HMI with a 5.7-inch QVGA 256-color touch panel. It monitors force, distance and time for presses and riveters, with configurable measurement and force ranges. It stores up to 49 recipes and has 24 inputs and 23 outputs, expandable. Sensors include strain gage, piezoelectric and potentiometric sensors.</p>'
 if path=='sales-representatives': body+='<p>For sales assistance, contact Grant Riveters at <a href="tel:8002272150">800-227-2150</a>, sales extension 101, or <a href="mailto:sales@grantriveters.com">sales@grantriveters.com</a>.</p>'
 if path=='riveting-methods': body+='<p>Grant Riveters’ “Tailor-Made” system fits the machine to the job. The product line includes orbital, spin riveting, impact, squeeze, blind and press type riveting.</p><h2>Forming processes</h2><p>Orbital, Multi-Spin™, Twin-Spin™ and Spin-Press™ forming techniques are available.</p>'
 if path=='history': body+='<p>Grant Manufacturing and Machine Company’s first invention was in 1860. The company was incorporated in 1904 and its history includes steam engines, the tire valve, the vertical motor, the spark plug and innovations in riveting.</p>'
 if path in PRODUCTS or path.startswith('riveters/orbital/'):
  body+=product_body(path)
 elif path!='riveters':
  body+=source_content(files)
 if path in LITERATURE:
  body+='<h2>Literature</h2><ul>'+''.join(f'<li><a href="/assets/docs/{quote(name)}">{escape(doc_label(name))}</a></li>' for name in LITERATURE[path])+'</ul>'
 if path in PRODUCTS or path.startswith('riveters/orbital/') or path in ('process-inspector','services'): body+='<p class="cta-link">'+link('Request a quote','/request-a-quote/')+'</p>'
 body+='</section>'
 write(path,title,desc,body)
for path,title in [('contact','Contact'),('request-a-quote','Request a quote')]:
 body=hero(title,'Contact Grant Riveters about your application.')+'<section class="section wrap contact-layout"><div><h2>Grant Riveters</h2><p>90 Silliman Avenue<br>P.O. Box 3350<br>Bridgeport, Connecticut 06605, USA</p><p><a href="tel:8002272150">800-227-2150</a> (sales: ext. 101)<br><a href="tel:2033664557">203-366-4557</a><br>Fax 203-366-0370<br><a href="mailto:sales@grantriveters.com">sales@grantriveters.com</a></p></div><div>'+fields(path=='request-a-quote')+'</div></section>'
 write(path,title,'Contact Grant Riveters about your application.',body)
docs=list((SITE/'assets/docs').iterdir()); body=hero('Product literature','Grant Riveters product literature and specifications.')+'<section class="section wrap"><div class="docs">'+''.join(f'<a href="/assets/docs/{quote(p.name)}"><span>{escape(doc_label(p.name))}</span><b>↓</b></a>' for p in sorted(docs))+'</div></section>';write('literature','Product literature','Grant Riveters product literature and specifications.',body)
(SITE/'404.html').write_text(separate_actions(layout('Page not found','The requested page could not be found.',hero('Page not found','The requested page could not be found.')+'<section class="section wrap"><a href="/">Return home</a></section>','404')))
# Redirect each crawled path, including unsuccessful paths.
mapnames={'products':'riveters','prodbt':'riveters/orbital/bench-top','pneumaticbt':'riveters/orbital/bench-top','hydraulicbt':'riveters/orbital/bench-top','servobt':'riveters/orbital/bench-top','prodph':'riveters/orbital/power-head','pneumaticph':'riveters/orbital/power-head','hydraulicph':'riveters/orbital/power-head','servoph':'riveters/orbital/power-head','servo electric riveters':'riveters/orbital/bench-top','orbitfeed':'riveters/orbitfeed','double-ended':'riveters/double-ended','prod03':'riveters/impact','prod04':'riveters/squeeze','prod06':'riveters','prod05':'presses','pneumaticpress':'presses','aostandardfeatures':'presses','aoproductoptions':'presses','prodrk':'riveting-kits','automation':'automation','riveting_methods':'riveting-methods','riveting methods':'riveting-methods','toolsandtheprocesses':'riveting-methods','prod02':'riveting-methods','grantadvantage':'riveting-methods','services':'services','rivetingserv':'services','proto-typing':'services','consulting':'services','granthistory':'history','reps':'sales-representatives','contact_information':'contact','feedback':'contact','rfq':'request-a-quote','literature':'literature','grantrivetersvideo':'automation','search':'','register':'contact','toc':'','oldhomepage1':'','news':'','index':''}
redirects={}
with (REF/'pages.tsv').open() as f:
 for row in csv.DictReader(f,delimiter='\t'):
  old=row['old_path']; key=unquote(old).strip('/').removesuffix('.htm').lower(); dest='/'+mapnames.get(key,'')+'/' if mapnames.get(key,'') else '/'
  if old!='/' and old!=dest: redirects[old]=dest
for p in docs:
 for prefix in ['/','/docs/','/pdf/']:
  redirects[prefix+quote(p.name)]='/assets/docs/'+quote(p.name)
(SITE/'_redirects').write_text(''.join(f'{k} {v} 301\n' for k,v in redirects.items()))
(SITE/'_headers').write_text('/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  X-Frame-Options: DENY\n  X-Robots-Tag: noindex\n/assets/*\n  Cache-Control: public, max-age=31536000, immutable\n')
(SITE/'robots.txt').write_text('User-agent: *\nDisallow: /\nSitemap: https://www.grantriveters.com/sitemap.xml\n')
paths=['']+list(PAGES)+['contact','request-a-quote','literature'];(SITE/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>https://www.grantriveters.com/'+p+('/' if p else '')+'</loc></url>' for p in paths)+'</urlset>')
(SITE/'assets/img/favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" fill="#b5272d"/><text x="32" y="45" text-anchor="middle" font-family="sans-serif" font-size="40" font-weight="bold" fill="white">G</text></svg>')
