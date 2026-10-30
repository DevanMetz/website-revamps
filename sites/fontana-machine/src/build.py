from pathlib import Path
from PIL import Image
from html import escape
import json
import shutil
from data import ROUTES
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'site'
(OUT / 'assets/fonts').mkdir(parents=True, exist_ok=True)
for font in (ROOT / 'src/fonts').glob('*.woff2'):
    shutil.copy2(font, OUT / 'assets/fonts' / font.name)
for source, dest in [('heavyturbine.gif','heavy-turbine.png'),('portablemachining.jpg','portable-machining.jpg'),('heavyclass.gif','heavy-class.png'),('heavyscmap.gif','heavy-map.png')]:
    im = Image.open(ROOT / 'src/assets/img/images' / source).convert('RGB')
    if dest == 'portable-machining.jpg':
        im = im.crop((12, 15, 134, 161))  # trim the baked-in white mat and shadow
    im.save(OUT / 'assets/img' / dest, quality=82, optimize=True)

shutil.copy2(ROOT / 'src/assets/logo/original.gif', OUT / 'assets/img/brand-header.gif')

def image(name, alt, w, h):
    return f'<img src="/assets/img/{name}" alt="{alt}" width="{w}" height="{h}">'

def page(title, desc, path, body):
    nav = '\n'.join(f'<li><a href="{url}"{(" aria-current=\"page\"" if path == url else "")}>{label}</a></li>' for label,url in [('Home','/'),('Directions','/directions/'),('Contact','/contact/'),('Privacy','/privacy/')])
    schema = {'@context':'https://schema.org','@type':'Organization','name':'Fontana Machine & Engineering Co.','url':'https://www.fontanamachine.com/','telephone':'909-823-0657','faxNumber':'909-823-0619','email':'info@FontanaMachine.com','address':{'@type':'PostalAddress','streetAddress':'10703 Poplar Ave','addressLocality':'Fontana','addressRegion':'CA','postalCode':'92337','addressCountry':'USA'}}
    strip = '<div class="emergency-strip"><div class="wrap"><span>24/7 emergency pager <a href="tel:9093221616">909-322-1616</a></span><span>Phone <a href="tel:9098230657">909-823-0657</a></span></div></div>'

    if path == '/contact/':
        strip = '<div class="emergency-strip"><div class="wrap"><span>24/7 emergency pager <a href="tel:9093221616">909-322-1616</a></span></div></div>'
    footer_details = '' if path == '/contact/' else '<div><a href="tel:9098230657">909-823-0657</a><br>Fax 909-823-0619<br>Pager <a href="tel:9093221616">909-322-1616</a><br><a href="mailto:info@fontanamachine.com">info@FontanaMachine.com</a></div>'
    back = '<div class="inner-back"><div class="wrap"><a href="/">← Home</a></div></div>' if path != '/' else ''
    html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>{title} | Fontana Machine &amp; Engineering Co.</title><meta name="description" content="{desc}"><meta property="og:title" content="{title} | Fontana Machine &amp; Engineering Co."><meta property="og:description" content="{desc}"><meta property="og:type" content="website"><meta property="og:url" content="https://www.fontanamachine.com{path}"><link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml"><link rel="preload" href="/assets/fonts/big-shoulders-display-latin-900-normal.woff2" as="font" type="font/woff2" crossorigin><link rel="stylesheet" href="/assets/css/site.css"><script type="application/ld+json">{json.dumps(schema)}</script><script src="/assets/js/site.js" defer></script></head><body><a class="skip" href="#main">Skip to content</a><header class="header">{strip}<div class="wrap header-inner"><a class="brand" href="/" aria-label="Fontana Machine &amp; Engineering"><img src="/assets/img/brand-header.gif" alt="Fontana Machine &amp; Engineering" width="600" height="75"><span aria-hidden="true">Fontana Machine &amp; Engineering</span></a><div class="header-actions"><button class="menu" type="button" aria-expanded="false" aria-controls="navigation">Menu</button></div><nav id="navigation" aria-label="Main navigation"><ul>{nav}</ul></nav><a class="header-contact" href="/contact/">Contact us</a></div></header><main id="main">{back}{body}</main><footer><div class="wrap footer-inner"><div><strong>Fontana Machine &amp; Engineering Co.</strong><p>10703 Poplar Ave<br>Fontana, CA 92337, USA</p></div>{footer_details}<a href="/privacy/">Privacy policy</a></div></footer></body></html>'''
    target = OUT / ('index.html' if path == '/' else path.strip('/') + '/index.html')
    target.parent.mkdir(parents=True, exist_ok=True); target.write_text(html)

