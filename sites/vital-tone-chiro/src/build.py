from pathlib import Path
from urllib.parse import quote_plus
import html
import json
import re
import shutil

from PIL import Image

import data as d

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / 'src'
SITE = ROOT / 'site'
IMG = SITE / 'assets/img'

PHOTO_WIDTHS = (640, 1280)
LOGOS = {'logo': 640, 'logo-clay': 480, 'logo-vertical': 560}
ADDRESS_QUERY = f'{d.STREET} {d.SUITE}, {d.CITY_LINE}'
MAPS_URL = 'https://www.google.com/maps/search/?api=1&query=' + quote_plus(ADDRESS_QUERY)

esc = lambda text: html.escape(text, quote=False)
attr = lambda text: html.escape(text, quote=True)


def rich(text):
    return re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', esc(text))


def paras(lines):
    return ''.join(f'<p>{rich(line)}</p>' for line in lines)


def bullets(items):
    return '<ul class="ticks">' + ''.join(f'<li>{rich(item)}</li>' for item in items) + '</ul>'


def reset_site():
    if SITE.exists():
        shutil.rmtree(SITE)
    for folder in ('css', 'js', 'img', 'fonts'):
        (SITE / 'assets' / folder).mkdir(parents=True)
    shutil.copyfile(SRC / 'assets/css/site.css', SITE / 'assets/css/site.css')
    shutil.copyfile(SRC / 'assets/js/site.js', SITE / 'assets/js/site.js')
    for font in (SRC / 'fonts').glob('*.woff2'):
        shutil.copyfile(font, SITE / 'assets/fonts' / font.name)
    for name in ('favicon.png', 'logo-og.png'):
        shutil.copyfile(SRC / 'assets/img' / name, IMG / name)


def logo_img(name, alt):
    image = Image.open(SRC / 'assets/img' / f'{name}.png')
    width = LOGOS[name]
    size = (width, round(image.height * width / image.width))
    out = IMG / f'{name}.png'
    if not out.exists():
        image.resize(size, Image.LANCZOS).save(out, optimize=True)
    return f'<img src="/assets/img/{name}.png" alt="{attr(alt)}" width="{size[0]}" height="{size[1]}">'


def photo(name, alt, sizes='(max-width: 900px) 100vw, 50vw', priority=False):
    image = Image.open(SRC / 'assets/img' / f'{name}.jpg')
    candidates = []
    for width in PHOTO_WIDTHS:
        if width > image.width:
            continue
        out = IMG / f'{name}-{width}.webp'
        if not out.exists():
            size = (width, round(image.height * width / image.width))
            image.resize(size, Image.LANCZOS).save(out, format='WEBP', quality=80, method=6)
        candidates.append((width, out.name))
    largest_width, largest = candidates[-1]
    height = round(image.height * largest_width / image.width)
    srcset = ', '.join(f'/assets/img/{file} {width}w' for width, file in candidates)
    loading = 'loading="eager" fetchpriority="high"' if priority else 'loading="lazy"'
    return f'<img src="/assets/img/{largest}" srcset="{srcset}" sizes="{sizes}" alt="{attr(alt)}" width="{largest_width}" height="{height}" {loading} decoding="async">'


def cta(label=d.CTA, style=''):
    classes = f'button {style}'.strip()
    return f'<a class="{classes}" href="/contact/">{esc(label)}</a>'


def contact_links():
    return (f'<p><a href="mailto:{d.EMAIL}">{d.EMAIL}</a><br>'
            f'<a href="{d.TEL}">{d.PHONE}</a></p>')


def hours_list():
    rows = ''.join(f'<div><dt>{day}</dt><dd>{"<br>".join(shown)}</dd></div>' for day, shown, _ in d.HOURS)
    return f'<dl class="hours">{rows}</dl>'


