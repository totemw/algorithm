"""
Write a function to swap a number in place
"""


def numSwap(a, b):
    a ^= b
    b ^= a
    a ^= b
    return a, b
