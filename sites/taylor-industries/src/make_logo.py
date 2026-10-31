"""Header logo with the "A Family Owned & Operated Company" tagline.

The only original artwork (img-originals/logo/original.jpg, 325x51) has the
tagline at ~7px tall, too small to upscale cleanly, so the tagline is
re-set in a Times-style italic (Nimbus Roman Italic), grey and right-aligned
under the wordmark as in the original, but spanning the full wordmark width
(original: ~72%) so it stays legible at header sizes. It sits on the existing
cleaned mark brand/logo-full.png.
Run from the site folder: python3 src/make_logo.py
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

S = Path('site/assets/img/brand')
FONT = '/usr/share/fonts/opentype/urw-base35/NimbusRoman-Italic.otf'
TEXT = 'A Family Owned & Operated Company'
COLOR = (77, 77, 77)
SS = 4  # supersample

mark = Image.open(S / 'logo-full.png').convert('RGBA')  # 600x78, wordmark x100-599, rows 2-55
W = mark.width
text_l, text_r = 100, 599
span = text_r - text_l - 4
font_size = 10
while True:
    f = ImageFont.truetype(FONT, font_size * SS)
    if f.getlength(TEXT) / SS > span:
        break
    font_size += 0.5
font_size -= 0.5
f = ImageFont.truetype(FONT, round(font_size * SS))
l, t, r, b = f.getbbox(TEXT)
top = 61  # cap top, a small gap under the wordmark's descenders (as in original)
H = top + (b - t) // SS + 3
big = Image.new('L', (W * SS, H * SS), 0)
d = ImageDraw.Draw(big)
x = (text_r + 1) * SS - r
d.text((x, top * SS - t), TEXT, fill=255, font=f)
a = big.resize((W, H), Image.LANCZOS)
tag = Image.new('RGBA', (W, H), COLOR + (0,))
tag.putalpha(a)
out = Image.new('RGBA', (W, H), (0, 0, 0, 0))
out.alpha_composite(mark, (0, 0))
out.alpha_composite(tag)
bbox = out.getbbox()
out = out.crop((0, 0, W, bbox[3] + 1))
out.save(S / 'logo-tagline.png', optimize=True)
print('font', font_size, 'size', out.size)
