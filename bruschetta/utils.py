# eoding: utf-8

import re


def str_to_bool(s):
    p = re.compile(r'(true|yes|on)\Z', re.IGNORECASE)
    if p.match(s):
        return True
    else:
        return False