def form():
    fields = ''
    for label, kind, required, autocomplete in d.FORM_FIELDS:
        field_id = 'field-' + re.sub('[^a-z0-9]+', '-', label.lower()).strip('-')
        flag = ' required' if required else ''
        complete = f' autocomplete="{autocomplete}"' if autocomplete else ''
        name = attr(label)
        if kind == 'name':
            parts = ''.join(f'<div class="field"><label for="{field_id}-{part}">{esc(part_label)}</label>'
                            f'<input id="{field_id}-{part}" name="{attr(part_label)}" type="text"{flag} autocomplete="{part}"></div>'
                            for part_label, part in d.NAME_PARTS)
            fields += f'<fieldset class="name-fields"><legend>{esc(label)}</legend>{parts}</fieldset>'
            continue
        if kind == 'textarea':
            control = f'<textarea id="{field_id}" name="{name}" rows="5"{flag}></textarea>'
        else:
            control = f'<input id="{field_id}" name="{name}" type="{kind}"{flag}{complete}>'
        fields += f'<div class="field"><label for="{field_id}">{esc(label)}</label>{control}</div>'
    return (f'<form class="contact-form" action="mailto:{d.EMAIL}" method="post" enctype="text/plain">{fields}'
            f'<button class="button" type="submit">{d.FORM_SUBMIT}</button><p class="status" role="status"></p></form>')


def form_section(heading, text, image=None):
    picture = f'<div class="form-photo">{image}</div>' if image else ''
    intro = ''.join(f'<p>{rich(line)}</p>' for line in text)
    return (f'<section class="section form-section"><div class="wrap form-grid"><div class="form-intro">'
            f'<h2>{heading}</h2>{intro}{picture}</div><div class="form-card">{form()}</div></div></section>')


def banner(heading):
    return f'<section class="pagehead"><div class="wrap"><h1>{esc(heading)}</h1></div></section>'


def structured_data():
    hours = [{'@type': 'OpeningHoursSpecification', 'dayOfWeek': day, 'opens': opens, 'closes': closes}
             for day, _, spans in d.HOURS for opens, closes in spans]
    return {
        '@context': 'https://schema.org',
        '@type': 'Chiropractor',
        'name': d.NAME,
        'url': d.SITE_ORIGIN + '/',
        'logo': d.SITE_ORIGIN + '/assets/img/logo-og.png',
        'image': d.SITE_ORIGIN + '/assets/img/logo-og.png',
        'telephone': d.PHONE,
        'email': d.EMAIL,
        'address': {
            '@type': 'PostalAddress',
            'streetAddress': f'{d.STREET} {d.SUITE}',
            'addressLocality': 'Germantown',
            'addressRegion': 'WI',
            'postalCode': '53022',
        },
        'openingHoursSpecification': hours,
        'sameAs': [d.FACEBOOK, d.INSTAGRAM],
    }


FACEBOOK_ICON = '<svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path fill="currentColor" d="M13.5 21v-7.5h2.6l.4-3h-3V8.6c0-.9.3-1.5 1.5-1.5h1.6V4.4c-.3 0-1.2-.1-2.3-.1-2.3 0-3.8 1.4-3.8 3.9v2.3H8v3h2.5V21h3Z"/></svg>'
INSTAGRAM_ICON = '<svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.8" d="M7.5 3h9A4.5 4.5 0 0 1 21 7.5v9a4.5 4.5 0 0 1-4.5 4.5h-9A4.5 4.5 0 0 1 3 16.5v-9A4.5 4.5 0 0 1 7.5 3Z"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="17.3" cy="6.7" r="1.2" fill="currentColor"/></svg>'


def footer():
    return f'''<footer><div class="wrap footer-grid">
<div class="footer-brand"><a class="brand" href="/" aria-label="{d.NAME} home">{logo_img('logo-clay', d.NAME)}</a><p class="tagline">{d.TAGLINE}</p>
<ul class="social"><li><a href="{d.FACEBOOK}" aria-label="Facebook" rel="noopener">{FACEBOOK_ICON}</a></li><li><a href="{d.INSTAGRAM}" aria-label="Instagram" rel="noopener">{INSTAGRAM_ICON}</a></li></ul></div>
<div><h2>Office Hours:</h2>{hours_list()}</div>
<div><h2>Contact:</h2>{contact_links()}<h2>Address:</h2><address><a href="{attr(MAPS_URL)}" rel="noopener">{d.NAME}<br>{d.STREET} {d.SUITE}<br>{d.CITY_LINE}</a></address></div>
</div><div class="wrap footer-legal"><a href="/privacy-policy/">PRIVACY POLICY</a><p><a href="{d.CORE_IDENTITY}" rel="noopener">Core Identity</a> - All Rights Reserved 2026</p></div></footer>'''


