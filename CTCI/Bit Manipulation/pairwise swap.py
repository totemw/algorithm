"""
Swap odd and even bits in an integer with as few instructions as possible
"""


def swapOddEvenBits(x):
    EVEN = 0x5555555555555555
    ODD =  0xAAAAAAAAAAAAAAAA
    return ((x & ODD) >> 1) | ((x & EVEN) << 1)