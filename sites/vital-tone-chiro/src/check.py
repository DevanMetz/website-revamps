from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import re
import sys

from bs4 import BeautifulSoup, NavigableString

sys.path.insert(0, str(Path(__file__).resolve().parent))
import data as d

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / 'site'
REFERENCE = ROOT / 'reference'
errors = []

EXTERNAL = {d.FACEBOOK, d.INSTAGRAM, d.CORE_IDENTITY}
SOURCE_PAGES = {'/': 'home', '/services-1/': 'services-1', '/services/': 'services-1', '/about/': 'about',
                '/faq/': 'faq', '/contact/': 'contact', '/privacy-policy/': 'privacy-policy'}
BANNED = ['Upgrade my website', '/keep/', 'stripe.com', 'preview-subscribe', 'squarespace', 'Personal Training']
FORM_TEXT = {label for label, *_ in d.FORM_FIELDS} | {label for label, _ in d.NAME_PARTS} | {d.FORM_SUBMIT}


class Page(HTMLParser):
    def __init__(self, file):
        super().__init__()
        self.file = file
        self.ids = set()
        self.fragments = []
        self.labels = set()
        self.fields = []
        self.aria = []
        self.headings = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if len(a) != len(attrs):
            errors.append(f'{self.file}: duplicate attribute on {tag}')
        if 'id' in a:
            if a['id'] in self.ids:
                errors.append(f'{self.file}: duplicate id {a["id"]}')
            self.ids.add(a['id'])
        if tag == 'label' and 'for' in a:
            self.labels.add(a['for'])
        if tag in ('input', 'textarea'):
            self.fields.append(a.get('id'))
        for key in ('aria-controls', 'aria-labelledby', 'aria-describedby'):
            self.aria.extend(a.get(key, '').split())
        if re.fullmatch('h[1-6]', tag):
            self.headings.append(int(tag[1]))
        if tag == 'img':
            if not all(key in a for key in ('alt', 'width', 'height')):
                errors.append(f'{self.file}: incomplete image {a.get("src")}')
            elif not a['alt'].strip():
                errors.append(f'{self.file}: empty alt {a.get("src")}')
        for key in ('href', 'src'):
            self.check_url(tag, key, a.get(key, ''), a)

    def check_url(self, tag, key, value, attrs):
        parts = urlsplit(value)
        if parts.scheme in ('http', 'https') and tag == 'a' and value not in EXTERNAL and 'google.com/maps' not in value:
            errors.append(f'{self.file}: unexpected external link {value}')
        if parts.scheme in ('http', 'https') and tag != 'a' and not value.startswith(d.SITE_ORIGIN):
            errors.append(f'{self.file}: external resource {value}')
        if value.startswith('/') and not value.startswith('//'):
            target = SITE / unquote(parts.path.lstrip('/'))
            target = target / 'index.html' if parts.path.endswith('/') else target
            if not target.is_file():
                errors.append(f'{self.file}: missing {value}')


def squash(text):
    """Compare text without whitespace, which the source and the layout break differently."""
    return re.sub(r'[\s​-‍﻿\xa0]+', '', text)


def page_path(file):
    relative = file.parent.relative_to(SITE).as_posix()
    return '/' if relative == '.' else f'/{relative}/'


def source_copy():
    copy = {}
    for name in sorted(set(SOURCE_PAGES.values())):
        soup = BeautifulSoup((REFERENCE / 'pages' / f'{name}.html').read_text(encoding='utf8'), 'html.parser')
        for junk in soup(['script', 'style', 'noscript']):
            junk.decompose()
        copy[name] = soup
    return copy


def check_verbatim_copy(built):
    """Every visible string must come from the source page, and all source copy must be present."""
    sources = source_copy()
    for path, soup in built.items():
        source = sources[SOURCE_PAGES[path]]
        source_text = squash(source.get_text(''))
        for region in (soup.find('main'), soup.find('footer')):
            for node in region.find_all(string=True):
                text = node.strip() if isinstance(node, NavigableString) else ''
                if not text or text in FORM_TEXT or text == d.TAGLINE:
                    continue
                if squash(text) not in source_text:
                    errors.append(f'{path}: text not in source: {text[:90]}')
        built_text = squash(soup.find('main').get_text(''))
        main = source.find('main')
        for block in main.select('h1,h2,h3,h4,p,li,.accordion-item__title'):
            if block.find(['p', 'li']):
                continue
            text = block.get_text('').strip().lstrip('•')
            # The homepage marquee repeats its H1 many times; it is built once as the page heading.
            if squash(text).startswith('PersonalizedCare.NaturalHealing.ModernTechnology.Personalized'):
                continue
            if squash(text) and squash(text) not in ('.', '-') and squash(text) not in built_text:
                errors.append(f'{path}: source copy missing: {text[:90]}')


def check_meta(path, soup):
    meta_path = '/services-1/' if path == '/services/' else path
    title, description = d.META[meta_path]
    if soup.title.string != title:
        errors.append(f'{path}: title differs')
    tag = soup.find('meta', attrs={'name': 'description'})
    if (tag['content'] if tag else None) != description:
        errors.append(f'{path}: description differs')
    canonical = soup.find('link', rel='canonical')['href']
    if canonical != d.SITE_ORIGIN + meta_path:
        errors.append(f'{path}: canonical {canonical}')
    if soup.find('meta', attrs={'name': 'robots', 'content': 'noindex'}) is None:
        errors.append(f'{path}: missing preview noindex')