def layout(path, title, description, body, canonical_path=None):
    current_paths = {'/services/': '/services-1/'}
    current = current_paths.get(path, path)
    links = ''.join(f'<li><a href="{url}"' + (' aria-current="page"' if url == current else '') + f'>{label}</a></li>'
                    for label, url in d.NAV)
    cta_current = ' aria-current="page"' if current == '/contact/' else ''
    canonical = d.SITE_ORIGIN + (canonical_path or path)
    meta = f'<meta name="description" content="{attr(description)}"><meta property="og:description" content="{attr(description)}">' if description else ''
    head = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>{esc(title)}</title>{meta}<link rel="canonical" href="{canonical}"><meta property="og:title" content="{attr(title)}"><meta property="og:type" content="website"><meta property="og:url" content="{canonical}"><meta property="og:image" content="{d.SITE_ORIGIN}/assets/img/logo-og.png"><link rel="icon" href="/assets/img/favicon.png" type="image/png"><link rel="preload" href="/assets/fonts/instrument-serif-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="/assets/fonts/almarai-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin><link rel="stylesheet" href="/assets/css/site.css"><script type="application/ld+json">{json.dumps(structured_data(), ensure_ascii=False)}</script><script src="/assets/js/site.js" defer></script></head>'''
    header = f'''<body><a class="skip" href="#main">Skip to content</a><header><div class="wrap header-bar"><a class="brand" href="/" aria-label="{d.NAME} home">{logo_img('logo', d.NAME)}</a><button class="menu" type="button" aria-expanded="false" aria-controls="nav">Menu</button><nav id="nav" aria-label="Main navigation"><ul>{links}<li class="nav-cta"><a class="button" href="/contact/"{cta_current}>{d.CTA}</a></li></ul></nav></div></header>'''
    return f'{head}{header}<main id="main">{body}</main>{footer()}</body></html>'


def write(path, body, canonical_path=None, meta_path=None):
    title, description = d.META[meta_path or path]
    target = SITE / path.strip('/') / 'index.html' if path != '/' else SITE / 'index.html'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(layout(path, title, description, body, canonical_path))


def home_page():
    c = d.HOME
    pillars = ' '.join(f'<span>{name} <i class="dot">.</i></span>' for name in c['pillars'])
    items = ''.join(f'<article class="pillar"><h3>{esc(title)}</h3><p>{esc(text)}</p></article>' for title, text in c['approach_items'])
    return f'''<section class="hero"><div class="wrap hero-grid"><div class="hero-copy"><p class="eyebrow">{c['eyebrow']}</p><h1 class="pillars">{pillars}</h1>{cta()}</div>
