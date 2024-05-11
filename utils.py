import re
import string
import random
import os

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