def check_reference_meta():
    content = (REFERENCE / 'CONTENT.md').read_text(encoding='utf8')
    for block in re.findall(r'===== PAGE (\S+) .*?\nTITLE: (.*?)\nMETA description: (.*?)\n', content):
        path = '/' if block[0] == '/' else block[0] + '/'
        description = None if block[2] == 'None' else block[2]
        if d.META.get(path) != (block[1], description):
            errors.append(f'{path}: data.py meta differs from CONTENT.md')


def check_form(path, soup):
    forms = soup.select('form.contact-form')
    if path == '/privacy-policy/':
        if forms:
            errors.append(f'{path}: unexpected form')
        return
    if len(forms) != 1:
        errors.append(f'{path}: expected one form, found {len(forms)}')
        return
    form = forms[0]
    if form.get('action') != f'mailto:{d.EMAIL}':
        errors.append(f'{path}: form must use mailto')
    labels = [label.get_text() for label in form.find_all(['legend', 'label'])]
    expected = []
    for label, kind, *_ in d.FORM_FIELDS:
        expected.append(label)
        if kind == 'name':
            expected.extend(part for part, _ in d.NAME_PARTS)
    if labels != expected:
        errors.append(f'{path}: form labels {labels}')


def main():
    pages = {}
    built = {}
    for file in SITE.rglob('*.html'):
        source = file.read_text()
        page = Page(file)
        page.feed(source)
        pages[file] = page
        if page.headings.count(1) != 1:
            errors.append(f'{file}: {page.headings.count(1)} h1s')
        for before, after in zip(page.headings, page.headings[1:]):
            if after > before + 1:
                errors.append(f'{file}: heading jumps h{before} to h{after}')
        for field in page.fields:
            if not field or field not in page.labels:
                errors.append(f'{file}: unlabeled field {field}')
        for ref in page.labels | set(page.aria):
            if ref not in page.ids:
                errors.append(f'{file}: missing target {ref}')
        for word in BANNED:
            if word.lower() in source.lower():
                errors.append(f'{file}: banned text {word}')
        for structured in re.findall(r'<script type="application/ld\+json">(.*?)</script>', source, re.S):
            json.loads(structured)
        if file.name == 'index.html':
            built[page_path(file)] = BeautifulSoup(source, 'html.parser')

    expected = set(SOURCE_PAGES)
    if set(built) != expected:
        errors.append(f'pages differ: {sorted(set(built) ^ expected)}')
    for path, soup in built.items():
        check_meta(path, soup)
        check_form(path, soup)
        source = str(soup)
        for needle in (f'mailto:{d.EMAIL}', d.TEL, d.FACEBOOK, d.INSTAGRAM, d.CORE_IDENTITY):
            if needle.replace('&', '&amp;') not in source and needle not in source:
                errors.append(f'{path}: missing link {needle}')
    if built['/services/'].find('main').decode() != built['/services-1/'].find('main').decode():
        errors.append('/services/ differs from /services-1/')

    if REFERENCE.exists():
        check_reference_meta()
        check_verbatim_copy(built)
    else:
        print('reference/ not present: skipped verbatim copy checks')

    home = built['/'].decode()
    for path in d.META:
        if path != '/' and f'href="{path}"' not in home:
            errors.append(f'{path}: not linked from home')

    sitemap = (SITE / 'sitemap.xml').read_text()
    if re.findall('<loc>(.*?)</loc>', sitemap) != [d.SITE_ORIGIN + path for path in d.META]:
        errors.append('sitemap paths differ')
    robots = (SITE / 'robots.txt').read_text()
    if 'User-agent: *\nDisallow: /\n' not in robots or f'Sitemap: {d.SITE_ORIGIN}/sitemap.xml' not in robots:
        errors.append('robots.txt incomplete')
    headers = (SITE / '_headers').read_text()
    if 'X-Robots-Tag: noindex' not in headers:
        errors.append('missing preview noindex header')
    for folder, policy in (('css', 'max-age=0, must-revalidate'), ('js', 'max-age=0, must-revalidate'),
                           ('img', 'max-age=31536000, immutable'), ('fonts', 'max-age=31536000, immutable')):
        if f'/assets/{folder}/*\n  Cache-Control: public, {policy}' not in headers:
            errors.append(f'{folder}: cache header')

    css = (SITE / 'assets/css/site.css').read_text()
    js = (SITE / 'assets/js/site.js').read_text()
    if re.search(r'url\(["\']?https?://|@import', css):
        errors.append('external CSS request')
    if len(css.encode()) > 25600 or len(js.encode()) > 6144:
        errors.append('asset size exceeded')
    for image in (SITE / 'assets/img').iterdir():
        if not re.fullmatch(r'[a-z0-9-]+\.(png|webp)', image.name):
            errors.append(f'unclean image name {image.name}')
    for forbidden in ('.github', 'keep.py'):
        if (ROOT / forbidden).exists() or (ROOT / 'src' / forbidden).exists():
            errors.append(f'{forbidden} must not exist')

    images = len(list((SITE / 'assets/img').iterdir()))
    print(f'{len(pages)} HTML pages; {images} images; CSS {len(css.encode())} bytes; JS {len(js.encode())} bytes')
    print('\n'.join(errors) if errors else 'All static checks passed.')
    raise SystemExit(bool(errors))


if __name__ == '__main__':
    main()
