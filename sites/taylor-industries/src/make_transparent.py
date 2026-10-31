"""Cut the white studio background out of the electrode photos.

Run from the site folder:  python3 src/make_transparent.py
Reads the original JPEGs in site/assets/img/ and writes WebP files with alpha to
src/transparent/<folder>/<name>.webp. build.py copies those into site/ and uses them.

Method: flood-fill the near-white background in from the image border (so white foam,
gel pads and backing inside the outline are kept), also clear enclosed pure-white gaps
(e.g. inside wire loops), then give the 1px outline a soft alpha from its contrast with
the background and un-mix the white from those edge pixels so no halo is left.
"""
from pathlib import Path
import sys
import numpy as np
from PIL import Image
from scipy import ndimage as ndi

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / 'site/assets/img'
OUT = ROOT / 'src/transparent'
FILES = sorted(str(p.relative_to(SRC)) for d in ('ecg', 'tens', 'strip') for p in (SRC / d).glob('*.jpg')) + [
    'misc/tab.jpg', 'misc/custom_electrodes.jpg', 'misc/gp96.jpg']
# Per-image overrides. gp96's coiled lead wire leaves many tiny white gaps, so inside
# key_box the alpha is keyed from colour contrast instead (the wire is dark teal).
TUNE = {'misc/gp96.jpg': dict(key_box=(131, 0, 351, 263), key_ref=150)}
# Photos shot sideways on the original site; turned 90 degrees counterclockwise.
ROTATE_CCW = {f'ecg/{c}_Disposable_ECG_Electrode.jpg' for c in (
    '1000ZT', '1100ZT', '1200ZT', '2000ZT', '2300ZT', '2500ZT', '2600ZT', '3000ZT',
    '4000ZT', '4500ZT', '4500RZT', '4600ZT', '5000ZT')}


def cutout(path, t_lo=10, t_hole=6, min_hole=None, key_box=None, key_ref=150):
    rgb = np.asarray(Image.open(path).convert('RGB')).astype(np.float64)
    h, w, _ = rgb.shape
    border = np.concatenate([rgb[0], rgb[-1], rgb[:, 0], rgb[:, -1]])
    bg = np.median(border, axis=0)
    d = np.abs(rgb - bg).max(axis=2)
    four = ndi.generate_binary_structure(2, 1)
    # 1. background = near-white pixels connected to the border
    lab, _ = ndi.label(d <= t_lo, structure=four)
    edge_ids = np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))
    B = np.isin(lab, edge_ids[edge_ids > 0])
    # 2. enclosed pure-white gaps (inside wire loops, between parts)
    min_hole = min_hole or max(10, h * w // 600)
    lab2, n2 = ndi.label((d <= t_hole) & ~B, structure=four)
    if n2:
        sizes = ndi.sum(np.ones_like(d), lab2, range(1, n2 + 1))
        for i, s in enumerate(sizes, 1):
            if s >= min_hole:
                B |= ndi.binary_dilation(lab2 == i, iterations=1) & (d <= t_lo)
    M = ~B
    # drop JPEG specks
    lab3, n3 = ndi.label(M, structure=np.ones((3, 3)))
    if n3:
        sizes = ndi.sum(np.ones_like(d), lab3, range(1, n3 + 1))
        M &= np.isin(lab3, [i for i, s in enumerate(sizes, 1) if s >= 6])
    # 3. soft edge: alpha from contrast against the background on the 1px rims
    inner = ndi.binary_erosion(M, structure=four, border_value=1)
    ring_in = M & ~inner
    ring_out = ndi.binary_dilation(M, structure=four) & ~M
    ref = ndi.maximum_filter(np.where(inner, d, 0), size=5)
    ref = np.maximum(np.where(ref > 0, ref, 40), 22)
    alpha = np.zeros_like(d)
    alpha[inner] = 1
    alpha[ring_in] = np.clip(d[ring_in] / ref[ring_in], 0.15, 1)
    alpha[ring_out] = np.clip((d[ring_out] - 2) / ref[ring_out], 0, 0.4)
    # light feather across the rim only
    soft = ndi.gaussian_filter(alpha, 0.45)
    band = ring_in | ring_out
    alpha[band] = np.minimum(1, np.maximum(alpha[band] * 0.6 + soft[band] * 0.4, 0))
    # smooth the staircase of the pixel mask: trace it at 4x, blur, threshold, box-downsample
    up = np.asarray(Image.fromarray((M * 255).astype(np.uint8)).resize((w * 4, h * 4), Image.BILINEAR), float) / 255
    up = (ndi.gaussian_filter(up, 1.6) > 0.5).astype(float)
    shape = up.reshape(h, 4, w, 4).mean(axis=(1, 3))
    alpha[band] = np.minimum(alpha[band], 0.5 * alpha[band] + 0.5 * shape[band])
    deep = ndi.binary_erosion(M, structure=four, iterations=2, border_value=1)
    alpha[deep] = 1
    if key_box:
        x0, y0, x1, y1 = key_box
        k = np.zeros_like(M); k[y0:y1, x0:x1] = True
        keyed = np.clip((d - 6) / (key_ref - 6), 0, 1)
        keyed[~ndi.binary_dilation(M, iterations=1)] = 0
        alpha[k] = keyed[k]
    # 4. un-mix the white background from partly transparent pixels
    a = alpha[..., None]
    col = np.where(a > 0.01, (rgb - (1 - a) * bg) / np.maximum(a, 0.01), rgb)
    col = np.clip(col, 0, 255)
    out = np.dstack([col, alpha * 255]).round().astype(np.uint8)
    out[alpha <= 0.01] = 0
    return Image.fromarray(out, 'RGBA')


def main(only=None):
    for rel in FILES:
        if only and rel not in only:
            continue
        im = cutout(SRC / rel, **TUNE.get(rel, {}))
        if rel in ROTATE_CCW:
            im = im.rotate(90, expand=True)
        dst = OUT / Path(rel).with_suffix('.webp')
        dst.parent.mkdir(parents=True, exist_ok=True)
        im.save(dst, 'WEBP', quality=92, alpha_quality=100, method=6, exact=False)
        print(dst.relative_to(ROOT), im.size, dst.stat().st_size)


if __name__ == '__main__':
    main(sys.argv[1:])
