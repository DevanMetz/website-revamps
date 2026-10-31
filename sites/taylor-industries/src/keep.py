# Preview-only "/keep/" page: how to switch to this new site, ending in the Stripe checkout.
# Built from the contact page's header and footer, only while PREVIEW_SUBSCRIBE_URL is set.
import re, shutil
from html import escape as esc
from data import STRIPE_PORTAL_URL
SITE_CFG = {"name": "Taylor Industries Inc.", "domain": "taylor-ind.com", "accent": "var(--navy)", "ink": "var(--ink)", "line": "var(--line)", "surface": "var(--tray)", "radius": "3px", "container": "wrap", "slug": "taylor-industries"}
KEEP_CODE_URL = 'https://github.com/DevanMetz/website-revamps/tree/main/sites/' + SITE_CFG['slug']
I = lambda d: '<svg class="keep-ico" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'+d+'</svg>'
ICONS = {
 'code': I('<path d="m8 8-4 4 4 4M16 8l4 4-4 4M13.5 5l-3 14"/>'),
 'care': I('<path d="M12 3 5 6v5c0 4.4 3 8.3 7 10 4-1.7 7-5.6 7-10V6z"/><path d="m9 12 2 2 4-4"/>'),
 'card': I('<rect x="3" y="5.5" width="18" height="13" rx="2"/><path d="M3 10h18M7 15h4"/>'),
 'dns': I('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3z"/>'),
 'off': I('<circle cx="12" cy="12" r="9"/><path d="m9 9 6 6M15 9l-6 6"/>'),
 'live': I('<circle cx="12" cy="12" r="9"/><path d="m8 12.5 2.7 2.7L16.5 9.5"/>'),
}
def _css(c):
 a,ink,line,surf=c['accent'],c['ink'],c['line'],c['surface']
 return ('.keep{padding:clamp(20px,3.2vh,40px) 0 clamp(24px,4vh,48px)}'
  '.keep h1{font-size:clamp(2.2rem,4vw,3rem);margin:0 0 6px;max-width:none}'
  '.keep h2{font-size:clamp(1.25rem,1.8vw,1.5rem);margin:0;line-height:1.15;max-width:none}'
  '.keep h3{font-size:1.05rem;margin:0;line-height:1.25}'
  '.keep p{margin:0}'
  '.keep-lede{font-size:1.1rem;max-width:40em}'
  '.keep-ico{display:block;width:24px;height:24px;color:'+a+';flex:none}'
  '.keep-head{display:flex;align-items:center;gap:10px}'
  '.keep-choices{display:grid;gap:16px;margin:clamp(18px,3vh,28px) 0 0;padding:0;list-style:none}'
  '.keep-choice{position:relative;display:flex;flex-direction:column;gap:8px;padding:20px 22px;border:1px solid '+line+';background:#fff;color:'+ink+';border-radius:'+c['radius']+'}'
  '.keep-choice.is-rec{border:2px solid '+a+';box-shadow:0 10px 28px rgba(0,0,0,.08)}'
  '.keep-price{font-size:1.05rem;font-weight:700}'
  '.keep-tag{position:absolute;top:-12px;left:20px;padding:2px 10px;background:'+a+';color:#fff;font-size:.75rem;font-weight:700;letter-spacing:.04em;text-transform:uppercase;border-radius:'+c['radius']+'}'
  '.keep-choice>a{margin-top:auto;align-self:flex-start}'
  '.keep-choice>a:not(.button){color:'+a+';font-weight:700;text-underline-offset:3px;display:inline-flex;align-items:center;min-height:44px}'
  '.keep-choice .button{min-height:46px;padding-inline:22px}'
  '.keep-how{margin-top:clamp(22px,3.6vh,36px)}'
  '.keep-steps{display:grid;gap:14px;margin:12px 0 0;padding:0;list-style:none}'
  '.keep-step{display:flex;flex-direction:column;gap:8px;padding:16px 18px;border:1px solid '+line+';background:#fff;color:'+ink+';border-radius:'+c['radius']+'}'
  '.keep-step p{font-size:.9rem;line-height:1.45}'
  '.keep-num{display:inline-flex;align-items:center;justify-content:center;width:30px;height:30px;border-radius:50%;background:'+a+';color:#fff;font-weight:700;font-size:.95rem;flex:none}'
  '.keep-foot{margin-top:clamp(18px,3vh,28px);display:flex;flex-wrap:wrap;align-items:center;gap:16px 40px}'
  '.keep-foot .button{min-height:52px;padding-inline:28px;font-size:1.05rem;max-width:100%;text-align:center}'
  '.keep-faq{display:flex;flex-wrap:wrap;gap:12px 40px}'
  '.keep-faq h3{margin:0 0 2px;font-size:1rem}'
  '.keep-faq p{font-size:.95rem}'
  '.keep a:focus-visible{outline:3px solid '+a+';outline-offset:3px}'
  '@media (min-width:720px){.keep-choices{grid-template-columns:1fr 1fr}.keep-steps{grid-template-columns:1fr 1fr}}'
  '@media (min-width:1000px){.keep-steps{grid-template-columns:repeat(4,1fr)}}')