home = f'''<section class="hero"><div class="wrap"><h1>Heavy machining and fabrication for aerospace and industry</h1><div class="actions"><a class="button" href="/contact/">Contact us</a> <a class="text-link light" href="/directions/">Get directions</a></div></div></section><div class="services"><section class="feature"><div class="feature-copy"><h2>Production &amp; prototype work</h2><p>We are fully equipped to handle even the smallest production or prototype work. Whether you require a piece weighing mere ounces or one up to 50 tons, our modern CNC equipped facility has close tolerance capabilities. Our plant is over 30,000 square feet on 5 acres.</p></div><figure class="feature-figure">{image('heavy-turbine.png','A large turbine in the machining shop',192,128)}</figure></section><section class="feature"><div class="feature-copy"><h2>Refurbishing &amp; in-place machining</h2><p>Refurbishing your manufacturing and machine tools should never be left to chance. Our team has the technical expertise and plant capabilities to get the job done right, on time, and on budget.</p></div><figure class="feature-figure">{image('portable-machining.jpg','In-place mobile machining',122,146)}</figure></section><section class="feature"><div class="feature-copy"><h2>Training &amp; mentor program</h2><p>Fontana Machine believes that with proper training and guidance our employees can accomplish anything. We support vocational training in the heavy machining high school program and at the community college level. We strongly believe in these programs and the importance of industry's involvement.</p></div><figure class="feature-figure">{image('heavy-class.png','A graduating class from the mentor program',114,91)}</figure></section></div><section class="location"><div class="wrap location-inner"><div><h2>Fontana, California</h2><p>Convenient to the Port of Los Angeles, Ontario International Airport and rail service.</p></div><a class="button" href="/directions/">Directions</a></div></section>'''
route_html = ''.join(f'<section class="route"><h2>{escape(k)}</h2><p>{escape(v)}</p></section>' for k,v in ROUTES.items())
directions = f'''<section class="page-head"><div class="wrap"><h1>Driving directions</h1><p>10703 Poplar Ave, Fontana, CA 92337</p><a class="text-link light" href="https://www.google.com/maps/search/?api=1&amp;query=10703+Poplar+Ave%2C+Fontana%2C+CA+92337">Open in Google Maps</a></div></section><div class="wrap directions"><div class="routes">{route_html}</div><aside class="map"><div class="photo-well">{image('heavy-map.png','Map showing Fontana Machine’s location',356,309)}</div></aside></div>'''
contact = '''<section class="page-head"><div class="wrap"><h1>Contact us</h1></div></section><div class="wrap contact-grid"><div class="contact-info"><p class="emergency-note">Available 24/7/365 for emergency repairs; contact us after hours by pager above.</p><div class="contact-details"><h2>Contact details</h2><p>Phone: <a href="tel:9098230657">909-823-0657</a><br>Fax: 909-823-0619<br>Email: <a href="mailto:info@fontanamachine.com">info@FontanaMachine.com</a></p><p>Fontana Machine &amp; Engineering Co.<br>10703 Poplar Ave<br>Fontana, CA 92337<br>USA</p></div></div><div class="inquiry"><h2>Send an inquiry</h2><!-- Replace the mailto fallback with a production form endpoint here. --><form id="inquiry"><div class="form-grid"><label>Name<input name="Name" autocomplete="name" required></label><label>Company<input name="Company" autocomplete="organization"></label><label>Phone<input name="Phone" type="tel" autocomplete="tel"></label><label>Email<input name="Email" type="email" autocomplete="email" required></label></div><label>Part size and weight<input name="Part size and weight"></label><label>Message<textarea name="Message" rows="6" required></textarea></label><button class="button" type="submit">Send inquiry</button><p id="form-status" role="status"></p></form></div></div>'''
privacy = '''<section class="page-head"><div class="wrap"><h1>Privacy policy</h1></div></section><div class="wrap prose"><p>Any information you send to us is company confidential. We will never sell or distribute it to individuals or organizations not owned or controlled by us. We will not place cookies on your system, nor will our server do so intentionally.</p></div>'''
page('Heavy machining and fabrication','Heavy machining and fabrication for aerospace and industry in Fontana, California.','/',home)
page('Directions','Driving directions to Fontana Machine & Engineering Co. in Fontana, California.','/directions/',directions)
page('Contact','Contact Fontana Machine & Engineering Co. for machining and emergency repairs.','/contact/',contact)
page('Privacy policy','Fontana Machine & Engineering Co. privacy policy.','/privacy/',privacy)
(OUT/'404.html').write_text((OUT/'privacy/index.html').read_text().replace('<title>Privacy policy', '<title>Page not found').replace('<h1>Privacy policy</h1>', '<h1>Page not found</h1>').replace(' aria-current="page"', '').replace('<div class="wrap prose"><p>Any information you send to us is company confidential. We will never sell or distribute it to individuals or organizations not owned or controlled by us. We will not place cookies on your system, nor will our server do so intentionally.</p></div>', '<div class="wrap prose"><a href="/">Return home</a></div>'))


# Preview-only "Keep this site" subscribe button, added to every page after the build.
# Set PREVIEW_SUBSCRIBE_URL = '' in src/data.py and rebuild to remove it.
from data import PREVIEW_SUBSCRIBE_URL
def add_preview_subscribe():
 import re
 from html import escape as esc
 site_dir=Path(__file__).resolve().parent.parent/'site'
 css=("a.preview-subscribe{position:fixed;right:max(20px,calc(env(safe-area-inset-right) + 12px));bottom:max(20px,calc(env(safe-area-inset-bottom) + 12px));z-index:19;display:inline-flex;align-items:center;min-height:66px;padding:0 27px;border-radius:999px;background:#660000;color:#fff;font:600 22.5px/1.1 'Work Sans',sans-serif;letter-spacing:.01em;text-transform:none;text-decoration:none;white-space:nowrap;box-shadow:0 9px 27px rgba(0,0,0,.22);transition:background-color .15s,opacity .2s,visibility .2s}"
  "a.preview-subscribe:hover{background:#4a0000;color:#fff;text-decoration:none}"
  "a.preview-subscribe:focus-visible{background:#660000;color:#fff;outline:3px solid #7b0c12;outline-offset:3px;box-shadow:0 0 0 3px #fff,0 6px 18px rgba(0,0,0,.22)}"
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
