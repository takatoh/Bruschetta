import re
import string
import random


def str_to_bool(s):
    p = re.compile(r'(true|yes|on)\Z', re.IGNORECASE)
    if p.match(s):
        return True
    else:
        return False


def mk_filename():
    filename = randstring(12) + '.jpg'
    return filename


def randstring(n):
    pool = string.ascii_lowercase + string.digits
    s = ''
    random.seed()
    for x in range(n):
        s = s + pool[random.randrange(len(pool))]
    return s