<div class="mosaic"><div class="tile tile-fern">{photo('hero-fern', 'Black and white photograph of a fern leaf', '(max-width: 900px) 50vw, 25vw', True)}</div><div class="tile tile-logo">{logo_img('logo-vertical', d.NAME)}</div><div class="tile tile-waves">{photo('hero-ocean-waves', 'Black and white overhead photograph of ocean waves', '(max-width: 900px) 50vw, 25vw')}</div></div></div></section>
<section class="section"><div class="wrap split"><div class="split-photo">{photo('adjustment-room', 'Vital Tone Chiropractic adjustment room with a nervous system poster and wooden bench')}</div><div><h2>{c['approach_heading']}</h2><p class="lead">{esc(c['approach_lead'])}</p><div class="pillar-list">{items}</div>{cta()}</div></div></section>
<section class="band band-photo">{photo('office', 'Vital Tone Chiropractic office with an adjusting table', '100vw')}<div class="wrap band-copy"><h2>{c['band'][0]}<br>{c['band'][1]}</h2>{cta(style='light')}</div></section>
{form_section(c['form_heading'], c['form_text'])}'''


def services_page():
    c = d.SERVICES
    audiences = ''.join(f'<article class="card"><h3>{esc(title)}</h3><p>{esc(text)}</p></article>' for title, text in c['audiences'])
    process = ''
    for title, before, items, after in c['process']:
        process += f'<article class="card"><h3>{esc(title)}</h3>{paras(before)}{bullets(items)}{paras(after)}</article>'
    steps = ''.join(f'<li class="step"><h3>{esc(title)}</h3><p class="step-lead">{esc(lead)}</p><p>{esc(text)}</p></li>' for title, lead, text in c['first_visit_steps'])
    return f'''<section class="pagehero">{photo('office', 'Vital Tone Chiropractic office with an adjusting table', '100vw', True)}<div class="wrap pagehero-copy"><h1>{c['heading']}</h1>{cta(style='light')}</div></section>
<section class="section"><div class="wrap split split-text-first"><div><h2>{c['neuro_heading']}</h2>{paras(c['neuro_text'])}</div><div class="split-photo landscape">{photo('spine-model', 'Spine and brain models on a wooden desk')}</div></div><div class="wrap cards four">{audiences}</div><div class="wrap center">{cta()}</div></section>
<section class="section tint"><div class="wrap split"><div class="split-photo landscape">{photo('office', 'Vital Tone Chiropractic office with an adjusting table')}</div><div><h2>{c['different_heading'][0]}<br>{c['different_heading'][1]}</h2><h3 class="sub">{c['different_sub'][0]}<br>{c['different_sub'][1]}</h3>{paras(c['different_text'])}{cta()}</div></div></section>
<section class="section"><div class="wrap"><h2 class="center-heading">{c['process_heading']}</h2><div class="cards two">{process}</div><div class="center">{cta()}</div></div></section>
<section class="band band-plain"><div class="wrap band-copy"><h2>{esc(c['welcome'])}</h2></div></section>
<section class="section"><div class="wrap"><div class="split split-text-first first-visit"><div><h2>{c['first_visit_heading']}</h2><p class="lead">{esc(c['first_visit_lead'])}</p></div><div class="split-photo landscape">{photo('office', 'Vital Tone Chiropractic office with an adjusting table')}</div></div><ol class="steps">{steps}</ol><div class="center">{cta(c['first_visit_cta'])}</div></div></section>
{form_section(c['form_heading'], c['form_text'], photo('lets-connect', 'Desk with a notebook reading Let’s connect, a spine model and a brain model', '(max-width: 900px) 100vw, 40vw'))}'''


def about_page():
    c = d.ABOUT
    doctors = ''
    for index, (heading, image, alt, text) in enumerate(c['doctors']):
        priority = index == 0
        doctors += f'<article class="doctor"><div class="doctor-photo">{photo(image, alt, "(max-width: 900px) 100vw, 40vw", priority)}</div><div><h2>{heading}</h2>{paras(text)}</div></article>'
    return f'''{banner(c['heading'])}
<section class="section doctors"><div class="wrap">{doctors}</div></section>
<section class="section tint"><div class="wrap two-up"><div><h2>{c['philosophy_heading']}</h2><p class="lead">{c['philosophy_lead']}</p>{paras(c['philosophy_text'])}</div><div><h2>{c['mission_heading']}</h2>{paras(c['mission_text'])}</div></div></section>
<section class="section"><div class="wrap two-up"><div><h2>{c['stages_heading']}</h2><p class="lead">{c['stages_lead']}</p>{paras(c['stages_text'])}</div><div><h2>{c['gentle_heading']}</h2><p class="lead">{rich(c['gentle_lead'])}</p>{paras(c['gentle_text'])}</div></div></section>
<section class="band band-plain"><div class="wrap band-copy"><h2>{c['band']}</h2>{cta(style='light')}</div></section>
{form_section(c['form_heading'], c['form_text'], photo('lets-connect', 'Desk with a notebook reading Let’s connect, a spine model and a brain model', '(max-width: 900px) 100vw, 40vw'))}'''


def faq_page():
    c = d.FAQ
    items = ''.join(f'<details><summary>{esc(question)}</summary><p>{esc(answer)}</p></details>' for question, answer in c['items'])
    return f'''{banner(c['heading'])}
