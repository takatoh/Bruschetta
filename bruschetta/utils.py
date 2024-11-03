import re
import string
import random
import os
from PIL import Image

PICTURES_EXTS = [".png", ".jpg", ".jpeg"]


def str_to_bool(s):
    p = re.compile(r"(true|yes|on)\Z", re.IGNORECASE)
    if p.match(s):
        return True
    else:
        return False


def mk_filename():
    filename = randstring(12) + ".jpg"
    return filename


def randstring(n):
    pool = string.ascii_lowercase + string.digits
    random.seed()
    s = "".join(random.choices(pool, k=n))
    return s


def is_picture(filename):
    base, ext = os.path.splitext(filename)
    return ext.lower() in PICTURES_EXTS


def save_coverart(tmp_filename, coverart_dir):
    coverart_filename = mk_filename()
    while os.path.isfile(os.path.join(coverart_dir, coverart_filename)):
        coverart_filename = mk_filename()
    img = Image.open(tmp_filename)
    img.thumbnail((300, 300))
    img = img.convert("RGB")
    img.save(os.path.join(coverart_dir, coverart_filename))
    return coverart_filename
