from PIL import Image, ImageOps, ImageFilter
import os

SRC = r"c:/Users/2504/Documents/Claude/Mom site/product_photos"
OUT = r"c:/Users/2504/Documents/Claude/Mom site/site/images"
os.makedirs(OUT, exist_ok=True)

jobs = [
    ("Lavender.jpg", "lavender", 0.685),
    ("Lemongrass.jpg", "lemongrass", 0.72),
    ("Seasalt.jpg", "seasalt", 0.72),
]

for fname, slug, crop_frac in jobs:
    im = Image.open(os.path.join(SRC, fname))
    im = ImageOps.exif_transpose(im)
    w, h = im.size
    # crop off dead empty surface at bottom, keep a little grounding shadow
    new_h = int(h * crop_frac)
    im = im.crop((0, 0, w, new_h))
    # target width for web
    target_w = 1100
    ratio = target_w / im.width
    im = im.resize((target_w, int(im.height * ratio)), Image.LANCZOS)
    im.save(os.path.join(OUT, f"{slug}.jpg"), "JPEG", quality=84, optimize=True)

    # small thumbnail / avif-less fallback
    thumb_w = 640
    ratio2 = thumb_w / im.width
    thumb = im.resize((thumb_w, int(im.height * ratio2)), Image.LANCZOS)
    thumb.save(os.path.join(OUT, f"{slug}-sm.jpg"), "JPEG", quality=80, optimize=True)

    print(slug, "->", im.size)

print("done")