def build_keep(site_dir, url):
 out=site_dir/'keep'
 if not url:
  if out.exists(): shutil.rmtree(out)
  return
 c=SITE_CFG; name=esc(c['name']); dom=esc(c['domain'])
 html=(site_dir/'contact'/'index.html').read_text()
 html=re.sub(r'<!-- preview-subscribe -->.*?<!-- /preview-subscribe -->','',html,flags=re.S)
 html=re.sub(r'<script type="application/ld\+json">.*?</script>','',html,flags=re.S)
 html=re.sub(r'<meta property="og:url"[^>]*>','',html)
 html=re.sub(r'<link rel="canonical"[^>]*>','',html)
 title='Upgrade your website | '+name
 desc='How to keep the new '+name+' website.'
 html=re.sub(r'<title>.*?</title>','<title>'+title+'</title>',html,count=1,flags=re.S)
 html=re.sub(r'<meta property="og:title" content="[^"]*">','<meta property="og:title" content="'+title+'">',html)
 html=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="'+desc+'">',html)
 html=re.sub(r'<meta property="og:description" content="[^"]*">','<meta property="og:description" content="'+desc+'">',html)
 if '<meta name="robots" content="noindex">' not in html: html=html.replace('<meta charset="utf-8">','<meta charset="utf-8"><meta name="robots" content="noindex">',1)
 html=re.sub(r'\s*aria-current="page"','',html)
 html=html.replace('</head>','<!-- keep-funnel --><style>'+_css(c)+'</style><!-- /keep-funnel --></head>',1)
 W=c['container']
 main=('<main id="main"><section class="keep" aria-labelledby="keep-title"><div class="'+W+' keep-in">'
  '<h1 id="keep-title">Upgrade your website</h1>'
  '<p class="keep-lede">Two ways to keep the new '+name+' website.</p>'
  '<ul class="keep-choices">'
  '<li class="keep-choice"><div class="keep-head">'+ICONS['code']+'<h2>Do it yourself</h2></div><p class="keep-price">Free</p>'
  '<p>Take the full source code for free, then set it up and manage it yourself.</p>'
  '<a href="'+esc(KEEP_CODE_URL)+'" target="_blank" rel="noopener" aria-label="Get the code (opens in a new tab)">Get the code</a></li>'
  '<li class="keep-choice is-rec"><span class="keep-tag">Recommended</span><div class="keep-head">'+ICONS['care']+'<h2>I’ll take care of everything</h2></div><p class="keep-price">$20/month</p>'
  '<p>Hosting, management, and any changes you ask for, free. Cancel anytime.</p>'
  '<a class="button" href="'+esc(url)+'">Continue to checkout · $20/mo</a></li>'
  '</ul>'
  '<section class="keep-how" id="keep-how" aria-labelledby="keep-how-title"><h2 id="keep-how-title">Switching takes 4 steps</h2>'
  '<ol class="keep-steps">'
  '<li class="keep-step"><div class="keep-head"><span class="keep-num" aria-hidden="true">1</span><h3>Subscribe</h3></div><p>Checkout takes about a minute.</p></li>'
  '<li class="keep-step"><div class="keep-head"><span class="keep-num" aria-hidden="true">2</span><h3>Add one record</h3></div><p>Devan emails you a single DNS record (a CNAME for www) to paste in wherever your domain is registered, such as GoDaddy or Network Solutions. Your email keeps working, because nothing else changes.</p></li>'
  '<li class="keep-step"><div class="keep-head"><span class="keep-num" aria-hidden="true">3</span><h3>You’re live</h3></div><p>www.'+dom+' shows the new site with HTTPS within about a day. Devan handles everything after that. To request a change, just email Devan.</p></li>'
  '<li class="keep-step"><div class="keep-head"><span class="keep-num" aria-hidden="true">4</span><h3>Cancel your old hosting</h3></div><p>Once the new site shows on your domain, cancel your old web host or site builder plan. Keep your domain registration and email service active. Devan can help if you’re not sure which is which.</p></li>'
  '</ol>'
  '</section>'
  '<div class="keep-foot"><a class="button" href="'+esc(url)+'">Continue to checkout · $20/mo</a>'
  '<section class="keep-faq" aria-label="Questions">'
  '<div><h3>Will my email break?</h3><p>No. We only point www at the new site.</p></div>'
  '<div><h3>Can I cancel?</h3><p>Yes, anytime. <a href="'+esc(STRIPE_PORTAL_URL)+'" target="_blank" rel="noopener" aria-label="Manage or cancel your subscription (opens in a new tab)">Manage or cancel your subscription here</a>.</p></div>'
  '</section></div>'
  '</div></section></main>')
 html=re.sub(r'<main id="main">.*</main>',lambda m:main,html,count=1,flags=re.S)
 out.mkdir(exist_ok=True); (out/'index.html').write_text(html)
