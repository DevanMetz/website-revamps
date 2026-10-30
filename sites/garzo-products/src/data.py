from pathlib import Path
import re
text=Path('src/assets/crawl-page-text.txt').read_text()
def source(path):
    blocks=text.split('====================================================================================================')
    for b in blocks:
        if re.search(r'URL: https://garzoproducts.com/'+re.escape(path)+r'\s', b):
            s=b.split('October 29, 2026',1)[-1].split('Home | Products | Product Registration | Contact Us')[0]
            lines=[re.sub(r'\s+', ' ',x).strip() for x in s.splitlines()]
            return [x for x in lines if x and x not in ('Quality at every level.','Image Soon','Coming Soon!')]
    return []
products=[('Oil level regulator 101','/products/oil-level-regulators/101/','101b.jpg'),('Oil level regulator 108','/products/oil-level-regulators/108/','108b.jpg'),('Low flow meters','/products/low-flow-meters/','300b.jpg'),('Lubricator box controls','/products/lubricator-box-controls/211/','211sm.jpg'),('Linear diaphragm operators','/products/linear-diaphragm-operators/','501gp.jpg')]

# Preview-only "Keep this site · $20/mo" button (Stripe Payment Link). Set to '' to remove it from every page.
PREVIEW_SUBSCRIBE_URL = 'https://buy.stripe.com/28EcN70ECbLVgYA9Vw4c808'
STRIPE_PORTAL_URL = 'https://billing.stripe.com/p/login/5kQ8wR5YW17hgYAaZA4c800'
