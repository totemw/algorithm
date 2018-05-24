"""
use + / << >> to multiply two numbers
"""


def Product(smaller, bigger):
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger
    s = smaller >> 1
    half = Product(s, bigger)
    if smaller % 2:
        return half + half + bigger
    else:
        return half + half

