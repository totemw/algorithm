"""
Determine the number of bits you would need to flip to
convert integer A to integer B
"""


# XOR
def bitSwapRequired(a, b):
    count = 0
    c = a ^ b
    while c != 0:
        count += 1
        c = c & (c - 1)
    return count