<section class="section"><div class="wrap faq">{items}</div></section>
{form_section(c['form_heading'], c['form_text'])}'''


def contact_page():
    c = d.CONTACT
    return f'''{banner(c['heading'])}
<section class="section contact-top"><div class="wrap split"><div class="split-photo landscape">{photo('consultation', 'Patient reviewing a clipboard with a staff member at a front desk', priority=True)}</div><div class="office"><h2>{c['office_heading']}</h2><div class="office-grid"><div><h3>{c['contact_label']}</h3>{contact_links()}<h3>{c['location_label']}</h3><address><a href="{attr(MAPS_URL)}" rel="noopener">{d.NAME}<br>{d.STREET}<br>{d.SUITE}<br>{d.CITY_LINE}</a></address></div><div><h3>{c['hours_label']}</h3>{hours_list()}</div></div></div></div></section>
<section class="section form-section"><div class="wrap contact-form-wrap"><div class="form-card">{form()}</div></div></section>'''


def privacy_page():
    c = d.PRIVACY
    sections = ''
    for heading, items in c['sections']:
        rows = ''.join(f'<li><strong>{esc(label)}</strong> {esc(text)}</li>' for label, text in items)
        sections += f'<h2>{esc(heading)}</h2><ul class="ticks">{rows}</ul>'
    return f'''<section class="pagehead"><div class="wrap"><h1>{c['heading']}</h1><p>{c['effective']}</p></div></section>
<section class="section"><div class="wrap prose"><p>{c['intro']}</p>{sections}<h2>{c['contact_heading']}</h2><p>{d.NAME}<br>Email: <a href="mailto:{d.EMAIL}">{d.EMAIL}</a><br>Phone: <a href="{d.TEL}">{c['phone_display']}</a></p><h2>{esc(c['sms_heading'])}</h2>{paras(c['sms_intro'])}{bullets(c['sms_items'])}<h2>{c['consent_heading']}</h2><ul class="ticks"><li>{c['consent']}</li></ul></div></section>'''


def not_found_page():
    body = f'{banner("Page not found")}<section class="section"><div class="wrap center">{cta("Home").replace("/contact/", "/")}</div></section>'
    (SITE / '404.html').write_text(layout('/404.html', 'Page not found — Vital Tone Chiropractic', None, body, '/'))


def write_support_files():
    urls = ''.join(f'<url><loc>{d.SITE_ORIGIN}{path}</loc></url>' for path in d.META)
    (SITE / 'sitemap.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
    (SITE / 'robots.txt').write_text(f'User-agent: *\nDisallow: /\nSitemap: {d.SITE_ORIGIN}/sitemap.xml\n')
    (SITE / '_headers').write_text('/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  X-Frame-Options: DENY\n  X-Robots-Tag: noindex\n\n/assets/css/*\n  Cache-Control: public, max-age=0, must-revalidate\n\n/assets/js/*\n  Cache-Control: public, max-age=0, must-revalidate\n\n/assets/img/*\n  Cache-Control: public, max-age=31536000, immutable\n\n/assets/fonts/*\n  Cache-Control: public, max-age=31536000, immutable\n')


def main():
    reset_site()
    write('/', home_page())
    services = services_page()
    write('/services-1/', services)
    # /services/ replaces the orphan Squarespace shop with the same content as /services-1/.
    write('/services/', services, canonical_path='/services-1/', meta_path='/services-1/')
    write('/about/', about_page())
    write('/faq/', faq_page())
    write('/contact/', contact_page())
    write('/privacy-policy/', privacy_page())
    not_found_page()
    write_support_files()


if __name__ == '__main__':
    main()
